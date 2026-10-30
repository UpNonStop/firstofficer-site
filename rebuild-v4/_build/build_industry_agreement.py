# Builds for-dental-agreement.html: the honest agreement-ladder industry page mockup (dental).
# Reuses the v4 head, nav and footer from for-dental.html. Mockup only, not production.
import os, re
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
s = open(os.path.join(root, 'for-dental.html')).read()
head = s[:s.find('<!-- MOCKUP')]
nav = s[s.find('<header class="nav"'):s.find('<div class="fotick"')]
foot = s[s.find('<footer'):s.find('<script src="assets/site.js">')]
head = head.replace('<title>First Officer for Dental</title>', '<title>First Officer for Dental Practices · Agreement ladder mockup</title>')
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Your supply, lab and equipment spend already earns travel. A monthly desk works it across 50+ programs.">', head)
foot = re.sub(r'<p class="dn">.*?</p>', '<p class="dn">Dr. Priya is a fictional persona. Every figure on this page is an illustrative estimate, not a result or a promise. Your numbers depend on your cards, your vendors and published program terms.</p>', foot, flags=re.S)
assert 'UpNonStop | 235 Pavonia Avenue | Jersey City, NJ 07302 | Proudly Made in 🇺🇸' in foot

CSS = r'''<style>
/* industry agreement ladder mockup: page-local styles on top of the v4 skin */
:root{--learnL:#5AB0E6}
#hero{position:relative;isolation:isolate;overflow:hidden;padding-top:40px}
#hero .aph{position:absolute;inset:0;z-index:-1;pointer-events:none;background:var(--bg)}
#hero .aph img{position:absolute;right:0;top:0;height:100%;width:62%;object-fit:cover;object-position:50% 40%;opacity:.22;filter:saturate(.85)}
#hero .aph::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--bg) 0,var(--bg) 34%,rgba(250,246,238,.55) 62%,rgba(250,246,238,.25) 100%)}
#hero .h1{font-size:40px;line-height:1.06}
@media(min-width:900px){#hero .h1{font-size:60px;line-height:1.02}#hero{padding:72px 0 84px}}
.belief{display:inline-block;margin-top:18px;font:600 13px/1.4 var(--mono);letter-spacing:.06em;color:var(--ink2);border:1px dashed var(--pinkLine);background:#fff;border-radius:12px;padding:10px 14px}
.belief b{color:var(--pinkdeep)}
.hbtns{display:grid;gap:10px;margin-top:22px}
@media(min-width:700px){.hbtns{display:flex}.hbtns .btn{width:auto;min-width:220px}}
.persona .tag{display:inline-block;font:600 10.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);border:1px solid var(--line);border-radius:999px;padding:6px 9px}
.persona .who{display:flex;gap:12px;align-items:center;margin-top:12px}
.persona .av{width:46px;height:46px;border-radius:50%;background:var(--pinkWash);border:1px solid var(--pinkLine);display:grid;place-items:center;font:400 20px/1 var(--serif);color:var(--pinkdeep);flex:none}
.ladder{counter-reset:r;display:grid;gap:10px;max-width:860px}
.rung{display:grid;grid-template-columns:44px 1fr;gap:14px;align-items:start;background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px 18px;transition:border-color .25s,background .25s}
.rung .n{width:44px;height:44px;border-radius:12px;display:grid;place-items:center;font:700 13px/1 var(--mono);color:var(--pinkdeep);background:var(--pinkWash);border:1px solid var(--pinkLine)}
.rung h3{font:400 21px/1.25 var(--serif);color:var(--ink)}
.rung p{margin-top:4px;font:400 14.5px/1.5 var(--font);color:var(--ink2)}
.rung .yn{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
.rung .yn button{font:600 13px/1 var(--font);border-radius:999px;padding:9px 14px;border:1px solid var(--line);background:#fff;color:var(--ink2);cursor:pointer}
.rung .yn button[aria-pressed="true"].y{background:var(--earn);border-color:var(--earn);color:#fff}
.rung .yn button[aria-pressed="true"].no{background:var(--ink2);border-color:var(--ink2);color:#fff}
.rung.yes{border-color:color-mix(in srgb,var(--earn) 45%,#fff);background:#FBFEFC}
.rung .tie{display:block;margin-top:8px;font:600 11px/1.3 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--ink3)}
.tally{margin-top:16px;max-width:860px}
.calc{display:grid;gap:16px}
@media(min-width:1000px){.calc{grid-template-columns:1.05fr .95fr;gap:28px;align-items:start}}
.sl{padding:16px 0;border-top:1px solid var(--line)}
.sl:first-of-type{border-top:0}
.sl .top{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.sl .top b{font:700 20px/1.2 var(--font);font-variant-numeric:tabular-nums}
.sl .top span{font:600 15px/1.35 var(--font)}
.cmpx{margin-top:14px;display:grid;gap:12px}
.cmpx .ln{display:flex;justify-content:space-between;gap:10px;font:500 14px/1.35 var(--font);color:var(--ink2)}
.cmpx .ln b{color:var(--ink);font-variant-numeric:tabular-nums}
.cmpx .bar{height:10px;border-radius:5px;background:var(--track,#EFEAF0);overflow:hidden;margin-top:6px}
.cmpx .bar i{display:block;height:100%;border-radius:5px;background:var(--c,var(--ink3));width:var(--w,0%);transition:width .5s var(--ease,ease)}
.verdict{margin-top:14px;border-radius:14px;padding:12px 14px;font:500 14px/1.5 var(--font)}
.verdict.ok{background:var(--earn-w);color:#0D5E38}
.verdict.no{background:#F4F1F5;color:var(--ink2)}
.est{display:inline-block;font:700 10.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#fff;background:var(--ink2);border-radius:6px;padding:5px 7px;vertical-align:middle;margin-left:6px}
.pillars{display:grid;gap:12px}
@media(min-width:760px){.pillars{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.pillars{grid-template-columns:repeat(4,1fr)}}
.pillars>.card+.card,.obj>.card+.card{margin-top:0}
.pil{border-top:5px solid var(--c)}
.pil .lab{color:var(--c)!important}
.pil .q{display:block;margin-top:12px;padding-top:12px;border-top:1px dashed var(--line);font:italic 400 15px/1.45 var(--serif);color:var(--ink)}
.hsteps{display:grid;gap:10px;max-width:900px;counter-reset:s}
.hstep{display:grid;grid-template-columns:54px 1fr;gap:14px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:16px 18px}
.hstep .k{font:700 11px/1.2 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--c,var(--pinkdeep));padding-top:4px}
.hstep h3{font:400 20px/1.25 var(--serif)}
.hstep p{margin-top:4px;font:400 14.5px/1.5 var(--font);color:var(--ink2)}
.obj{display:grid;gap:12px}
@media(min-width:900px){.obj{grid-template-columns:1fr 1fr}}
.obj .card .said{display:block;font:600 12px/1.3 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink3)}
.obj .card h3{margin-top:8px}
.offer{display:grid;gap:16px}
@media(min-width:1000px){.offer{grid-template-columns:1.1fr .9fr;align-items:center}}
.offer .price{font:400 64px/1 var(--serif);color:var(--ink)}
.offer .price small{font:500 16px/1 var(--font);color:var(--ink3);margin-left:6px}
.chk{display:grid;gap:8px;margin-top:14px}
.chk div{display:flex;gap:10px;font:500 15px/1.45 var(--font);color:var(--ink2)}
.chk div::before{content:"✓";color:var(--earn);font-weight:700}
.faq details{background:#fff;border:1px solid var(--line);border-radius:16px;padding:0 18px}
.faq details+details{margin-top:10px}
.faq summary{cursor:pointer;list-style:none;padding:16px 0;font:600 16px/1.4 var(--font);color:var(--ink);display:flex;justify-content:space-between;gap:12px}
.faq summary::after{content:"+";color:var(--pink2);font-weight:700}
.faq details[open] summary::after{content:"–"}
.faq details p{padding:0 0 16px;font:400 15px/1.55 var(--font);color:var(--ink2)}
.easyno{margin-top:14px;font:italic 400 17px/1.45 var(--serif);color:var(--ink2)}
</style>'''

