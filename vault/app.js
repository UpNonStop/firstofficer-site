// The vault upload page: a person gives their consent and sends their travel documents, and can never read them back
// (Ohad, 11/20/2026: "client can only upload, never read their upload (only operator), for safety and security reasons").
//
// The link carries all the page needs after # (a browser never sends that part to a server): a Cloud Storage policy the
// desk signed that lets this page add files to one folder and do nothing else, the desk's public key, and the names. Each
// file is sealed here, on this device, to the desk's key (fov.js), and only then sent. The consent goes first to the
// consent ledger (who, when, from where, and the words' fingerprint, never a name) and then, sealed, to the desk.
// Nothing is kept in this browser: no storage, no cookie, and nothing from anywhere but Google Cloud Storage and the
// ledger, which the page's own content policy enforces.

import { unpackLink, intakeFields, intakeKey, wordsFor, childWords, WORDS, WORDS_VERSION, IN_SHORT } from './vaultlink.js';
import { seal, sha256, b64u } from './fov.js';

const CONSENT_URL = 'https://cuzuzzbezswvejnoskum.supabase.co/functions/v1/fo-vault-consent';
const PAGE = 'vault page 1';
const WRITE_TO = 'compliance@upnonstop.com';
const MAX_FILE = 25 * 1024 * 1024;
const TYPE_OF = { pdf: 'application/pdf', jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', heic: 'image/heic', heif: 'image/heif', webp: 'image/webp' };
const OK_TYPES = new Set(Object.values(TYPE_OF));
const DOCS = {
  passport: { t: 'Passport photo page', hint: 'The page with the photo: flat, in good light, all 4 corners in view. A photo or a PDF.' },
  auth: { t: 'Visa or travel authorization', hint: 'The visa page, or the approval a country sent. A photo or a PDF.' },
  photos: { t: 'Photo for an application', hint: 'Only the photo the application asks for.' },
  trip: { t: 'Trip letter', hint: 'Such as consent for a child traveling without both parents. A photo or a PDF.' },
};

/* ---- small helpers ---- */
function h(tag, attrs, ...kids) {
  const [t, ...cls] = tag.split('.');
  const el = document.createElement(t);
  if (cls.length) el.className = cls.join(' ');
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === null || v === undefined || v === false) continue;
    if (k.startsWith('on')) el.addEventListener(k.slice(2), v); else el.setAttribute(k, v === true ? '' : String(v));
  }
  for (const k of kids.flat(Infinity)) if (k !== null && k !== undefined && k !== false) el.append(k instanceof Node ? k : document.createTextNode(String(k)));
  return el;
}
const app = document.getElementById('app');
const mount = (...kids) => { app.replaceChildren(...kids.flat(Infinity).filter(Boolean)); };
const when = (t) => new Intl.DateTimeFormat('en-US', { month: '2-digit', day: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit', hourCycle: 'h23', timeZoneName: 'short' }).format(new Date(t)).replace(',', '');
const size = (b) => (b >= 1048576 ? (b / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(b / 1024)) + ' KB');
const initials = (n) => n.split(/\s+/).filter(Boolean).slice(0, 2).map((x) => x[0].toUpperCase()).join('');
const listWords = (xs) => (xs.length < 3 ? xs.join(' and ') : xs.slice(0, -1).join(', ') + ' and ' + xs[xs.length - 1]);
const mail = () => h('a', { href: 'mailto:' + WRITE_TO }, WRITE_TO);
function sealIcon() {
  const ns = 'http://www.w3.org/2000/svg';
  const s = document.createElementNS(ns, 'svg'); s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('fill', 'none'); s.setAttribute('stroke', 'currentColor'); s.setAttribute('stroke-width', '1.8'); s.setAttribute('aria-hidden', 'true');
  const p = document.createElementNS(ns, 'path'); p.setAttribute('d', 'M7 10V7.5a5 5 0 0 1 10 0V10M5.5 10h13v10h-13z'); s.append(p); return s;
}
const head = (ink, pink, sub) => [h('h1', null, ink, h('br'), h('span.pk', null, pink)), sub ? h('p.fg-sub', null, sub) : null];
function focusTop() { const t = app.querySelector('h1'); if (t) { t.setAttribute('tabindex', '-1'); t.focus({ preventScroll: true }); } window.scrollTo(0, 0); }

/* ---- the link ---- */
const L = unpackLink(location.hash);
const people = L ? L.people.map((p) => Object.assign({}, p, { name: L.names[p.pid].trim() })) : [];
const self = people.find((p) => p.as === 'self') || null;
const kids = people.filter((p) => p.as === 'parent');
const S = { consent: null, picked: new Map(), sent: [], busy: false };
const asked = L ? Date.parse(L.date.replace(/^(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)(\d\d)Z$/, '$1-$2-$3T$4:$5:$6Z')) : 0;

function steps(at) {
  const all = [['consent', 'Your consent'], ['docs', 'Your documents'], ['done', 'Done']];
  const i = all.findIndex(([k]) => k === at);
  return h('ol.steps', { 'aria-label': 'Steps' }, all.map(([k, t], j) => h('li' + (j < i ? '.done' : ''), { 'aria-current': j === i ? 'step' : null }, h('i', null, String(j + 1)), t)));
}
function whoList() {
  return h('ul.who', null, people.map((p) => h('li', null, h('span.av', { 'aria-hidden': 'true' }, initials(p.name)),
    h('span', null, h('b', null, p.name), h('small', null, listWords(p.slots.map((k) => DOCS[k].t.toLowerCase())) + (p.as === 'parent' ? ', with your consent as their parent or guardian' : ''))))));
}

/* ---- sending: sealed here, then into the link's own folder, where nothing can be read back ---- */
function send(note, bytes, onProgress) {
  return seal(L.key, note, bytes).then((sealed) => new Promise((done, fail) => {
    const name = Date.now().toString(36) + '-' + b64u(crypto.getRandomValues(new Uint8Array(12)));
    const fd = new FormData();
    for (const [k, v] of intakeFields(L, intakeKey(L, name))) fd.append(k, v);
    fd.append('file', new Blob([sealed], { type: 'application/octet-stream' }), 'sealed');
    const x = new XMLHttpRequest();
    x.open('POST', 'https://storage.googleapis.com/' + L.bucket);
    if (onProgress) x.upload.onprogress = (e) => { if (e.lengthComputable) onProgress(e.loaded / e.total); };
    x.onload = () => (x.status >= 200 && x.status < 300 ? done() : fail(new Error(x.status === 403 ? 'The link would not take it: it may have ended, or the file is over 25 MB.' : 'Not sent: storage answered ' + x.status + '. Try again.')));
    x.onerror = () => fail(new Error('Not sent: the connection dropped. Press Send again.'));
    x.send(fd);
  }));
}

/* ---- step 1: the consent ---- */
function consentStep() {
  const name = h('input.fld', { type: 'text', autocomplete: 'name', autocapitalize: 'words', spellcheck: 'false', 'aria-describedby': 'v-sig' });
  const tickSelf = self ? h('input', { type: 'checkbox' }) : null;
  const tickKids = kids.map(() => h('input', { type: 'checkbox' }));
  const errEl = h('p.err', { role: 'alert', hidden: true });
  const go = h('button.btn.pk.wide', { type: 'button' }, 'Agree and continue');
  const words = wordsFor(kids.map((k) => k.name));
  go.addEventListener('click', async () => {
    if (S.busy) return;
    const signer = name.value.trim().replace(/\s+/g, ' ');
    const say = (t) => { errEl.textContent = t; errEl.hidden = false; };
    if (signer.length < 3 || signer.length > 80) return say('Type your full name, as your signature.');
    if (tickSelf && !tickSelf.checked) return say('Tick the box to agree to the words, or close this page.');
    if (tickKids.some((x) => !x.checked)) return say('Tick the box for each child, or close this page.');
    errEl.hidden = true; S.busy = true; go.disabled = true; go.textContent = 'Recording your consent';
    try {
      const fp = await sha256(words);
      const as = Object.fromEntries(people.map((p) => [p.pid, p.as]));
      const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      let r;
      try { r = await fetch(CONSENT_URL, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ link: { c: L.client, l: L.link, w: L.who, d: L.date, x: L.exp, s: L.sig }, as, words: { version: WORDS_VERSION, sha256: fp }, device: { tz } }), credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store' }); }
      catch (_) { throw new Error('Your consent was not recorded: the connection dropped. Nothing was sent. Press Agree and continue again.'); }
      const j = await r.json().catch(() => null);
      if (!r.ok || !j || !j.ok) throw new Error((j && j.error ? j.error + ' ' : '') + 'Your consent was not recorded, so nothing was sent.');
      go.textContent = 'Sending your consent to First Officer';
      const record = { kind: 'vault consent', version: WORDS_VERSION, words, sha256: fp, signer, as, names: Object.fromEntries(people.map((p) => [p.pid, p.name])), ledger: { seq: j.seq, row_hash: j.row_hash, at: j.at },
        device: { tz, lang: navigator.language || '', ua: navigator.userAgent.slice(0, 300) }, page: PAGE, link: L.link };
      await send({ t: 'consent', l: L.link, for: people.map((p) => p.pid), a: new Date().toISOString() }, new TextEncoder().encode(JSON.stringify(record)));
      S.consent = { signer, at: j.at, seq: j.seq };
      S.busy = false; docsStep(); focusTop();
    } catch (e) {
      S.busy = false; go.disabled = false; go.textContent = 'Agree and continue'; say(e.message || 'That did not go through. Try again.');
    }
  });
  mount(head('Your travel documents,', 'sent safely.', [L.from ? h('b', null, 'For ' + L.from + '. ') : null, 'Your First Officer advisor asks for these, to plan and book your travel. They are sealed on this device before they leave it, and only your advisor can open them.']),
    steps('consent'),
    h('section.card', { 'aria-labelledby': 'v-ask' }, h('h2', { id: 'v-ask' }, 'What is asked'), h('p.lede', null, 'Asked on ' + when(asked) + '. This link works until ' + when(L.exp * 1000) + '.'), whoList()),
    h('section.card', { 'aria-labelledby': 'v-consent' }, h('h2', { id: 'v-consent' }, 'Your consent'),
      h('p.lede', null, 'Before anything is sent, in short:'),
      h('ul.short', null, IN_SHORT.map((t) => h('li', null, h('span', null, t)))),
      h('details.words', null, h('summary', null, 'The words you agree to'), h('blockquote', null, h('p', null, WORDS), kids.map((k) => h('p', null, childWords(k.name))))),
      h('label.fl', null, h('span', null, 'Your full name'), name, h('small.v', { id: 'v-sig' }, 'Typed as your signature.')),
      self ? h('label.tick', null, tickSelf, h('span', null, 'I agree to these words, for myself.')) : null,
      kids.map((k, i) => h('label.tick', null, tickKids[i], h('span', null, 'I am ' + k.name + '\'s parent or legal guardian, ' + k.name + ' is under the age of majority where they live, and I agree for them.'))),
      errEl, go,
      h('p.note', null, 'Your consent is recorded with the time, this device and the address it came from, and the words above. To take it back at any time, write to ', mail(), '.')));
}

/* ---- step 2: the documents ---- */
const kindOf = (f) => (OK_TYPES.has(f.type) ? f.type : TYPE_OF[(f.name.split('.').pop() || '').toLowerCase()] || '');
function docsStep() {
  const errEl = h('p.err', { role: 'alert', hidden: true });
  const go = h('button.btn.pk.wide', { type: 'button' }, 'Send');
  const lists = new Map();
  const count = () => { const n = [...S.picked.values()].flat().filter((x) => x.st !== 'sent').length; go.disabled = S.busy || n === 0; go.textContent = n ? 'Send ' + (n === 1 ? '1 file' : n + ' files') : 'Send'; };
  const draw = (key) => {
    const ul = lists.get(key); const items = S.picked.get(key) || [];
    ul.replaceChildren(...items.map((it) => h('li', null,
      it.url ? h('img.th', { src: it.url, alt: '' }) : h('span.th', { 'aria-hidden': 'true' }, it.type === 'application/pdf' ? 'PDF' : 'IMG'),
      h('span', null, h('b', null, it.file.name), h('small', null, it.st === 'sent' ? 'Sent ' + when(it.at) : it.st === 'sending' ? 'Sealing and sending' : size(it.file.size) + ', not sent yet'), it.st === 'sending' ? h('span.bar', null, it.barEl) : null),
      it.st === 'sent' ? h('span.ok', null, 'Sent') : h('button.x', { type: 'button', disabled: S.busy, 'aria-label': 'Remove ' + it.file.name, onclick: () => { if (it.url) URL.revokeObjectURL(it.url); S.picked.set(key, items.filter((x) => x !== it)); draw(key); count(); } }, 'Remove'))));
  };
  const cards = [];
  for (const p of people) for (const k of p.slots) {
    const key = p.pid + '/' + k;
    const ul = h('ul.files'); lists.set(key, ul);
    const input = h('input', { type: 'file', multiple: true, accept: 'image/*,application/pdf,.pdf,.heic,.heif', 'aria-label': 'Add ' + DOCS[k].t.toLowerCase() + ' for ' + p.name });
    input.addEventListener('change', () => {
      const add = [...input.files]; input.value = '';
      const bad = [];
      for (const f of add) {
        const type = kindOf(f);
        if (!type) { bad.push(f.name + ' is not a photo or a PDF.'); continue; }
        if (f.size > MAX_FILE) { bad.push(f.name + ' is over 25 MB.'); continue; }
        if (!f.size) { bad.push(f.name + ' is empty.'); continue; }
        const it = { file: f, type, st: 'picked', url: type.startsWith('image/') && type !== 'image/heic' && type !== 'image/heif' ? URL.createObjectURL(f) : null, barEl: h('i') };
        S.picked.set(key, (S.picked.get(key) || []).concat([it]));
      }
      errEl.textContent = bad.join(' '); errEl.hidden = !bad.length;
      draw(key); count();
    });
    cards.push(h('div.doc', null, h('h3', null, DOCS[k].t), h('p.for', null, 'For ' + p.name), h('p.hint', null, DOCS[k].hint),
      h('span.pick', null, h('span.btn.ghost', { 'aria-hidden': 'true' }, 'Add a photo or PDF'), input), ul));
    draw(key);
  }
  go.addEventListener('click', async () => {
    if (S.busy) return;
    S.busy = true; errEl.hidden = true; count();
    try {
      for (const [key, items] of S.picked) {
        const [pid, slot] = key.split('/');
        for (const it of items) {
          if (it.st === 'sent') continue;
          it.st = 'sending'; draw(key);
          const bytes = new Uint8Array(await it.file.arrayBuffer());
          await send({ t: 'doc', l: L.link, i: pid, s: slot, n: it.file.name.slice(0, 120), y: it.type, z: it.file.size, a: new Date().toISOString() }, bytes, (f) => { it.barEl.style.width = Math.round(f * 100) + '%'; });
          it.st = 'sent'; it.at = Date.now();
          if (it.url) { URL.revokeObjectURL(it.url); it.url = null; }   /* sent: this page keeps no picture of it */
          S.sent.push({ name: it.file.name, size: it.file.size, at: it.at, what: DOCS[slot].t, who: people.find((p) => p.pid === pid).name });
          it.file = { name: it.file.name, size: it.file.size };
          draw(key);
        }
      }
      S.busy = false; doneStep(); focusTop();
    } catch (e) {
      for (const [key, items] of S.picked) { for (const it of items) if (it.st === 'sending') it.st = 'picked'; draw(key); }
      S.busy = false; count(); errEl.textContent = e.message || 'Not sent. Try again.'; errEl.hidden = false;
    }
  });
  mount(head('Your consent', 'is recorded.', 'Now add each document. A phone photo is fine. Each file is sealed on this device before it is sent.'),
    steps('docs'),
    h('section.card', { 'aria-labelledby': 'v-docs' }, h('h2', { id: 'v-docs' }, 'Your documents'), h('p.lede', null, 'Add what you have now. You can open this link again for the rest until ' + when(L.exp * 1000) + '.'),
      cards, errEl, go,
      h('p.seal', null, sealIcon(), h('span', null, 'Once sent, a document cannot be opened from this page again, not even by you. Only your First Officer advisor can open it.'))));
  count();
}

/* ---- step 3: done ---- */
function doneStep() {
  mount(head('Sent.', 'Thank you.', 'Your First Officer advisor has them now. For your safety, this page cannot open them again, not even for you.'),
    steps('done'),
    h('section.card', { 'aria-labelledby': 'v-sent' }, h('h2', { id: 'v-sent' }, 'What you sent'),
      S.sent.length ? h('ul.sent', null, S.sent.map((x) => h('li', null, h('span', null, x.what + ' for ' + x.who, h('small', null, x.name + ', ' + size(x.size) + ', sent ' + when(x.at)))))) : h('p.lede', null, 'Your consent, and no document yet.'),
      h('div.acts', null, h('button.btn.ghost.wide', { type: 'button', onclick: () => { S.picked.clear(); docsStep(); focusTop(); } }, 'Send another document')),
      h('p.note', null, 'You can close this page. To see, correct or delete what First Officer keeps, or to take your consent back, write to ', mail(), '.')));
}

/* ---- a link that is not whole, or has ended ---- */
if (!L) mount(head('This link', 'is not complete.', 'Open it again from the message it came in. If it still says this, ask your First Officer advisor for a new one.'));
else if (L.exp * 1000 <= Date.now()) mount(head('This link', 'has ended.', 'For your safety, a link works for 7 days at most. Ask your First Officer advisor for a new one.'));
else consentStep();
window.addEventListener('hashchange', () => location.reload());
