# Builds calculator-modes.html at the repo root: the calculator as a sibling of home-modes.html.
# Same hero system as the landing (rotating background photos, crossfade, cream overlay, hero type),
# the Basic calculator as a landing-style card in the hero, then Go advanced, How we got this number,
# and the landing's compact CTA. Site chrome (nav, 32px ticker, footer) identical to home-modes. Mockup only.
import os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import build as B

WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call'
# the landing's program logos and Ohad's signature, read from build_modes.py (not imported: importing it rebuilds the landing)
_BM=open(os.path.join(HERE,'build_modes.py')).read()
SIG=re.search(r"^SIG='(.*?)'\s*$",_BM,re.M).group(1)
LOGOS=[1,12,2,17,47,18,25,9]
NAMES={1:'Amex',2:'Chase',17:'United',12:'Hyatt',47:'Virgin Atlantic',25:'Aeroplan',9:'Marriott',18:'Delta'}
SL={1:'amex',2:'chase',17:'united',12:'hyatt',47:'virgin-atlantic',25:'aeroplan',9:'marriott',18:'delta'}

def bal(id_):
    return """<div class="cbal" id="""+'"'+id_+'"'+""" role="img" aria-label="Monthly value found against the $550 fee">
<div class="cbt"><i class="base"></i><i class="over"></i><i class="short"></i><i class="rng"></i><i class="mark"><span>$550 fee</span></i></div>
<div class="cbx"><span>$0</span><span data-k="bmax">$1,650</span></div>
</div>"""

def card():
    return """<div class="cq fit" id="bas">
<div class="cqh"><span class="wk">Does it clear the fee?</span><a class="cqa" href="#advs" id="bgo">Go advanced <span class="ar">↓</span></a></div>
<label class="bql" for="bv">Your business card spend each month</label>
<div class="bin"><span>$</span><input id="bv" type="text" inputmode="numeric" autocomplete="off" value="35,000" aria-label="Your business card spend each month, in dollars"><small>a month</small></div>
<div class="bsw"><input id="bs" class="bsl" type="range" min="0" max="100000" step="500" value="35000" aria-label="Your business card spend each month, slider"><i class="bgt" style="left:25%"><span>~$25K fit</span></i></div>
<div class="bsx"><span>$0</span><span>$50K</span><span>$100K+</span></div>
<div class="ba" aria-live="polite">
<div class="baf"><span class="wk">Your desk finds</span><b class="bfind" data-k="find">~$850</b><span class="bsub">a month found, est. <em data-k="findr">$650–$1,050</em></span></div>
<dl class="bk"><div><dt>vs the fee</dt><dd>$550</dd><small>a month, flat</small></div><div class="ret"><dt>Return</dt><dd data-k="rx">1.5×</dd><small><span data-k="net">+$300</span> a month left</small></div></dl>
</div>
"""+bal('bbal')+"""
<p class="bverd"><b class="bvk" aria-hidden="true">✓</b><span><strong id="bvt">Clears the fee.</strong> <span id="bvp"></span></span></p>
<div class="bact"><button type="button" class="brun" id="brun" aria-pressed="false"><i></i><span>Watch it run</span></button><small>$10K to $80K. Touch anything to stop.</small></div>
<div class="mctas"><a class="btn pk" id="bc1" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn wa" href='"""+WA+"""'>💬 Text Your First Officer</a></div>
<p class="wfine">Blended rate, est.: about 1.2 points per $1 on your cards today, about 3.4 with your desk. Your lines can earn more or less. <a href="#advs">Go advanced</a> for every line.</p>
</div>"""

def hero():
    logos=''.join('<img src="img/hero/prog/%02d-%s.jpg" alt="%s">'%(n,SL[n],NAMES[n]) for n in LOGOS)
    return """<section class="mh ch" id="mh"><div class="mbg" aria-hidden="true"></div>
<div class="chw">
<div class="chl">
<span class="mpill"><i></i>The calculator · est.</span>
<h1>Every loyalty program is built to confuse you. <span class="pk">Here's what your spend is really worth.</span></h1>
</div>
<div class="chr">"""+card()+"""</div>
<div class="chb">
<ul class="mprob cok" aria-label="What you get here">
<li><b>✓</b><span>One slider. One answer, in dollars a month.</span></li>
<li><b>✓</b><span>Set against the $550 a month fee, side by side.</span></li>
<li><b>✓</b><span>Not a fit? It says so, plainly.</span></li>
</ul>
<p class="msub">Move the slider to what your business puts on cards each month. You see what your desk finds, est., next to its flat fee. Want every line of your spend? Go advanced below.</p>
<div class="mlogos">"""+logos+"""<span>Every loyalty program. One desk to rule them all.</span></div>
</div>
</div></section>
"""

