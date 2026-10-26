#!/usr/bin/env python3
"""Ohad pt193u: one top nav sitewide on the live site (feature/freebies-3h).

Desktop .fonav .links and the top of the mobile .nsheet menu:
    Product, Pricing, Freebies (pink brush marker, same marker as the v4 mockup nav), Calculator, About
How is not a top-nav item: how.html stays reachable from the Product page and the footer (sitedir: How It Works).
Trust and Your Industry sit in the footer and at the end of the mobile menu.
Freebies carries aria-current="page" on free-from-the-desk.html.

Usage: FO_SITE=/workspace/fo-main python3 rebuild-v4/_build/live_nav.py [--write]   (dry run by default)
Idempotent: re-running rewrites the same nav.
"""
import glob, os, re, sys

SITE = os.environ.get('FO_SITE', '/workspace/fo-main')
WRITE = '--write' in sys.argv
FREEBIES = 'free-from-the-desk.html'
MARK = ('<svg class="fzmk" viewBox="0 0 100 24" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
        '<path pathLength="1" d="M4 15.5C18 13.2 31 14.6 46 12.9S77 12.2 96 10.6"/>'
        '<path class="b" pathLength="1" d="M6 11.4C24 10.8 40 12.1 58 10.4S84 9.6 93 8.9"/></svg>')
CSS = ('<style id="navfz">'
       '/* Freebies: hand-drawn pink highlighter swipe behind the word (v4 mockup nav marker) */'
       '.fonav .links a.fz{color:var(--ink);font-weight:600}'
       '.fz>span{position:relative;z-index:0;display:inline-block}'
       '.fzmk{position:absolute;z-index:-1;left:-6px;top:-.16em;width:calc(100% + 12px);height:1.2em;transform:rotate(-2deg);overflow:visible;pointer-events:none}'
       '.fzmk path{fill:none;stroke:#FA1896;stroke-opacity:.4;stroke-width:9;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke;stroke-dasharray:1;stroke-dashoffset:1;animation:fzDraw .6s cubic-bezier(.6,.05,.3,1) .35s forwards}'
       '.fzmk path.b{stroke-opacity:.18;stroke-width:6;animation-delay:.5s}'
       '.fz[aria-current="page"] .fzmk path{stroke-opacity:.55}.fz[aria-current="page"] .fzmk path.b{stroke-opacity:.26}'
       '@keyframes fzDraw{to{stroke-dashoffset:0}}'
       '@media(prefers-reduced-motion:reduce){.fzmk path{animation:none;stroke-dashoffset:0}}'
       '</style>')
A = re.compile(r'<a href="([^"]*)"([^>]*)>([^<]*)</a>')


def links_of(block):
    return {t.strip(): (h, rest) for h, rest, t in A.findall(block)}


def fz(prefix, active, onclick=''):
    cur = ' aria-current="page"' if active else ''
    return f'<a class="fz" href="{prefix}{FREEBIES}"{cur}{onclick}><span>{MARK}Freebies</span></a>'


def build(old, prefix, active, mobile, has_ind):
    got = links_of(old)
    def a(label, default_href, default_rest=''):
        h, rest = got.get(label, (default_href, default_rest))
        return f'<a href="{h}"{rest}>{label}</a>'
    oc = ' onclick="foNav(false)"' if mobile else ''
    top = (a('Product', prefix + 'product.html') + a('Pricing', prefix + 'pricing.html', oc)
           + fz(prefix, active) + a('Calculator', prefix + 'calculator.html', oc) + a('About', prefix + 'about.html', oc))
    if not mobile:
        return top
    ind = ('#industries', oc) if has_ind else (prefix + 'index.html#industries', '')
    return (top + a('Field Notes', prefix + 'field-notes.html') + a('The Daily Redemption', 'https://upnonstop.com')
            + a('Your Industry', *ind) + a('Trust', prefix + 'trust.html'))


changed = []
for f in sorted(glob.glob(os.path.join(SITE, '*.html'))):
    s = open(f, encoding='utf-8').read()
    m = re.search(r'(<div class="links">)(.*?)(</div>)', s, re.S)
    if not m:
        continue
    name = os.path.basename(f)
    active = name == FREEBIES
    pm = re.search(r'href="([^"]*?)product\.html"', m.group(2))
    prefix = pm.group(1) if pm else ''
    t = s[:m.start(2)] + build(m.group(2), prefix, active, False, False) + s[m.end(2):]
    n = re.search(r'(<nav class="nlist">)(.*?)(</nav>)', t, re.S)
    if n:
        t = t[:n.start(2)] + build(n.group(2), prefix, active, True, 'id="industries"' in t) + t[n.end(2):]
    t = re.sub(r'<style id="navfz">.*?</style>', '', t, flags=re.S)
    t = t.replace('</head>', CSS + '</head>', 1)
    assert 'how.html">How</a>' not in t[m.start():m.start() + 4000]
    if t != s:
        changed.append(name)
        if WRITE:
            open(f, 'w', encoding='utf-8').write(t)
print(('wrote' if WRITE else 'would change'), len(changed), 'pages:', ' '.join(changed))
