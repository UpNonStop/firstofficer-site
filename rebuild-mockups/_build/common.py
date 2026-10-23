import re, json, os, html as H
ROOT='/workspace/fo-rebuild-mockups'
SRC='/workspace/fo-rebuild-src'
V2='/workspace/fo-home-v2'
WA='https://wa.me/16199404040?text=First%20Officer'
INDS=[('agencies','Agencies','📣'),('auto-repair','Auto Repair','🔧'),('cleaning','Cleaning','🧽'),('consulting','Consulting','💼'),('contractors','Contractors','🏗️'),('cpa-firms','CPA Firms','🧮'),('dental','Dental','🦷'),('ecommerce','E-Commerce','📦'),('fitness','Fitness','🏋️'),('hvac','HVAC','❄️'),('it-services','IT & MSP','🖥️'),('landscaping','Landscaping','🌿'),('law-firms','Law Firms','⚖️'),('medical','Medical','🩺'),('property-management','Property Management','🏢'),('real-estate','Real Estate','🏡'),('restaurants','Restaurants','🍽️'),('salons','Salons','💇'),('trucking','Trucking','🚚'),('veterinary','Veterinary','🐾')]
APPROVED="Your strategy is reviewed and fine-tuned by a person before it reaches you. Every redemption is booked by a person. Day-to-day answers are software-led, and a person steps in when needed."
DATANOTE="Client stories are shared with permission. Names, figures and examples on this page may be illustrative or altered to protect privacy."
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">'
HERO_FONTS='<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;0,9..40,900;1,9..40,400&family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'

def nav(pre='', active=''):
    L=[('product.html','Product'),('pricing.html','Pricing'),('how.html','How'),('trust.html','Trust'),('calculator.html','Calculator'),('about.html','About')]
    links=''.join(f'<a href="{pre}{h}"{" class=on" if h==active else ""}>{t}</a>' for h,t in L)
    dd=''.join(f'<a href="{pre}for-{s}.html"><span>{e}</span>{n}</a>' for s,n,e in INDS)
    sheet=''.join(f'<a href="{pre}{h}">{t}</a>' for h,t in L)+'<details><summary>Industries ▾</summary>'+''.join(f'<a href="{pre}for-{s}.html">{e} {n}</a>' for s,n,e in INDS)+f'<a href="{pre}industries.html">All industries →</a></details><a href="{pre}free-from-the-desk.html">Free From the Desk</a><a href="{pre}field-notes.html">Field Notes</a>'
    return f'''<header class="fonav"><div class="fonav-in">
<a class="brand" href="{pre}home.html" aria-label="First Officer home"><img src="{pre}img/fo-chevron-alpha.png" alt=""><div><div class="n">First Officer</div><div class="by">by UpNonStop™</div></div></a>
<nav class="nlinks" aria-label="Main">{links}<div class="dd"><button type="button" aria-haspopup="true">Industries</button><div class="ddm"><div class="ddh"><span>Your industry</span><a href="{pre}industries.html">All 20 →</a></div>{dd}</div></div></nav>
<div class="ncta"><a class="pill green sm" href="{WA}" title="Texting is coming soon. WhatsApp for now.">💬 Text Your First Officer</a><a class="pill green wa-ic" href="{WA}" aria-label="Text Your First Officer (WhatsApp for now)">💬</a><a class="pill pink sm" href="{pre}book.html">Get your desk</a></div>
<button class="nburger" aria-label="Open menu" onclick="document.querySelector('.nsheet').classList.toggle('open')"><span></span><span></span><span></span></button>
</div></header>
<div class="nsheet">{sheet}<a class="pill green" href="{WA}">💬 Text Your First Officer</a><a class="pill pink" href="{pre}book.html">Get your desk</a></div>'''

TICK=[('HVAC contractor','$4,000','Bonus cleared'),('E-commerce owner','$6,940','Transfer bonus caught'),('Real estate broker','$2,300','Hotel nights on points'),('Trucking operator','$1,760','Fleet fuel rerouted'),('Agency founder','$1,240','Ad spend moved to 3x'),('IT / MSP owner','$1,130','SaaS stack restacked'),('Law firm partner','$980','Retention offer landed'),('Restaurant group','$890','Amber gate, working'),('Dental practice','$610','Wholesale flag cleared'),('Landscaper','','Honest no under the bar, told free')]
def ticker():
    items=''.join(f'<span><b>{a}</b> <span class="v">{v}</span> {t}</span>' for a,v,t in TICK)
    one=f'<span class="lab">◉ A month at the desk, illustrated</span>{items}'
    return f'<div class="ticker" aria-label="Illustrative month"><div class="tk-in">{one}{one}</div></div>'

