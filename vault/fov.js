// fov.js: a file sealed on the client's device to the desk's upload key, so only the desk can open it. The same file byte
// for byte on the desk (mc/live/fov.js) and on the client's page (site/vault/fov.js); tools/mc_check/intake.js checks it.
//
// The desk keeps one key pair (P-256) in Google Drive, made the first time it asks for documents; the public half rides in
// every upload link. For each file the page makes a new key pair, agrees a secret with the desk's public key (ECDH), and
// derives two AES-256-GCM keys from it (HKDF-SHA-256): one for a short note of what the file is, one for the file. The
// upload bucket, Google, the desk's app and anyone holding the link see only this:
//
//   "FOV1" | the desk key's id (8 bytes) | the page's one-time public key (65) | the note's length (4) |
//   the note's nonce (12) | the sealed note | the file's nonce (12) | the sealed file
//
// Everything before the note's length is bound into both seals, so no part can be swapped. The desk reads the note from
// the first few KB alone, and the file only when it files it. WebCrypto only: a browser, Node or Deno.

const te = new TextEncoder();
const td = new TextDecoder();
const subtle = globalThis.crypto.subtle;
const MAGIC = te.encode('FOV1');
const HEAD = 77;   /* magic 4, key id 8, one-time public key 65 */
/** The longest note: the desk reads this much and the head to know what a file is. */
export const NOTE_MAX = 4096;
export const READ_FIRST = HEAD + 4 + 12 + NOTE_MAX;

const cat = (...parts) => { const out = new Uint8Array(parts.reduce((t, p) => t + p.length, 0)); let i = 0; for (const p of parts) { out.set(p, i); i += p.length; } return out; };
const hex = (b) => [...b].map((x) => x.toString(16).padStart(2, '0')).join('');
const rand = (n) => globalThis.crypto.getRandomValues(new Uint8Array(n));
export const b64u = (b) => { let s = ''; for (const x of b) s += String.fromCharCode(x); return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); };
export const unb64u = (s) => { const t = String(s).replace(/-/g, '+').replace(/_/g, '/'); const bin = atob(t + '='.repeat((4 - (t.length % 4)) % 4)); const out = new Uint8Array(bin.length); for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i); return out; };
const EC = { name: 'ECDH', namedCurve: 'P-256' };

/** The key's id: the first 8 bytes of SHA-256 of its public half, as 16 hex digits. */
export async function keyId(pubRaw) { return hex(new Uint8Array(await subtle.digest('SHA-256', pubRaw)).slice(0, 8)); }
/** A new key pair for the desk: { pub (base64url, 87 letters), kid, jwk (the private half, kept in Drive) }. */
export async function newDeskKey() {
  const kp = await subtle.generateKey(EC, true, ['deriveBits']);
  const pub = new Uint8Array(await subtle.exportKey('raw', kp.publicKey));
  return { pub: b64u(pub), kid: await keyId(pub), jwk: await subtle.exportKey('jwk', kp.privateKey) };
}
const rawOf = (jwk) => cat(new Uint8Array([4]), unb64u(jwk.x), unb64u(jwk.y));
async function twoKeys(shared, oneRaw, deskRaw) {
  const ikm = await subtle.importKey('raw', shared, 'HKDF', false, ['deriveKey']);
  const salt = cat(oneRaw, deskRaw);
  const k = (info) => subtle.deriveKey({ name: 'HKDF', hash: 'SHA-256', salt, info: te.encode(info) }, ikm, { name: 'AES-GCM', length: 256 }, false, ['encrypt', 'decrypt']);
  return { note: await k('FOV1 note'), body: await k('FOV1 body') };
}

/** Seals a note (an object) and a file (bytes) to the desk's public key. */
export async function seal(deskPub, note, body) {
  const deskRaw = unb64u(deskPub);
  if (deskRaw.length !== 65 || deskRaw[0] !== 4) throw new Error('That is not the desk\'s upload key.');
  const desk = await subtle.importKey('raw', deskRaw, EC, false, []);
  const one = await subtle.generateKey(EC, false, ['deriveBits']);
  const oneRaw = new Uint8Array(await subtle.exportKey('raw', one.publicKey));
  const K = await twoKeys(await subtle.deriveBits({ name: 'ECDH', public: desk }, one.privateKey, 256), oneRaw, deskRaw);
  const kid = new Uint8Array((await keyId(deskRaw)).match(/../g).map((x) => parseInt(x, 16)));
  const head = cat(MAGIC, kid, oneRaw);
  const ivN = rand(12); const ivB = rand(12);
  const n = new Uint8Array(await subtle.encrypt({ name: 'AES-GCM', iv: ivN, additionalData: head }, K.note, te.encode(JSON.stringify(note))));
  if (n.length > NOTE_MAX) throw new Error('The note is too long.');
  const b = new Uint8Array(await subtle.encrypt({ name: 'AES-GCM', iv: ivB, additionalData: head }, K.body, body));
  const len = new Uint8Array(4); new DataView(len.buffer).setUint32(0, n.length);
  return cat(head, len, ivN, n, ivB, b);
}
async function keysFor(jwk, bytes) {
  if (!(bytes instanceof Uint8Array) || bytes.length < HEAD + 4 + 12 + 16 || hex(bytes.subarray(0, 4)) !== hex(MAGIC)) throw new Error('This is not a sealed upload.');
  const deskRaw = rawOf(jwk);
  if (hex(bytes.subarray(4, 12)) !== await keyId(deskRaw)) throw new Error('This upload was sealed to another desk key.');
  const oneRaw = bytes.slice(12, HEAD);
  const priv = await subtle.importKey('jwk', jwk, EC, false, ['deriveBits']);
  const one = await subtle.importKey('raw', oneRaw, EC, false, []);
  return { K: await twoKeys(await subtle.deriveBits({ name: 'ECDH', public: one }, priv, 256), oneRaw, deskRaw), head: bytes.subarray(0, HEAD) };
}
/** The note alone, from the start of a sealed file (READ_FIRST bytes are enough): { note, bodyAt }. */
export async function openNote(jwk, bytes) {
  const { K, head } = await keysFor(jwk, bytes);
  const n = new DataView(bytes.buffer, bytes.byteOffset + HEAD, 4).getUint32(0);
  if (n > NOTE_MAX || bytes.length < HEAD + 4 + 12 + n) throw new Error('The upload was cut short.');
  const at = HEAD + 4;
  const plain = await subtle.decrypt({ name: 'AES-GCM', iv: bytes.subarray(at, at + 12), additionalData: head }, K.note, bytes.subarray(at + 12, at + 12 + n));
  return { note: JSON.parse(td.decode(plain)), bodyAt: at + 12 + n };
}
/** The note and the file: { note, body }. A file changed by a single bit does not open. */
export async function open(jwk, bytes) {
  const { note, bodyAt } = await openNote(jwk, bytes);
  const { K, head } = await keysFor(jwk, bytes);
  if (bytes.length < bodyAt + 12 + 16) throw new Error('The upload was cut short.');
  const body = new Uint8Array(await subtle.decrypt({ name: 'AES-GCM', iv: bytes.subarray(bodyAt, bodyAt + 12), additionalData: head }, K.body, bytes.subarray(bodyAt + 12)));
  return { note, body };
}
/** SHA-256 of a text, as hex: the words a person agreed to are recorded by it. */
export async function sha256(text) { return hex(new Uint8Array(await subtle.digest('SHA-256', te.encode(text)))); }
