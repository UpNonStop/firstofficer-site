"""Mobile-first persona homepage mockup (Darnell, fictional). Static: no hero engine.
Layout follows the Claude mobile landing: hero, then 3 numbered steps (Meet / His desk / What he sees), then stat blocks.
Run: python3 _build/home_persona.py  ->  rebuild-v3/home-persona.html"""
import math, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fosite
from fosite import *

# ---------------- numbers (every figure shown is labelled est.) ----------------
SPEND  = 260_000     # annual card spend, $
TODAY_X = 1.0        # points per $ today (flat 1x)
DESK_X  = 3.8        # points per $ with the desk (brief figure; calculator caps reach ~3.58x max at this spend)
CPP    = 0.03        # $ per point, calculator default 3.0c
UTIL   = 0.85        # share of points redeemed, calculator default 85%
CASH   = 0.02        # cash back benchmark, calculator 2%
FEE_M  = 550         # flat monthly
pts_today = round(SPEND*TODAY_X)                     # 260,000
pts_desk  = round(SPEND*DESK_X/10_000)*10_000        # 988,000 -> 990,000
gross     = round(pts_desk*CPP*UTIL)                 # 25,245
fee_y     = FEE_M*12                                 # 6,600
net       = gross-fee_y                              # 18,645
cashback  = round(SPEND*CASH)                        # 5,200
K=lambda n: f'{n/1000:,.0f}k'
print('figures', pts_today, pts_desk, gross, fee_y, net, cashback)

fosite.TICK_FONT = HERO_FONTS   # this page needs DM Serif/DM Sans (hero fonts already include JetBrains Mono); shared file untouched

HERO_PH=['bg-0%d'%k for k in range(1,9)]+['d-'+n for n in ['lisbon','santorini','maldives','kyoto','bali','paris','cabo','iceland','costarica','alps','rome','barcelona','dubai','nyc','connemara']]
CHEV='img/fo-chevron-transparent-v2.png'
LOGO=lambda n: 'img/hero/prog/'+n+'.jpg'

subs=[p.strip() for p in HERO_SUB.split('\n\n')]
sub_html=''.join(f'<p>{p}</p>' for p in subs[:-1])+f'<p class="tag">{subs[-1]}</p>'
CTAS=lambda c='': f'<div class="pctas {c}"><a class="c1" href="book.html?from=index">Get your desk</a><a class="c2" href="how.html">See how it works</a></div>'

hero=f'''<section id="top" class="phero">{ph(HERO_PH,6000)}<div class="pw">
<div class="kick"><span class="ld"></span>Earn · Burn · Return · Learn</div>
<h1>You are not bad at Points &amp; Miles.<br>You are just <span>outnumbered.</span></h1>
<div class="sub">{sub_html}</div>
<div class="deskk"><span class="lv"></span><span><b>First Officer's specialists</b> · 50+ programs, trained on new data nightly</span></div>
</div></section>'''

def beat(n, t, em=''):
    return f'<h2 class="beat"><span class="n">{n}</span><span>{t}{f" <em>{em}</em>" if em else ""}</span></h2>'

