# Rebuild v3: what changed and why (home, book, for-dental)

Preview only. Not for merge. The live Ghost site is untouched.

v3 is a ground-up restyle in the New Bot app's design language, built mobile first (390, then 1440). All copy is ported verbatim from the v2 builders. New lines are listed in PROPOSALS.md.

## Design system
- **assets/fo-site-tokens.css** holds only values copied from the app source. See the file header for the exact sources:
  - native: `src/ui/theme.ts` @3848f6d, `kit.tsx`, `screens/owner.tsx`, `screens/plan.tsx`, `src/ui/tokens.ts`
  - prototype: `fo-tokens.css` and `fonts/InterVariable.woff2`
- Surfaces are cream #FAF6EE, cream2 and white paper, with --line #E9E7EE borders and the app's soft shadow. Radii: card 18, row 14, button 28.
- Ink is #2A2230 / #5F5767 / #8E8796, from theme.ts @3848f6d (the build that rendered shots 10–26). The current tokens.ts says #4A4550; I matched the shots instead.
- Pillar colors come from owner.tsx: Earn #2E9E6A (green, as the app renders it; the brief said "gold"), Burn #E07B39, Learn #3A9BB8, Return #E60F86. Gold #F5B700 is used for progress and "now" states.
- Inter is used for every site section. The hero keeps DM Serif / DM Sans, and the ticker keeps JetBrains Mono, both unchanged.

## Rules applied
- **Money and numbers are never pink, including the $.** All figures are dark ink.
- Pink appears only on the chevron mark, primary buttons, links and the Return pillar's small accents. The ledger and Capture Report cards moved off pink to green and gold.
- Low-opacity photos (.phx) sit behind the cards on every section, with white scrims.
- No seats or availability claims were added, and no card or issuer names in new components. Estimates carry "Estimated, illustrative" pills or captions.
- The hero is untouched (v9/v10 port plus the earlier fixes), and the ticker is verbatim.

## Visual aids: v2 version → v3 app component
- Dial donut → the "What the balance buys" pattern: a hero number card plus ranked rows (flights, hotels, everything else) with meters.
- Spread axis → three label/value rows with meters (cents per mile).
- Pink seal / miniseal and the orbit → removed. A note card with the chevron replaces them.
- Destination cards → photo, "Same points" eyebrow, the points as a dark number, and **one comparison bar pair** (the usual way in grey, with your desk in Burn), followed by the "3.6x more trip" multiplier and an "Estimated" caption.
- Stacked ledger bar → the app's Ledger pattern: a $19,850 hero card with a green progress meter (9 captured / 1 honest no) and ranked lrow rows. The Landscaper row gets an "HONEST NO · $0" pill.
- Cashback → a summary comparison card plus two kv cards in the "Worth it" style.
- Book clock donut → a "20 min" number card. The flow is now the app's door rows (radio, plus a "Coming soon" pill on Text me), with a step progress bar and labels.
- Book next steps → the app timeline with status dots. The written answer is shown as Yes / Honest-no cards with meters and Pills.
- Book "converge" SVG → a channel rows card that ends in "one desk", plus numbered cards 01–03.
- Dental routing flow SVG → a $2,222/mo hero card and a "starting profile" rows card. Each line shows its $ value, an Nx pill and a meter.
- Dental calculator → slider rows, each with its value, a pill, a meter and a points label, plus a sticky result card in the "Worth it" style.
- Dental mistakes → cards with a "The math" panel of labeled comparison bars.
- Dental swipe card → a $5,000 card with a two-number pair and one comparison bar pair.
- Dental waterfall → two comparison groups: points 1x vs routed, then sticker → honest → fee → net.
- Dental cash cycle → a two-step timeline. The calendar is now a readable 12-month strip with month names.
- Dental 4 steps → the timeline.
- Dental verticals marquee → a ranked rows card: top 8, with Dental highlighted as "this page", and a "Show all 20 verticals" button.

## Layout
- Nav: the brand chevron, links, the green "💬 Text Your First Officer" button and the pink "Get your desk" button. Industries is a plain link instead of a dropdown. The mobile sheet now lists all 20 industries.
- Mobile deck: all 15 trip cards sit in a snap carousel with a progress meter and a counter. "Show all 15 trips" stacks them. v2 showed 5 cards plus a button.
- Desktop: two-column splits with sticky result cards. The featured destination card goes horizontal at 1000px and wider.

