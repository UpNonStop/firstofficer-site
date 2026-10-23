# PROPOSALS: open decisions for Ohad (mockups/rebuild-v1)

Nothing below was changed silently. Each item is either kept as-is in the mockups and flagged, or is a suggestion for the real build.

## Copy & compliance
1. **Legal pages (privacy, terms):** these still mention "AI" (4× each), "availability" (privacy 1, terms 5) and the Anthropic/Claude subprocessor line. They were kept verbatim, because legal text shouldn't be rewritten by find-and-replace. Proposal: legal review to reduce "AI" mentions and decide whether naming subprocessors fits the "never expose internal setup" rule.
2. **Trust page:** it contains a SOC 2 / ISO *negation* line ("we don't claim…"). The rule is no SOC 2/ISO claims. Proposal: delete the line entirely, because even a negation puts the acronym on the page.
3. **Airline and program names** (e.g. "Delta", plus one "Chase" on about.html) remain in home, hello, field-notes, strategist, trust and legal. The rule bans card, issuer and source names, but not airlines. Proposal: decide whether airlines are fine. Remove "Chase" from about.html (it's an issuer).
4. **IRS / EPA citations** (home tax panel: IRS Announcement 2002-18; Free From the Desk: IRS 1099-K, EPA 40 CFR 82.154) are kept because they are government sources that back up the claims. Proposal: confirm that they're allowed under "no source names".
5. **"Not a licensed financial advisor"** disclaimer on FFD and the industry pages: kept. It's a disclaimer, not a licensing claim. Confirm.
6. **"your customers / your clients"** meaning *the business owner's* customers (e.g. "when your clients pay by card") is kept. This is not "our customers".
7. **"United States Treasury"** in the legal text is kept.
8. **UPNS dispatches:** these contain aggregate claims (e.g. "across an illustrative client base, X% …"). They're labelled illustrative now. Proposal: either source them or cut them before publishing.
9. **Hello / field-notes:** these have a "$25K/$35K" spend figure and 2 "seat(s)" mentions in quoted persona stories. Proposal: change "seat" to "fare" in the persona quotes too, and label the $ figures "Example".
10. **New disclaimer.html** was assembled from existing site lines and needs legal review.

## Hero (PR #11) follow-ups (hero left untouched as instructed)
11. The hero chat loads **Inter** (outside the 3-font system). Proposal: swap it for DM Sans.
12. The hero (identical to PR #11, commit e0f8299) still carries **card, issuer and co-brand names** after the generic-cards pass. In the chat and dossier data: "Membership Rewards" (71×), "Ultimate Rewards" (43×), "ThankYou" (6×), "Capital One miles" (8×), co-brand cards such as "Hyatt business card" (8×), "Marriott business card" (4×), "United business card" (3×), "Southwest business card" (3×), "Premium Delta business card" and "Atmos business card". The specialist pods on the desk floor are labelled and show logos for Amex, Chase, Capital One and Citi. You approved the pods "as is", so the mockups leave all of this untouched. Proposal: one more hero pass in PR #11 that maps the currencies to "Bank A/B/C points", the co-brand cards to "airline business card" / "hotel business card", and the issuer pods to lettered bank pods. Airline and hotel *program* pods would stay.
13. The hero says "reviewed weekly". Confirm it doesn't conflict with "Strategy within 24 hours".

## Content
14. **Industry pages:** fo-home-v2 data (nuggets, MCC table, thin note) is used. Main has richer per-industry copy (longer intros and FAQs). Proposal: merge main's FAQs back in once the nuggets are approved.
15. **Free From the Desk:** the source chips ("Visa MDSM") were removed. Proposal: one generic footnote, "Merchant codes come from the card networks' published lists", is already in the text. Confirm that's enough.
16. **Text Me option** on the Book page is shown disabled ("Coming soon"). Proposal: keep it visible as a teaser, or hide it until texting is live.
17. **Gallery note:** in production, home.html becomes `/`, and index.html (the gallery) is not shipped.

## Added in the resume pass (Oct 23)
18. **Mobile hero persona card** shows blank in full-page screenshots because it animates in on scroll. It renders correctly in the browser. This is a screenshot artifact, not a bug.
19. **upns-064** still opens with "This year's biggest door opens Thursday, July 30". That's a dated timing line. It was kept as-is, because the dispatch is an archived issue. Proposal: add "Example:" or an archive date stamp, the same as the PR #10 offer lines.
20. **Not mocked up:** auth/google.html (the OAuth callback, not a public page) and the 11 redirect stubs (access, affiliates, cashback, complexity, education, expiration, loyalty, privacy, proactive, timing and value). They only forward to pricing, field-notes anchors or privacy-policy#do-not-sell.
