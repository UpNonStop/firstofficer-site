# Builds calculator-modes.html at the repo root: the calculator in the landing's visual language
# (home-modes: rotating hero photos, 32px ticker, the same nav, the same iPhone, proof marquee). Mockup only.
import os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
import build as B
# reuse the landing's own builders (proof marquee) without rebuilding home-modes.html
_src=open(os.path.join(HERE,'build_modes.py')).read()
_w="open(os.path.join(ROOT,'home-modes.html'),'w').write(page())"
assert _w in _src
M={'__file__':os.path.join(HERE,'build_modes.py'),'__name__':'build_modes_lib'}
exec(_src.replace(_w,'').replace("print('built home-modes.html')",''),M)

WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call'
TABS='''<nav class="mtb" aria-label="App tabs">
<button data-t="earn"><svg viewBox="0 0 24 24"><path d="M4 17l5-5 4 4 7-8"/><path d="M15 8h5v5"/></svg>Earn</button>
<button data-t="burn"><svg viewBox="0 0 24 24"><path d="M3 14l18-7-6 13-3-6-9 0z"/></svg>Burn</button>
<button data-t="return"><svg viewBox="0 0 24 24"><path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/></svg>Return</button>
<button data-t="learn"><svg viewBox="0 0 24 24"><path d="M3 5h7a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2H3z"/><path d="M21 5h-7a2 2 0 0 0-2 2v13a2 2 0 0 1 2-2h7z"/></svg>Learn</button>
</nav>'''
PHONE='''<div class="mphone p-earn" id="mphone"><div class="mscr">
<div class="msb"><span class="mclk" data-k="clock">9:41</span><span class="isl"></span><span class="sig"><svg width="16" height="10" viewBox="0 0 17 11"><rect x="0" y="7" width="3" height="4" rx="1"/><rect x="4.5" y="5" width="3" height="6" rx="1"/><rect x="9" y="2.5" width="3" height="8.5" rx="1"/><rect x="13.5" y="0" width="3" height="11" rx="1"/></svg><u></u></span></div>
<div class="mah"><img src="img/rec/chev.png" alt=""><b>First Officer</b><span>Example</span></div>
<div class="mgr"><small data-k="greet">Good evening, Leo</small><h4 data-k="title">Linden Row's Earn</h4></div>
<div class="mpanes"><div class="mpane on" data-t="earn"></div><div class="mpane" data-t="burn"></div><div class="mpane" data-t="return"></div><div class="mpane" data-t="learn"></div></div>
'''+TABS+'''<div class="mhome"></div>
</div></div>'''

