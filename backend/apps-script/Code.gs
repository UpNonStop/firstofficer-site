/** @OnlyCurrentDoc */
/**
 * First Officer, "Call me back" requests (book.html, option four).
 *
 * A Google Apps Script web app bound to the Google Sheet "First Officer - Call-me-back requests".
 * The site's form POSTs one JSON body (Content-Type text/plain, so the browser sends it without a CORS preflight).
 * Each real request becomes one row on the "Requests" tab and one email to the desk.
 *
 *  - Spam: the hidden "company_site" field (a honeypot people never see) and a form filled in under 2 seconds are
 *    dropped silently, with no row and no email. The same phone and email within 10 minutes is saved as "Repeat", no email.
 *  - Test rows: a request whose first name or business starts with "TEST" is written with "TEST" in the Status
 *    column and does NOT send the desk email, so trying the form never fills the inbox.
 *  - Nothing here sends anything to the visitor. Nothing goes to Google Analytics.
 *  - Cells that start with = + - @ are prefixed with ' so a request can never run as a formula in the sheet.
 */

// Where the desk email goes. Leave '' to send it to the Google account that deploys the script (the sheet's owner).
var NOTIFY_TO = '';
var SHEET_TAB = 'Requests';
var TZ = 'America/New_York';

var HEADERS = [
  'Timestamp (ET)', 'Name', 'Email', 'Phone', 'Business', 'Card spend a month', 'Trade',
  'Preferred time', 'Source page', 'UTM / referrer',
  'Status', 'Reference', 'Role', 'Confirm by', 'How soon', 'Cardholders', 'Points balance', 'Cards',
  'Spend lines', 'Goals', 'Trip', 'Notes', 'Heard about us', 'Consent text', 'Seconds to fill', 'Request ID'
];

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
  // The five required answers, checked again here.
  if (!str_(d.first_name) || !str_(d.business) || str_(d.phone).replace(/\D/g, '').length < 10 ||
      !/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(str_(d.email)) || !str_(d.tz) || d.consent !== true) {
    return json_({ ok: false, error: 'missing_fields' });
  }

  var isTest = /^TEST/i.test(str_(d.first_name)) || /^TEST/i.test(str_(d.business));

  // The same phone and email again within 10 minutes (a double tap, or a correction) is still saved, marked "Repeat",
  // but sends no second email, so a flood cannot fill the inbox.
  var cache = CacheService.getScriptCache();
  var key = 'cb:' + str_(d.phone).replace(/\D/g, '') + ':' + str_(d.email).toLowerCase();
  var isRepeat = !isTest && !!cache.get(key);

  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var sh = sheet_();
    var m = d.meta || {};
    var utm = m.utm || {};
    var utmText = Object.keys(utm).map(function (k) { return k + '=' + utm[k]; }).join('&');
    if (m.referrer) utmText += (utmText ? ' | ' : '') + 'referrer ' + m.referrer;
    var ft = m.first_touch || {};
    if (ft && Object.keys(ft).length) utmText += (utmText ? ' | ' : '') + 'first touch ' + JSON.stringify(ft);

    var when = [list_(d.days), list_(d.times), tzName_(d.tz)].filter(String).join(' · ');
    var row = [
      Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd HH:mm:ss'),
      [str_(d.first_name), str_(d.last_name)].filter(String).join(' '),
      str_(d.email), str_(d.phone), str_(d.business), str_(d.spend), str_(d.industry),
      when, str_(m.url || m.page), utmText,
      isTest ? 'TEST' : (isRepeat ? 'Repeat' : 'New'), ref_(d), str_(d.role), str_(d.confirm_by), str_(d.urgency),
      str_(d.cardholders), str_(d.points), list_(d.cards), list_(d.spend_lines), list_(d.goals),
      str_(d.trip), str_(d.notes), str_(d.heard), str_(d.consent_text),
      Math.round((Number(d.fill_ms) || 0) / 1000), str_(d.request_id)
    ].map(safe_);
    sh.appendRow(row);
    if (!isTest) cache.put(key, '1', 600);
  } finally {
    lock.releaseLock();
  }

  if (!isTest && !isRepeat) notify_(d, row, when);
  return json_({ ok: true, ref: ref_(d) });
}

// A GET just says the endpoint is alive (handy for checking the deploy). It reveals nothing.
function doGet() {
  return json_({ ok: true, service: 'First Officer call-me-back', time_et: Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd HH:mm') });
}

function notify_(d, row, when) {
  var to = NOTIFY_TO || Session.getEffectiveUser().getEmail();
  if (!to) return;
  var name = row[1], subject = 'Call-me-back: ' + name + ', ' + row[4] + (row[5] ? ' (' + row[5] + ')' : '');
  var lines = [];
  for (var i = 0; i < HEADERS.length; i++) if (row[i] !== '' && row[i] !== null) lines.push(HEADERS[i] + ': ' + row[i]);
  var body = 'New call-me-back request from firstofficer.upnonstop.com\n\n' + lines.join('\n') +
    '\n\nSheet: ' + SpreadsheetApp.getActiveSpreadsheet().getUrl();
  MailApp.sendEmail({ to: to, subject: subject, body: body, replyTo: str_(d.email), name: 'First Officer site' });
}

function sheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET_TAB) || ss.insertSheet(SHEET_TAB);
  if (sh.getLastRow() === 0) {
    sh.appendRow(HEADERS);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
  }
  return sh;
}

function ref_(d) { return 'FO-' + str_(d.request_id).replace(/[^a-z0-9]/gi, '').slice(0, 8).toUpperCase(); }
function str_(v) { return v === undefined || v === null ? '' : String(v).trim().slice(0, 1000); }
function list_(v) { return Array.isArray(v) ? v.map(str_).filter(String).join(', ') : str_(v); }
function safe_(v) { return typeof v === 'string' && /^[=+\-@]/.test(v) ? "'" + v : v; }
function tzName_(v) {
  var m = { 'America/New_York': 'Eastern', 'America/Chicago': 'Central', 'America/Denver': 'Mountain',
    'America/Phoenix': 'Arizona', 'America/Los_Angeles': 'Pacific', 'America/Anchorage': 'Alaska', 'Pacific/Honolulu': 'Hawaii' };
  return m[v] ? m[v] + ' time' : str_(v);
}
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/** Run once from the editor (Run > setup) to create the header row and grant permissions before deploying. */
function setup() { var sh = sheet_(); sh.setFrozenRows(1); sh.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold'); Logger.log('Ready. Desk emails go to ' + (NOTIFY_TO || Session.getEffectiveUser().getEmail())); }
