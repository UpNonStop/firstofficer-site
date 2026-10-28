# Builds calculator-modes.html at the repo root: a standalone, editorial ROI calculator.
# No app screens. Site chrome (nav, 32px ticker, footer) identical to home-modes. Mockup only.
import os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import build as B

WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call'

PH='https://cdn.jsdelivr.net/gh/UpNonStop/firstofficer-site@696503d9ba166267a9a219c98b98bcf4c09d74c1/'

def hero():
    return """<section class="ch" id="top"><div class="cw chg">
<div class="cht">
<span class="mpill"><i></i>The calculator · est.</span>
<h1>Every loyalty program is built to confuse you. Here's what your spend is <span class="pk">really worth.</span></h1>
<p class="clede">One number in, one answer out: what your desk finds each month against its $550 fee. Want every line? Go advanced.</p>
<p class="cfl"><span>$550 a month, flat</span><span>Fit from ~$25K a month on cards</span><span>Found Money Call · 20 min, free</span></p>
</div>
<figure class="chph"><img class="a" src="""+'"'+PH+"""rebuild-v2/img/ph/e-laptop.webp" alt="A business owner working at a laptop at a bright desk" width="1600" height="1066" fetchpriority="high"><img class="b" src="""+'"'+PH+"""rebuild-v2/img/ph/e-arrive.webp" alt="Two travellers arriving in a hotel lobby with their luggage" width="1600" height="1066"></figure>
</div></section>
"""

def bal(id_):
    return """<div class="cbal" id="""+'"'+id_+'"'+""" role="img" aria-label="Monthly value found against the $550 fee">
<div class="cbt"><i class="base"></i><i class="over"></i><i class="short"></i><i class="rng"></i><i class="mark"><span>$550 fee</span></i></div>
<div class="cbx"><span>$0</span><span data-k="bmax">$1,650</span></div>
</div>"""

def tier(id_):
    return '<figure class="ctier" id="'+id_+'"><div class="ctp"></div><figcaption><b data-k="tier">Pays for itself</b><span data-k="tierx">Return 1.5×, est.</span></figcaption></figure>'

def mini():
    return """<div class="cmini" aria-hidden="true"><div><small>Desk finds, a month</small><b data-k="m-find">~$850</b></div><div><small>Fee</small><b>$550</b></div><div><small>Return</small><b class="rx" data-k="m-rx">1.5×</b></div></div>"""

def basic():
    return """<div class="cbas" id="bas" role="tabpanel" aria-labelledby="tb-b">
<div class="bq">
<label class="bql" for="bv">What do you put on cards each month?</label>
<div class="bin"><span>$</span><input id="bv" type="text" inputmode="numeric" autocomplete="off" value="35,000" aria-label="Card spend, dollars a month"><small>a month</small></div>
<div class="bsw"><input id="bs" class="bsl" type="range" min="0" max="100000" step="500" value="35000" aria-label="Card spend a month, slider"><i class="bgt" style="left:25%"><span>~$25K fit</span></i></div>
<div class="bsx"><span>$0</span><span>$50K</span><span>$100K+</span></div>
<p class="bmin" aria-hidden="true">Your desk finds <b data-k="find">~$850</b> a month, est. · Return <b data-k="rx">1.5×</b></p>
<div class="bact"><button type="button" class="brun" id="brun" aria-pressed="false"><i></i><span>Watch it run</span></button><small>$10K to $80K, once. Touch anything to stop.</small></div>
<p class="bbl">Blended rate, est.: ~1.2 points per $1 on your cards today, ~3.4 with your desk.</p>
</div>
<div class="ba" aria-live="polite">
<small class="bal">Your desk finds</small>
<b class="bfind" data-k="find">~$850</b>
<span class="bsub">a month, est. <em data-k="findr">$650–$1,050</em></span>
<div class="bvs"><span>vs</span><b>$550</b><span>a month, flat</span></div>
<dl class="bk"><div class="ret"><dt>Return of</dt><dd data-k="rx">1.5×</dd></div><div><dt>Left each month</dt><dd data-k="net">+$300</dd></div></dl>
<p class="bverd" id="bv1"><b id="bvt">Clears the fee.</b> <span id="bvp"></span></p>
</div>
"""+tier('btier')+"""
<div class="bbar">"""+bal('bbal')+"""</div>
<div class="bgo"><button type="button" class="bgob" id="bgo">Go advanced <span>· your lines, your cards, how you'll use the points</span> <i>→</i></button><a class="btn pk" id="bc1" href="book.html">Book your Found Money Call <span class="ar">→</span></a></div>
</div>
"""

