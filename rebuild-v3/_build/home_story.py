"""Homepage: faithful port of the Claude mobile landing (claude-mobile-landing.png), persona Darnell (fictional).
Only mandatory fixes vs Claude: nav (Product, Pricing, Freebies with pink marker, Calculator, About), violet/lavender -> brand pink/cream,
no 'Client stories are shared with permission', compliance copy (est. labels, no live seats, no AI, 50+ programs).
Run: python3 _build/home_story.py  ->  rebuild-v3/home-story.html + story-map.html"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fosite
from fosite import *

# ---------------- numbers (est., calculator honest formula, planned not realized) ----------------
SPEND=260_000
MIX=[('Ads',58_000,4),('Equipment',52_000,2),('Everything else',50_000,2),('Utilities',34_000,2),('Software',26_000,4),('Gas &amp; travel',22_000,4),('Internet &amp; phone',18_000,3)]
assert sum(v for _,v,_ in MIX)==SPEND
PTS_DESK=sum(v*x for _,v,x in MIX)          # 750,000 (calculator pools: ads/software/gas 4x, internet 3x, rest 2x)
PTS_TODAY=SPEND                              # 1x today
K=lambda n: f'{n/1000:,.0f}k'
print('points', PTS_TODAY, PTS_DESK)

# ---------------- mandatory fixes on the shared chrome (shared fosite.py untouched) ----------------
fosite.TICK_FONT=HERO_FONTS                  # Claude look: DM Serif Display + DM Sans + JetBrains Mono
fosite.DATANOTE=''
_nav=fosite.nav
def nav():
    h=_nav().replace('<a href="how.html">How</a>','')
    import re
    h=re.sub(r'<svg class="fzmk".*?</svg>','',h)       # one bold pink brush marker instead of the thin swipe (CSS below)
    return h
fosite.nav=nav
_foot=fosite.footer
def footer(src):
    h=_foot('book')                                     # Claude ends on the stat grid; no extra end CTA card
    h=h.replace('<p class="dn"></p>','').replace('<a href="how.html">How It Works</a>','')
    return h
fosite.footer=footer

CHEV='img/fo-chevron-transparent-v2.png'
LOGO=lambda n: 'img/hero/prog/'+n+'.jpg'
CTAS='<div class="cl-ctas"><a class="c1" href="book.html?from=home">Get your desk</a><a class="c2" href="product.html">See how it works</a></div>'
def step(n,t,small=''):
    return f'<h2 class="cl-step"><span class="n">{n}</span><span class="t">{t}</span>{f"<small>{small}</small>" if small else ""}</h2>'

# ---------------- hero (Claude copy verbatim; deskk pill: "trained on new data nightly" dropped, no AI) ----------------
subs=[p.strip() for p in HERO_SUB.split('\n\n')]
HERO_TXT=f'''<div class="cl-kick"><i></i>Earn · Burn · Return · Learn</div>
<h1>You are not bad at Points &amp; Miles.<br>You are just <span>outnumbered.</span></h1>
<div class="cl-sub"><p>{subs[0]}</p><p>{subs[1]}</p></div>
<p class="cl-tag">Same spend. More points.<br>Better trips, for fewer points.</p>
<div class="cl-deskk"><i></i><span>First Officer's specialists · 50+ programs, one desk</span></div>
<div class="cl-hcta">{CTAS}</div>'''

# ---------------- step 1: meet Darnell (Claude's dossier card, persona swapped) ----------------
CARD_I='<svg viewBox="0 0 20 14" aria-hidden="true"><rect x=".75" y=".75" width="18.5" height="12.5" rx="2.2" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M1 4.6h18" stroke="currentColor" stroke-width="1.3"/></svg>'
DUMB='<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 8v4M5.5 6.5v7M14.5 6.5v7M17 8v4M5.5 10h9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'
EST='<em class="est">est</em>'
dossier=f'''<div class="cl-card"><div class="who"><span class="av">DW<b>{DUMB}</b></span><div><h3>Darnell</h3><p>Ironwood Strength Club · Chicago, IL</p></div></div>
<div class="strat"><span>Bespoke strategy</span><b>B418D27</b></div>
<div class="dh"><b>Desk dossier</b><span>5 of 50+ tracked</span></div>
<div class="rw"><span class="k">Cards on file</span><div class="v"><span class="chip">{CARD_I}Business points card</span><span class="chip">{CARD_I}Travel points card</span></div></div>
<div class="rw"><span class="k">Card spend</span><div class="v"><b>$260k a year</b> {EST}<small>Equipment, ads, utilities</small></div></div>
<div class="rw"><span class="k">Points a year</span><div class="v"><b>{K(PTS_TODAY)} today</b> <span class="ar">→</span> <span class="pk">{K(PTS_DESK)}</span> {EST}</div></div>
<div class="rw"><span class="k">Next trip</span><div class="v"><b class="blk">Business to Rome for two</b><span class="pk sm">3c+ a point vs the cash fare</span> {EST}</div></div>
<div class="rw"><span class="k">Requests</span><div class="v"><ul class="rq"><li class="on">Rome anniversary trip <em class="tg">on it</em></li><li>Hotel nights on points</li><li>Ads on 4x <em class="tg">new</em></li></ul></div></div>
<p class="fn">Example owner. Fictional details. Figures are estimates.</p></div>'''
s1=f'''<section class="cl-s cl-s1"><div class="cl-w">{step(1,'Meet Darnell')}<div class="cl-cardwrap">{dossier}</div>
<div class="cl-ctawrap">{CTAS}</div></div></section>'''

# ---------------- step 2: his desk (Claude's hex tree, exact grid; Callum's five highlighted spots kept) ----------------
X0,DX,Y0,DY=511,58,88,97.4
GRID=[[(-3,'24-atmos-rewards'),(-1,'07-bank-of-america'),(1,'43-sas'),(3,'45-korean-air')],
 [(-4,'14-wyndham'),(-2,'41-virgin-australia'),(0,'44-air-india'),(2,'29-aer-lingus'),(4,'12-hyatt')],
 [(-5,'05-bilt'),(-3,'28-iberia'),(-1,'06-wells-fargo'),(1,'23-allegiant'),(3,'49-aeromexico'),(5,'37-ana')],
 [(-6,'31-emirates'),(-4,'22-frontier'),(-2,'04-citi'),(0,'36-lifemiles'),(2,'01-amex'),(4,'39-qantas'),(6,'08-u-s-bank')],
 [(-7,'19-american'),(-5,'11-ihg'),(-3,'30-qatar-airways'),(3,'27-british-airways'),(5,'50-jal'),(7,'32-singapore')],
 [(-6,'17-united'),(-4,'10-hilton'),(4,'16-radisson'),(6,'47-virgin-atlantic')],
 [(-7,'26-flying-blue'),(7,'09-marriott')],
 [(-6,'38-eva-air'),(6,'20-southwest')],
 [(-5,'02-chase'),(-3,'33-cathay'),(-1,'42-finnair'),(1,'40-air-new-zealand'),(3,'25-aeroplan'),(5,'34-etihad')],
 [(-4,'46-latam'),(-2,'48-tap-air-portugal'),(2,'18-delta'),(4,'15-choice')],
 [(-3,'03-capital-one'),(-1,'35-turkish'),(1,'21-jetblue'),(3,'13-accor')]]
BIG={'04-citi','01-amex','30-qatar-airways','27-british-airways','10-hilton'}
pos={}
for r,row in enumerate(GRID):
    for c,p in row: pos[p]=(X0+c*DX,Y0+r*DY)
assert len(pos)==50
PK,PK2,GR,GR2='#FA1896','#F9B9DA','#2E9E62','#A6D8BB'
import random, math
def mob_pos():
    W,cx,cy,sx,sy=390,195,0,56,64
    cells=[]
    for row in range(-7,8):
        off=0 if row%2==0 else sx/2
        for k in range(-4,5):
            x=k*sx+off
            if abs(x)>168: continue
            cells.append((x,row*sy))
    hole=[c for c in cells if math.hypot(c[0],c[1])<75]
    rest=[c for c in cells if c not in hole]
    rest.sort(key=lambda c:(math.hypot(c[0],c[1]*.62),c[1],c[0]))
    rest=rest[:50]
    ring=sorted(rest[:12],key=lambda c:math.atan2(c[1],c[0]))
    bigc=[ring[i] for i in (0,2,5,8,10)][:5]
    names=[p for p in pos if p not in BIG]
    rnd=random.Random(3); rnd.shuffle(names)
    out={}; bi=iter(sorted(BIG))
    for c in rest:
        out[next(bi) if c in bigc else names.pop()]=c
    ys=[c[1] for c in rest]; top=min(ys)-40
    H=max(ys)-top+60
    return {p:(x+cx,y-top) for p,(x,y) in out.items()},(cx,-top),H
def desk(P,C,W,H,rs,rb,rc,cls,lab,dotr,dotg,fs):
    rnd=random.Random(7); CX,CY=C; o=[]; defs=[]
    for p,(x,y) in P.items():
        big=p in BIG; r=rb if big else rs; k=p.split('-')[0]; ri=r-(r*.12 if big else r*.07)
        defs.append(f'<clipPath id="{cls}{k}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{ri:.1f}"/></clipPath>')
        iw=ri*2*.86
        cols=[PK2,PK2,PK2] if big else [GR if rnd.random()<.45 else GR2 for _ in range(3)]
        if big: cols[rnd.randrange(3)]=PK
        dots=''.join(f'<circle class="d" cx="{x-dotg+i*dotg:.1f}" cy="{y+r+dotr*2.4:.1f}" r="{dotr}" fill="{cc}"/>' for i,cc in enumerate(cols))
        o.append(f'<g class="sp{" big" if big else ""}" data-k="{p}" data-x="{x-CX:.1f}" data-y="{y-CY:.1f}" data-r="{r}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="bub"/>'
                 f'<image href="{LOGO(p)}" x="{x-iw/2:.1f}" y="{y-iw/2:.1f}" width="{iw:.1f}" height="{iw:.1f}" clip-path="url(#{cls}{k})" preserveAspectRatio="xMidYMid slice"/>{dots}</g>')
    iw=rc*1.15
    fo=(f'<g class="fo" data-r="{rc}"><circle cx="{CX}" cy="{CY}" r="{rc}" class="foc"/>'
        f'<image href="{CHEV}" x="{CX-iw/2:.1f}" y="{CY-iw*.62:.1f}" width="{iw:.1f}" height="{iw*1.25:.1f}" preserveAspectRatio="xMidYMid meet"/></g>'
        f'<text x="{CX}" y="{CY+rc+fs*1.5:.1f}" class="fo1" style="font-size:{fs}px" text-anchor="middle">First Officer</text>'
        f'<text x="{CX}" y="{CY+rc+fs*2.75:.1f}" class="fo2" style="font-size:{fs*.82:.1f}px" text-anchor="middle">at the desk</text>' if lab else '')
    return (f'<svg class="cl-desk {cls}" data-lh="{fs*3 if lab else 0:.0f}" viewBox="0 0 {W} {H:.0f}" role="img" aria-label="Darnell\'s desk: First Officer in the centre, surrounded by specialists across 50+ programs. Each one thinks, then takes its turn at the desk.">'
            f'<defs>{"".join(defs)}</defs>{"".join(o)}{fo}</svg>')
desk_d=desk(pos,(511,560),1028,1110,38,46,47,'dkd',1,6,20,36)
MP,MC,MH=mob_pos()
desk_m=desk(MP,MC,390,MH,22,25,28,'dkm',1,3.2,9.5,15).replace('data-lh="45"','data-lh="54"')
desk_svg='<div class="dqw">'+desk_d+desk_m+'<div class="dq-q" aria-hidden="true"></div><div class="dq-a" aria-hidden="true"></div></div>'
FIVE='<div class="cl-five"><span class="h">Working Darnell&#39;s five</span>'+''.join(f'<span class="c">{n}</span>' for n in ['Citi','Amex','Qatar Airways','British Airways','Hilton'])+'</div>'
s2=f'''<section class="cl-s cl-s2"><div class="cl-w">{step(2,'His desk','50+ programs, one desk')}{desk_svg}<p class="cl-dcap">Every specialist keeps thinking. One at a time, each takes its turn at the desk, then steps back.</p>{FIVE}</div></section>'''

# ---------------- step 3: what Darnell sees in the app (Claude's phone and thread, verbatim) ----------------
TH=[('o','Rome in May, for our anniversary?\nBusiness if the points stretch.'),
    ('f','They stretch.\nBusiness via London, for two.'),
    ('f','Hotel on Hilton points too.\nFive nights.'),
    ('o','Love it.\nWhat do you need?'),
    ('f','Rough dates, please.\nWe vet it, then the desk books it.')]
def bub(i,w,t):
    ps=''.join(f'<span>{x}</span>' for x in t.split('\n'))
    av=f'<img class="av" src="{CHEV}" alt="">' if w=='f' else ''
    lab='<div class="who">First Officer</div>' if w=='f' else ''
    last=' last' if i==len(TH)-1 else ''
    rd='<div class="rd">Read 9:41 PM</div>' if i==3 else ''
    return f'{lab}<div class="mm {w}{last}">{av}<div class="b">{ps}</div></div>{rd}'
TABI={'Home':'<path d="M3 9.5 10 4l7 5.5V16a1 1 0 0 1-1 1h-3.5v-4.5h-5V17H4a1 1 0 0 1-1-1z"/>',
      'Earn':'<rect x="3" y="3" width="14" height="14" rx="4"/><path d="M10 13.5v-7M7 9.3 10 6.3l3 3"/>',
      'Burn':'<path d="M10 2.5c.9 0 1.4.8 1.4 1.8v3.6l5.6 3.3v1.6l-5.6-1.6v3.3l1.6 1.2v1.3L10 16.2l-3 .8v-1.3l1.6-1.2v-3.3L3 12.8v-1.6l5.6-3.3V4.3c0-1 .5-1.8 1.4-1.8z"/>',
      'Return':'<path d="M3 13a7 7 0 0 1 14 0z"/><path d="M10 13l3-4"/>',
      'Learn':'<path d="M3 4.5c2.6-.6 5-.3 7 1.2 2-1.5 4.4-1.8 7-1.2v11c-2.6-.6-5-.3-7 1.2-2-1.5-4.4-1.8-7-1.2zM10 5.7v11"/>'}
tabs=''.join(f'<span class="{("on" if n=="Return" else "")}"><svg viewBox="0 0 20 20" aria-hidden="true">{p}</svg>{n}</span>' for n,p in TABI.items())
mapcard=f'''<div class="mc"><div class="ph" style="background-image:url(img/ph/d-rome.webp)"><span class="pin"></span><em>Award space not guaranteed</em></div>
<div class="tx"><b>Business to Rome for two</b><span>Via London, value per point checked. About 3c+ a point vs the cash fare {EST}</span><small>Example · fictional</small></div></div>'''
phone=f'''<div class="cl-phwrap"><div class="cl-ph" role="img" aria-label="Example chat in the First Officer app between Darnell and First Officer about a Rome anniversary trip, fictional">
<div class="scr"><div class="isl"></div><div class="sb"><b>9:41</b><span class="ic"><svg viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx=".7"/><rect x="5" y="5.5" width="3" height="6.5" rx=".7"/><rect x="10" y="3" width="3" height="9" rx=".7"/><rect x="15" y="0" width="3" height="12" rx=".7"/></svg><svg viewBox="0 0 16 12"><path d="M8 11.5 5.6 8.9a3.4 3.4 0 0 1 4.8 0zM3.4 6.6a6.6 6.6 0 0 1 9.2 0l-1.3 1.3a4.8 4.8 0 0 0-6.6 0zM1.2 4.4a9.7 9.7 0 0 1 13.6 0l-1.3 1.3a7.9 7.9 0 0 0-11 0z"/></svg><i class="bat"><i></i></i></span></div>
<div class="tb"><span class="bg"><i></i><i></i><i></i></span><span class="ttl"><img src="{CHEV}" alt=""><b>First Officer</b></span><span class="me">DW</span></div>
<div class="seg"><span class="on">First Officer</span><span>Your plan</span></div>
<div class="th"><div class="in">{mapcard}{''.join(bub(i,w,t) for i,(w,t) in enumerate(TH))}</div></div>
<div class="tabs">{tabs}</div><div class="hb"></div></div></div></div>'''
MICRO='Illustrative example. Owners and chats are fictional. Figures are estimates, not guarantees. Not affiliated with any bank, airline or hotel program. <a href="disclaimer.html">Important information</a>'
TMK='Program names and logos are trademarks of their respective owners, shown for identification only. No endorsement is implied. Award availability, pricing and transfer terms are set by each program and can change without notice.'
s3=f'''<section class="cl-s cl-s3"><div class="cl-w"><div class="cl-s3h">{step(3,'What Darnell sees','in the app')}</div>{phone}
{CTAS}<p class="cl-micro">{MICRO}</p><p class="cl-tmk">{TMK}</p></div></section>'''
STATS=[('$550','Flat monthly · Cancel anytime',' pk'),('20 min','The Found Money Call, free · We size your capture first',''),
       ('Friday','Dollars saved reported every Friday',''),('Yours','Every decision, always','')]
s4='<section class="cl-stats"><div class="cl-w"><div class="g">'+''.join(f'<div><b class="{c.strip()}">{a}</b><span>{b}</span></div>' for a,b,c in STATS)+'</div></div></section>'

# ---------------- desktop band: the same app, "Your plan" tab (customer-facing, no operator view) ----------------
ADS=dict((n,(v,x)) for n,v,x in MIX)['Ads']
PLAN=[('Earn','Ads on the 4x card',f'+{K(ADS[0]*(ADS[1]-1))} points a year {EST}'),
      ('Burn','Rome for two, business','We vet the award rules, then the desk books it'),
      ('Return','Your Friday report','Dollars saved, every Friday'),
      ('Learn','Two-minute note','How transfer partners work')]
plan_in=('<div class="pl"><div class="plh"><b>Darnell\'s plan</b><span>This week</span></div>'+
  ''.join(f'<div class="pr"><span class="pt">{a}</span><div><b>{b}</b><small>{c}</small></div></div>' for a,b,c in PLAN)+
  f'<div class="pp"><span>Points a year</span><b>{K(PTS_TODAY)} <i>→</i> {K(PTS_DESK)}</b> {EST}</div><small class="fx">Example · fictional</small></div>')
i0=phone.index('<div class="th">'); i1=phone.index('<div class="tabs">')
plan_phone=(phone[:i0]+f'<div class="th pl-th">{plan_in}</div>'+phone[i1:]).replace(
  '<span class="on">First Officer</span><span>Your plan</span>','<span>First Officer</span><span class="on">Your plan</span>').replace(
  'cl-phwrap','cl-phwrap plw').replace('Example chat in the First Officer app between Darnell and First Officer about a Rome anniversary trip, fictional',
  "Example of Darnell's plan in the First Officer app, fictional")

# ---------------- brush marker for Freebies (one bold brush, from desk_clean) ----------------
from urllib.parse import quote
def _svg(vb,d,c,tf):
    s=f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='{vb}' preserveAspectRatio='none'><path d='{d}' fill='{c}' transform='{tf}'/></svg>"
    return 'url("data:image/svg+xml,'+quote(s,safe=" =:/',.-()")+'")'
BL="M40 6 L24 6.6 C18 7 15 8.6 13 11.5 C11 15 10 19 8.5 23 C6.5 29 4.5 35 2.5 41 C1.2 45.5 2.5 49.5 7 51 C15 52.3 28 52 40 52Z"
BM="M0 6 C25 4.8 50 5.4 75 3.9 C86 3.3 94 3.1 100 3 L100 49 C82 49.8 64 49.2 45 50.6 C28 51.6 14 51.8 0 52Z"
BR="M0 3 L22 2.6 C29 2.5 34 3.4 36.5 5.8 C38.5 8.2 36 10.5 38.8 12.8 L33.5 15.6 C37 18.3 39 21.5 36.8 24.6 L31 26.6 C34.5 29.6 35.2 33.6 32.2 37.6 C28.4 42.4 22 46 14 48 C8 48.9 4 49 0 49Z"
def brush(c='#FA1896',cap='.7em'):
    tf='translate(0 2) scale(1 1)'
    return (f"{_svg('0 0 40 56',BL,c,tf)} left center/{cap} 100% no-repeat,{_svg('0 0 40 56',BR,c,tf)} right center/{cap} 100% no-repeat,"
            f"{_svg('0 0 100 56',BM,c,tf)} center/calc(100% - 2*{cap} + 2px) 100% no-repeat")
BRUSH=brush()

CSS='''<style>
.fz>span{background:%(BRUSH)s;color:#fff!important;padding:.16em .42em .18em;margin:0 -.1em;font-weight:700}
.nlinks a.fz,.sheet a.fz{color:#fff}
body{background:#fff}
main#main *{text-wrap:wrap!important}
.nav{background:#fff!important}
main#main{font-family:'DM Sans',system-ui,sans-serif;color:#141216;-webkit-font-smoothing:antialiased}
.cl-w{max-width:560px;margin:0 auto;padding:0 18px;position:relative}
.cl-hero{background:#fff;padding:24px 0 0}
.cl-hero .cl-w{text-align:left}
.cl-kick{display:flex;width:max-content;margin:0 auto;align-items:center;gap:10px;height:33px;padding:0 17px;border:1.5px solid #F7B5D8;background:#FDE8F3;border-radius:99px;color:#E60F86;font:700 11.5px/1 'DM Sans',sans-serif;letter-spacing:.17em;text-transform:uppercase}
.cl-kick i{width:6px;height:6px;border-radius:1.5px;background:#FA1896}
.cl-hero h1{font:400 24.5px/26.6px 'DM Serif Display',serif;letter-spacing:-.022em;margin:15px 0 0;color:#141216}
.cl-hero h1 span{color:#FA1896}
.cl-sub p{font-size:15.9px;line-height:24.3px;color:#47414C;margin:15px 0 0;letter-spacing:-.003em}
.cl-sub p+p{margin-top:13px}
.cl-tag{font-size:17.5px;line-height:23.6px;font-weight:700;margin:16px 0 0;letter-spacing:-.01em}
.cl-deskk{display:flex;align-items:center;gap:12px;margin:21px 0 0;padding:6px 18px 6px 14px;min-height:48px;border:1px solid #E7E2DD;border-radius:26px;background:#fff;box-shadow:0 1px 3px rgba(20,18,22,.05);font-size:12.35px;line-height:16px;color:#3A343D;text-align:center}
.cl-deskk span{flex:1}
.cl-deskk i{flex:none;width:8px;height:8px;border-radius:2px;background:#2E9E62;box-shadow:0 0 0 3.5px rgba(46,158,98,.18)}
.cl-s1,.cl-s2,.cl-s3{background:linear-gradient(#fff,#FAF6EE 220px)}
.cl-s2,.cl-s3{background:#FAF6EE}
.cl-s1{padding:30px 0 0}
.cl-step{display:flex;align-items:center;gap:12px;margin:0;font:700 19.8px/1.1 'DM Sans',sans-serif;letter-spacing:-.01em;color:#141216;position:relative;z-index:2}
.cl-step .n{flex:none;width:28px;height:28px;border-radius:8px;background:#FA1896;color:#fff;display:grid;place-items:center;font-size:13.5px;font-weight:600}
.cl-step small{font-size:14px;font-weight:400;color:#7A737E;margin-left:2px}
.cl-cardwrap{position:relative;margin:16px -2px 0}
.cl-card{position:relative;z-index:1;background:#fff;border:1.5px solid #F4CDE2;border-radius:17px;padding:14px 15px 12px;box-shadow:0 6px 18px rgba(20,18,22,.06)}
.cl-cardwrap .thr{position:absolute;z-index:2;right:0;bottom:0;width:59%%;height:36%%;border-right:2px solid #FA1896;border-bottom:2px solid #FA1896;border-bottom-right-radius:17px;pointer-events:none}
.cl-card .who{display:flex;align-items:center;gap:13px}
.cl-card .av{position:relative;flex:none;width:44px;height:44px;border-radius:12px;background:#FCDCC8;color:#B4521A;display:grid;place-items:center;font-weight:700;font-size:14.2px;letter-spacing:.02em}
.cl-card .av b{position:absolute;right:-6px;bottom:-4px;width:19px;height:19px;border-radius:6px;background:#fff;border:1px solid #E7E2DD;color:#9A939E;display:grid;place-items:center}
.cl-card .av b svg{width:12px;height:12px}
.cl-card h3{margin:0;font-size:18.5px;font-weight:600;letter-spacing:-.01em}
.cl-card .who p{margin:3px 0 0;font-size:12.5px;color:#6B6470}
.cl-card .strat{display:flex;justify-content:space-between;align-items:center;margin:13px 0 0;padding:0 13px;height:36px;border-radius:9px;background:#FDE3F0;color:#E60F86}
.cl-card .strat span{font-size:12.8px;font-weight:600}
.cl-card .strat b{font-size:15.2px;letter-spacing:.12em;font-weight:700}
.cl-card .dh{display:flex;justify-content:space-between;align-items:baseline;margin:15px 0 0;padding-bottom:5px;border-bottom:1px solid #ECE8EE;font-size:12.3px;color:#6B6470}
.cl-card .dh b{color:#141216;font-weight:700;font-size:12.3px}
.cl-card .rw{display:grid;grid-template-columns:110px 1fr;gap:0;padding:7px 0;border-bottom:1px solid #ECE8EE;font-size:12.5px}
.cl-card .rw .k{color:#6B6470}
.cl-card .rw .v{color:#141216}
.cl-card .rw .v b{font-weight:600}
.cl-card .rw .v>b.blk{display:block}
.cl-card .rw .v small{display:block;color:#6B6470;font-size:11.8px;margin-top:2px}
.cl-card .chip{border:0;cursor:default;font-family:inherit;line-height:1.2;display:inline-flex;align-items:center;gap:8px;height:24px;padding:0 11px 0 8px;border-radius:99px;background:#F3F1F0;font-weight:600;font-size:12.3px;margin:0 0 4px}
.cl-card .chip svg{width:13px;height:10px;color:#8A8390}
.cl-card .est{font-style:normal;display:inline-block;padding:1px 6px;border-radius:4px;background:#ECEAE8;color:#6B6470;font-size:10.9px;line-height:15px;vertical-align:1px}
.cl-card .pk{color:#E60F86;font-weight:600}
.cl-card .pk.sm{font-size:12.0px}
.cl-card .ar{color:#6B6470}
.cl-card .rq{list-style:none;margin:0;padding:0}
.cl-card .rq li{position:relative;padding-left:20px;font-weight:600;margin-bottom:3px}
.cl-card .rq li:before{content:"";position:absolute;left:0;top:4px;width:8px;height:8px;border-radius:2px;border:1.5px solid #FA1896}
.cl-card .rq li.on:before{background:#FA1896}
.cl-card .tg{font-style:normal;font-weight:600;font-size:10.5px;padding:1px 7px;border-radius:99px;background:#FDE3F0;color:#E60F86;margin-left:4px}
.cl-card .fn{margin:9px 0 0;font-size:10.9px;color:#8A8390}
.cl-ctawrap{position:relative;padding:20px 0 0}
.cl-ctawrap .vline{position:absolute;left:50%%;top:-2px;bottom:-60px;width:2px;margin-left:-1px;background:#FA1896}
.cl-ctas{position:relative;z-index:1;display:flex;justify-content:center;gap:9px}
.cl-ctas a{height:46px;display:inline-flex;align-items:center;justify-content:center;border-radius:99px;font-weight:700;font-size:14.5px;text-decoration:none}
.cl-ctas .c1{width:143px;background:#FA1896;color:#fff;box-shadow:0 6px 14px rgba(250,24,150,.28)}
.cl-ctas .c2{width:165px;background:#fff;color:#141216;border:1.5px solid #D9D4D0}
.cl-s2{padding:40px 0 0}
.cl-desk .fo1{font:700 35px 'DM Sans',sans-serif;fill:#E60F86}
.cl-desk .fo2{font:500 30px 'DM Sans',sans-serif;fill:#8E5A76}
.cl-s3h{position:relative;height:42px;margin:0}
.cl-s3h .cl-step{position:absolute;left:0;top:0;height:28px}
.cl-phwrap{position:relative;margin:0 -18px;padding:0 0 0;}
.cl-phwrap:before{content:"";position:absolute;left:26px;right:26px;top:40px;bottom:-26px;background:#F3ECE0;border-radius:4px}
.cl-ph{position:relative;width:304px;height:634px;margin:0 auto;border-radius:52px;padding:5px;background:linear-gradient(135deg,#C9C4BD,#7F7A74 40%%,#B5B0AA 70%%,#6E6964);box-shadow:0 18px 40px rgba(20,18,22,.18)}
.cl-ph .scr{position:relative;height:100%%;border-radius:47px;background:#fff;border:6px solid #0E0D10;overflow:hidden;font-family:'DM Sans',sans-serif}
.cl-ph .isl{position:absolute;left:50%%;top:9px;width:90px;height:26px;margin-left:-45px;background:#0E0D10;border-radius:20px;z-index:3}
.cl-ph .sb{display:flex;justify-content:space-between;align-items:center;padding:12px 22px 0 33px;height:30px;font-size:13.7px}
.cl-ph .sb b{font-weight:600}
.cl-ph .sb .ic{display:flex;gap:5px;align-items:center}
.cl-ph .sb svg{width:16px;height:11px;fill:#141216}
.cl-ph .bat{display:inline-block;width:22px;height:11px;border:1.2px solid #8a8590;border-radius:3.5px;padding:1px}
.cl-ph .bat i{display:block;height:100%%;width:82%%;background:#141216;border-radius:1.5px}
.cl-ph .tb{display:flex;align-items:center;justify-content:space-between;padding:0 12px 0 14px;height:34px;margin-top:6px}
.cl-ph .bg{display:flex;flex-direction:column;gap:4px;width:18px}.cl-ph .bg i{height:1.6px;background:#141216;border-radius:2px}
.cl-ph .bg i:nth-child(2){width:80%%}
.cl-ph .ttl{display:flex;align-items:center;gap:5px;font-size:13px}.cl-ph .ttl img{width:11px;height:11px}.cl-ph .ttl b{font-weight:600}
.cl-ph .me{width:22px;height:22px;border-radius:7px;background:#FCDCC8;color:#B4521A;font-size:9px;font-weight:700;display:grid;place-items:center}
.cl-ph .seg{display:flex;margin:6px 6px 0;padding:3px;height:23px;border-radius:8px;background:#EEEBE8;font-size:10.8px;color:#5A545E}
.cl-ph .seg span{flex:1;display:grid;place-items:center;border-radius:7px}
.cl-ph .seg .on{background:#fff;color:#141216;font-weight:500;box-shadow:0 1px 2px rgba(0,0,0,.1)}
.cl-ph .th{position:absolute;left:0;right:0;top:112px;bottom:61px;overflow:hidden}
.cl-ph .th .in{position:absolute;left:0;right:0;bottom:0;padding:0 8px 0 10px}
.cl-ph .mc{margin:0 0 6px 34px;width:198px;border:1px solid #E5E1DD;border-radius:12px;overflow:hidden;background:#fff}
.cl-ph .mc .ph{position:relative;height:150px;background-size:cover;background-position:center}
.cl-ph .mc .pin{position:absolute;left:50%%;bottom:16px;width:10px;height:10px;margin-left:-5px;background:#FA1896;transform:rotate(45deg);border-radius:2px}
.cl-ph .mc .ph em{position:absolute;right:8px;bottom:24px;font-style:normal;font-size:9.3px;font-weight:600;background:#fff;border-radius:99px;padding:2px 7px;color:#141216}
.cl-ph .mc .tx{padding:4px 8px 7px;font-size:9.6px;line-height:13px;color:#3A343D}
.cl-ph .mc .tx b{display:block;font-size:11.2px;color:#141216;margin-bottom:1px}
.cl-ph .mc .tx small{display:block;color:#8A8390;font-size:8.5px;margin-top:3px}
.cl-ph .mc .est{font-style:normal;padding:0 4px;border-radius:3px;background:#ECEAE8;font-size:8.5px}
.cl-ph .who{margin:9px 0 3px 36px;font-size:10.4px;color:#5A545E}
.cl-ph .mm{display:flex;align-items:flex-end;gap:7px}
.cl-ph .mm .av{width:17px;height:21px;margin:0 0 6px 2px}
.cl-ph .mm.o{justify-content:flex-end;margin-top:6px}
.cl-ph .b{max-width:220px;padding:6px 10px;border-radius:13px;font-size:12.5px;line-height:15.6px}
.cl-ph .b span{display:block}
.cl-ph .f .b{background:#FA1896;color:#fff;max-width:218px}
.cl-ph .last .b{background:#FB6EBB}
.cl-ph .o .b{background:#E9E9EB;color:#141216}
.cl-ph .rd{text-align:right;font-size:9.6px;color:#6B6470;margin:4px 2px 0}
.cl-ph .tabs{position:absolute;left:0;right:0;bottom:0;height:61px;display:flex;justify-content:space-around;padding:6px 6px 0;background:#fff;border-top:1px solid #EEEAE6}
.cl-ph .tabs span{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:8.8px;color:#6B6470;width:46px}
.cl-ph .tabs svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.4;stroke-linejoin:round;stroke-linecap:round}
.cl-ph .tabs .on{color:#E60F86;font-weight:600}.cl-ph .tabs .on svg{fill:#FA1896;stroke:#E60F86}
.cl-ph .hb{position:absolute;left:50%%;bottom:6px;width:100px;height:4px;margin-left:-50px;background:#141216;border-radius:3px}
.cl-s3 .cl-ctas{margin-top:34px}
.cl-micro{text-align:center;font-size:12.6px;line-height:18.3px;color:#47414C;margin:19px 4px 0}
.cl-micro a{color:#141216;font-weight:700;text-decoration:underline;text-underline-offset:2px}
.cl-tmk{text-align:center;font-size:11.7px;line-height:18.2px;color:#857E88;margin:12px 4px 0}
.cl-s3{padding-bottom:118px}
.cl-stats{background:linear-gradient(#FAF6EE 34px,#fff 34px);padding:0 0 36px;margin-top:-34px}
.cl-stats .g{display:grid;grid-template-columns:1fr 1fr;background:#fff;border:1px solid #E7E2DD;border-radius:17px;overflow:hidden;box-shadow:0 8px 20px rgba(20,18,22,.06)}
.cl-stats .g div{padding:16px 16px 18px;min-height:120px}
.cl-stats .g div:nth-child(odd){border-right:1px solid #ECE8EE}
.cl-stats .g div:nth-child(-n+2){border-bottom:1px solid #ECE8EE}
.cl-stats b{display:block;font:400 30px/1.1 'DM Serif Display',serif;letter-spacing:-.01em;color:#141216}
.cl-stats b.pk{color:#FA1896}
.cl-stats span{display:block;margin-top:9px;font-size:13.1px;line-height:18.5px;color:#5A545E}
</style>'''%{'BRUSH':BRUSH}


import re as _re
BUILD=os.path.dirname(os.path.abspath(__file__))
# ---------------- home: photo hero with Claude's rotating scenarios, cream desk with Q&A, Darnell's four-pillar app ----------------
CSS2='<style>'+open(os.path.join(BUILD,'home_story_v2.css')).read()+'</style>'
JS2=open(os.path.join(BUILD,'home_story_v2.js.html')).read()
JS2=_re.sub(r'<script id="herospin">.*?</script>','',JS2,flags=_re.S)
JS2=_re.sub(r'<script id="deskmotion">.*?</script>','',JS2,flags=_re.S)
import html as H

# ======================= p5: the shared set kit (pt210u + urgent steering) =======================
import re as _re
BUILD=os.path.dirname(os.path.abspath(__file__))
PREV_FREEBIES='https://htmlpreview.github.io/?https://github.com/UpNonStop/firstofficer-site/blob/087c5d4ac80bed4aca88cb3b2910c71e50531298/free-from-the-desk.html'
LIVE='https://firstofficer.upnonstop.com/'
SET=['home-story','product','pricing','calculator','about','industries','book','story-map','for-dental']

# ---- ticker: desk tips, no figures, one pillar tag each ----
TIPS=[('Earn','Ad spend','Match it to a bonus category'),('Burn','Award rules','Vet them before you book'),
      ('Earn','Internet &amp; phone','Often a bonus category'),('Burn','Transfer bonuses','Check before you move points'),
      ('Return','Hotel nights','Compare points against cash'),('Learn','Expiring points','Every program keeps its own clock'),
      ('Return','Statement credits','Use them before they lapse'),('Burn','Partner charts','Often beat the airline&#39;s own price'),
      ('Learn','Idle points','Lose ground while they sit'),('Return','Friday report','Every week, in plain words')]
_t='<span class="tk"><span class="tk-dot"></span><b>DESK TIPS, ILLUSTRATED</b></span>'+''.join(
    f'<span class="tk tip"><i class="pl-{p.lower()}">{p.upper()}</i> <b>{a}</b> <span>{c.upper()}</span></span>' for p,a,c in TIPS)
fosite.TICK_HTML=f'<div class="fotick" aria-label="Desk tips"><div class="fotick-in">{_t}{_t}</div></div>'

# ---- nav: sheet order = desktop order, then Trust, Industries. No Field Notes. Brand -> home-story ----
_nav2=fosite.nav
def nav():
    h=_nav2()
    h=h.replace('<a href="field-notes.html">Field Notes</a>','')
    i0=h.index('<div class="sheet">'); i1=h.index('<a class="btn wa"',i0)
    sheet=('<a href="product.html">Product</a><a href="pricing.html">Pricing</a>'
           '<a class="fz" href="free-from-the-desk.html"><span>Freebies</span></a>'
           '<a href="calculator.html">Calculator</a><a href="about.html">About</a>'
           '<a href="trust.html">Trust</a><a href="industries.html">Industries</a>')
    h=h[:i0]+'<div class="sheet">'+sheet+h[i1:]
    return h
fosite.nav=nav

def fixlinks(html):
    def rep(m):
        href=m.group(1)
        if href.startswith(('http','#','mailto:','tel:','javascript')): return m.group(0)
        base=href.split('#')[0].split('?')[0]
        if base=='home.html': return m.group(0).replace(href,'home-story.html'+href[len(base):])
        if base=='free-from-the-desk.html': return m.group(0).replace(href,PREV_FREEBIES)
        if base=='disclaimer.html': return m.group(0).replace(href,LIVE+'terms-of-service.html')
        if base.endswith('.html') and base[:-5] in SET: return m.group(0)
        if base.endswith('.html') and os.path.exists(os.path.join(ROOT,'..',base)): return m.group(0).replace(href,LIVE+href)
        return m.group(0)
    html=_re.sub(r'href="([^"]+)"',rep,html)
    html=html.replace('<a href="upns.html">The Intelligence Report</a>','').replace(f'<a href="{LIVE}terms-of-service.html">Disclaimer</a>','')
    html=html.replace('</head>','<style>i,em{font-style:normal}</style></head>',1)
    return html
_page=page
def page(name,title,body,desc='',hero=False,src='site',tail=''):
    _page(name,title,body,desc=desc,hero=hero,src=src,tail=tail)
    p=os.path.join(ROOT,name); h=open(p).read(); open(p,'w').write(fixlinks(h))

# ---- the app phone: Claude's rotating scenarios, four pillar states, time-aware greeting ----
ACC={'earn':('#16A06A','#E3F6EC'),'burn':('#F26419','#FFF0E6'),'return':('#7348F0','#EFE9FF'),'learn':('#2E9BE8','#E4F3FD')}
PNAME={'earn':'Earn','burn':'Burn','return':'Return','learn':'Learn'}
PIC={'earn':TABI['Earn'],'burn':TABI['Burn'],'return':TABI['Return'],'learn':TABI['Learn']}
PROGN={'01':'Amex','02':'Chase','04':'Citi','10':'Hilton','12':'Hyatt','26':'Flying Blue','27':'British Airways','28':'Iberia','30':'Qatar Airways','32':'Singapore','17':'United'}
PROGF={'01':'01-amex','02':'02-chase','04':'04-citi','10':'10-hilton','12':'12-hyatt','26':'26-flying-blue','27':'27-british-airways','28':'28-iberia','30':'30-qatar-airways','32':'32-singapore','17':'17-united'}
def amsg(m):
    k=m[0]
    if k=='o': return f'<div class="m o"><div class="b">{m[1]}</div></div>'
    if k=='f': return f'<div class="m f"><span class="fa">FO</span><div class="b">{m[1]}</div></div>'
    if k=='s':
        n=m[1]; return (f'<div class="m s"><img class="sa" src="{LOGO(PROGF[n])}" alt=""><div class="b"><small>{PROGN[n]} specialist</small>{m[2]}</div></div>')
    if k=='card': return f'<div class="m c">{m[1]}</div>'
    return ''
def app(screens,aria,start=0,cls=''):
    sc=''
    for i,s in enumerate(screens):
        sc+=(f'<div class="sc{" on" if i==start else ""}" data-p="{s["p"]}" data-first="{s["first"]}" data-me="{s["me"]}" data-lab="{H.escape(s["lab"])}" data-ac="{ACC[s["p"]][0]}" data-at="{ACC[s["p"]][1]}">'
             f'<div class="in">{"".join(amsg(m) for m in s["msgs"])}<div class="ty"><span class="fa">FO</span><i></i><i></i><i></i></div></div></div>')
    s0=screens[start]; a,t=ACC[s0['p']]
    tabs=''.join(f'<span class="{"on" if n.lower()==s0["p"] else ""}" data-t="{n.lower()}"><svg viewBox="0 0 20 20" aria-hidden="true">{p}</svg>{n}</span>' for n,p in TABI.items())
    segs=''.join(f'<i class="{"on" if s["p"]==s0["p"] else ""}" data-t="{s["p"]}"></i>' for s in screens)
    return f'''<div class="cl-phwrap ap {cls}"><div class="cl-ph app" data-app style="--ac:{a};--at:{t}" role="img" aria-label="{aria}">
<div class="scr"><div class="isl"></div><div class="sb"><b>9:41</b><span class="ic"><svg viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx=".7"/><rect x="5" y="5.5" width="3" height="6.5" rx=".7"/><rect x="10" y="3" width="3" height="9" rx=".7"/><rect x="15" y="0" width="3" height="12" rx=".7"/></svg><i class="bat"><i></i></i></span></div>
<div class="tb"><span class="bg"><i></i><i></i><i></i></span><span class="ttl"><img src="{CHEV}" alt=""><b>First Officer</b></span><span class="me">{s0["me"]}</span></div>
<div class="gr"><span class="hi">Good evening, <b>{s0["first"]}</b></span><span class="pb"><svg viewBox="0 0 20 20" aria-hidden="true">{PIC[s0["p"]]}</svg><b>{H.escape(s0["lab"])}</b></span><span class="sg">{segs}</span></div>
<div class="th">{sc}</div>
<div class="tabs">{tabs}</div><div class="hb"></div></div></div></div>'''

E2='<em class="est">est</em>'
MAPC=lambda img,t,s: f'<div class="mc2"><div class="ph" style="background-image:url(img/ph/{img}.webp)"><em>Award space not guaranteed</em></div><div class="tx"><b>{t}</b><span>{s}</span></div></div>'
# Claude's hero scenarios (rebuild-v3/hero/fo-hero-data.js, from the hero v9/v10 mockups), one owner per pillar, beats kept verbatim where possible
CLAUDE=[
 dict(p='earn',first='Ines',me='IN',lab="Maple & Moss's Earn",msgs=[
  ('o','I spend so much on Meta and Google ads. Am I earning what I should?'),
  ('f','Probably not all of it. What do ads and shipping run per month, roughly?'),
  ('o','About 9k ads and 3k shipping. Everything is on the cash-back card for the 2% back.'),
  ('s','01','The business points card earns 4x on its top 2 eligible categories each billing cycle, on the first $150k a year combined.'),
  ('s','01',f'Her $108k {E2} a year in ads plus $36k {E2} shipping is about $144k {E2}, just under the cap.'),
  ('f',f'Simple version: ads and shipping move to the 4x card. About 576k points a year {E2}, instead of about $2,900 back.'),
  ('o','Love it. Do it.')]),
 dict(p='burn',first='Imani',me='IM',lab="Velvet Chair's Burn",msgs=[
  ('o','Me and 3 friends want Paris in April. Economy is fine. Can points do 4 tickets?'),
  ('f','Paris with your girls, yes! From Newark? And are your dates flexible?'),
  ('o','Newark. Any week in April.'),
  ('s','26','Flying Blue runs Promo Rewards each month with discounted award prices on select routes.'),
  ('card',MAPC('d-paris','Paris in April, economy','Watching the monthly promo. Requirements vetted first.')),
  ('f','Requirements vetted: 2 travelers on points, Newark, April, economy. The desk books once the sale opens.'),
  ('o','🥐🥐')]),
 dict(p='return',first='Callum',me='CL',lab="Stride PT's Return",msgs=[
  ('o','Is Qsuites actually worth the points or just hype?'),
  ('f','Fair question! Where would you fly, and when?'),
  ('o','Maldives, honeymoon, next fall. From Nashville.'),
  ('s','30','Qatar Privilege Club prices business awards in Avios on a distance-based chart.'),
  ('s','04','ThankYou points move 1:1 to Privilege Club.'),
  ('f',f'The honest value check: on points it often works out to 4c or more a point {E2}. Cash back would be about 1c.'),
  ('o','So roughly 4 times more. Okay!')]),
 dict(p='learn',first='Joanne',me='JO',lab="Joanne's Learn",msgs=[
  ('o','London after tax season with my daughter. Every time I check points, the fees are awful.'),
  ('f','You are not imagining it. Mind if the desk explains, then I make it simple?'),
  ('s','27','British Airways adds high carrier-imposed surcharges on its own flights from the US, even on awards.'),
  ('s','28','Iberia awards on Iberia flights typically carry lower surcharges.'),
  ('f','The lesson in plain words: the airline, not the points, decides the fees.'),
  ('o','Through Madrid sounds fun actually.'),
  ('f','Logged. I will remind you 11 months before April 20.')]),
]
REPC=(f'<div class="rp"><div class="rh"><b>Friday report</b><span>This month {E2}</span></div>'
      f'<div class="rr"><span>Points earned</span><b>62,500</b></div><div class="rr"><span>Valued honestly</span><b>$1,148</b></div>'
      f'<div class="rr"><span>Desk fee</span><b>−$550</b></div><div class="rr t"><span>Net to Ironwood</span><b>$598</b></div>'
      f'<div class="rr s"><span>A flat 2% card</span><b>$433</b></div></div>')
NOTEC=('<div class="nt"><span class="nk">Two-minute note</span><b>Hyatt points expire after 24 months without activity.</b>'
       '<span>One paid stay, award night or transfer in resets the clock.</span></div>')
EARNC=(f'<div class="em"><div class="eh"><b>Ads, software, gas</b><span>$106k a year {E2}</span></div>'
       '<div class="ebar"><span>Today 1x</span><i style="width:25%"></i></div><div class="ebar on"><span>At the desk 4x</span><i style="width:100%"></i></div>'
       f'<div class="ef">+318k points a year {E2}</div></div>')
DARNELL=[
 dict(p='earn',first='Darnell',me='DW',lab="Ironwood's Earn",msgs=[
  ('o','Are my ads earning what they should?'),
  ('f',f'Not yet. About $58k {E2} a year of ads sits on a 1x card.'),
  ('s','01','The business points card earns 4x on its top 2 eligible categories, on the first $150k a year combined.'),
  ('card',EARNC),
  ('f','Ads, software and gas move to the 4x card. Approve?'),
  ('o','Approved. Do it.')]),
 dict(p='burn',first='Darnell',me='DW',lab="Ironwood's Burn",msgs=[
  ('o','Rome in May, for our anniversary? Business if the points stretch.'),
  ('s','27','Avios price business to Rome via London. Vetting the award rules.'),
  ('card',MAPC('d-rome',"Business to Rome for two",f'Value per point checked. About 3c+ a point vs the cash fare {E2}')),
  ('f','They stretch. Hotel on Hilton points too, five nights.'),
  ('o','Love it. What do you need?'),
  ('f','Rough dates, please. We vet it, then the desk books it.')]),
 dict(p='return',first='Darnell',me='DW',lab="Ironwood's Return",msgs=[
  ('f','Your Friday report is in.'),
  ('card',REPC),
  ('o','So it clears the fee?'),
  ('f','By our estimate, yes. Estimates, not guarantees. Every move still waits for your yes.')]),
 dict(p='learn',first='Darnell',me='DW',lab="Darnell's Learn",msgs=[
  ('o','I have Hyatt points from years ago. Are they still good?'),
  ('f','Let us check before anything expires.'),
  ('s','12','World of Hyatt points expire after 24 months without qualifying activity. Earning or redeeming resets the clock.'),
  ('card',NOTEC),
  ('f','Yours may be close. One night on points saves them.'),
  ('o','Do it.')]),
]
app_claude=lambda start=0,cls='': app(CLAUDE,'The First Officer app, rotating through four example owners: Earn, Burn, Return, Learn. Fictional.',start,cls)
app_darnell=lambda start=1,cls='': app(DARNELL,"Darnell's First Officer app, rotating through Ironwood's Earn, Burn and Return, and Darnell's Learn. Fictional, figures est.",start,cls)

# ---- shared page parts ----
SETCSS='<style>'+open(os.path.join(BUILD,'set.css')).read()+'</style>'
SETJS=open(os.path.join(BUILD,'set.js.html')).read()
CH=[('home-story.html','Home','Meet Darnell'),('product.html','Product','Week one'),('pricing.html','Pricing','$550 a month'),
    ('calculator.html','Calculator','His numbers'),('about.html','About','Why a desk'),('industries.html','Industries','Your trade')]
def chapters(cur):
    return '<nav class="chs" aria-label="Darnell\'s story"><div class="chs-in"><span class="chs-h">Darnell&#39;s story</span>'+''.join(
        f'<a class="{"on" if h==cur else ""}" href="{h}"><span class="n">{i+1}</span><span class="t"><b>{n}</b><small>{d}</small></span></a>' for i,(h,n,d) in enumerate(CH))+'</div></nav>'
def phero(kick,h1,h2,sub,right,extra='',cls=''):
    return f'''<section class="cl-hero pg {cls}"><div class="hbg" aria-hidden="true"><i class="hp"></i><i class="hp"></i></div>
<div class="hx"><div class="cl-w ht"><div class="cl-kick"><i></i>{kick}</div><h1>{h1}<br><span>{h2}</span></h1><div class="cl-sub">{sub}</div>{extra}</div><div class="hph"><div class="hbg hbm" aria-hidden="true"><i class="hp"></i><i class="hp"></i></div>{right}</div></div></section>'''
def blk(cls,inner,id_=''):
    return f'<section class="bk {cls}"{f" id={chr(34)}{id_}{chr(34)}" if id_ else ""}><div class="bk-in">{inner}</div></section>'
def bh(n,t,s='',lead=''):
    return f'<div class="bh">{f"<span class={chr(34)}bn{chr(34)}>{n}</span>" if n else ""}<h2>{t}{f"<br><span>{s}</span>" if s else ""}</h2>{f"<p>{lead}</p>" if lead else ""}</div>'
def nextch(href,kick,t,s,cta):
    return f'''<section class="nx"><div class="hbg" aria-hidden="true"><i class="hp"></i><i class="hp"></i></div><div class="nx-in"><span class="nk">{kick}</span><h2>{t}<br><span>{s}</span></h2>
<div class="nx-c"><a class="c1" href="{href}">{cta} →</a><a class="c2" href="book.html?from=story">Get your desk</a></div></div></section>'''
STATS_H=s4
def mcta(src): return f'<a class="mcta" id="mcta" href="book.html?from={src}">Book Your "Found Money" Call</a>'
def setpage(name,title,body,desc,src):
    page(name,title,CSS+CSS2+SETCSS+body+mcta(src),desc=desc,src=src,tail=JS2+SETJS)
PHCAP='<div class="ph-cap"><i></i>Four example owners, one app. Earn, Burn, Return, Learn.</div>'
hero=f'''<section class="cl-hero"><div class="hbg" aria-hidden="true"><i class="hp"></i><i class="hp"></i></div>
<div class="hx"><div class="cl-w ht">{HERO_TXT}</div><div class="hph"><div class="hbg hbm" aria-hidden="true"><i class="hp"></i><i class="hp"></i></div>{app_claude(0)}{PHCAP}</div></div></section>'''
s3h=f'''<section class="cl-s cl-s3"><div class="cl-w"><div class="cl-s3h">{step(3,'What Darnell sees','in the app')}</div>{app_darnell(1)}
{CTAS}<p class="cl-micro">{MICRO}</p><p class="cl-tmk">{TMK}</p></div></section>'''
bandh='<div class="bandh"><h2>Meet Darnell.<br><span>Watch his desk work.</span></h2><p>One example owner, start to finish: his dossier, the desk of specialists answering his questions, and the four pillars he sees in the app. Fictional details. Figures are estimates.</p></div>'
PLI={'Earn':TABI['Earn'],'Burn':TABI['Burn'],'Return':TABI['Return'],'Learn':TABI['Learn']}
PILL=[('Earn',"Ironwood's Earn",'Every dollar of card spend lands on the card that pays most for it.',f'Ads moved from 1x to 4x. About +174k points a year {EST}.'),
      ('Burn',"Ironwood's Burn",'Points turn into trips. We vet the award rules, then the desk books it.','Rome in May, business for two. Requirements vetted first.'),
      ('Return',"Ironwood's Return",'Every Friday, what the points are worth in plain dollars, after our fee.',f'$598 net this month {EST}, against $433 from a flat 2% card.'),
      ('Learn',"Darnell's Learn",'Two-minute notes on the rules that cost owners the most.','Hyatt points expire after 24 months without activity.')]
def pillars(on=''):
    return ('<h2 class="pl-h">Earn, Burn, Return, Learn.<span>That is the whole system.</span></h2><div class="pls">'+''.join(
        f'<div class="pl{" on" if n==on else ""}"><div class="pn"><u><svg viewBox="0 0 20 20" aria-hidden="true">{PLI[n]}</svg></u><b>{n}</b></div><span class="ow">{o}</span><p>{d}</p><div class="ex">{e}</div></div>' for n,o,d,e in PILL)+'</div>')
home_pill=blk('w',pillars())
body=hero+chapters('home-story.html')+f'<section class="sbg">{bandh}<div class="band">{s1}{s2}{s3h}</div></section>'+home_pill+s4+nextch('product.html','Next chapter · Product','Week one at the desk.','Three leaks, found and fixed.','See week one')
setpage('home-story.html','First Officer by UpNonStop · You are not bad at Points & Miles',body,
     'A desk of specialists across 50+ programs, working for your business card spend. Meet Darnell, an example owner.','home')

# ---------------- story-map.html: how Darnell's story carries page to page (Claude style) ----------------
SM=[('home-story.html','Home','You are not bad at Points & Miles.','You are just outnumbered.',
     'Meet Darnell, an example gym owner, planning business to Rome for two on points. His desk, and what he sees in the app.',
     'Photo hero with the app rotating through four example owners, then dossier, the desk answering his questions, and his Earn, Burn, Return, Learn in the app','Product','See how it works'),
    ('product.html','Product','Week one, Darnell\'s desk','found three leaks.',
     'How it works, folded in: Earn, Burn, Return, Learn, told through his first week. Burn vets requirements; the desk books as an ad hoc service.',
     'Three leak cards, the four pillars, how you start, the desk at work','Pricing','See what it costs'),
    ('pricing.html','Pricing','$550 a month.','Here is what it buys for Darnell.',
     'One flat plan, cancel anytime. What the desk does for Darnell each week, value shown as est.',
     'Plan card, his month receipt est., a week at the desk, the yes-or-no gate, questions','Calculator','Run the numbers'),
    ('calculator.html','Calculator','His numbers first.','Then yours.',
     'Opens on the Darnell preset: $260k a year, 260k points today to 750k est. Then the owner swaps in their own mix.',
     'Darnell preset, category sliders, est. points and value','About','Who is behind the desk'),
    ('about.html','About','Why we built a desk,','not another hack.',
     'Why a desk of specialists beats one more trick. Ohad, Founder, UpNonStop.',
     'Founder note, principles, the four pillars, how a desk compares','Industries','See your trade'),
    ('industries.html','Industries','Darnell runs a gym.','Now, your trade.',
     'Same story, other trades: one example owner per industry, fictional, figures est.',
     '20 trades, each with an est. monthly mix and a link to its calculator preset','Get your desk','Get your desk'),
]
def smcard(i,r):
    href,name,h1,h2,beat,screens,nxt,cta=r
    last=i==len(SM)-1
    nh='book.html?from=story-map' if last else SM[i+1][0]
    return f'''<div class="sm-st">{step(i+1,name,'page '+str(i+1)+' of 6')}
<div class="cl-cardwrap"><div class="cl-card sm-c">
<p class="sm-h">{h1}<br><span>{h2}</span></p>
<div class="rw"><span class="k">Darnell's beat</span><div class="v">{beat}</div></div>
<div class="rw"><span class="k">On the page</span><div class="v">{screens}</div></div>
<div class="rw"><span class="k">Hand-off</span><div class="v"><a class="pk" href="{nh}">{cta} → {nxt}</a></div></div>
<p class="fn"><a href="{href}">Open {name}</a> · Example owner. Fictional details. Figures are estimates.</p>
</div>{'' if last else '<div class="thr"></div>'}</div>{'' if last else '<div class="sm-v"></div>'}</div>'''
smbody=CSS+'''<style>
.sm-top{padding:24px 0 8px}.sm-top h1{font:400 24.5px/26.6px 'DM Serif Display',serif;letter-spacing:-.022em;margin:15px 0 0}.sm-top h1 span{color:#FA1896}
.sm-top p{font-size:15.9px;line-height:24.3px;color:#47414C;margin:12px 0 0}
.sm{background:linear-gradient(#fff,#FAF6EE 220px);padding:22px 0 60px}
.sm-st{position:relative}.sm-v{width:2px;height:46px;margin:0 auto;background:#FA1896}
.sm-h{font:400 21px/24px 'DM Serif Display',serif!important;margin:0 0 10px!important;color:#141216}.sm-h span{color:#FA1896}
.sm-c .rw{grid-template-columns:104px 1fr}.sm-c .fn a{color:#141216;font-weight:700}
.sm-c a.pk{text-decoration:none}
@media(min-width:900px){.sm-top{padding-top:56px}.sm-top h1{font-size:44px;line-height:48px}.sm-h{font-size:26px!important;line-height:30px!important}}
</style>'''+f'''<section class="cl-hero sm-top"><div class="cl-w"><span class="cl-kick"><i></i>Story map</span>
<h1>One owner, six pages.<br><span>Darnell carries the story.</span></h1>
<p>Each page picks up where the last one left off, in the same First Officer voice. Darnell is an example owner. Fictional details. Figures are estimates.</p></div></section>
<section class="sm"><div class="cl-w">{''.join(smcard(i,r) for i,r in enumerate(SM))}
<div class="cl-ctawrap">{CTAS}</div><p class="cl-micro">{MICRO}</p></div></section>'''
page('story-map.html','First Officer · Story map',smbody,desc='How Darnell, an example owner, carries the First Officer story from page to page.',src='home')

# ======================= p6: product, pricing, calculator, about, industries =======================
IND=json.load(open('/tmp/hs/ind.json')) if os.path.exists('/tmp/hs/ind.json') else json.load(open(os.path.join(BUILD,'ind.json')))
DESKQ='<div class="dqside">'+desk_svg+'</div>'
def fmt(n): return f'${n:,.0f}'

# ---------- product ----------
LEAKS=[('Leak 1 · Earn','Ads on a 1x card',f'About $58k {EST} a year of ad spend earned 1 point a dollar. The business points card pays 4x on it.',[('Today 1x','58k',25,False),('At the desk 4x','232k',100,True)],f'+174k points a year {EST}'),
       ('Leak 2 · Earn','Software and gas, same card',f'Software and gas, about $48k {EST} a year, also qualify for 4x inside the same yearly cap.',[('Today 1x','48k',25,False),('At the desk 4x','192k',100,True)],f'+144k points a year {EST}'),
       ('Leak 3 · Earn','Everything else at 1x',f'Equipment, utilities, internet and the rest, about $154k {EST} a year, move to 2x and 3x cards.',[('Today 1x','154k',45,False),('At the desk 2x to 3x','326k',100,True)],f'+172k points a year {EST}')]
def leak(k,t,p,rows,f):
    m=''.join(f'<div class="r"><span>{a}</span><b>{b}</b></div><div class="t{" on" if on else ""}"><i style="width:{w}%"></i></div>' for a,b,w,on in rows)
    return f'<div class="cd"><span class="k"><i></i>{k}</span><h3>{t}</h3><p>{p}</p><div class="meter">{m}</div><span class="big">{f.split(" points")[0]}<small>points a year {EST}</small></span></div>'
TOT=f'<div class="cd" style="margin-top:12px;background:#141216;background:#FA1896;color:#fff;border-color:#FA1896"><span class="k" style="color:#FFE3F1"><i style="background:#fff"></i>Week one, in total</span><h3 style="color:#fff">260k points a year today. About 750k {EST} at the desk.</h3><p style="color:#FFF1F8">Same spend, same cards he can get, a different card for each line. Nothing moved without his yes.</p></div>'
HOWS=[('The Found Money Call','Free, 20 minutes, 6 questions. We size what your spend could capture first.'),
      ('Your Bespoke Strategy','A written plan: which card for which line, and the trips worth saving for. Yours to approve.'),
      ('The desk goes to work','Specialists across 50+ programs answer your questions, watch the rules and vet every award.'),
      ('The Friday report','What the points are worth in plain dollars, after our fee. Every week.')]
howlist='<ol class="st">'+''.join(f'<li><span class="n">{i+1}</span><div><b>{a}</b><span>{b}</span></div></li>' for i,(a,b) in enumerate(HOWS))+'</ol>'
prod=(phero('Product · Chapter 2',"Week one, Darnell's desk",'found three leaks.',
   f'<p>Darnell runs Ironwood Strength Club in Chicago and puts about $21.7k {EST} a month on cards. In his first week, the desk found three places his spend earned less than it should.</p>',
   app_darnell(0),f'<div class="cl-hcta">{CTAS}</div>')+chapters('product.html')
 +blk('c',bh('1','Three leaks.','Found in week one.',f'Every figure is an estimate from his own monthly mix. Earning rules are set by each card and can change.')+'<div class="g3">'+''.join(leak(*l) for l in LEAKS)+'</div>'+TOT)
 +blk('w',pillars())
 +blk('d','<div class="split r"><div>'+bh('2','How you start.','Then the desk takes over.')+howlist+'</div><div>'+DESKQ+'<p class="cl-dcap">Darnell asks, a specialist picks it up, First Officer answers in one voice.</p></div></div>')
 +blk('p','<div class="split"><div>'+bh('3','One voice.','Every program.','You text First Officer. Behind it, specialists for 50+ programs check the rules, then you get one plain answer, with the math, waiting for your yes.')+f'<div class="cl-ctawrap">{CTAS}</div></div><div>{app_claude(2)}</div></div>')
 +s4+nextch('pricing.html','Next chapter · Pricing','$550 a month.','Here is what it buys for Darnell.','See pricing'))
setpage('product.html','First Officer · Product · Week one at Darnell\'s desk',prod,'How First Officer works, told through Darnell\'s first week: three leaks, the four pillars, and the desk at work.','product')

# ---------- pricing ----------
PLAN=f'''<div class="rcp" style="max-width:380px;margin:0 auto"><span class="k" style="font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#E60F86">One plan</span>
<h3 style="font-size:40px;line-height:44px;margin-top:6px">$550<small style="font:600 15px 'DM Sans',sans-serif;color:#6B6470"> a month</small></h3>
<div class="r"><span>The desk, across 50+ programs</span><b>Included</b></div><div class="r"><span>Bespoke Strategy</span><b>Included</b></div>
<div class="r"><span>Friday report, every week</span><b>Included</b></div><div class="r"><span>Award booking, after vetting</span><b>$500 flat</b></div>
<div class="r"><span>Cancel anytime</span><b>Yes</b></div><a class="mb" href="book.html?from=pricing" style="display:flex;margin-top:14px;height:50px;border-radius:12px;background:#FA1896;color:#fff;font-weight:800;align-items:center;justify-content:center;text-decoration:none">Get your desk</a>
<small>No affiliate money, ever. Estimates, not guarantees.</small></div>'''
TILES=[('$550','The desk','A month, flat. Earn, Burn, Return and Learn for the whole business. Cancel anytime.'),
       ('$500','Per award itinerary','Flat, any party size. An ad hoc service: the desk books after the requirements are vetted. Award space not guaranteed.'),
       ('$0','The Found Money Call','20 minutes, 6 questions. We size your capture before you pay a cent.'),
       ('None','Affiliate money','No commissions from any bank, airline or hotel program. Ever.')]
tiles='<div class="g4">'+''.join(f'<div class="cd"><span class="k"><i></i>{b}</span><span class="big">{a}</span><p>{c}</p></div>' for a,b,c in TILES)+'</div>'
RCP=f'''<div class="rcp"><h3>Darnell's month, est.</h3>
<div class="r"><span>Card spend</span><b>$21,667</b></div><div class="r"><span>Points earned at the desk</span><b>62,500</b></div>
<div class="r"><span>Points used (85%)</span><b>53,125</b></div><div class="r"><span>Travel at sticker, 3c a point</span><b>$1,594</b></div>
<div class="r"><span>Valued honestly (60% would be bought anyway)</span><b>$1,148</b></div><div class="r"><span>Desk fee</span><b>−$550</b></div>
<div class="r t"><span>Net to Ironwood {EST}</span><b>$598</b></div><div class="r"><span>A flat 2% cash-back card, same spend</span><b>$433</b></div>
<small>Same assumptions as the calculator defaults. Your numbers will differ. Estimates, not guarantees.</small></div>'''
WEEK=[('Mon','Ads charge lands on the 4x card. Checked.'),('Tue','Darnell asks about Rome. British Airways specialist vets the award rules.'),
      ('Wed','Hilton specialist compares points and cash, night by night.'),('Thu','Hyatt clock checked. A note goes out before anything expires.'),
      ('Fri','The Friday report: points, dollars, after our fee.')]
week='<div class="wk">'+''.join(f'<div class="{"fr" if d=="Fri" else ""}"><b>{d}</b><span>{t}</span></div>' for d,t in WEEK)+'</div>'
GATE='<div class="gate"><u>✓</u><div><b>If the call shows our work will not clear the fee, we tell you in writing, and you never pay.</b><span>The Found Money Call sizes your capture first. An honest no if the math says no.</span></div></div>'
FAQ=[('Is the rate locked?','Your $550 a month stays as long as you stay. Cancel anytime, with no notice period and no exit fee.'),
     ('What does the $500 award fee cover?','One itinerary, any party size. We vet the requirements first, then the desk books it as an ad hoc service. Award space is set by each program and is not guaranteed.'),
     ('Do you take commissions from card issuers?','No. No affiliate money from any bank, airline or hotel program, ever.'),
     ('Do you guarantee savings?','No. Every figure we show is an estimate, labelled est. The Friday report shows what actually happened.'),
     ('Who makes the decisions?','You do. Every move waits for your yes.')]
faq='<div class="fq">'+''.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i,(q,a) in enumerate(FAQ))+'</div>'
pric=(phero('Pricing · Chapter 3','$550 a month.','Here is what it buys for Darnell.',
   '<p>One flat plan. No tiers, no affiliate money, cancel anytime. Here is the month it buys for an example gym owner.</p>',PLAN)+chapters('pricing.html')
 +blk('c',bh('1','Four numbers.','That is the whole price list.')+tiles)
 +blk('w','<div class="split">'+'<div>'+bh('2','His month, est.','Fee included.','The same defaults the calculator opens on. Value counted honestly, not at sticker.')+GATE+'</div>'+RCP+'</div>')
 +blk('d',bh('3','A week at the desk.','What $550 looks like.')+week)
 +blk('c','<div class="split"><div>'+bh('4','Questions,','answered plainly.')+'</div>'+faq+'</div>')
 +s4+nextch('calculator.html','Next chapter · Calculator','His numbers first.','Then yours.','Run the numbers'))
setpage('pricing.html','First Officer · Pricing · $550 a month',pric,'One flat plan at $550 a month, cancel anytime. Here is what it buys for Darnell, an example gym owner.','pricing')

# ---------- calculator ----------
DARN={'id':'darnell','nm':"Darnell's gym (example)",'pg':'home-story.html','off':[],'cats':[
 {'n':'Ads','h':'Meta, Google, local radio','v':58000/12,'mx':4,'b':['G4','P3','F2']},
 {'n':'Equipment','h':'Racks, machines, repairs','v':52000/12,'mx':2,'b':['F2']},
 {'n':'Everything else','h':'Supplies, smaller vendors','v':50000/12,'mx':2,'b':['F2']},
 {'n':'Utilities','h':'Power, water, HVAC','v':34000/12,'mx':2,'b':['F2']},
 {'n':'Software','h':'Booking, payroll, cloud','v':26000/12,'mx':4,'b':['G4','F2']},
 {'n':'Gas & travel','h':'Fuel, tolls, trips','v':22000/12,'mx':4,'b':['G4','F2']},
 {'n':'Internet & phone','h':'Lines and wireless','v':18000/12,'mx':3,'b':['P3','F2']}]}
INDC=[DARN]+IND
CALCJS='<script id="calcjs">(function(){var IND='+json.dumps(INDC)+r''';
var sel=document.getElementById('indSel'),cats=document.getElementById('cats');
IND.forEach(function(x,i){var o=document.createElement('option');o.value=i;o.textContent=x.nm;sel.appendChild(o)});
var q=(location.search.match(/[?&]ind=([a-z]+)/)||[])[1];if(q){IND.forEach(function(x,i){if(x.id===q)sel.value=i})}
var cur,vals=[];function money(n){return '$'+Math.round(n).toLocaleString('en-US')}
function build(){cur=IND[+sel.value];vals=cur.cats.map(function(c){return c.v});cats.innerHTML='';
 cur.cats.forEach(function(c,i){var max=Math.max(20000,Math.ceil(c.v*4/5000)*5000),st=max<=60000?500:1000;var d=document.createElement('div');d.className='crow';
  d.innerHTML='<div class="t"><b id="cn'+i+'">'+c.n.replace(/&/g,'&amp;')+'<span class="rt">'+(c.mx>=3?'up to '+c.mx+'x':c.mx+'x')+'</span></b><span data-v="'+i+'">'+money(c.v)+'</span></div><div class="h">'+(c.h||'')+'</div><input type="range" min="0" max="'+max+'" step="'+st+'" value="'+Math.round(c.v)+'" data-i="'+i+'" aria-labelledby="cn'+i+'">';
  cats.appendChild(d)});
 cats.querySelectorAll('input').forEach(function(inp){inp.addEventListener('input',function(){vals[+inp.dataset.i]=+inp.value;cats.querySelector('[data-v="'+inp.dataset.i+'"]').textContent=money(+inp.value);calc()})});
 document.getElementById('offN').textContent=cur.off&&cur.off.length?'Left off the card: '+cur.off.join(', ')+'. The desk decides those line by line.':'';calc()}
function calc(){var CAPS={G4:150000,P3:150000},RATE={G4:4,P3:3,F2:2,I1:1};var spend=0,pts=0,left={G4:CAPS.G4,P3:CAPS.P3},rem=[],base=0;
 cur.cats.forEach(function(c,i){var v=vals[i]||0;spend+=v;rem[i]=v*12});
 ['G4','P3'].forEach(function(pool){var idx=[];cur.cats.forEach(function(c,i){if(c.b.indexOf(pool)>=0)idx.push(i)});
  idx.sort(function(a,b){var fa=cur.cats[a].b,fb=cur.cats[b].b;return (RATE[fa[fa.indexOf(pool)+1]]||1)-(RATE[fb[fb.indexOf(pool)+1]]||1)});
  idx.forEach(function(i){var t=Math.min(rem[i],left[pool]);if(t>0){pts+=t*RATE[pool];left[pool]-=t;rem[i]-=t}})});
 cur.cats.forEach(function(c,i){if(rem[i]>0){var fb=c.b[c.b.length-1];pts+=rem[i]*((fb==='F2'||fb==='I1')?RATE[fb]:1)}});
 pts=pts/12;var cpp=+document.getElementById('cpp').value/10,util=+document.getElementById('util').value/100,real=+document.getElementById('real').value/100;
 var used=pts*util,sticker=used*cpp/100,cash=sticker*real+sticker*(1-real)*.3,fee=550,net=cash-fee,two=spend*.02;
 function s(id,v){document.getElementById(id).textContent=v}
 s('mSpend',money(spend));s('mPts',Math.round(pts).toLocaleString('en-US'));s('mToday',Math.round(spend).toLocaleString('en-US'));s('mEarn',(spend?pts/spend:0).toFixed(1)+'x');
 s('cppV',cpp.toFixed(1)+'c');s('utilV',Math.round(util*100)+'%');s('realV',Math.round(real*100)+'%');
 s('oUsed',Math.round(used).toLocaleString('en-US'));s('oStk',money(sticker));s('oCash',money(cash));s('oNet',(net<0?'−':'')+money(Math.abs(net)));s('oBig',(net<0?'−':'')+money(Math.abs(net)));s('oTwo',money(two));
 s('oVs',net>two?'By this estimate the desk beats a flat 2% card by '+money(net-two)+' a month.':(net>0?'By this estimate a flat 2% card wins at this spend. The call will tell you so.':'By this estimate the desk does not clear the fee at this spend. We would tell you so on the call, in writing.'))}
sel.addEventListener('change',build);['cpp','util','real'].forEach(function(id){document.getElementById(id).addEventListener('input',calc)});build()})();</script>'''
CALC=f'''<div class="calc"><div class="cpan"><label class="sel" for="indSel">Start from</label><select id="indSel"></select>
<div class="mtl"><div><span>Monthly spend</span><b id="mSpend">$0</b></div><div><span>Points today, 1x</span><b id="mToday">0</b></div><div><span>Points at the desk {EST}</span><b id="mPts">0</b></div><div><span>Points per dollar</span><b id="mEarn">0x</b></div></div>
<div id="cats"></div><p class="h" id="offN" style="font-size:12px;color:#6B6470;margin:10px 0 0"></p>
<div class="knobs"><div class="knob"><div class="t"><span>Value per point</span><b id="cppV">3.0c</b></div><input id="cpp" type="range" min="10" max="50" value="30" aria-label="Value per point"><small>Cents a point when redeemed for travel. 1c is cash back; partner awards often run higher. est.</small></div>
<div class="knob"><div class="t"><span>Points you actually use</span><b id="utilV">85%</b></div><input id="util" type="range" min="40" max="100" value="85" aria-label="Points used"></div>
<div class="knob"><div class="t"><span>Trips you would buy anyway</span><b id="realV">60%</b></div><input id="real" type="range" min="0" max="100" value="60" aria-label="Trips you would buy anyway"><small>The rest counts at 30% of sticker. That is the honest discount.</small></div></div></div>
<div class="out" aria-live="polite"><span class="k">Net to you each month {EST}</span><div class="big" id="oBig">$0</div><div class="sub">After the $550 desk fee.</div>
<div class="r"><span>Points used</span><b id="oUsed">0</b></div><div class="r"><span>Travel at sticker</span><b id="oStk">$0</b></div><div class="r"><span>Valued honestly</span><b id="oCash">$0</b></div>
<div class="r"><span>Desk fee</span><b>−$550</b></div><div class="r t"><span>Net {EST}</span><b id="oNet">$0</b></div><div class="r"><span>A flat 2% card instead</span><b id="oTwo">$0</b></div>
<div class="vs" id="oVs"></div><a href="book.html?from=calculator">Book Your "Found Money" Call</a>
<small>Earning on published card terms: 4x and 3x pools on the first $150,000 a year each, then 2x. Card annual fees not deducted. Estimates, not guarantees. Not tax, legal or financial advice.</small></div></div>'''
calc=(phero('Calculator · Chapter 4','His numbers first.','Then yours.',
   f'<p>The calculator opens on Darnell: about $260k {EST} a year on cards, 260k points today, about 750k {EST} at the desk. Then pick your trade and move the sliders.</p>',
   app_darnell(2),f'<div class="cl-hcta">{CTAS}</div>')+chapters('calculator.html')
 +blk('c',bh('1','Run the numbers.','Honestly.','Every slider is yours. The defaults are Darnell&#39;s.')+CALC)
 +blk('d','<div class="split r"><div>'+bh('2','The math,','shown.')+'<ol class="st"><li><span class="n">1</span><div><b>Each line goes to its best card</b><span>Ads, software and gas to 4x, internet to 3x, the rest to 2x, inside each card&#39;s yearly cap.</span></div></li><li><span class="n">2</span><div><b>Only the points you use count</b><span>Unused points are worth nothing, so we count 85% by default.</span></div></li><li><span class="n">3</span><div><b>Trips you would not buy count less</b><span>A free trip you would never have paid for counts at 30%.</span></div></li><li><span class="n">4</span><div><b>Our fee comes off</b><span>Then we compare it with a flat 2% card. If we lose, we say so.</span></div></li></ol></div><div>'+GATE+'</div></div>')
 +s4+nextch('about.html','Next chapter · About','Why we built a desk,','not another hack.','Read why'))
setpage('calculator.html','First Officer · Calculator · Darnell first, then you',calc,'Run your own numbers. Opens on Darnell, an example gym owner: about 260k points a year today, about 750k est at the desk.','calculator',)
p=os.path.join(ROOT,'calculator.html');h=open(p).read();h=h.replace('<script src="assets/site.js"></script>',CALCJS+'<script src="assets/site.js"></script>',1);open(p,'w').write(h)

# ---------- about ----------
IDC='<div class="id"><u>OS</u><b>Ohad Sternberg</b><span>Founder, UpNonStop</span></div>'
NOTE='''<div class="nt"><p>I built First Officer because I kept watching brilliant business owners leave real money on the table. Not from carelessness. From busyness.</p>
<p>Nobody has spare hours to babysit transfer bonuses and statement credits. So the desk babysits them for you, and every single decision stays yours: shown with its math, approved by you, cancel anytime.</p>
<p>That is what financial freedom looks like to me. Not a lottery ticket. A system that quietly hands you back what you already earned.</p><p class="sig">You have already earned it. Ohad</p></div>'''
PRIN=[('01','Zero affiliate money','No commissions from issuers, ever. Our advice has exactly one customer: you.'),
      ('02','Math shown, yes required','No black boxes and no surprises. If we cannot show the number, we do not make the call.'),
      ('03','Every decision yours','Nothing moves until you say yes. Estimates are labelled est., never promised.')]
prin='<div class="g3">'+''.join(f'<div class="cd"><span class="k"><i></i>{n}</span><h3>{t}</h3><p>{d}</p></div>' for n,t,d in PRIN)+'</div>'
CMP='''<div class="cmp"><div><b>Courses and masterminds</b><p>They certify you.</p><ul><li>Curriculum and homework</li><li>The work stays yours</li><li>Often paid on card signups</li></ul></div>
<div><b>Affiliate content</b><p>They get paid to point.</p><ul><li>Facts usually accurate</li><li>Order of cards bought</li><li>Top card pays most per click</li></ul></div>
<div class="us"><b>First Officer</b><p>We do the work.</p><ul><li>$550 a month, flat</li><li>No affiliate money</li><li>A dollar number every Friday</li></ul></div></div>'''
MISSION=f'<div class="split"><div>{bh("1","Return what was","already earned.")}</div><p class="lead2">Give every American small and medium business a professional rewards desk, so the dollars their spending already earned come back as capital and flights instead of quietly expiring. Owners run payroll, chase invoices and take care of people. Nobody has spare hours to babysit transfer bonuses and statement credits. That is a full-time job. So we made it one.</p></div>'
abt=(phero('About · Chapter 5','Why we built a desk,','not another hack.',
   '<p>Darnell did not need another tip. He needed someone on his side of the table, every week. That is the desk.</p>',
   app_claude(3),f'<div class="cl-hcta">{CTAS}</div>')+chapters('about.html')
 +blk('c',MISSION)
 +blk('w',bh('2','From the founder.','One promise.')+f'<div class="fd">{IDC}{NOTE}</div>')
 +blk('d',bh('3','Simple,','and non-negotiable.')+prin)
 +blk('c',pillars())
 +blk('w',bh('4','Not a course. Not a card pitch.','An operator.','Everything else in this space either teaches you to do the work or gets paid when you apply for something. We do neither.')+CMP)
 +s4+nextch('industries.html','Next chapter · Industries','Darnell runs a gym.','Now, your trade.','Find your trade'))
setpage('about.html','First Officer · About · Why a desk',abt,'Why First Officer is a desk, not another hack. A note from Ohad Sternberg, Founder, UpNonStop.','about')

# ---------- industries ----------
def ini(n): return ''.join(w[0] for w in n.replace('/',' ').split()[:2]).upper()
tl=f'<a class="ft" href="calculator.html"><u>DW</u><b>Fitness · Darnell</b><span>Ironwood Strength Club. About $21.7k {EST} a month. The story you just read.</span><em>Run his numbers →</em></a>'
for x in IND:
    if x['id'] in ('other','fitness'): continue
    sp=sum(c['v'] for c in x['cats'])
    top=sorted(x['cats'],key=lambda c:-c['v'])[:2]
    tl+=f'<a href="calculator.html?ind={x["id"]}"><u>{ini(x["nm"])}</u><b>{x["nm"]}</b><span>Example mix: about {fmt(sp)} {EST} a month. Biggest lines: {H.escape(top[0]["n"])}, {H.escape(top[1]["n"])}.</span><em>Run this preset →</em></a>'
pages='<div class="tpl">'+''.join(f'<a href="{x["pg"]}"><u>{ini(x["nm"])}</u><b>{x["nm"]}</b><i>→</i></a>' for x in IND if x['id']!='other')+'</div>'
indp=(phero('Industries · Chapter 6','Darnell runs a gym.','Now, your trade.',
   '<p>Same desk, other trades. Each preset is an example monthly mix for that trade. Pick yours and the calculator opens on it.</p>',
   app_claude(1),f'<div class="cl-hcta">{CTAS}</div>')+chapters('industries.html')
 +blk('c',bh('1','20 trades.','One desk.','Example mixes only. Your own numbers come from the Found Money Call.')+'<div class="inds">'+tl+'</div>')
 +blk('d','<div class="split r"><div>'+bh('2','Different trade,','same four pillars.','A salon, a law firm or a trucking company: the desk Earns, Burns, Returns and helps you Learn the same way.')+'</div><div>'+pillars()+'</div></div>')
 +blk('w',bh('3','Read about','your trade.')+pages)
 +s4+nextch('book.html?from=industries','The last chapter is yours','Your trade,','your desk.','Get your desk'))
setpage('industries.html','First Officer · Industries · Your trade',indp,'Darnell runs a gym. Now your trade: 20 industries, each with an example monthly mix and a calculator preset.','industries')
