"""Busy-sphere explorations of desk variation 4 (the orbit). All 50 program logos on a filled sphere.
Background: many specialists show dancing 3-dot typing. Activation: the dots stop, the logo lights up and lifts,
its response appears, First Officer pulses. No connector lines.
Run: python3 _build/desk_spheres.py -> desk-sphere-1.html .. -3.html + desk-spheres.html (and refreshes desk-variations.html link via desk_vars)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import desk_vars as dv
from desk_vars import NAME, LOGO, DARN, PC, PILLARS, CON, CHEV, WK, BASE_CSS, BASE_JS, LEDE, CAP, lg, fo, E
from fosite import page

# order on the sphere: Darnell's five spread across the Fibonacci sequence
ORDER = [n for n in range(1, 51) if n not in DARN]
for pos, n in zip([6, 15, 24, 32, 41], [12, 2, 17, 11, 20]):
    ORDER.insert(pos, n)
# brief generic responses from the rest of the desk, each tied to a pillar (used for the v3 counters)
GEN = [('Watching bonuses','Earn'),('Card offers scan','Earn'),('Logging miles','Earn'),('Spend cap watch','Earn'),
       ('Award chart check','Burn'),('Partner awards','Burn'),('Transfer ratios','Burn'),('Surcharge check','Burn'),
       ('Cash rate compare','Return'),('Fare rules','Return'),('Free night rules','Return'),
       ('Rules checked','Learn'),('Updating rules','Learn'),('Nightly data sync','Learn'),('Routing rules','Learn')]
SP = [
 ('Rotating globe', 'All 50 programs on a slowly turning globe. Busy dots everywhere; on every beat one to three go quiet, light up and answer, and the answers land in a live feed.'),
 ('Packed cluster', 'A dense, breathing cluster of every program with First Officer at its heart. Answers pop up right beside the logos that respond.'),
 ('Wave sweeps', 'A soft band sweeps the globe on a steady rhythm and every busy specialist it crosses answers at once, with Earn, Burn, Return and Learn counting up.'),
]
SUB = 'All 50+ programs on the desk. When a specialist\'s dots go quiet, it is answering First Officer.'

def nodes():
    return ''.join(f'<div class="sn{" dk" if n in DARN else ""}" data-n="{n}"><span class="lg"><img src="{LOGO(n)}" alt="" decoding="async"></span><span class="pip">{WK}</span></div>' for n in ORDER)

def stage(extra=''):
    return (f'<div class="sph" aria-label="The desk: specialists for 50+ programs, with First Officer at the centre" role="img">'
            f'<div class="sbody">{extra}</div><div class="sshade"></div>{nodes()}<div class="sfo"><img src="{CHEV}" alt=""></div></div>')

def card(c, serif=False):
    n, p, k, sh, t = c
    return (f'<div class="rh">{lg(n)}<b>{NAME[n]}</b><span class="arr">to First Officer</span><span class="pg" style="--c:{PC[p]}">{p}</span></div>'
            f'<div class="rt{" serif" if serif else ""}">{t}</div>')

SCSS = '''
.sx{display:grid;gap:14px;justify-items:center}
.sph{--W:min(400px,calc(100vw - 36px));--b:calc(var(--W) * .115);width:var(--W);height:var(--W);position:relative;margin:0 auto;contain:layout}
.sbody{position:absolute;inset:3%;border-radius:50%;overflow:hidden;background:radial-gradient(circle at 36% 30%,#fff 0,#fdf5fa 38%,#f6eff7 66%,#ece4f0 100%);box-shadow:inset 0 -18px 40px -24px rgba(113,73,201,.25),inset 0 0 0 1px rgba(20,18,22,.04)}
.sshade{position:absolute;left:18%;right:18%;bottom:-5%;height:7%;border-radius:50%;background:radial-gradient(closest-side,rgba(20,18,22,.13),transparent);z-index:0}
.sn{position:absolute;left:50%;top:50%;width:var(--b);height:var(--b);margin:calc(var(--b) / -2) 0 0 calc(var(--b) / -2);will-change:transform,opacity;transform-origin:50% 50%}
.sn .lg{width:100%;height:100%;box-shadow:0 0 0 1px #e6e1ea,0 4px 10px -6px rgba(20,18,22,.25);transition:box-shadow .35s}
.sn.dk .lg{box-shadow:0 0 0 1.5px #f6b5d8,0 4px 10px -6px rgba(20,18,22,.25)}
.pip{position:absolute;right:-16%;top:-14%;background:#fff;border-radius:999px;padding:3px 4px;line-height:0;box-shadow:0 0 0 1px #ebe6ee,0 3px 8px -4px rgba(20,18,22,.3);opacity:0;transform:scale(.5);transition:opacity .25s,transform .25s,background .25s}
.pip .wk{height:5px;gap:2px}.pip .wk i{width:3px;height:3px}
.sn.busy .pip,.sn.hush .pip,.sn.act .pip{opacity:1;transform:none}
.sn.hush .wk i{animation:none;opacity:1;transform:none;background:#FA1896}
.sn.act .lg{box-shadow:0 0 0 1.5px #FA1896,0 0 0 5px rgba(250,24,150,.10),0 10px 24px -10px rgba(250,24,150,.5)}
.sn.act .pip{background:#FA1896;box-shadow:none}.sn.act .wk{display:none}
.sn.act .pip::after{content:"\\2713";display:block;color:#fff;font:700 8px/5px 'DM Sans',sans-serif;width:11px;height:5px;text-align:center}
.paused .wk i{animation-play-state:paused}
.sfo{position:absolute;left:50%;top:50%;width:calc(var(--b) * 1.25);height:calc(var(--b) * 1.25);transform:translate(-50%,-50%);z-index:600;border-radius:50%;background:#fff;box-shadow:0 0 0 1.5px #FA1896,0 14px 30px -12px rgba(250,24,150,.55);display:grid;place-items:center}
.sfo img{width:60%;height:60%;object-fit:contain}
.sfo::after{content:"";position:absolute;inset:-1px;border-radius:50%;box-shadow:0 0 0 2px #FA1896;opacity:0}
.sfo.beat{animation:fobeat .55s cubic-bezier(.2,.7,.2,1)}.sfo.beat::after{animation:fping 1s ease-out}
@keyframes fobeat{0%{transform:translate(-50%,-50%) scale(1)}40%{transform:translate(-50%,-50%) scale(1.08)}100%{transform:translate(-50%,-50%) scale(1)}}
.ssub{font:500 12.5px/1.45 'DM Sans',sans-serif;color:var(--mute);text-align:center;margin:2px 0 0;max-width:30em}
/* response card (fixed height so nothing jumps) */
.rcard{width:100%;max-width:520px;height:142px;background:#fff;border-radius:16px;box-shadow:0 0 0 1.5px #FA1896,0 16px 30px -24px rgba(250,24,150,.6);padding:12px 14px;overflow:hidden}
.rk{display:flex;align-items:center;gap:6px;font:600 10.5px 'JetBrains Mono',monospace;letter-spacing:.08em;text-transform:uppercase;color:#a0889a;margin:0 0 7px}
.rk .lv{width:6px;height:6px;border-radius:50%;background:#12834E;box-shadow:0 0 0 3px rgba(18,131,78,.14)}
.rh{display:flex;align-items:center;gap:6px;font:700 12.5px 'DM Sans',sans-serif;color:var(--ink)}.rh .lg{--s:22px}
.arr{font-weight:500;color:var(--mute)}
.pg{font:700 10px/1 'DM Sans',sans-serif;color:#fff;background:var(--c);border-radius:999px;padding:4px 8px;margin-left:auto}
.rt{font:400 13.5px/1.45 'DM Sans',sans-serif;color:var(--body);margin-top:6px}
.rt.serif{font:400 17px/1.3 'DM Serif Display',Georgia,serif;color:var(--ink)}.rt.serif .etag{font-family:'DM Sans',sans-serif;vertical-align:2px}
.also2{width:100%;max-width:520px;height:20px;font:500 12px/20px 'DM Sans',sans-serif;color:var(--mute);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-align:center}
.also2 b{color:var(--ink);font-weight:700}
.side{display:none}
@media(min-width:1024px){
 .sx{grid-template-columns:580px minmax(0,1fr);gap:56px;align-items:center;justify-items:stretch}
 .sph{--W:580px;--b:60px}
 .pip{padding:4px 5px}.pip .wk{height:6px;gap:3px}.pip .wk i{width:4px;height:4px}.sn.act .pip::after{font-size:10px;width:14px;height:6px;line-height:6px}
 .sx>.rcard,.sx>.also2{display:none}
 .side{display:flex;flex-direction:column;gap:14px;min-width:0}
 .side .rcard{max-width:none;height:150px;padding:15px 18px}.side .rt{font-size:14.5px}.side .rt.serif{font-size:21px}
 .ssub{grid-column:1/-1;justify-self:center}
}
@media (prefers-reduced-motion:reduce){.sfo.beat,.sfo.beat::after{animation:none}}
'''

ENGINE = r'''<script>window.SPH=function(root,o){var D=DV,st=D.$('.sph',root),fo=D.$('.sfo',root);
var G=Math.PI*(3-Math.sqrt(5)),nodes=D.$$('.sn',st).map(function(el,i){return {el:el,n:+el.dataset.n,i:i,dk:el.classList.contains('dk'),l:0,lt:0,busy:false,act:false,px:0,py:0,d:0,zi:-1}});
var N=nodes.length,byN={};nodes.forEach(function(nd,i){byN[nd.n]=nd;var y=1-2*(i+.5)/N,r=Math.sqrt(1-y*y),th=i*G;nd.x=Math.cos(th)*r;nd.y=y;nd.z=Math.sin(th)*r;
 var rr=Math.sqrt((i+3.2)/(N+3.2));nd.cr=rr;nd.cx=Math.cos(th)*rr;nd.cy=Math.sin(th)*rr});
var W,R,B,F;function size(){W=st.clientWidth;B=nodes[0].el.offsetWidth;F=fo.offsetWidth;R=W/2-B*.5-2}size();
var mode=o.mode||'globe',ang=o.a0||.5,tilt=-.34,T=0;
function place(){var ca=Math.cos(ang),sa=Math.sin(ang),ct=Math.cos(tilt),stt=Math.sin(tilt);
 for(var k=0;k<N;k++){var nd=nodes[k],px,py,d,s,op;
  if(mode=='cluster'){var br=Math.sin(T*1.3-nd.cr*4.4)*.5+.5;d=(1-nd.cr*nd.cr*.8)*.85+br*.15;var f=.975+.025*br;px=nd.cx*R*f;py=nd.cy*R*f;s=.42+.5*d;op=.5+.5*d}
  else{var x1=nd.x*ca+nd.z*sa,z1=-nd.x*sa+nd.z*ca,y2=nd.y*ct-z1*stt,z2=nd.y*stt+z1*ct;d=(z2+1)/2;var pf=.9+.1*d;px=x1*R*pf;py=y2*R*pf;s=.38+.62*d;op=.12+.88*Math.pow(d,1.6)}
  nd.l+=(nd.lt-nd.l)*.16;if(Math.abs(nd.lt-nd.l)<.002)nd.l=nd.lt;nd.d=d;nd.px=px;nd.py=py;
  s*=1+.2*nd.l;op=Math.min(1,op+nd.l);
  nd.el.style.transform='translate3d('+px.toFixed(1)+'px,'+py.toFixed(1)+'px,0) scale('+s.toFixed(3)+')';nd.el.style.opacity=op.toFixed(3);
  var zi=nd.l>.02?400+Math.round(nd.l*20):Math.round(d*300);if(zi!==nd.zi){nd.zi=zi;nd.el.style.zIndex=zi}}}
function setBusy(nd,b){nd.busy=b;nd.el.classList.toggle('busy',b)}
function eligible(nd,minD){return !nd.act&&nd.l<.05&&nd.d>(minD==null?.6:minD)&&Math.sqrt(nd.px*nd.px+nd.py*nd.py)>F*.8}
var GEN=o.gen,ci=0;
function genResp(){var g=D.pick(GEN);return {dk:false,s:g[0],p:g[1]}}
function activate(nd,resp,hold){if(nd.act)return;nd.act=true;setBusy(nd,true);nd.el.classList.add('hush');
 setTimeout(function(){nd.el.classList.remove('hush');nd.el.classList.add('act');nd.lt=1;fo.classList.remove('beat');void fo.offsetWidth;fo.classList.add('beat');o.onAct&&o.onAct(nd,resp)},D.RM?0:340);
 if(D.RM){nd.l=1;return}
 setTimeout(function(){nd.el.classList.remove('act');nd.lt=0;nd.act=false;setBusy(nd,false)},340+(hold||1600))}
function nextDarnell(minD){for(var j=0;j<D.con.length;j++){var c=D.con[(ci+j)%D.con.length],nd=byN[c.n];if(eligible(nd,minD)){ci=ci+j+1;return [nd,{dk:true,c:c,p:c.p}]}}return null}
var api={nodes:nodes,byN:byN,activate:activate,eligible:eligible,nextDarnell:nextDarnell,genResp:genResp,stage:st,R:function(){return R},B:function(){return B},setBusy:setBusy};
/* start: about half the desk typing */
D.shuffle(nodes).slice(0,Math.round(N*.5)).forEach(function(nd){setBusy(nd,true)});
nodes.forEach(function(nd){if(nd.dk)setBusy(nd,true)});
place();
if(D.RM){var dd=nextDarnell(.45);if(dd)activate(dd[0],dd[1]);var g=D.shuffle(nodes.filter(function(nd){return !nd.dk&&eligible(nd,.55)})).slice(0,2);g.forEach(function(nd){activate(nd,genResp())});place();o.onStatic&&o.onStatic(api);return api}
var wait=D.clock(root),raf=0,last=0,vis=false;
function frame(now){raf=requestAnimationFrame(frame);var dt=Math.min(.05,(now-last)/1000);last=now;T+=dt;ang+=(o.rot||0)*dt;if(o.onFrame)o.onFrame(dt,T,api);place()}
if('IntersectionObserver' in window){new IntersectionObserver(function(e){vis=e[0].isIntersecting;root.classList.toggle('paused',!vis);
 if(vis&&!raf){last=performance.now();raf=requestAnimationFrame(frame)}else if(!vis&&raf){cancelAnimationFrame(raf);raf=0}},{threshold:0}).observe(root)}
else{last=performance.now();raf=requestAnimationFrame(frame)}
addEventListener('resize',function(){size()});
/* background busyness: dots keep starting and stopping across the sphere */
(async function(){for(;;){await wait(260);var nb=nodes.filter(function(nd){return nd.busy&&!nd.act&&!nd.dk}).length,c=D.pick(nodes.filter(function(nd){return !nd.act&&!nd.dk}));
 if(c)setBusy(c,nb<N*.48?true:!c.busy?false:false)}})();
/* rhythmic beats: every 1.6s one to three specialists stop typing and answer together */
if(o.beats!==false)(async function(){await wait(500);for(;;){await wait(1600);var k=1+(Math.random()<.55)+(Math.random()<.3),picks=[];
 if(Math.random()<.72){var dd=nextDarnell(o.minD);if(dd)picks.push(dd)}
 var pool=D.shuffle(nodes.filter(function(nd){return !nd.dk&&nd.busy&&eligible(nd,o.minD)}));
 while(picks.length<k&&pool.length)picks.push([pool.pop(),genResp()]);
 picks.forEach(function(p,ix){setTimeout(function(){activate(p[0],p[1],p[1].dk?2300:1400)},ix*70)})}})();
return api};</script>'''

def shell_s(i, css, vis, js):
    name, desc = SP[i-1]
    prv = f'<a href="desk-sphere-{i-1}.html">← {SP[i-2][0]}</a>' if i > 1 else '<a href="desk-var-4.html">← The orbit</a>'
    nxt = f'<a href="desk-sphere-{i+1}.html">{SP[i][0]} →</a>' if i < 3 else '<a href="desk-variations.html">All variations →</a>'
    body = f'''<style>{BASE_CSS}{SCSS}{css}</style>
<section class="dv"><div class="dvw">
<div class="dvk">Busy sphere {i} of 3 · {name}</div>
<h2 class="beat"><span class="n">2</span><span>His desk</span></h2>
<p class="lede2">{LEDE}</p>
{vis}
<p class="cap2">{CAP}</p>
<nav class="dvnav" aria-label="Sphere explorations">{prv}<a class="all" href="desk-spheres.html">All three</a>{nxt}</nav>
</div></section>'''
    page(f'desk-sphere-{i}.html', f'First Officer · His desk, busy sphere {i}: {name} (mockup)', body,
         desc='Mockup of the His desk step as a busy sphere. Fictional owner, estimated figures.', src='home',
         tail=BASE_JS + ENGINE + '<script>window.GEN=' + json.dumps(GEN) + ';</script>' + js)

CARD_JS = r'''<script>window.RC=function(c,serif){return '<div class="rh">'+DV.lg(c.n)+'<b>'+DV.names[c.n]+'</b><span class="arr">to First Officer</span><span class="pg" style="--c:'+DV.pc[c.p]+'">'+c.p+'</span></div><div class="rt'+(serif?' serif':'')+'">'+c.t+'</div>'};</script>'''

# ---------------------------------------------------------------- 1. rotating globe + feed
def sp1():
    c0 = CON[0]
    feed0 = ''.join(f'<li class="fg">{lg(n)}<b>{NAME[n]}</b><span>{s}</span><i>✓</i></li>' for n, s in [(18,'Rules checked'),(25,'Partner awards'),(9,'Watching bonuses'),(1,'Card offers scan')])
    vis = f'''<div class="sx" id="s1">{stage()}
<div class="rcard"><div class="rk"><span class="lv"></span>Latest for Darnell</div><div class="fi fade">{card(c0)}</div></div>
<div class="also2 fade">Just now: <b>Delta</b> rules checked · <b>Aeroplan</b> partner awards</div>
<aside class="side"><div class="rcard"><div class="rk"><span class="lv"></span>Latest for Darnell</div><div class="fi fade">{card(c0)}</div></div>
<div class="fcol"><div class="fh"><b>Live from the desk</b><span>50+ programs</span></div><ol class="fl">{feed0}</ol></div></aside>
<p class="ssub">{SUB}</p></div>'''
    css = '''
.fcol{background:#faf8fb;border-radius:18px;box-shadow:inset 0 0 0 1px #eee9f1;padding:14px 16px 6px}
.fh{display:flex;align-items:baseline;justify-content:space-between;font:700 13px 'DM Sans',sans-serif;color:var(--ink);margin:0 0 8px}.fh span{font:500 12px 'DM Sans',sans-serif;color:var(--mute)}
.fl{list-style:none;margin:0;padding:0;height:286px;overflow:hidden;-webkit-mask-image:linear-gradient(#000 72%,transparent);mask-image:linear-gradient(#000 72%,transparent)}
.fl li{display:flex;align-items:center;gap:9px;padding:7px 2px;border-bottom:1px solid #f0ecf2;font:500 13px 'DM Sans',sans-serif;color:var(--mute);animation:fin .45s cubic-bezier(.2,.7,.2,1) both}
@keyframes fin{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:none}}
.fl li .lg{--s:26px}.fl li b{color:var(--ink);font-weight:700;white-space:nowrap}.fl li>span:not(.lg){flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.fl li i{font-style:normal;font-weight:700;color:#FA1896;font-size:12px}
.fl li.fd{align-items:flex-start}.fl li.fd>span:not(.lg){white-space:normal;color:var(--body);line-height:1.4}.fl li.fd i{color:#fff;background:var(--c);border-radius:999px;padding:3px 7px;font-size:10px;line-height:1}
'''
    js = CARD_JS + r'''<script>(function(){var D=DV,root=document.getElementById('s1');var cards=D.$$('.rcard .fi',root),also=D.$('.also2',root),fl=D.$('.fl',root),recent=[];
function onAct(nd,r){if(r.dk){cards.forEach(function(c){D.swap(c,RC(r.c))});
  fl.insertAdjacentHTML('afterbegin','<li class="fd" style="--c:'+D.pc[r.p]+'">'+D.lg(nd.n)+'<b>'+D.names[nd.n]+'</b><span>'+r.c.s+'</span><i>'+r.p+'</i></li>')}
 else{fl.insertAdjacentHTML('afterbegin','<li class="fg">'+D.lg(nd.n)+'<b>'+D.names[nd.n]+'</b><span>'+r.s+'</span><i>\u2713</i></li>');
  recent.unshift('<b>'+D.names[nd.n]+'</b> '+r.s.toLowerCase());recent=recent.slice(0,2);D.swap(also,'Just now: '+recent.join(' · '))}
 while(fl.children.length>9)fl.lastElementChild.remove()}
SPH(root,{mode:'globe',rot:.12,a0:.4,gen:GEN,onAct:onAct,minD:.6});
})();</script>'''
    shell_s(1, css, vis, js)

# ---------------------------------------------------------------- 2. packed cluster + bubbles
def sp2():
    c0 = CON[6]
    shorts = ''.join(f'<li style="--c:{PC[c[1]]}"><i></i>{c[3]}</li>' for c in CON[:5])
    vis = f'''<div class="sx" id="s2">{stage()}
<div class="rcard"><div class="rk"><span class="lv"></span>First Officer · latest for Darnell</div><div class="fi fade">{card(c0, True)}</div></div>
<aside class="side"><div class="rcard"><div class="rk"><span class="lv"></span>First Officer · latest for Darnell</div><div class="fi fade">{card(c0, True)}</div></div>
<div class="sh2"><b>In Darnell's plan today</b><ul class="sl2">{shorts}</ul></div></aside>
<p class="ssub">{SUB}</p></div>'''
    css = '''
#s2 .sbody{inset:1%;background:radial-gradient(circle at 50% 50%,#fff 0,#fff3f9 30%,#f7f0f8 62%,#efe8f2 100%)}
.bb{position:absolute;left:50%;top:50%;z-index:550;pointer-events:none;background:#fff;border-radius:999px;padding:5px 10px 5px 8px;font:600 11px/1.2 'DM Sans',sans-serif;color:var(--body);white-space:nowrap;box-shadow:0 0 0 1px #ebe6ee,0 10px 22px -12px rgba(20,18,22,.35);display:flex;align-items:center;gap:6px;animation:bbin .38s cubic-bezier(.2,.8,.2,1.2) both}
.bb i{width:7px;height:7px;border-radius:50%;background:var(--c,#bdb6c4);flex:none}
.bb.dk{box-shadow:0 0 0 1.5px var(--c),0 12px 24px -12px var(--c);color:var(--ink);font-weight:700}
.bb b{font-weight:700;color:var(--ink)}
.bb.out{animation:bbout .35s ease both}
@keyframes bbin{from{opacity:0;scale:.7}to{opacity:1;scale:1}}@keyframes bbout{to{opacity:0;scale:.9}}
.sh2{background:#faf8fb;border-radius:18px;box-shadow:inset 0 0 0 1px #eee9f1;padding:14px 16px}
.sh2>b{display:block;font:700 13px 'DM Sans',sans-serif;color:var(--ink);margin:0 0 10px}
.sl2{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:7px;height:104px;overflow:hidden;align-content:flex-start}
.sl2 li{display:inline-flex;align-items:center;gap:6px;background:#fff;border-radius:999px;box-shadow:0 0 0 1px #ece7ef;padding:6px 11px;font:600 12.5px 'DM Sans',sans-serif;color:var(--ink);animation:bbin .4s both}
.sl2 li i{width:7px;height:7px;border-radius:50%;background:var(--c)}
@media(min-width:1024px){.bb{font-size:12px;padding:6px 12px 6px 9px}}
@media (prefers-reduced-motion:reduce){.bb,.sl2 li{animation:none}}
'''
    js = CARD_JS + r'''<script>(function(){var D=DV,root=document.getElementById('s2');var cards=D.$$('.rcard .fi',root),sl=D.$('.sl2',root);
var api,desk=function(){return innerWidth>=1024};
function bubble(nd,r,hold){var st=api.stage,W=st.clientWidth,el=document.createElement('div');el.className='bb'+(r.dk?' dk':'');el.style.setProperty('--c',D.pc[r.p]);
 el.innerHTML='<i></i>'+(r.dk?(desk()?'<b>'+D.names[nd.n]+'</b> '+r.c.s:r.c.s):(desk()?'<b>'+D.names[nd.n]+'</b> '+r.s:r.s));st.appendChild(el);
 var bw=el.offsetWidth,bh=el.offsetHeight,half=api.B()*(.42+.5*nd.d)*1.2/2,x=nd.px>=0?nd.px+half+6:nd.px-half-6-bw;
 x=Math.max(-W/2+2,Math.min(W/2-bw-2,x));var y=Math.max(-W/2+2,Math.min(W/2-bh-2,nd.py-bh/2));
 el.style.transform='translate('+x.toFixed(1)+'px,'+y.toFixed(1)+'px)';
 if(!D.RM)setTimeout(function(){el.classList.add('out');setTimeout(function(){el.remove()},360)},hold)}
function onAct(nd,r){bubble(nd,r,r.dk?2300:1500);if(r.dk){cards.forEach(function(c){D.swap(c,RC(r.c,true))});
 D.$$('li',sl).forEach(function(li){if(li.textContent==r.c.s)li.remove()});sl.insertAdjacentHTML('afterbegin','<li style="--c:'+D.pc[r.p]+'"><i></i>'+r.c.s+'</li>');while(sl.children.length>8)sl.lastElementChild.remove()}}
api=SPH(root,{mode:'cluster',gen:GEN,onAct:onAct,minD:0});
})();</script>'''
    shell_s(2, css, vis, js)

# ---------------------------------------------------------------- 3. wave sweeps + counters
def sp3():
    c0 = CON[3]
    START = {'Earn':214,'Burn':167,'Return':129,'Learn':238}
    cnt = ''.join(f'<div class="cn" data-p="{p}" style="--c:{PC[p]}"><b>{START[p]}</b><span>{p}</span></div>' for p in PILLARS)
    strip = f'<div class="cstrip"><div class="ck"><span class="lv"></span>Answers on the desk today</div><div class="cns">{cnt}</div></div>'
    vis = f'''<div class="sx" id="s3">{strip}{stage('<div class="band"></div>')}
<div class="rcard"><div class="rk"><span class="lv"></span>Latest for Darnell</div><div class="fi fade">{card(c0)}</div></div>
<div class="also2 sw fade">This sweep: <b>6</b> answers</div>
<aside class="side">{strip}<div class="rcard"><div class="rk"><span class="lv"></span>Latest for Darnell</div><div class="fi fade">{card(c0)}</div></div>
<div class="sweep"><b>This sweep</b><div class="swl"></div></div></aside>
<p class="ssub">{SUB}</p></div>'''
    css = '''
.band{position:absolute;top:0;bottom:0;left:50%;width:96px;margin-left:-48px;background:linear-gradient(90deg,rgba(250,24,150,0),rgba(250,24,150,.07) 30%,rgba(250,24,150,.16) 50%,rgba(250,24,150,.07) 70%,rgba(250,24,150,0));will-change:transform;opacity:0;transition:opacity .3s}
.band.on{opacity:1}
.cstrip{width:100%;max-width:520px;background:#fff;border-radius:16px;box-shadow:0 0 0 1px #ece7ef;padding:10px 12px}
.ck{display:flex;align-items:center;gap:6px;font:600 10.5px 'JetBrains Mono',monospace;letter-spacing:.08em;text-transform:uppercase;color:#a0889a;margin:0 0 6px}
.ck .lv,.rk .lv{width:6px;height:6px;border-radius:50%;background:#12834E;box-shadow:0 0 0 3px rgba(18,131,78,.14)}
.cns{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.cn{display:flex;flex-direction:column;align-items:center;border-radius:10px;padding:4px 0;transition:background .3s}
.cn b{font:700 20px/1.1 'DM Sans',sans-serif;color:var(--c);font-variant-numeric:tabular-nums}.cn span{font:600 11px 'DM Sans',sans-serif;color:var(--mute)}
.cn.up{background:color-mix(in srgb,var(--c) 9%,#fff)}
.sweep{background:#faf8fb;border-radius:18px;box-shadow:inset 0 0 0 1px #eee9f1;padding:14px 16px}
.sweep>b{display:block;font:700 13px 'DM Sans',sans-serif;color:var(--ink);margin:0 0 10px}
.swl{display:flex;flex-wrap:wrap;gap:8px;height:104px;align-content:flex-start;overflow:hidden}
.swl .swc{display:inline-flex;align-items:center;gap:6px;font:600 12px 'DM Sans',sans-serif;color:var(--body);background:#fff;border-radius:999px;box-shadow:0 0 0 1px #ece7ef;padding:4px 10px 4px 4px;animation:fin2 .35s both}
.swl .swc .lg{--s:20px}.swl .swc i{width:6px;height:6px;border-radius:50%;background:var(--c)}
@keyframes fin2{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:none}}
@media(min-width:1024px){.sx>.cstrip{display:none}.side .cstrip{max-width:none;padding:14px 16px}.cn b{font-size:26px}.cn span{font-size:12px}}
@media (prefers-reduced-motion:reduce){.swl .swc{animation:none}}
'''
    js = CARD_JS + r'''<script>(function(){var D=DV,root=document.getElementById('s3');var cards=D.$$('.rcard .fi',root),band=D.$('.band',root),sw=D.$('.also2.sw',root),swl=D.$('.swl',root),cnt=0;
function bump(p){D.$$('.cn[data-p="'+p+'"]',root).forEach(function(c){var b=D.$('b',c);b.textContent=+b.textContent+1;c.classList.add('up');clearTimeout(c._t);c._t=setTimeout(function(){c.classList.remove('up')},500)})}
var fresh=false;function onAct(nd,r){if(fresh){fresh=false;swl.innerHTML=''}bump(r.p);cnt++;sw.innerHTML='This sweep: <b>'+cnt+'</b> answers';
 swl.insertAdjacentHTML('beforeend','<span class="swc" style="--c:'+D.pc[r.p]+'">'+D.lg(nd.n)+(r.dk?r.c.s:r.s)+'<i></i></span>');while(swl.children.length>9)swl.firstElementChild.remove();
 if(r.dk)cards.forEach(function(c){D.swap(c,RC(r.c))})}
var ph='rest',pt=0,bx=0,dkUsed=false,sweeps=0;
function onFrame(dt,T,api){pt+=dt;var R=api.R(),bw=band.parentNode.clientWidth/2;
 if(ph=='rest'&&pt>.9){ph='sweep';pt=0;cnt=0;fresh=true;band.classList.add('on');dkUsed=false;sweeps++;api.nodes.forEach(function(nd){nd.sw=false})}
 if(ph=='sweep'){var dur=2.3,u=pt/dur,e=u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2;bx=-bw-60+(2*bw+120)*e;band.style.transform='translateX('+bx.toFixed(1)+'px)';
  api.nodes.forEach(function(nd){if(nd.sw||nd.act)return;if(Math.abs(nd.px-bx)<16){nd.sw=true;
   if(nd.dk&&!dkUsed&&api.eligible(nd,.45)){var L=D.con.filter(function(c){return c.n==nd.n});nd.k=(nd.k||0)+1;var c=L[nd.k%L.length];dkUsed=true;api.activate(nd,{dk:true,c:c,p:c.p},2300)}
   else if(!nd.dk&&nd.busy&&api.eligible(nd,.5)&&Math.random()<.55)api.activate(nd,api.genResp(),1300)}});
  if(u>=1){ph='rest';pt=0;band.classList.remove('on')}}}
SPH(root,{mode:'globe',rot:.07,a0:1.1,gen:GEN,onAct:onAct,onFrame:onFrame,beats:false,
 onStatic:function(){}});
})();</script>'''
    shell_s(3, css, vis, js)

def gallery_s():
    cards = ''
    for i, (name, desc) in enumerate(SP, 1):
        cards += f'''<a class="gc" href="desk-sphere-{i}.html"><div class="gth"><img class="gd" src="_shots/sphere-{i}-1440.jpg" alt="Sphere {i} at desktop width" loading="lazy"><img class="gm" src="_shots/sphere-{i}-390.jpg" alt="Sphere {i} on a phone" loading="lazy"></div>
<div class="gt"><span class="gn">{i}</span><div><b>{name}</b><p>{desc}</p><span class="go">Open sphere {i} →</span></div></div></a>'''
    body = f'''<style>{BASE_CSS}{dv.GAL_CSS}</style>
<section class="dv"><div class="dvw">
<div class="dvk">Mockups · Step 2, His desk · Variation 4 explored</div>
<h2 class="beat"><span class="n">2</span><span>His desk: the busy sphere</span></h2>
<p class="lede2">Variation 4, the orbit, filled in. Every one of the 50 program logos sits on a sphere around First Officer. Many keep typing in the background; on a steady beat some go quiet, light up and answer, and First Officer pulses back. No connector lines.</p>
<div class="gl2">{cards}</div>
<p class="cap2">{CAP}</p>
<nav class="dvnav"><a href="desk-var-4.html">← Variation 4. The orbit</a><a class="all" href="desk-variations.html">All five variations</a><span></span></nav>
</div></section>'''
    page('desk-spheres.html', 'First Officer · His desk, busy sphere explorations (mockup)', body, desc='Three busy-sphere explorations of the His desk step.', src='home')

if __name__ == '__main__':
    sp1(); sp2(); sp3(); gallery_s()
