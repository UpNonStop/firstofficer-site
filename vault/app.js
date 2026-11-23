// The vault upload page: a person gives their consent and sends what an award booking needs, and can never read it back
// (Ohad, 11/20/2026: "client can only upload, never read their upload (only operator), for safety and security reasons").
// What it asks is Ohad's list (11/20/2026): the name exactly as on the passport, each passport with its photo page, the
// Known Traveler and redress numbers, each visa and travel authorization with its dates and page, airline and hotel
// accounts with a sign-in only where the person chooses to give one, and for the owner each card on file: everything but
// its number. A card's number and code come only for one booking, by a link of its own (the card step below).
//
// The link carries all the page needs after # (a browser never sends that part to a server): a Cloud Storage policy the
// desk signed that lets this page add files to one folder and do nothing else, the desk's public key, and the names.
// Everything is sealed here, on this device, to the desk's key (fov.js), and only then sent. The consent goes first to
// the consent ledger (who, when, from where, and the words' fingerprint, never a name) and then, sealed, to the desk.
// Nothing is kept in this browser: no storage, no cookie, and nothing from anywhere but Google Cloud Storage and the
// ledger, which the page's own content policy enforces.

import { unpackLink, intakeFields, intakeKey, wordsFor, childWords, WORDS, WORDS_VERSION, IN_SHORT, CARD_VERSION, cardWords } from './vaultlink.js';
import { seal, sha256, b64u } from './fov.js';

