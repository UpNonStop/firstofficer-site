# Builds home-recovered.html and product-recovered.html at the repo root. Mockup only.
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS='https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800;9..40,900&family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@400;500;600;700&display=swap'
SUB="Every loyalty program has their team constantly rewriting the rules. While you're busy running your business, your spend earns less than it should, and your points and miles buy less than they could.\\n\\nFirstOfficer by UpNonStop runs a desk of specialists across 50+ programs, each an expert in its niche. They all work for you, so you skip those rookie mistakes. Your Bespoke Strategy is reviewed weekly and optimized continuously, so every dollar you spend works harder.\\n\\nSame spend. More points. Better trips, for fewer points."
WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call'

def head(title,desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="robots" content="noindex">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="img/fo-chevron-alpha.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="recovered/rec.css">
</head>
'''

def nav(on):
    L=[('Product','product-recovered.html'),('Pricing','pricing.html'),('Freebies','freebies.html'),('Calculator','calculator.html'),('About','about.html')]
    links=''.join(f'<a href="{h}" class="{"brush " if n=="Freebies" else ""}{"on" if n==on else ""}">{n}</a>' for n,h in L)
    sheet=''.join(f'<a href="{h}"><span class="t{" brush in" if n=="Freebies" else ""}">{n}</span><small>0{i+1}</small></a>' for i,(n,h) in enumerate(L))
    return f'''<header class="nav"><div class="nin">
<a class="brand" href="home-recovered.html" aria-label="First Officer home"><img src="img/fo-chevron-alpha.png" alt=""><span><b>First Officer</b><small>by UpNonStop™</small></span></a>
<nav class="links" aria-label="Main">{links}</nav>
<a class="btn pk" href="{WA}">💬 Text Your First Officer</a>
<button class="burger" aria-label="Open menu" aria-expanded="false" onclick="foNav(true)"><span></span><span></span></button>
</div></header>
<div class="sheet" id="sheet" aria-hidden="true">
<div class="top"><a class="brand" href="home-recovered.html"><img src="img/fo-chevron-alpha.png" alt=""><span><b>First Officer</b><small>by UpNonStop™</small></span></a><button class="x" aria-label="Close menu" onclick="foNav(false)">×</button></div>
<nav>{sheet}<div class="sublabel">More</div><a class="sub" href="trust.html">Trust</a><a class="sub" href="industries.html">Industries</a></nav>
<a class="btn pk" href="{WA}">💬 Text Your First Officer</a>
</div>
'''

TIPS=[('E','EARN','Ad spend','Match it to a bonus category'),('B','BURN','Award rules','Vet them before you book'),('E','EARN','Internet &amp; phone','Check it against bonus categories'),('B','BURN','Transfer bonuses','Check before you move points'),('R','RETURN','Hotel nights','Compare points against cash'),('L','LEARN','Expiring points','Every program keeps its own clock'),('R','RETURN','Statement credits','Use them before they lapse'),('B','BURN','Partner charts','Compare them with the airline&#39;s price'),('L','LEARN','Idle points','Lose ground while they sit'),('R','RETURN','Friday report','Every week, in plain words')]
def ticker():
    one='<span class="h"><b>Desk tips, illustrated</b></span>'+''.join(f'<span><em class="{c}">{p}</em> <b>{t}</b> {d}</span>' for c,p,t,d in TIPS)
    return f'<div class="tick" aria-label="Desk tips"><div class="tr">{one}{one}</div></div>\n'

def footer():
    return f'''<footer class="foot"><div class="wrap">
<div class="cols">
<div><a class="brand" href="home-recovered.html"><img src="img/fo-chevron-alpha.png" alt=""><span><b>First Officer</b><small>by UpNonStop™</small></span></a><p class="tl">Your rewards desk. One conversation, 50+ programs, trained on new data nightly.</p></div>
<div><h6>Site</h6><a href="product-recovered.html">Product</a><a href="pricing.html">Pricing</a><a href="freebies.html">Freebies</a><a href="calculator.html">Calculator</a><a href="about.html">About</a></div>
<div><h6>More</h6><a href="trust.html">Trust</a><a href="industries.html">Industries</a><a href="{WA}">Text Your First Officer</a></div>
</div>
<div class="bar"><span class="addr"><span>UpNonStop | 235 Pavonia Avenue | Jersey City, NJ 07302 | Proudly Made in 🇺🇸</span></span><span class="fine">Leo and Linden Row Insurance are fictional. All figures are examples and estimates.</span></div>
</div></footer>
<div class="mcta"><div><small>Flat monthly · Cancel anytime</small><b>$550 a month</b></div><a class="btn pk" href="book.html">Get your desk</a></div>
'''

def cta():
    return f'''<section class="sec tight"><div class="wrap"><div class="ctab reveal">
<div><h2>Get your desk.</h2><p>$550 a month, flat, for every business whatever the spend. Cancel anytime. Start with the free 20 minute Found Money Call.</p></div>
<div class="bt"><a class="btn ink" href="book.html">Book the Found Money Call <span class="ar">→</span></a><a class="btn cr" href="{WA}">💬 Text Your First Officer</a></div>
</div></div></section>
'''

SB='<div class="sb"><span>9:41</span><i><svg width="17" height="11" viewBox="0 0 17 11"><rect x="0" y="7" width="3" height="4" rx="1"/><rect x="4.5" y="5" width="3" height="6" rx="1"/><rect x="9" y="2.5" width="3" height="8.5" rx="1"/><rect x="13.5" y="0" width="3" height="11" rx="1"/></svg><u></u></i></div>'
def hd():
    return SB+'<div class="hd"><div class="lk"><img src="img/rec/chev.png" alt=""><span><b>First Officer</b><small>by UpNonStop™</small></span></div><span class="ex">Example</span></div>'

SHR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7.5 7.5 12 3l4.5 4.5M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7"/></svg>'
def nm(k,t,sub,v,btn):
    return f'<div class="nm"><div class="nmk">Next mission</div><div class="nmr"><div><b>{t}</b><small>{sub}</small></div><span class="nmv">{v}</span></div><div class="nmb"><span class="ok">{btn}</span><span class="sh">{SHR}Share</span></div></div>'

def cs_found(on=''):
    return f'''<div class="cs{on}" data-confetti="1">{hd()}
<div class="bd">✓ It's confirmed</div><div class="lb">Found money</div>
<div class="bg" data-to="6720" data-pre="+$">+$6,720</div><div class="sub">a year, now confirmed <em>est.</em></div>
<p class="p">Software and carrier travel moved to better-earning cards. Your statements confirm it, so it moved from waiting to found.</p>
<div class="mini"><div><small>Travel this month</small><b>$5,000</b></div><div><small>Points earned</small><b>25,000</b></div><div><small>All moves, est.</small><b>$15,120</b></div></div>
<div class="by"><i>✓</i>Checked by the desk against your statement</div>
{nm('a','Ads to the 4x card','Waiting for your OK','+$7,200 <em>est.</em>','Approve')}
<div class="cta">See it on my ledger</div><div class="home"></div></div>'''

def cs_ahead(on=''):
    return f'''<div class="cs{on}">{hd()}
<div class="bd">October scorecard</div><div class="lb">You're ahead of flat cash back by</div>
<div class="bg" data-to="654" data-pre="$">$654</div><div class="sub">this month, after our $550 fee <em>est.</em></div>
<div class="cmp"><div><div class="r"><span>Flat 2% cash back</span><b>$700</b></div><div class="t"><i style="--w:52%"></i></div></div><div><div class="r"><span>First Officer, after fee</span><b>$1,354</b></div><div class="t"><i class="g" style="--w:100%"></i></div></div></div>
<p class="p">Same $35,000 of spend. The same frictions come out of both columns.</p>
<div class="by"><i>✓</i>Checked by the desk</div>
{nm('s','November scorecard','Lands December 1, same $35,000 spend','+$654 <em>est.</em>','Remind me')}
<div class="cta">See the full month</div><div class="home"></div></div>'''

def cs_goal(on=''):
    return f'''<div class="cs{on}" data-confetti="1">{hd()}
<div class="bd pkb">Milestone · Tokyo</div><div class="lb">Points toward Tokyo</div>
<div class="bg pk" data-to="102400">102,400</div><div class="sub">of about 320,000 points <em>est.</em></div>
<div class="goal"><div class="im" style="background-image:url(img/tokyo.jpg)"></div><div class="gb"><b>Tokyo, spring 2027</b><small>Business for 2, round trip, est.</small><div class="tr"><i></i></div><div class="ax"><span>Aug 2026</span><span>32% today</span><span>Mar 2027</span></div></div></div>
<p class="p">The desk vets the requirements and books after you approve.</p>
{nm('g','Pick your Tokyo dates','Spring 2027 window, business for 2','68% to go','Pick dates')}
<div class="cta gd">See my plan</div><div class="home"></div></div>'''

def celphone(slides,cls='',attrs=''):
    return f'<div class="phone cel {cls}" {attrs}><div class="scr">{slides}</div><img class="bz" src="img/rec/app/bezel.webp" alt=""></div>'

def shot(name,alt,cls=''):
    return f'<div class="phone {cls}"><img class="shot" src="img/rec/app/{name}.webp" alt="{alt}" loading="lazy"></div>'

def scorecard():
    return '''<div class="wc sc reveal"><div class="top"><h5>Week 43 scorecard</h5><span class="tag p">Example</span></div>
<div class="v" data-io><span data-count="1860" data-pre="$">$1,860</span><small>this week, est.</small></div>
<ul><li><span>Software on the 4x card</span><b>$640</b></li><li><span>Carrier visits through the card travel portal</span><b>$690</b></li><li><span>Unused travel credit, claimed</span><b>$530</b></li></ul></div>'''

def versus():
    return '''<div class="wc mv reveal d1" data-io><div class="top"><h5>October · Us vs flat 2% cash back</h5><span class="tag d">Example</span></div>
<div class="v">+$654<small style="color:#a49cad">ahead, after fee</small></div>
<div class="bars"><div><span>Flat 2% cash back</span><u><i style="--w:52%"></i></u><b>$700</b></div><div><span>First Officer, after fee</span><u><i class="g" style="--w:100%"></i></u><b>$1,354</b></div></div></div>'''

def share():
    return '''<div class="wc sh reveal d2"><div class="top"><h5>Your ledger, shareable</h5><span class="tag" style="background:rgba(255,255,255,.2);color:#fff">Example</span></div>
<div class="card"><b>Linden Row Insurance routed its spend and is <span data-amt="32%" data-hid="well on its way">32%</span> of the way to Tokyo.</b><small>Found money this year: <span data-amt="$15,120 est." data-hid="hidden">$15,120 est.</span></small></div>
<div class="tg"><span>Hide dollar amounts</span><button class="tgl" aria-label="Hide dollar amounts"></button></div>
<p class="fine">Nothing is shared until you tap Share.</p></div>'''

def scripts(hero=False):
    s='<script src="recovered/rec.js"></script>\n'
    if hero:
        s=('<script src="hero/fo-hero-data.js"></script>\n'
           '<script src="recovered/fo-hero-rec-data.js"></script>\n'
           '<script src="recovered/fo-hero-rec.js"></script>\n')+s
    return s

# ---------------- HOME ----------------
def home():
    h=head('First Officer | You are not bad at Points & Miles','First Officer by UpNonStop: your rewards desk across 50+ programs. One conversation, every pillar.')
    h+='<body>\n'
    h+=f'<script>window.FO_SUBHEAD="{SUB}";</script>\n'
    h+=nav('')+ticker()
    h+='''<style id="fo9hero">#top.dhero{padding:0!important;display:block}
#top>#fohero{max-width:none!important;width:100%!important;margin:0!important;padding:0!important;position:relative!important;left:auto!important}</style>
<main>
<section class="sec dhero secphoto" id="top" style="--ph:none"><div id="fohero"></div></section>

<section class="sec arc" id="story"><div class="wrap">
<div class="arc-head">
<div class="reveal"><span class="kick">One owner. Five beats.</span><h2 class="h2">Meet Leo.<br>He runs <span class="brush">Linden Row</span>.</h2></div>
<div class="who reveal d2"><div class="av">LR</div><div><b>Leo, owner</b><small>Linden Row Insurance · fictional example</small></div></div>
</div>
<nav class="mrail" aria-label="Story beats"><a href="#b1" class="on"><b>01</b>Problem</a><a href="#b2"><b>02</b>Pain</a><a href="#b3"><b>03</b>Solution</a><a href="#b4"><b>04</b>Win</a><a href="#b5"><b>05</b>Why you</a></nav>
<div class="arc-grid">
<nav class="rail" aria-label="Story beats"><a href="#b1" class="on"><b>01</b>Problem</a><a href="#b2"><b>02</b>Pain</a><a href="#b3"><b>03</b>Solution</a><a href="#b4"><b>04</b>Win</a><a href="#b5"><b>05</b>Why you</a><div class="prog"><i></i></div></nav>
<div class="beats">

<article class="beat" id="b1">
<div class="reveal"><div class="bn"><i>01</i>The problem</div><h3 class="h3">About $35,000 a month goes on cards.</h3>
<p class="short">Lead-gen ads. Agency software. Visits to carriers.</p><p>The spend is real. The rewards are an afterthought. Nobody at Linden Row owns them.</p></div>
<div class="panel ink reveal d2" data-io><div class="ph"><h4>Leo's month on cards</h4><span class="tag d">Example</span></div>
<div class="spend">
<div class="row"><div class="l"><b>Lead-gen ads</b><small>On a card that earns 1x</small></div><span class="amt">$12,500</span><span class="chipx">1x</span><div class="bar"><i style="--w:100%"></i></div></div>
<div class="row"><div class="l"><b>Office and vendors</b><small>Spread across cards</small></div><span class="amt">$12,500</span><span class="chipx">1.5x</span><div class="bar"><i style="--w:100%"></i></div></div>
<div class="row"><div class="l"><b>Agency software</b><small>Renews every month</small></div><span class="amt">$5,000</span><span class="chipx">1x</span><div class="bar"><i style="--w:40%"></i></div></div>
<div class="row"><div class="l"><b>Carrier travel</b><small>Booked wherever was quick</small></div><span class="amt">$5,000</span><span class="chipx">1x</span><div class="bar"><i style="--w:40%"></i></div></div>
<div class="tot"><span class="est">About $420,000 a year</span><b class="num">$35,000</b></div>
</div></div>
</article>

<article class="beat" id="b2">
<div class="reveal"><div class="bn"><i>02</i>The pain</div><h3 class="h3">He earns 1.2x on a good day.</h3>
<p class="short">The rules change while he sells policies.</p><p>Points scatter. Credits lapse. The Tokyo trip stays a someday.</p></div>
<div class="pain">
<div class="big reveal d1" data-io><div class="rate">1.2<small>x</small></div><div class="vs"><b>Left on the table</b><strong data-count="15120" data-pre="$">$15,120</strong><span>a year, at the same spend. Example, est.</span></div></div>
<div class="pc reveal d2"><span class="x">×</span><b>Ads on a 1x card</b><small>His biggest line earns the least.</small></div>
<div class="pc reveal d3"><span class="x">×</span><b>Rules rewritten monthly</b><small>Every program keeps its own clock.</small></div>
</div>
</article>

<article class="beat" id="b3">
<div class="reveal"><div class="bn"><i>03</i>The solution</div><h3 class="h3">He texts First Officer. The desk takes it from there.</h3>
<p class="short">One conversation. Specialists across 50+ programs behind it.</p><p>Trained on new data nightly. Every move vetted. Nothing moves without his yes.</p></div>
<div class="sol reveal d2">
'''+shot('earn','Linden Row\'s Earn screen','p1')+shot('burn','Linden Row\'s Burn screen','p2')+'''
<div class="float f1"><small>Earn · waiting for your OK</small><b>Ads 1x → 4x</b>$7,200 a year, est.</div>
<div class="float f2"><small>Burn · on pace</small><b>Tokyo, 32% there</b>Business for 2, est.</div>
</div>
</article>

<article class="beat" id="b4" style="display:block">
<div class="whead reveal"><div><div class="bn"><i>04</i>The win</div><h3 class="h3">The money shows up. <span class="brush gold">The app cheers.</span></h3></div>
<div><p class="short">Earn goes from 1.2x to 3.4x.</p><p>$6,720 a year is confirmed against his statements. Tokyo in business for two is 32% there, on pace for March 2027. All est.</p></div></div>
<div class="win3">
<div class="wcards">'''+scorecard()+'''</div>
<div class="reveal d1 celcol">'''+celphone(cs_found(' on')+cs_ahead()+cs_goal())+'''<div class="celnav"><button>Found money</button><button>Ahead</button><button>Milestone</button></div></div>
<div class="wcards">'''+versus()+share()+'''</div>
</div>
</article>

<article class="beat" id="b5" style="display:block">
<div class="reveal"><div class="bn"><i>05</i>Why you</div><h3 class="h3">You run the business. <span class="brush">The desk runs the points.</span></h3>
<p class="short" style="max-width:640px">Same spend. More points. Better trips, for fewer points.</p></div>
<div class="why">
<div class="reveal"><b>$550</b><span>Flat monthly, whatever the spend. Cancel anytime.</span></div>
<div class="reveal d1"><b>20 min</b><span>The Found Money Call, free.</span></div>
<div class="reveal d2"><b>Friday</b><span>Your scorecard. One number, in dollars.</span></div>
<div class="reveal d3"><b>Yours</b><span>Every move is your call. The desk books after vetting.</span></div>
</div>
</article>

</div></div></div></section>
'''+cta()+'</main>\n'+footer()+scripts(True)+'</body>\n</html>\n'
    return h

# ---------------- PRODUCT ----------------
def product():
    h=head('First Officer | Product','One desk, four pillars: Earn, Burn, Return, Learn. See how First Officer works and what you see in the app.')
    h+='<body>\n'+nav('Product')+ticker()+'<main>\n'
    h+='''<section class="phead"><div class="wrap g">
<div class="reveal"><span class="kick">Product</span><h1>One desk. <span class="brush">Four pillars.</span> <span class="l3">Every move your call.</span></h1>
<p class="lede">First Officer is one conversation. Behind it, specialists across 50+ programs, trained on new data nightly. Here is how the desk works, and what you see in the app.</p>
<div class="pillchips"><span><b>01</b>Earn</span><span><b>02</b>Burn</span><span><b>03</b>Return</span><span><b>04</b>Learn</span></div>
<div class="ctas"><a class="btn pk" href="book.html">Book the Found Money Call <span class="ar">→</span></a><a class="btn ghost" href="#tour">See the app</a></div></div>
<div class="fan reveal d2">'''+shot('earn','Linden Row\'s Earn screen','a')+shot('burn','Linden Row\'s Burn screen','b')+shot('return','Linden Row\'s Return screen','c')+'''</div>
</div></section>

<section class="sec" style="padding-top:60px" id="how"><div class="how onink"><div class="wrap">
<div class="reveal"><span class="kick">How it works</span><h2 class="h2">Ask once. <span class="brush">The whole desk</span> works it.</h2>
<p class="lede">You talk to First Officer. The right specialists pick it up, check it against your spend and the latest rules, and hand back one clear answer.</p></div>
<div class="howg">
<ol class="steps reveal">
<li class="on"><b>Talk for 20 minutes</b><span>The Found Money Call, free. Your spend, your goals, your trips.</span></li>
<li><b>Get your Bespoke Strategy</b><span>Which card for which spend, line by line. Reviewed weekly.</span></li>
<li><b>Approve moves in one tap</b><span>Nothing moves without your yes.</span></li>
<li><b>Read your Friday scorecard</b><span>One number, in dollars, every week.</span></li>
<li><b>Plan the trip. The desk books.</b><span>We vet the requirements with you, then book after you approve.</span></li>
</ol>
<div class="desk reveal d1" aria-label="Animation: specialists pick up a question and hand one answer to First Officer">
<div class="q"></div>
<div class="core"><div class="tile"><img src="img/fo-chevron-alpha.png" alt=""></div><div class="lbl">First Officer<small>At the Desk</small></div></div>
<div class="a"></div>
</div>
</div></div></div></section>

<section class="sec" id="tour"><div class="wrap">
<div class="reveal"><span class="kick">Inside the app</span><h2 class="h2">Earn. Burn. Return. <span class="brush">Learn.</span></h2>
<p class="lede">Earn, Burn and Return belong to the company. Learn belongs to the person. Here is Leo's desk at Linden Row Insurance. Example data.</p></div>
<div class="tour">
<div class="reveal"><div class="phone"><div class="scr stack">
<img src="img/rec/app/home-am.webp" data-greet="img/rec/app/home-{p}.webp" alt="Desk home screen">
<img src="img/rec/app/earn.webp" alt="Earn screen" style="opacity:0">
<img src="img/rec/app/burn.webp" alt="Burn screen" style="opacity:0">
<img src="img/rec/app/return.webp" alt="Return screen" style="opacity:0">
<img src="img/rec/app/learn.webp" alt="Learn screen" style="opacity:0">
</div></div></div>
<div class="tside reveal d1">
<div class="ttabs" role="tablist"><button>Desk</button><button>Earn</button><button>Burn</button><button>Return</button><button>Learn</button></div>
<div class="tpane"><span class="kick">The desk</span><h3 class="h3">Good morning, Leo. Here is your day.</h3><p>All four pillars in one view. The greeting follows your time of day. Ask First Officer anything, in one conversation.</p>
<div class="facts"><div><b>4</b><span>pillars, one view</span></div><div><b>1</b><span>conversation, every pillar</span></div><div><b>50+</b><span>programs watched nightly</span></div></div></div>
<div class="tpane"><span class="kick">Pillar 01 · Earn</span><h3 class="h3">Linden Row's Earn.</h3><p>Which card for which spend. Each move shows what it is worth a year, and waits for your OK.</p>
<div class="facts"><div><b data-to="15120" data-pre="$">$15,120</b><span>found per year, est.</span></div><div><b>3.4x</b><span>per $1, was 1.2x</span></div><div><b>1</b><span>move waiting for your OK</span></div></div></div>
<div class="tpane"><span class="kick">Pillar 02 · Burn</span><h3 class="h3">Linden Row's Burn.</h3><p>Turn points into trips. A goal, a pace, and a plan. The desk vets the requirements and books after you approve.</p>
<div class="facts"><div><b data-to="32" data-suf="%">32%</b><span>of the Tokyo goal</span></div><div><b>102,400</b><span>of about 320,000 points</span></div><div><b>Mar 2027</b><span>on pace, est.</span></div></div></div>
<div class="tpane"><span class="kick">Pillar 03 · Return</span><h3 class="h3">Linden Row's Return.</h3><p>What the desk found, counted in dollars and checked against your statements. Every Friday.</p>
<div class="facts"><div><b data-to="1860" data-pre="$">$1,860</b><span>last Friday, week 43</span></div><div><b>$6,720</b><span>since joining, est.</span></div><div><b>3</b><span>findings last week</span></div></div></div>
<div class="tpane"><span class="kick">Pillar 04 · Learn</span><h3 class="h3">Leo's Learn.</h3><p>One short lesson a week, built from your own data. What changed in your programs, and what it means for your goal.</p>
<div class="facts"><div><b>1.6¢</b><span>what one card point is worth, est.</span></div><div><b>2 min</b><span>this week's lesson</span></div><div><b>Weekly</b><span>from your own data</span></div></div></div>
</div>
</div></div></section>

<section class="sec onink" id="cheer" style="border-radius:40px;margin:0 16px"><div class="wrap">
<div class="reveal"><span class="kick">The win</span><h2 class="h2">When money lands, <span class="brush">the app cheers.</span></h2>
<p class="lede">Found money, a month ahead of flat cash back, a points milestone. Each one gets its moment. All figures are examples and estimates.</p></div>
<div class="cels">
<figure class="reveal">'''+celphone(cs_found(' on'),'','data-auto="0"')+'''<figcaption><b>Found money</b><span>+$6,720 a year, confirmed, est.</span></figcaption></figure>
<figure class="reveal d1">'''+celphone(cs_ahead(' on'),'','data-auto="0" data-delay="500"')+'''<figcaption><b>Ahead of flat cash back</b><span>$654 this month, after the fee, est.</span></figcaption></figure>
<figure class="reveal d2">'''+celphone(cs_goal(' on'),'','data-auto="0" data-delay="1000"')+'''<figcaption><b>Points milestone</b><span>102,400 toward Tokyo, est.</span></figcaption></figure>
</div>
<div class="cels-cards">'''+scorecard()+versus()+share()+'''</div>
</div></section>

<section class="sec" id="after"><div class="wrap">
<div class="reveal"><span class="kick">After you're in</span><h2 class="h2">Your first 90 days, <span class="brush">step by step.</span></h2>
<p class="lede">Some things are fast. Some take time. Here is what happens, and what we ask of you.</p></div>
<div class="after">
<div class="reveal"><small>Today</small><b>Your desk opens</b><span>Tell First Officer about your spend and goals. About 10 minutes.</span></div>
<div class="reveal d1"><small>Day 1</small><b>Day One fixes</b><span>Time-boxed fixes first: a credit about to reset, points about to lapse.</span></div>
<div class="reveal d2"><small>Within 24 hours</small><b>Your Bespoke Strategy</b><span>Which card for which spend, line by line.</span></div>
<div class="reveal d3"><small>Week 1</small><b>Your first moves</b><span>Three moves, with the exact taps shown. Nothing moves without your yes.</span></div>
<div class="reveal"><small>Every Friday</small><b>Your scorecard</b><span>One number, in dollars, never in points.</span></div>
<div class="reveal d1"><small>Month 1</small><b>Us vs flat cash back</b><span>Your month next to a flat 2% card, after the $550 fee.</span></div>
<div class="reveal d2"><small>Month 3</small><b>Your first trip goal</b><span>The desk vets the requirements with you and books after you approve.</span></div>
</div>
</div></section>
'''+cta()+'</main>\n'+footer()+scripts(False)+'</body>\n</html>\n'
    return h

open(os.path.join(ROOT,'home-recovered.html'),'w').write(home())
open(os.path.join(ROOT,'product-recovered.html'),'w').write(product())
print('built')
