# First Officer call-me-back backend: deploy in 5 steps (about 5 minutes)

The sheet already exists in your Drive, with the header row in place:
**First Officer - Call-me-back requests**
https://docs.google.com/spreadsheets/d/1g1ZqWfkf8WnenG7cFe5yWhRMgCaVLnCFnFhhutm2jac/edit

1. **Open the script editor from the sheet.** In the sheet: Extensions > Apps Script. A project bound to this sheet opens.
2. **Paste the two files.** Replace everything in `Code.gs` with this folder's `Code.gs`. Then Project Settings (gear) >
   tick "Show appsscript.json manifest file in editor", open `appsscript.json` and replace it with this folder's `appsscript.json`.
   Save (Ctrl/Cmd+S). Optional: set `NOTIFY_TO` at the top of Code.gs to the address that should get each request
   (left empty, it goes to the Google account you are signed in with).
3. **Run setup once to grant permissions.** Pick `setup` in the function menu, click Run, then Review permissions >
   your account > Advanced > Go to project (unsafe) > Allow. Google asks because the script is yours and unverified; it asks
   for: this spreadsheet only, sending email as you, and your email address. The log should say "Ready".
4. **Deploy as a web app.** Deploy > New deployment > gear > Web app. Description "callback v1",
   Execute as **Me**, Who has access **Anyone**. Deploy, and copy the **Web app URL** (it ends in `/exec`).
   Check it: open the URL in a browser; it should show `{"ok":true,"service":"First Officer call-me-back",...}`.
5. **Put the URL in the site.** In `assets/fo-callback.js` on PR #41 (branch fix/book-callback-rebased-2026-10-31), set
   `var CALLBACK_ENDPOINT='https://script.google.com/macros/s/.../exec';` (line 9), commit, and merge #41 when you are ready
   (or paste the URL to Claude and it commits it). Until it is set, the form still works: its Send button
   hands the same answers to email instead.

**Trying it safely:** put `TEST` at the start of the first name or the business name. That request is written to the
sheet with `TEST` in the Status column and sends no email. Delete TEST rows whenever you like.

**v3, 10 Nov 2026 (answers save as you go, themed emails):** paste the new `Code.gs`, then **Run > setup once** (it asks for one
new permission, to run the two timed jobs), then Deploy > Manage deployments > pencil > Version: New version > Deploy. Same `/exec` URL.
- A new **Started** tab: one row per visitor who starts the Book form and types an email or phone, updated as they go (Stage Started,
  then Submitted when they send it). Switch: `SAVE_STARTED`.
- The desk email is now a themed HTML email with Call, WhatsApp and Email buttons (the plain text stays inside it for any mail app).
- `dailyDigest`, 8:00 ET: one email to the desk listing the last day's starts that were not sent. A quiet day sends nothing. Switch: `SEND_DIGEST` (on).
- `hourlyTick`: one themed "finish your application" email to a visitor who typed an email and went quiet for `NUDGE_AFTER_HOURS` (2),
  never after 72 hours, never twice, never after they sent it. Switch: `SEND_NUDGE` (off).
- `SEND_CONFIRMATION` (on, Ohad's call on Nov 10): the visitor's themed confirmation when they send it, reply-to desk@upnonstop.com.
- Until v3 is deployed, the site's saves are refused by the old script (they carry no consent), so nothing changes in the sheet.

**v2, 11 Nov 2026 (the wallet picker):** paste the new `Code.gs`, then Deploy > Manage deployments > pencil > Version: New version >
Deploy. The `/exec` URL stays the same, so nothing changes on the site. The first request after that adds two column titles at the
end of the Requests tab, "Business cards" and "Personal cards"; older rows keep their cells. Until you redeploy, every picked card
still arrives in the "Cards" column, one line per bank. The visitor confirmation email ships switched off: set
`SEND_CONFIRMATION = true` at the top of Code.gs (and deploy a new version) to turn it on; its text is in `confirm_()`.

**Later changes to Code.gs:** Deploy > Manage deployments > pencil > Version: New version > Deploy. The `/exec` URL stays the same.
(A brand-new deployment would make a new URL, which then needs step 5 again.)

What it does: each real request is one row (Timestamp ET, Name, Email, Phone, Business, Card spend, Trade, Preferred time,
Source page, UTM/referrer, then the rest of the answers) and one email to you with every answer, reply-to set to the visitor.
Hidden honeypot field filled or the form sent in under 2 seconds: dropped silently. The same phone and email again within
10 minutes: saved as a "Repeat" row with no second email. Nothing is emailed to the visitor and nothing goes to Google Analytics.
Free: Apps Script's consumer quota is 100 emails a day (1,500 on Workspace), far above the form's volume.
