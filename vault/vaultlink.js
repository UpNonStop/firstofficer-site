// vaultlink.js: the client's upload link, the same file byte for byte in four places (tools/mc_check/intake.js checks it):
//   mc/live/vaultlink.js                              the desk, which makes a link and reads what came in by it
//   site/vault/vaultlink.js                           the client's page at firstofficer.upnonstop.com/vault
//   infra/desk-gateway/vaultlink.js                   the desk's app, which signs a link as the upload account
//   supabase/functions/fo-vault-consent/vaultlink.js  the consent record, which checks a link before it writes
//
// A link lets a client put files into the upload bucket and nothing else (Ohad, 11/20/2026: "client can only upload,
// never read their upload (only operator)"). It carries a Google Cloud Storage V4 POST policy that the desk's app signed
// as the upload account, whose only role on the bucket is to create objects: the page can add files under this link's own
// folder, of the size the policy allows, until it ends, and can never read, list, replace or delete one. Who the link is
// for, and which documents it asks for, are inside the signed policy, so neither the page nor anyone holding the link can
// change them. Plain JavaScript, no imports: it runs in a browser, in Node and in Deno.

/** Where uploads land, and the account that signs a link: made in the desk's Google Cloud project (fo-desk-aa241e). */
export const BUCKET = 'fo-desk-aa241e-vault-intake';
export const SIGNER = 'vault-intake@fo-desk-aa241e.iam.gserviceaccount.com';
/** The documents a link can ask for, and their one-letter codes inside a link. */
export const SLOTS = { passport: 'p', auth: 'v', photos: 'f', trip: 't' };
export const SLOT_OF = { p: 'passport', v: 'auth', f: 'photos', t: 'trip' };
/** 25 MB a file, and room for the few hundred bytes the sealing adds. */
export const MAX_BYTES = 25 * 1024 * 1024 + 65536;
/** The longest a link lasts: Google's limit for a signed policy. */
export const MAX_DAYS = 7;

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/;
const LINK = /^[A-Za-z0-9_-]{22}$/;
const WHO = /^P\d{2,3}[sc]-[pvft]{1,4}(\.P\d{2,3}[sc]-[pvft]{1,4}){0,5}$/;
const DATE = /^\d{8}T\d{6}Z$/;

export const isClient = (s) => UUID.test(String(s || ''));
export const isLink = (s) => LINK.test(String(s || ''));
/**
 * Who a link is for, as P01s-pv.P02c-p: each person's number on the vault card, s when they give their own consent or c
 * when the one holding the link gives it as their parent or guardian, then the documents asked for. At most 6 people, at
 * most one of them giving their own.
 */
export function parseWho(w) {
  if (!WHO.test(String(w || ''))) return null;
  const people = String(w).split('.').map((x) => ({ pid: x.slice(0, x.indexOf('-') - 1), as: x[x.indexOf('-') - 1] === 's' ? 'self' : 'parent', slots: [...x.slice(x.indexOf('-') + 1)].map((c) => SLOT_OF[c]) }));
  const pids = new Set(people.map((p) => p.pid));
  if (pids.size !== people.length || people.filter((p) => p.as === 'self').length > 1) return null;
  if (people.some((p) => new Set(p.slots).size !== p.slots.length)) return null;
  return people;
}
export function makeWho(people) {
  return people.map((p) => p.pid + (p.as === 'self' ? 's' : 'c') + '-' + p.slots.map((k) => SLOTS[k]).join('')).join('.');
}

/** The policy, exactly as the desk's app signs it and as Google checks it: the same inputs give the same bytes everywhere. */
export function intakePolicy(o) {
  const conditions = [
    ['starts-with', '$key', 'in/' + o.client + '/' + o.link + '/'],
    { bucket: o.bucket },
    ['content-length-range', 1, o.max],
    ['eq', '$Content-Type', 'application/octet-stream'],
    { 'x-goog-meta-fo-who': o.who },
    { 'x-goog-date': o.date },
    { 'x-goog-credential': o.signer + '/' + o.date.slice(0, 8) + '/auto/storage/goog4_request' },
    { 'x-goog-algorithm': 'GOOG4-RSA-SHA256' },
  ];
  const expiration = new Date(o.exp * 1000).toISOString().replace(/\.\d{3}Z$/, 'Z');
  const json = JSON.stringify({ conditions, expiration });
  if (!/^[\x20-\x7e]*$/.test(json)) throw new Error('a policy holds only plain characters');
  return { json, b64: btoa(json) };
}
/** The fields of the upload, in the order Google wants them, the file last. */
export function intakeFields(o, key) {
  return [['key', key], ['Content-Type', 'application/octet-stream'], ['x-goog-meta-fo-who', o.who], ['x-goog-algorithm', 'GOOG4-RSA-SHA256'],
    ['x-goog-credential', o.signer + '/' + o.date.slice(0, 8) + '/auto/storage/goog4_request'], ['x-goog-date', o.date], ['policy', intakePolicy(o).b64], ['x-goog-signature', o.sig]];
}
export const intakeKey = (o, name) => 'in/' + o.client + '/' + o.link + '/' + name;
export const OBJECT = /^in\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\/[A-Za-z0-9_-]{22}\/[A-Za-z0-9_-]{8,64}$/;

