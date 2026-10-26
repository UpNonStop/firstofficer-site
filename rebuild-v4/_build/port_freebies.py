#!/usr/bin/env python3
"""
Build free-from-the-desk.html (the Freebies page) for the live site.

Inputs
  - the desk page built by the mockup pipeline (rebuild-v4/_build on the
    mockups/rebuild-v4 branch, ffd_c_opts.py -> ffd-c-opt-3h.html). Pass its path
    as argv[1]; default ../fo-v4-wt/rebuild-v4/ffd-c-opt-3h.html.
  - this repo's own chrome: <head>, nav, mobile sheet and footer are taken verbatim
    from field-notes.html, and the running ticker verbatim from index.html, so the
    page closes and opens exactly like every other live page.

What it does
  - keeps the desk shelf as built (cards, filters, search, reading view, deep links)
    and its scripts, and recounts every number on the page from the shelf itself:
    items = sum of each card's data-n, cards = number of cards, trades = trade
    filter options, codes = distinct merchant codes on the shelf.
  - scopes all desk CSS under #ffd so none of it can touch the live nav or footer.
  - copies the photos it needs into img/ph and img/ind, and the desk script into
    assets/ffd/site.js.
  - sign-up forms stay guarded: SIGNUP_LIVE comes from the mockup build
    (False = nothing is posted). Run with --signup-live to post to the same
    Daily Redemption members endpoint the live footer form already uses.

Usage
  FO_SITE=/path/to/site-checkout python3 rebuild-v4/_build/port_freebies.py [--signup-live]
"""
import os, re, sys, shutil, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
# ROOT = a checkout of the live site (main / feature branch); SRC defaults to the 3h build next to this script
ROOT = os.path.abspath(os.environ.get('FO_SITE', os.path.join(HERE, '..', '..', '..', 'fo-main')))
SIGNUP_LIVE = '--signup-live' in sys.argv
sys.argv = [a for a in sys.argv if a != '--signup-live']
SRC = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'ffd-c-opt-3h.html'))
SRCDIR = os.path.dirname(SRC)
OUT = os.path.join(ROOT, 'free-from-the-desk.html')
URL = 'https://firstofficer.upnonstop.com/free-from-the-desk.html'

src = open(SRC, encoding='utf-8').read()
tpl = open(os.path.join(ROOT, 'field-notes.html'), encoding='utf-8').read()
idx = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()


# ------------------------------------------------------------------ CSS scoping
def _split_top(sel):
    out, d, cur = [], 0, ''
    for ch in sel:
        if ch in '([': d += 1
        elif ch in ')]': d -= 1
        if ch == ',' and d == 0:
            out.append(cur); cur = ''
        else:
            cur += ch
    out.append(cur)
    return out


def _lead(sel):
    """split a selector into its first compound and the rest"""
    d = 0
    for i, ch in enumerate(sel):
        if ch in '([': d += 1
        elif ch in ')]': d -= 1
        elif d == 0 and ch in ' >+~':
            return sel[:i], sel[i:]
    return sel, ''


def scope_sel(sel, S='#ffd'):
    sel = sel.strip()
    if not sel:
        return sel
    head, rest = _lead(sel)
    if head in (':root', 'html', 'body'):
        return S + rest
    if head.startswith('html') or head.startswith(':root'):
        r = rest.lstrip()
        if 'rdr-lock' in head and r in ('', 'body'):
            return sel                      # the reading view locks the page scroll itself
        if r.startswith('body'):
            bh, br = _lead(r)
            return f'{head} {S}{bh[4:]}{br}'
        return f'{head} {S}{rest}' if rest else f'{head} {S}'
    if head.startswith('body'):
        return S + head[4:] + rest
    return f'{S} {sel}'


def scope_css(css, S='#ffd'):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out, i, n = [], 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j < 0:
            out.append(css[i:]); break
        pre = css[i:j]
        # find matching brace
        d, k = 1, j + 1
        while k < n and d:
            if css[k] == '{': d += 1
            elif css[k] == '}': d -= 1
            k += 1
        body = css[j + 1:k - 1]
        p = pre.strip()
        # statements like @import / @charset before this block
        semi = pre.rfind(';')
        lead = ''
        if p.startswith('@') is False and semi >= 0 and '{' not in pre:
            lead, pre = pre[:semi + 1], pre[semi + 1:]
            p = pre.strip()
        if p.startswith('@media') or p.startswith('@supports') or p.startswith('@container') or p.startswith('@layer'):
            out.append(f'{lead}{p}{{{scope_css(body, S)}}}')
        elif p.startswith('@'):
            out.append(f'{lead}{p}{{{body}}}')
        else:
            out.append(lead + ','.join(scope_sel(x, S) for x in _split_top(p)) + '{' + body + '}')
        i = k
    return ''.join(out)