## Wow pass (after "wow me and keep it professional")
One signature moment per page, built from app components and real tokens only:
- **Home, #fomo featured destination (signature):** larger hero-grade card (`.ptile.sig`), 44–52px dark points number, 22px dark dollar values, 14px comparison bars (usual way neutral grey, with your desk in Burn, the section's one accent), 56–68px multiplier, count-up on every city change, slow scaleX fill. Fixed a bug where the `$` rendered larger than the digits.
- **Book, booking card (signature):** app-style card header (chevron tile, "The Found Money Call", "Free · 20 minutes · your way", green Open pill), goldLine border plus the app's `--shadow`. Hero eyebrow pink → gold. "Text me" coming-soon door fixed (was inheriting the small .soon pill style).
- **Dental, "Worth it" card (signature):** replaces the "Net, this month" hero card. Cream2 card with goldLine (app shot 15), net this year $26,668 as the big number, a value-vs-fee split bar (earn vs ink2), and rows: valued honestly $33,268 / our fee −$6,600 / net per month $2,222. All numbers are the v2 numbers.
- **One accent per section:** dental profile all Earn; mistakes in Burn with grey; routing in Learn; real math in Earn with grey sticker/honest bars; book hero in gold.
- Reduced motion: count-up, bars, meters and split bars are static under `prefers-reduced-motion`.

## Brand rule fix (mark on transparent only)
- Every site mark now uses /workspace/brand/firstofficer-chevron-transparent.png (copied to img/fo-chevron-transparent.png), including the favicon link.
- Removed every tile, fill, border, radius and shadow behind the mark: nav brand, home chat header, booking card header, "one desk behind every door" note, CTA card, footer. A global guard rule `.mk,.bkm{background:none;border:0;box-shadow:none;border-radius:0}` stops it returning.
- The hero data's mark path swapped to the transparent file; hero styling not changed (see open item on the hero node rings).


## Oct 24: chevron re-cut, app-exact bubbles, calm delight

**Chevron**
- `img/fo-chevron-transparent-v2.png` is a re-cut of Ohad's pink chevrons. The master is untouched.
- The master had 14,309 semi-transparent edge pixels, all near-white: the white halo. The v2 file has 0 near-white pixels. Its 2,635 semi-transparent edge pixels are all pink, so the edge is decontaminated against white.
- Stray specks were removed (59 components found, only the 2 chevrons kept) and the image was trimmed with 4% even padding.
- Every reference now points to v2: nav, footer, chat header, booking card, CTA cards, note line, favicon and hero.
- Global guard: `.mk,.bkm` never get a background, border, radius or shadow.
- Hero First Officer node: the outline rings stay. There is no fill, and the pink glow is gone.

**Bubbles, to the New Bot app spec**
- Client bubble: white, 1px goldLine, 18px radius with a 6px tail corner, 10/14 padding, Inter 15 to 15.5px, 82% max width.
- First Officer replies: unboxed ink text, as in the app. They are no longer pink bubbles with white text.
- Specialist bubbles: white with a neutral hairline.
- Inline figures: goldWash chips with ink text, so numbers are never pink or white-on-pink.
- Typing dots: ink3.
- Timestamps and read receipts: 12px ink3.
- Hero phone screen: cream `#FAF6EE`.
- Spacing: 4px between bubbles in the same turn, 14px between turns.
- These overrides live in `hero/fo-hero-app.js` and are appended to the hero's shadow-DOM CSS. The hero JS is unchanged.
- Home chat: same spec. Specialist names show as an ink3 label with a colored dot, not colored text.
- Composer: 22px radius, and the send key is goldLine with an ink arrow (it was white on pale gold, which failed contrast).
- Pills: ink2 text with a colored dot (the text was colored before).
- TeamBadge: 6px dot, 12px semibold, matching the app.

**Delight:** see INSPIRATION.md. It adds press feedback, pointer-only hover lift, the book check pop, the dental Worth-it settle and the home multiplier underline. Everything is off under reduced motion.

No copy was changed.
- Fixed the top ticker: dollar figures were pink (`#FA1896`) and are now gold2. Numbers are never pink.

## Hero never looks empty at 390 (Oct 24)
- Mobile persona card ("Meet <name>") now renders filled at load (header, Bespoke strategy code, dossier rows, final numbers) instead of waiting for scroll-into-view, so the part peeking above the sticky "Book Your Found Money Call" bar has content at the fold.
- Mobile phone thread: the first client/First Officer messages (up to 3, stopping before any specialist beat) render immediately and statically; the rest of the thread continues with typing-then-reveal once the desk scrolls into view.
- prefers-reduced-motion: full thread renders static (no typing), card renders static, no auto-cycling to the next persona. Applies on desktop too.
- Fixed a broken image: img/hero/fo-avatar.png (First Officer notification/avatar icon) was missing; it is now the transparent pink chevron mark.
- No copy changes.

