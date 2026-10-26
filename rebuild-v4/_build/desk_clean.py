"""3h desk: the hand-painted brush, and the 'our own voice' cleanup.

Ohad (Oct 26): the pink highlight must look like a true brush; no source names
and no checked/as-of dates on the page. Everything here runs on the built 3h
HTML in ffd_c_opts.py, and check() fails the build if anything comes back.
"""
import re
from urllib.parse import quote


def brush(color='#FA1896', seed=4):
    """One dry-brush stroke as an SVG data URL.

    Tapered, frayed ends; ragged top and bottom (feTurbulence -> feDisplacementMap);
    bristle streaks (a second, stretched turbulence used as an alpha mask); a slight
    tilt (left end lower) and a lighter start and finish. preserveAspectRatio=none,
    so it stretches to any phrase; pair with box-decoration-break:clone for wraps.
    """
    body = ("M1 38 C4 28 8 19 18 15 C44 10 76 12 116 9 C176 6 244 8 304 5 C342 4 372 4 393 3 "
            "C398 7 400 13 396 18 C399 25 395 31 398 38 C392 45 362 44 330 46 C270 48 200 47 140 50 "
            "C90 52 50 52 22 54 C13 55 7 53 4 49 C7 47 2 44 1 38Z")
    pass2 = ("M8 30 C40 22 90 21 150 18 C220 15 300 13 388 11 C390 17 388 24 390 30 "
             "C320 33 240 34 170 37 C110 40 60 42 10 46Z")
    fray = ("M0 44 L22 41 M3 33 L30 31 M6 49 L26 46 "
            "M372 9 L399 7 M370 34 L398 34 M378 21 L400 19")
    c = color
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 56' preserveAspectRatio='none'>"
           f"<defs><linearGradient id='g' x1='0' x2='1'>"
           f"<stop offset='0' stop-color='{c}' stop-opacity='.6'/><stop offset='.16' stop-color='{c}' stop-opacity='.88'/>"
           f"<stop offset='.55' stop-color='{c}' stop-opacity='.78'/><stop offset='.86' stop-color='{c}' stop-opacity='.86'/>"
           f"<stop offset='1' stop-color='{c}' stop-opacity='.58'/></linearGradient>"
           f"<filter id='b' x='-2%' y='-30%' width='104%' height='160%' color-interpolation-filters='sRGB'>"
           f"<feTurbulence type='fractalNoise' baseFrequency='0.02 0.22' numOctaves='3' seed='{seed}' result='edge'/>"
           f"<feDisplacementMap in='SourceGraphic' in2='edge' scale='7' xChannelSelector='R' yChannelSelector='G' result='rag'/>"
           f"<feTurbulence type='fractalNoise' baseFrequency='0.0035 0.55' numOctaves='2' seed='{seed + 5}' result='bristle'/>"
           f"<feColorMatrix in='bristle' type='matrix' values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -2.6 2.15' result='streaks'/>"
           f"<feComposite in='rag' in2='streaks' operator='in'/></filter></defs>"
           f"<g filter='url(#b)'><path d='{body}' fill='url(#g)'/>"
           f"<path d='{pass2}' fill='{c}' fill-opacity='.42'/>"
           f"<path d='{fray}' fill='none' stroke='{c}' stroke-opacity='.55' stroke-width='2.2' stroke-linecap='round'/></g></svg>")
    return 'url("data:image/svg+xml,' + quote(svg, safe=" =:/',.-()") + '")'


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
