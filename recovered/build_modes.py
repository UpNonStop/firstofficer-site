import re
# Builds home-modes.html at the repo root: landing mockup with the iPhone modes hero and 10 rotating example owners.
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import build as B
ROOT=B.ROOT
LOGOS=[1,2,17,12,47,25,9,18]
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
<div class="msb"><span>9:41</span><span class="isl"></span><span class="sig"><svg width="16" height="10" viewBox="0 0 17 11"><rect x="0" y="7" width="3" height="4" rx="1"/><rect x="4.5" y="5" width="3" height="6" rx="1"/><rect x="9" y="2.5" width="3" height="8.5" rx="1"/><rect x="13.5" y="0" width="3" height="11" rx="1"/></svg><u></u></span></div>
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
<div class="mmodes" role="group" aria-label="Try the different modes">
<div class="mmh"><b>Try the different modes</b><span data-k="mline">More points from the same spend</span></div>
<div class="mchips"><button data-t="earn">Earn</button><button data-t="burn">Burn</button><button data-t="return">Return</button><button data-t="learn">Learn</button></div>
</div>
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
<p class="msub">Every loyalty program has a team constantly rewriting the rules. While you run your business, your spend earns less than it should, and your points buy less than they could. Your desk of specialists fixes that.</p>
<p class="mtag">Your spend, working harder.<br>Your points, going further.</p>
<div class="mctas" id="mctas"><a class="btn pk" href="book.html">Get your desk <span class="ar">→</span></a><a class="btn ghost" href="#how">See how it works</a></div>
<div class="mlogos">{logos}<span>Every program. One desk.</span></div>
</div>
</div></section>
'''
NAMES={1:'Amex',2:'Chase',17:'United',12:'Hyatt',47:'Virgin Atlantic',25:'Aeroplan',9:'Marriott',18:'Delta'}
SL={1:'amex',2:'chase',17:'united',12:'hyatt',47:'virgin-atlantic',25:'aeroplan',9:'marriott',18:'delta'}
def B_slug(n): return SL[n]

def how():
    P=[('01','Earn','More points from the spend you already have.','Your desk matches every line of spend to the card that earns most on it.','earn'),
       ('02','Burn','Better trips for the points you earn.','Your desk vets every requirement with you, then books after you approve.','burn'),
       ('03','Return','Money found, every Friday.','Counted in dollars and checked against your statements.','return'),
       ('04','Learn','Know what your points are worth.','One short lesson a week, built from your own data.','learn')]
    cards=''.join(f'<div class="pc4 reveal d{i}"><div class="pn"><b>{n}</b>{t}</div><h3>{h}</h3><p>{p}</p><div class="pm" data-k="h-{k}"></div></div>' for i,(n,t,h,p,k) in enumerate(P))
    return f'''<section class="sec mhow" id="how"><div class="wrap">
<div class="reveal"><span class="kick">How your desk works</span><h2 class="h2">Fix your Earn. <span class="brush">Everything else follows.</span></h2>
<p class="lede">Your desk starts where the money is: what your spend earns. That feeds better trips, money found every Friday, and a little learning along the way. Every move is your call.</p></div>
<div class="p4">{cards}</div>
<p class="p4f" data-k="h-label"></p>
</div></section>
'''

def win():
    return '''<section class="sec mwinsec" id="win"><div class="wrap">
