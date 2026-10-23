# Rebuild v2 — copy changes (disclosed)

Mockups only. Nothing here is published; the live Ghost site was not touched. Branch: mockups/rebuild-v2 (no PR, no merge).

## Copy changes I made to Ohad's lines (each needs a yes)

| Page | Was (live/v1) | Now (v2) | Why |
|---|---|---|---|
| home | "on dates that actually have space" | "on the right dates" | No seats/availability rule |
| home | (booking line) | "the desk books once you approve" | Desk-books rule |
| home | "already hold it" | "already have it" | No "held/holding" rule |
| home | Barcelona line | reworded to drop availability claim | No seats/availability rule |
| book | "We call you at the time you pick." | "We call the number you give." | No "Pick a time" rule |
| book | "Tell us where to send the invite / Choose a time and you'll get a calendar invite…" | "Tell us where to reach you / We reply within one business day to set the time." | No "Pick a time" rule |
| for-dental | Mistake 02: "4x holds on the first $150,000…" | "4x applies on the first $150,000…" | No "held/holding" rule |
| for-dental | v1 "what we could not source yet" note under the nuggets | dropped; kept "Check your own statements; the desk verifies every one before routing." | Reads as an internal note |
| for-dental | Hero flow labels | shortened vendor labels in the diagram only (e.g. "Implants & ortho") | Fit; body copy unchanged |

Everything else on the three pages is Ohad's live copy (dental is the live page copy verbatim, plus v1 gold-nugget copy).
Book step 1 heading "How do you want to reach us?" is v1 copy, kept.
Hero: a faithful port of v9/v10, not redesigned. Ticker: identical to origin/main.

## Review fixes, Oct 23 (design only, no copy changes)

- Sticky mobile CTA ("Book Your Found Money Call"): it now hides whenever text, a figure, a card, an image or a control would sit under it, and comes back over empty section space. The story card's multiplier is never covered. Mobile pages get 84px bottom padding so the end of the page is never under it. On book.html it stays hidden, because that page is the booking flow.
- Background photos: the scrims are lighter, so the photos read at about 20–45% strength instead of near-white. Secondary text colours over photo sections are a step darker so they stay at AA.
- Hero dossier card: the frame is now a full, static accent ring. It replaces the travelling dash, which read as a clipped bottom border with a stray pink line in stills.
- Story card at 390: the sub-labels ("Statement credit, at 1¢ a point", trip lines) are tighter mono on one line, with no awkward wrap.
- Secondary text over photo sections (`.ps`) is darker again (mute #332e39, small mute #3b3641, body #26222b), and the deck section's light scrim is lifted slightly (desktop .56/.40, mobile .58/.42). Worst-case maths for a near-black photo pixel under the lightest text-zone scrim (.56): ink 5.7:1, body 4.5:1+; at a typical dark pixel (rgb 40,40,50) mute text is about 4.6:1.

## Hero fix applied (from HERO-LOGO-FIX.md / PR #11), Oct 23

- `hero/fo-hero.js` and `hero/fo-hero-data.js` are now PR #11's fixed files (byte-identical to mockups/rebuild-v1 `rebuild-mockups/hero/`), with three v2 edits:
  - The static dossier ring above (replaces the travelling dash).
  - No Inter: every Inter / `-apple-system,Inter` stack in the hero CSS is `'DM Sans'`; the font-ready check and preloads use DM Sans; the Inter Google Fonts family is dropped from home.html's head.
- What the fix brings in: generic card descriptions in the personas and dossier chips (no card or issuer names or logos in chips); logo tiles and label plates contained inside their pod frames (plus the fit() font step-down for long names); the v9 circle First Officer node with its rings, pink chevrons (`img/fo-chevron-alpha.png`) on transparent.
- Live ticker: markup was already identical to origin/main; the two `.fotick` / `.fotick .tk` rules now match the live CSS verbatim (pinned font-size, weight, style and line-height).

### 390 foot + small-print fixes (Oct 23, late)
- Story card and the 15-trip deck cards at ≤760px: the "Estimated, illustrative" pill and the "est. taxes" line stay on one line each (nowrap, 9px/10px mono, tighter tracking). No copy change.
- Method / fine-print notes that sit directly on a photo section (`.ps p.method`, `.ps p.fine`, `.ps p.meth`) now get a soft cream plate (82% opacity, 10px radius) so 11px text never lands on a busy patch of photo. Left-aligned fine print stays left.
