# HERO-DIFF: mockup / PR #11 hero vs the v9 (desktop) and v10 (mobile) finals

Oct 23, 2026. References: `/workspace/fo-hero-v3/final/hero-v9.html` (desktop) and `hero-v10.html` (mobile).
Compared against PR #11 (`hero/firstofficer-v9`, `index.html` + `hero/fo-hero.js` + `hero/fo-hero-data.js`) and the mockup home
(`mockups/rebuild-v1`, `rebuild-mockups/home.html`, which loads the same two hero files byte for byte).
The comparison covered the CFG data (every key), the C.css lines, the engine JS, the assets (the 8 background photos match v9/v10 by md5), the visible
hero text at 1440 and 390, and screenshots (`/workspace/fo-hero-v9-shots/herodiff/`).

Status: **A** = already approved by Ohad. **P** = pending Ohad's approval. Nothing marked P was changed on my own initiative;
the items restored on Oct 23 by Ohad's instruction are listed under "Restored" for the record.

## Restored on Oct 23 (Ohad's instructions)
- R1. **Live ticker, exactly as on origin/main (8587e8d).** These are the only two live pages with a ticker:
  - home.html now has live index.html's dark `.fotick` running ticker under the nav.
  - hello.html now has live hello.html's `.tickerbar` operator wire, with its date, last-month and marquee script.
  - The markup is verbatim. Computed styles were compared element by element against the live page and match (88/88 and 198/198 elements). The only differences were animation-phase opacity, which is timing.
  - The live and mockup strips look the same at 1440 and 390: `/workspace/fo-hero-v9-shots/ticker/cmp-left.png`.
  - PR #11 already has the live ticker unchanged (its index.html ticker markup and CSS are identical to main).
- R2. **Hero background photo.** The mockup home was missing v9's `secphoto` CSS, so the photo never showed. It is added verbatim.
  - v9/v10 behaviour: **one** of 8 photos is chosen at random per page load (never the same as the last one, `localStorage fo9_bg`) under the white wash. That is what PR #11 and the mockup now do.
  - The pool matches v9/v10 by md5.
  - The engine (`fo-hero.js`) had this code all along; only the CSS was missing in the mockup.
- R3. **First Officer node.** The v9 circle node and its white and pale-pink rings are back, on desktop and on the v10 mobile rings, and the wires meet the ring. The pink chevrons sit on transparent inside it. See P2 for the one interpretation.

## Approved differences (A)
- A1. Generic card names in the dossiers and chats (e.g. "Business points card"), not issuer card names. In CFG `personas`/`tasks` this shows as "Amex"→"Card" in one task string.
- A2. No issuer logos in the dossier card chips.
- A3. Button links (CTA hrefs).
- A4. The avatar mark swap: the First Officer avatar in the chat is the transparent pink chevron (`.mm .av.avfo`).

## Pending differences (P), for Ohad's approval
- P1. **The restored hello ticker breaks the locked no-seats rule.** It has two live lines:
  - "TWO TRANSATLANTIC BUSINESS SEATS FOR THE SEPTEMBER BUYING TRIP"
  - "TWO BUSINESS SEATS FOUND ON A DATE THAT READ SOLD OUT"

  They are kept exactly as live, per "exactly". Proposed wording if Ohad wants the rule applied: "TWO TRANSATLANTIC BUSINESS FARES FOR THE SEPTEMBER BUYING TRIP" and "TWO BUSINESS AWARD TICKETS BOOKED FOR THE TRIP".
- P2. **Node interior.** v9's node is a solid pink disc with white chevrons. Ohad asked for pink chevrons on transparent with no tile or fill, so the rings and circle are kept, the pink disc is removed, and the interior is transparent (the photo shows through). The chevron is padded 15%/22%/13% inside the circle. Compare: `/workspace/fo-hero-v9-shots/herodiff/sheet-node-v9-pr-mock-v10.png` (v9 | PR | mockup at 1440, then v10 | PR | mockup at 390).
- P3. **Logo-tile containment fix (BA, Atmos and 32 more tiles).** v9 has the same bleed, so the fix differs from v9 in three ways. The text is unchanged.
  - Label plates are capped at the tile width minus 8px.
  - Active plates use 6px side padding, or 2px for long names.
  - A long active name or status line that is wider than its plate is shrunk to fit (11px → about 9.5–10.5px, never below 9px). The fitter is in fo-hero.js.

  Details: `/workspace/fo-rebuild-v2/HERO-LOGO-FIX.md`.
- P4. **Burn/Learn accent colours.** PR uses Burn #F26419 and Learn #2E9BE8. v9/v10 use Burn #E8590C and Learn #1F8AD6, in both C.css `.t-burn/.t-learn` and CFG `acc`. This was inherited from PR #11's first commit, not changed today.
- P5. **v10 mobile changes made on Oct 23 that are not in PR #11.** `hero-v10.html` was edited today (19:15 JST); `hero-v10.html.bak-20261023` is the earlier v10 that PR #11 was ported from. The new v10 has:
  - (a) A second "Get your desk / See how it works" button pair right under the Meet card on mobile (`CTA1`). PR #11 and the mockup have only the pair at the end.
  - (b) The owner's first message is shown in the phone before the beat-2 playback (`preOwner`).
  - (c) The card intro on first view, with the spend/after figures filled at once (`SEEN.c0`), and changed beat spacing (+24/+18 offsets).

  I did not port these. Say if they should go in.
- P6. **Desk header icons (DESKH).** In PR the program icons use `object-fit:contain`. In v9 they are round (`border-radius:50%`). This was inherited from PR #11.
- P7. **The "First Officer is ready" (FOREADY) line fonts** differ slightly from v9. This was inherited from PR #11.
- P8. **`#disc` null guard.** PR's engine skips the disclaimer element when the host page has none; v9 assumes it exists. This is behaviour only and invisible.
- P9. **Page wrapper (mockup only).** The mockup home uses the rebuild nav and the mockup sticky bar ("The Found Money Call"), where v9/v10 and PR #11 use the live nav and the live sticky bar ("Your yearly capture $19,492"). The hero itself is the same file.
- P10. **Photo semantics.** Ohad described "dozens of low-opacity auto-rotating photos". v9/v10 actually show one photo (from 8) per load, changing on each reload, not a continuous slideshow. The 12-photo daily `POOL` in hero-v9.html belongs to the live sections below the hero (`.sec.photo`), not to the hero. If Ohad wants a timed crossfade inside the hero, that would be new behaviour; it needs approval.

## Not differences
- The persona, chatter and status texts differ between screenshots only because of the random chatter and status rotation. The same persona (p=5) gives the same dossier.
- The 8 hero photos, the 20 map cards, the logos and the chevron asset are the same files.