def mini():
    return """<div class="cmini" aria-hidden="true"><div><small>Desk finds</small><b data-k="m-find">~$850</b></div><div><small>Fee</small><b>$550</b></div><div><small>Return</small><b class="rx" data-k="m-rx">1.5×</b></div></div>"""

def advanced():
    return """<section class="sec cadv" id="advs"><div class="wrap">
<div class="reveal"><span class="kick">Go advanced · 2 minutes</span><h2 class="h2">Every line of your spend. <span class="brush">Every card, every point.</span></h2>
<p class="lede">Pick your industry for a typical spend mix, then type your own numbers. Each line goes to its best card, and the answer moves as you do.</p></div>
<div class="cbox" id="adv">
<div class="cin">
"""+mini()+"""
<div class="clab"><span><label for="cind">Your industry</label></span><small id="cwho">Typical mix: $35K a month, est.</small></div>
<div class="csel"><select id="cind" aria-describedby="cwho"><option>Insurance agency</option></select></div>
<div class="ccon" aria-live="polite"><b id="ccth">Things to consider for insurance agency</b><ul id="ccul"></ul><small>General prompts, not advice. Your Found Money Call goes through your real lines.</small></div>
<div class="clab c2"><span>Your spend by line, a month</span><small>Type or drag</small></div>
<div class="crows" id="crows"></div>
<div class="csum"><div><small>On cards</small><b data-k="mo">$35,000</b><span>a month</span></div><div><small>Earns today</small><b data-k="bl">1.2x</b><span>per $1, est.</span></div><div><small>Points today</small><b data-k="vt">42k</b><span>a month</span></div></div>
<div class="cpick">
<div class="cmix"><span>Your cards today</span><div class="cseg" id="cmix" role="radiogroup" aria-label="Your cards today">
<button type="button" data-m="ex" class="on" role="radio" aria-checked="true">As entered</button><button type="button" data-m="1" role="radio" aria-checked="false">One 1x card</button><button type="button" data-m="1.5" role="radio" aria-checked="false">One 1.5x card</button><button type="button" data-m="2" role="radio" aria-checked="false">2% cash back</button></div></div>
<div class="cuse"><span>How you'll use the points</span><div class="cul" id="cuse" role="radiogroup" aria-label="How you will use the points"></div><p class="cfine">Cents a point, est. The floor is a plain cash out. The top is a level a well-planned booking can reach again and again, not a one-off.</p></div>
</div>
</div>
<aside class="cres" aria-live="polite"><div class="cstk">
<div class="clab"><span class="rr">Your month, est.</span><small data-k="who">Insurance agency · at 1.0¢–1.6¢ a point</small></div>
<div class="chead">
<div class="cfind"><small>Your desk finds</small><b data-k="find">~$850</b><span>a month found, est. <em data-k="findr">$650–$1,050</em></span></div>
<div class="cvs">vs</div>
<div class="cfee"><small>Your desk costs</small><b>$550</b><span>a month, flat</span></div>
</div>
"""+bal('cbal')+"""
<dl class="ckpi">
<div class="net"><dt>Left each month</dt><dd data-k="net">+$300</dd><small data-k="netr">+$100 to +$500, est.</small></div>
<div class="ret"><dt>Return</dt><dd data-k="rx">1.5×</dd><small data-k="rxr">1.2× to 1.9×, est.</small></div>
<div><dt>Extra points</dt><dd data-k="plus">+77k</dd><small>a month; we count 85%</small></div>
</dl>
<div class="cv" id="cv"><h3><b class="bvk" aria-hidden="true">✓</b><span id="cvt">Clears the fee.</span></h3><p id="cvp"></p></div>
<div class="cet" id="cet" role="table" aria-label="Points a month by line"></div>
<div class="cgate"><div class="csh"><span>Fit gate · ~$25K a month on cards</span><b data-k="gatev">You: $35K</b></div><div class="csc" id="cgt"><i class="fill"></i><i class="fee"></i></div></div>
<div class="cbtn"><a class="btn pk" id="cc1" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn wa" href='"""+WA+"""'>💬 Text Your First Officer</a></div>
<a class="chowl" href="#how">How we got this number ↓</a>
</div></aside>
</div>
</div></section>
"""