CARD_SVG='<svg viewBox="0 0 20 14" aria-hidden="true"><rect x=".75" y=".75" width="18.5" height="12.5" rx="2.2" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M1 4.6h18" stroke="currentColor" stroke-width="1.3"/></svg>'
dossier=f'''<article class="dos" aria-label="Example owner dossier, fictional">
<div class="dh"><span class="av">DI</span><div><div class="nm">Darnell</div><div class="bz">Ironwood Strength Club · Chicago, IL</div></div></div>
<div class="dpill"><span>Bespoke strategy</span><b>D-IW-0412</b></div>
<div class="rw"><span>Desk dossier</span><div><b>5 of 50+</b> programs tracked</div></div>
<div class="rw"><span>Cards on file</span><div class="cds"><i>{CARD_SVG}United business card</i><i>{CARD_SVG}Office-category card</i></div></div>
<div class="rw"><span>Card spend</span><div><b>${K(SPEND)} a year</b> <em class="etag">est.</em><small>Equipment, ads, utilities</small></div></div>
<div class="rw"><span>Points a year</span><div><b>{K(pts_today)}</b> today <span class="ar">→</span> <b class="e">{K(pts_desk)}</b> with the desk <em class="etag">est.</em><small>About {TODAY_X:g}x today, about {DESK_X:g}x with the desk, est.</small></div></div>
<div class="rw"><span>Worth a year</span><div><b class="r">≈ ${net:,}</b> after the fee <em class="etag">est.</em><small>vs ≈ ${cashback:,} at 2% cash back, est.</small></div></div>
<div class="rw"><span>Next trip</span><div><b>Chicago weekend with the kids on Hyatt points</b><small>2¢+ a point, est.</small></div></div>
<div class="rw"><span>Requests</span><ul class="rq"><li><i class="dt on"></i>Save Hyatt points from expiring<em>On it</em></li><li><i class="dt"></i>Weekend away with the kids</li><li><i class="dt"></i>Internet to 5x</li></ul></div>
<div class="fn">Example owner. Fictional details. Figures are estimates.</div>
</article>
<details class="math" open><summary>How we got to ${net:,}, est.</summary>
<ol><li>${SPEND:,} a year on cards × about {DESK_X:g}x = about {pts_desk:,} points, est. Today, at {TODAY_X:g}x: {pts_today:,}.</li>
<li>{pts_desk:,} points × {UTIL:.0%} redeemed × {CPP*100:g}¢ a point = about ${gross:,} in travel value, est.</li>
<li>Less the flat ${FEE_M} a month (${fee_y:,} a year) = about ${net:,}, est.</li>
<li>The same ${SPEND:,} at 2% cash back = about ${cashback:,}, est.</li></ol>
<p>Illustrative. Earning rates, caps and point values vary by card and program.</p></details>'''

# ---------------- step 2: the desk, live (one SVG, exact geometry) ----------------
# Every specialist sits in its ring at low opacity. One at a time, a contributing specialist comes up
# (forward toward First Officer, full opacity), a thin line draws edge-to-edge and a pulse runs out and back,
# then it settles back to its place at low opacity. Static state (no JS / reduced motion): Darnell's five up.
W,Hh=390,392; CX,CY=195,192
RL=19                                   # logo circle radius (border stroke centre at RL+1.5)
RC=24                                   # First Officer circle radius, ~25% larger than a logo circle
RIN,NIN=108,12; ROUT,NOUT=163,20        # two calm rings, 32 of the 50+ shown
UP=1.08                                 # scale when a specialist comes up
DARN={'12-hyatt':'Hyatt','02-chase':'Chase','17-united':'United','11-ihg':'IHG','20-southwest':'Southwest'}
# inner-ring slot (index 0 = top, clockwise) for Darnell's programs: upper and side sectors, clear of the label below FO
SLOT={'12-hyatt':0,'02-chase':2,'20-southwest':3,'11-ihg':9,'17-united':10}
NAMES={'01-amex':'Amex','05-bilt':'Bilt','09-marriott':'Marriott','10-hilton':'Hilton','25-aeroplan':'Aeroplan','26-flying-blue':'Flying Blue',
       '18-delta':'Delta','19-american':'American','03-capital-one':'Capital One','04-citi':'Citi','27-british-airways':'British Airways','32-singapore':'Singapore'}
allp=sorted(f[:-4] for f in os.listdir(os.path.join(ROOT,'img/hero/prog')) if f.endswith('.jpg'))
rest=[p for p in allp if p not in DARN]
inner=[None]*NIN
for p,s in SLOT.items(): inner[s]=p
fill=iter(rest)
for i in range(NIN):
    if inner[i] is None: inner[i]=next(fill)
outer=[next(fill) for _ in range(NOUT)]
geo={}                                  # id -> (ring centre x,y, unit vector, forward distance)
for i,p in enumerate(inner):
    a=-math.pi/2+i*2*math.pi/NIN; geo[p]=(CX+RIN*math.cos(a),CY+RIN*math.sin(a),math.cos(a),math.sin(a),14)