# ------------------------------------------------------------------ pieces of the desk page
sh = src[:src.index('</head>')]
css_files = re.findall(r'<link rel="stylesheet" href="(assets/[^"]+\.css)">', sh)
css = ''
for f in css_files:
    c = open(os.path.join(SRCDIR, f), encoding='utf-8').read()
    c = c.replace('url(../fonts/', 'url(assets/ffd/fonts/')
    css += f'\n/* {f} */\n' + c
css += ''.join(re.findall(r'<style[^>]*>(.*?)</style>', sh, re.S))
desk_css = scope_css(css)

body = src[src.index('<body'):]
main = body[body.index('<main'):body.index('<footer')]          # desk + band (section#band)
scripts = body[body.index('</footer>') + len('</footer>'):body.rindex('</body>')]
scripts = scripts.replace('src="assets/site.js"', 'src="assets/ffd/site.js"')
# the reading view and the phone filter bar are mounted inside #ffd so the scoped styles reach them
_n = scripts.count('document.body.appendChild(')
scripts = scripts.replace('document.body.appendChild(', "(document.getElementById('ffd')||document.body).appendChild(")
assert _n == 2, _n
# the phone filter bar docks under the live nav (.fonav), not the mockup's .nav
assert scripts.count("document.querySelector('.nav')") == 1
scripts = scripts.replace("document.querySelector('.nav')", "document.querySelector('.fonav')")
assert scripts.count('var LIVE=false;') == 1
if SIGNUP_LIVE:
    scripts = scripts.replace('var LIVE=false;', 'var LIVE=true;')
scripts = scripts.replace("'Mockup only, nothing was sent. On the live site this adds you to The Daily Redemption.'",
                          "'Nothing was sent yet. Sign-ups from this form open soon.'")
html_tag = re.search(r'<html[^>]*>', src).group(0)

# industry links point at the live industry pages
main = re.sub(r'href="(for-[a-z-]+?)-v2\.html', r'href="\1.html', main)

# ------------------------------------------------------------------ counts, from the shelf itself
grid = main[main.index('id="desk-grid"'):]
cards = re.findall(r'<article class="dk[^"]*"[^>]*data-n="(\d+)"', grid)
N_CARDS = len(cards)
N_ITEMS = sum(int(x) for x in cards)
N_TRADES = len(re.findall(r'<option value="(?!all")', re.search(r'<select id="tradesel".*?</select>', main, re.S).group(0)))
codes = set(re.findall(r'<b>(\d{4})</b>', grid)) | set(re.findall(r'\b(\d{4})\b', ' '.join(re.findall(r'<b class="mcc[^"]*">([^<]*)<', grid))))
mq = set(re.findall(r'<span class="mq-i"><b>(\d{4})</b>', main))
N_CODES = len(codes | mq)


def fix_counts(s):
    s = re.sub(r'<b>\d+</b>smart items', f'<b>{N_ITEMS}</b>smart items', s)
    s = re.sub(r'<b>\d+</b>trades', f'<b>{N_TRADES}</b>trades', s)
    s = re.sub(r'<b>\d+</b>cards on the desk', f'<b>{N_CARDS}</b>cards on the desk', s)
    s = re.sub(r'Search \d+ items', f'Search {N_ITEMS} items', s)
    s = re.sub(r'\b\d+ smart items for business owners', f'{N_ITEMS} smart items for business owners', s)
    return s


main = fix_counts(main)
CODES_TXT = re.search(r'<b>(\d+)</b>merchant codes decoded', main)
# runtime guard: the numbers are re-read from the shelf in the browser too
COUNT_JS = ('<script id="ffd-counts">(function(){var g=document.getElementById("desk-grid");if(!g)return;'
            'var c=g.querySelectorAll("article.dk[data-n]"),n=0;c.forEach(function(a){n+=+a.getAttribute("data-n")||0});'
            'document.querySelectorAll(".deskline span").forEach(function(s){var b=s.querySelector("b");if(!b)return;'
            'if(/smart items/.test(s.textContent))b.textContent=n;else if(/cards on the desk/.test(s.textContent))b.textContent=c.length;});'
            'var q=document.getElementById("deskq");if(q){q.placeholder=q.placeholder.replace(/Search \\d+ items/,"Search "+n+" items");'
            'var d=q.getAttribute("data-short");if(d)q.setAttribute("data-short",d.replace(/\\d+/,n));}})();</script>')

