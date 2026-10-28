# Builds calculator-modes.html at the repo root: a standalone, editorial ROI calculator.
# No app screens. Site chrome (nav, 32px ticker, footer) identical to home-modes. Mockup only.
import os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import build as B

WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call'

def hero():
    return '''<section class="ch" id="top"><div class="cw chg">
<div class="cht">
<span class="mpill"><i></i>The calculator · est.</span>
<h1>Every program is built to outnumber you. See what your spend is <span class="pk">really worth.</span></h1>
</div>
<div class="chp">
<p class="clede">Type what you put on cards each month. You'll see what it earns today, what it could earn with your desk, and whether $550 a month pays for itself. If it doesn't, we'll say so.</p>
<dl class="cfacts"><div><dt>Flat fee</dt><dd>$550<small>a month</small></dd></div><div><dt>Fit gate</dt><dd>~$25K<small>a month on cards</small></dd></div><div><dt>Found Money Call</dt><dd>20 min<small>free</small></dd></div></dl>
</div>
</div></section>
'''

def tool():
    return '''<section class="ct" id="calc"><div class="cw"><div class="cbox">
<div class="cin">
<div class="clab cle"><span>01 · Start from an example</span><small id="cwho">Fictional owners</small></div>
<div class="cex" id="cex" role="tablist" aria-label="Example owners"></div>
<div class="clab cle c2"><span>02 · Your spend by line, a month</span><small>Today → with your desk, per $1</small></div>
<div class="crows" id="crows"></div>
<div class="csum">
<div><small>On cards</small><b id="ctot">$35,000</b><span>a month</span></div>
<div><small>A year</small><b id="ctoty">$420k</b><span>on cards</span></div>
<div><small>Earns today</small><b id="cbl">1.2x</b><span>per $1, est.</span></div>
<div class="csm"><small>Points a year</small><b><span data-k="today">504k</span> → <span class="pk" data-k="desk">1.43M</span></b><span>est.</span></div>
</div>
<div class="cgap"><div class="clab c2">04 · Where the extra comes from<small>Extra points a year, by line</small></div><div id="cgap"></div></div>
<div class="cmix"><span>Your cards today</span><div class="cseg" id="cmix" role="radiogroup" aria-label="Your cards today">
<button type="button" data-m="ex" class="on" role="radio" aria-checked="true">As entered</button><button type="button" data-m="1" role="radio" aria-checked="false">One 1x card</button><button type="button" data-m="1.5" role="radio" aria-checked="false">One 1.5x card</button><button type="button" data-m="2" role="radio" aria-checked="false">2% cash back</button></div></div>
</div>
<aside class="cres" aria-live="polite">
<div class="clab cle"><span>03 · Your result</span><small>Points a year, est.</small></div>
<div class="cbig"><div class="cbt"><small>Today</small><b data-k="today">504k</b></div><span class="car" aria-hidden="true">→</span><div class="cbd"><small>With your desk</small><b data-k="desk">1.43M</b></div></div>
<div class="cbars"><div><span>Today</span><u><i id="cbT"></i></u></div><div><span>With your desk</span><u><i class="cg" id="cbD"></i></u></div></div>
<dl class="cdl">
<div><dt>Extra points a year</dt><dd data-k="plus">+924k</dd></div>
<div><dt>Worth, est. at 1.0¢ to 1.6¢</dt><dd data-k="range">$7.9k–$12.6k</dd></div>
<div><dt>Your desk, $550 a month</dt><dd>$6,600</dd></div>
<div class="cnet"><dt>Left after the fee, est.</dt><dd data-k="net">+$1.3k to +$6k</dd></div>
</dl>
<div class="cscale"><div class="csh"><span>Value range vs the fee</span><b data-k="vsh">Clears</b></div><div class="csc" id="cvs"><i class="band"></i><i class="fee"></i><em class="feel">$6,600 fee</em></div></div>
<div class="cscale"><div class="csh"><span>Fit gate · ~$25K a month on cards</span><b data-k="gatev">$35K</b></div><div class="csc gate" id="cgt"><i class="fill"></i><i class="fee"></i><em class="feel">~$25K</em></div></div>
<div class="cv" id="cv"><div class="cvl">Verdict</div><h3 id="cvt">Clears the fee.</h3><p id="cvp"></p><ol id="cvo"></ol>
<div class="cbtn"><a class="btn pk" id="cc1" href="book.html">Book your Found Money Call <span class="ar">→</span></a><a class="btn wa" href="'''+WA+'''">💬 Text Your First Officer</a></div></div>
</aside>
</div></div></section>
'''