const CONSENT_URL = 'https://cuzuzzbezswvejnoskum.supabase.co/functions/v1/fo-vault-consent';
const PAGE = 'vault page 2';
const WRITE_TO = 'compliance@upnonstop.com';
const MAX_FILE = 25 * 1024 * 1024;
const TYPE_OF = { pdf: 'application/pdf', jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png', heic: 'image/heic', heif: 'image/heif', webp: 'image/webp' };
const OK_TYPES = new Set(Object.values(TYPE_OF));
const PART_WORDS = { details: 'name as on the passport, passports and how to reach them', visas: 'visas and travel authorizations', accounts: 'airline and hotel accounts', cards: 'cards on file', booking: 'one card, for one booking' };

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
const plural = (n, one, many) => n + ' ' + (n === 1 ? one : many || one + 's');
const mail = () => h('a', { href: 'mailto:' + WRITE_TO }, WRITE_TO);
function sealIcon() {
  const ns = 'http://www.w3.org/2000/svg';
  const s = document.createElementNS(ns, 'svg'); s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('fill', 'none'); s.setAttribute('stroke', 'currentColor'); s.setAttribute('stroke-width', '1.8'); s.setAttribute('aria-hidden', 'true');
  const p = document.createElementNS(ns, 'path'); p.setAttribute('d', 'M7 10V7.5a5 5 0 0 1 10 0V10M5.5 10h13v10h-13z'); s.append(p); return s;
}
const head = (ink, pink, sub) => [h('h1', null, ink, h('br'), h('span.pk', null, pink)), sub ? h('p.fg-sub', null, sub) : null];
function focusTop() { const t = app.querySelector('h1'); if (t) { t.setAttribute('tabindex', '-1'); t.focus({ preventScroll: true }); } window.scrollTo(0, 0); }
let uid = 0;
const nid = () => 'v-' + (++uid);

/* ---- what each line takes, checked here as the desk checks it again when it files ---- */
const two = (n) => String(n).padStart(2, '0');
function parseD(v) { const m = /^(\d{2})\/(\d{2})\/(\d{4})$/.exec(String(v || '').trim()); if (!m) return null; const t = Date.UTC(+m[3], +m[1] - 1, +m[2], 12); const d = new Date(t); return d.getUTCMonth() === +m[1] - 1 && d.getUTCDate() === +m[2] ? t : null; }
const fmt = (t) => { const d = new Date(t); return two(d.getUTCMonth() + 1) + '/' + two(d.getUTCDate()) + '/' + d.getUTCFullYear(); };
const today = () => { const n = new Date(); return Date.UTC(n.getFullYear(), n.getMonth(), n.getDate(), 12); };
const luhn = (d) => { let t = 0; for (let i = 0; i < d.length; i++) { let n = +d[d.length - 1 - i]; if (i % 2) { n *= 2; if (n > 9) n -= 9; } t += n; } return t % 10 === 0; };
const cardLike = (x) => /\b(?:\d[ -]?){13,19}\b/.test(x) || /\b\d{3}-\d{2}-\d{4}\b/.test(x);
const RULE = {
  name: (v) => (/^[A-Za-z][A-Za-z' -]{0,39}$/.test(v.replace(/\s+/g, ' ')) ? { v: v.replace(/\s+/g, ' ') } : { err: 'As on the passport, in plain letters (no accents), spaces, hyphens and apostrophes.' }),
  text: (v) => (v.length > 80 ? { err: 'That is longer than this line takes.' } : cardLike(v) ? { err: 'That looks like a card or Social Security number: never type one here.' } : { v }),
  date: (v) => { const t = parseD(v); return t && t > Date.UTC(1900, 0, 1) ? { v: fmt(t) } : { err: 'A date as MM/DD/YYYY.' }; },
  past: (v) => { const t = parseD(v); return t && t > Date.UTC(1900, 0, 1) && t <= today() ? { v: fmt(t) } : { err: t ? 'That date is still to come.' : 'A date as MM/DD/YYYY.' }; },
  code: (min, max) => (v) => { const x = v.toUpperCase().replace(/[\s-]/g, ''); return new RegExp('^[A-Z0-9]{' + min + ',' + max + '}$').test(x) ? { v: x } : { err: 'Letters and digits only, ' + min + ' to ' + max + ' of them.' }; },
  member: (v) => { const x = v.toUpperCase().replace(/[\s-]/g, ''); if (!/^[A-Z0-9]{4,24}$/.test(x)) return { err: 'Letters and digits only, 4 to 24 of them.' }; if (/^\d{13,19}$/.test(x) && luhn(x)) return { err: 'That looks like a card number: the member number, please.' }; return { v: x }; },
  phone: (v) => (/^\+?[0-9 ().-]{7,20}$/.test(v) ? { v } : { err: 'A phone number, with its country code if it is not in the US.' }),
  email: (v) => (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) && v.length <= 120 ? { v: v.toLowerCase() } : { err: 'An email address.' }),
  last4: (v) => (/^\d{4}$/.test(v) ? { v } : { err: 'The last 4 digits, and nothing more.' }),
  mmyy: (v) => { const m = /^(0[1-9]|1[0-2])\s*\/?\s*(\d{2})$/.exec(v); if (!m) return { err: 'The month and year it expires, as MM/YY.' }; return Date.UTC(2000 + +m[2], +m[1], 1) <= Date.now() ? { err: 'That card has expired.' } : { v: m[1] + '/' + m[2] }; },
  zip: (v) => { const x = v.toUpperCase(); return /^[A-Z0-9][A-Z0-9 -]{1,9}$/.test(x) ? { v: x } : { err: 'A ZIP or postal code.' }; },
  region: (v) => (/^[A-Za-z][A-Za-z .'-]{1,39}$/.test(v) ? { v: /^[A-Za-z]{2}$/.test(v) ? v.toUpperCase() : v } : { err: 'The state or region: two letters in the US.' }),
};
/** One form line: its label, its input, its own error under it, and how it is checked. */
function line(label, rule, o) {
  o = o || {};
  const id = nid();
  const input = o.opts ? h('select.fld', { id }, h('option', { value: '' }, o.ph || 'Pick one'), o.opts.map((x) => h('option', { value: x }, x)))
    : h('input.fld', { id, type: o.type || 'text', inputmode: o.mode || null, autocomplete: o.ac || 'off', autocapitalize: o.cap || 'off', spellcheck: 'false', placeholder: o.ph || '', maxlength: o.max || null });
  const err = h('small.ferr', { role: 'alert', hidden: true });
  const L1 = { input, err, need: !!o.need, rule, label,
    node: h('label.fl' + (o.wide ? '.wide' : ''), { for: id }, h('span', null, label, o.need ? null : h('em', null, ' optional')), input, err, o.hint ? h('small.v', null, o.hint) : null),
    read() { err.hidden = true; const raw = String(input.value || '').trim(); if (!raw) { if (L1.need) { err.textContent = label + ', please.'; err.hidden = false; return { bad: true }; } return { v: '' }; } const r = o.opts ? (o.opts.includes(raw) ? { v: raw } : { err: 'Pick one.' }) : rule(raw); if (r.err) { err.textContent = r.err; err.hidden = false; return { bad: true }; } return { v: r.v }; },
    clear() { input.value = ''; } };
  return L1;
}
const grid = (...ls) => h('div.g2', null, ls.map((x) => x.node));
const kindOf = (f) => (OK_TYPES.has(f.type) ? f.type : TYPE_OF[(f.name.split('.').pop() || '').toLowerCase()] || '');
/** A file for one line: a photo or a PDF, picked here and sealed only when everything is sent. */
function filePick(what, need) {
  const err = h('small.ferr', { role: 'alert', hidden: true }); const shown = h('span.picked');
  const input = h('input', { type: 'file', accept: 'image/*,application/pdf,.pdf,.heic,.heif', 'aria-label': what });
  const P = { file: null, type: '', err,
    node: h('div.filebox', null, h('span.pick', null, h('span.btn.ghost', { 'aria-hidden': 'true' }, 'Add ' + what.toLowerCase()), input), shown, err),
    read() { err.hidden = true; if (!P.file && need) { err.textContent = what + ', please: a phone photo or a PDF.'; err.hidden = false; return { bad: true }; } return { file: P.file }; } };
  input.addEventListener('change', () => {
    const f = input.files[0]; input.value = ''; err.hidden = true; if (!f) return;
    const type = kindOf(f);
    const bad = !type ? f.name + ' is not a photo or a PDF.' : f.size > MAX_FILE ? f.name + ' is over 25 MB.' : !f.size ? f.name + ' is empty.' : '';
    if (bad) { err.textContent = bad; err.hidden = false; return; }
    P.file = f; P.type = type; shown.replaceChildren(h('b', null, f.name), h('small', null, size(f.size) + ', sealed when you send'), h('button.x', { type: 'button', onclick: () => { P.file = null; shown.replaceChildren(); } }, 'Remove'));
  });
  return P;
}
/** Lines that repeat (another passport, visa, account or card), each with its own Remove. */
function repeat(make, addLabel, first) {
  const list = h('div.reps'); const items = [];
  const add = () => { const it = make(); items.push(it); const box = h('div.rep', null, it.node, h('button.x', { type: 'button', onclick: () => { items.splice(items.indexOf(it), 1); box.remove(); } }, 'Remove this one')); list.append(box); };
  if (first) add();
  return { items, node: h('div', null, list, h('button.btn.ghost', { type: 'button', onclick: add }, addLabel)) };
}

/* ---- the link ---- */
const L = unpackLink(location.hash);
const people = L ? L.people.map((p) => Object.assign({}, p, { name: L.names[p.pid].trim() })) : [];
const self = people.find((p) => p.as === 'self') || null;
const kids = people.filter((p) => p.as === 'parent');
const isBooking = !!(L && L.booking);
const S = { consent: null, sent: [], busy: false };
const asked = L ? Date.parse(L.date.replace(/^(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)(\d\d)Z$/, '$1-$2-$3T$4:$5:$6Z')) : 0;

function steps(at) {
  const all = isBooking ? [['card', 'The card'], ['done', 'Done']] : [['consent', 'Your consent'], ['details', 'Your details'], ['done', 'Done']];
  const i = all.findIndex(([k]) => k === at);
  return h('ol.steps', { 'aria-label': 'Steps' }, all.map(([k, t], j) => h('li' + (j < i ? '.done' : ''), { 'aria-current': j === i ? 'step' : null }, h('i', null, String(j + 1)), t)));
}
function whoList() {
  return h('ul.who', null, people.map((p) => h('li', null, h('span.av', { 'aria-hidden': 'true' }, initials(p.name)),
    h('span', null, h('b', null, p.name), h('small', null, listWords(p.parts.map((k) => PART_WORDS[k])) + (p.as === 'parent' ? ', with your consent as their parent or guardian' : ''))))));
}

/* ---- sending: sealed here, then into the link's own folder, where nothing can be read back ---- */
function send(note, bytes, onProgress, suffix) {
  return seal(L.key, note, bytes).then((sealed) => new Promise((done, fail) => {
    const name = Date.now().toString(36) + '-' + b64u(crypto.getRandomValues(new Uint8Array(12))) + (suffix || '');
    const fd = new FormData();
    for (const [k, v] of intakeFields(L, intakeKey(L, name))) fd.append(k, v);
    fd.append('file', new Blob([sealed], { type: 'application/octet-stream' }), 'sealed');
    const x = new XMLHttpRequest();
    x.open('POST', 'https://storage.googleapis.com/' + L.bucket);
    if (onProgress) x.upload.onprogress = (e) => { if (e.lengthComputable) onProgress(e.loaded / e.total); };
    x.onload = () => (x.status >= 200 && x.status < 300 ? done() : fail(new Error(x.status === 403 ? 'The link would not take it: it may have ended, or a file is over 25 MB.' : 'Not sent: storage answered ' + x.status + '. Try again.')));
    x.onerror = () => fail(new Error('Not sent: the connection dropped. Press Send again.'));
    x.send(fd);
  }));
}
/** The consent ledger: who, when, from where and the words' fingerprint, never a name, before anything is sent. */
async function ledger(body, what) {
  let r;
  try { r = await fetch(CONSENT_URL, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(Object.assign({ link: { c: L.client, l: L.link, w: L.who, d: L.date, x: L.exp, s: L.sig } }, body)), credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store' }); }
  catch (_) { throw new Error('Your ' + what + ' was not recorded: the connection dropped. Nothing was sent. Try again.'); }
  const j = await r.json().catch(() => null);
  if (!r.ok || !j || !j.ok) throw new Error((j && j.error ? j.error + ' ' : '') + 'Your ' + what + ' was not recorded, so nothing was sent.');
  return j;
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
      const j = await ledger({ as, words: { version: WORDS_VERSION, sha256: fp }, device: { tz } }, 'consent');
      go.textContent = 'Sending your consent to First Officer';
      const record = { kind: 'vault consent', version: WORDS_VERSION, words, sha256: fp, signer, as, names: Object.fromEntries(people.map((p) => [p.pid, p.name])), ledger: { seq: j.seq, row_hash: j.row_hash, at: j.at },
        device: { tz, lang: navigator.language || '', ua: navigator.userAgent.slice(0, 300) }, page: PAGE, link: L.link };
      await send({ t: 'consent', l: L.link, for: people.map((p) => p.pid), a: new Date().toISOString() }, new TextEncoder().encode(JSON.stringify(record)));
      S.consent = { signer, at: j.at, seq: j.seq };
      S.busy = false; detailsStep(); focusTop();
    } catch (e) {
      S.busy = false; go.disabled = false; go.textContent = 'Agree and continue'; say(e.message || 'That did not go through. Try again.');
    }
  });
  mount(head('Your travel details,', 'sent safely.', [L.from ? h('b', null, 'For ' + L.from + '. ') : null, 'Your First Officer advisor asks for these, to plan and book your travel. They are sealed on this device before they leave it, and only your advisor can open them.']),
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

/* ---- step 2: the details, one section a person, each part as the desk asked it ---- */
function personForm(p) {
  const you = p.as === 'self';
  const whose = you ? 'your' : p.name.split(' ')[0] + '\'s';
  const F = { p, parts: [], sections: [] };
  if (p.parts.includes('details')) {
    const n = { First: line('First name', RULE.name, { need: true, ac: you ? 'given-name' : 'off' }), Middle: line('Middle name', RULE.name, { ac: you ? 'additional-name' : 'off' }), Last: line('Last name', RULE.name, { need: true, ac: you ? 'family-name' : 'off' }),
      Suffix: line('Suffix', null, { opts: ['Jr', 'Sr', 'II', 'III', 'IV'], ph: 'None' }) };
    const id = { Dob: line('Date of birth', RULE.past, { need: true, ph: 'MM/DD/YYYY', mode: 'numeric' }), Sex: line('Sex, as on the passport', null, { opts: ['F', 'M', 'X'], need: true }), Nat: line('Nationality', RULE.text, { hint: 'Both, for a dual citizen.' }) };
    const passports = repeat(() => {
      const it = { Country: line('Country that issued it', RULE.text, { need: true }), Number: line('Passport number', RULE.code(5, 12), { need: true }), Issued: line('Issued', RULE.past, { ph: 'MM/DD/YYYY', mode: 'numeric' }), Expires: line('Expires', RULE.date, { need: true, ph: 'MM/DD/YYYY', mode: 'numeric' }), page: filePick('The photo page', true) };
      it.node = h('div', null, grid(it.Country, it.Number, it.Issued, it.Expires), h('p.sub', null, 'The photo page: flat, in good light, all 4 corners in view.'), it.page.node); return it;
    }, 'Add another passport', true);
    const tt = { Ktn: line('Known Traveler Number', RULE.code(8, 10), { hint: 'From TSA PreCheck, Global Entry, NEXUS or SENTRI. PreCheck has no card: the number is what a booking takes.' }), Prog: line('Its program', null, { opts: ['TSA PreCheck', 'Global Entry', 'NEXUS', 'SENTRI'] }), KtnEnd: line('It expires', RULE.date, { ph: 'MM/DD/YYYY', mode: 'numeric' }), Redress: line('Redress number', RULE.code(6, 13), { hint: 'Only if you have one.' }) };
    const reach = { Mobile: line('Mobile', RULE.phone, { ac: you ? 'tel' : 'off', mode: 'tel', ph: '+1 917 555 0100' }), Email: line('Email', RULE.email, { ac: you ? 'email' : 'off', type: 'email' }),
      Seat: line('Seat', null, { opts: ['Window', 'Aisle', 'No preference'] }), Meal: line('Meal', null, { opts: ['No preference', 'Vegetarian', 'Vegan', 'Child meal'], hint: 'A meal for health or religion goes on each booking, never on file.' }) };
    F.details = { n, id, passports, tt, reach };
    F.sections.push(h('div.part', null, h('h3', null, 'The name, exactly as on ' + whose + ' passport'), grid(n.First, n.Middle, n.Last, n.Suffix), grid(id.Dob, id.Sex, id.Nat),
      h('h3', null, you ? 'Your passport' : p.name.split(' ')[0] + '\'s passport'), h('p.sub', null, 'Each one, for a dual citizen.'), passports.node,
      h('h3', null, 'Known Traveler and redress numbers'), grid(tt.Ktn, tt.Prog, tt.KtnEnd, tt.Redress),
      h('h3', null, 'To reach ' + (you ? 'you' : p.name.split(' ')[0]) + ' on a trip'), grid(reach.Mobile, reach.Email, reach.Seat, reach.Meal)));
  }
  if (p.parts.includes('visas')) {
    const visas = repeat(() => {
      const it = { Kind: line('Kind', null, { opts: ['Visa', 'Travel authorization'], need: true }), Country: line('Country it is for', RULE.text, { need: true }), Type: line('Which one', RULE.text, { hint: 'A visa\'s type, such as tourist or business; or the authorization, such as ESTA or the UK\'s ETA.' }),
        Number: line('Its number or reference', RULE.code(4, 20)), Issued: line('Issued or approved on', RULE.past, { ph: 'MM/DD/YYYY', mode: 'numeric' }), Expires: line('Valid until', RULE.date, { need: true, ph: 'MM/DD/YYYY', mode: 'numeric' }),
        Entries: line('Entries', null, { opts: ['Single', 'Double', 'Multiple'], hint: 'For a visa.' }), Pass: line('The passport it is in or tied to', RULE.code(5, 12), { hint: 'Its number. A new passport ends a travel authorization.' }), page: filePick('The visa page or the approval', false) };
      it.node = h('div', null, grid(it.Kind, it.Country, it.Type, it.Number, it.Issued, it.Expires, it.Entries, it.Pass), it.page.node); return it;
    }, 'Add another visa or authorization', false);
    F.visas = visas;
    F.sections.push(h('div.part', null, h('h3', null, 'Visas and travel authorizations'), h('p.sub', null, 'Each one ' + (you ? 'you hold' : p.name.split(' ')[0] + ' holds') + ' now, if any. Leave this empty if there are none.'), visas.node));
  }
  if (p.parts.includes('accounts')) {
    const accounts = repeat(() => {
      const it = { Program: line('Program', RULE.text, { need: true, hint: 'Such as United MileagePlus or World of Hyatt.' }), Member: line('Member number', RULE.member, { need: true }), Name: line('Name on the account', RULE.text, {}) };
      const keep = h('input', { type: 'checkbox' }); const user = line('Sign-in name', RULE.text, { hint: 'The email, username or member number it asks for.' }); const pw = line('Password', (v) => (v.length > 200 ? { err: 'That is longer than this line takes.' } : { v }), { type: 'password', ac: 'off' });
      const agree = h('input', { type: 'checkbox' }); const agreeErr = h('small.ferr', { role: 'alert', hidden: true });
      const signBox = h('div.signin', { hidden: true }, grid(user, pw), h('label.tick', null, agree, h('span', null, 'I agree that First Officer keeps this sign-in, sealed, to book in this account for me, until I take it back.')), agreeErr);
      keep.addEventListener('change', () => { signBox.hidden = !keep.checked; });
      Object.assign(it, { keep, user, pw, agree, agreeErr });
      it.node = h('div', null, grid(it.Program, it.Member, it.Name), h('label.tick', null, keep, h('span', null, 'Also give the sign-in for this account, so your advisor can book in it')), signBox); return it;
    }, 'Add another account', true);
    F.accounts = accounts;
    F.sections.push(h('div.part', null, h('h3', null, 'Airline and hotel accounts'), h('p.sub', null, 'A sign-in only if you choose to give it: never a bank\'s or a card\'s.'), accounts.node));
  }
  if (p.parts.includes('cards')) {
    const cards = repeat(() => {
      const it = { Whose: line('Whose card', null, { opts: ['The company\'s', 'Mine'], need: true }), Called: line('What you call it', RULE.text, { need: true, hint: 'Such as the business card.' }), Name: line('Name on the card', RULE.text, { need: true }),
        Last4: line('Last 4 digits', RULE.last4, { need: true, mode: 'numeric', max: 4 }), Exp: line('Expires', RULE.mmyy, { need: true, ph: 'MM/YY', mode: 'numeric' }),
        B1: line('Billing address, line 1', RULE.text, { need: true, ac: 'off' }), B2: line('Billing address, line 2', RULE.text, {}), City: line('City', RULE.text, { need: true }), State: line('State or region', RULE.region, {}), Zip: line('ZIP or postal code', RULE.zip, { need: true }), Country: line('Country', RULE.text, { need: true }) };
      it.node = h('div', null, grid(it.Whose, it.Called, it.Name, it.Last4, it.Exp), grid(it.B1, it.B2, it.City, it.State, it.Zip, it.Country)); return it;
    }, 'Add another card', true);
    F.cards = cards;
    F.sections.push(h('div.part', null, h('h3', null, 'Cards on file'), h('p.sub', null, 'Never the full number or the security code: those you send only for one booking, by a link of its own.'), cards.node));
  }
  F.node = h('section.card.person', { 'aria-label': p.name }, h('h2', null, p.name), F.sections);
  return F;
}
/** A row left wholly empty: an optional passport, visa, account or card not given, so it is skipped, not flagged. */
const blank = (it) => Object.values(it).every((x) => !x || !x.input || !String(x.input.value || '').trim()) && !(it.page && it.page.file) && !(it.keep && it.keep.checked);
/** One person's form, read and checked: { bad } or { body, files }. */
function readForm(F) {
  let bad = 0; const val = (x) => { const r = x.read(); if (r.bad) bad++; return r.v || ''; };
  const body = { v: 1, i: F.p.pid, details: null, passports: [], visas: [], accounts: [], cards: [] }; const files = [];
  if (F.details) {
    const { n, id, passports, tt, reach } = F.details;
    body.details = { 'First name': val(n.First), 'Middle name': val(n.Middle), 'Last name': val(n.Last), Suffix: val(n.Suffix), 'Date of birth': val(id.Dob), 'Sex (as on passport)': val(id.Sex), Nationality: val(id.Nat),
      'Known Traveler Number': val(tt.Ktn), 'KTN program': val(tt.Prog), 'KTN expires': val(tt.KtnEnd), 'Redress number': val(tt.Redress), Mobile: val(reach.Mobile), Email: val(reach.Email), Seat: val(reach.Seat), Meal: val(reach.Meal) };
    for (const it of passports.items) {
      if (blank(it)) continue;
      const v = { Country: val(it.Country), Number: val(it.Number), Issued: val(it.Issued), Expires: val(it.Expires) }; const pg = it.page.read(); if (pg.bad) bad++;
      if (v.Issued && v.Expires && parseD(v.Expires) <= parseD(v.Issued)) { it.Expires.err.textContent = 'It ends before it was issued.'; it.Expires.err.hidden = false; bad++; }
      const ref = 'f' + (files.length + 1); if (pg.file) files.push({ ref, file: pg.file, type: it.page.type, slot: 'passport' });
      body.passports.push(Object.assign(v, { file: pg.file ? ref : '' }));
    }
  }
  if (F.visas) for (const it of F.visas.items) {
    if (blank(it)) continue;
    const v = { Kind: val(it.Kind), Country: val(it.Country), Type: val(it.Type), Number: val(it.Number), Issued: val(it.Issued), Expires: val(it.Expires), Entries: val(it.Entries), 'In passport': val(it.Pass) }; const pg = it.page.read();
    const ref = 'f' + (files.length + 1); if (pg.file) files.push({ ref, file: pg.file, type: it.page.type, slot: 'auth' });
    body.visas.push(Object.assign(v, { file: pg.file ? ref : '' }));
  }
  if (F.accounts) for (const it of F.accounts.items) {
    if (blank(it)) continue;
    const v = { Program: val(it.Program), 'Member number': val(it.Member), 'Name on the account': val(it.Name), signin: null };
    if (it.keep.checked) {
      it.agreeErr.hidden = true;
      const u = it.user.input.value.trim(); const pw = it.pw.input.value;
      if (!u || !pw) { (u ? it.pw : it.user).err.textContent = 'Both the sign-in name and the password, or untick the box.'; (u ? it.pw : it.user).err.hidden = false; bad++; }
      else if (u.length > 120 || pw.length > 200) { it.user.err.textContent = 'That is longer than this line takes.'; it.user.err.hidden = false; bad++; }
      else if (!it.agree.checked) { it.agreeErr.textContent = 'Tick the box to give it, or untick the box above.'; it.agreeErr.hidden = false; bad++; }
      else v.signin = { u, p: pw, agreed: true };
    }
    body.accounts.push(v);
  }
  if (F.cards) for (const it of F.cards.items) {
    if (blank(it)) continue;
    const whose = val(it.Whose);
    body.cards.push({ 'Belongs to': whose === 'Mine' ? F.p.pid : whose ? 'The company' : '', Called: val(it.Called), 'Name on the card': val(it.Name), 'Last 4': val(it.Last4), Expires: val(it.Exp),
      'Billing line 1': val(it.B1), 'Billing line 2': val(it.B2), City: val(it.City), 'State or region': val(it.State), 'ZIP or postal code': val(it.Zip), Country: val(it.Country) });
  }
  return bad ? { bad } : { body, files };
}
function detailsStep() {
  const forms = people.map(personForm);
  const errEl = h('p.err', { role: 'alert', hidden: true });
  const go = h('button.btn.pk.wide', { type: 'button' }, 'Send it all');
  const bar = h('i'); const prog = h('p.prog', { hidden: true }, h('span', null, ''), h('span.bar', null, bar));
  go.addEventListener('click', async () => {
    if (S.busy) return;
    errEl.hidden = true;
    const read = forms.map(readForm);
    const bad = read.reduce((t, r) => t + (r.bad || 0), 0);
    if (bad) { errEl.textContent = plural(bad, 'line needs', 'lines need') + ' another look, marked above. Nothing was sent.'; errEl.hidden = false; const first = app.querySelector('.ferr:not([hidden])'); if (first) first.closest('label, div').scrollIntoView({ block: 'center' }); return; }
    S.busy = true; go.disabled = true; prog.hidden = false;
    const total = read.reduce((t, r) => t + 1 + r.files.length, 0); let done = 0;
    const step = (t) => { prog.firstChild.textContent = t; bar.style.width = Math.round((done / total) * 100) + '%'; };
    try {
      for (const [i, r] of read.entries()) {
        const p = forms[i].p;
        const counts = { passports: r.body.passports.length, visas: r.body.visas.length, accounts: r.body.accounts.length, signins: r.body.accounts.filter((a) => a.signin).length, cards: r.body.cards.length, files: r.files.length };
        step('Sealing and sending ' + p.name + '\'s details');
        await send({ t: 'details', l: L.link, i: p.pid, parts: p.parts, c: counts, a: new Date().toISOString() }, new TextEncoder().encode(JSON.stringify(r.body)));
        done++;
        for (const f of r.files) {
          step('Sealing and sending ' + f.file.name);
          await send({ t: 'doc', l: L.link, i: p.pid, s: f.slot, r: f.ref, n: f.file.name.slice(0, 120), y: f.type, z: f.file.size, a: new Date().toISOString() }, new Uint8Array(await f.file.arrayBuffer()));
          done++; step('Sent ' + f.file.name);
        }
        S.sent.push({ who: p.name, counts });
      }
      /* sent: this page keeps nothing of it */
      for (const F of forms) F.node.querySelectorAll('input').forEach((x) => { if (x.type !== 'checkbox' && x.type !== 'file') x.value = ''; });
      S.busy = false; doneStep(); focusTop();
    } catch (e) {
      S.busy = false; go.disabled = false; prog.hidden = true; errEl.textContent = (e.message || 'Not sent. Try again.') + ' What was sent before it stays sent.'; errEl.hidden = false;
    }
  });
  mount(head('Your consent', 'is recorded.', 'Now the details your advisor asked for. Type each one as it is on the document. Everything is sealed on this device before it is sent.'),
    steps('details'), forms.map((F) => F.node),
    h('section.card', null, errEl, prog, go,
      h('p.seal', null, sealIcon(), h('span', null, 'Once sent, nothing can be opened from this page again, not even by you. Only your First Officer advisor can open it. You can open this link again until ' + when(L.exp * 1000) + ' to send more.'))));
}

/* ---- a card, for one booking: its number and code, sealed, deleted once the ticket is issued ---- */
function cardStep() {
  const B = L.booking; const p = self;
  const name = line('Name on the card', RULE.text, { need: true, ac: 'cc-name' });
  const num = line('Card number', (v) => { const d = v.replace(/[\s-]/g, ''); if (!/^\d{13,19}$/.test(d) || !luhn(d)) return { err: 'That is not a whole card number. Check each digit.' }; if (d.slice(-4) !== B.last4) return { err: 'This card does not end in ' + B.last4 + ', the card this booking is for.' }; return { v: d }; }, { need: true, ac: 'cc-number', mode: 'numeric' });
  const exp = line('Expires', RULE.mmyy, { need: true, ac: 'cc-exp', ph: 'MM/YY', mode: 'numeric' });
  const cvc = line('Security code', (v) => (/^\d{3,4}$/.test(v) ? { v } : { err: 'The 3 or 4 digits on the card.' }), { need: true, ac: 'cc-csc', mode: 'numeric', max: 4 });
  const sig = h('input.fld', { type: 'text', autocomplete: 'name', autocapitalize: 'words', spellcheck: 'false' }); const tick = h('input', { type: 'checkbox' });
  const errEl = h('p.err', { role: 'alert', hidden: true }); const go = h('button.btn.pk.wide', { type: 'button' }, 'Authorize and send');
  const words = cardWords(B);
  go.addEventListener('click', async () => {
    if (S.busy) return;
    errEl.hidden = true; const say = (t) => { errEl.textContent = t; errEl.hidden = false; };
    const got = [name, num, exp, cvc].map((x) => x.read());
    if (got.some((r) => r.bad)) return say('A line needs another look, marked above. Nothing was sent.');
    const signer = sig.value.trim().replace(/\s+/g, ' ');
    if (signer.length < 3 || signer.length > 80) return say('Type your full name, as your signature.');
    if (!tick.checked) return say('Tick the box to authorize this card for this booking, or close this page.');
    S.busy = true; go.disabled = true; go.textContent = 'Recording your authorization';
    try {
      const fp = await sha256(words); const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      const j = await ledger({ kind: 'card', as: { [p.pid]: 'self' }, words: { version: CARD_VERSION, sha256: fp }, booking: B, device: { tz } }, 'authorization');
      go.textContent = 'Sealing and sending the card';
      const body = { kind: 'card', version: CARD_VERSION, words, sha256: fp, signer, booking: B, card: { name: got[0].v, number: got[1].v, exp: got[2].v, cvc: got[3].v }, ledger: { seq: j.seq, row_hash: j.row_hash, at: j.at }, device: { tz, lang: navigator.language || '', ua: navigator.userAgent.slice(0, 300) }, page: PAGE, link: L.link };
      await send({ t: 'card', l: L.link, i: p.pid, e: B.last4, a: new Date().toISOString() }, new TextEncoder().encode(JSON.stringify(body)), null, '-card');
      [name, num, exp, cvc].forEach((x) => x.clear()); body.card = null;
      S.sent.push({ who: p.name, card: B.last4 });
      S.busy = false; doneStep(); focusTop();
    } catch (e) { S.busy = false; go.disabled = false; go.textContent = 'Authorize and send'; say(e.message || 'That did not go through. Try again.'); }
  });
  mount(head('A card for', 'one booking.', [L.from ? h('b', null, 'For ' + L.from + '. ') : null, 'Your First Officer advisor asks for this card to pay the taxes and fees of one booking. It is sealed on this device before it leaves it, and deleted once the ticket is issued.']),
    steps('card'),
    h('section.card', { 'aria-labelledby': 'v-bk' }, h('h2', { id: 'v-bk' }, 'The booking'), h('dl.bk', null, h('dt', null, 'For'), h('dd', null, B.line), h('dt', null, 'Up to'), h('dd', null, '$' + Number(B.amount).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' in taxes, fees and carrier charges'), h('dt', null, 'The card'), h('dd', null, 'The one ending ' + B.last4)),
      h('p.lede', null, 'This link works until ' + when(L.exp * 1000) + '.')),
    h('section.card', { 'aria-labelledby': 'v-cd' }, h('h2', { id: 'v-cd' }, 'The card'), grid(name, num, exp, cvc),
      h('details.words', { open: true }, h('summary', null, 'What you authorize'), h('blockquote', null, h('p', null, words))),
      h('label.fl', null, h('span', null, 'Your full name'), sig, h('small.v', null, 'Typed as your signature.')), h('label.tick', null, tick, h('span', null, 'I authorize this card for this booking, as written above.')),
      errEl, go, h('p.seal', null, sealIcon(), h('span', null, 'Once sent, this page cannot show the card again. Your advisor opens it for this booking only.'))));
}

/* ---- step 3: done ---- */
function doneStep() {
  const said = (x) => x.card ? 'The card ending ' + x.card + ', for the booking' : [x.counts.passports ? plural(x.counts.passports, 'passport') : '', x.counts.visas ? plural(x.counts.visas, 'visa or authorization', 'visas or authorizations') : '', x.counts.accounts ? plural(x.counts.accounts, 'account') + (x.counts.signins ? ' (' + plural(x.counts.signins, 'sign-in') + ')' : '') : '', x.counts.cards ? plural(x.counts.cards, 'card') : '', x.counts.files ? plural(x.counts.files, 'page') : ''].filter(Boolean).join(', ') || 'their details';
  mount(head('Sent.', 'Thank you.', isBooking ? 'Your advisor has the card for this booking. It is deleted once the ticket is issued, and this page cannot show it again.' : 'Your First Officer advisor has them now. For your safety, this page cannot open them again, not even for you.'),
    steps('done'),
    h('section.card', { 'aria-labelledby': 'v-sent' }, h('h2', { id: 'v-sent' }, 'What you sent'),
      S.sent.length ? h('ul.sent', null, S.sent.map((x) => h('li', null, h('span', null, x.who, h('small', null, said(x)))))) : h('p.lede', null, 'Your consent, and nothing more yet.'),
      isBooking ? null : h('div.acts', null, h('button.btn.ghost.wide', { type: 'button', onclick: () => { detailsStep(); focusTop(); } }, 'Send more')),
      h('p.note', null, 'You can close this page. To see, correct or delete what First Officer keeps, or to take your consent back, write to ', mail(), '.')));
}

/* ---- a link that is not whole, or has ended ---- */
if (!L) mount(head('This link', 'is not complete.', 'Open it again from the message it came in. If it still says this, ask your First Officer advisor for a new one.'));
else if (L.exp * 1000 <= Date.now()) mount(head('This link', 'has ended.', 'For your safety, a link works for 7 days at most. Ask your First Officer advisor for a new one.'));
else if (isBooking) cardStep();
else consentStep();
window.addEventListener('hashchange', () => location.reload());