def advanced():
    return """<div class="cbox" id="adv" role="tabpanel" aria-labelledby="tb-a" hidden>
<div class="cin">
"""+mini()+"""
<figure class="cind"><div class="cip"></div><figcaption><b id="cinb">Leo</b><span id="cins">Linden Row Insurance · Insurance agency · fictional</span></figcaption></figure>
<div class="clab"><span>Start from an example</span><small id="cwho">Fictional owners</small></div>
<div class="cex" id="cex" role="tablist" aria-label="Start from an example owner"></div>
<div class="clab c2"><span>Your spend by line, a month</span><small>Type or drag</small></div>
<div class="crows" id="crows"></div>
<div class="csum"><div><small>On cards</small><b data-k="mo">$35,000</b><span>a month</span></div><div><small>Earns today</small><b data-k="bl">1.2x</b><span>per $1, est.</span></div><div><small>Points today</small><b data-k="vt">42k</b><span>a month</span></div></div>
<div class="cpick">
<div class="cmix"><span>Your cards today</span><div class="cseg" id="cmix" role="radiogroup" aria-label="Your cards today">
<button type="button" data-m="ex" class="on" role="radio" aria-checked="true">As entered</button><button type="button" data-m="1" role="radio" aria-checked="false">One 1x card</button><button type="button" data-m="1.5" role="radio" aria-checked="false">One 1.5x card</button><button type="button" data-m="2" role="radio" aria-checked="false">2% cash back</button></div></div>
<div class="cuse"><span>How you'll use the points</span><div class="cul" id="cuse" role="radiogroup" aria-label="How you will use the points"></div><p class="cfine">Cents a point, est. Floor is a plain cash out. The top is a level a well-planned booking can reach again and again, not a one-off.</p></div>
</div>
</div>
<aside class="cres" aria-live="polite"><div class="cstk">
"""+tier('atier')+"""
<div class="clab"><span class="rr">Your month, est.</span><small data-k="who">Leo · at 1.0¢–1.6¢ a point</small></div>
<div class="chead">
<div class="cfind"><small>Your desk finds</small><b data-k="find">~$850</b><span>a month, est. <em data-k="findr">$650–$1,050</em></span></div>
<div class="cvs">vs</div>
<div class="cfee"><small>Your desk costs</small><b>$550</b><span>a month, flat</span></div>
</div>
"""+bal('cbal')+"""
<dl class="ckpi">
<div class="net"><dt>Left each month</dt><dd data-k="net">+$300</dd><small data-k="netr">+$100 to +$500, est.</small></div>
<div class="ret"><dt>Return of</dt><dd data-k="rx">1.5×</dd><small data-k="rxr">1.2× to 1.9×, est.</small></div>
<div><dt>Extra points</dt><dd data-k="plus">+77k</dd><small>a month; we count 85%</small></div>
</dl>
<div class="cv" id="cv"><h3 id="cvt">Clears the fee.</h3><p id="cvp"></p></div>
<div class="cet" id="cet" role="table" aria-label="Points a month by line"></div>
<div class="cgate"><div class="csh"><span>Fit gate · ~$25K a month on cards</span><b data-k="gatev">You: $35K</b></div><div class="csc" id="cgt"><i class="fill"></i><i class="fee"></i></div></div>
<div class="cbtn"><a class="btn pk" id="cc1" href="book.html">Book your Found Money Call <span class="ar">→</span></a><a class="btn wa" href='"""+WA+"""'>💬 Text Your First Officer</a></div>
<a class="chowl" href="#how">How we got this number ↓</a>
</div></aside>
</div>
"""

def tool():
    return """<section class="ct" id="calc"><div class="cw">
<div class="cmode" role="tablist" aria-label="Calculator level">
<button type="button" role="tab" id="tb-b" aria-controls="bas" aria-selected="true" class="on" data-m="b"><small>Level 1</small><b>Basic</b><span>10 seconds · one number</span></button>
<button type="button" role="tab" id="tb-a" aria-controls="adv" aria-selected="false" data-m="a"><small>Level 2</small><b>Advanced</b><span>2 minutes · every line</span></button>
</div>
"""+basic()+advanced()+"""</div></section>
"""

def how():
    rows=[('Basic','One number, one blended rate: about 1.2 points per $1 on your cards today and about 3.4 with your desk putting each line on its best card. That is the mix of a service business like the example Leo, so Basic at $35K matches him. Your own lines can earn more or less; Advanced uses the rates of each line.'),
          ('Spend','Basic: your total a month. Advanced: your monthly card spend, by line, as typed. Examples are fictional owners.'),
          ('Earn rates','Advanced: each line earns the rate shown per $1, today and with your desk. "Your cards today" swaps your current rate for one flat card.'),
          ('Extra points','Points a month with your desk, minus points a month today.'),
          ('Points counted','85% of the extra points. The rest stays out of every estimate.'),
          ('Cents a point','Basic uses the mix. Advanced, by how you\'ll use the points: mixed 1.0¢–1.6¢, cash out 1.0¢, economy 1.0¢–1.4¢, top hotels 1.2¢–2.0¢, business class 1.5¢–2.0¢. Floor is a plain cash out. Estimates, not results from past bookings.'),
          ('Found a month','Extra points counted × cents a point, at the middle of the range. The range uses the floor and the top.'),
          ('Return','What your desk finds a month divided by the $550 a month fee.'),
          ('Verdict','Clears the fee when even the floor beats $550 a month. Close call when only the top does. Under ~$25K a month on cards, not a fit yet.')]
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
    h=B.head('Calculator | What is your spend really worth? | First Officer','Put in your monthly card spend and see what your desk finds each month against its $550 a month fee. Estimates only.')
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
