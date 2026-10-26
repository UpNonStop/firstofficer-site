"""3h desk: the hand-painted brush, and the 'our own voice' cleanup.

Ohad (Oct 26): the pink highlight must look like a true brush; no source names
and no checked/as-of dates on the page. Everything here runs on the built 3h
HTML in ffd_c_opts.py, and check() fails the build if anything comes back.
"""
import re
from urllib.parse import quote


def _svg(vb, d, c):
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='{vb}' preserveAspectRatio='none'>"
           f"<path d='{d}' fill='{c}' transform='translate(0 11) scale(1 .8)'/></svg>")
    return 'url("data:image/svg+xml,' + quote(svg, safe=" =:/',.-()") + '")'


# one bold, solid brush swipe (Ohad, Oct 26: "just needs a bigger one brush stroke").
# Three pieces so the ends never distort: a slanted touch-down cap on the left, a body
# that stretches to the phrase (gently uneven top and bottom, about -1deg of lift to
# the right), and a tapered tail on the right with two small dry-brush notches.
# The stroke sits low: it covers the x-height to just under the cap height.
BRUSH_L = ("M40 6 L24 6.6 C18 7 15 8.6 13 11.5 C11 15 10 19 8.5 23 C6.5 29 4.5 35 2.5 41 "
           "C1.2 45.5 2.5 49.5 7 51 C15 52.3 28 52 40 52Z")
BRUSH_M = ("M0 6 C25 4.8 50 5.4 75 3.9 C86 3.3 94 3.1 100 3 L100 49 C82 49.8 64 49.2 45 50.6 "
           "C28 51.6 14 51.8 0 52Z")
BRUSH_R = ("M0 3 L22 2.6 C29 2.5 34 3.4 36.5 5.8 C38.5 8.2 36 10.5 38.8 12.8 L33.5 15.6 "
           "C37 18.3 39 21.5 36.8 24.6 L31 26.6 C34.5 29.6 35.2 33.6 32.2 37.6 C28.4 42.4 22 46 14 48 "
           "C8 48.9 4 49 0 49Z")


def brush(color='#FA1896', cap='.8em'):
    """Full CSS background value (three layers) for one solid brush swipe."""
    return (f"{_svg('0 0 40 56', BRUSH_L, color)} left center/{cap} 100% no-repeat,"
            f"{_svg('0 0 40 56', BRUSH_R, color)} right center/{cap} 100% no-repeat,"
            f"{_svg('0 0 100 56', BRUSH_M, color)} center/calc(100% - 2*{cap} + 2px) 100% no-repeat")


# ---------------------------------------------------------------- sources out
# label-style attributions are dropped outright; prose that named a source is
# rewritten in the desk's own voice (before -> after, reported to Ohad)
REWRITES = [
    # fine print under cards and groups
    (" Codes and names from Visa's April 2026 manual.", ""),
    ("Codes and names from Visa's April 2026 manual. ", ""),
    (" Merchant codes are defined in the Visa Merchant Data Standards Manual.", ""),
    ("Based on Visa's US surcharge and convenience fee rules.", "This follows the card networks' US surcharge and convenience fee rules."),
    ("A PAYDEX needs three payment experiences from at least two vendors.", "A business payment score needs three payment experiences from at least two vendors."),
    ("Based on DOL Fact Sheet 15.", "Based on the federal tip rules."),
    ("Based on ABA Model Rule 1.15(b) and Connecticut Bar Informal Opinion 2014-02.", "Based on the model trust-account rule and one state bar opinion."),
    ("Based on the IFTA Procedures Manual, section P550, effective August 26, 2026.", "Based on the interstate fuel-tax receipt rules."),
    ("Based on the CFPB's RESPA FAQs.", "Based on federal RESPA guidance."),
    ("Under 40 CFR 82.154(c), a buyer", "Under federal refrigerant rules, a buyer"),
    ("The $2,000 line is from the IRS 1099 instructions.", "The $2,000 line is the 1099 reporting threshold."),
    ("The 60-day line comes from IRS accountable plan rules in Pub 463.", "The 60-day line comes from the accountable plan rules."),
    ("Based on 40 CFR Part 441.", "Based on the federal dental amalgam rule."),
    ("Based on 40 CFR Parts 82 and 84.", "Based on the federal refrigerant rules."),
    # card one-liners that read as a source label
    ("PAYDEX, Intelliscore, SBSS and the SBA.", "Four business scores and the loan program that reads them."),
    ("The spa rule in Visa's own manual, and why hair and makeup can be spa.", "The spa code rule, and why hair and makeup can be spa."),
    # dates: nothing on the page says when it was checked
    (" Every rule was checked on October 12, 2026. Rules change after that, so confirm before you act.", " Rules change, so confirm before you act."),
    ("Every rule was checked on October 12, 2026. Rules change after that, so confirm before you act.", "Rules change, so confirm before you act."),
    ("Rules were checked on October 12, 2026; they change, so check", "Rules change, so check"),
    ("Dates as of October 12, 2026, for calendar-year filers.", "Dates are for calendar-year filers."),
    ("Government fees and rules as of October 12, 2026.", "Government fees and rules change."),
    (", as of September 2026.", "."),
]


