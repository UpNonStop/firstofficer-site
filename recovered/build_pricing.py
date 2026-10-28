# Builds pricing-modes.html at the repo root: Pricing as a sibling of home-modes.html and calculator-modes.html.
# Same hero system (rotating background photos), the calculator's Basic card embedded in the hero (same engine:
# calc.js + fo-calc-basis.js, same CSS: modes.css + calc.css), its Go advanced pill linking to the full calculator.
# Prices and promises as on pricing.html. Mockup only; every figure is an estimate.
import os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import build as B
import build_calc as C
WA=C.WA
FULL='calculator-modes.html'

def hero():
    logos=''.join('<img src="img/hero/prog/%02d-%s.jpg" alt="%s">'%(n,C.SL[n],C.NAMES[n]) for n in C.LOGOS)
    card=C.card(adv=FULL+'?m=adv',fine='Blended rate, est.: about 1.2 points per $1 on your cards today, about 3.4 with your desk. Your lines can earn more or less. <a href="'+FULL+'?m=adv" data-full="'+FULL+'">Run the full calculator</a> for every line.')
    card=card.replace('id="bgo">','id="bgo" data-full="'+FULL+'">',1)
    return """<section class="mh ch" id="mh"><div class="mbg" aria-hidden="true"></div>
<div class="chw">
<div class="chl">
<span class="mpill"><i></i>Pricing · one plan</span>
<h1>$550 a month, flat. <span class="pk">And an honest no if it won't clear.</span></h1>
</div>
<div class="chr">"""+card+"""</div>
<div class="chb">
<ul class="mprob cok" aria-label="What you pay">
<li><b>✓</b><span>One price for every business, whatever your spend.</span></li>
<li><b>✓</b><span>Rate locked at signup. Cancel anytime.</span></li>
<li><b>✓</b><span>Won't clear? You get a no, in writing, and never pay.</span></li>
</ul>
<p class="msub">Price is the second question. The first is whether your spend clears $550 a month. Move the slider to what your business puts on cards each month and see it, est., side by side.</p>
<div class="mlogos">"""+logos+"""<span>Every loyalty program. One desk to rule them all.</span></div>
</div>
</div></section>
"""

def prices():
    P=[('earn','$550','a month, flat','Your desk','Every line of your spend routed to its best card, every point used well, and a Friday scorecard in dollars. Rate locked at signup. Cancel anytime, no notice period and no exit fee.'),
       ('learn','$500','per itinerary, flat','Award trips','Never a percentage of the trip, any party size, for clients only. A family of five costs the same as a solo trip.'),
       ('fee','$0','20 minutes, free','Your Found Money Call','Six questions on the channel you choose, and your number from your real statements. No card needed, no obligation.')]
    cards=''.join('<div class="pc4 pp k-%s reveal d%d"><div class="pn"><b>%02d</b>%s</div><p class="ppv"><span>%s</span><small>%s</small></p><p>%s</p></div>'%(k,i,i+1,h,v,u,p) for i,(k,v,u,h,p) in enumerate(P))
    return """<section class="sec chow pnum" id="price"><div class="wrap">
<div class="reveal"><span class="kick">The number</span><h2 class="h2">One price. <span class="brush">No tiers, no percentage.</span></h2>
<p class="lede">What you pay is the same whatever you spend. What it finds depends on your spend, so the card above does that part.</p></div>
<div class="p4 p3">"""+cards+"""</div>
</div></section>
"""

