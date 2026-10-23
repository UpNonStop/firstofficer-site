# CHANGES: everything changed that wasn't explicitly asked for (mockups/rebuild-v1)

Built from the PR #11 hero branch (hero/firstofficer-v9) plus the copy and compliance text from PR #10/#12/#13. These are static mockups. Nothing on the live Ghost site was touched, and no PR was opened.

## Structural / design changes (not asked for explicitly)

- **index.html is the mockup gallery**, and the site home lives at **home.html**. In production, home.html would become `/`.
- **New page: disclaimer.html.** There was no standalone disclaimer page, so I built one from disclaimer lines that already exist across the site, organised into 7 sections. It needs a legal review before it ships.
- **app.html is now an "app coming soon" page** ("Your desk, in your pocket"). The source page is a deep-link handoff. Production should keep the existing "This link needs to come from your thread" behaviour.
- **Redirect stubs get no mockups.** These are the ~500-byte source files that only redirect, so they are not public pages.
- **Bespoke rebuilds** of day-one, welcome, briefing and 404. The copy is the same as the source pages, laid out in the new system. On day-one, "Open the app" became "The app · coming soon". On briefing, only question 01 is shown open, and the other 11 questions are listed. The program lists in question 03 are not mocked up.
- **UPNS dispatches** are embedded with their own namespaced styling (already DM fonts and pink). An embedded base64 logo was replaced with img/fo-chevron-alpha.png, and the "UR" label in a chart became "A".
- **Free From the Desk gold cards** use the 🪙-in-a-circle icon instead of the v2 nugget SVG.
- **Inner page heroes** use one split-hero pattern: a pink-accent serif H1 and a polaroid photo with its Unsplash credit where a photo exists. The chevron watermark is the only brand mark.
- **The ticker** (Oct 23, Ohad): the live site's tickers are restored exactly as on origin/main (8587e8d), with the same look and content: the dark `.fotick` running ticker under the nav on home.html (from live index.html) and the dark `.tickerbar` operator wire on hello.html (from live hello.html, with its date, last-month and marquee script). These are the only two live pages with a ticker. The markup is the verbatim live fragment (`_build/live_ticker_home.html`, `_build/live_ticker_hello.html`), not run through the copy fixes, and the CSS/JS is in `assets/live-ticker.css` / `assets/live-ticker.js`, scoped so fo.css cannot restyle it. The earlier light ticker is no longer used. Note: the restored hello ticker contains two live lines about "seats" / "sold out" that conflict with the locked no-seats rule (see HERO-DIFF.md, item P1).
- **Hero (Oct 23):** the hero background photo is shown again (the v9 `secphoto` CSS was missing from the mockup home): one of the 8 v9 photos per load, never the same twice in a row, under v9's white wash. The First Officer node is the v9 circle with its rings again, and the pink chevrons sit on transparent inside it. Logo tiles no longer cross their pod borders (see HERO-DIFF.md and /workspace/fo-rebuild-v2/HERO-LOGO-FIX.md).
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


## Automatic copy substitutions, by page

