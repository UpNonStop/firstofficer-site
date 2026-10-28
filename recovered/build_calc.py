# Builds calculator-modes.html at the repo root: a standalone, editorial ROI calculator.
# No app screens. Site chrome (nav, 32px ticker, footer) identical to home-modes. Mockup only.
import os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import build as B

WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call'

def hero():
    return """<section class="ch" id="top"><div class="cw chg">
<div class="cht">
<span class="mpill"><i></i>The calculator · est.</span>
<h1>Every loyalty program is built to confuse you. Here's what your spend is <span class="pk">really worth.</span></h1>
</div>
<div class="chp">
<p class="clede">Put in what you spend on cards each month. Watch it turn into points, then trips, then a return on your desk fee. Every step is shown, and if $550 a month doesn't pay for itself, we'll say so.</p>
<dl class="cfacts"><div><dt>Flat fee</dt><dd>$550<small>a month</small></dd></div><div><dt>Fit gate</dt><dd>~$25K<small>a month on cards</small></dd></div><div><dt>Found Money Call</dt><dd>20 min<small>free</small></dd></div></dl>
</div>
</div></section>
"""

def rail():
    st=[('s0','01','Spend','spend','a month on cards'),('s1','02','Earn','vel','points a month with your desk'),
        ('s2','03','Timeline','first','to your first trip'),('s3','04','Burn','cpp','a point, est.'),('s4','05','Return','ret','on the $6,600 fee, est.')]
    return '<ol class="crail" aria-label="How your spend translates">'+''.join(
        '<li class="%s"><span class="crn">%s · %s</span><b data-k="r-%s">–</b><small data-k="r-%s-s">%s</small></li>'%(c,n,t,k,k,sub) for c,n,t,k,sub in st)+'</ol>'

def tool():
    return """<section class="ct" id="calc"><div class="cw"><div class="cbox">
"""+rail()+"""
<div class="cgrid">
<div class="cin">
<div class="clab"><span>01 · Spend</span><small id="cwho">Fictional owners</small></div>
<div class="cex" id="cex" role="tablist" aria-label="Start from an example owner"></div>
<div class="clab c2"><span>Your spend by line, a month</span><small>Type or drag</small></div>
<div class="crows" id="crows"></div>
<div class="csum"><div><small>On cards</small><b data-k="mo">$35,000</b><span>a month</span></div><div><small>A year</small><b data-k="yr">$420k</b><span>on cards</span></div><div><small>Earns today</small><b data-k="bl">1.2x</b><span>per $1, est.</span></div></div>
<div class="cmix"><span>Your cards today</span><div class="cseg" id="cmix" role="radiogroup" aria-label="Your cards today">
<button type="button" data-m="ex" class="on" role="radio" aria-checked="true">As entered</button><button type="button" data-m="1" role="radio" aria-checked="false">One 1x card</button><button type="button" data-m="1.5" role="radio" aria-checked="false">One 1.5x card</button><button type="button" data-m="2" role="radio" aria-checked="false">2% cash back</button></div></div>
<div class="cuse"><span>How you'll use the points</span><div class="cul" id="cuse" role="radiogroup" aria-label="How you will use the points"></div></div>
</div>
<div class="cearn">
<div class="clab cle"><span>02 · Earn</span><small>Points per $1, line by line</small></div>
<div class="cvel">
<div><small>Today</small><b data-k="vt">42k</b><span>points a month</span></div>
<div class="d"><small>With your desk</small><b data-k="vd">119k</b><span>points a month</span></div>
<div><small>Velocity</small><b data-k="vx">2.8×</b><span>faster, est.</span></div>
</div>
<div class="cet" id="cet" role="table" aria-label="Earn by line"></div>
<div class="clab cle c3"><span>03 · Timeline</span><div class="cseg sm" id="cunit" role="radiogroup" aria-label="Show the timeline as"><button type="button" data-u="pts" class="on" role="radio" aria-checked="true">Points</button><button type="button" data-u="usd" role="radio" aria-checked="false">Dollars</button><button type="button" data-u="trip" role="radio" aria-checked="false">Trips</button></div></div>
<div class="cchart" id="cchart"><svg id="csvg" role="img" aria-label="Points earned over 12 months, today and with your desk"></svg>
<div class="ckey"><span class="kt">Today</span><span class="kd">With your desk</span><span class="kg">The gap your desk finds</span></div></div>
<ol class="cms" id="cms"></ol>
</div>
</div>
<div class="cgrid2">
<div class="cburn">
<div class="clab clb"><span>04 · Burn</span><small>Based on how these points redeem, est.</small></div>
<div class="cbt" id="cbasis" role="table" aria-label="Cents per point by redemption type"></div>
<p class="cfine">Cents a point, est. Floor is a plain cash out. The bar runs to a level a well-planned booking can reach again and again, not a one-off. We count 85% of the extra points.</p>
<div class="clab clb c4"><span>What your extra points could be, a year</span><small>Points prices, est. 85% counted</small></div>
<div class="ctr" id="ctr"></div>
</div>
<aside class="cret" aria-live="polite">
<div class="clab"><span class="rr">05 · Return</span><small>On the extra points only</small></div>
<div class="cbigr"><small>Return of</small><b data-k="rx">1.5×</b><span data-k="rxr">1.2× to 1.9× est.</span></div>
<dl class="cdl">
<div><dt>Extra points a year</dt><dd data-k="plus">+924k</dd></div>
<div><dt data-k="rangel">Worth, est. at 1.0¢ to 1.6¢</dt><dd data-k="range">$7.9k–$12.6k</dd></div>
<div><dt>Your desk, $550 a month</dt><dd>$6,600</dd></div>
<div class="cnet"><dt>Left after the fee, est.</dt><dd data-k="net">+$1.3k to +$6k</dd></div>
</dl>
<div class="cscale"><div class="csh"><span>Fit gate · ~$25K a month on cards</span><b data-k="gatev">You: $35K</b></div><div class="csc gate" id="cgt"><i class="fill"></i><i class="fee"></i></div></div>
<div class="cv" id="cv"><h3 id="cvt">Clears the fee.</h3><p id="cvp"></p><ol id="cvo"></ol></div>
<div class="cbtn"><a class="btn pk" id="cc1" href="book.html">Book your Found Money Call <span class="ar">→</span></a><a class="btn wa" href='"""+WA+"""'>💬 Text Your First Officer</a></div>
<a class="chowl" href="#how">How we got this number ↓</a>
</aside>
</div>
</div></div></section>
"""