def live_ticker(kind, pre=''):
    """The live site's ticker, exactly as on origin/main (8587e8d): home gets index.html's .fotick, hello gets
    hello.html's .tickerbar. Markup is the verbatim live fragment (not run through the copy fixes); CSS and JS are
    in assets/live-ticker.css / live-ticker.js."""
    import os
    frag=open(os.path.join(os.path.dirname(__file__),f'live_ticker_{kind}.html')).read()
    js=f'<script src="{pre}assets/live-ticker.js"></script>' if kind=='hello' else ''
    return f'<link rel="stylesheet" href="{pre}assets/live-ticker.css">{frag}{js}'

def pinkband(pre='', src='site', h='Your Competitors Route Their Spend. Do You?', p='The Found Money Call: free, 20 minutes, 6 questions, on the channel you choose. Your capture number, computed. An honest no if the math says no.'):
    return f'''<section class="pinkband"><img class="mk" src="{pre}img/fo-chevron-alpha.png" alt=""><h2>{h}</h2><p>{p}</p>
<div class="ctas"><a class="pill white" href="{pre}book.html?from={src}">Book Your "Found Money" Call</a><a class="pill outline" href="#focap">Get the weekday note</a></div></section>'''

def footer(pre='', band=True, src='site', datanote=True):
    ind=''.join(f'<a href="{pre}for-{s}.html">{n}</a>' for s,n,e in INDS)
    out=(pinkband(pre,src) if band else '')+f'''<footer class="fofoot">
<section class="focap" id="focap"><div class="focap-k">The Daily Redemption</div><h2>One real redemption, every weekday.</h2>
<p>The newsletter behind the desk: what the desk found on request, what it cost in points, and what it would have cost in cash. Free, and you can leave whenever you like.</p>
<form onsubmit="return false"><input type="email" placeholder="you@yourbusiness.com" aria-label="Your email address"><button class="pill pink" type="submit">Get the newsletter</button></form></section>
{f'<p class="fo-datanote">{DATANOTE}</p>' if datanote else ''}
<div class="sitedir">
<div class="fbrand"><img src="{pre}img/fo-chevron-alpha.png" alt=""><div class="brand"><div><div class="n">First Officer</div><div class="by">by UpNonStop™</div></div></div><p>A desk of specialists across 96 programs, working for your business spend.</p></div>
<div><div class="sd-h">Product</div><a href="{pre}pricing.html">Pricing</a><a href="{pre}how.html">How It Works</a><a href="{pre}product.html">The Product</a><a href="{pre}strategist.html">The Strategist</a><a href="{pre}trust.html">Trust &amp; Security</a><a href="{pre}calculator.html">Run The Numbers</a><a href="{pre}app.html">The App <span class="soon">Soon</span></a></div>
<div class="sd-ind"><div class="sd-h">Your Industry</div><div class="ind">{ind}</div><a href="{pre}industries.html" style="color:var(--pinkdeep);font-weight:600">All industries →</a></div>
<div><div class="sd-h">Free</div><a href="{pre}free-from-the-desk.html">Free From the Desk</a><a href="{pre}field-notes.html">Field Notes</a><a href="{pre}upns.html">The Intelligence Report</a><a href="https://upnonstop.com">The Daily Redemption</a><a href="{pre}hello.html">The Long Version</a></div>
<div><div class="sd-h">Company</div><a href="{pre}about.html">About</a><a href="{pre}connect.html">Connect</a><a href="{pre}privacy-policy.html">Privacy Policy</a><a href="{pre}privacy-policy.html#do-not-sell">Do Not Sell My Info</a><a href="{pre}terms-of-service.html">Terms of Service</a><a href="{pre}disclaimer.html">Disclaimer</a></div>
</div>
<div class="ftbar"><div class="addr">UpNonStop | 235 Pavonia Avenue | Jersey City, NJ 07302 | Proudly Made in 🇺🇸</div><div class="legal">Independent: no affiliate relationships with any issuer. An educational tool, not a licensed financial advisor. US businesses only. © 2026 UpNonStop.</div></div>
</footer>
<a class="pill pink mcta" href="{pre}book.html?from={src}">Book Your "Found Money" Call</a>'''
    return out