/* base64url, for the link's fragment */
const b64u = (s) => btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const unb64u = (s) => { const t = String(s).replace(/-/g, '+').replace(/_/g, '/'); return atob(t + '='.repeat((4 - (t.length % 4)) % 4)); };
const utf8 = (s) => unescape(encodeURIComponent(s));
const unutf8 = (s) => decodeURIComponent(escape(s));
const hexOf = (bin) => [...bin].map((c) => c.charCodeAt(0).toString(16).padStart(2, '0')).join('');
const binOf = (hex) => String(hex).match(/../g).map((x) => String.fromCharCode(parseInt(x, 16))).join('');

/**
 * Everything the page needs, in the part of the address after #, which a browser never sends to any server: the signed
 * policy's inputs and its signature, the desk's public key the files are sealed to, and the names the page greets by.
 * Fields are joined by ! (which none of them holds), so a link stays near 600 letters.
 */
export function packLink(o) {
  return ['1', o.client, o.link, o.who, o.date, o.exp.toString(36), b64u(binOf(o.sig)), o.key, b64u(utf8(JSON.stringify({ n: o.names, f: o.from || '' })))].join('!');
}
/** A link back from its fragment, checked; null when anything in it is not what a link holds. */
export function unpackLink(frag) {
  const f = String(frag || '').replace(/^#/, '').split('!');
  if (f.length !== 9 || f[0] !== '1') return null;
  let sig = ''; let extra = null;
  try { sig = hexOf(unb64u(f[6])); extra = JSON.parse(unutf8(unb64u(f[8]))); } catch (_) { return null; }
  const people = parseWho(f[3]);
  const o = { bucket: BUCKET, signer: SIGNER, max: MAX_BYTES, client: f[1], link: f[2], who: f[3], date: f[4], exp: parseInt(f[5], 36), sig, key: f[7], names: extra && extra.n, from: extra && extra.f, people };
  const names = o.names && typeof o.names === 'object' ? o.names : null;
  if (!isClient(o.client) || !isLink(o.link) || !people || !DATE.test(o.date) || !/^[0-9a-z]{1,10}$/.test(f[5]) || !Number.isInteger(o.exp) || !/^[0-9a-f]{512}$/.test(o.sig)) return null;
  if (!/^[A-Za-z0-9_-]{87}$/.test(o.key) || !names || !people.every((p) => typeof names[p.pid] === 'string' && names[p.pid].trim().length > 0 && names[p.pid].length <= 80)) return null;
  if (typeof o.from !== 'string' || o.from.length > 80) return null;
  return o;
}

/* ---- the words a person agrees to on the page: compliance.md 13.11, version 2, a draft for counsel ---- */
export const WORDS_VERSION = 'Vault consent, version 2';
export const WORDS = 'I agree that UpNonStop LLC, which runs First Officer, keeps the travel documents I send on this page, such as my passport photo page and visas, and the travel details in them, in its private vault in Google Drive, so it can plan and book travel for me and my company. They are encrypted on my device before they are sent. Only First Officer\'s staff can open them. This page cannot show them again, not even to me, and a person viewing them in the vault cannot download, print or copy them. Each document is deleted on its date: a passport when it is renewed, a visa when it expires, an application photo when the application is decided, and a trip letter 30 days after the trip. Everything is deleted 30 days after I stop being a client. First Officer never keeps my Social Security number, card numbers or bank sign-ins. I can see, correct or delete what is kept, or take this back, at any time by writing to compliance@upnonstop.com. (Vault consent, version 2.)';
export const childWords = (name) => 'I am ' + name + '\'s parent or legal guardian, ' + name + ' is under the age of majority where they live, and I agree, for them, to the above for their documents.';
/** The exact words for one consent: the paragraph, then one sentence for each child it is given for. */
export const wordsFor = (children) => [WORDS].concat((children || []).map(childWords)).join(' ');
/** The words as the consent ledger keeps them: a child's name never leaves the vault, so it stands as [the child's name]. */
export const wordsTemplate = (n) => (n ? WORDS + ' ' + childWords('[the child\'s name]') : WORDS);
/** The short version, above the words, in the client's own terms. */
export const IN_SHORT = [
  'First Officer keeps these documents only to plan and book your travel.',
  'They are encrypted on this device before they leave it. Only your First Officer advisor can open them.',
  'Once sent, this page cannot show them again, not even to you.',
  'Each one is deleted on its date, and everything 30 days after you stop being a client.',
  'You can see, correct or delete what is kept, or take this back, at any time.',
];