def how():
    rows=[('Spend','Your monthly card spend, by line, as typed. Examples are fictional owners.'),
          ('Earn rates','Each line earns the rate shown, today and with your desk, per $1. "Your cards today" swaps your current rate for one flat card.'),
          ('Velocity','Points a month: a year of earning divided by 12, posted monthly like a statement.'),
          ('Timeline','The month your points with your desk first cover a trip, set against when today\'s cards would. Example points prices; no seats are held.'),
          ('Points counted','85% of the extra points. The rest stays out of every estimate.'),
          ('Cents a point','From the table above, by how you use them. Floor is a plain cash out. Estimates, not results from past bookings.'),
          ('Return','Value of the extra points at the middle of the range, divided by the $6,600 a year fee. The range uses the floor and the top.'),
          ('Verdict','Clears the fee when even the floor beats $6,600. Close call when only the top does. Under ~$25K a month on cards, not a fit yet.')]
    return """<section class="cx chow" id="how"><div class="cw"><details open>
<summary><span class="clab cll"><span>Learn · how we got this number</span></span><h2>Every step, <span class="pk">in plain sight.</span></h2></summary>
<dl class="casl">"""+''.join('<div><dt>%s</dt><dd>%s</dd></div>'%r for r in rows)+"""</dl>
<p class="cnote">Points prices move by date and program, so every figure here is an estimate. Your desk checks live prices with you and books only after you approve.</p>
</details></div></section>
<section class="cx ccta"><div class="cw"><div class="cctab">
<div><span class="clab cle"><span>Next · 20 minutes, free</span></span><h2>Bring your statements to <span class="pk">the Found Money Call.</span></h2><p>Your desk runs this on your real numbers. If $550 a month doesn't clear, you'll hear that on the call.</p></div>
<div class="cctb"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn ghost" href="book.html">Book the Found Money Call</a></div>
</div></div></section>
"""

def page():
    h=B.head('Calculator | What is your spend really worth? | First Officer','Put in your monthly card spend and watch it turn into points, trips and a return on the $550 a month desk fee. Estimates only.')
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">\n<link rel="stylesheet" href="recovered/calc.css">')
    h+='<body class="modes calc">\n'+B.nav('Calculator').replace('home-recovered.html','home-modes.html')+B.ticker()+'<main>\n'+hero()+tool()+how()+'</main>\n'
    h+=B.footer().replace('home-recovered.html','home-modes.html').replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.','Every owner shown is a fictional example. All figures are examples and estimates.')
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