def page(title, body, pre='', active='', extra_head='', tick=False, band=True, src='site', fonts=None, foot=True, desc=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{H.escape(desc)}"><meta name="robots" content="noindex">
{fonts or FONTS}<link rel="icon" href="{pre}img/fo-chevron-alpha.png"><link rel="stylesheet" href="{pre}assets/fo.css">{extra_head}</head><body>
<!-- MOCKUP · First Officer rebuild v1 · static HTML, not production -->
{nav(pre,active)}{live_ticker(tick,pre) if tick in ('home','hello') else (ticker() if tick else '')}
<main id="main">{body}</main>
{footer(pre,band,src) if foot else ''}
<script src="{pre}assets/fo.js"></script></body></html>'''

# ---------- copy fixes (locked rules). each: (regex, repl, rule) ----------
FIXES=[
 (r'we do not own the seats', 'we do not control award space', 'No seats or availability'),
 (r'(?i)\beconomy seats\b', 'economy fares', 'No seats or availability'),
 (r'business class seat\b', 'business class ticket', 'No seats or availability'),
 (r'Award pricing and availability change constantly', 'Award pricing and award space change constantly', 'No seats or availability'),
 (r'Availability and pricing change\.', 'Award space and pricing change.', 'No seats or availability'),
 (r'Award availability, pricing', 'Award space, pricing', 'No seats or availability'),
 (r'>Windows open<', '>Worth acting on<', 'No "just opened"/window-open availability language'),
 (r'Coverage across 50 programs', 'Coverage across 96 programs', 'Counts: 96 programs'),
 (r'coverage across 50 programs', 'coverage across 96 programs', 'Counts: 96 programs'),
 (r'across 50 programs', 'across 96 programs', 'Counts: 96 programs'),
 (r'(?i)\b629 (loyalty )?programs', lambda m: '96 '+(m.group(1) or '')+('Programs' if m.group(0).endswith('Programs') else 'programs'), 'Counts: 96 programs'),
 (r'\b13 Banks\b', '13 Issuers', 'Counts: 13 issuers'),
 (r'\b13 banks\b', '13 issuers', 'Counts: 13 issuers'),
 (r'Software-led coverage across 96 programs, a person when needed,', 'Coverage across 96 programs, strategy within 24 hours,', 'Approved human-review line'),
 (r'Software does most of the work, and a person from our team steps in when needed\.', APPROVED, 'Approved human-review line'),
 (r'a consortium brain underneath, with a person stepping in when needed, one thread in your messages\.', 'specialists underneath, one thread in your messages. '+APPROVED, 'Approved human-review line; minimal "AI"'),
 (r'You run a business with roughly \$25K a month or more of non-payroll spend\.', 'You run a business with real non-payroll spend on cards and vendors. Not sure it is enough? <a href="calculator.html">Run your number on the calculator</a>.', 'No minimum spend shown; point to calculator'),
 (r'You put \$35K\+ a month on vendors and cards\.', 'You put serious money on vendors and cards every month.', 'No minimum spend shown'),
 (r'on WhatsApp or SMS \(and soon on your App!\)', 'on WhatsApp for now (texting and the app are coming soon)', 'Texting and app are coming soon'),
 (r'>\$500 FLAT<', '>$500 PER TRIP<', 'Award search is a separate $500 per trip, always'),
 (r'Award space, when the trip is real', 'Award search, always separate', 'Award search is a separate $500 per trip, always'),
 (r'Per award itinerary, any party size', 'Award search, per trip, any party size', 'Award search is a separate $500 per trip, always'),
 (r'Flat per itinerary,', 'Flat per trip, always separate from the monthly fee,', 'Award search is a separate $500 per trip, always'),
 (r'after EFS coding verification', 'after fuel-card coding verification', 'No card names'),
 (r'McKinsey estimated in 2018', 'An industry study estimated in 2018', 'No source names'),
 (r'Breakage and unredeemed miles from McKinsey, 2018\.', 'Breakage and unredeemed miles from a 2018 industry study.', 'No source names'),
 (r'(?i)Source: Visa Merchant Data Standards Manual\. ?', '', 'No source names'),
 (r'Visa definition', 'Definition', 'No card/source names'),
 (r'Coding: Visa MDSM', 'Coding: network code standards', 'No source names'),
 (r'Source: Visa MDSM', 'Source: network code standards', 'No source names'),
 (r'across our client base', 'across an illustrative client base', 'Personas fictional; never "our clients"'),
 (r'(?i)\bour clients\b', lambda m: 'Illustrative clients' if m.group(0)[0]=='O' else 'illustrative clients', 'Personas fictional; never "our clients"'),
 (r'(?i)\bour customers\b', lambda m: 'Clients' if m.group(0)[0]=='O' else 'clients', 'Never "our customers"'),
 (r'\bBen\b', 'Leo', 'Leo of Linden Row Insurance replaces Ben'),
 (r'Remco Agency', 'Linden Row Insurance', 'Leo of Linden Row Insurance replaces Remco Agency'),
]
LOG={}

EXTRA_FIXES=[
    (r'no seat to book','no award to book','No seats or availability'),
    (r'>UR</text>','>A</text>','No card, issuer or source names'),
 (r'>629</(div|span)>(\s*)<div class="l">Programs read', lambda m: f'>96</{m.group(1)}>{m.group(2)}<div class="l">Programs read', 'Counts: 96 programs'),
 (r'\b629 Programs read', '96 Programs read', 'Counts: 96 programs'),
 (r'Verdict held', 'Verdict stood', 'Never "held"'),
 (r'verdict held', 'verdict stood', 'Never "held"'),
 (r'for wallets holding Bank D points', 'for wallets with Bank D points', 'Never "holding"'),
 (r'still holding their points', 'still sitting on their points', 'Never "holding"'),
 (r'Visa defines', 'The card networks define', 'No card/network source names'),
 (r'Seats Are Hard', 'Award Space Is Hard', 'No seats or availability'),
 # seats / availability wording (booking language)
 (r'Award seats vanish', 'Award space vanishes', 'No seats or availability'),
 (r'Award seats and rates change', 'Award space and rates change', 'No seats or availability'),
 (r'(?i)\baward availability\b', lambda m: ('Award' if m.group(0)[0]=='A' else 'award')+' space', 'No seats or availability'),
 (r'When a seat does not exist', 'When award space does not exist', 'No seats or availability'),
 (r'as availability, prices, and programs shift', 'as award space, prices, and programs shift', 'No seats or availability'),
 (r'the availability, and the timing', 'the award space, and the timing', 'No seats or availability'),
 (r'airlines release award seats', 'airlines release award space', 'No seats or availability'),
 (r'Airlines release award seats', 'Airlines release award space', 'No seats or availability'),
 (r'The best seats \(First, Business\) go fast', 'The best cabins (First, Business) go fast', 'No seats or availability'),
 (r'the seat you want books for', 'the flight you want prices at', 'No seats or availability'),
 (r'The same seat can cost', 'The same flight can cost', 'No seats or availability'),
 (r'The same seat costs', 'The same flight costs', 'No seats or availability'),
 (r'own profile held in isolation', 'own profile kept in isolation', 'No "held" wording'),
 # minimum spend -> calculator
 (r'<div class="v">\$15K</div><div class="l">Minimum 12-mo capture to join</div>', '<div class="v">24 hrs</div><div class="l">Your strategy, reviewed by a person</div>', 'No minimum spend shown'),
 (r'<div class="v">\$35K</div><div class="l">Monthly spend floor · We check first</div>', '<div class="v"><a href="calculator.html">Calculator</a></div><div class="l">Run your own number first</div>', 'No minimum spend shown'),
 (r'You own a business with <b>\$35K\+ a month of non-payroll spend</b>', 'You own a business with <b>real non-payroll spend</b> (<a href="calculator.html">run your number</a>)', 'No minimum spend shown'),
 (r'You spend <b>under \$25K a month</b> on cards', 'Your card spend is <b>still light</b>', 'No minimum spend shown'),
 (r'<h3>Clears the bar at \$35K\+/mo non-payroll</h3>', '<h3>Clears the bar on the calculator</h3>', 'No minimum spend shown'),
 (r"Between \$25K and \$35K a month, same rule: the call computes your 12-month capture, and if it clears \$15K, you're in\.", "Wherever you land, same rule: the call computes your 12-month capture, and if it clears the fee with room to spare, you're in.", 'No minimum spend shown'),
 (r'<h3>Below \$25K a month</h3>', '<h3>When the math is thin</h3>', 'No minimum spend shown'),
 (r'THE CALL: \$35K\+ MONTHLY NON-PAYROLL SPEND, OR A COMPUTED 12-MONTH CAPTURE ABOVE \$15K', 'THE CALL: WE RUN YOUR NUMBER FIRST · <a href="calculator.html">TRY THE CALCULATOR</a>', 'No minimum spend shown'),
 (r'Below roughly \$25K a month in non-payroll spend, the fee is unlikely', 'When non-payroll spend is light, the fee is unlikely', 'No minimum spend shown'),
 (r'(?i)\b(you put )\$35K\+ a month on', r'\1serious money every month on', 'No minimum spend shown'),
 # texting / app
 (r'WHATSAPP TODAY · APP \+ SMS NEXT', 'WHATSAPP TODAY · TEXTING + APP COMING SOON', 'Texting/app coming soon'),
 (r'WhatsApp and SMS today, the app next\.', 'WhatsApp today. Texting and the app are coming soon.', 'Texting/app coming soon'),
 # card networks / AI
 (r'Costco only accepts Visa in-store\.', 'Costco only accepts one card network in-store.', 'No card/issuer/source names'),
 (r'Costco in-store takes Visa only: route accordingly', 'Costco in-store takes one card network only: route accordingly', 'No card/issuer/source names'),
 (r'a personal Visa earning 1x', 'a personal card earning 1x', 'No card/issuer/source names'),
 (r'Sample outputs are AI-generated illustrations', 'Sample outputs are software-generated illustrations', 'Minimal "AI"'),
 (r'<b>629</b> PROGRAMS MONITORED', '<b>96</b> PROGRAMS MONITORED', 'Counts: 96 programs'),
 (r'<span class="pk">13</span></span><span>Banks Tracked', '<span class="pk">96</span></span><span>Programs Monitored', 'Counts: 96 programs / 13 issuers (duplicate 13 Banks row)'),
 # pass 2 (resume): claims that overstate what runs today
 (r'watches 108 cards and 13 issuers around the clock', 'watches 108 cards and 13 issuers on scheduled scans', 'Truth: scheduled scans, not around the clock'),
 (r'OPS (·|&middot;) LIVE WATCH', r'OPS \1 SCHEDULED SCANS', 'Truth: scheduled scans, not live watch'),
 (r'The Strategist monitors award space for your specific routes and dates\.', 'The Strategist scans award pricing for your routes and dates on a schedule, and the desk books once you approve.', 'Truth: scheduled scans; desk books'),
 (r'We find the space; you claim it in your own account, which is the only place your points ever sit\.', 'We vet your requirements, and once you approve, a person on the desk books it in your own account, which is the only place your points ever sit.', 'Burn vets, desk books'),
 (r'Two-minute fix: seat assignments for the Denver run', 'Two-minute fix: bag fees for the Denver run', 'No seats or availability'),
 (r'Airline credits cover seats and bags, not fares', 'Airline credits cover add-ons like bags, not fares', 'No seats or availability'),
]
LEGAL={'privacy-policy.html','terms-of-service.html','disclaimer.html'}

def fix(s, page):
    s=s.replace('\u00a0',' ').replace('&nbsp;',' ')
    for pat,rep,rule in FIXES+([] if page in LEGAL else EXTRA_FIXES):
        s2,n=re.subn(pat,rep,s)
        if n:
            LOG.setdefault(page,[]).append((pat if isinstance(pat,str) else pat, rep if isinstance(rep,str) else '(case-matched)', rule, n))
            s=s2
    return s
def save_log():
    import os
    f=ROOT+'/_build/fixlog.json'; old=json.load(open(f)) if os.path.exists(f) else {}
    old.update(LOG); json.dump(old,open(f,'w'),indent=1)
def write(name, html):
    p=os.path.join(ROOT,name); os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,'w').write(html)