def rung(n, h, p, tie):
    return f'''<div class="rung" data-rung><span class="n">{n:02d}</span><div><h3>{h}</h3><p>{p}</p><span class="tie">{tie}</span><div class="yn" role="group" aria-label="Is this true for you?"><button type="button" class="y" aria-pressed="false">True for us</button><button type="button" class="no" aria-pressed="false">Not really</button></div></div></div>'''

RUNGS = [
 ("Supplies, lab fees and equipment already go on a card.", "Gloves, composite, crowns, aligner cases, imaging, software. It is the biggest line on the statement, and it gets paid every month whether anyone watches it or not.", "Possibility"),
 ("Those cards already earn points on all of it.", "Not a new expense, not a new vendor. The practice is already earning; the only open question is what that earning turns into.", "Benefit"),
 ("The points mostly sit, or go to whatever was quickest.", "A statement credit here, a gift card there. Nobody chose that. It is just what happens when no one owns the balance.", "Honest status quo"),
 ("Nobody at the practice has time to learn 50+ programs.", "Transfer partners, award rules and bonus categories change through the year. Keeping up is a job in itself, and it is not the job you trained for.", "Not your fault"),
 ("You would rather the points became trips you actually want.", "A family trip at school break, a conference trip done properly, a long weekend that the practice spend already paid for.", "Personal benefit"),
 ("If someone else did that job every month, it would be worth knowing what it is worth.", "Not a promise. An estimate on your own spend, with our fee taken out first and plain cash back as the yardstick.", "Fit"),
]