for i,p in enumerate(outer):
    a=-math.pi/2+(i+.5)*2*math.pi/NOUT; geo[p]=(CX+ROUT*math.cos(a),CY+ROUT*math.sin(a),math.cos(a),math.sin(a),22)
# rotation: Darnell's five, with a few others from the 50+ between them; none sits in the bottom sector (label)
ROT=['02-chase','01-amex','12-hyatt','17-united','25-aeroplan','11-ihg','20-southwest','09-marriott']
for p in ROT: assert p in geo and geo[p][3] < .82, p
names={**NAMES,**DARN}
defs=[];logos=[]
for p,(x,y,ux,uy,fwd) in geo.items():
    k=p.split('-',1)[0]
    defs.append(f'<clipPath id="c{k}"><circle r="{RL}"/></clipPath>')
    nm=names.get(p,'')
    lab=(f'<text class="nm" y="{RL+15}" text-anchor="middle">{nm}</text>') if nm and p in ROT else ''
    dark=' dk' if p in DARN else ''
    logos.append(f'<g transform="translate({x:.2f} {y:.2f})"><g class="sp{dark}" data-p="{p}" style="--dx:{-ux*fwd:.2f}px;--dy:{-uy*fwd:.2f}px">'
                 f'<circle r="{RL+1.5}" fill="#fff"/><image href="{LOGO(p)}" x="{-RL}" y="{-RL}" width="{2*RL}" height="{2*RL}" clip-path="url(#c{k})" preserveAspectRatio="xMidYMid slice"/>'
                 f'<circle class="bd" r="{RL+1.5}" fill="none" stroke-width="1"/>{lab}</g></g>')
CH=30
fo=(f'<g class="fo"><circle cx="{CX}" cy="{CY}" r="{RC}" fill="#fff" stroke="#FA1896" stroke-width="1.5"/><circle class="halo" cx="{CX}" cy="{CY}" r="{RC}" fill="none" stroke="#FA1896" stroke-width="1"/>'
    f'<image href="{CHEV}" x="{CX-CH/2}" y="{CY-CH/2+1}" width="{CH}" height="{CH}" preserveAspectRatio="xMidYMid meet"/></g>')
desk_svg=(f'<svg class="net still" id="deskNet" viewBox="0 0 {W} {Hh}" role="img" aria-label="First Officer at the desk, working with the specialists for Darnell\'s programs: Hyatt, Chase, United, IHG and Southwest, inside a desk that covers 50+ programs">'
          f'<defs>{"".join(defs)}</defs>{"".join(logos)}{fo}</svg>')
desk=f'''<div class="deskwrap">{desk_svg}<div class="fol" style="top:{(CY+RC+6)/Hh*100:.2f}%"><b>First Officer</b><span>At the Desk</span></div></div>
<p class="cap2">The specialists for his programs light up. The rest of the 50+ stay on watch.</p>'''
DESK_JS='''<script>(function(){var s=document.getElementById('deskNet');if(!s)return;
if(matchMedia('(prefers-reduced-motion: reduce)').matches||!s.animate)return;
var ROT=%s,i=0,T=3200,run=false,tm=null;
function q(sel){return s.querySelector(sel)}
function beat(){var p=ROT[i%%ROT.length];i++;var g=q('.sp[data-p="'+p+'"]');if(!g)return;
 var w=g.parentNode;s.insertBefore(w,q('.fo'));g.getBoundingClientRect();g.classList.add('on');
 q('.halo').animate([{opacity:0,transform:'scale(1)'},{opacity:.5,offset:.3},{opacity:0,transform:'scale(1.35)'}],{duration:900,delay:1100,easing:'ease-out'});
 setTimeout(function(){g.classList.remove('on')},2850);}
function loop(){if(!run)return;beat();tm=setTimeout(loop,T)}
function start(){if(run)return;run=true;s.classList.remove('still');tm=setTimeout(loop,400)}
function stop(){run=false;clearTimeout(tm)}
if('IntersectionObserver'in window){new IntersectionObserver(function(e){e[0].isIntersecting?start():stop()},{threshold:.15}).observe(s)}else start();
})();</script>'''%json.dumps(ROT)