def desource(s):
    # 'Source: IRS' meta label on every card (and the dot before it)
    s = re.sub(r'<span class="sep" aria-hidden="true">&middot;</span><span class="src">[^<]*</span>', '', s)
    # citation chips in the nuggets (Visa MDSM, IRS Pub 463, myFICO ...)
    s = re.sub(r'\s*<a class="chip a"[^>]*>[^<]*</a>', '', s)
    # 'Sources: <a>..</a>, <a>..</a>.' / 'Source: ...' sentences in fine print
    s = re.sub(r'Sources?: (?:<a [^>]*>[^<]*</a>|[^<.])*(?:, (?:<a [^>]*>[^<]*</a>|[^<.,])*)*\.\s*', '', s)
    s = s.replace(' The rules behind them are linked in the card nuggets.', '')
    # 'Coding: Visa MDSM' style tags
    s = re.sub(r'Coding: Visa MDSM\.?\s*', '', s)
    for a, b in REWRITES:
        s = s.replace(a, b)
    # the stats row's 'Checked October 12, 2026' cell
    s = re.sub(r'<span class="ck">[^<]*</span>', '', s)
    return s


# names that must never appear as a label or attribution on 3h
LABEL_NAMES = (r"\b(?:Visa MDSM|MDSM|myFICO|Federal court|settlement site|Issuer pages?|Pub 463|CFR|"
               r"DOL Fact Sheet|CFPB's RESPA FAQs|Merchant Data Standards)\b")
# the business-score names may be explained inside a card, never used as the card's label
CARD_LABEL_NAMES = re.compile(r"\b(?:PAYDEX|Intelliscore|SBSS|D&amp;B|D&B|ic3)\b")
LABEL_POS = re.compile(r'<(?:span class="(?:kind|src|ck)"|a class="chip a"|p class="fine"|p class="love"|h3)[^>]*>(.*?)</(?:span|a|p|h3)>', re.S)
AGENCY = re.compile(r"\b(?:Visa|IRS|FinCEN|CFPB|DOL|DHS|GSA|EPA|FBI|Nacha|FICO|SBA|OSHA|IFTA|ABA|BMI|ASCAP|TSA|Chase|Capital One|Equifax|Experian|TransUnion)\b")


def check(s):
    """Fail the build if a source label, citation or checked date comes back."""
    bad = []
    for pat, why in [(r'class="src"', 'Source label'), (r'\bSources?:', 'Source line'), (r'class="chip a"', 'citation chip'),
                     (r'MDSM', 'Visa MDSM tag'), (r'Coding:', 'Coding tag'), (r'class="ck"', 'Checked cell'),
                     (r'October 12', 'checked date'), (r'\b(?:[Cc]hecked|[Uu]pdated) (?:on )?(?:January|February|March|April|May|June|July|August|September|October|November|December)', 'checked/updated date'),
                     (r'\bas of (?:January|February|March|April|May|June|July|August|September|October|November|December),? 20\d\d', 'as-of date'),
                     (LABEL_NAMES, 'source name'), (r'ic3\.gov</a>', 'linked source')]:
        for m in re.finditer(pat, s):
            bad.append(f'{why}: ...{s[max(0, m.start() - 50):m.end() + 30]}...')
    for m in LABEL_POS.finditer(s):
        txt = re.sub(r'<[^>]+>', '', m.group(1))
        # fine print and card lines may say what a rule is about (an EPA deadline, DEA paperwork),
        # but never cite where it came from
        if re.search(r'\b(?:Based on|from|defined in|according to|per)\s+(?:the\s+)?' + AGENCY.pattern, txt) or \
           re.search(r"\b(?:Visa|IRS|CFPB|DOL)'s (?:own |US |April )?(?:manual|rules|FAQs|instructions)", txt) or \
           (m.group(0).startswith(('<span class="kind"', '<span class="src"', '<a class="chip'))) and AGENCY.search(txt) or \
           m.group(0).startswith(('<p class="love"', '<h3', '<span class="kind"')) and CARD_LABEL_NAMES.search(txt):
            bad.append(f'attribution: {txt[:120]}')
    assert not bad, '3h source/date check failed:\n' + '\n'.join(bad[:30])
    return s


