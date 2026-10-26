import json, html as H
import os; ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # builds into this checkout
WA='https://wa.me/16199404040?text=First%20Officer'
APPROVED="Your strategy is reviewed and fine-tuned by a person before it reaches you. Every redemption is booked by a person. Day-to-day answers are software-led, and a person steps in when needed."
DATANOTE="Client stories are shared with permission. Names, figures and examples on this page may be illustrative or altered to protect privacy."
TICK_HTML=open(ROOT+'/_build/ticker.html').read().strip()
HERO_SUB="Every loyalty program has their team constantly rewriting the rules. While you're busy running your business, your spend earns less than it should, and your points and miles buy less than they could.\n\nFirstOfficer by UpNonStop runs a desk of specialists across 50+ programs, each an expert in its niche. They all work for you, so you skip those rookie mistakes. Your Bespoke Strategy is reviewed weekly and optimized continuously, so every dollar you spend works harder.\n\nSame spend. More points. Better trips, for fewer points."
INDS=[('agencies','Agencies','📣'),('auto-repair','Auto Repair','🔧'),('cleaning','Cleaning','🧽'),('consulting','Consulting','💼'),('contractors','Contractors','🏗️'),('cpa-firms','CPA Firms','🧮'),('dental','Dental','🦷'),('ecommerce','E-Commerce','📦'),('fitness','Fitness','🏋️'),('hvac','HVAC','❄️'),('it-services','IT & MSP','🖥️'),('landscaping','Landscaping','🌿'),('law-firms','Law Firms','⚖️'),('medical','Medical','🩺'),('property-management','Property Management','🏢'),('real-estate','Real Estate','🏡'),('restaurants','Restaurants','🍽️'),('salons','Salons','💇'),('trucking','Trucking','🚚'),('veterinary','Veterinary','🐾')]
# ticker + hero keep their own fonts (verbatim / faithful port); site sections use Inter from the app.
TICK_FONT='<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">'
HERO_FONTS='<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;0,9..40,900;1,9..40,400&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">'
MK='<span class="mk"><img src="img/fo-chevron-transparent-v2.png" alt=""></span>'

def ph(names, iv=8000):
    return f'<div class="phx" data-iv="{iv}" data-ph="{",".join("img/ph/"+n+".webp" for n in names)}" aria-hidden="true"></div>'
def head(lab, h, lede='', cls='', labc=''):
    return f'<div class="head {cls}" data-rv><span class="lab {labc}">{lab}</span><h2 class="h2">{h}</h2>{f"<p class=lede>{lede}</p>" if lede else ""}</div>'
def kv(k, v, cls=''): return f'<div class="kv {cls}"><span>{k}</span><b>{v}</b></div>'
def meter(w, c='', dl=0): return f'<div class="meter"><i style="--w:{w:.1f}%;{("--c:"+c+";") if c else ""}--dl:{dl}s"></i></div>'
def bar(label, val, w, c='', sub='', cls='', dl=0):
    return f'<div class="{cls}"><div class="ln"><span>{label}{f"<small>{sub}</small>" if sub else ""}</span><b>{val}</b></div><div class="bar"><i style="--w:{w:.1f}%;{("--c:"+c+";") if c else ""}--dl:{dl}s"></i></div></div>'
def row(t, s='', v='', c='', extra='', cls='', href=None, vsub=''):
    tag='a' if href else 'div'; hr=f' href="{href}"' if href else ''
    vv=f'<span class="v">{v}{f"<small>{vsub}</small>" if vsub else ""}</span>' if v else ''
    return f'<{tag} class="row {cls}"{hr}><span class="dot" style="--c:{c or "var(--gold2)"}"></span><span class="bd"><span class="t">{t}</span>{f"<span class=s>{s}</span>" if s else ""}{extra}</span>{vv}</{tag}>'
def tl(steps):
    o=''
    for st,t,d,ss in steps:
        o+=f'<div class="st {st}"><span class="dt"></span><span class="t">{t}</span><span class="ss">{ss}</span><span class="d">{d}</span></div>'
    return f'<div class="tl">{o}</div>'

def nav():
    links=[('product.html','Product'),('pricing.html','Pricing'),('how.html','How'),('trust.html','Trust'),('calculator.html','Calculator'),('about.html','About'),('industries.html','Industries')]
    MARK='<svg class="fzmk" viewBox="0 0 100 24" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path pathLength="1" d="M4 15.5C18 13.2 31 14.6 46 12.9S77 12.2 96 10.6"/><path class="b" pathLength="1" d="M6 11.4C24 10.8 40 12.1 58 10.4S84 9.6 93 8.9"/></svg>'
    FZ=f'<a class="fz" href="free-from-the-desk.html"><span>{MARK}Freebies</span></a>'  # hand-drawn pink highlighter swipe
    nl=''.join(f'<a href="{h}">{t}</a>'+(FZ if h=='pricing.html' else '') for h,t in links)
    sh=''.join(f'<a href="{h}">{t}</a>' for h,t in links)+FZ+'<a href="field-notes.html">Field Notes</a>'+'<span class="lab" style="display:block;margin:18px 0 4px">Your industry</span><div class="sind">'+''.join(f'<a href="for-{a}.html">{e} {n}</a>' for a,n,e in INDS)+'</div>'
    return f'''<header class="nav"><div class="nav-in">
<a class="brand" href="home.html" aria-label="First Officer home">{MK}<span><b>First Officer</b><small>by UpNonStop™</small></span></a>
<nav class="nlinks" aria-label="Main">{nl}</nav>
<div class="ncta"><a class="btn-sm wa" href="{WA}" title="Texting is coming soon. WhatsApp for now." aria-label="Text Your First Officer (WhatsApp for now)">💬<span class="t">Text Your First Officer</span></a><a class="btn-sm pk" href="book.html">Get your desk</a>
<button class="burger" aria-label="Open menu" onclick="document.querySelector('.sheet').classList.toggle('open')"><i></i></button></div>
</div><div class="nsub">{FZ}</div></header>
<div class="sheet">{sh}<a class="btn wa" href="{WA}">💬 Text Your First Officer</a><a class="btn" href="book.html">Get your desk</a></div>'''

