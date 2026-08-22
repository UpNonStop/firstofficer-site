#!/usr/bin/env python3
"""First Officer site battery — the gate that actually fails.

Usage:
  python3 tools/battery.py            # run all checks (rendered pass runs if playwright is installed)
  python3 tools/battery.py --static   # static checks only
  python3 tools/battery.py --stamp N  # after a PASSING run: stamp BUILD_MANIFEST.json as build N

Rules of the house this battery enforces (history: builds 133-160 kept re-breaking these):
  - every class used in markup has a selector on the same page
  - a capture band is a full component: section.focap wrapper + all form CSS + focapjs
  - no card-issuer names in any served text (deny-list below); transfer partners and vendors are fine
  - the footer ftsep dot stays dead
  - the a/an typos stay fixed
  - every content page carries Do Not Sell + the advisor disclaimer; value-quoting pages carry l4note
  - internal links and sitemap resolve
  - rendered: no JS errors, no naked full-width text, heroes keep photo+scrim, nav pins on scroll,
    capture forms are styled — checked at 1440px AND after scrolling
Regenerating any page (a "restamp") without re-running this battery is how every regression happened.
"""
import re, sys, os, glob, json, hashlib

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FAIL = []
def fail(check, f, detail): FAIL.append((check, f, str(detail)[:160]))

DENY = re.compile(r'\bInk\b|\bSapphire\b|Freedom Flex|\bBBP\b|Blue Business|\bUR\b|\bMR\b'
                  r'|Ultimate Rewards|Membership Rewards|\bAmex\b|American Express|\bChase\b'
                  r'|\bCSP\b|\bCSR\b|\bCiti\b|Capital One')
TYPOS = [' a agency ', ' a ecommerce ', ' a HVAC ', ' a IT ', ' a auto ']
CLASS_WHITELIST = {'ft-disc'}          # styled inline where used
VAR_WHITELIST = {'--h', '--ph'}        # legacy/runtime-set (ab5js, herospin)
VAL_RE = re.compile(r'[\d,]{3,}\s*(?:points|pts)\s*(?:=|as|worth|to)\s*\$|=\s*\$[\d,]+'
                    r'|points?\s+at\s+about\s+a\s+penny|prices?\s+your\s+points')

pages = sorted(glob.glob('*.html'))
content = [f for f in pages if 'http-equiv="refresh"' not in open(f).read()]
shells = [f for f in pages if f not in content]
HB = {'hb-license-x7.html', 'hb-review-x7.html'}

for f in content:
    src = open(f).read()
    css = '\n'.join(m.group(1) for m in re.finditer(r'<style[^>]*>(.*?)</style>', src, re.S))
    body = re.sub(r'<script.*?</script>|<style.*?</style>', '', src, flags=re.S)

    # 1. class-def gate
    cls = {c for m in re.finditer(r'class="([^"]+)"', body) for c in m.group(1).split()
           if not c.startswith('js-') and c not in CLASS_WHITELIST}
    for c in sorted(cls):
        if not re.search(r'\.' + re.escape(c) + r'[\s{.,:#>\[)+~]', css):
            fail('class-def', f, c)

    # 2. var gate
    for m in re.finditer(r'var\((--[\w-]+)\)', src):
        v = m.group(1)
        if v not in VAR_WHITELIST and v + ':' not in src:
            fail('var-def', f, v)

    # 3. focap integrity
    if 'focap-in' in body:
        if '<section class="focap"' not in src: fail('focap', f, 'missing section.focap wrapper')
        for c in ['focap-in','focap-k','focap-h','focap-s','focap-f','focap-i','focap-b','focap-msg']:
            if not re.search(r'\.' + c + r'[\s{.,:]', css): fail('focap', f, 'missing CSS .' + c)
        if 'id="focapjs"' not in src: fail('focap', f, 'missing focapjs')

    # 4. issuer deny-list (ignore base64 payloads)
    scan = re.sub(r'data:image/[^"\']+', '', src)
    for m in DENY.finditer(scan):
        s = max(0, m.start()-60)
        fail('issuer', f, f"{m.group(0)} :: {scan[s:m.end()+60]}")

    # 5. ftsep kill
    if 'class="ftsep"' in src and not re.search(r'\.ftsep\{display:none', src):
        fail('ftsep', f, 'dot not killed')

    # 6. typos
    for t in TYPOS:
        if t in src: fail('typo', f, t)

    # 7. compliance
    if f not in HB and f != '404.html':
        if 'href="privacy.html">Do Not Sell My Info<' not in src: fail('compliance', f, 'no Do Not Sell footer link')
        if 'not a licensed financial advisor' not in src: fail('compliance', f, 'no disclaimer')

    # 8. l4 on value-quoting pages
    text = re.sub(r'<[^>]+>', ' ', body)
    if f not in HB and VAL_RE.search(text) and 'l4note' not in src:
        fail('l4', f, 'quotes values without l4note')

    # 9. internal links
    for m in re.finditer(r'href="([a-zA-Z0-9-]+\.html)', src):
        if not os.path.exists(m.group(1)): fail('links', f, m.group(1))

