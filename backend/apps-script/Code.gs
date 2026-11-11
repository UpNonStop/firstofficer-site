/** @OnlyCurrentDoc */
/**
 * First Officer: the Book application ("Call me back", book.html) and enterprise inquiries (enterprise.html, "Talk to our team").
 * v3, 10 Nov 2026. A Google Apps Script web app bound to the Google Sheet "First Officer - Call-me-back requests".
 *
 * The site POSTs one JSON body (Content-Type text/plain, so the browser sends it without a CORS preflight). Two kinds:
 *  - stage "draft": the Book form saves as the visitor types, once there is an email or a 10-digit phone.
 *    One row per visitor on the "Started" tab, updated in place by Request ID. No email.
 *  - anything else is a sent application: one row on "Requests", one themed email to the desk, and the visitor's
 *    "Started" row turns "Submitted". The visitor's themed confirmation goes out only if SEND_CONFIRMATION is true.
 * Two timed jobs, installed by setup():
 *  - hourlyTick: a visitor who started, typed an email and went quiet for NUDGE_AFTER_HOURS gets one themed
 *    "finish your application" email, only if SEND_NUDGE is true. Never twice, never after they sent it.
 *  - dailyDigest (8:00 ET): the desk gets the last day's starts that were not sent, if SEND_DIGEST is true.
 *    They did not tick consent to be called or texted, so the digest says to email them.
 *
 *  - Spam: the hidden "company_site" field (a honeypot people never see) and a form filled in under 2 seconds are
 *    dropped silently, with no row and no email. The same phone and email within 10 minutes is saved as "Repeat", no email.
 *  - Test rows: a first name or business starting with "TEST" is written as TEST and sends no email to anyone.
 *  - Cards: "Cards" keeps one line per bank, e.g. "Amex (business: Business Gold / personal: Gold Card)".
 *    "Business cards" and "Personal cards" list each picked card with its bank, from the form's wallet picker.
 *  - Cells that start with = + - @ are prefixed with ' so an answer can never run as a formula. Nothing goes to Google Analytics.
 */

// ---- settings --------------------------------------------------------------------------------------------------
// Where the desk email goes. Leave '' to send it to the Google account that deploys the script (the sheet's owner).
var NOTIFY_TO = '';
var DESK_REPLY_TO = 'desk@upnonstop.com';   // where a visitor's reply to our email lands
var SITE = 'https://firstofficer.upnonstop.com';
var SAVE_STARTED = true;        // keep a "Started" row for every visitor who starts the Book form (email or phone typed)
var SEND_CONFIRMATION = false;  // the visitor's themed confirmation when they send it
var SEND_NUDGE = false;         // one themed "finish your application" email to a visitor who started and went quiet
var NUDGE_AFTER_HOURS = 2;      // how long a start stays quiet before the nudge (it is never sent after 72 hours)
var SEND_DIGEST = true;         // a morning email to the desk: started, not sent
var SHEET_TAB = 'Requests';
var STARTED_TAB = 'Started';
var TZ = 'America/New_York';

var HEADERS = [
  'Timestamp (ET)', 'Name', 'Email', 'Phone', 'Business', 'Card spend a month', 'Trade',
  'Preferred time', 'Source page', 'UTM / referrer',
  'Status', 'Reference', 'Role', 'Confirm by', 'How soon', 'Cardholders', 'Points balance', 'Cards',
  'Spend lines', 'Goals', 'Trip', 'Notes', 'Heard about us', 'Consent text', 'Seconds to fill', 'Request ID',
  'Business cards', 'Personal cards'
];
var STARTED_HEADERS = [
  'First seen', 'Last update', 'Stage', 'Name', 'Email', 'Phone', 'Business', 'Trade', 'Card spend a month', 'Cards',
  'Answers filled', 'Page', 'UTM / referrer', 'Nudged', 'Request ID'
];