PILLARS = [
 ("Earn", "--earn", "Every vendor on the right card", "The desk maps how your distributors, labs and software vendors code, then routes each one to the card that earns the most on it, inside published caps.", "Would you agree the same supply invoice should earn as much as it can?"),
 ("Burn", "--burn", "Points into trips you choose", "When you want to go somewhere, Burn checks the program rules, transfer terms and fees first, then the desk books it for you as an ad hoc service.", "Would you rather spend points on purpose than let them sit?"),
 ("Return", "--return", "A monthly recap in plain numbers", "Each month you see what was earned, what was used and what it was worth against 2% cash back. No dashboards to learn.", "Is it fair to want proof every month, not a pitch once a year?"),
 ("Learn", "--learnL", "Your setup, explained", "Program terms change. Learn tells you what changed, why it matters for the practice, and what the desk did about it, in language you could hand to your accountant.", "Would it help to actually understand your own setup?"),
]

STEPS = [
 ("Call", "--pinkdeep", "A free 20-minute Found Money Call", "We look at your card mix and vendor list together. If plain cash back wins for your practice, we say so on the call."),
 ("Earn", "--earn", "The desk maps and routes your spend", "Vendor codes verified against real statements, each line routed to the card that earns the most on it. You approve every change."),
 ("Burn", "--burn", "You ask for a trip; Burn vets it first", "Dates, places, who is travelling. Burn checks the program requirements, transfer terms and fees before anything moves, then the desk books it as an ad hoc service and you confirm."),
 ("Return", "--return", "A recap lands every month", "Earned, used, valued, and compared with 2% cash back, after our fee."),
 ("Learn", "--learnL", "What changed, in plain words", "When a program changes its terms, you hear what it means for the practice and what the desk did."),
]

OBJ = [
 ("“I already have a good card.”", "Agreed, and that is the right starting point.", "A good card is the base. The question is whether every vendor lands on the card that earns most on it, and whether the points become something you wanted. The desk works with the cards you have and only suggests a change when the math clears it."),
 ("“I don't have time for another thing.”", "Exactly. That is the whole reason this exists.", "You do not learn the programs; the desk does. Your part is a yes or a no on changes and trips. If even that feels like too much in a given month, you can stop."),
 ("“Is $550 a month really worth it?”", "Only if the numbers say so. That is a fair test.", "The estimate takes the $550 out before it shows you anything, and it lines up against plain 2% cash back. If cash back wins at your spend, the page says so, and so will we."),
 ("“What if it doesn't work out?”", "Then you should be able to leave. You can.", "Month to month, no exit fee, no annual contract. You stay because each month's recap is worth it, or you go."),
]

FAQ = [
 ("Is First Officer a credit card?", "No. First Officer is an independent desk. We have no affiliate relationships with any issuer, so a card recommendation is only ever about your numbers."),
 ("Do I have to change the cards the practice uses?", "Not by default. The desk starts with what you have. Any change is proposed with the math behind it, and nothing moves without your yes."),
 ("What does the estimate on this page include?", "Points from spend times a blended earn rate, valued at about 3 cents a point, with 85% of points assumed used and a further discount for travel you would not have bought anyway. Our $550 monthly fee comes out before the net figure. It is an estimate, not a projection of your results."),
 ("How does booking a trip work?", "You tell the desk what you want. Burn vets the requirements first: program rules, transfer terms and fees. Then the desk books it for you as an ad hoc service, and you confirm before anything is final."),
 ("Is this a one-time optimization?", "No. You are an ongoing client. Programs change through the year, so the desk works your accounts every month, with white-glove service throughout."),
 ("Can I cancel?", "Yes, any month. Month to month, no exit fee."),
]