# sitemap
for u in re.findall(r'<loc>https://firstofficer\.upnonstop\.com/([^<]*)</loc>', open('sitemap.xml').read()):
    if u and not os.path.exists(u): fail('sitemap', 'sitemap.xml', u)

static_fail = len(FAIL)
rendered = 'skipped'
if '--static' not in sys.argv:
    try:
        from playwright.sync_api import sync_playwright
        rendered = 0
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            pg = b.new_page(viewport={'width': 1440, 'height': 820})
            pg.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file://') else r.abort())
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)[:90]))
            for f in content:
                errs.clear()
                pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(280)
                r = pg.evaluate("""() => {
                  const out = {naked: 0};
                  for (const el of document.querySelectorAll('p,h1,h2,h3,li,blockquote,div')) {
                    if (el.children.length > 0 && el.tagName === 'DIV') continue;
                    const t = (el.textContent || '').trim(); if (t.length < 40) continue;
                    const rc = el.getBoundingClientRect(); if (rc.width === 0) continue;
                    if (rc.left < 15 && rc.width > 1200) out.naked++;
                  }
                  const top = document.getElementById('top');
                  if (top && top.className.includes('secphoto')) {
                    out.photo = getComputedStyle(top, '::before').backgroundImage !== 'none';
                    out.scrim = getComputedStyle(top, '::after').backgroundImage.includes('linear-gradient');
                  }
                  const fi = document.getElementById('focapEmail');
                  if (fi) {
                    out.fi = parseInt(getComputedStyle(fi).borderRadius) > 20;
                    const bt = document.querySelector('.focap-b');
                    out.fb = bt ? getComputedStyle(bt).backgroundColor === 'rgb(250, 24, 150)' : false;
                  }
                  const ft = document.querySelector('.ftsep');
                  if (ft) out.ftHidden = getComputedStyle(ft).display === 'none';
                  return out;
                }""")
                pg.evaluate("window.scrollTo(0,2000)"); pg.wait_for_timeout(220)
                nav = pg.evaluate("""() => { const n = document.querySelector('.fonav'); if (!n) return null;
                  const rc = n.getBoundingClientRect();
                  return ['fixed','sticky'].includes(getComputedStyle(n).position) && rc.y <= 1 && rc.y > -2; }""")
                if r['naked'] and f not in HB: fail('naked', f, r['naked'])
                if r.get('photo') is False: fail('hero', f, 'no photo layer')
                if r.get('scrim') is False: fail('hero', f, 'no scrim')
                if r.get('fi') is False or r.get('fb') is False: fail('focap-render', f, 'form unstyled')
                if r.get('ftHidden') is False: fail('ftsep-render', f, 'dot visible')
                if nav is False and f not in HB: fail('nav-pin', f, 'nav not pinned at scroll')
                if errs and f not in HB: fail('jserror', f, errs[0])
                rendered += 1
            b.close()
    except ImportError:
        print('NOTE: playwright not available, rendered checks skipped')

print(f"\npages: {len(content)} content / {len(shells)} shells | rendered: {rendered}")
if FAIL:
    print(f"BATTERY FAIL — {len(FAIL)} finding(s):")
    for c, f, d in FAIL: print(f"  [{c}] {f}: {d}")
    sys.exit(1)
print("BATTERY PASS")

if '--stamp' in sys.argv:
    n = int(sys.argv[sys.argv.index('--stamp') + 1])
    import datetime
    m = json.load(open('BUILD_MANIFEST.json'))
    sha = {f: hashlib.sha256(open(f,'rb').read()).hexdigest()[:16] for f in pages}
    m.update(build=n, generated=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             files=len(sha), sha256=sha)
    m['battery'] = {'static_findings': 0, 'rendered_pages': rendered,
                    'content_pages': len(content), 'shells': len(shells)}
    json.dump(m, open('BUILD_MANIFEST.json','w'), indent=2)
    print(f"stamped BUILD_MANIFEST.json build {n} ({len(sha)} files hashed)")