// ---- the web app -----------------------------------------------------------------------------------------------
function doPost(e) {
  var d;
  try {
    d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
  } catch (err) {
    return json_({ ok: false, error: 'bad_json' });
  }

  // Honeypot and speed check: answer "ok" so a bot learns nothing, but keep nothing.
  if (str_(d.company_site) || (Number(d.fill_ms) > 0 && Number(d.fill_ms) < 2000)) {
    return json_({ ok: true, ref: ref_(d) });
  }
  if (d.stage === 'draft') return draft_(d);

  // The five required answers, checked again here.
  if (!str_(d.first_name) || !str_(d.business) || str_(d.phone).replace(/\D/g, '').length < 10 ||
      !isEmail_(str_(d.email)) || !str_(d.tz) || d.consent !== true) {
    return json_({ ok: false, error: 'missing_fields' });
  }

  var isTest = test_(d);

  // The same phone and email again within 10 minutes (a double tap, or a correction) is still saved, marked "Repeat",
  // but sends no second email, so a flood cannot fill the inbox.
  var cache = CacheService.getScriptCache();
  var key = 'cb:' + str_(d.phone).replace(/\D/g, '') + ':' + str_(d.email).toLowerCase();
  var isRepeat = !isTest && !!cache.get(key);

  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  var row, when;
  try {
    var sh = tab_(SHEET_TAB, HEADERS);
    var m = d.meta || {};
    when = [list_(d.days), list_(d.times), tzName_(d.tz)].filter(String).join(' · ');
    row = [
      Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd HH:mm:ss'),
      [str_(d.first_name), str_(d.last_name)].filter(String).join(' '),
      str_(d.email), str_(d.phone), str_(d.business), str_(d.spend), str_(d.industry),
      when, str_(m.url || m.page), utm_(m),
      isTest ? 'TEST' : (isRepeat ? 'Repeat' : 'New'), ref_(d), str_(d.role), str_(d.confirm_by), str_(d.urgency),
      str_(d.cardholders), str_(d.points), list_(d.cards), list_(d.spend_lines), list_(d.goals),
      str_(d.trip), str_(d.notes), str_(d.heard), str_(d.consent_text),
      Math.round((Number(d.fill_ms) || 0) / 1000), str_(d.request_id),
      wallet_(d.wallet, 'business'), wallet_(d.wallet, 'personal')
    ].map(safe_);
    sh.appendRow(row);
    if (!isTest) cache.put(key, '1', 600);
    if (!enterprise_(d)) started_(d, 'Submitted');
  } finally {
    lock.releaseLock();
  }

  if (!isTest && !isRepeat) notify_(d, row, when);
  if (SEND_CONFIRMATION && !isTest && !isRepeat && !enterprise_(d)) confirm_(d, when);
  return json_({ ok: true, ref: ref_(d) });
}