def how():
    S=[('earn','01','Earn','Each line goes to its best card','Ads and software to the 4x card, internet and phone to 3x, the rest to 2x. That is your desk\'s points a month, next to what your cards earn today.'),
       ('burn','02','Count','Only 85% of the new points count','Some points always go unused, so 15% stays out of every estimate. Your points today are not counted at all, only the extra.'),
       ('learn','03','Value','Valued at how you will use them','A cash out is the floor, about 1¢ a point. Planned trips run higher. The answer is the middle of that range, and the range is shown.'),
       ('fee','04','Fee','Then the $550 comes off','What your desk finds, against $550 a month, flat. Return is the one divided by the other. Under ~$25K a month on cards, it says not a fit yet.')]
    cards=''.join('<div class="pc4 k-%s reveal d%d"><div class="pn"><b>%s</b>%s</div><h3>%s</h3><p>%s</p></div>'%(k,i,n,t,h,p) for i,(k,n,t,h,p) in enumerate(S))
    rows=[('Basic','One spend figure at a blended rate: about 1.2 points per $1 today and about 3.4 with your desk. That is a service business like the insurance agency mix, so Basic at $35K matches it.'),
          ('Advanced','Your spend by line, at the rate shown for each line, today and with your desk. "Your cards today" can swap your rates for one flat card.'),
          ('Cents a point','Mixed 1.0¢–1.6¢, cash out 1.0¢, economy 1.0¢–1.4¢, top hotels 1.2¢–2.0¢, business class 1.5¢–2.0¢. Estimates, not results from past bookings.'),
          ('Verdict','Clears the fee when even the floor beats $550 a month. Close call when only the top does. Under ~$25K a month on cards, not a fit yet.')]
    return """<section class="sec chow" id="how"><div class="wrap">
<div class="reveal"><span class="kick">How we got this number</span><h2 class="h2">The math, in plain words. <span class="brush">Four steps, no magic.</span></h2>
<p class="lede">The same four steps run on your Found Money Call, from your real statements. Every figure here is an estimate.</p></div>
<div class="p4">"""+cards+"""</div>
<details class="cdet"><summary>Every assumption, line by line</summary><dl class="casl">"""+''.join('<div><dt>%s</dt><dd>%s</dd></div>'%r for r in rows)+"""</dl>
<p class="cnote">Points prices move by date and program. Your desk checks live prices with you and books only after you approve.</p></details>
<div class="cpro reveal">
<p class="mlead">If your numbers don't clear $550 a month, I'll tell you on the call, in writing. You won't pay a cent.</p>
<div class="cpsig">"""+SIG+"""<span><b>Ohad Sternberg</b>Founder, UpNonStop</span></div>
</div>
</div></section>
<section class="sec tight"><div class="wrap"><div class="why">
<div class="reveal"><b>$550</b><span>Flat monthly, whatever your spend. Cancel anytime.</span></div>
<div class="reveal d1"><b>20 min</b><span>Your Found Money Call, free.</span></div>
<div class="reveal d2"><b>Friday</b><span>Your scorecard. One number, in dollars.</span></div>
<div class="reveal d3"><b>Yours</b><span>Every move is your call. The desk books after you approve.</span></div>
</div>
<div class="pcta"><div class="pctx"><b>Get your desk.</b><span>$550 a month, flat. Cancel anytime. The desk books only after you approve.</span></div><div class="pbtn"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn wa" href='"""+WA+"""'>💬 Text Your First Officer</a></div></div>
</div></section>
"""

def page():
    h=B.head('Calculator | What is your spend really worth? | First Officer','Put in your business card spend each month and see what your desk finds against its $550 a month fee. Estimates only.')
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kalam:wght@300;400&display=swap">\n<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">\n<link rel="stylesheet" href="recovered/calc.css">')
    h+='<body class="modes calc">\n'+B.nav('Calculator').replace('home-recovered.html','home-modes.html')+B.ticker()+'<main>\n'+hero()+advanced()+how()+'</main>\n'
    h+=B.footer().replace('home-recovered.html','home-modes.html').replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.','Every industry mix shown is a typical example. All figures are examples and estimates.')
    h+='<script>window.FO_A="'+B.ASSET+'";</script>\n<script src="recovered/rec.js"></script>\n<script src="recovered/fo-modes-data.js"></script>\n<script src="recovered/fo-calc-basis.js"></script>\n<script src="recovered/calc.js"></script>\n</body>\n</html>\n'
    h=h.replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')
    h=re.sub(r'<div class="mcta">.*?</a></div>\n?','',h,flags=re.S)
    # nav exactly as the landing: pink Get your desk + green Text Your First Officer (bar and menu sheet)
    h=h.replace('<a class="btn pk" href="'+WA+'">💬 Text Your First Officer</a>\n<button class="burger"','<span class="nbtns"><a class="btn pk" href="book.html">Get your desk</a><a class="btn wa" href="'+WA+'">💬 Text Your First Officer</a></span>\n<button class="burger"',1)
    h=h.replace('<a class="btn pk" href="'+WA+'">💬 Text Your First Officer</a>\n</div>','<a class="btn wa" href="'+WA+'">💬 Text Your First Officer</a>\n</div>',1)
    assert 'class="nbtns"' in h and 'class="btn pk" href="'+WA not in h
    h=h.replace('href="calculator.html"','href="calculator-modes.html"')
    return B.absol(h)
open(os.path.join(B.ROOT,'calculator-modes.html'),'w').write(page())
print('built calculator-modes.html')