def burn():
    return '''<section class="cx cburn" id="burn"><div class="cw">
<div class="chd"><div><span class="clab clb"><span>Burn · what that buys</span></span><h2>A year of points, <span class="pk">going further.</span></h2></div>
<p>A year of points with your desk, set against a few example trips. Points prices move by date and program, so every figure here is an estimate.</p></div>
<div class="ctrips" id="ctrips"></div>
<p class="cnote">No seats are held or shown here. When you want a trip, your desk checks the live price with you and books only after you approve.</p>
</div></section>
'''

def assume():
    rows=[('Earn rates','Each line earns the rate shown, today and with your desk. "Your cards today" swaps your current rate for one flat card.'),
          ('Points used','We count 85% of the points you earn. The rest stays out of every estimate.'),
          ('Point value','1.0¢ a point at the low end (cash back) to 1.6¢ at the high end (a well-planned trip).'),
          ('The fee','$550 a month, flat, whatever your spend. That is $6,600 a year, set against the value range.'),
          ('The fit gate','About $25K a month on cards. Below that, the fee usually costs more than it finds, so we say it is not a fit yet.'),
          ('Verdict','Clears the fee when even the low end beats $6,600. Close call when only the top end does.'),
          ('Trips','Example points prices for common trips. No seats are held. Your desk books only after you approve.'),
          ('Examples','Every owner shown is fictional. Your Found Money Call checks the numbers against your real statements.')]
    return '''<section class="cx cas" id="assumptions"><div class="cw">
<div class="chd"><div><span class="clab cll"><span>Learn · the assumptions</span></span><h2>How the math works, <span class="pk">plainly.</span></h2></div>
<p>No hidden multipliers. Everything the calculator uses is on this list, and every figure is an estimate.</p></div>
<dl class="casl">'''+''.join('<div><dt>%s</dt><dd>%s</dd></div>'%r for r in rows)+'''</dl>
</div></section>
<section class="cx ccta"><div class="cw"><div class="cctab">
<div><span class="clab cle"><span>Next · 20 minutes, free</span></span><h2>Bring your statements to <span class="pk">the Found Money Call.</span></h2><p>Your desk runs this on your real numbers. If $550 a month doesn't clear, you'll hear that on the call.</p></div>
<div class="cctb"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn ghost" href="book.html">Book the Found Money Call</a></div>
</div></div></section>
'''

def page():
    h=B.head('Calculator | What is your spend really worth? | First Officer','Type your monthly card spend and see what it earns today, what it could earn with your desk, and whether $550 a month clears. Estimates only.')
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">\n<link rel="stylesheet" href="recovered/calc.css">')
    h+='<body class="modes calc">\n'+B.nav('Calculator').replace('home-recovered.html','home-modes.html')+B.ticker()+'<main>\n'+hero()+tool()+burn()+assume()+'</main>\n'
    h+=B.footer().replace('home-recovered.html','home-modes.html').replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.','Every owner shown is a fictional example. All figures are examples and estimates.')
    h+='<script>window.FO_A="'+B.ASSET+'";</script>\n<script src="recovered/rec.js"></script>\n<script src="recovered/fo-modes-data.js"></script>\n<script src="recovered/calc.js"></script>\n</body>\n</html>\n'
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
