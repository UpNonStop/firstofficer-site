import re
# Builds home-modes.html at the repo root: landing mockup with the iPhone modes hero and 10 rotating example owners.
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build as B
ROOT=B.ROOT
LOGOS=[1,12,2,17,47,18,25,9]  # by colour: blues, reds, then dark
def hero():
    logos=''.join(f'<img src="img/hero/prog/{n:02d}-{B_slug(n)}.jpg" alt="{NAMES[n]}">' for n in LOGOS)
    return f'''<section class="mh" id="mh"><div class="mbg" aria-hidden="true"></div>
<div class="mwrap">
<div class="mtop">
<span class="mpill"><i></i>Earn · Burn · Return · Learn</span>
<h1>You are not bad at Points &amp; Miles. You are just <span class="pk">outnumbered.</span></h1>
<ul class="mprob" aria-label="The problem">
<li><b>×</b><span>Your biggest spend earns <strong data-k="fromx">1.2x</strong>.</span></li>
<li><b>×</b><span>Your points sit while the rules change.</span></li>
<li class="m3"><b>×</b><span>Your credits lapse before anyone looks.</span></li>
</ul>
</div>
<div class="mstage">
<div class="mphone p-earn" id="mphone"><div class="mscr">
<div class="msb"><span class="mclk" data-k="clock">9:41</span><span class="isl"></span><span class="sig"><svg width="16" height="10" viewBox="0 0 17 11"><rect x="0" y="7" width="3" height="4" rx="1"/><rect x="4.5" y="5" width="3" height="6" rx="1"/><rect x="9" y="2.5" width="3" height="8.5" rx="1"/><rect x="13.5" y="0" width="3" height="11" rx="1"/></svg><u></u></span></div>
<div class="mah"><img src="img/rec/chev.png" alt=""><b>First Officer</b><span>Example</span></div>
<div class="mgr"><small data-k="greet">Good evening, Leo</small><h4 data-k="title">Linden Row's Earn</h4></div>
<div class="mpanes"><div class="mpane" data-t="earn"></div><div class="mpane" data-t="burn"></div><div class="mpane" data-t="return"></div><div class="mpane" data-t="learn"></div></div>
<nav class="mtb" aria-label="App tabs">
<button data-t="earn"><svg viewBox="0 0 24 24"><path d="M4 17l5-5 4 4 7-8"/><path d="M15 8h5v5"/></svg>Earn</button>
<button data-t="burn"><svg viewBox="0 0 24 24"><path d="M3 14l18-7-6 13-3-6-9 0z"/></svg>Burn</button>
<button data-t="return"><svg viewBox="0 0 24 24"><path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/></svg>Return</button>
<button data-t="learn"><svg viewBox="0 0 24 24"><path d="M3 5h7a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2H3z"/><path d="M21 5h-7a2 2 0 0 0-2 2v13a2 2 0 0 1 2-2h7z"/></svg>Learn</button>
</nav><div class="mhome"></div>
</div></div>
<div class="mstk" aria-hidden="true"><svg class="mstka" viewBox="0 0 70 34"><path d="M67 4 C46 3 22 10 6 27"/><path d="M9.2 15.4 L6 27 L17.4 23.1"/></svg><span>Tap the tabs.<br>Try each mode.</span></div>
<p class="mcap">Tap a tab to try each mode.</p>
</div>
<div class="mwin">
<div class="wp"><span class="wk">Your spend today</span><b class="wbig" data-k="spend">$420k</b><small data-k="spendsub">a year on cards, earning 1.2x</small>
<ul class="wl" data-k="cats"></ul></div>
<div class="ww"><span class="wk">What your desk finds, est.</span><small class="wlab">Points a year</small>
<div class="wnum"><span data-k="before">504k</span><i>→</i><b data-k="after">1.43M</b></div>
<div class="wbars"><div><span>Today</span><u><i data-k="barb"></i></u></div><div><span>With your desk</span><u><i class="wg" data-k="bara"></i></u></div></div>
<div class="wtrip"><span data-k="tripimg"></span><div><small>Your points, going further</small><b data-k="trip">Tokyo in business for 2</b><em data-k="trippct">32% there, est.</em></div></div></div>
<p class="wfine"><span data-k="label">Example: Leo, Linden Row Insurance, Columbus, OH. Fictional. Figures are estimates.</span> <button class="wnext" type="button">Next example →</button></p>
</div>
<div class="mrest">
<p class="mlab"><span data-k="label">Example: Leo, Linden Row Insurance, Columbus, OH. Fictional. Figures are estimates.</span> <button class="wnext" type="button">Next example →</button></p>
<p class="msub">Every loyalty program has a team constantly rewriting the rules. While you run your business, your spend earns less than it should, and your points buy less than they could. Your desk of specialists works on that with you.</p>
<p class="mtag">Your spend, working harder.<br>Your points, going further.</p>
<div class="mctas" id="mctas"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn wa" href="https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call">💬 Text Your First Officer</a></div>
<a class="mcalc" href="calculator.html">or run the calculator <span class="ar">→</span></a>
<div class="mlogos">{logos}<span>Every loyalty program. One desk to rule them all.</span></div>
<p class="mtm">Program names and logos belong to their owners. No affiliation implied.</p>
</div>
</div></section>
'''
NAMES={1:'Amex',2:'Chase',17:'United',12:'Hyatt',47:'Virgin Atlantic',25:'Aeroplan',9:'Marriott',18:'Delta'}
SL={1:'amex',2:'chase',17:'united',12:'hyatt',47:'virgin-atlantic',25:'aeroplan',9:'marriott',18:'delta'}
def B_slug(n): return SL[n]