body = f'''<!-- MOCKUP · industry page, honest agreement ladder (dental) · built by _build/build_industry_agreement.py · static HTML, not production -->
<main id="main">
<section class="sec" id="hero"><div class="aph" aria-hidden="true"><img src="img/ph/i-dental2.webp" alt=""></div><div class="wrap"><div class="split">
<div class="head" style="margin-bottom:0"><span class="hlab"><span class="lab earn">First Officer for Dental Practices</span></span>
<h1 class="h1" style="margin-top:14px">Your supply bills already earn travel. <em>Someone just has to work them.</em></h1>
<p class="lede">The practice already puts supplies, lab fees and equipment on cards. First Officer is a monthly desk that works that spend across 50+ programs, so the points turn into trips you actually take. You keep running the practice.</p>
<span class="belief"><b>The one idea:</b> spend you already make + a desk working it every month = travel the practice has already paid for.</span>
<div class="hbtns"><a class="btn" href="#estimate">See my estimate</a><a class="btn ghost" href="book.html?from=for-dental-agreement-hero">Book a Found Money Call</a></div>
<p class="cap" style="margin-top:12px">$550 a month, month to month, no exit fee. Estimates on this page are illustrative.</p></div>
<div class="card hero persona"><span class="tag">Fictional persona · illustrative</span>
<div class="who"><span class="av">P</span><div><b style="font:600 16px/1.3 var(--font)">Dr. Priya, practice owner</b><span class="cap" style="display:block;margin:0">Two-chair general practice · about $520K a year on cards</span></div></div>
<div class="div"></div>
<div class="kv"><span>Dental supply distributors</span><b>$240,000</b></div><div class="kv"><span>Lab fees</span><b>$120,000</b></div><div class="kv"><span>Equipment and imaging</span><b>$90,000</b></div><div class="kv"><span>Practice software and phones</span><b>$40,000</b></div><div class="kv"><span>Everything else</span><b>$30,000</b></div>
<div class="kv tot"><span>Card spend, a year</span><b>$520,000</b></div>
<p class="cap" style="margin-top:10px">Dr. Priya is not a client. She is a composite profile used to show how the estimate works. Rent and payroll stay off the card.</p></div>
</div></div></section>

<section class="sec" id="ladder"><div class="wrap">
<div class="head"><span class="lab">Start with what you already know</span><h2 class="h2">Six things most practice owners <em>already agree with.</em></h2><p class="lede">No pitch yet. Just check the ones that are true for your practice. If most are not, this page is not for you, and that is a perfectly good answer.</p></div>
<div class="ladder">{''.join(rung(i+1,*r) for i,r in enumerate(RUNGS))}</div>
<div class="note tally" id="tally" aria-live="polite"><span class="ic">✓</span><span>Tap “True for us” on the ones that fit. Nothing here is saved or sent anywhere.</span></div>
</div></section>

<section class="sec" id="estimate"><div class="wrap">
<div class="head"><span class="lab earn">Your estimate <span class="est">Estimate</span></span><h2 class="h2">What your card spend could be worth, <em>after our fee.</em></h2><p class="lede">Move the sliders to your practice. The math is on the page, the $550 fee comes out first, and the yardstick is plain 2% cash back, the easiest thing you could do instead.</p></div>
<div class="calc">
<div class="card">
<div class="sl"><div class="top"><span>Practice card spend, a year</span><b id="vSp">$520,000</b></div><input class="rng" id="sp" type="range" min="100000" max="1500000" step="10000" value="520000" aria-label="Practice card spend per year"><span class="cap">Supplies, labs, equipment, software, phones. Not rent or payroll.</span></div>
<div class="sl"><div class="top"><span>Blended earn rate</span><b id="vEr">2.1x</b></div><input class="rng" id="er" type="range" min="1" max="3" step="0.1" value="2.1" aria-label="Blended points per dollar"><span class="cap">Points per dollar across all lines, inside published caps. Most practice profiles we model land near 2x; the desk verifies yours.</span></div>
<p class="cap" style="margin-top:12px"><b>The formula.</b> Points = spend × earn rate. Value = points × about 3 cents × 85% of points used × 72% for travel you would not have bought anyway. Net = value minus $550 a month. Compared with 2% cash back on the same spend.</p>
</div>
<div class="card hero top" style="--c:var(--earn)"><span class="lab earn">Estimated net, a year, after our fee <span class="est">Estimate</span></span><span class="num tn" id="oNet" style="margin-top:8px">$0</span>
<div class="div"></div>
<div class="kv"><span>Points a year</span><b id="oPts">0</b></div>
<div class="kv"><span>Valued honestly</span><b id="oVal">$0</b></div>
<div class="kv neg"><span>Our fee, $550 × 12</span><b>−$6,600</b></div>
<div class="kv tot"><span>Net, a month</span><b id="oMo">$0</b></div>
<div class="cmpx"><div><div class="ln"><span>2% cash back, a year</span><b id="oCb">$0</b></div><div class="bar"><i id="bCb" style="--c:var(--ink3)"></i></div></div><div><div class="ln"><span>First Officer, a year, after fee</span><b id="oFo">$0</b></div><div class="bar"><i id="bFo" style="--c:var(--earn)"></i></div></div></div>
<div class="verdict" id="verdict"></div>
<a class="btn" href="book.html?from=for-dental-agreement-estimate" style="margin-top:16px">Check it against my real statements</a>
<p class="cap" style="margin-top:10px">Estimated and illustrative. Not a projection of your results. Program terms, caps and point values change, and redemption value depends on what you book.</p></div>
</div></div></section>

<section class="sec" id="pillars"><div class="wrap">
<div class="head"><span class="lab">What the $550 covers</span><h2 class="h2">Four jobs, <em>every month.</em></h2><p class="lede">Each one answers a question you have probably already asked yourself about the practice cards.</p></div>
<div class="pillars">{''.join(f'<article class="card pil" style="--c:var({c})"><span class="lab">{n}</span><h3 class="h3" style="margin-top:8px">{t}</h3><p style="margin-top:6px">{d}</p><span class="q">{q}</span></article>' for n,c,t,d,q in PILLARS)}</div>
</div></section>

<section class="sec" id="how"><div class="wrap">
<div class="head"><span class="lab">How it works</span><h2 class="h2">You say yes or no. <em>The desk does the rest.</em></h2></div>
<div class="hsteps">{''.join(f'<div class="hstep" style="--c:var({c})"><span class="k">{k}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for k,c,h,p in STEPS)}</div>
</div></section>

<section class="sec" id="objections"><div class="wrap">
<div class="head"><span class="lab">Fair questions</span><h2 class="h2">The doubts worth having, <em>answered straight.</em></h2></div>
<div class="obj">{''.join(f'<article class="card"><span class="said">{a}</span><h3 class="h3">{b}</h3><p style="margin-top:6px">{c}</p></article>' for a,b,c in OBJ)}</div>
<div class="note" style="margin-top:16px"><span class="ic">⏱</span><span><b>On timing, honestly.</b> There is no deadline on this page. The only clock is the one you already have: every month of practice spend earns something, and months nobody works are value that does not come back.</span></div>
</div></section>

<section class="sec" id="offer"><div class="wrap"><div class="card hero offer">
<div><span class="lab">The offer</span><h2 class="h2" style="margin-top:10px">One desk for the practice cards. <em>Every month.</em></h2>
<div class="chk"><div>Earn, Burn, Return and Learn, every month</div><div>Ongoing white-glove client service, not a one-off review</div><div>Trips booked for you as an ad hoc service, vetted by Burn first</div><div>Month to month. No exit fee. No annual contract.</div></div></div>
<div style="text-align:center"><span class="price">$550<small>/ month</small></span><p class="cap" style="margin-top:8px">If your estimate does not clear the fee and beat 2% cash back, we will tell you not to sign up.</p></div>
</div></div></section>

<section class="sec" id="call"><div class="wrap"><div class="card hero cta-card"><span class="mk"><img src="img/fo-chevron-transparent-v2.png" alt=""></span><h3 class="h2" style="font-size:30px">If the numbers work, is it worth a 20-minute call?</h3><p class="lede">The Found Money Call is free. We check your estimate against real statements and tell you plainly whether First Officer is worth it for your practice.</p><div class="btns"><a class="btn" href="book.html?from=for-dental-agreement-cta">Book Your “Found Money” Call</a></div><p class="easyno">And if it is not a fit, that is a perfectly good answer.</p></div></div></section>

<section class="sec faq" id="faq"><div class="wrap" style="max-width:860px">
<div class="head"><span class="lab">FAQ</span><h2 class="h2">Questions practice owners <em>ask first.</em></h2></div>
{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)}
</div></section>
</main>
'''

