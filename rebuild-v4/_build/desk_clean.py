"""3h desk: the hand-painted brush, and the 'our own voice' cleanup.

Ohad (Oct 26): the pink highlight must look like a true brush; no source names
and no checked/as-of dates on the page. Everything here runs on the built 3h
HTML in ffd_c_opts.py, and check() fails the build if anything comes back.
"""
import re
from urllib.parse import quote


def _svg(vb, d, c, tf='translate(0 11) scale(1 .8)'):
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='{vb}' preserveAspectRatio='none'>"
           f"<path d='{d}' fill='{c}' transform='{tf}'/></svg>")
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


def brush(color='#FA1896', cap='.8em', full=False):
    """Full CSS background value (three layers) for one solid brush swipe.
    full=True centres the stroke and fills the box height (eyebrow: text sits ON the brush)."""
    tf = 'translate(0 2) scale(1 1)' if full else 'translate(0 11) scale(1 .8)'
    return (f"{_svg('0 0 40 56', BRUSH_L, color, tf)} left center/{cap} 100% no-repeat,"
            f"{_svg('0 0 40 56', BRUSH_R, color, tf)} right center/{cap} 100% no-repeat,"
            f"{_svg('0 0 100 56', BRUSH_M, color, tf)} center/calc(100% - 2*{cap} + 2px) 100% no-repeat")


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


# ---------------------------------------------------------------- email capture (Ohad, Oct 26: "I want their emails",
# then "Put them on The Daily Redemption list and merge the forms")
# Every sign-up on the page goes to The Daily Redemption, wired exactly like the live site-wide
# form (index.html #focapjs): POST JSON to the Ghost members API on www.upnonstop.com,
#   {"email": <email>, "emailType": "signup", "labels": ["First Officer site"], "name": ""}
# Ghost then emails a confirmation (magic) link; the member is created on confirm.
# MOCKUP GUARD: SIGNUP_LIVE is False in the preview, so nothing is posted. Set it to True to go live.
SIGNUP_ENDPOINT = 'https://www.upnonstop.com/members/api/send-magic-link/'
SIGNUP_LABELS = ['First Officer site']
SIGNUP_LIVE = False
TAGLINE = 'New ones go to your inbox.'
TAGLINE_OPTIONS = [
    'Free to read. New ones go to your inbox.',                       # picked
    'Free. Want the new ones first? Leave your email.',
    'Free to read. Leave your email and the next ones come to you.',
    'Free. New notes land in your inbox, one email at a time.',
    'Free to read. Your email gets you the new ones as they land.',
]
# matches how the site describes the list: "One real redemption, every weekday."
MICRO = 'You get The Daily Redemption, every weekday. Leave whenever you like.'


def signup_form(cls, btn, idp, micro=MICRO):
    return (f'<form class="cap {cls}" data-fo-signup data-endpoint="{SIGNUP_ENDPOINT}" data-labels="{",".join(SIGNUP_LABELS)}" novalidate>'
            f'<label class="cap-l" for="{idp}-e">Your email address</label>'
            f'<div class="cap-row"><input id="{idp}-e" type="email" name="email" required autocomplete="email" placeholder="you@yourbusiness.com">'
            f'<button type="submit">{btn}</button></div>'
            + (f'<p class="cap-m">{micro}</p>' if micro else '')
            + '<p class="cap-msg" role="status" aria-live="polite"></p></form>')


# one handler for every [data-fo-signup] form; same request body as the live #focapjs
SIGNUP_JS = ('<script id="fo-signup">(function(){var LIVE=' + ('true' if SIGNUP_LIVE else 'false') + ";\n"
 "document.querySelectorAll('form[data-fo-signup]').forEach(function(f){\n"
 " var i=f.querySelector('input[type=email]'),b=f.querySelector('button'),m=f.querySelector('.cap-msg');\n"
 " f.addEventListener('submit',function(e){e.preventDefault();var v=(i.value||'').trim();\n"
 "  if(!v||v.indexOf('@')<1){m.textContent='Please enter a valid email address.';i.focus();return;}\n"
 "  if(!LIVE){f.classList.add('sent');m.textContent='Mockup only, nothing was sent. On the live site this adds you to The Daily Redemption.';return;}\n"
 "  b.disabled=true;m.textContent='Sending...';\n"
 "  fetch(f.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},\n"
 "   body:JSON.stringify({email:v,emailType:'signup',labels:f.dataset.labels.split(','),name:''})})\n"
 "  .then(function(r){if(r.ok){f.classList.add('sent');f.querySelector('.cap-row').style.display='none';m.textContent='Check your inbox for the confirmation link.';\n"
 "    if(typeof gtag==='function')gtag('event','newsletter_signup',{page_path:location.pathname});}\n"
 "   else{b.disabled=false;m.textContent='That did not go through. Try again in a moment.';}})\n"
 "  .catch(function(){b.disabled=false;m.textContent='That did not go through. Try again in a moment.';});});});})();</script>")

EMAIL_REWRITES = [
    # lede tagline
    ('Free. <span class="hl">No email. No catch.</span></p>',
     f'Free to read. <strong class="tl">{TAGLINE}</strong></p>' + signup_form('cap-hero', 'Send me new ones', 'caph')),
    # meta description
    ('for business owners, free. No email. No catch.', 'for business owners, free to read. Leave your email for the new ones.'),
    # stats row: the '0 emails asked for' cell becomes the real card count shown on the shelves
    ('<span><b>0</b>emails asked for</span>', '<span><b>109</b>cards on the desk</span>'),
]