# ---------------- step 3: the app ----------------
TH=[('o','I have Hyatt points from years ago. Are they still good?'),
    ('f','Let us check before anything expires. When did you last earn or use them?'),
    ('o','A trip in 2024, I think.'),
    ('f','Hyatt points expire after 24 months with no activity. Yours may be close.'),
    ('o','Oh no. How many do I have?'),
    ('f','The app shows about 38,000. That is a nice weekend, so let us use them.'),
    ('o','A Chicago weekend with the kids?'),
    ('f','Smart. That typically covers 2 nights at a nice downtown Chicago Hyatt, est. A weekend in March?'),
    ('o','Yes please!'),
    ('f','Requirements vetted: 2 nights, a March weekend, downtown, one room for 2 adults and 2 kids. The desk takes it from there once you approve.'),
    ('o','💪')]
def bub(w,t,last):
    av=f'<img class="av" src="{CHEV}" alt="">' if w=='f' else ''
    return f'<div class="mm {w}">{av}<div class="b6">{t}</div></div>'+('<div class="rd">Read 9:41 PM</div>' if last else '')
TABI={'Home':'<path d="M3 9.5 10 4l7 5.5V16a1 1 0 0 1-1 1h-3.5v-4.5h-5V17H4a1 1 0 0 1-1-1z"/>',
      'Earn':'<circle cx="10" cy="10" r="6.5"/><path d="M10 6.5v7M7.8 8.4c0-1 1-1.6 2.2-1.6s2.2.6 2.2 1.6-1 1.4-2.2 1.6-2.2.6-2.2 1.6 1 1.6 2.2 1.6 2.2-.6 2.2-1.6"/>',
      'Burn':'<path d="M3 11.5 17 5l-3.2 11-3.3-3.8L6 15.5V12z"/>',
      'Return':'<path d="M4 8h10.5a2.5 2.5 0 0 1 0 5H8M7 5 4 8l3 3"/>',
      'Learn':'<path d="M2.5 7.5 10 4l7.5 3.5L10 11z"/><path d="M5.5 9v3.6c1.3 1 2.8 1.4 4.5 1.4s3.2-.4 4.5-1.4V9"/>'}
tabs=''.join(f'<span class="{("on" if n=="Learn" else "")}"><svg viewBox="0 0 20 20" aria-hidden="true">{p}</svg>{n}</span>' for n,p in TABI.items())
phone=f'''<div class="iph" role="img" aria-label="Example chat in the First Officer app between Darnell and First Officer about Hyatt points, fictional">
<div class="scr"><div class="isl"></div><div class="sb"><b>9:41</b><span class="sig"><i></i><i></i><i></i><i></i></span></div>
<div class="tb"><img src="{CHEV}" alt=""><b>First Officer</b><span class="me">DI</span></div>
<div class="seg"><span class="on">First Officer</span><span>Behind the desk</span></div>
<div class="th"><div class="day">Today 9:38 PM</div>{''.join(bub(w,t,i==len(TH)-1) for i,(w,t) in enumerate(TH))}</div>
<div class="cmp6"><span>Message First Officer</span><i></i></div>
<div class="tabs">{tabs}</div><div class="hb"></div></div></div>'''

MICRO='Illustrative example. Owners and chats are fictional. Figures are estimates, not guarantees. Not affiliated with any bank, airline or hotel program.'
TMK='Program names and logos are trademarks of their respective owners, shown for identification only. No endorsement is implied. Award availability, pricing and transfer terms are set by each program and can change without notice.'