| Page | Find | Replace | Rule | Hits |
|---|---|---|---|---|
| about.html | `WhatsApp and SMS today, the app next\.` | WhatsApp today. Texting and the app are coming soon. | Texting/app coming soon | 1 |
| about.html | `watches 108 cards and 13 issuers around the clock` | watches 108 cards and 13 issuers on scheduled scans | Truth: scheduled scans, not around the clock | 1 |
| briefing.html | `Award seats and rates change` | Award space and rates change | No seats or availability | 1 |
| calculator.html | `Award pricing and availability change constantly` | Award pricing and award space change constantly | No seats or availability | 1 |
| field-notes.html | `business class seat\b` | business class ticket | No seats or availability | 1 |
| field-notes.html | `(?i)\baward availability\b` | (case-matched) | No seats or availability | 1 |
| field-notes.html | `the availability, and the timing` | the award space, and the timing | No seats or availability | 1 |
| field-notes.html | `Airlines release award seats` | Airlines release award space | No seats or availability | 1 |
| field-notes.html | `The best seats \(First, Business\) go fast` | The best cabins (First, Business) go fast | No seats or availability | 1 |
| field-notes.html | `the seat you want books for` | the flight you want prices at | No seats or availability | 1 |
| field-notes.html | `The same seat can cost` | The same flight can cost | No seats or availability | 1 |
| field-notes.html | `The same seat costs` | The same flight costs | No seats or availability | 1 |
| for-cpa-firms.html | `Visa defines` | The card networks define | No card/network source names | 1 |
| for-trucking.html | `Visa defines` | The card networks define | No card/network source names | 1 |
| hello.html | `business class seat\b` | business class ticket | No seats or availability | 2 |
| hello.html | `Coverage across 50 programs` | Coverage across 96 programs | Counts: 96 programs | 1 |
| hello.html | `coverage across 50 programs` | coverage across 96 programs | Counts: 96 programs | 1 |
| hello.html | `a consortium brain underneath, with a person stepping in when needed, one thread in your messages\.` | specialists underneath, one thread in your messages. Your strategy is reviewed and fine-tuned by a person before it reaches you. Every redemption is booked by a person. Day-to-day answers are software-led, and a person steps in when needed. | Approved human-review line; minimal "AI" | 1 |
| hello.html | `You put \$35K\+ a month on vendors and cards\.` | You put serious money on vendors and cards every month. | No minimum spend shown | 1 |
| hello.html | `on WhatsApp or SMS \(and soon on your App!\)` | on WhatsApp for now (texting and the app are coming soon) | Texting and app are coming soon | 1 |
| hello.html | `after EFS coding verification` | after fuel-card coding verification | No card names | 1 |
| hello.html | `Seats Are Hard` | Award Space Is Hard | No seats or availability | 1 |
| hello.html | `Award seats vanish` | Award space vanishes | No seats or availability | 1 |
| hello.html | `<div class="v">\$15K</div><div class="l">Minimum 12-mo capture to join</div>` | <div class="v">24 hrs</div><div class="l">Your strategy, reviewed by a person</div> | No minimum spend shown | 1 |
| hello.html | `<div class="v">\$35K</div><div class="l">Monthly spend floor · We check first</div>` | <div class="v"><a href="calculator.html">Calculator</a></div><div class="l">Run your own number first</div> | No minimum spend shown | 1 |
| hello.html | `You own a business with <b>\$35K\+ a month of non-payroll spend</b>` | You own a business with <b>real non-payroll spend</b> (<a href="calculator.html">run your number</a>) | No minimum spend shown | 1 |
| hello.html | `You spend <b>under \$25K a month</b> on cards` | Your card spend is <b>still light</b> | No minimum spend shown | 1 |
| hello.html | `<h3>Clears the bar at \$35K\+/mo non-payroll</h3>` | <h3>Clears the bar on the calculator</h3> | No minimum spend shown | 1 |
| hello.html | `Between \$25K and \$35K a month, same rule: the call computes your 12-month capture, and if it clears \$15K, you're in\.` | Wherever you land, same rule: the call computes your 12-month capture, and if it clears the fee with room to spare, you're in. | No minimum spend shown | 1 |
| hello.html | `<h3>Below \$25K a month</h3>` | <h3>When the math is thin</h3> | No minimum spend shown | 1 |
| hello.html | `THE CALL: \$35K\+ MONTHLY NON-PAYROLL SPEND, OR A COMPUTED 12-MONTH CAPTURE ABOVE \$15K` | THE CALL: WE RUN YOUR NUMBER FIRST · <a href="calculator.html">TRY THE CALCULATOR</a> | No minimum spend shown | 1 |
| hello.html | `WHATSAPP TODAY · APP \+ SMS NEXT` | WHATSAPP TODAY · TEXTING + APP COMING SOON | Texting/app coming soon | 1 |
| hello.html | `Costco only accepts Visa in-store\.` | Costco only accepts one card network in-store. | No card/issuer/source names | 1 |
| hello.html | `Costco in-store takes Visa only: route accordingly` | Costco in-store takes one card network only: route accordingly | No card/issuer/source names | 1 |
| hello.html | `Sample outputs are AI-generated illustrations` | Sample outputs are software-generated illustrations | Minimal "AI" | 1 |
| hello.html | `<b>629</b> PROGRAMS MONITORED` | <b>96</b> PROGRAMS MONITORED | Counts: 96 programs | 1 |
| hello.html | `Two-minute fix: seat assignments for the Denver run` | Two-minute fix: bag fees for the Denver run | No seats or availability | 1 |
| hello.html | `Airline credits cover seats and bags, not fares` | Airline credits cover add-ons like bags, not fares | No seats or availability | 1 |
| home.html | `we do not own the seats` | we do not control award space | No seats or availability | 1 |
| home.html | `Award pricing and availability change constantly` | Award pricing and award space change constantly | No seats or availability | 1 |
| home.html | `Availability and pricing change\.` | Award space and pricing change. | No seats or availability | 1 |
| home.html | `Coverage across 50 programs` | Coverage across 96 programs | Counts: 96 programs | 1 |
| home.html | `after EFS coding verification` | after fuel-card coding verification | No card names | 1 |
| home.html | `McKinsey estimated in 2018` | An industry study estimated in 2018 | No source names | 1 |
| home.html | `Breakage and unredeemed miles from McKinsey, 2018\.` | Breakage and unredeemed miles from a 2018 industry study. | No source names | 1 |
| how.html | `>Windows open<` | >Worth acting on< | No "just opened"/window-open availability language | 1 |
| pricing.html | `coverage across 50 programs` | coverage across 96 programs | Counts: 96 programs | 1 |
| pricing.html | `Software-led coverage across 96 programs, a person when needed,` | Coverage across 96 programs, strategy within 24 hours, | Approved human-review line | 1 |
| pricing.html | `You run a business with roughly \$25K a month or more of non-payroll spend\.` | You run a business with real non-payroll spend on cards and vendors. Not sure it is enough? <a href="calculator.html">Run your number on the calculator</a>. | No minimum spend shown; point to calculator | 1 |
| pricing.html | `>\$500 FLAT<` | >$500 PER TRIP< | Award search is a separate $500 per trip, always | 1 |
| pricing.html | `Award space, when the trip is real` | Award search, always separate | Award search is a separate $500 per trip, always | 1 |
| pricing.html | `Per award itinerary, any party size` | Award search, per trip, any party size | Award search is a separate $500 per trip, always | 1 |
| pricing.html | `Flat per itinerary,` | Flat per trip, always separate from the monthly fee, | Award search is a separate $500 per trip, always | 1 |
| product.html | `Coverage across 50 programs` | Coverage across 96 programs | Counts: 96 programs | 1 |
| product.html | `(?i)\bour customers\b` | (case-matched) | Never "our customers" | 1 |
| product.html | `When a seat does not exist` | When award space does not exist | No seats or availability | 1 |
| product.html | `as availability, prices, and programs shift` | as award space, prices, and programs shift | No seats or availability | 1 |
| product.html | `own profile held in isolation` | own profile kept in isolation | No "held" wording | 1 |
| product.html | `Below roughly \$25K a month in non-payroll spend, the fee is unlikely` | When non-payroll spend is light, the fee is unlikely | No minimum spend shown | 1 |
| product.html | `OPS (·\|&middot;) LIVE WATCH` | OPS \1 SCHEDULED SCANS | Truth: scheduled scans, not live watch | 1 |
| strategist.html | `(?i)\baward availability\b` | (case-matched) | No seats or availability | 1 |
| strategist.html | `a personal Visa earning 1x` | a personal card earning 1x | No card/issuer/source names | 1 |
| strategist.html | `<span class="pk">13</span></span><span>Banks Tracked` | <span class="pk">96</span></span><span>Programs Monitored | Counts: 96 programs / 13 issuers (duplicate 13 Banks row) | 1 |
| strategist.html | `The Strategist monitors award space for your specific routes and dates\.` | The Strategist scans award pricing for your routes and dates on a schedule, and the desk books once you approve. | Truth: scheduled scans; desk books | 1 |
| trust.html | `(?i)\baward availability\b` | (case-matched) | No seats or availability | 1 |
| trust.html | `We find the space; you claim it in your own account, which is the only place your points ever sit\.` | We vet your requirements, and once you approve, a person on the desk books it in your own account, which is the only place your points ever sit. | Burn vets, desk books | 1 |
| upns-062.html | `(?i)\b629 (loyalty )?programs` | (case-matched) | Counts: 96 programs | 2 |
| upns-062.html | `\b13 Banks\b` | 13 Issuers | Counts: 13 issuers | 1 |
| upns-062.html | `\b13 banks\b` | 13 issuers | Counts: 13 issuers | 1 |
| upns-062.html | `across our client base` | across an illustrative client base | Personas fictional; never "our clients" | 1 |
| upns-062.html | `(?i)\bour clients\b` | (case-matched) | Personas fictional; never "our clients" | 15 |
| upns-062.html | `no seat to book` | no award to book | No seats or availability | 1 |
| upns-062.html | `>UR</text>` | >A</text> | No card, issuer or source names | 1 |
| upns-062.html | `for wallets holding Bank D points` | for wallets with Bank D points | Never "holding" | 1 |
| upns-062.html | `(?i)\baward availability\b` | (case-matched) | No seats or availability | 1 |
| upns-063.html | `(?i)\b629 (loyalty )?programs` | (case-matched) | Counts: 96 programs | 3 |
| upns-063.html | `\b13 Banks\b` | 13 Issuers | Counts: 13 issuers | 1 |
| upns-063.html | `\b13 banks\b` | 13 issuers | Counts: 13 issuers | 2 |
| upns-063.html | `across our client base` | across an illustrative client base | Personas fictional; never "our clients" | 1 |
| upns-063.html | `(?i)\bour clients\b` | (case-matched) | Personas fictional; never "our clients" | 15 |
| upns-063.html | `no seat to book` | no award to book | No seats or availability | 1 |
| upns-063.html | `>UR</text>` | >A</text> | No card, issuer or source names | 1 |
| upns-063.html | `still holding their points` | still sitting on their points | Never "holding" | 1 |
| upns-063.html | `(?i)\baward availability\b` | (case-matched) | No seats or availability | 1 |
| upns-064.html | `(?i)\b629 (loyalty )?programs` | (case-matched) | Counts: 96 programs | 3 |
| upns-064.html | `\b13 Banks\b` | 13 Issuers | Counts: 13 issuers | 1 |
| upns-064.html | `\b13 banks\b` | 13 issuers | Counts: 13 issuers | 2 |
| upns-064.html | `across our client base` | across an illustrative client base | Personas fictional; never "our clients" | 2 |
| upns-064.html | `(?i)\bour clients\b` | (case-matched) | Personas fictional; never "our clients" | 17 |
| upns-064.html | `no seat to book` | no award to book | No seats or availability | 1 |
| upns-064.html | `>629</(div\|span)>(\s*)<div class="l">Programs read` | (case-matched) | Counts: 96 programs | 2 |
| upns-064.html | `Verdict held` | Verdict stood | Never "held" | 1 |
| upns-064.html | `verdict held` | verdict stood | Never "held" | 1 |
| upns-064.html | `(?i)\baward availability\b` | (case-matched) | No seats or availability | 1 |

### Totals by rule

- Personas fictional; never "our clients": 51
- No seats or availability: 29
- Counts: 96 programs: 16
- No minimum spend shown: 10
- Counts: 13 issuers: 8
- Award search is a separate $500 per trip, always: 4
- No card/issuer/source names: 3
- Texting/app coming soon: 2
- No card/network source names: 2
- No card names: 2
- No source names: 2
- No card, issuer or source names: 2
- Never "holding": 2
- Never "held": 2
- Truth: scheduled scans, not around the clock: 1
- Approved human-review line; minimal "AI": 1
- Texting and app are coming soon: 1
- Minimal "AI": 1
- No "just opened"/window-open availability language: 1
- Approved human-review line: 1
- No minimum spend shown; point to calculator: 1
- Never "our customers": 1
- No "held" wording: 1
- Truth: scheduled scans, not live watch: 1
- Counts: 96 programs / 13 issuers (duplicate 13 Banks row): 1
- Truth: scheduled scans; desk books: 1
- Burn vets, desk books: 1
