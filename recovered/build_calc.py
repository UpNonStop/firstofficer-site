# Builds calculator-modes.html at the repo root: the calculator on the home-modes design system
# (rec.css + modes.css tokens, same nav, ticker, footer and fonts) plus recovered/calc.css and calc.js. Mockup only.
import os,sys,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build as B

def main():
    return '''<section class="ch" id="top"><div class="wrap chw">
<div class="chl">
<span class="mpill"><i></i>The calculator · est.</span>
<h1>Your spend, run through <span class="pk">your desk.</span></h1>
<p class="chs">Move the sliders. You see what your spend earns today, what it could earn with your desk, and whether $550 a month clears. If it doesn't, the calculator says so.</p>
</div>
<div class="chr"><span class="wk">Start from an example</span>
<div class="cex" id="cex" role="tablist" aria-label="Example owners"></div>
<p class="cexn">Every owner here is a fictional example. Ines is under the gate, so you can see an honest no.</p></div>
</div></section>

<section class="cs0" id="calc"><div class="wrap cgrid">
<div class="cin">
<div class="cc c-earn">
<div class="cch"><span class="cpl">Earn</span><h2>Your spend by category</h2><span class="cmini" id="cmini"></span></div>
<p class="ccs" id="cwho"></p>
<div class="crows" id="crows"></div>
<div class="ctot"><span>On cards</span><b id="ctot">$35,000 a month</b><small id="ctoty">$420k a year</small></div>
</div>
<div class="cc c-mix">
<div class="cch"><span class="cpl">Earn</span><h2>Your card mix today</h2></div>
<p class="ccs">What your spend runs on now. The desk's mix is on the right of each line below.</p>
<div class="cseg" id="cmix" role="radiogroup" aria-label="Card mix today">
<button type="button" data-m="ex" class="on" role="radio" aria-checked="true">Your mix<small>per line, example</small></button>
<button type="button" data-m="1" role="radio" aria-checked="false">One 1x card<small>1 point per $1</small></button>
<button type="button" data-m="1.5" role="radio" aria-checked="false">One 1.5x card<small>flat card</small></button>
<button type="button" data-m="2" role="radio" aria-checked="false">2% cash back<small>counted as 2x</small></button>
</div>
<table class="croute" aria-label="How your desk routes your spend"><thead><tr><th>Line</th><th>Today</th><th>With your desk</th><th>Points a year, est.</th></tr></thead><tbody id="croute"></tbody></table>
</div>
</div>

<aside class="cout" aria-live="polite">
<div class="cr">
<span class="wk">Your result, est.</span>
<small class="clab">Points a year</small>
<div class="cnum"><span id="rToday">495k</span><i>→</i><b id="rDesk">1.32M</b></div>
<div class="cbars"><div><span>Today</span><u><i id="bT"></i></u></div><div><span>With your desk</span><u><i class="g" id="bD"></i></u></div></div>
<div class="cblend" id="rBlend"></div>
<div class="crng"><div><small>Value of the extra points, est.</small><b id="rVal">$7.0k–$11.2k</b><span>a year</span></div><div><small>Your desk</small><b>$6,600</b><span>a year · $550 a month, flat</span></div></div>
<div class="cgate"><div class="cgt"><small>Fit gate</small><span>~$25K a month on cards</span></div><div class="cgm"><u><i id="gFill"></i></u><em class="cgk"></em></div><div class="cgl"><span>$0</span><span>$25K</span><span>$60K a month</span></div></div>
<div class="cv" id="rV"><b id="rVt">A fit, by this estimate</b><p id="rVp"></p></div>
<div class="cctas"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn ghost" href="book.html">The Found Money Call</a></div>
<p class="cfine">The Found Money Call is 20 minutes and free. Estimates only: 85% of points used, 1.0¢ to 1.6¢ a point. Your call checks it against your real statements.</p>
</div>
</aside>
</div></section>

<section class="sec tight cburn" id="burn"><div class="wrap">
<div class="cbh"><div><span class="kick">What you could do with it</span><h2 class="h2">Your points, <span class="brush">going further.</span></h2></div>
<p class="lede">A year of points with your desk, set against a few example trips. Points prices change by date and program, so every figure is an estimate.</p></div>
<div class="cb4" id="cb4"></div>
<p class="p4f">No seats are held or shown here. When you want a trip, your desk checks the live price with you and books only after you approve.</p>
</div></section>

<section class="sec tight crl"><div class="wrap"><div class="crl2">
<div class="cc c-ret"><div class="cch"><span class="cpl">Return</span><h2>Money found, every Friday</h2></div>
<div class="crlv"><b id="retV">$1,860</b><span>found in one example Friday, est.</span></div><ul class="crll" id="retL"></ul></div>
<div class="cc c-lrn"><div class="cch"><span class="cpl">Learn</span><h2 id="lrnH">What one card point is worth</h2></div>
<div class="crlv"><b id="lrnV">1.6¢</b><span id="lrnS">a point on your plan, est.</span></div><div class="clb" id="lrnB"></div><p class="ccs" id="lrnF"></p></div>
</div></div></section>

<section class="sec tight"><div class="wrap">
<div class="why">
<div><b>$550</b><span>Flat monthly, whatever your spend. Cancel anytime.</span></div>
<div><b>~$25K</b><span>A month on cards. Below that, we'll tell you it's not a fit.</span></div>
<div><b>85%</b><span>Of your points used. The rest is left out of every estimate.</span></div>
<div><b>1.0–1.6¢</b><span>A point, from cash back to a well-planned trip.</span></div>
</div>
<div class="pcta"><div class="pctx"><b>Get your desk.</b><span>$550 a month, flat. Cancel anytime. The desk books only after you approve.</span></div><div class="pbtn"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn ghost" href="book.html">The Found Money Call</a></div></div>
</div></section>
'''

def page():
    h=B.head('Calculator | First Officer','Run your spend through your desk: points a year today and with your desk, the value range, and an honest fit check against $550 a month. Estimates only.')
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">\n<link rel="stylesheet" href="recovered/calc.css">')
    nav=B.nav('Calculator').replace('home-recovered.html','home-modes.html')
    h+='<body class="modes calc">\n'+nav+B.ticker()+'<main>\n'+main()+'</main>\n'
    h+=B.footer().replace('home-recovered.html','home-modes.html').replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.').replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.','Every owner shown is a fictional example. All figures are examples and estimates.')
    h=re.sub(r'<div class="mcta">.*?</a></div>\n?','',h,flags=re.S)
    h=h.replace('href="calculator.html"','href="calculator-modes.html"')
    h+='<script>window.FO_A="'+B.ASSET+'";</script>\n<script src="recovered/rec.js"></script>\n<script src="recovered/fo-modes-data.js"></script>\n<script src="recovered/calc.js"></script>\n</body>\n</html>\n'
    return B.absol(h)
open(os.path.join(B.ROOT,'calculator-modes.html'),'w').write(page())
print('built calculator-modes.html')