// A GET just says the endpoint is alive (handy for checking the deploy). It reveals nothing.
function doGet() {
  return json_({ ok: true, service: 'First Officer call-me-back', version: 3, time_et: Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd HH:mm') });
}

// A save as you go: one "Started" row per visitor, updated in place. Needs an email or a 10-digit phone.
function draft_(d) {
  if (!SAVE_STARTED) return json_({ ok: true });
  if (!isEmail_(str_(d.email)) && str_(d.phone).replace(/\D/g, '').length < 10) return json_({ ok: false, error: 'too_early' });
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try { started_(d, 'Started'); } finally { lock.releaseLock(); }
  return json_({ ok: true });
}

function started_(d, stage) {
  var rid = str_(d.request_id);
  if (!rid || !SAVE_STARTED) return;
  var sh = tab_(STARTED_TAB, STARTED_HEADERS), C = cols_(STARTED_HEADERS), last = sh.getLastRow(), at = 0;
  if (last > 1) {
    var ids = sh.getRange(2, C['Request ID'] + 1, last - 1, 1).getValues();
    for (var i = ids.length - 1; i >= 0; i--) if (String(ids[i][0]) === rid) { at = i + 2; break; }
  }
  var now = new Date(), m = d.meta || {};
  var v = {
    'Last update': now, 'Stage': test_(d) ? 'TEST' : stage,
    'Name': [str_(d.first_name), str_(d.last_name)].filter(String).join(' '), 'Email': str_(d.email), 'Phone': str_(d.phone),
    'Business': str_(d.business), 'Trade': str_(d.industry), 'Card spend a month': str_(d.spend), 'Cards': list_(d.cards),
    'Answers filled': Number(d.filled) || '', 'Page': str_(m.url || m.page), 'UTM / referrer': utm_(m), 'Request ID': rid
  };
  if (at) {
    var cur = sh.getRange(at, 1, 1, STARTED_HEADERS.length).getValues()[0];
    if (cur[C['Stage']] === 'Submitted' && stage === 'Started') return;   // a late save after Send changes nothing
    STARTED_HEADERS.forEach(function (h, j) {
      if (!(h in v)) return;
      if (h === 'Stage' || h === 'Last update' || v[h] !== '') cur[j] = safe_(v[h]);
    });
    sh.getRange(at, 1, 1, cur.length).setValues([cur]);
  } else {
    sh.appendRow(STARTED_HEADERS.map(function (h) { return h === 'First seen' ? now : (h in v ? safe_(v[h]) : ''); }));
  }
}

// ---- timed jobs (setup() installs them) ------------------------------------------------------------------------
function hourlyTick() {
  if (!SEND_NUDGE || !SAVE_STARTED) return;
  var sh = tab_(STARTED_TAB, STARTED_HEADERS), C = cols_(STARTED_HEADERS), last = sh.getLastRow();
  if (last < 2) return;
  var rows = sh.getRange(2, 1, last - 1, STARTED_HEADERS.length).getValues(), sent = sentEmails_(), now = Date.now();
  rows.forEach(function (r, i) {
    var email = str_(r[C['Email']]).toLowerCase(), age = now - new Date(r[C['Last update']]).getTime();
    if (r[C['Stage']] !== 'Started' || r[C['Nudged']] || !isEmail_(email) || sent[email]) return;
    if (!(age >= NUDGE_AFTER_HOURS * 3600e3 && age <= 72 * 3600e3)) return;
    nudge_(str_(r[C['Name']]).split(' ')[0], email);
    sh.getRange(i + 2, C['Nudged'] + 1).setValue(new Date());
  });
}

function dailyDigest() {
  if (!SEND_DIGEST || !SAVE_STARTED) return;
  var to = NOTIFY_TO || Session.getEffectiveUser().getEmail();
  if (!to) return;
  var sh = tab_(STARTED_TAB, STARTED_HEADERS), C = cols_(STARTED_HEADERS), last = sh.getLastRow();
  if (last < 2) return;
  var since = Date.now() - 24 * 3600e3, sent = sentEmails_();
  var list = sh.getRange(2, 1, last - 1, STARTED_HEADERS.length).getValues().filter(function (r) {
    return r[C['Stage']] === 'Started' && new Date(r[C['Last update']]).getTime() >= since && !sent[str_(r[C['Email']]).toLowerCase()];
  });
  if (!list.length) return;   // a quiet day sends nothing
  var n = list.length, subject = 'Started, not sent: ' + n + (n === 1 ? ' application' : ' applications') + ' since yesterday';
  MailApp.sendEmail({ to: to, subject: subject, htmlBody: digestHtml_(list, C), body: digestText_(list, C), name: 'First Officer site' });
}

/** Run once from the editor (Run > setup): creates both tabs' titles, asks for permissions and installs the two timed jobs. */
function setup() {
  tab_(SHEET_TAB, HEADERS);
  tab_(STARTED_TAB, STARTED_HEADERS);
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (['hourlyTick', 'dailyDigest'].indexOf(t.getHandlerFunction()) >= 0) ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('hourlyTick').timeBased().everyHours(1).create();
  ScriptApp.newTrigger('dailyDigest').timeBased().atHour(8).everyDays(1).inTimezone(TZ).create();
  Logger.log('Ready. Desk emails go to ' + (NOTIFY_TO || Session.getEffectiveUser().getEmail()) +
    '. Confirmation ' + (SEND_CONFIRMATION ? 'on' : 'off') + ', nudge ' + (SEND_NUDGE ? 'on' : 'off') + ', digest ' + (SEND_DIGEST ? 'on' : 'off') + '.');
}

// ---- the four themed emails ------------------------------------------------------------------------------------
// One look for all four: cream page, beige card, pink accents, the logo from the site, Georgia for the big line.
function notify_(d, row, when) {
  var to = NOTIFY_TO || Session.getEffectiveUser().getEmail();
  if (!to) return;
  var ent = enterprise_(d), name = row[1], phone = phone_(d.phone), digits = str_(d.phone).replace(/\D/g, '');
  var subject = (ent ? 'Enterprise: ' : 'Call-me-back: ') + name + ', ' + row[4] + (row[5] ? ' (' + row[5] + ')' : '');
  var wa = 'https://wa.me/' + (digits.length === 10 ? '1' + digits : digits);
  var html = shell_(
    '<tr><td style="padding:22px 28px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>' +
      kicker_(ent ? 'New enterprise inquiry' : 'New application') + '</td><td align="right" style="font:700 12px/1 \'Courier New\',monospace;color:#6E6776">' + h_(ref_(d)) + '</td></tr></table>' +
    '<div style="font:400 30px/1.15 Georgia,\'Times New Roman\',serif;color:#141216;margin:12px 0 4px">' + h_(name) + '</div>' +
    '<div style="font:15px/1.45 Helvetica,Arial,sans-serif;color:#4A4550">' + h_([str_(d.role), str_(d.business)].filter(String).join(', ')) + '</div>' +
    '<div style="margin-top:16px">' + button_('tel:' + (digits.length === 10 ? '+1' + digits : '+' + digits), 'Call ' + phone, '#FA1896', '#FFFFFF') +
      button_(wa, 'WhatsApp', '#25D366', '#FFFFFF') + button_('mailto:' + str_(d.email), 'Email', '#FBF7EF', '#141216', '#D9CCB4') + '</div></td></tr>' +
    block_('Call window', [['When', when], ['How soon', d.urgency], ['Confirm by', d.confirm_by]]) +
    block_('Contact', [['Mobile', phone], ['Email', d.email], ['Business', d.business], ['Role', d.role]]) +
    block_('Business', [['Trade', d.industry], ['Card spend', d.spend], ['People with cards', d.cardholders], ['Points on hand', d.points], ['Spend goes to', list_(d.spend_lines)]]) +
    block_('Wallet', [['Business cards', wallet_(d.wallet, 'business')], ['Personal cards', wallet_(d.wallet, 'personal')], ['By bank', list_(d.cards)]]) +
    block_('What they want', [['Pillars', list_(d.goals)], ['Trip in mind', d.trip], ['Notes', d.notes], ['Heard from', d.heard]]) +
    block_('Where they came from', [['Page', row[8]], ['UTM / referrer', row[9]], ['Time to fill', row[24] ? row[24] + 's' : '']]) +
    '<tr><td style="padding:18px 28px 0;font:14px/1.5 Helvetica,Arial,sans-serif;color:#4A4550">Reply to reach ' + h_(d.email) +
      ' directly. <a href="' + h_(SpreadsheetApp.getActiveSpreadsheet().getUrl()) + '" style="color:#A30D5C;font-weight:700">Open the sheet</a></td></tr>',
    (ent ? 'Enterprise inquiry from ' : 'Application from ') + name);
  var lines = [];
  for (var i = 0; i < HEADERS.length; i++) if (row[i] !== '' && row[i] !== null) lines.push(HEADERS[i] + ': ' + row[i]);
  var body = (ent ? 'New enterprise inquiry' : 'New call-me-back request') + ' from firstofficer.upnonstop.com\n\n' + lines.join('\n') +
    '\n\nSheet: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl();
  MailApp.sendEmail({ to: to, subject: subject, body: body, htmlBody: html, replyTo: str_(d.email), name: 'First Officer site' });
}

// The visitor's confirmation, only when SEND_CONFIRMATION is true. From the deploying account, reply-to the desk.
function confirm_(d, when) {
  var first = str_(d.first_name), to = str_(d.email);
  if (!first || !to) return;
  var by = { 'Text message': 'text message', 'Email': 'email', 'WhatsApp': 'WhatsApp' }[str_(d.confirm_by)] || 'text message';
  var win = window_(d);
  var callLine = 'We will call ' + phone_(d.phone) + ' ' + (win ? win + ', ' : 'at a time that suits you, ') + tzName_(d.tz) + '. We confirm the exact time with you first, by ' + by + '.';
  var steps = [
    ['Within one business day', 'We confirm the time by ' + by + '.'],
    ['The call, twenty minutes, free', 'Where your card spend goes and what it already earns. Last month\'s card statements help, or a rough split of where the spend goes. No card login needed.'],
    ['Our recommendation', 'In dollars: what the desk could find, est., and whether it clears the $550 monthly fee.'],
    ['Your call', 'Say yes and the desk opens, month to month. Say no and you keep the recommendation.']
  ];
  var html = shell_(
    '<tr><td style="padding:22px 28px 0">' + kicker_('Application received') +
    '<div style="font:400 30px/1.15 Georgia,\'Times New Roman\',serif;color:#141216;margin:12px 0 0">Thanks, ' + h_(first) + '.<br><span style="color:#FA1896">We have your request.</span></div>' +
    '<p style="font:16px/1.55 Helvetica,Arial,sans-serif;color:#4A4550;margin:14px 0 0">' + h_(callLine) + '</p></td></tr>' +
    '<tr><td style="padding:20px 28px 0"><div style="background:#EAE0CE;border-radius:14px;padding:16px 18px 6px">' + kicker_('What happens next') + '<div style="height:12px"></div>' +
      steps.map(function (s, k) { return step_('0' + (k + 1), s[0], s[1]); }).join('') + '</div></td></tr>' +
    '<tr><td style="padding:18px 28px 0;font:15px/1.55 Helvetica,Arial,sans-serif;color:#4A4550">Need to change something? Reply to this email, or ' +
      '<a href="https://wa.me/16199404040" style="color:#0E6B35;font-weight:700">message us on WhatsApp</a> at +1 619 940 4040.' +
      '<div style="margin-top:16px;color:#141216">The desk at First Officer</div><div style="margin-top:4px;font:12px/1.4 \'Courier New\',monospace;color:#6E6776">Reference ' + h_(ref_(d)) + '</div></td></tr>',
    'We will call you ' + (win || 'at a time that suits you') + '. Reference ' + ref_(d) + '.',
    'You are getting this because you asked for a call at firstofficer.upnonstop.com.');
  var body = ['Thanks, ' + first + '. We have your request.', '', callLine, '', 'What happens next']
    .concat(steps.map(function (s, k) { return '0' + (k + 1) + ' ' + s[0] + ': ' + s[1]; }))
    .concat(['', 'Need to change something? Reply to this email, or message us on WhatsApp at +1 619 940 4040.', '', 'The desk at First Officer', 'Reference ' + ref_(d), '',
      'First Officer by UpNonStop is a points and rewards advisory service, not a licensed financial advisor. Figures are estimates, not guarantees.',
      'UpNonStop LLC | 235 Pavonia Avenue | Jersey City, NJ 07302', 'You are getting this because you asked for a call at firstofficer.upnonstop.com.']).join('\n');
  MailApp.sendEmail({ to: to, subject: 'Got it, ' + first + ': your call request is in', body: body, htmlBody: html, replyTo: DESK_REPLY_TO, name: 'First Officer' });
}

// One "finish your application" email, only when SEND_NUDGE is true (hourlyTick decides who).
function nudge_(first, to) {
  var hi = first ? 'Hi ' + first + ',' : 'Hi there,', link = SITE + '/book.html#callback';
  var html = shell_(
    '<tr><td style="padding:22px 28px 0">' + kicker_('Your application') +
    '<div style="font:400 30px/1.15 Georgia,\'Times New Roman\',serif;color:#141216;margin:12px 0 0">Your Found Money Call,<br><span style="color:#FA1896">half done.</span></div>' +
    '<p style="font:16px/1.55 Helvetica,Arial,sans-serif;color:#4A4550;margin:14px 0 0">' + h_(hi) + ' you started an application for the Found Money Call and stopped partway. ' +
      'It takes about two more minutes. On the device you used, your answers are still there.</p>' +
    '<div style="margin:20px 0 4px">' + button_(link, 'Finish my application', '#FA1896', '#FFFFFF') + '</div>' +
    '<p style="font:15px/1.55 Helvetica,Arial,sans-serif;color:#4A4550;margin:10px 0 0">The call is free and takes twenty minutes: where your card spend goes, ' +
      'what it already earns, and what the desk could find, in dollars, est.</p>' +
    '<p style="font:15px/1.55 Helvetica,Arial,sans-serif;color:#4A4550;margin:14px 0 0">Not for you? Ignore this email. It is the only one we send about it.</p>' +
    '<div style="margin-top:16px;font:15px/1.55 Helvetica,Arial,sans-serif;color:#141216">The desk at First Officer</div></td></tr>',
    'About two more minutes to finish. Your answers are still there.',
    'You are getting this one email because you started an application at firstofficer.upnonstop.com.');
  var body = [hi, '', 'You started an application for the Found Money Call and stopped partway. It takes about two more minutes. On the device you used, your answers are still there.', '',
    'Finish my application: ' + link, '', 'The call is free and takes twenty minutes: where your card spend goes, what it already earns, and what the desk could find, in dollars, est.', '',
    'Not for you? Ignore this email. It is the only one we send about it.', '', 'The desk at First Officer', '',
    'First Officer by UpNonStop is a points and rewards advisory service, not a licensed financial advisor.', 'UpNonStop LLC | 235 Pavonia Avenue | Jersey City, NJ 07302',
    'You are getting this one email because you started an application at firstofficer.upnonstop.com.'].join('\n');
  MailApp.sendEmail({ to: to, subject: 'Your Found Money Call application is half done', body: body, htmlBody: html, replyTo: DESK_REPLY_TO, name: 'First Officer' });
}

function digestHtml_(list, C) {
  var cards = list.map(function (r) {
    var em = str_(r[C['Email']]);
    return '<div style="background:#EAE0CE;border-radius:14px;padding:14px 16px;margin:0 0 10px">' +
      '<div style="font:700 16px/1.3 Helvetica,Arial,sans-serif;color:#141216">' + h_(str_(r[C['Name']]) || 'No name yet') +
        (str_(r[C['Business']]) ? '<span style="font-weight:500;color:#4A4550">, ' + h_(r[C['Business']]) + '</span>' : '') + '</div>' +
      '<div style="font:14px/1.5 Helvetica,Arial,sans-serif;color:#4A4550;margin-top:4px">' +
        (em ? '<a href="mailto:' + h_(em) + '" style="color:#A30D5C;font-weight:700">' + h_(em) + '</a>' : 'No email') +
        (str_(r[C['Phone']]) ? ' · ' + h_(phone_(r[C['Phone']])) : '') + '</div>' +
      '<div style="font:13px/1.5 Helvetica,Arial,sans-serif;color:#6E6776;margin-top:4px">' +
        h_([str_(r[C['Trade']]), str_(r[C['Card spend a month']]), str_(r[C['Cards']])].filter(String).join(' · ') || 'Few answers yet') +
        ' · ' + h_(r[C['Answers filled']] || 0) + ' answers · last seen ' + h_(Utilities.formatDate(new Date(r[C['Last update']]), TZ, 'MMM d, h:mm a')) + ' ET' +
        (r[C['Nudged']] ? ' · nudged' : '') + '</div></div>';
  }).join('');
  return shell_(
    '<tr><td style="padding:22px 28px 0">' + kicker_('Started, not sent') +
    '<div style="font:400 30px/1.15 Georgia,\'Times New Roman\',serif;color:#141216;margin:12px 0 0">' + list.length + (list.length === 1 ? ' person' : ' people') +
      ' started<br><span style="color:#FA1896">and did not press Send.</span></div>' +
    '<p style="font:15px/1.55 Helvetica,Arial,sans-serif;color:#4A4550;margin:14px 0 18px">They did not tick consent to be called or texted, so reach them by email. ' +
      'All of them are on the Started tab.</p>' + cards +
    '<a href="' + h_(SpreadsheetApp.getActiveSpreadsheet().getUrl()) + '" style="font:700 14px/1.5 Helvetica,Arial,sans-serif;color:#A30D5C">Open the sheet</a></td></tr>',
    list.length + ' started the application and did not send it.');
}
function digestText_(list, C) {
  return ['Started, not sent, in the last day (email only: they did not tick consent to be called or texted):', '']
    .concat(list.map(function (r) {
      return '- ' + [str_(r[C['Name']]) || 'No name yet', str_(r[C['Business']]), str_(r[C['Email']]), phone_(r[C['Phone']]), str_(r[C['Trade']]),
        str_(r[C['Card spend a month']]), (r[C['Answers filled']] || 0) + ' answers'].filter(String).join(' · ');
    })).concat(['', 'Sheet: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl()]).join('\n');
}

// ---- the email look --------------------------------------------------------------------------------------------
function shell_(inner, preheader, why) {
  return '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"></head>' +
    '<body style="margin:0;padding:0;background:#FAF6EE">' +
    (preheader ? '<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:#FAF6EE">' + h_(preheader) + '</div>' : '') +
    '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FAF6EE"><tr><td align="center" style="padding:28px 12px">' +
    '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:600px;background:#F3ECDF;border:1px solid #E2D7C4;border-radius:18px">' +
    '<tr><td style="padding:24px 28px 0"><table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="padding-right:10px"><img src="' + SITE + '/logo-128.png" width="36" height="36" alt="First Officer" style="display:block;border:0"></td>' +
      '<td><div style="font:800 17px/1.1 Helvetica,Arial,sans-serif;color:#141216">First Officer</div><div style="font:500 12px/1.3 Helvetica,Arial,sans-serif;color:#6E6776">by UpNonStop&trade;</div></td></tr></table></td></tr>' +
    inner +
    '<tr><td style="padding:22px 28px 26px"><div style="border-top:1px solid #E2D7C4;padding-top:14px;font:12px/1.55 Helvetica,Arial,sans-serif;color:#7A7280">' +
      'First Officer by UpNonStop is a points and rewards advisory service, not a licensed financial advisor. Figures are estimates, not guarantees.<br>' +
      'UpNonStop LLC | 235 Pavonia Avenue | Jersey City, NJ 07302' + (why ? '<br>' + h_(why) : '') + '</div></td></tr>' +
    '</table></td></tr></table></body></html>';
}
function kicker_(t) { return '<div style="font:700 11px/1 \'Courier New\',monospace;letter-spacing:.14em;text-transform:uppercase;color:#A30D5C">' + h_(t) + '</div>'; }
function button_(href, label, bg, fg, border) {
  return '<a href="' + h_(href) + '" style="display:inline-block;margin:0 8px 8px 0;padding:12px 18px;border-radius:999px;background:' + bg + ';color:' + fg +
    ';border:1.5px solid ' + (border || bg) + ';font:700 14px/1 Helvetica,Arial,sans-serif;text-decoration:none">' + h_(label) + '</a>';
}
function block_(title, pairs) {
  var rows = pairs.filter(function (p) { return str_(p[1]) !== ''; }).map(function (p) {
    return '<tr><td width="124" style="width:124px;padding:6px 12px 6px 0;vertical-align:top;font:12px/1.45 Helvetica,Arial,sans-serif;color:#6E6776">' + h_(p[0]) +
      '</td><td style="padding:6px 0;vertical-align:top;font:14px/1.45 Helvetica,Arial,sans-serif;color:#141216;word-break:break-word">' + h_(p[1]) + '</td></tr>';
  }).join('');
  return rows ? '<tr><td style="padding:16px 28px 0"><div style="background:#EAE0CE;border-radius:14px;padding:14px 16px 8px">' + kicker_(title) +
    '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="table-layout:fixed;margin-top:6px">' + rows + '</table></div></td></tr>' : '';
}
function step_(n, title, text) {
  return '<table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 0 12px"><tr><td style="vertical-align:top;padding-right:12px">' +
    '<div style="width:28px;height:28px;border-radius:8px;border:1.5px solid #FA1896;background:#FBF7EF;color:#A30D5C;font:700 12px/28px \'Courier New\',monospace;text-align:center">' + n + '</div></td>' +
    '<td style="vertical-align:top"><div style="font:700 15px/1.35 Helvetica,Arial,sans-serif;color:#141216">' + h_(title) + '</div>' +
    '<div style="font:15px/1.5 Helvetica,Arial,sans-serif;color:#4A4550;margin-top:2px">' + h_(text) + '</div></td></tr></table>';
}

// ---- helpers ---------------------------------------------------------------------------------------------------
function tab_(name, headers) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(name) || ss.insertSheet(name);
  if (sh.getLastRow() === 0) {
    sh.appendRow(headers);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, headers.length).setFontWeight('bold');
  } else if (sh.getLastColumn() < headers.length) {
    // A tab made by an older version: add the new column titles at the end; earlier rows keep their cells.
    var from = sh.getLastColumn() + 1;
    sh.getRange(1, from, 1, headers.length - from + 1).setValues([headers.slice(from - 1)]).setFontWeight('bold');
  }
  return sh;
}
function cols_(headers) { var o = {}; headers.forEach(function (h, i) { o[h] = i; }); return o; }
// Emails that already sent an application, so nobody who sent it gets a nudge or lands in the digest.
function sentEmails_() {
  var sh = tab_(SHEET_TAB, HEADERS), last = sh.getLastRow(), o = {};
  if (last < 2) return o;
  sh.getRange(2, HEADERS.indexOf('Email') + 1, last - 1, 1).getValues().forEach(function (r) { var e = str_(r[0]).toLowerCase(); if (e) o[e] = true; });
  return o;
}
// The picked cards of one line, each with its bank: "Amex Business Gold, Chase Ink Business Preferred".
function wallet_(w, line) {
  if (!Array.isArray(w)) return '';
  return w.filter(function (x) { return x && x.line === line && str_(x.card); })
    .map(function (x) { var b = str_(x.issuer), c = str_(x.card); return c.indexOf(b) === 0 ? c : b + ' ' + c; })
    .join(', ');
}
function utm_(m) {
  var utm = m.utm || {}, t = Object.keys(utm).map(function (k) { return k + '=' + utm[k]; }).join('&');
  if (m.referrer) t += (t ? ' | ' : '') + 'referrer ' + m.referrer;
  var ft = m.first_touch || {};
  if (ft && Object.keys(ft).length) t += (t ? ' | ' : '') + 'first touch ' + JSON.stringify(ft);
  return t;
}
// "(201) 555-0123" for a US number, as typed otherwise.
function phone_(v) {
  var raw = str_(v), d = raw.replace(/\D/g, '');
  if (d.length === 11 && d.charAt(0) === '1') d = d.slice(1);
  return d.length === 10 ? '(' + d.slice(0, 3) + ') ' + d.slice(3, 6) + '-' + d.slice(6) : raw;
}
// The call window as the page says it: "on Tue or Thu, morning".
function window_(d) {
  var or = function (a) { return a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + ' or ' + a[a.length - 1]; };
  var days = Array.isArray(d.days) ? d.days.map(str_).filter(String) : [], times = Array.isArray(d.times) ? d.times.map(function (t) { return str_(t).split(',')[0].toLowerCase(); }).filter(String) : [];
  return [days.length ? 'on ' + or(days) : '', or(times)].filter(String).join(', ');
}
function enterprise_(d) { return /^enterprise/.test(str_((d.meta || {}).form)); }
function test_(d) { return /^TEST/i.test(str_(d.first_name)) || /^TEST/i.test(str_(d.business)); }
function isEmail_(v) { return /^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(v); }
function ref_(d) { return 'FO-' + str_(d.request_id).replace(/[^a-z0-9]/gi, '').slice(0, 8).toUpperCase(); }
function str_(v) { return v === undefined || v === null ? '' : String(v).trim().slice(0, 1000); }
function list_(v) { return Array.isArray(v) ? v.map(str_).filter(String).join(', ') : str_(v); }
function safe_(v) { return typeof v === 'string' && /^[=+\-@]/.test(v) ? "'" + v : v; }
function h_(v) { return String(v === undefined || v === null ? '' : v).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
function tzName_(v) {
  var m = { 'America/New_York': 'Eastern', 'America/Chicago': 'Central', 'America/Denver': 'Mountain',
    'America/Phoenix': 'Arizona', 'America/Los_Angeles': 'Pacific', 'America/Anchorage': 'Alaska', 'Pacific/Honolulu': 'Hawaii' };
  return m[v] ? m[v] + ' time' : str_(v);
}
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
