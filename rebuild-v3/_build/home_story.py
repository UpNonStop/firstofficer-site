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
MIX=[('Ads',58_000,4),('Equipment',52_000,2),('Everything else',50_000,2),('Utilities',34_000,2),('Software',26_000,4),('Gas &amp; travel',22_000,4),('Internet &amp; phone',18_000,5)]
assert sum(v for _,v,_ in MIX)==SPEND
PTS_DESK=sum(v*x for _,v,x in MIX)          # 786,000
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
        o.append(f'<g class="sp{" big" if big else ""}" data-x="{x-CX:.1f}" data-y="{y-CY:.1f}" data-r="{r}"><circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" class="bub"/>'
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
desk_svg=desk_d+desk_m
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


# ---------------- v2 assembly: hero (photos + cream wash, desktop two-column with Darnell's app), colour-block band, sticky bar ----------------
CSS2='<style>'+open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'home_story_v2.css')).read()+'</style>'
JS2=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'home_story_v2.js.html')).read()
hero=f'''<section class="cl-hero"><div class="hbg" aria-hidden="true"><i class="hp"></i><i class="hp"></i></div>
<div class="hx"><div class="cl-w ht">{HERO_TXT}</div><div class="hph">{phone}</div></div></section>'''
phone_m=phone.replace('class="cl-phwrap"','class="cl-phwrap mob"',1)
s3=s3.replace(phone,phone_m+plan_phone)
bandh='<div class="bandh"><h2>Meet Darnell.<br><span>Watch his desk work.</span></h2><p>One example owner, start to finish: his dossier, the desk of specialists working his programs, and the plan he sees in the app. Fictional details. Figures are estimates.</p></div>'
MCTA='<a class="mcta" id="mcta" href="book.html?from=home">Book Your "Found Money" Call</a>'
body=CSS+CSS2+hero+f'<section class="sbg">{bandh}<div class="band">{s1}{s2}{s3}</div></section>'+s4+MCTA
page('home-story.html','First Officer by UpNonStop · You are not bad at Points & Miles',body,
     desc='A desk of specialists across 50+ programs, working for your business card spend. Meet Darnell, an example owner.',src='home',tail=JS2)

# ---------------- story-map.html: how Darnell's story carries page to page (Claude style) ----------------
SM=[('home-story.html','Home','You are not bad at Points & Miles.','You are just outnumbered.',
     'Meet Darnell, an example gym owner, planning business to Rome for two on points. His desk, and what he sees in the app.',
     'Hero with his app chat, then dossier, desk of 50+ programs and Your plan side by side','Product','See how it works'),
    ('product.html','Product','Week one, Darnell\'s desk','found three leaks.',
     'How it works, folded in: Earn, Burn, Return, Learn, told through his first week. Burn vets requirements; the desk books as an ad hoc service.',
     'Earn leak card, Burn trip check, Return report, Learn note','Pricing','See what it costs'),
    ('pricing.html','Pricing','$550 a month.','Here is what his buys.',
     'One flat plan, cancel anytime. What the desk does for Darnell each week, value shown as est.',
     'Plan card, what the desk covers, Friday report preview','Calculator','Run the numbers'),
    ('calculator.html','Calculator','His numbers first.','Then yours.',
     'Opens on the Darnell preset: $260k a year, 260k points today to 786k est. Then the owner swaps in their own mix.',
     'Darnell preset, category sliders, est. points and value','About','Who is behind the desk'),
    ('about.html','About','Why we built a desk,','not another hack.',
     'Why a desk of specialists beats one more trick. Ohad, Founder, UpNonStop.',
     'Founder note, the four pillars, how the desk works for you','Industries','See your trade'),
    ('industries.html','Industries','A gym owner like Darnell.','Now, your trade.',
     'Same story, other trades: one example owner per industry, fictional, figures est.',
     'Industry cards, one example owner each','Get your desk','Get your desk'),
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