# the one bottom sign-up: the site-wide Daily Redemption band, re-dressed as a desk ticket
DR_OLD = re.compile(r'<div class="card news" id="focap"[^>]*>.*?</form></div>', re.S)
DR_NEW = ('<div class="dr" id="focap" data-rv><div class="dr-stub"><span class="dr-k">The Daily Redemption</span>'
          '<span class="dr-f">Every weekday</span></div><div class="dr-main">'
          '<h3 class="dr-h">New freebies and notes from the desk, in your inbox.</h3>'
          '<p class="dr-s">The Daily Redemption is the newsletter behind the desk: one real redemption every weekday, '
          'and the new freebies as they land. Free, and you can leave whenever you like.</p>'
          + signup_form('cap-dr', 'Get the newsletter', 'capd', micro='') + '</div></div>')


def capture(s):
    for a, b in EMAIL_REWRITES:
        assert s.count(a) == 1, f'capture rewrite target missing: {a[:60]}'
        s = s.replace(a, b)
    assert len(DR_OLD.findall(s)) == 1, 'Daily Redemption band not found'
    s = DR_OLD.sub(lambda m: DR_NEW, s)
    assert s.count('</body>') == 1
    s = s.replace('</body>', SIGNUP_JS + '\n</body>')
    bad = [m.group(0) for m in re.finditer(r'(?i)no e-?mails?\b|no sign-?ups?|no catch|emails asked for', s)]
    assert not bad, f'email copy contradicts the capture: {bad}'
    forms = re.findall(r'<form[^>]*>.*?</form>', s, re.S)
    sign = [f for f in forms if 'data-fo-signup' in f]
    assert len(sign) == 2, 'expected exactly two Daily Redemption sign-ups (hero + band)'
    assert not [f for f in forms if 'type="email"' in f and 'data-fo-signup' not in f], 'unwired email form left'
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


# ---------------------------------------------------------------- Ohad pt190u: the things 3h had dropped
# rotating hero photos: the same set and timing as the Freebies hero on rebuild-v3 (section#fftop .phx);
# site.js crossfades them (2.4s), pauses off-screen and stays still under prefers-reduced-motion.
HERO_PH = ['i-desk', 'e-coffee', 'e-laptop', 'e-tablet']
HERO_IV = 6500


def hero_photos(s):
    tag = '<div class="pop-hero bleed">'
    assert s.count(tag) == 1
    phx = (f'<div class="phx" data-iv="{HERO_IV}" data-ph="' + ','.join(f'img/ph/{n}.webp' for n in HERO_PH)
           + '" aria-hidden="true"></div>')
    return s.replace(tag, tag + phx)


# the desk's Golden Nugget, redrawn flat: one faceted nugget in brand golds, ink outline,
# three pink glints (the prior page's nugget icon, refined). No bar, no 3D, no circles.
NUGGET = ("<svg class=\"nugart\" viewBox=\"0 0 64 64\" aria-hidden=\"true\" focusable=\"false\">"
          "<path d=\"M9 37 L15 23 L27 15 L41 16 L53 25 L56 39 L46 50 L28 53 L14 47 Z\" fill=\"#E8C547\"/>"
          "<path d=\"M15 23 L27 15 L41 16 L35 28 L22 30 Z\" fill=\"#FBE9A6\"/>"
          "<path d=\"M41 16 L53 25 L56 39 L44 36 L35 28 Z\" fill=\"#D7AA2E\"/>"
          "<path d=\"M22 30 L35 28 L44 36 L34 44 L20 42 Z\" fill=\"#F2D266\"/>"
          "<path d=\"M9 37 L15 23 L22 30 L20 42 L14 47 Z\" fill=\"#DDB73E\"/>"
          "<path d=\"M20 42 L34 44 L44 36 L56 39 L46 50 L28 53 L14 47 Z\" fill=\"#B98A1E\"/>"
          "<path d=\"M15 23 L22 30 L35 28 L41 16 M22 30 L20 42 L34 44 L44 36 L35 28 M44 36 L56 39 M20 42 L14 47 M34 44 L28 53\" fill=\"none\" stroke=\"#141216\" stroke-opacity=\".28\" stroke-width=\"1.3\" stroke-linejoin=\"round\"/>"
          "<path d=\"M9 37 L15 23 L27 15 L41 16 L53 25 L56 39 L46 50 L28 53 L14 47 Z\" fill=\"none\" stroke=\"#141216\" stroke-width=\"2.4\" stroke-linejoin=\"round\"/>"
          "<path d=\"M50 9 l1.6 -5 M55.5 14 l5 -1.2 M46 6.5 l-1 -4\" stroke=\"#FA1896\" stroke-width=\"2.4\" stroke-linecap=\"round\"/>"
          "</svg>")


def nug_art(s):
    a = '<a class="pv pv1" href="#nug-cards" data-open="nug-cards">'
    g = '<div class="grp" data-grp="nuggets"><h2>Golden Nuggets</h2>'
    c = re.search(r'<article class="dk gold" id="nug-cards"[^>]*>', s)
    assert s.count(a) == 1 and s.count(g) == 1 and c
    s = s.replace(a, a + NUGGET).replace(g, g + NUGGET)
    return s.replace(c.group(0), c.group(0) + NUGGET, 1)
