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