def fit():
    F=[('earn','For you if','The math already favors you','You run a business with about $25K a month or more on cards. You would rather forward a statement than build the spreadsheet, and you are happy to judge your desk by one dollar number, every Friday.'),
       ('burn','Not for you if','The fee would eat the win','Under the bar, $550 a month costs more than it finds. The calculator says so above, and your Found Money Call says so too, before you pay anything.'),
       ('fee','The gate','A no, in writing','Your call works out your number from your real statements. If it does not clear the fee, you get a free and honest no. A fee that eats the win helps nobody.')]
    cards=''.join('<div class="pc4 k-%s reveal d%d"><div class="pn"><b>%s</b></div><h3>%s</h3><p>%s</p></div>'%(k,i,t,h,p) for i,(k,t,h,p) in enumerate(F))
    return """<section class="sec chow pfit" id="fit"><div class="wrap">
<div class="reveal"><span class="kick">Who it is for</span><h2 class="h2">Built for a specific owner. <span class="brush">Maybe you.</span></h2></div>
<div class="p4 p3">"""+cards+"""</div>
</div></section>
"""

def faq():
    Q=[('Is there a contract?','No. $550 a month, rate locked at signup. Cancel anytime, no notice period and no exit fee.'),
       ('Is the number above a promise?','No. Every figure is an estimate, labelled est. Your Found Money Call works it out from your real statements, and your Friday scorecard shows what actually happened.'),
       ('Do you take money from card issuers?','No. No affiliate money from any bank, airline or hotel program.'),
       ('Who makes the decisions?','You do. Every move waits for your yes, and your desk books only after you approve.'),
       ('What if my spend is under ~$25K a month?','Then it most likely won\'t clear the fee, and the calculator says not a fit yet. Keep the card you have and come back when the spend grows.'),
       ('How is the number worked out?','Your spend, at the rate it earns today and with your desk, 85% of the extra points counted, valued at how you will use them, then the $550 comes off. <a href="'+FULL+'#how">See every step</a>.')]
    rows=''.join('<div><dt>%s</dt><dd>%s</dd></div>'%q for q in Q)
    return """<section class="sec chow pfaq" id="faq"><div class="wrap">
<div class="reveal"><span class="kick">Questions</span><h2 class="h2">Asked on every call. <span class="brush">Answered here.</span></h2></div>
<details class="cdet" open><summary>Pricing questions</summary><dl class="casl pq">"""+rows+"""</dl></details>
<div class="cpro reveal">
<p class="mlead">If your numbers don't clear $550 a month, I'll tell you on the call, in writing. You won't pay a cent.</p>
<div class="cpsig">"""+C.SIG+"""<span><b>Ohad Sternberg</b>Founder, UpNonStop</span></div>
</div>
</div></section>
<section class="sec tight"><div class="wrap">
<div class="pcta"><div class="pctx"><b>Get your desk.</b><span>$550 a month, flat. Cancel anytime. The desk books only after you approve.</span></div><div class="pbtn"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn wa" href='"""+WA+"""'>💬 Text Your First Officer</a></div></div>
</div></section>
"""

def page():
    h=C.page()
    a=h.index('<main>')+len('<main>\n');b=h.index('</main>')
    h=h[:a]+hero()+prices()+fit()+faq()+h[b:]
    h=re.sub(r'<title>.*?</title>','<title>Pricing | $550 a month, flat | First Officer</title>',h,count=1,flags=re.S)
    h=re.sub(r'(<meta name="description" content=")[^"]*','\\1$550 a month, flat, for every business. Cancel anytime. See if your spend clears the fee, est., and get an honest no in writing if it will not.',h,count=1)
    h=h.replace('<a href="pricing-modes.html" class="">Pricing</a>','<a href="pricing-modes.html" class="on">Pricing</a>').replace('<a href="calculator-modes.html" class="on">Calculator</a>','<a href="calculator-modes.html" class="">Calculator</a>')
    assert 'class="on">Pricing' in h
    h=h.replace('<body class="modes calc">','<body class="modes calc pricing">')
    h=h.replace('Every industry mix shown is a typical example. All figures are examples and estimates.','All figures are estimates.')
    return B.absol(h)

if __name__=='__main__':
    open(os.path.join(B.ROOT,'pricing-modes.html'),'w').write(page())
    print('built pricing-modes.html')