# ------------------------------------------------------------------ live chrome
th = tpl[:tpl.index('</head>')]
TITLE = "Free from the desk | Everything I'd tell you over coffee"
DESC = f"Everything I'd tell you over coffee: {N_ITEMS} smart items for business owners, free to read. Leave your email for the new ones."
th = re.sub(r'<title>.*?</title>', f'<title>{H.escape(TITLE)}</title>', th, count=1)
th = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{H.escape(TITLE)}">', th)
th = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{H.escape(DESC)}">', th)
th = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{H.escape(TITLE)}">', th)
th = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{H.escape(DESC)}">', th)
th = th.replace('https://firstofficer.upnonstop.com/field-notes.html', URL)
# page-specific JSON-LD from field notes: replace with a plain WebPage
th = re.sub(r'<script type="application/ld\+json">.*?</script>',
            lambda m: '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":' +
            '"' + TITLE.replace('"', '') + '","url":"' + URL + '","description":"' + DESC.replace('"', '') + '"}</script>'
            if 'field-notes' in m.group(0) or 'Field Notes' in m.group(0) else m.group(0), th, flags=re.S)
assert 'field-notes.html' not in th.replace('href="field-notes.html"', ''), 'field-notes leftovers in head'
fonts = ('<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800'
         '&family=DM+Serif+Display&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">')
head_js = ''.join(m for m in re.findall(r'<script>.*?</script>', sh, re.S))  # html classes + per-lane card limit
th += head_js + fonts + '\n<style id="ffdcss">\n' + desk_css + '\n#ffd{display:block;position:relative;overflow-x:clip}\n#ffd .rdr{z-index:350}\n</style>\n'

tb = tpl[tpl.index('</head>'):]
nav_end = tb.index('<style id="fncss"')
chrome_top = tb[:nav_end]
foot = tb[tb.index('<div class="fofoot"'):]
ft = re.search(r'<div class="fotick".*?</div></div>', idx, re.S).group(0)
assert ft.count('<div') == 2
# the ticker's styles live only on the home page: take them verbatim
a = idx.index('/* running ticker under the nav */')
b = idx.index('.tk-dot{', a); b = idx.index('}', b) + 1
tick_css = idx[a:b]
if '@keyframes livepulse' not in tpl:
    m = re.search(r'@keyframes livepulse\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}', idx)
    tick_css += '\n' + m.group(0)
th += '<style id="ffdtick">\n' + tick_css + '\n</style>\n'

page = (th + chrome_top + ft + '\n<div id="ffd">' + main + '</div>\n' + foot)
page = page.replace('</body>', scripts + COUNT_JS + '\n</body>')
# html classes the desk sets on <html>
hcls = re.search(r'class="([^"]*)"', html_tag)
if hcls:
    page = page.replace('<html lang="en">', f'<html lang="en" class="{hcls.group(1)}">', 1)
page = page.replace('href="field-notes.html" aria-current="page"', 'href="field-notes.html"')

open(OUT, 'w', encoding='utf-8').write(page)

# ------------------------------------------------------------------ assets
need = set(re.findall(r'img/(?:ph|ind)/[\w.-]+\.(?:webp|jpg|png)', main))
for a in sorted(need):
    os.makedirs(os.path.join(ROOT, os.path.dirname(a)), exist_ok=True)
    shutil.copy2(os.path.join(SRCDIR, a), os.path.join(ROOT, a))
os.makedirs(os.path.join(ROOT, 'assets', 'ffd'), exist_ok=True)
shutil.copy2(os.path.join(SRCDIR, 'assets', 'site.js'), os.path.join(ROOT, 'assets', 'ffd', 'site.js'))
if 'assets/ffd/fonts/' in desk_css:
    os.makedirs(os.path.join(ROOT, 'assets', 'ffd', 'fonts'), exist_ok=True)
    for f in os.listdir(os.path.join(SRCDIR, 'fonts')):
        shutil.copy2(os.path.join(SRCDIR, 'fonts', f), os.path.join(ROOT, 'assets', 'ffd', 'fonts', f))

print(f'free-from-the-desk.html {len(page)} bytes | cards {N_CARDS} items {N_ITEMS} trades {N_TRADES} '
      f'signup-live {SIGNUP_LIVE} | codes-on-page {CODES_TXT.group(1) if CODES_TXT else "-"} codes-found {N_CODES} | assets {len(need)}')