PC={'earn':'#12834E','burn':'#E8590C','return':'#7149C9','learn':'#1E78B8'}
def how():
    P=[('01','Earn','More points from the spend you already have.','Your desk matches every line of your spend to the card that earns most on it.','earn'),
       ('02','Burn','Better trips for the points you earn.','Your desk vets every requirement with you, then books after you approve.','burn'),
       ('03','Return','Money found, every Friday.','Counted in dollars and checked against your statements.','return'),
       ('04','Learn','Know what your points are worth.','One short lesson a week, built from your own data.','learn')]
    cards=''.join(f'<div class="pc4 k-{k} reveal d{i}"><div class="pn"><b>{n}</b>{t}</div><h3>{h}</h3><p>{p}</p><div class="pm" data-k="h-{k}"></div></div>' for i,(n,t,h,p,k) in enumerate(P))
    return f'''<section class="sec mhow" id="how"><div class="wrap">
<div class="mpay reveal"><p class="mlead">Now, let me explain what we do.</p><h2 class="mpayh">You run the business. <span class="pk">The desk runs the points.</span></h2></div>
<div class="reveal"><span class="kick">How your desk works</span><h3 class="h2 mpay2">Let First Officer guide you. <span class="brush">The desk takes it from there.</span></h3>
<p class="lede">It starts with Earn: what your spend earns. That feeds Burn, better trips for your points. Then Return, money found every Friday, and Learn, a little knowing along the way. Every move is your call.</p></div>
<div class="p4">{cards}</div>
<p class="p4f" data-k="h-label"></p>
<div class="mcv"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn ghost" href="calculator.html">Run the calculator</a></div>
</div></section>
'''

def win():
    return '''<section class="sec mwinsec" id="win"><div class="wrap">
<div class="reveal"><span class="kick">The win</span><h2 class="h2">When money lands, <span class="brush">your app cheers.</span></h2>
<p class="lede">Found money, a month ahead of flat cash back, a points milestone. Each one gets its moment, every week.</p></div>
<div class="win3">
<div class="wcards">'''+B.scorecard()+'''</div>
<div class="reveal d1 celcol">'''+B.celphone(B.cs_found(' on')+B.cs_ahead()+B.cs_goal())+'''<div class="celnav"><button>Found money</button><button>Ahead</button><button>Milestone</button></div></div>
<div class="wcards">'''+B.versus()+B.share().replace(' style="background:rgba(255,255,255,.2);color:#fff"','')+'''</div>
</div>
<p class="p4f">Example: Leo, Linden Row Insurance. Fictional. Figures are estimates.</p>
</div></section>
<section class="sec tight"><div class="wrap"><div class="why">
<div class="reveal"><b>$550</b><span>Flat monthly, whatever your spend.</span></div>
<div class="reveal d1"><b>20 min</b><span>Your Found Money Call, free.</span></div>
<div class="reveal d2"><b>Friday</b><span>Your scorecard. One number, in dollars.</span></div>
<div class="reveal d3"><b>Yours</b><span>Every move is your call. The desk books after you approve.</span></div>
</div></div></section>
'''

import json,subprocess
def personas():
    return json.loads(subprocess.check_output(['node','-e',"global.window={};require(process.argv[1]);process.stdout.write(JSON.stringify(window.FO_MODES))",os.path.join(os.path.dirname(os.path.abspath(__file__)),'fo-modes-data.js')]))
