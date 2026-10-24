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
