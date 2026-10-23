## Structural / design changes (not asked for explicitly)

- **index.html is the mockup gallery**, and the site home lives at **home.html**. In production, home.html would become `/`.
- **New page: disclaimer.html.** There was no standalone disclaimer page, so I built one from disclaimer lines that already exist across the site, organised into 7 sections. It needs a legal review before it ships.
- **app.html is now an "app coming soon" page** ("Your desk, in your pocket"). The source page is a deep-link handoff. Production should keep the existing "This link needs to come from your thread" behaviour.
- **Redirect stubs get no mockups.** These are the ~500-byte source files that only redirect, so they are not public pages.
- **Bespoke rebuilds** of day-one, welcome, briefing and 404. The copy is the same as the source pages, laid out in the new system. On day-one, "Open the app" became "The app · coming soon". On briefing, only question 01 is shown open, and the other 11 questions are listed. The program lists in question 03 are not mocked up.
- **UPNS dispatches** are embedded with their own namespaced styling (already DM fonts and pink). An embedded base64 logo was replaced with img/fo-chevron-alpha.png, and the "UR" label in a chart became "A".
- **Free From the Desk gold cards** use the 🪙-in-a-circle icon instead of the v2 nugget SVG.
- **Inner page heroes** use one split-hero pattern: a pink-accent serif H1 and a polaroid photo with its Unsplash credit where a photo exists. The chevron watermark is the only brand mark.
- **The ticker** under the nav is the light version (cream with pink accents) instead of a dark bar, to keep the theme light.
- **Home is fully re-laid-out** in the new system. The sections, copy and figures are the same as the live home: house wins, FOMO, the July ledger, cashback against points with the tax panel, the trip deck, the four pillars, the Friday Capture Report and Explore.
- **Book page:**
  - 4 contact options: WhatsApp (default), Email, Call me back, and Text me (disabled, "Coming soon").
  - A Phone call / Google Meet choice for The Found Money Call.
  - The form fields are first name, business email, industry, phone, preferred day/time and notes.
  - It never mentions seats or availability.
- **Calculator:**
  - The formula and JS are reused unchanged.
  - Band copy: "economy seats" became "economy fares", and "booked when space opens" became "booked when award space appears". This follows the no-seats rule.
  - The minimum-spend messaging is unchanged. No minimum is shown.
- **Industries:**
  - A new index with a dropdown jump plus 20 photo cards.
  - Each industry page has a link to the calculator preset for that industry (`calculator.html?ind=…`).
  - Industry content comes from the fo-home-v2 data: nuggets, the thin note and the MCC table. Main's richer per-industry copy is not used; see PROPOSALS.
  - The "source" chips on the nuggets were removed because of the no-source-names rule.
  - Each page ends with an "Another industry…" dropdown.
- **Free From the Desk:**
  - Content is the fo-home-v2 version: coffee hero, calculator feature, 6 cards and the picker.
  - All Visa / "Visa MDSM" names were replaced with "card networks' published merchant code lists".
  - The Found Money Call link points to book.html instead of connect.html.
  - The signature uses DM Serif italic instead of Caveat, because of the 3-font rule.
- **UPNS archive (upns.html):** a new index of the 3 dispatches, built on the teaser images. The dispatches are restyled, and the lettered "Bank A / Airline A" placeholders are kept.
- **Hello:** stats that implied real customers were replaced with labelled estimates. A duplicated row on the strategist page was removed.
- **Mobile nav:** the green "💬 Text Your First Officer" button collapses to a green WhatsApp-icon pill under 1060px.
- **Mock-data note** ("Client stories are shared with permission…") is in every footer.

## Copy substitutions applied automatically
All of the locked-rule enforcements below were applied by pattern. Each one is listed with its page and hit count in the table that follows.

- **Resume pass (Oct 23), truth fixes:**
  - about: "watches 108 cards and 13 issuers around the clock" became "on scheduled scans".
  - product ops board: "LIVE WATCH" became "SCHEDULED SCANS".
  - strategist: "monitors award space for your specific routes and dates" became "scans award pricing for your routes and dates on a schedule, and the desk books once you approve".
  - trust: "We find the space; you claim it in your own account" became "We vet your requirements, and once you approve, a person on the desk books it in your own account".
  - hello: "seat assignments" became "bag fees", and "cover seats and bags" became "cover add-ons like bags".
  - All of these are also in the table below.
- **Resume pass, layout:**
  - On phones, the industry MCC tables get tighter cell padding, because the IT services table ran 11px past the screen.
  - The home "Friday Capture Report" caption now wraps instead of running 10px past the screen at 390.
  - The contact-sheet script no longer includes its own output.