steps=f'''<section class="psteps"><div class="pw">
<div class="st s1"><div class="tx">{beat(1,'Meet Darnell')}<p class="lede2">He runs a gym in Chicago. His cards earn about 1x on ${K(SPEND)} a year, est. His points sit where he left them.</p>{CTAS('d')}</div>
<div class="vis">{dossier}{CTAS('m')}</div></div>
<div class="st s2"><div class="tx">{beat(2,'His desk')}<p class="lede2">First Officer runs his account and briefs the specialist for each of his programs. Each one knows its program's rules, partners and fine print.</p></div>
<div class="vis">{desk}</div></div>
<div class="st s3"><div class="tx">{beat(3,'What Darnell sees','in the app')}<p class="lede2">One thread. First Officer brings back what the desk learned, in plain words. Every decision stays his.</p>{CTAS('d')}</div>
<div class="vis">{phone}{CTAS('m')}</div></div>
<div class="fine"><p>{MICRO} <a href="#imp">Important information</a></p><p>{TMK}</p></div>
</div></section>'''

stats='''<section class="pstats" id="terms"><div class="pw"><div class="sg">
<div><div class="v">$550</div><div class="k">Flat monthly · Cancel anytime</div></div>
<div><div class="v">20 min</div><div class="k">The Found Money Call, free · We size your capture first</div></div>
<div><div class="v">Friday</div><div class="k">Dollars saved reported every Friday</div></div>
<div><div class="v">Yours</div><div class="k">Every decision, always</div></div>
</div></div></section>'''