# ---------------------------------------------------------------- email capture (Ohad, Oct 26: "I want their emails")
# The page used to promise "No email". It now asks for one, plainly, with a reason.
# MOCKUP: the form posts nowhere. action="#capture-placeholder" must be swapped for the real
# list endpoint before launch; onsubmit only shows a thank-you line in the page.
CAPTURE_ACTION = '#capture-placeholder'
TAGLINE = 'New ones go to your inbox.'
TAGLINE_OPTIONS = [
    'Free to read. New ones go to your inbox.',                       # picked
    'Free. Want the new ones first? Leave your email.',
    'Free to read. Leave your email and the next ones come to you.',
    'Free. New notes land in your inbox, one email at a time.',
    'Free to read. Your email gets you the new ones as they land.',
]
MICRO = 'One email when something new lands. Unsubscribe anytime.'


def capture_form(cls, btn='Send me new ones', idp='cap'):
    return (f'<form class="cap {cls}" action="{CAPTURE_ACTION}" method="post" data-placeholder="mockup: not connected to any list" '
            f'onsubmit="this.classList.add(\'sent\');return false">'
            f'<label class="cap-l" for="{idp}-e">Email for new notes</label>'
            f'<div class="cap-row"><input id="{idp}-e" type="email" name="email" required autocomplete="email" placeholder="you@yourbusiness.com">'
            f'<button type="submit">{btn}</button></div>'
            f'<p class="cap-m">{MICRO}</p><p class="cap-ok" role="status">Thanks. Mockup only, nothing was sent.</p></form>')


EMAIL_REWRITES = [
    # lede tagline
    ('Free. <span class="hl">No email. No catch.</span></p>',
     f'Free to read. <span class="hl">{TAGLINE}</span></p>' + capture_form('cap-hero', idp='caph')),
    # meta description
    ('for business owners, free. No email. No catch.', 'for business owners, free to read. Leave your email for the new ones.'),
    # stats row: the '0 emails asked for' cell becomes the real card count shown on the shelves
    ('<span><b>0</b>emails asked for</span>', '<span><b>109</b>cards on the desk</span>'),
]


def capture(s):
    for a, b in EMAIL_REWRITES:
        assert s.count(a) == 1, f'capture rewrite target missing: {a[:60]}'
        s = s.replace(a, b)
    # end of the desk: the same capture inside the closing note, under its paragraph
    m = re.search(r'<section class="endnote bleed">\n(<p>.*?</p>)\n<span class="sign">Ohad</span>\n</section>', s, re.S)
    assert m, 'endnote not found'
    s = s[:m.start()] + ('<section class="endnote bleed">\n<div class="en-main">' + m.group(1)
                         + '<div class="en-cap"><p class="cap-ask">Want the new ones when they are added? Leave your email.</p>'
                         + capture_form('cap-foot', idp='capf') + '</div></div>\n<span class="sign">Ohad</span>\n</section>') + s[m.end():]
    bad = [m.group(0) for m in re.finditer(r'(?i)no e-?mails?\b|no sign-?ups?|no catch|emails asked for', s)]
    assert not bad, f'email copy contradicts the capture: {bad}'
    return s


# ---------------------------------------------------------------- chevron only in the logo (Ohad, Oct 26)
CHEV_OK = re.compile(r'<link rel="icon" href="img/fo-chevron-transparent(?:-v2)?\.png">|'
                     r'<span class="mk"><img src="img/fo-chevron-transparent(?:-v2)?\.png" alt="">')
CHEV_CP = 'polygon(50% 0,100% 50%,100% 100%,50% 50%,0 100%,0 50%)'


def nochev(s):
    """Fail the build if the chevron is used anywhere but the header/footer logo and the favicon."""
    rest = CHEV_OK.sub('', s)
    bad = [rest[max(0, m.start() - 80):m.end() + 20] for m in re.finditer(r'fo-chevron[^"\')\s]*', rest)]
    if CHEV_CP in s:
        bad.append('chevron clip-path ' + CHEV_CP)
    assert not bad, 'chevron used outside the logo/favicon:\n' + '\n'.join(bad[:20])
    return s