def footer(src):
    endcta='' if src in ('book','for-dental') else f'''<div class="card hero cta-card" data-rv>{MK}
<h2 class="h2">Your Competitors Route Their Spend. Do You?</h2><p class="lede">The Found Money Call: free, 20 minutes, 6 questions, on the channel you choose. Your capture number, computed. An honest no if the math says no.</p>
<div class="btns"><a class="btn" href="book.html?from={src}">Book Your "Found Money" Call</a><a class="btn ghost" href="#focap">Get the weekday note</a></div></div>'''
    ind=''.join(f'<a href="for-{s}.html">{n}</a>' for s,n,_ in INDS)
    return f'''<section class="sec" id="band">{ph(['d-bali','bg-05','d-maldives'])}<div class="wrap">{endcta}
<div class="card news" id="focap" style="margin-top:12px" data-rv><span class="lab gold">The Daily Redemption</span><h3 class="h3" style="margin-top:8px">One real redemption, every weekday.</h3>
<p style="margin-top:6px">The newsletter behind the desk: what the desk found on request, what it cost in points, and what it would have cost in cash. Free, and you can leave whenever you like.</p>
<form onsubmit="return false"><input type="email" placeholder="you@yourbusiness.com" aria-label="Your email address"><button class="btn" type="submit">Get the newsletter</button></form></div></div></section>
<footer class="foot"><div class="wrap">
<p class="dn">{DATANOTE}</p>
<div class="fdir">
<div class="fb"><a class="brand" href="home.html">{MK}<span><b>First Officer</b><small>by UpNonStop™</small></span></a><p>A desk of specialists across 96 programs, working for your business spend.</p></div>
<div><span class="lab">Product</span><a href="pricing.html">Pricing</a><a href="how.html">How It Works</a><a href="product.html">The Product</a><a href="strategist.html">The Strategist</a><a href="trust.html">Trust &amp; Security</a><a href="calculator.html">Run The Numbers</a><a href="app.html">The App <span class="soon">Soon</span></a></div>
<div class="ind"><span class="lab">Your Industry</span><div class="lst">{ind}</div><a href="industries.html" style="color:var(--pink2);font-weight:600">All industries →</a></div>
<div><span class="lab">Free</span><a href="free-from-the-desk.html">Free From the Desk</a><a href="field-notes.html">Field Notes</a><a href="upns.html">The Intelligence Report</a><a href="https://upnonstop.com">The Daily Redemption</a><a href="hello.html">The Long Version</a></div>
<div><span class="lab">Company</span><a href="about.html">About</a><a href="connect.html">Connect</a><a href="privacy-policy.html">Privacy Policy</a><a href="privacy-policy.html#do-not-sell">Do Not Sell My Info</a><a href="terms-of-service.html">Terms of Service</a><a href="disclaimer.html">Disclaimer</a></div>
</div>
<div class="fbar"><div>UpNonStop | 235 Pavonia Avenue | Jersey City, NJ 07302 | Proudly Made in 🇺🇸</div><div>Independent: no affiliate relationships with any issuer. An educational tool, not a licensed financial advisor. US businesses only. © 2026 UpNonStop.</div></div>
</div></footer>'''

def page(name, title, body, desc='', hero=False, src='site', tail=''):
    fonts=TICK_FONT+(HERO_FONTS if hero else '')
    hh=('<script>window.FO_SUBHEAD='+json.dumps(HERO_SUB)+';</script>') if hero else ''
    scripts=('<script src="hero/fo-hero-data.js"></script><script src="hero/fo-hero-app.js"></script><script src="hero/fo-hero.js"></script>' if hero else '')+tail+'<script src="assets/site.js"></script>'
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{H.escape(desc)}"><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{fonts}
<link rel="preload" href="fonts/InterVariable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="img/fo-chevron-transparent-v2.png"><link rel="stylesheet" href="assets/fo-site-tokens.css"><link rel="stylesheet" href="assets/fo-site.css"><link rel="stylesheet" href="assets/hero-frame.css">{hh}</head><body>
<!-- MOCKUP · First Officer rebuild v3 (app design language) · static HTML, not production -->
{nav()}
{TICK_HTML}
<main id="main">{body}</main>
{footer(src)}
{scripts}</body></html>'''
    open(f'{ROOT}/{name}','w').write(html); print(name, len(html))