<div class="reveal"><span class="kick">The win</span><h2 class="h2">When money lands, <span class="brush">your app cheers.</span></h2>
<p class="lede">Found money, a month ahead of flat cash back, a points milestone. Each one gets its moment, every week.</p></div>
<div class="win3">
<div class="wcards">'''+B.scorecard()+'''</div>
<div class="reveal d1 celcol">'''+B.celphone(B.cs_found(' on')+B.cs_ahead()+B.cs_goal())+'''<div class="celnav"><button>Found money</button><button>Ahead</button><button>Milestone</button></div></div>
<div class="wcards">'''+B.versus()+B.share()+'''</div>
</div>
<p class="p4f">Example: Leo, Linden Row Insurance. Fictional. Figures are estimates.</p>
</div></section>
<section class="sec tight"><div class="wrap"><div class="why">
<div class="reveal"><b>$550</b><span>Flat monthly, whatever your spend. Cancel anytime.</span></div>
<div class="reveal d1"><b>20 min</b><span>Your Found Money Call, free.</span></div>
<div class="reveal d2"><b>Friday</b><span>Your scorecard. One number, in dollars.</span></div>
<div class="reveal d3"><b>Yours</b><span>Every move is your call. The desk books after you approve.</span></div>
</div></div></section>
'''

SIG='<svg class="nsvg" viewBox="0 0 200 84" role="img" aria-label="Ohad"><title>Ohad</title><g transform="skewX(-12) translate(14 0)" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path stroke-width="2.7" d="M40 22 C24 22 12 40 14 54 C16 68 32 70 44 58 C56 46 58 26 48 20 C42 16 34 20 32 26"/><path stroke-width="2.3" d="M46 52 C56 46 66 34 72 20 C76 10 76 4 72 5 C68 6 66 18 64 32 C62 46 61 58 61 66 C63 56 68 48 74 46 C80 44 82 50 81 58 C81 63 83 66 87 64"/><path stroke-width="2.2" d="M101 50 C95 44 86 48 86 57 C86 65 94 66 99 58 C101 54 102 50 102 48 C101 56 101 63 105 65 C108 66 112 62 115 58"/><path stroke-width="2.1" d="M131 50 C125 44 116 48 116 57 C116 65 124 66 129 58 C134 48 138 28 142 10 C144 4 141 4 139 12 C135 30 133 50 135 62 C136 67 141 66 146 60"/><path stroke-width="1.5" d="M16 78 C58 72 108 70 148 72 C164 73 176 70 186 64"/></g></svg>'
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
    s=''.join(out)
    # this pen's capital I reads like a slash; borrow a plainer hand for that one letter
    return re.sub(r'(>|\s)I(?=[\s\'.,f<])',lambda m:m.group(1)+'<b class="nI">I</b>',s)
def note():
    P=["Honestly? You might not need us.",
       "Everything I've learned, tested and dug up about points and miles is on this site, free. Read it, use it, keep it.",
       "But if you'd rather have my team and me in your corner, doing the work and getting you there faster, we've priced it for owners like you: $550 a month, flat.",
       "Our promise is simple: make programs that look complicated feel easy.",
       '<a href="calculator.html">Run your numbers in the calculator</a> today. If we\'re not a fit, it\'ll tell you, and so will I.']
    body=''.join('<p%s>%s</p>\n'%(' class="nlead"' if i==0 else '',_jit(t,i*97+11)) for i,t in enumerate(P))
    return ('<section class="mnote" id="note" aria-label="Note from Ohad"><div class="wrap">\n<div class="ncard reveal">\n'
      '<span class="nlab">Note from Ohad</span>\n<div class="nbody">\n'+body+
      '<p class="nsig"><span class="ndash">—</span> '+SIG+'</p>\n</div></div>\n</div></section>\n')

def page():
    h=B.head('First Officer | You are not bad at Points & Miles','First Officer by UpNonStop: your rewards desk. Earn, Burn, Return, Learn.')
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nothing+You+Could+Do&family=Over+the+Rainbow&display=swap">\n<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">')
    h+='<body class="modes">\n'+B.nav('').replace('home-recovered.html','home-modes.html').replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')+B.ticker()+'<main>\n'+hero()+note()+how()+win()+B.cta()+'</main>\n'
    h+=B.footer().replace('home-recovered.html','home-modes.html').replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.','Every owner shown is a fictional example. All figures are examples and estimates.')
    h+='<script>window.FO_A="'+B.ASSET+'";</script>\n<script src="recovered/rec.js"></script>\n<script src="recovered/fo-modes-data.js"></script>\n<script src="recovered/modes.js"></script>\n</body>\n</html>\n'
    h=h.replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')
    h=re.sub(r'<div class="mcta">.*?</a></div>\n?','',h,flags=re.S)
    return B.absol(h)
open(os.path.join(ROOT,'home-modes.html'),'w').write(page())
print('built home-modes.html')