def _x(n): return ('%.1f'%n).rstrip('0').rstrip('.')+'x'
def _usd(n): return '${:,}'.format(int(round(n)))
def _pts(n):
    return (('%.2f'%(n/1e6)).rstrip('0').rstrip('.')+'M') if n>=1e6 else ('%dk'%round(n/1e3))
def pcard(p,k):
    who=f"{p['first']}, {p['biz']}".replace('&','&amp;')
    if k=='earn': v,sub=_x(p['to']),f"per $1 on your spend, up from {_x(p['from'])}"
    elif k=='burn': v,sub=f"{p['pct']}%",f"of the way to {p['trip'][0].lower()+p['trip'][1:] if p['trip'].split()[0] in ('Team','A') else p['trip']}"
    elif k=='return': v,sub=_usd(sum(r[1] for r in p['ret'])),f"found in one Friday, from {p['ret'][0][0][0].lower()+p['ret'][0][0][1:]} and more"
    else: v,sub=p['learn'][1],re.sub(r',? est\.$','',p['learn'][2])
    v=v.replace('<','&lt;');lab=k.capitalize()
    return f'<div class="pf k-{k}"><div class="pft"><b>{lab}</b><span>Example, est.</span></div><div class="pfv">{v}</div><p>{sub}</p><small>{who}</small></div>'
def proof():
    P=personas();K=['earn','burn','return','learn']
    r1=''.join(pcard(P[i],K[i%4]) for i in range(10))
    r2=''.join(pcard(P[(i+5)%10],K[(i+2)%4]) for i in range(10))
    row=lambda c,cls:f'<div class="prow {cls}"><div class="ptrack">{c}<div class="pdup" aria-hidden="true">{c}</div></div></div>'
    return f'''<section class="sec mproof" id="proof"><div class="wrap">
<div class="reveal"><span class="kick">The proof</span><h2 class="h2">Proof in every pillar. <span class="brush">Earn, Burn, Return, Learn.</span></h2>
<p class="lede">What a desk finds for owners like you. Every owner here is a fictional example, and every figure is an estimate.</p></div></div>
<div class="prows" aria-label="Example proofs">{row(r1,'r1')}{row(r2,'r2')}</div>
<div class="wrap"><p class="p4f">Fictional owners. Illustrative mockup figures, est.</p></div>
<div class="wrap"><div class="pcta"><div class="pctx"><b>Get your desk.</b><span>$550 a month, flat. The desk books only after you approve.</span></div><div class="pbtn"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn ghost" href="calculator.html">Run the calculator</a></div></div></div>
</section>
'''

SIG='<svg class="nsvg" viewBox="0 0 200 84" width="171" height="72" role="img" aria-label="Ohad"><title>Ohad</title><g transform="skewX(-12) translate(14 0)" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path stroke-width="2.7" d="M40 22 C24 22 12 40 14 54 C16 68 32 70 44 58 C56 46 58 26 48 20 C42 16 34 20 32 26"/><path stroke-width="2.3" d="M46 52 C56 46 66 34 72 20 C76 10 76 4 72 5 C68 6 66 18 64 32 C62 46 61 58 61 66 C63 56 68 48 74 46 C80 44 82 50 81 58 C81 63 83 66 87 64"/><path stroke-width="2.2" d="M101 50 C95 44 86 48 86 57 C86 65 94 66 99 58 C101 54 102 50 102 48 C101 56 101 63 105 65 C108 66 112 62 115 58"/><path stroke-width="2.1" d="M131 50 C125 44 116 48 116 57 C116 65 124 66 129 58 C134 48 138 28 142 10 C144 4 141 4 139 12 C135 30 133 50 135 62 C136 67 141 66 146 60"/><path stroke-width="1.5" d="M16 78 C58 72 108 70 148 72 C164 73 176 70 186 64"/></g></svg>'
def _jit(html,seed):
    """wrap each word in a span with a small, repeatable rotation and baseline shift, like a real pen line"""
    k=[seed]
    def r():
        k[0]=(k[0]*1103515245+12345)%2147483648; return k[0]/2147483648
    def wrap(t):
        out=[]
        for w in t.split(' '):
            if not w: out.append(w);continue
            out.append('<span style="--r:%.2fdeg;--y:%.1fpx">%s</span>'%((r()-.5)*1.6,(r()-.5)*2.2,w))
        return ' '.join(out)
    parts=re.split(r'(<[^>]+>)',html);out=[];inl=False
    for x in parts:
        if x.startswith('<a'): inl=True;out.append(x);continue
        if x.startswith('</a'): inl=False;out.append(x);continue
        out.append(x if (x.startswith('<') or inl) else wrap(x))
    return ''.join(out)