JS = r'''<script>
(function(){
  var $=function(i){return document.getElementById(i)};
  var usd=function(n){return (n<0?'−$':'$')+Math.round(Math.abs(n)).toLocaleString('en-US')};
  /* value per point = 3.0 cents x 85% used x 72% honest discount = 0.01836 */
  var VPP=0.03*0.85*0.72, FEE=550*12;
  function upd(){
    var sp=+$('sp').value, er=+$('er').value, pts=sp*er, val=pts*VPP, net=val-FEE, cb=sp*0.02;
    $('vSp').textContent=usd(sp); $('vEr').textContent=er.toFixed(1)+'x';
    [['sp',sp,100000,1500000],['er',er,1,3]].forEach(function(a){$(a[0]).style.setProperty('--p',((a[1]-a[2])/(a[3]-a[2])*100)+'%')});
    $('oPts').textContent=Math.round(pts).toLocaleString('en-US'); $('oVal').textContent=usd(val);
    $('oNet').textContent=usd(net); $('oMo').textContent=usd(net/12); $('oCb').textContent=usd(cb); $('oFo').textContent=usd(net);
    var mx=Math.max(cb,net,1); $('bCb').style.setProperty('--w',Math.max(0,cb/mx*100)+'%'); $('bFo').style.setProperty('--w',Math.max(0,net/mx*100)+'%');
    var v=$('verdict'), d=net-cb;
    if(d>0){v.className='verdict ok';v.textContent='At these numbers, the estimate beats 2% cash back by about '+usd(d)+' a year after our fee. Worth checking against your real statements.'}
    else{v.className='verdict no';v.textContent='At these numbers, plain 2% cash back likely wins by about '+usd(-d)+' a year. That is an honest no, and we would tell you the same on a call.'}
  }
  ['sp','er'].forEach(function(i){$(i).addEventListener('input',upd)}); upd();
  var rs=[].slice.call(document.querySelectorAll('[data-rung]'));
  function tally(){
    var y=rs.filter(function(r){return r.classList.contains('yes')}).length, n=rs.filter(function(r){return r.dataset.no}).length, t=$('tally').lastElementChild;
    if(!y&&!n){t.textContent='Tap “True for us” on the ones that fit. Nothing here is saved or sent anywhere.';return}
    t.innerHTML=y>=4?'<b>'+y+' of '+rs.length+' true for your practice.</b> Then the estimate below is worth two minutes of your time.':'<b>'+y+' of '+rs.length+' so far.</b> If most of these do not fit, First Officer probably is not for you, and that is fine.';
  }
  rs.forEach(function(r){var b=r.querySelectorAll('button');
    b[0].addEventListener('click',function(){var on=b[0].getAttribute('aria-pressed')!=='true';b[0].setAttribute('aria-pressed',on);b[1].setAttribute('aria-pressed','false');r.classList.toggle('yes',on);delete r.dataset.no;tally()});
    b[1].addEventListener('click',function(){var on=b[1].getAttribute('aria-pressed')!=='true';b[1].setAttribute('aria-pressed',on);b[0].setAttribute('aria-pressed','false');r.classList.remove('yes');if(on)r.dataset.no='1';else delete r.dataset.no;tally()});
  });
})();
</script>'''

html = head.replace('</head>', CSS + '</head>') + body.replace('<main id="main">', nav + '<main id="main">', 1) + foot + '<script src="assets/site.js"></script>' + JS + '</body></html>'
# hard-rule guards
low = html.lower()
for bad in [' ai ', 'a.i.', 'artificial intelligence', 'countdown', 'held', 'seats left', 'availability', 'edan', 'kevin', 'remco', '—']:
    assert bad not in low.replace('fo-chevron',''), bad
assert '50+ programs' in html
open(os.path.join(root, 'for-dental-agreement.html'), 'w').write(html)
print('ok', len(html))