## Sticky CTA removed, inline Found Money CTAs (Oct 24)
- Removed the fixed/sliding mobile "Book Your Found Money Call" bar on all v3 pages, at all widths, plus its JS (show/hide over empty space) and the 110px of footer bottom padding reserved for it (now 40px).
- Home: one calm inline CTA row directly after the destination signature card in "Same points. Two very different bookings." (white card, lead "See this on your own numbers.", secondary-weight button). Hero buttons, the existing button in the spend dial card, and the end-of-page CTA card stay as they were.
- Dental: one inline CTA row at the end of "See What You're Leaving Behind" (#numbers). Kept the page's own end card (#call); dropped the shared site footer CTA card on this page so the total is 3 (hero, numbers, end). No CTA added after mistakes (would have made 4).
- Book: dropped the shared footer CTA card. The page is the booking flow, so the flow and its submit are the only CTA. The newsletter card stays.
- Desktop hero phone: the first client/First Officer messages (up to 3, before any specialist beat) render at load; the rest types in.
- Nav WhatsApp button and "Get your desk" pill unchanged.

## Three alternatives + delight (Oct 24)
Comparisons now show three ways, labeled exactly **No strategy**, **Cash back** and **Mock-up strategy**, each with an illustrative note. Numbers stay dark; only the Mock-up strategy bar carries colour.

**Label and copy changes (for your yes):**
- Home destination cards (signature card plus all 15 deck cards):
  - "The usual way" → "No strategy" (same 1¢ statement-credit value).
  - New middle row, "Cash back": the spend that earns the card's points at the page's 2.1x blended rate, at 2% cash back. Example: Kyoto 150,000 pts → $1,429.
  - "With your desk" → "Mock-up strategy".
  - The method notes now explain all three ways.
  - Note: at 2.1x, 2% cash back comes out slightly *below* the 1¢ statement credit. That is the honest math, and it is shown as is.
- Home "The same $420,000, both ways" → "three ways":
  - New row: "No strategy · A debit card, earns nothing · $0".
  - "“2% back on everything”" became the row "Cash back", with the old line kept as its sub.
  - "Routed on the earn, booked on the burn" became "Mock-up strategy", with the old line kept as its sub.
  - New line: "Mock-up strategy is illustrative, not a projection of your results."
- Dental calculator:
  - New live rows, "Same spend, three ways · a year": No strategy $0 (debit), Cash back = card-able spend × 12 × 2% ($17,040 at defaults), Mock-up strategy = net after our fee ($26,668 at defaults).
  - Appended to the cap: "Cash back at 2% cash back on the monthly card-able spend, times 12. Mock-up strategy is illustrative."
- Dental "From sticker to net": the same three rows on $852,000, plus "Mock-up strategy is illustrative, not client data."
- Dental header: a passport stamp, "Dental · cleared for takeoff".
- Dental Worth-it card: a FROM $71,000 spend a month → TO 151,000 points a month stub (both figures were already on the page).
- Dental #routing:
  - Three status chips: "Vendor codes verified, not guessed", "Caps flagged before the pool fills", "The call printed before the booking".
  - New "Two lines, routed · a year" card. It uses only page-stated math from the mistakes section: supply distributors flat-2x 816,000 vs no-fee 2x 458,000; software and imaging 216,000 vs invoice card at 2x 108,000; stacking to 1,032,000. A card-types-only note is included.
- Home signature photo: a before/after slider. "What most people book · ≈ $X statement credit" vs "What the desk books · <trip>, est.", with a "<pts> pts · fixed" chip. Dragging it stops the auto-cycle.
- Home hero chat: an "Evening, <name>." greeting plus chips "Plan a trip", "This week’s earn" and "Ask the desk".
- Book submit: the button turns into rings → check, reading "Opening your email", then opens the email app (after 1.3s, or instantly under reduced motion).

**Behaviour:**
- Background photo layers now lead with photos that match the visitor's local time: dawn 5–8, day 8–17, dusk 17–20, night 20–5. Only existing photos are used, and the original order is kept as a fallback when fewer than 2 match.
- Routing lanes slide in and the points bar stacks up, all static under reduced motion.
- Existing press/settle micro-interactions are kept.
- Not done: a routing flow on home. Home has no per-vendor spend lines to route, and we did not invent any.

## Home three-way ladder reorder + headings (Oct 24)
- Home destination cards (signature card + all 15 deck cards): rows now ascend honestly, 1) Cash back (2% on the same spend), 2) Points, no strategy (statement credit at 1¢; label was "No strategy"), 3) Mock-up strategy. The 1¢ figure and the 3.6x multiplier are unchanged. Method notes reworded to the new order and label; card aria-labels updated to match.
- Home heading "Same points. Two very different bookings." → "Same points. Three very different outcomes."
- Deck intro "what it buys the usual way, and what it buys with your desk." → "what it buys three ways."
- Dental and the home "$420,000, three ways" block keep the "No strategy" (debit, $0) label.
- Dental boarding pass: plane icon about 1.5x bigger at 390 (16px → 24px).
