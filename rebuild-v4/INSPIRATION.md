# Delight pass: inspiration log (Oct 24, 2026)

Source: WebSearch over Dribbble and similar galleries. Dribbble's tag pages block our fetcher with a JavaScript robot check, so I could only read individual shot pages and search summaries. The ideas below are general, well-known interaction patterns. We did not copy any layout, asset, color or code. Every pattern is rebuilt from the First Officer app tokens (cream, gold, goldLine, goldWash, ink, pink2 for CTAs only). Each one turns off under `prefers-reduced-motion`.

| # | Pattern | What it is | Seen in (reference only) | Where it shows up on our pages |
|---|---------|------------|--------------------------|---------------------------------|
| 1 | Typing, then reveal | Three quiet dots, then the message rises in with a soft spring | Chat UI shots with typing indicators and micro-interactions (e.g. "Gaming Messenger UI", Dribbble) | Home hero phone thread (now app-styled: ink3 dots, client bubbles in white and goldLine, First Officer replies unboxed) and the home "This is the entire product" chat |
| 2 | Scroll-filled progress with a count-up | Bars fill as the card enters, and the number counts up to its value | Fintech landing animations (Genuine Impact, Merixstudio); savings milestone bars | Home signature card: the bars fill, the multiplier counts up, then a goldWash underline draws under it |
| 3 | Settle-in verdict ("found money") | Once the math lands, a single soft highlight passes and the verdict chip settles. No confetti | Cash-back reward flows (Credit Karma Cash Back, Dribbble) | Dental "Worth it" card: the bars fill, a soft gold ring breathes once, a gold sheen passes once, and the "Worth it" pill settles |
| 4 | Selection with a check pop | Press-down on tap, then the radio dot springs in with a small ring ripple | Booking and seat-selection flows; checkbox micro-animation shots | Book page option cards ("doors") and the phone or Meet choice |
| 5 | Haptic-feeling press | The button scales to 0.97 on press with a short spring back, and its shadow drops | Common native-app press feedback (Revolut chat and send interactions) | Every `.btn` and `.chip` on all three pages |
| 6 | Hover lift, pointer only | 3px lift, a warm gold shadow, and a 2.5% image push-in | Card galleries across travel and fintech shots | Home and dental story tiles (`.ptile`), CTA cards. Touch devices are untouched |
| 7 | Slow photo crossfade | The low-opacity background photos rotate with an opacity crossfade, never a slide | Travel landing pages | Already in place on every section (`data-ph`). Kept as is |

**One signature moment per page**
- Home: the hero thread, with typing before each reveal.
- Book: the option-card check pop.
- For-dental: the Worth-it settle.

Everything else is small press and hover feedback.

## Round 2: Dribbble patterns (Oct 24, 2026)

We used the patterns only and copied no designs. Everything is rebuilt from our own tokens and is calm under `prefers-reduced-motion`.

| # | Pattern | Where it lives now |
|---|---------|--------------------|
| 1 | Ticket / boarding-pass card: notched side cutouts and a dashed tear line | Dental hero "Worth it" card (`.card.bp`). The notches line up with the tear line via a CSS mask. A FROM → TO stub shows $71,000 spend a month → 151,000 points a month, both figures already on the page |
| 2 | SVG route arc drawn with stroke-dashoffset, with a small plane following it on `offset-path` | Same card: a pink dashed arc on cream and an ink plane, with no glow. Under reduced motion it shows drawn and static |
| 3 | Lighter comma groups on big numbers, plus a blur-to-sharp reveal | Dental hero net figure (`data-dg`): the comma is dimmed and the number sharpens from a 6px blur on reveal. No blur under reduced motion |
| 4 | Photo card with floating white stat chips over the photo | Home signature destination card: white label chips on both halves and a white "150,000 pts · fixed" chip |
| 5 | Rewards progress rows: big figure, thin fill, numbers dark, mini bar per row | Every three-way comparison (`.cmp.alt3`): No strategy / Cash back / Mock-up strategy |
| 6 | Recommendation card: one highlighted best option, with a dimmed "Alternative" row | Dental #routing "Two lines, routed" lanes card. It shows card types only, never names |
| 7 | Serif-italic greeting with pill suggestion chips that have coloured dots | Home hero chat: "Evening, Kofi." (the thread is set "Tonight") with three dotted pills |
| 8 | Pulsing concentric rings that collapse into a check | Book page submit button, before the email app opens. Instant under reduced motion |

**One hero moment per page**
- Home: the hero thread, now opening with the greeting.
- For-dental: the boarding-pass Worth-it card.
- Book: the ring-to-check on submit.

The before/after slider, the routing lanes and the three-way rows are quiet and in-flow.
