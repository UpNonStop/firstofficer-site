"""Five variations of step 2 'His desk' on the persona homepage (Darnell, fictional).
No connector lines anywhere. Specialists keep thinking (3-dot typing), then respond and contribute to First Officer.
Run: python3 _build/desk_vars.py  ->  rebuild-v3/desk-var-1.html ... desk-var-5.html + desk-variations.html"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fosite
from fosite import *

fosite.TICK_FONT = HERO_FONTS          # DM Serif / DM Sans, as on home-persona.html; shared file untouched
CHEV = 'img/fo-chevron-transparent-v2.png'
FILES = {int(f[:2]): f for f in sorted(os.listdir(os.path.join(ROOT, 'img/hero/prog'))) if f.endswith('.jpg')}
NAME = {1:"Amex",2:"Chase",3:"Capital One",4:"Citi",5:"Bilt",6:"Wells Fargo",7:"Bank of America",8:"U.S. Bank",9:"Marriott",10:"Hilton",11:"IHG",12:"Hyatt",13:"Accor",14:"Wyndham",15:"Choice",16:"Radisson",17:"United",18:"Delta",19:"American",20:"Southwest",21:"JetBlue",22:"Frontier",23:"Allegiant",24:"Atmos Rewards",25:"Aeroplan",26:"Flying Blue",27:"British Airways",28:"Iberia",29:"Aer Lingus",30:"Qatar Airways",31:"Emirates",32:"Singapore",33:"Cathay",34:"Etihad",35:"Turkish",36:"LifeMiles",37:"ANA",38:"EVA Air",39:"Qantas",40:"Air New Zealand",41:"Virgin Australia",42:"Finnair",43:"SAS",44:"Air India",45:"Korean Air",46:"LATAM",47:"Virgin Atlantic",48:"TAP Air Portugal",49:"Aeromexico",50:"JAL"}
LOGO = lambda n: 'img/hero/prog/' + FILES[n]
DARN = [12, 2, 17, 11, 20]             # Hyatt, Chase, United, IHG, Southwest
PC = {'Earn':'#12834E','Burn':'#E8590C','Return':'#7149C9','Learn':'#1E78B8'}
PILLARS = ['Earn','Burn','Return','Learn']
GROUPS = [('Banks', list(range(1,9))), ('Hotels', list(range(9,17))), ('US airlines', list(range(17,25))), ('Partner airlines', list(range(25,51)))]
CAT = {n: g for g, ids in GROUPS for n in ids}
AMB = {'Banks':['Watching bonuses','Updating rules','Card offers scan','Spend cap watch','Transfer ratios','Logging posts'],
       'Hotels':['Award chart check','Logging stays','Cash rate compare','Nightly data sync','Free night rules'],
       'US airlines':['Partner awards','Logging miles','Surcharge check','Fare rules','Nightly data sync'],
       'Partner airlines':['Partner awards','Surcharge check','Routing rules','Updating rules','Transfer ratios']}
E = '<em class="etag">est.</em>'
# Darnell's contributions, in loop order (n, pillar, thinking label, short, full text html). Plain, customer-facing, no booking, no availability.
CON = [
 (2,'Earn','Category review','Internet to 5x','Internet and phone bills can earn 5x on an office-category card, on the first $25k a year.'),
 (12,'Learn','Expiry check','Points kept active','Hyatt points expire after 24 months with no activity. One small earn or stay resets the clock.'),
 (2,'Burn','Transfer math','1:1 to Hyatt','Chase points move 1:1 to Hyatt, so his Chase balance can top up a Chicago weekend.'),
 (11,'Return','4th night math','4th night free','With the right IHG card, the 4th night of an award stay can be free. About 25% off, '+E),
 (17,'Learn','Partner rules','No expiry','United miles do not expire, so there is no rush to spend them on a weak deal.'),
 (20,'Return','Fare vs points','Fare drops','Southwest award prices follow the cash fare. If the fare drops, the points difference can come back to him.'),
 (12,'Burn','Award chart check','Chicago weekend','A downtown Chicago weekend on Hyatt points works out to about 2¢+ a point, '+E),
 (17,'Earn','Card earn check','Gas to 2x','Gas and office supplies earn 2x on his United business card, vs 1x today, '+E),
]
PLAN = ['Internet to 5x','Hyatt points kept active','Chase to Hyatt, 1:1','IHG 4th night free','United miles: no rush','Southwest fare drops','Chicago weekend on points','Gas to 2x']
FOR = ['Noted. Adding it to Darnell\'s plan.','Good. I will explain the math to Darnell in plain words.','Added. It goes in his Friday report.','Thanks. Darnell decides, I lay out the options.']
DATA = dict(names={k:v for k,v in NAME.items()}, logos={n:LOGO(n) for n in NAME}, cat=CAT, amb=AMB, darn=DARN, pc=PC,
            con=[dict(n=c[0],p=c[1],k=c[2],s=c[3],t=c[4]) for c in CON], plan=PLAN, fo=FOR, chev=CHEV)

VARS = [
 ('The floor', 'The original desk floor, restored without lines: Banks, Hotels, US airlines and Partner airlines, every specialist typing, Darnell\'s lighting up as they report to First Officer.'),
 ('Pillar lanes', 'Earn, Burn, Return and Learn as four lanes. Specialists type in their lane, then drop a short finding that First Officer collects.'),
 ('The desk feed', 'A live thread behind the desk. Specialists type, post one plain line to First Officer, and his plan fills in beside it.'),
 ('The orbit', 'A calm ring of program specialists around First Officer. One at a time a specialist comes forward with a typing bubble that turns into its finding.'),
 ('The mosaic', 'A wall of specialist tiles in quiet ambient motion, with First Officer\'s summary pinned in the middle and updating as findings land.'),
]
LEDE = 'First Officer runs his account and briefs the specialist for each of his programs. Each one knows its program\'s rules, partners and fine print.'
CAP = 'Illustrative example. Darnell is fictional. Figures are estimates, not guarantees. Program names and logos are trademarks of their owners, shown for identification only.'
WK = '<span class="wk" aria-hidden="true"><i></i><i></i><i></i></span>'
def lg(n, cls='lg'): return f'<span class="{cls}"><img src="{LOGO(n)}" alt="" loading="lazy" decoding="async"></span>'
def fo(cls='foc'): return f'<span class="{cls}"><img src="{CHEV}" alt=""></span>'

# ---------------------------------------------------------------- shared CSS / JS
BASE_CSS = '''
.dv{--ink:#141216;--body:#3d3843;--mute:#6f6977;--pink:#FA1896;font-family:'DM Sans',system-ui,sans-serif;background:#fff;padding:26px 0 40px;overflow:hidden}
.dvw{max-width:1180px;margin:0 auto;padding:0 18px}
.dvk{display:inline-flex;gap:8px;align-items:center;font:600 11px/1 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#d40f7d;background:#fff0f8;border-radius:999px;padding:7px 12px;margin:0 0 14px}
.beat{display:flex;gap:11px;align-items:center;font:700 20px/1.2 'DM Sans',sans-serif;color:var(--ink);margin:0 0 8px;letter-spacing:-.01em}
.beat .n{width:28px;height:28px;border-radius:50%;background:#FA1896;color:#fff;font:700 14px/28px 'DM Sans',sans-serif;text-align:center;flex:none}
.lede2{font:400 15px/1.55 'DM Sans',sans-serif;color:var(--body);margin:0 0 18px;max-width:36em}
.cap2{font:500 12.5px/1.5 'DM Sans',sans-serif;color:var(--mute);text-align:center;margin:16px auto 0;max-width:34em}
.dvnav{display:flex;justify-content:space-between;gap:10px;margin:26px 0 0;padding-top:16px;border-top:1px solid #f0edf2;font:600 13.5px 'DM Sans',sans-serif}
.dvnav a{color:var(--ink);text-decoration:none;padding:8px 0}.dvnav a:hover{color:#d40f7d}.dvnav .all{color:#d40f7d}
.etag{font:600 10.5px/1 'DM Sans',sans-serif;font-style:normal;color:#6f6977;background:#efedf1;border-radius:5px;padding:2px 5px;vertical-align:1px;white-space:nowrap}
/* logos and the First Officer circle (chevron on transparent, inside a thin pink ring; ~25% larger than a logo) */
.lg{--s:40px;width:var(--s);height:var(--s);border-radius:50%;background:#fff;box-shadow:0 0 0 1px #e6e1ea;display:grid;place-items:center;overflow:hidden;flex:none;transition:box-shadow .5s,transform .6s cubic-bezier(.2,.7,.2,1)}
.lg img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}
.foc{--s:50px;width:var(--s);height:var(--s);border-radius:50%;background:#fff;box-shadow:0 0 0 1.5px #FA1896;display:grid;place-items:center;flex:none;position:relative}
.foc img{width:62%;height:62%;object-fit:contain;display:block}
.foc::after{content:"";position:absolute;inset:-1px;border-radius:50%;box-shadow:0 0 0 1px #FA1896;opacity:0}
.foc.ping::after{animation:fping 1s ease-out}
@keyframes fping{0%{opacity:.6;transform:scale(1)}100%{opacity:0;transform:scale(1.4)}}
/* the 3-dot typing indicator */
.wk{display:inline-flex;gap:3px;align-items:center;height:8px}
.wk i{width:4px;height:4px;border-radius:50%;background:#bdb6c4;animation:wk 1.25s ease-in-out infinite;animation-delay:var(--d,0s)}
.wk i:nth-child(2){animation-delay:calc(var(--d,0s) + .16s)}.wk i:nth-child(3){animation-delay:calc(var(--d,0s) + .32s)}
@keyframes wk{0%,60%,100%{transform:translateY(0);opacity:.45}30%{transform:translateY(-3px);opacity:1}}
.fade{transition:opacity .28s ease,transform .28s ease}.fade.out{opacity:0;transform:translateY(4px)}
@media(min-width:980px){.dv{padding:56px 0 64px}.beat{font-size:26px}.beat .n{width:34px;height:34px;line-height:34px;font-size:16px}.lede2{font-size:17px;margin-bottom:28px}}
@media (prefers-reduced-motion:reduce){.wk i{animation:none;opacity:.7}.fade,.lg{transition:none}.foc.ping::after{animation:none}}
'''
BASE_JS = '''<script>window.DV=(function(){var D=%s;
D.RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
D.$=function(s,r){return (r||document).querySelector(s)};D.$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
D.pick=function(a){return a[Math.floor(Math.random()*a.length)]};
D.shuffle=function(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a};
/* a clock that pauses while the section is off screen */
D.clock=function(el){var vis=false,q=[];if('IntersectionObserver' in window){new IntersectionObserver(function(e){vis=e[0].isIntersecting;if(vis)q.splice(0).forEach(function(f){f()})},{threshold:.05}).observe(el)}else vis=true;
 return function(ms){return new Promise(function(r){setTimeout(function(){vis?r():q.push(r)},ms)})}};
D.swap=function(el,html){if(!el)return;if(D.RM){el.innerHTML=html;return}el.classList.add('out');setTimeout(function(){el.innerHTML=html;el.classList.remove('out')},280)};
D.ping=function(el){if(!el||D.RM)return;el.classList.remove('ping');void el.offsetWidth;el.classList.add('ping')};
D.WK='<span class="wk" aria-hidden="true"><i></i><i></i><i></i></span>';
D.lg=function(n,c){return '<span class="'+(c||'lg')+'"><img src="'+D.logos[n]+'" alt=""></span>'};
D.$$('.wk i').forEach(function(){});
return D})();
/* stagger every dot set so the room never pulses in unison */
DV.$$('.wk').forEach(function(w){w.style.setProperty('--d',(-Math.random()*1.2).toFixed(2)+'s')});
</script>''' % json.dumps(DATA)

def shell(i, css, vis, js):
    name, desc = VARS[i-1]
    prv = f'<a href="desk-var-{i-1}.html">← {i-1}. {VARS[i-2][0]}</a>' if i > 1 else '<span></span>'
    nxt = f'<a href="desk-var-{i+1}.html">{i+1}. {VARS[i][0]} →</a>' if i < 5 else '<span></span>'
    body = f'''<style>{BASE_CSS}{css}</style>
<section class="dv"><div class="dvw">
<div class="dvk">Variation {i} of 5 · {name}</div>
<h2 class="beat"><span class="n">2</span><span>His desk</span></h2>
<p class="lede2">{LEDE}</p>
{vis}
<p class="cap2">{CAP}</p>
<nav class="dvnav" aria-label="Desk variations">{prv}<a class="all" href="desk-variations.html">All five</a>{nxt}</nav>
</div></section>'''
    page(f'desk-var-{i}.html', f'First Officer · His desk, variation {i}: {name} (mockup)', body,
         desc='Mockup of the His desk step. Fictional owner, estimated figures.', src='home', tail=BASE_JS + js)

# ================================================================ 1. The floor (restored, no lines)
def var1():
    pods = ''
    for g, ids in GROUPS:
        cols = 7 if len(ids) > 8 else 2
        tiles = ''
        for k, n in enumerate(ids):
            dk = ' dk' if n in DARN else ''
            mob = ' mx' if (len(ids) > 8 and k >= 7) else ''
            tiles += f'<div class="tl{dk}{mob}" data-n="{n}">{lg(n)}<b>{NAME[n]}</b><span class="ss fade"></span>{WK}</div>'
        more = f'<div class="tl more"><span class="lg mo">+{len(ids)-7}</span></div>' if len(ids) > 8 else ''
        pods += (f'<div class="pod" data-g="{g}" style="--cols:{cols}"><div class="podh"><span class="lv"></span><span class="gl">{g}</span><span class="gs">{g.replace('Partner airlines','Partners')}</span><i>{len(ids)} working</i></div>'
                 f'<div class="tiles">{tiles}{more}</div><div class="pst fade"><b>{NAME[ids[-1]]}</b> · {AMB[g][1]}</div></div>')
    vis = f'''<div class="va" id="va">
<div class="vafo">{fo()}<div class="fol"><b>First Officer</b><span>At the Desk</span></div>
<div class="vafeed" aria-live="polite"><div class="fi fade"></div></div></div>
<div class="pods">{pods}</div></div>'''
    css = '''
.va{position:relative}
.vafo{display:flex;flex-direction:column;align-items:center;gap:10px;margin:0 0 18px}
.vafo .foc{--s:50px}
.fol{text-align:center;line-height:1.15}.fol b{display:block;font:700 13px 'DM Sans',sans-serif;color:#d40f7d}.fol span{display:block;font:500 11px 'DM Sans',sans-serif;color:#9a4f78}
.vafeed{width:100%;max-width:520px;min-height:92px;background:#fff;border-radius:16px;box-shadow:0 0 0 1.5px #FA1896,0 16px 34px -24px rgba(250,24,150,.55);padding:12px 14px}
.vafeed .wh{display:flex;align-items:center;gap:6px;font:700 12px 'DM Sans',sans-serif;color:var(--ink)}
.vafeed .wh .lg{--s:20px}.vafeed .wh em{font-style:normal;font-weight:500;color:var(--mute)}
.vafeed .wh u{text-decoration:none;margin-left:auto;font:700 10.5px 'DM Sans',sans-serif;color:#fff;background:var(--c);border-radius:999px;padding:3px 8px}
.vafeed .tx{font:400 13.5px/1.45 'DM Sans',sans-serif;color:var(--body);margin-top:6px}
.pods{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.pod{background:#faf8fb;border-radius:18px;box-shadow:inset 0 0 0 1px #eee9f1;padding:10px 10px 10px;display:flex;flex-direction:column}
.podh{display:flex;align-items:center;gap:6px;font:700 12px 'DM Sans',sans-serif;color:var(--ink);order:-1;margin:0 0 8px}
.podh i{font-style:normal;font-weight:600;color:#12834E;margin-left:auto;font-size:10.5px}
.lv{width:6px;height:6px;border-radius:50%;background:#12834E;box-shadow:0 0 0 3px rgba(18,131,78,.14)}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 4px}
.tl{display:flex;flex-direction:column;align-items:center;gap:5px;min-width:0;transition:transform .6s cubic-bezier(.2,.7,.2,1)}
.tl .lg{--s:34px}.tl b,.tl .ss{display:none}
.tl.dk .lg{box-shadow:0 0 0 1.5px #f6b5d8}
.tl.on{transform:translateY(-3px)}.tl.on .lg{box-shadow:0 0 0 2px #FA1896,0 8px 18px -8px rgba(250,24,150,.6)}
.tl.on .wk i{background:#FA1896}
.tl.mx{display:none}.lg.mo{font:700 11px 'DM Sans',sans-serif;color:var(--mute);background:#f2eff4}
.pst{margin-top:9px;min-height:34px;font:500 11.5px/1.35 'DM Sans',sans-serif;color:var(--mute);border-top:1px dashed #e6e1ea;padding-top:7px}
.pst b{color:var(--ink);font-weight:700}.pst .kk{color:var(--c);font-weight:700}
.wk2{display:none}.gl{display:none}@media(min-width:1024px){.gl{display:inline}.gs{display:none}}
@media(min-width:1024px){
 .va{display:grid;grid-template-columns:1fr;gap:0}
 .vafo{flex-direction:row;justify-content:center;gap:16px;margin-bottom:22px}
 .vafo .foc{--s:60px}.fol{text-align:left}
 .vafeed{margin-left:12px;max-width:540px}
 .pods{grid-template-columns:2fr 2fr 2fr 7fr;gap:10px}
 .pod{padding:12px 6px 10px}
 .podh{order:1;margin:10px 4px 0;font-size:12px}
 .tiles{grid-template-columns:repeat(var(--cols),1fr);gap:12px 2px}
 .tl{gap:3px}.tl .lg{--s:46px}.tl.dk .lg{--s:48px}
 .tl b{display:block;font:700 11px/1.15 'DM Sans',sans-serif;color:var(--ink);text-align:center;min-height:25px;display:flex;align-items:flex-start;justify-content:center;padding:0 2px}
 .tl .wk{height:24px;align-items:flex-start;padding-top:4px}
 .tl .ss{display:none;font:500 10px/1.2 'DM Sans',sans-serif;color:var(--mute);text-align:center;height:24px;overflow:hidden;max-width:100%;display:none;-webkit-line-clamp:2;-webkit-box-orient:vertical}
 .tl.say .ss{display:-webkit-box}.tl.say .wk{display:none}
 .tl.on .ss{color:#d40f7d;font-weight:700}
 .tl.mx{display:flex}.tl.more{display:none}
 .pst{display:none}
}
'''
    js = '''<script>(function(){var D=DV,root=document.getElementById('va');if(!root)return;var wait=D.clock(root);
var feed=D.$('.vafeed .fi',root),foc=D.$('.foc',root),T={};D.$$('.tl[data-n]',root).forEach(function(t){T[t.dataset.n]=t});
var desk=function(){return innerWidth>=1024};
function feedHtml(c){return '<div class="wh" style="--c:'+D.pc[c.p]+'">'+D.lg(c.n)+D.names[c.n]+' <em>to</em> First Officer<u>'+c.p+'</u></div><div class="tx">'+c.t+'</div>'}
function podSay(g,html,hold){var p=D.$('.pod[data-g="'+g+'"] .pst',root);if(!p)return;var now=Date.now();if(!hold&&p._h>now)return;if(hold)p._h=now+hold;D.swap(p,html)}
function say(t,txt){var s=D.$('.ss',t);if(t.classList.contains('say')){D.swap(s,txt)}else{s.textContent=txt;t.classList.add('say')}}
/* static start: a few specialists already reporting, Darnell's first finding in the feed */
var SAY=[];
feed.innerHTML=feedHtml(D.con[0]);
D.con.slice(0,5).forEach(function(c){var t=T[c.n];if(t&&!t.classList.contains('say')){D.$('.ss',t).textContent=c.s;t.classList.add('say')}});
if(D.RM)return;
D.$$('.tl.dk',root).forEach(function(t){t.classList.remove('say')});
/* ambient: some specialists show a short status, everyone else keeps typing */
function amb(){if(!desk()&&false)return;var ids=Object.keys(T).filter(function(n){return D.darn.indexOf(+n)<0});var n=D.pick(ids),t=T[n],g=D.cat[n];
 var txt=D.pick(D.amb[g]);say(t,txt);SAY.push(t);if(SAY.length>7){var o=SAY.shift();if(!o.classList.contains('on'))o.classList.remove('say')}
 podSay(g,'<b>'+D.names[n]+'</b> · '+txt)}
(async function(){for(;;){await wait(900);amb()}})();
(async function(){var i=0;await wait(700);for(;;){var c=D.con[i%D.con.length];i++;var t=T[c.n],g=D.cat[c.n];
 t.classList.remove('say');t.classList.add('on');podSay(g,'<b>'+D.names[c.n]+'</b> '+D.WK.replace('class="wk"','class="wk" style="margin-left:4px;vertical-align:1px"'),3000);
 await wait(1400);say(t,c.s);D.swap(feed,feedHtml(c));D.ping(foc);podSay(g,'<span class="kk" style="--c:'+D.pc[c.p]+'">'+c.p+'</span> · <b>'+D.names[c.n]+'</b> to First Officer: '+c.s,2600);
 await wait(1800);t.classList.remove('on');await wait(250);t.classList.remove('say');await wait(450)}})();
})();</script>'''
    shell(1, css, vis, js)

# ================================================================ 2. Pillar lanes
LANES = {'Earn':[2,17,1],'Burn':[12,2,25],'Return':[11,20,9],'Learn':[12,17,10]}
TAG = {'Earn':'More points, same spend','Burn':'Points where they go furthest','Return':'In dollars, every Friday','Learn':'The why, in plain words'}
def var2():
    lanes = ''
    first = {p: next(c for c in CON if c[1] == p) for p in PILLARS}
    for p in PILLARS:
        rows = ''.join(f'<div class="rw" data-n="{n}">{lg(n)}<span class="rn"><b>{NAME[n]}</b><span class="rs fade">{AMB[CAT[n]][k]}</span></span>{WK}</div>' for k, n in enumerate(LANES[p]))
        c = first[p]
        lanes += (f'<div class="lane" data-p="{p}" style="--c:{PC[p]}"><div class="lnh"><span class="pp">{p}</span><span class="tgl">{TAG[p]}</span></div>'
                  f'<div class="rws">{rows}</div><div class="chp"><div class="fi fade"><span class="cto">{NAME[c[0]]} → First Officer</span><span class="cct">{c[4]}</span></div></div></div>')
    cnt = ''.join(f'<span class="pc" data-p="{p}" style="--c:{PC[p]}"><i></i>{p} <b>{[c[1] for c in CON].count(p)}</b></span>' for p in PILLARS)
    vis = f'''<div class="vb" id="vb">
<div class="fos">{fo()}<div class="fot"><b>First Officer</b><span class="fos2">Darnell: <b class="tot">8</b> findings this week</span></div><div class="pcs">{cnt}</div></div>
<div class="lns">{lanes}</div></div>'''
    css = '''
.fos{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;align-items:center;background:#fff;border-radius:18px;box-shadow:0 0 0 1.5px #FA1896,0 18px 36px -28px rgba(250,24,150,.6);padding:12px 14px;margin:0 0 14px}
.fos .foc{--s:50px}
.fot b{display:block;font:700 15px 'DM Sans',sans-serif;color:var(--ink)}.fot span{display:block;font:500 12.5px/1.35 'DM Sans',sans-serif;color:var(--mute)}.fot .tot{display:inline;font-size:12.5px;color:#d40f7d}
.pcs{display:flex;flex-wrap:wrap;gap:6px 12px;grid-column:1/-1;border-top:1px solid #f6e3ee;padding-top:9px;justify-content:space-between}.pc{display:inline-flex;align-items:center;gap:5px;font:600 11.5px 'DM Sans',sans-serif;color:var(--body)}
.pc i{width:7px;height:7px;border-radius:50%;background:var(--c)}.pc b{color:var(--ink);transition:color .3s}.pc.up b{color:var(--c)}
.lns{display:grid;gap:10px}
.lane{background:#faf8fb;border-radius:18px;box-shadow:inset 0 0 0 1px #eee9f1;padding:12px 12px 12px 15px;position:relative;overflow:hidden;transition:box-shadow .4s}
.lane::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--c);opacity:.85}
.lnh{display:flex;align-items:center;gap:8px;margin:0 0 10px}
.pp{font:700 11.5px/1 'DM Sans',sans-serif;color:#fff;background:var(--c);border-radius:999px;padding:5px 10px}
.tgl{font:500 12.5px 'DM Sans',sans-serif;color:var(--mute)}
.rws{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.rw{display:flex;flex-direction:column;align-items:center;gap:5px;min-width:0;transition:transform .5s}
.rw .lg{--s:40px}.rn{display:none}
.rw.on{transform:translateY(-2px)}.rw.on .lg{box-shadow:0 0 0 2px var(--c),0 8px 16px -8px var(--c)}.rw.on .wk i{background:var(--c)}
.chp{margin-top:10px;background:#fff;border-radius:12px;box-shadow:0 0 0 1px #ece7ef;padding:9px 11px;min-height:80px}
.cto{display:block;font:700 11px 'DM Sans',sans-serif;color:var(--c);margin:0 0 3px}
.cct{display:block;font:400 13px/1.42 'DM Sans',sans-serif;color:var(--body)}
.chp .wk i{background:var(--c)}
.lane.hot{box-shadow:inset 0 0 0 1px var(--c)}
@media(min-width:1024px){
 .fos{grid-template-columns:auto auto 1fr;padding:14px 18px;gap:16px;margin-bottom:16px}.fos .foc{--s:60px;grid-row:auto}.pcs{justify-content:flex-end;gap:16px;grid-column:auto;border:0;padding:0}.pc{font-size:12.5px}
 .lns{grid-template-columns:repeat(4,1fr);gap:12px}
 .lane{padding:16px 14px 16px 17px;display:flex;flex-direction:column}
 .lnh{flex-direction:column;align-items:flex-start;gap:7px;margin-bottom:14px}.tgl{font-size:13px}
 .rws{grid-template-columns:1fr;gap:10px}
 .rw{flex-direction:row;gap:10px;background:#fff;border-radius:12px;padding:8px 10px;box-shadow:0 0 0 1px #efeaf2}
 .rw .lg{--s:48px}.rn{display:flex;flex-direction:column;min-width:0;flex:1}
 .rn b{font:700 13px 'DM Sans',sans-serif;color:var(--ink)}.rs{font:500 11.5px 'DM Sans',sans-serif;color:var(--mute);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
 .rw.on .rs{color:var(--c);font-weight:700}
 .chp{flex:1;min-height:150px;margin-top:12px}.cct{font-size:13.5px}
}
'''
    js = '''<script>(function(){var D=DV,root=document.getElementById('vb');if(!root||D.RM)return;var wait=D.clock(root);var tot=D.$('.tot',root),N=8;
function row(p,n){return D.$('.lane[data-p="'+p+'"] .rw[data-n="'+n+'"]',root)}
(async function(){for(;;){await wait(1100);var r=D.pick(D.$$('.rw:not(.on)',root)),n=r.dataset.n;D.swap(D.$('.rs',r),D.pick(D.amb[D.cat[n]]))}})();
(async function(){var i=0;await wait(600);for(;;){var c=D.con[i%D.con.length];i++;var ln=D.$('.lane[data-p="'+c.p+'"]',root),r=row(c.p,c.n),ch=D.$('.chp .fi',ln);
 r.classList.add('on');ln.classList.add('hot');D.swap(D.$('.rs',r),c.k+'…');
 D.swap(ch,'<span class="cto">'+D.names[c.n]+' · '+c.k+'</span><span class="cct">'+D.WK+'</span>');
 await wait(1700);D.swap(ch,'<span class="cto">'+D.names[c.n]+' → First Officer</span><span class="cct">'+c.t+'</span>');D.swap(D.$('.rs',r),'Sent: '+c.s);
 var pc=D.$('.pc[data-p="'+c.p+'"]',root),b=D.$('b',pc);b.textContent=+b.textContent+1;N++;tot.textContent=N;pc.classList.add('up');D.ping(D.$('.foc',root));
 await wait(2200);r.classList.remove('on');ln.classList.remove('hot');pc.classList.remove('up');await wait(300)}})();
})();</script>'''
    shell(2, css, vis, js)

# ================================================================ 3. The desk feed
def var3():
    def msg(c):
        n, p, k, sh, t = c
        return (f'<div class="m"><span class="mav">{lg(n)}</span><div class="mb"><div class="mh"><b>{NAME[n]}</b><span class="pg" style="--c:{PC[p]}">{p}</span></div>'
                f'<div class="mt">{t}</div></div></div>')
    def rep(t): return f'<div class="m fo"><div class="mb"><div class="mh"><b>First Officer</b></div><div class="mt">{t}</div></div><span class="mav">{fo()}</span></div>'
    seed = msg(CON[0]) + rep(FOR[0]) + msg(CON[1]) + msg(CON[2]) + rep(FOR[2])
    items = ''.join(f'<li class="{"in" if i < 3 else ""}" style="--c:{PC[CON[i][1]]}"><i class="pd"></i><span>{PLAN[i]}</span><em class="pst2">{"✓" if i < 3 else WK}</em></li>' for i in range(8))
    dots = ''.join(f'<i class="{"in" if i < 3 else ""}" style="--c:{PC[CON[i][1]]}"></i>' for i in range(8))
    vis = f'''<div class="vc" id="vc">
<div class="pin">{fo()}<div class="pint"><b>Darnell's plan</b><span><b class="pn">3</b> of 8 in this week</span></div><div class="pdots">{dots}</div></div>
<div class="fcard"><div class="fhead"><span class="lv"></span><b>Behind the desk</b><span class="fsub">Darnell's 5 programs</span></div>
<div class="feed" aria-live="off"><div class="fin">{seed}</div></div>
<div class="also fade"><span class="al">Also on the desk</span>{lg(18)}<b>Delta</b><span class="as">Logging miles</span>{WK}</div></div>
<aside class="plan"><div class="ph">{fo()}<div><b>First Officer</b><span>Darnell's plan, this week</span></div></div><ol class="pl">{items}</ol>
<p class="pfoot">Darnell decides. The desk books after vetting.</p></aside>
</div>'''
    css = '''
.vc{display:grid;gap:12px;align-items:start}
.pin{display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;gap:6px 12px;align-items:center;background:#fff;border-radius:16px;box-shadow:0 0 0 1.5px #FA1896,0 14px 30px -24px rgba(250,24,150,.6);padding:11px 14px}
.pin .foc{--s:45px;grid-row:span 2}
.pint b{display:block;font:700 14.5px 'DM Sans',sans-serif;color:var(--ink)}.pint span{font:500 12.5px 'DM Sans',sans-serif;color:var(--mute)}.pint .pn{display:inline;font-size:12.5px;color:#d40f7d}
.pdots{display:flex;gap:6px}.pdots i{width:14px;height:5px;border-radius:3px;background:#ece8ef;transition:background .5s}.pdots i.in{background:var(--c)}
.fcard{background:#faf8fb;border-radius:20px;box-shadow:inset 0 0 0 1px #eee9f1;padding:12px 12px 10px;min-width:0}
.fhead{display:flex;align-items:center;gap:7px;flex-wrap:wrap;font:700 13px 'DM Sans',sans-serif;color:var(--ink);padding:2px 2px 10px;border-bottom:1px solid #eee9f1}
.lv{width:6px;height:6px;border-radius:50%;background:#12834E;box-shadow:0 0 0 3px rgba(18,131,78,.14)}
.fsub{font:500 12px 'DM Sans',sans-serif;color:var(--mute);margin-left:auto}
.feed{height:420px;overflow:hidden;position:relative;-webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 70px);mask-image:linear-gradient(to bottom,transparent 0,#000 70px)}
.fin{position:absolute;left:0;right:0;bottom:0;display:flex;flex-direction:column;gap:10px;padding:10px 0 8px}
.m{display:flex;gap:8px;align-items:flex-end;max-width:92%;animation:min .45s cubic-bezier(.2,.7,.2,1) both}
@keyframes min{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.mav .lg{--s:28px}.mav .foc{--s:35px}
.mb{background:#fff;border-radius:14px 14px 14px 4px;box-shadow:0 0 0 1px #ebe6ee;padding:8px 11px;min-width:0}
.mh{display:flex;align-items:center;gap:6px;margin:0 0 2px}.mh b{font:700 12px 'DM Sans',sans-serif;color:var(--ink)}
.pg{font:700 10px/1 'DM Sans',sans-serif;color:var(--c);background:color-mix(in srgb,var(--c) 11%,#fff);border-radius:999px;padding:3px 7px}
.mt{font:400 13.5px/1.45 'DM Sans',sans-serif;color:var(--body)}
.m.typ .mb{padding:10px 12px}.m.typ .mt{font-size:12px;color:var(--mute);display:flex;align-items:center;gap:8px}
.m.typ .wk i{background:var(--c,#bdb6c4)}
.m.fo{align-self:flex-end}.m.fo .mb{background:#fff0f8;box-shadow:0 0 0 1px #fbc9e4;border-radius:14px 14px 4px 14px}.m.fo .mh b{color:#d40f7d}
.also{display:flex;align-items:center;gap:7px;border-top:1px solid #eee9f1;padding:9px 2px 0;font:500 12px 'DM Sans',sans-serif;color:var(--mute);white-space:nowrap;overflow:hidden}
.also .lg{--s:22px}.also b{color:var(--ink);font-weight:700}.al{font:600 10.5px 'JetBrains Mono',monospace;letter-spacing:.06em;text-transform:uppercase;color:#a29bab;margin-right:2px}
.plan{display:none}
@media(max-width:380px){.al{display:none}}
@media(min-width:1024px){
 .vc{grid-template-columns:1.45fr 1fr;gap:18px;align-items:stretch}
 .pin{display:none}
 .fcard{padding:16px 18px 12px;grid-row:1}.feed{height:470px}
 .mav .lg{--s:32px}.mav .foc{--s:40px}.mt{font-size:14px}.m{max-width:84%}
 .plan{display:block;background:#fff;border-radius:20px;box-shadow:0 0 0 1.5px #FA1896,0 22px 40px -30px rgba(250,24,150,.6);padding:18px 18px 14px;display:flex;flex-direction:column}
 .ph{display:flex;align-items:center;gap:12px;margin:0 0 12px}.ph .foc{--s:56px}.ph b{display:block;font:700 15px 'DM Sans',sans-serif;color:var(--ink)}.ph span{font:500 12.5px 'DM Sans',sans-serif;color:var(--mute)}
 .pl{list-style:none;margin:0;padding:0;display:grid;gap:2px}
 .pl li{display:flex;align-items:center;gap:10px;padding:9px 6px;border-bottom:1px solid #f3f0f5;font:500 14px 'DM Sans',sans-serif;color:var(--mute);transition:color .4s}
 .pl li:last-child{border-bottom:0}.pl li.in{color:var(--ink)}
 .pd{width:8px;height:8px;border-radius:50%;background:#e4dfe8;transition:background .4s;flex:none}.pl li.in .pd{background:var(--c)}
 .pst2{margin-left:auto;font-style:normal;font:700 13px 'DM Sans',sans-serif;color:var(--c)}
 .pl li.fresh{background:color-mix(in srgb,var(--c) 7%,#fff);border-radius:10px}
 .pfoot{font:500 12px 'DM Sans',sans-serif;color:var(--mute);margin:auto 6px 0;padding-top:10px}
}
'''
    js = '''<script>(function(){var D=DV,root=document.getElementById('vc');if(!root||D.RM)return;var wait=D.clock(root);var fin=D.$('.fin',root);
function add(h){fin.insertAdjacentHTML('beforeend',h);var ms=D.$$('.m',fin);while(ms.length>8){ms.shift().remove()}return fin.lastElementChild}
function av(n){return '<span class="mav">'+D.lg(n)+'</span>'}
var FOH='<span class="mav"><span class="foc"><img src="'+D.chev+'" alt=""></span></span>';
var others=Object.keys(D.names).filter(function(n){return D.darn.indexOf(+n)<0});
(async function(){var a=D.$('.also',root);for(;;){await wait(2300);var n=D.pick(others);D.swap(a,'<span class="al">Also on the desk</span>'+D.lg(n)+'<b>'+D.names[n]+'</b><span class="as">'+D.pick(D.amb[D.cat[n]])+'</span>'+D.WK)}})();
function setPlan(k){D.$$('.pl li',root).forEach(function(li,j){var on=j<k;li.classList.toggle('in',on);li.classList.toggle('fresh',j==k-1);D.$('.pst2',li).innerHTML=on?'\u2713':D.WK});
 D.$$('.pdots i',root).forEach(function(d,j){d.classList.toggle('in',j<k)});var pn=D.$('.pn',root);if(pn)pn.textContent=k}
(async function(){var i=3,r=1;await wait(900);for(;;){var j=i%8,c=D.con[j];i++;
 if(j==0){setPlan(0);await wait(500)}
 var m=add('<div class="m typ" style="--c:'+D.pc[c.p]+'">'+av(c.n)+'<div class="mb"><div class="mt"><b style="color:var(--ink)">'+D.names[c.n]+'</b> '+c.k+' '+D.WK+'</div></div></div>');
 await wait(1900);
 m.outerHTML='<div class="m">'+av(c.n)+'<div class="mb"><div class="mh"><b>'+D.names[c.n]+'</b><span class="pg" style="--c:'+D.pc[c.p]+'">'+c.p+'</span></div><div class="mt">'+c.t+'</div></div></div>';
 setPlan(j+1);D.$$('.foc',root).forEach(D.ping);
 await wait(1300);
 if(j%2==1){var f=add('<div class="m fo typ"><div class="mb"><div class="mt">'+D.WK+'</div></div>'+FOH+'</div>');await wait(1000);
  f.outerHTML='<div class="m fo"><div class="mb"><div class="mh"><b>First Officer</b></div><div class="mt">'+D.fo[r++%D.fo.length]+'</div></div>'+FOH+'</div>';await wait(1400)}
 else await wait(500)}})();
})();</script>'''
    shell(3, css, vis, js)

# ================================================================ 4. The orbit
RING = [2, 1, 9, 17, 25, 5, 12, 18, 26, 3, 20, 10, 27, 19, 11, 32]
def var4():
    k = len(RING); dots = ''
    for i, n in enumerate(RING):
        a = -math.pi/2 + i * 2*math.pi/k
        x, y = math.cos(a), math.sin(a)
        dk = ' dk' if n in DARN else ''
        dots += (f'<div class="ob{dk}" data-n="{n}" data-x="{x:.4f}" data-y="{y:.4f}" style="--x:{x:.4f};--y:{y:.4f}">{lg(n)}'
                 f'<span class="pip">{WK}</span><span class="nm">{NAME[n]}</span></div>')
    c = CON[0]
    vis = f'''<div class="vd" id="vd">
<div class="stage">
<div class="halo"></div>
{dots}
<div class="ctr">{fo()}<b>First Officer</b><span>Darnell</span></div>
<div class="bub2" aria-hidden="true"><div class="fi fade"></div></div>
</div>
<div class="ocap" style="--c:{PC[c[1]]}"><div class="fi fade"><div class="oh">{lg(c[0])}<b>{NAME[c[0]]}</b><span class="arr">to First Officer</span><span class="pg">{c[1]}</span></div><div class="ot">{c[4]}</div></div></div>
<p class="osub">The specialists for his programs come forward. The rest of the 50+ stay on watch.</p>
</div>'''
    css = '''
.vd{display:flex;flex-direction:column;align-items:center}
.stage{--W:min(358px,calc(100vw - 32px));--R:40.5%;--ls:36px;width:var(--W);height:var(--W);position:relative;margin:4px auto 0}
.halo{position:absolute;inset:9.5%;border-radius:50%;background:radial-gradient(circle,#fff6fb 0,#fff 62%,transparent 70%)}
.ob{position:absolute;left:calc(50% + var(--x) * var(--R));top:calc(50% + var(--y) * var(--R));transform:translate(-50%,-50%);transition:left .7s cubic-bezier(.2,.7,.2,1),top .7s cubic-bezier(.2,.7,.2,1),opacity .5s;z-index:2}
.ob .lg{--s:var(--ls);opacity:.82;transition:box-shadow .5s,opacity .5s,transform .6s}
.ob.dk .lg{opacity:1;box-shadow:0 0 0 1.5px #f6b5d8}
.ob .nm{display:none}
.pip{position:absolute;right:-7px;top:-7px;background:#fff;border-radius:999px;box-shadow:0 0 0 1px #e6e1ea,0 4px 10px -6px rgba(20,18,22,.3);padding:4px 5px;line-height:0;opacity:0;transform:scale(.6);transition:opacity .3s,transform .3s}
.pip .wk{height:6px}.pip .wk i{width:3.5px;height:3.5px}
.ob.th .pip{opacity:1;transform:none}
.ob.on{--R:30%;z-index:4}.ob.on .lg{opacity:1;transform:scale(1.14);box-shadow:0 0 0 2px var(--c),0 10px 22px -8px var(--c)}
.ob.on .pip .wk i{background:var(--c)}
.ob.ok .pip{background:var(--c);box-shadow:none}.ob.ok .pip .wk{display:none}.ob.ok .pip::after{content:"\\2713";color:#fff;font:700 9px/6px 'DM Sans',sans-serif;display:block;width:10px;height:6px;text-align:center}
.ctr{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;flex-direction:column;align-items:center;gap:5px;z-index:3}
.ctr .foc{--s:45px;box-shadow:0 0 0 1.5px #FA1896,0 12px 26px -12px rgba(250,24,150,.6)}
.ctr b{font:700 12px 'DM Sans',sans-serif;color:#d40f7d;white-space:nowrap}.ctr span{font:500 10.5px 'DM Sans',sans-serif;color:var(--mute);margin-top:-4px}
.bub2{display:none}
.ocap{width:100%;max-width:520px;margin:12px auto 0;background:#fff;border-radius:16px;box-shadow:0 0 0 1.5px var(--c),0 16px 30px -24px var(--c);padding:11px 13px;min-height:104px;transition:box-shadow .4s}
.oh{display:flex;align-items:center;gap:6px;font:700 12.5px 'DM Sans',sans-serif;color:var(--ink)}.oh .lg{--s:22px}
.arr{font-weight:500;color:var(--mute)}
.pg{font:700 10px/1 'DM Sans',sans-serif;color:#fff;background:var(--c);border-radius:999px;padding:4px 8px;margin-left:auto}
.ot{font:400 13.5px/1.45 'DM Sans',sans-serif;color:var(--body);margin-top:6px}
.ot .wk i{background:var(--c)}
.osub{font:500 12.5px/1.45 'DM Sans',sans-serif;color:var(--mute);text-align:center;margin:12px 0 0}
@media(min-width:1024px){
 .stage{--W:620px;--ls:52px}
 .ob .nm{display:block;position:absolute;left:50%;top:calc(100% + 4px);transform:translateX(-50%);font:600 10.5px 'DM Sans',sans-serif;color:var(--mute);white-space:nowrap;opacity:0;transition:opacity .3s}
 .ob.on .nm,.ob.dk .nm{opacity:1}.ob.on .nm{color:var(--ink);font-weight:700}
 .pip{right:-10px;top:-10px;padding:5px 7px}.pip .wk{height:8px}.pip .wk i{width:4px;height:4px}
 .ob.ok .pip::after{font-size:11px;width:12px;height:8px;line-height:8px}
 .ctr .foc{--s:65px}.ctr b{font-size:13.5px}.ctr span{font-size:11.5px}
 .bub2{display:block;position:absolute;width:236px;left:calc(50% + var(--bx,0px));top:calc(50% + var(--by,0px));transform:translate(-50%,-50%);z-index:5;background:#fff;border-radius:16px;box-shadow:0 0 0 1.5px var(--c,#FA1896),0 18px 36px -20px rgba(20,18,22,.35);padding:10px 12px;opacity:0;transition:opacity .35s}
 .bub2.show{opacity:1}
 .bub2 .oh{font-size:12px}.bub2 .ot{font-size:13px;margin-top:5px}
 .ocap{display:none}
 .osub{margin-top:8px}
}
@media (prefers-reduced-motion:reduce){.ob{transition:none}}
'''
    js = '''<script>(function(){var D=DV,root=document.getElementById('vd');if(!root||D.RM)return;var wait=D.clock(root);
var obs=D.$$('.ob',root),cap=D.$('.ocap',root),bub=D.$('.bub2',root),bi=D.$('.bub2 .fi',root),ci=D.$('.ocap .fi',root),foc=D.$('.ctr .foc',root),desk=function(){return innerWidth>=1024};
function ob(n){return D.$('.ob[data-n="'+n+'"]',root)}
function head(c){return '<div class="oh">'+D.lg(c.n)+'<b>'+D.names[c.n]+'</b><span class="arr">to First Officer</span><span class="pg">'+c.p+'</span></div>'}
/* ambient: a few logos always show a typing pip */
(async function(){for(;;){await wait(700);var idle=obs.filter(function(o){return !o.classList.contains('th')&&!o.classList.contains('on')});
 var o=D.pick(idle);o.classList.add('th');setTimeout(function(){if(!o.classList.contains('on'))o.classList.remove('th')},2600+Math.random()*1800)}})();
(async function(){var i=1;await wait(800);for(;;){var c=D.con[i%D.con.length];i++;var o=ob(c.n);var col=D.pc[c.p];
 o.style.setProperty('--c',col);o.classList.add('on','th');o.classList.remove('ok');
 cap.style.setProperty('--c',col);
 var tw=head(c)+'<div class="ot">'+D.names[c.n]+' · '+c.k+' '+D.WK+'</div>';
 if(desk()){var R=172;bub.style.setProperty('--bx',(+o.dataset.x*R)+'px');bub.style.setProperty('--by',(+o.dataset.y*R*.82)+'px');bub.style.setProperty('--c',col);bi.innerHTML=tw;bub.classList.add('show')}
 else D.swap(ci,tw);
 await wait(1700);
 var full=head(c)+'<div class="ot">'+c.t+'</div>';
 o.classList.add('ok');D.ping(foc);
 if(desk()){D.swap(bi,full)}else D.swap(ci,full);
 await wait(2600);
 if(desk())bub.classList.remove('show');
 o.classList.remove('on','ok','th');await wait(600)}})();
})();</script>'''
    shell(4, css, vis, js)

# ================================================================ 5. The mosaic
MOS = [1,12,9,25,2,18,26,3, 17,10,27,19, 11,30,5,20, 32,4,13,21,24,33,36,47]
def var5():
    tiles = ''
    for i, n in enumerate(MOS):
        dk = ' dk' if n in DARN else ''
        mx = ' mx' if i >= 16 else ''
        tiles += f'<div class="mt5{dk}{mx}" data-n="{n}">{lg(n)}<b>{NAME[n]}</b><span class="ms fade">{WK}</span></div>'
    c = CON[3]
    cnt = ''.join(f'<span class="sc" data-p="{p}" style="--c:{PC[p]}"><b>{[x[1] for x in CON].count(p)}</b>{p}</span>' for p in PILLARS)
    vis = f'''<div class="ve" id="ve"><div class="mos">
<div class="sum"><div class="sh">{fo()}<div><b>First Officer</b><span>Latest for Darnell</span></div></div>
<div class="sl"><div class="fi fade"><span class="sfrom" style="--c:{PC[c[1]]}">{lg(c[0])}{NAME[c[0]]} · {c[1]}</span><p class="sq">{c[4]}</p></div></div>
<div class="scs">{cnt}</div></div>
{tiles}</div></div>'''
    css = '''
.mos{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.sum{grid-column:1/-1;order:-1;background:#fff;border-radius:18px;box-shadow:0 0 0 1.5px #FA1896,0 18px 36px -26px rgba(250,24,150,.6);padding:13px 14px 12px;display:flex;flex-direction:column;margin-bottom:4px}
.sh{display:flex;align-items:center;gap:10px}.sh .foc{--s:45px}.sh b{display:block;font:700 14.5px 'DM Sans',sans-serif;color:var(--ink)}.sh span{font:500 12px 'DM Sans',sans-serif;color:var(--mute)}
.sl{min-height:118px;margin:10px 0 8px}
.sfrom{display:inline-flex;align-items:center;gap:6px;font:700 11.5px 'DM Sans',sans-serif;color:var(--c)}.sfrom .lg{--s:20px}
.sq{font:400 18px/1.32 'DM Serif Display',Georgia,serif;color:var(--ink);margin:6px 0 0;letter-spacing:-.005em}
.sq .etag{font-family:'DM Sans',sans-serif;vertical-align:3px}
.scs{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;border-top:1px solid #f1edf3;padding-top:10px}
.sc{display:flex;flex-direction:column;align-items:center;font:600 11px 'DM Sans',sans-serif;color:var(--mute)}
.sc b{font:700 18px/1.1 'DM Sans',sans-serif;color:var(--c);transition:transform .3s}.sc.up b{transform:scale(1.25)}
.mt5{background:#faf8fb;border-radius:14px;box-shadow:inset 0 0 0 1px #eee9f1;display:flex;flex-direction:column;align-items:center;gap:5px;padding:9px 3px 7px;min-width:0;transition:box-shadow .45s,background .45s}
.mt5 .lg{--s:36px}.mt5 b{display:none}
.ms{display:flex;align-items:center;justify-content:center;height:24px;font:600 9.5px/1.15 'DM Sans',sans-serif;color:var(--mute);text-align:center}
.mt5.dk .lg{box-shadow:0 0 0 1.5px #f6b5d8}
.mt5.on{background:#fff;box-shadow:inset 0 0 0 1.5px var(--c),0 10px 22px -16px var(--c)}
.mt5.on .wk i{background:var(--c)}.mt5.on .ms{color:var(--c)}
.mt5.mx{display:none}
@media(min-width:1024px){
 .mos{grid-template-columns:repeat(8,1fr);gap:10px}
 .sum{grid-column:3/7;grid-row:2/4;order:0;margin:0;padding:18px 22px 14px}
 .sh .foc{--s:56px}.sh b{font-size:15.5px}
 .sl{min-height:0;flex:1;margin:12px 0 10px}.sq{font-size:22px}
 .mt5{padding:14px 6px 10px;gap:6px}.mt5 .lg{--s:46px}
 .mt5 b{display:block;font:700 12px 'DM Sans',sans-serif;color:var(--ink);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%}
 .ms{font-size:10.5px;height:26px;padding:0 4px}
 .mt5.mx{display:flex}
}
'''
    js = '''<script>(function(){var D=DV,root=document.getElementById('ve');if(!root||D.RM)return;var wait=D.clock(root);
var T={};D.$$('.mt5',root).forEach(function(t){T[t.dataset.n]=t});var sl=D.$('.sl .fi',root),desk=function(){return innerWidth>=1024};
var others=Object.keys(T).filter(function(n){return D.darn.indexOf(+n)<0});
/* ambient: on desktop a few tiles flash a status, then go back to typing */
(async function(){for(;;){await wait(1000);if(!desk())continue;var n=D.pick(others),t=T[n],m=D.$('.ms',t);D.swap(m,D.pick(D.amb[D.cat[n]]));
 setTimeout(function(){D.swap(m,D.WK)},2600)}})();
(async function(){var i=4;await wait(700);for(;;){var c=D.con[i%D.con.length];i++;var t=T[c.n],m=D.$('.ms',t);
 t.style.setProperty('--c',D.pc[c.p]);t.classList.add('on');D.swap(m,(desk()?c.k+' ':'')+D.WK);
 await wait(1700);D.swap(m,'\u2192 '+c.s);
 D.swap(sl,'<span class="sfrom" style="--c:'+D.pc[c.p]+'">'+D.lg(c.n)+D.names[c.n]+' \u00b7 '+c.p+'</span><p class="sq">'+c.t+'</p>');
 var sc=D.$('.sc[data-p="'+c.p+'"]',root),b=D.$('b',sc);b.textContent=+b.textContent+1;sc.classList.add('up');D.ping(D.$('.sum .foc',root));
 await wait(2300);sc.classList.remove('up');t.classList.remove('on');D.swap(m,D.WK);await wait(500)}})();
})();</script>'''
    shell(5, css, vis, js)

# ================================================================ gallery
def gallery():
    cards = ''
    for i, (name, desc) in enumerate(VARS, 1):
        cards += f'''<a class="gc" href="desk-var-{i}.html"><div class="gth"><img class="gd" src="_shots/deskvar-{i}-1440.jpg" alt="Variation {i} at desktop width" loading="lazy"><img class="gm" src="_shots/deskvar-{i}-390.jpg" alt="Variation {i} on a phone" loading="lazy"></div>
<div class="gt"><span class="gn">{i}</span><div><b>{name}</b><p>{desc}</p><span class="go">Open variation {i} →</span></div></div></a>'''
    body = f'''<style>{BASE_CSS}
.gl2{{display:grid;gap:18px;margin-top:8px}}
.gc{{display:block;text-decoration:none;color:inherit;background:#faf8fb;border-radius:20px;box-shadow:inset 0 0 0 1px #eee9f1;padding:12px;transition:box-shadow .3s}}
.gc:hover{{box-shadow:inset 0 0 0 1.5px #FA1896}}
.gth{{display:grid;grid-template-columns:1fr 34%;gap:10px;align-items:start;height:220px;overflow:hidden;border-radius:12px}}
.gth img{{width:100%;display:block;border-radius:10px;box-shadow:0 0 0 1px #ebe6ee;background:#fff}}
.gt{{display:flex;gap:11px;padding:12px 4px 4px}}
.gn{{width:28px;height:28px;border-radius:50%;background:#FA1896;color:#fff;font:700 14px/28px 'DM Sans',sans-serif;text-align:center;flex:none}}
.gt b{{font:700 17px 'DM Sans',sans-serif;color:var(--ink)}}.gt p{{font:400 14px/1.5 'DM Sans',sans-serif;color:var(--body);margin:4px 0 6px}}
.go{{font:700 13px 'DM Sans',sans-serif;color:#d40f7d}}
@media(min-width:900px){{.gl2{{grid-template-columns:1fr 1fr;gap:22px}}.gth{{height:300px}}}}
</style>
<section class="dv"><div class="dvw">
<div class="dvk">Mockups · Step 2, His desk</div>
<h2 class="beat"><span class="n">2</span><span>His desk: five variations</span></h2>
<p class="lede2">No connector lines in any of them. In each one the specialists keep working, show the typing dots, then hand a short finding to First Officer. Each is built for desktop and designed separately for the phone.</p>
<div class="gl2">{cards}</div>
<p class="cap2">{CAP}</p>
</div></section>'''
    page('desk-variations.html', 'First Officer · His desk, five variations (mockup)', body, desc='Five mockup variations of the His desk step.', src='home')

if __name__ == '__main__':
    for f in [globals().get(f'var{i}') for i in range(1,6)] + [gallery]:
        if f: f()