CSS='''<style>
/* home-persona: mobile-first, page-scoped. Shared tokens untouched. */
.phero,.psteps,.pstats{--ink:#141216;--body:#3d3843;--mute:#6f6977;font-family:'DM Sans',system-ui,sans-serif}
.pw{max-width:1120px;margin:0 auto;padding:0 18px}
#top.phero{padding:0!important}
.phero .pw{position:relative;z-index:2;padding-top:26px;padding-bottom:30px;text-align:left}
.kick{display:flex;width:max-content;margin:0 auto 22px;align-items:center;gap:9px;font:700 12px 'DM Sans',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#e60f86;background:rgba(250,24,150,.08);border:1px solid rgba(250,24,150,.22);border-radius:999px;padding:8px 15px}
.kick .ld{width:7px;height:7px;border-radius:50%;background:#FA1896}
.phero h1{font:400 32px/1.06 'DM Serif Display',Georgia,serif;letter-spacing:-.022em;color:var(--ink);margin:0 0 16px}
.phero h1 span{color:#e60f86}
.phero .sub p{font:400 15.5px/1.6 'DM Sans',sans-serif;color:var(--body);margin:0 0 12px}
.phero .sub p.tag{font-weight:700;font-size:17.5px;line-height:1.4;color:var(--ink);margin:16px 0 0;max-width:20em}
.deskk{display:flex;gap:9px;align-items:center;margin:22px auto 0;width:max-content;max-width:100%;background:#fff;border-radius:999px;padding:7px 14px;box-shadow:0 0 0 1px rgba(20,18,22,.08),0 6px 16px -10px rgba(20,18,22,.3);font:500 12.5px/1.35 'DM Sans',sans-serif;color:var(--body)}
.deskk b{color:var(--ink)}
.lv{width:8px;height:8px;border-radius:50%;background:#16A06A;flex:none;box-shadow:0 0 0 3px rgba(22,160,106,.16)}
.psteps{background:#fff;padding:26px 0 8px}
.st{margin:0 0 34px}
.beat{display:flex;gap:11px;align-items:center;font:700 20px/1.2 'DM Sans',sans-serif;color:var(--ink);margin:0 0 8px;letter-spacing:-.01em}
.beat .n{width:28px;height:28px;border-radius:50%;background:#FA1896;color:#fff;font:700 14px/28px 'DM Sans',sans-serif;text-align:center;flex:none}
.beat em{font:500 13px 'DM Sans',sans-serif;color:var(--mute);font-style:normal;white-space:nowrap}
.lede2{font:400 15px/1.55 'DM Sans',sans-serif;color:var(--body);margin:0 0 16px}
.pctas{display:flex;gap:10px;margin:18px 0 0}
.pctas a{flex:1;text-align:center;text-decoration:none;font:700 15px/1 'DM Sans',sans-serif;padding:15px 12px;border-radius:999px;white-space:nowrap}
.pctas .c1{background:#FA1896;color:#fff;box-shadow:0 10px 24px -12px rgba(250,24,150,.7)}
.pctas .c2{background:#fff;color:var(--ink);box-shadow:0 0 0 1px rgba(20,18,22,.14)}
.pctas.d{display:none}
.s1 .vis{margin-top:6px}
/* dossier */
.dos{background:#fff;border-radius:22px;padding:18px 18px 14px;box-shadow:0 0 0 1.5px #e3dcf6,0 18px 40px -26px rgba(20,18,22,.35)}
.dh{display:flex;gap:12px;align-items:center}
.dh .av{width:46px;height:46px;border-radius:50%;background:#efe9ff;color:#5b3bb8;font:800 15px/46px 'DM Sans',sans-serif;text-align:center;flex:none}
.dh .nm{font:800 19px/1.15 'DM Sans',sans-serif;color:var(--ink)}
.dh .bz{font:500 12.5px/1.3 'DM Sans',sans-serif;color:var(--mute);margin-top:2px}
.dos .dpill{display:flex;justify-content:space-between;align-items:center;margin:14px 0 6px;background:#f6f3fb;border-radius:12px;padding:9px 12px;font:600 12.5px 'DM Sans',sans-serif;color:var(--body)}
.dos .dpill b{font:600 12px 'JetBrains Mono',monospace;letter-spacing:.04em;color:var(--ink)}
.rw{display:grid;grid-template-columns:96px 1fr;gap:10px;padding:10px 0;border-top:1px solid #f0edf2;font:400 13px/1.4 'DM Sans',sans-serif;color:var(--body)}
.rw:first-of-type{border-top:0}
.rw>span{color:var(--mute);font-weight:500;font-size:12.5px}
.rw b{color:var(--ink);font-weight:700}
.rw b.e{color:#12834E}.rw b.r{color:#7149C9}
.rw .ar{color:var(--mute);margin:0 2px}
.rw small{display:block;font-size:12px;color:var(--mute);margin-top:2px}
.etag{font:600 10.5px/1 'DM Sans',sans-serif;font-style:normal;color:#6f6977;background:#efedf1;border-radius:5px;padding:2px 5px 2px;vertical-align:1px;white-space:nowrap}
.cds{display:flex;flex-wrap:wrap;gap:6px}
.cds i{font-style:normal;display:inline-flex;align-items:center;gap:6px;background:#f5f3f7;border-radius:8px;padding:4px 8px;font-size:12px;color:var(--ink)}
.cds svg{width:15px;height:11px;color:#7149C9}
.rq{list-style:none;margin:0;padding:0}
.rq li{display:flex;align-items:center;gap:8px;padding:1px 0}
.rq em{font-style:normal;margin-left:auto;font:600 11px 'DM Sans',sans-serif;color:#1E78B8;background:#e4f3fd;border-radius:999px;padding:2px 8px;white-space:nowrap}
.dt{width:7px;height:7px;border-radius:50%;box-shadow:inset 0 0 0 1.5px #c9c3cf;flex:none}.dt.on{background:#1E78B8;box-shadow:none}
.fn{font:500 11px/1.4 'DM Sans',sans-serif;color:#8a8492;border-top:1px solid #f0edf2;padding-top:10px;margin-top:2px}
.math{margin:12px 2px 0;font:400 13px/1.5 'DM Sans',sans-serif;color:var(--body)}
.math summary{cursor:pointer;font-weight:700;color:var(--ink);list-style:none;display:flex;align-items:center;gap:8px}
.math summary::-webkit-details-marker{display:none}
.math summary::after{content:"";width:7px;height:7px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px)}
.math[open] summary::after{transform:rotate(-135deg)}
.math ol{margin:10px 0 6px;padding-left:18px}.math li{margin:3px 0}
.math p{font-size:11.5px;color:#8a8492;margin:0}
/* desk */
.deskwrap{position:relative;max-width:420px;margin:4px auto 0}
.net{display:block;width:100%;height:auto;overflow:visible}
.net .sp{opacity:.24;transform:translate(0,0) scale(.94);transform-origin:0 0;transition:transform 1.1s cubic-bezier(.4,0,.2,1),opacity 1.1s cubic-bezier(.4,0,.2,1)}
.net .sp .bd{stroke:#e2dde6}
.net .sp.on,.net.still .sp.dk{opacity:1;transform:translate(var(--dx),var(--dy)) scale(1.08)}
.net .sp.on .bd,.net.still .sp.dk .bd{stroke:#FA1896}
.net text.nm{font:700 11px 'DM Sans',sans-serif;fill:#141216;opacity:0;transition:opacity .6s ease;paint-order:stroke;stroke:#fff;stroke-width:3px;stroke-linejoin:round}
.net .sp.on text.nm{opacity:1}
.net .halo{opacity:0;transform-box:fill-box;transform-origin:center}
@media (prefers-reduced-motion:reduce){.net .sp,.net text.nm{transition:none}}
.fol{position:absolute;left:50%;transform:translateX(-50%);background:#fff;border-radius:999px;padding:5px 12px 6px;box-shadow:0 0 0 1.5px #FA1896;text-align:center;line-height:1.15;white-space:nowrap}
.fol b{display:block;font:700 12.5px 'DM Sans',sans-serif;color:#d40f7d}.fol span{display:block;font:500 10.5px 'DM Sans',sans-serif;color:#9a4f78}
.cap2{font:500 12.5px/1.5 'DM Sans',sans-serif;color:var(--mute);text-align:center;margin:6px auto 0;max-width:30em}
/* phone */
.s3 .vis{position:relative;display:flex;flex-direction:column;align-items:center}.s3 .vis .pctas{align-self:stretch}
.iph{width:318px;border-radius:52px;background:#0c0c0e;padding:11px;box-shadow:0 0 0 1px #2a2a2e,0 30px 60px -30px rgba(20,18,22,.55)}
.scr{position:relative;border-radius:42px;background:#fff;overflow:hidden;height:640px;display:flex;flex-direction:column}
.isl{position:absolute;top:10px;left:50%;transform:translateX(-50%);width:92px;height:26px;border-radius:20px;background:#0c0c0e;z-index:3}
.sb{display:flex;justify-content:space-between;align-items:center;padding:14px 26px 0;height:40px;font:600 14px -apple-system,'DM Sans',sans-serif;color:#000}
.sig{display:flex;gap:2px;align-items:flex-end}.sig i{width:3px;background:#000;border-radius:1px}.sig i:nth-child(1){height:4px}.sig i:nth-child(2){height:6px}.sig i:nth-child(3){height:8px}.sig i:nth-child(4){height:10px}
.tb{display:flex;align-items:center;gap:8px;padding:8px 16px 8px;border-bottom:1px solid #f0edf2}
.tb img{width:24px;height:24px;object-fit:contain}.tb b{font:700 15px 'DM Sans',sans-serif;color:#141216}
.tb .me{margin-left:auto;width:28px;height:28px;border-radius:50%;background:#efe9ff;color:#5b3bb8;font:800 11px/28px 'DM Sans',sans-serif;text-align:center}
.seg{display:flex;margin:8px 14px 0;background:#f2f0f4;border-radius:10px;padding:3px;font:600 12px 'DM Sans',sans-serif;color:#6f6977}
.seg span{flex:1;text-align:center;padding:6px 0;border-radius:8px}.seg .on{background:#fff;color:#141216;box-shadow:0 1px 3px rgba(20,18,22,.12)}
.th{flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding:0 12px 6px;overflow:hidden;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 60px);mask-image:linear-gradient(180deg,transparent 0,#000 60px)}
.day{text-align:center;font:600 11px 'DM Sans',sans-serif;color:#8a8492;margin:0 0 6px}
.mm{display:flex;gap:7px;align-items:flex-end;margin:4px 0}
.mm .av{width:22px;height:22px;object-fit:contain;flex:none}
.mm.o{justify-content:flex-end}
.b6{border-radius:18px;padding:8px 12px;font:400 14px/1.32 -apple-system,'SF Pro Text','DM Sans',sans-serif;letter-spacing:-.01em;max-width:80%}
.mm.o .b6{background:#e9e9eb;color:#141216;border-bottom-right-radius:6px}
.mm.f .b6{background:#FA1896;color:#fff;border-bottom-left-radius:6px}
.rd{text-align:right;font:500 10.5px 'DM Sans',sans-serif;color:#8a8492;margin:2px 2px 0}
.cmp6{display:flex;align-items:center;margin:4px 12px 8px;border-radius:999px;box-shadow:inset 0 0 0 1px #e2dde6;padding:8px 8px 8px 14px;font:400 13px 'DM Sans',sans-serif;color:#9a95a0}
.cmp6 i{margin-left:auto;width:24px;height:24px;border-radius:50%;background:#FA1896;position:relative}
.cmp6 i::after{content:"";position:absolute;left:8.5px;top:9px;width:6px;height:6px;border-left:1.6px solid #fff;border-top:1.6px solid #fff;transform:rotate(45deg)}
.tabs{display:flex;justify-content:space-around;border-top:1px solid #f0edf2;padding:7px 6px 0;font:600 10px 'DM Sans',sans-serif;color:#8a8492}
.tabs span{display:flex;flex-direction:column;align-items:center;gap:3px}
.tabs svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linejoin:round;stroke-linecap:round}
.tabs .on{color:#1E78B8}
.hb{width:110px;height:4px;border-radius:3px;background:#141216;margin:10px auto 8px}
.fine{border-top:1px solid #f0edf2;padding:16px 0 4px;margin-top:6px}
.fine p{font:400 11.5px/1.5 'DM Sans',sans-serif;color:#8a8492;margin:0 0 8px}.fine a{color:#6f6977}
/* stats */
.pstats{background:#fff;padding:10px 0 34px}
.sg{display:grid;grid-template-columns:1fr 1fr;border-radius:22px;background:#fff;box-shadow:0 0 0 1px rgba(20,18,22,.09),0 18px 40px -30px rgba(20,18,22,.35);overflow:hidden}
.sg>div{padding:20px 16px 18px}
.sg>div:nth-child(odd){border-right:1px solid #f0edf2}.sg>div:nth-child(-n+2){border-bottom:1px solid #f0edf2}
.sg .v{font:400 34px/1 'DM Serif Display',Georgia,serif;color:#141216;letter-spacing:-.01em}
.sg .k{font:500 12.5px/1.4 'DM Sans',sans-serif;color:#6f6977;margin-top:8px}
@media(min-width:760px){.phero h1{font-size:46px}.phero .pw{padding-top:44px;padding-bottom:48px}.phero .sub{max-width:620px}.kick,.deskk{margin-left:0}}
@media(min-width:980px){
 .pw{padding:0 32px}
 .phero h1{font-size:58px}
 .phero .pw{padding-top:64px;padding-bottom:64px}
 .psteps{padding:56px 0 20px}
 .st{display:grid;grid-template-columns:minmax(0,400px) minmax(0,1fr);gap:72px;align-items:center;margin:0 0 72px}
 .st .tx{align-self:center}
 .pctas.d{display:flex}.pctas.m{display:none}
 .beat{font-size:26px}.beat .n{width:34px;height:34px;line-height:34px;font-size:16px}
 .lede2{font-size:17px}
 .pctas{max-width:400px}
 .st .vis{max-width:540px;width:100%;justify-self:center}
 .deskwrap{max-width:540px}
 .iph{width:340px}.scr{height:680px}
 .sg{grid-template-columns:repeat(4,1fr)}.sg>div{border-bottom:0!important;border-right:1px solid #f0edf2;padding:26px 24px}.sg>div:last-child{border-right:0}
 .sg .v{font-size:44px}
 .pstats{padding:10px 0 64px}
}
</style>'''

body=CSS+hero+steps+stats
page('home-persona.html','First Officer · Meet Darnell (mockup)',body,
     desc='Mobile-first persona homepage mockup. Fictional owner, estimated figures.',src='home',tail=DESK_JS)