def note():
    P=["Honestly? You might not need a First Officer to optimize your points &amp; miles.",
       'Everything I\'ve learned, tested and dug up about points and miles is on this site, free. Read it, use it, keep it. I put it all in the <a href="freebies.html">"Freebies"</a> section which I update daily.',
       "But if you'd rather have my team and me in your corner, doing the work and getting you there faster, we've priced it for owners like you: $550 a month, flat.",
       '<mark class="nhl">Our promise is simple: make programs that look complicated feel easy.</mark>',
       '<a href="calculator.html">Run your numbers in the calculator</a> today. If we\'re not a fit, it\'ll tell you, and so will I.']
    body=''.join('<p%s>%s</p>\n'%(' class="nlead"' if i==0 else '',_jit(t,i*97+11)) for i,t in enumerate(P))
    return ('<section class="mnote" id="note" aria-label="Note from Ohad"><div class="wrap">\n<div class="ncard reveal">\n'
      '<span class="nlab">Note from Ohad</span>\n<div class="nbody">\n'+body+
      '<div class="nsig">'+SIG+'<p class="nname">'+_jit('— Ohad Sternberg',7)+'</p><p class="nrole">'+_jit('Founder, UpNonStop',23)+'</p></div>\n</div></div>\n'
      '<div class="ncv"><a class="btn ghost" href="calculator.html">Run the calculator <span class="ar">→</span></a><a class="btn ghost" href="freebies.html">Everything, free from the desk <span class="ar">→</span></a></div>\n</div></section>\n')

NXT='''<section class="sec tight pnx"><div class="wrap"><a class="nxt reveal" href="product-modes.html">
<span class="nxk"><span class="thr" aria-hidden="true"><i class="te"></i><i class="tb"></i><i class="tr"></i><i class="tl"></i></span>Next chapter · 02</span><b class="nxh">Meet Leo. <span class="pk">Watch the desk catch what he missed.</span></b><span class="nxp">One fictional insurance agency, four chapters: the ads on the wrong card, the Tokyo plan, the Friday count, the lesson.</span><span class="nxb">Follow Leo's year <span class="ar">→</span></span></a>
</div></section>
'''
def page():
    h=B.head('First Officer | You are not bad at Points & Miles','First Officer by UpNonStop: your rewards desk. Earn, Burn, Return, Learn.')
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kalam:wght@300;400&display=swap">\n<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">')
    h+='<body class="modes">\n'+B.nav('').replace('home-recovered.html','home-modes.html').replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')+B.ticker()+'<main>\n'+hero()+note()+how()+win()+proof()+NXT+'</main>\n'
    h+=B.footer().replace('home-recovered.html','home-modes.html').replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.','Every owner shown is a fictional example. All figures are examples and estimates.')
    h+='<script>window.FO_A="'+B.ASSET+'";</script>\n<script src="recovered/rec.js"></script>\n<script src="recovered/fo-modes-data.js"></script>\n<script src="recovered/modes.js"></script>\n</body>\n</html>\n'
    h=h.replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')
    h=re.sub(r'<div class="mcta">.*?</a></div>\n?','',h,flags=re.S)
    h=h.replace('<a class="btn pk" href="https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call">💬 Text Your First Officer</a>\n<button class="burger"','<span class="nbtns"><a class="btn pk" href="book.html">Get your desk</a><a class="btn wa" href="https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call">💬 Text Your First Officer</a></span>\n<button class="burger"',1)
    h=h.replace('<a class="btn pk" href="https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call">💬 Text Your First Officer</a>\n</div>','<a class="btn wa" href="https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call">💬 Text Your First Officer</a>\n</div>',1)
    assert h.count('class="btn wa"')==3
    h=h.replace('href="calculator.html"','href="calculator-modes.html"')
    for a,b in [('product-recovered.html','product-modes.html'),('pricing.html','pricing-modes.html'),('freebies.html','freebies-modes.html'),('about.html','about-modes.html'),('trust.html','trust-modes.html'),('industries.html','industries-modes.html'),('book.html','book-modes.html')]: h=h.replace('href="'+a,'href="'+b)
    return B.absol(h)
if __name__=='__main__':
    open(os.path.join(ROOT,'home-modes.html'),'w').write(page())
    print('built home-modes.html')