def hero():
    return '''<section class="mh qh" id="top"><div class="mbg" aria-hidden="true"></div>
<div class="qw">
<div class="qtop">
<span class="mpill"><i></i>The calculator · est.</span>
<h1>What is your spend <span class="pk">really worth?</span></h1>
<p class="qsub">Every program is built so your spend earns less than it could. Move your numbers. Watch your Earn screen change, and see if $550 a month clears. If it doesn't, you'll hear that too.</p>
</div>
<div class="qpick"><div class="qlab"><span>Start from an example owner</span><small>Fictional</small></div><div class="qtiles" id="qtiles" role="tablist" aria-label="Example owners"></div></div>
<div class="qstage">'''+PHONE+'''<p class="qcap">Your Earn screen, live. Tap the tabs.</p></div>
<div class="qquick" aria-hidden="true"><span class="wk">Points a year, est.</span><small>Today</small><b class="qqt" data-k="today">504k</b><small>With your desk</small><b class="qqd" data-k="desk">1.43M</b><small>Worth, est.</small><b class="qqv" data-k="range">$7.9k–$12.6k</b><span class="qqf" data-k="vshort">Clears the fee</span></div>
<div class="qin" id="calc">
<div class="qlab"><span>Your spend by line, a month</span><small id="qwho"></small></div>
<div class="qblocks" id="qblocks"></div>
</div>
<div class="qmore"><div class="qtot"><div><small>On cards</small><b id="qtot">$35,000</b><span>a month</span></div><div><small>A year</small><b id="qtoty">$420k</b></div><div><small>Earns today</small><b id="qbl">1.2x</b><span>per $1, est.</span></div></div>
<div class="qmix"><span>Your cards today</span><div class="qseg" id="qmix" role="radiogroup" aria-label="Your cards today">
<button type="button" data-m="ex" class="on" role="radio" aria-checked="true">As shown</button><button type="button" data-m="1" role="radio" aria-checked="false">One 1x card</button><button type="button" data-m="1.5" role="radio" aria-checked="false">One 1.5x card</button><button type="button" data-m="2" role="radio" aria-checked="false">2% cash back</button></div></div>
</div>
<aside class="qres" aria-live="polite">
<div class="qr">
<span class="wk">Points a year, est.</span>
<div class="qbig"><div class="qbt"><small>Today</small><b data-k="today">504k</b></div><span class="qar">→</span><div class="qbd"><small>With your desk</small><b data-k="desk">1.43M</b></div></div>
<p class="qplus" data-k="plus">+924k more points a year, est.</p>
<div class="wbars"><div><span>Today</span><u><i id="qbT"></i></u></div><div><span>With your desk</span><u><i class="wg" id="qbD"></i></u></div></div>
<div class="qvs"><div><small>Extra points, worth</small><b data-k="range">$7.9k–$12.6k</b><span>a year, est.</span></div><em>vs</em><div><small>Your desk</small><b>$6,600</b><span>a year · $550 a month</span></div></div>
<div class="qgate"><div class="qgt"><span>Fit gate · ~$25K a month on cards</span><b data-k="gatev">$35K</b></div><div class="qgm"><u><i id="qgf"></i></u><em class="qgk"></em></div></div>
<div class="qv" id="qv"><b id="qvt">Clears the fee.</b><p id="qvp"></p><ul id="qvl"></ul></div>
<div class="qctas" id="qctas"><a class="btn pk" id="qc1" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn wa" href="'''+WA+'''">💬 Text Your First Officer</a></div>
<div class="qsp"></div><p class="qfine">Your Found Money Call is 20 minutes and free. Estimates only: 85% of points used, 1.0¢ to 1.6¢ a point. The call checks it against your real statements.</p>
</div>
</aside>
</div></section>
'''

def below():
    return '''<section class="sec tight qburn" id="burn"><div class="wrap">
<div class="qhd"><div><span class="kick">Burn · what you could do with it</span><h2 class="h2">Your points, <span class="brush">going further.</span></h2></div>
<p class="lede">A year of points with your desk, set against a few example trips. Points prices move by date and program, so every figure is an estimate.</p></div>
<div class="qb4" id="qb4"></div>
<p class="p4f">No seats are held or shown here. When you want a trip, your desk checks the live price with you and books only after you approve.</p>
</div></section>
<section class="sec tight qrl"><div class="wrap"><div class="qrl2">
<div class="pc4 k-return"><div class="pn"><b>03</b>Return</div><h3>Money found, every Friday.</h3><div class="qrv"><b id="qretV">$1,860</b><span>found in one example Friday, est.</span></div><ul class="qrll" id="qretL"></ul></div>
<div class="pc4 k-learn"><div class="pn"><b>04</b>Learn</div><h3 id="qlrnH">What one card point is worth</h3><div class="qrv"><b id="qlrnV">1.6¢</b><span id="qlrnS"></span></div><div class="qlb" id="qlrnB"></div><p class="qlf" id="qlrnF"></p></div>
</div>
<div class="why qwhy">
<div><b>$550</b><span>Flat monthly, whatever your spend. Cancel anytime.</span></div>
<div><b>~$25K</b><span>A month on cards. Below that, we'll tell you it's not a fit.</span></div>
<div><b>85%</b><span>Of your points used. The rest stays out of every estimate.</span></div>
<div><b>1.0–1.6¢</b><span>A point, from cash back to a well-planned trip.</span></div>
</div></div></section>
'''

def page():
    h=B.head('Calculator | What is your spend really worth? | First Officer','Move your numbers and see what your spend earns today, what it could earn with your desk, and whether $550 a month clears. Estimates only.')
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">\n<link rel="stylesheet" href="recovered/calc.css">')
    proof=M['proof']().replace('<a class="btn ghost" href="calculator.html">Run the calculator</a>','<a class="btn wa" href="'+WA+'">💬 Text Your First Officer</a>')
    h+='<body class="modes calc">\n'+B.nav('Calculator').replace('home-recovered.html','home-modes.html')+B.ticker()+'<main>\n'+hero()+below()+proof+'</main>\n'
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
