/* First Officer hero (Oct 22, 2026). Desktop engine = mockup hero-v9 (layout B), mobile engine = mockup hero-v10 (direction B, three beats).
   Data and copy live in hero/fo-hero-data.js. Changes to the mockup engines: the "Important information" link no longer
   throws when the page has no #disc section, and the layout waits for the page's async web fonts before measuring. */
(function(){
/* the live page loads its web fonts asynchronously, so wait for the hero's faces before measuring the layout (max 4s) */
function FOREADY(){if(!document.fonts)return Promise.resolve();var t0=Date.now();
 var has=function(f){var ok=false;document.fonts.forEach(function(x){if(x.family.replace(/["']/g,'')===f)ok=true});return ok};
 return new Promise(function(res){(function w(){if((has('DM Sans')&&has('DM Serif Display')&&has('Inter'))||Date.now()-t0>4000){
  Promise.all(['400 16px "DM Sans"','700 16px "DM Sans"','400 16px "DM Serif Display"','400 16px Inter','600 16px Inter','700 16px Inter'].map(function(f){return document.fonts.load(f).catch(function(){})})).then(function(){return document.fonts.ready}).then(res,res)}else setTimeout(w,50)})()})}
var Q=new URLSearchParams(location.search);var MOB=Q.has('m')?Q.get('m')==='1':innerWidth<760;var C=window.CFG;if(!C)return;
/* desktop shows the v9 wording where the v9 and v10 data differ (one short line in one persona) */
if(!MOB&&C.personasD){C.personas.forEach(function(p){var o=C.personasD[p.s];if(o)for(var k in o)p.beats[+k]=o[k];});}
if(MOB){
(function(){
const C=window.CFG,PS=C.personas,NS='http://www.w3.org/2000/svg';
const Q=new URLSearchParams(location.search);
const host=document.getElementById('fohero');const root=host.attachShadow({mode:'open'});window.HROOT=root;
root.innerHTML=`<style>${C.css}</style><div id="hero"><div class="tint"></div><div id="stage"></div></div>`;
const $=(s,r=root)=>r.querySelector(s),$$=(s,r=root)=>[...r.querySelectorAll(s)];
let seed=Q.has('seed')?+Q.get('seed'):Math.floor(Math.random()*1e9);
function rnd(){seed=(seed*1664525+1013904223)%4294967296;return seed/4294967296}
const R=(a,b)=>a+rnd()*(b-a),pick=a=>a[Math.floor(rnd()*a.length)];
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(rnd()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const MOB=Q.has('m')?Q.get('m')==='1':innerWidth<760;
const B=$('#hero');B.classList.add(MOB?'M':'D');document.body.classList.add(MOB?'foM':'foD');
const LOGO=n=>C.logos[n],NAME=C.names;
const FF=+(Q.get('ff')||0),STOP=Q.has('stop')?+Q.get('stop'):-1;
const SH=MOB?{W:390,H:1500}:{W:1440,H:1230};
const stage=$('#stage'),hero=$('#hero');
function fit(){const s=Math.min(innerWidth,document.documentElement.clientWidth||innerWidth)/SH.W;stage.style.width=SH.W+'px';stage.style.height=SH.H+'px';stage.style.transform=`scale(${s})`;hero.style.height=SH.H*s+'px'}fit();addEventListener('resize',fit);
// ---------- hero photo: the live page's own rotating pool, never the same twice in a row
(function(){const pool=C.pool;let last=+localStorage.getItem('fo9_bg'),i;do{i=Math.floor(Math.random()*pool.length)}while(i===last&&pool.length>1);if(Q.has('bg'))i=+Q.get('bg')%pool.length;localStorage.setItem('fo9_bg',i);const top=document.getElementById('top');top&&top.style.setProperty('--ph',`url(${pool[i]})`)})();
const H=C.copy;
function el(tag,cls,html,st,par){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;if(st)Object.assign(e.style,st);(par||stage).appendChild(e);return e}
const px=v=>v+'px';
const SUBT=(window.FO_SUBHEAD||H.sub);
function subFill(d){const bl=SUBT.split(/\n\s*\n/).map(x=>x.trim()).filter(Boolean);bl.forEach((t,i)=>{const p=document.createElement('p');p.textContent=t;if(bl.length>1&&i===bl.length-1)p.className='tag';d.appendChild(p)});return d}
function fitH1(h,w){h.style.whiteSpace='nowrap';let f=parseFloat(h.style.fontSize);while(h.scrollWidth>w&&f>12){f-=.5;h.style.fontSize=f+'px'}return h}
// ---------- static copy (positions finalised in layout() once fonts are ready)
const TX=MOB?18:148;
const KICK=el('div','kick','<span class="ld"></span>Earn · Burn · Return · Learn',{left:px(TX),top:px(MOB?22:34)});
const H1=el('h1','',H.h1,{left:px(TX),top:px(MOB?64:74),fontSize:MOB?'30px':'52px'});
const SUB0=subFill(el('div','sub',null,MOB?{left:px(TX),width:'354px'}:{left:px(TX),width:'460px'}));
let B2T='';const SUB=SUB0;
const CTAS=el('div','ctas','<a href="book.html?from=index" style="display:flex;text-decoration:none"><b class="c1">Get your desk</b></a><a href="how.html" style="display:flex;text-decoration:none"><b class="c2">See how it works</b></a>',MOB?{left:'16px',right:'16px',justifyContent:'center'}:{left:px(TX)});
const DESKH=el('div','deskh',MOB?`<span class="k"><span class="lv"></span>First Officer's specialists · 50+ programs, trained on new data nightly</span>`:`<span class="k"><span class="lv"></span><b>First Officer's specialists</b><em>50+ programs, trained on new data nightly</em></span>`,MOB?{left:'0',right:'0',justifyContent:'center'}:{left:px(TX)});
const MICRO=el('div','micro',MOB?H.microM:H.micro,MOB?{left:'18px',width:'354px',textAlign:'center'}:{left:'120px',width:'1200px',textAlign:'center'});
const TMK=el('div','tmk',H.tmk,MOB?{left:'18px',width:'354px',textAlign:'center'}:{left:'120px',width:'1200px',textAlign:'center'});
// ---------- geometry (set in layout)
const G={};
let OWN=[];
function layout(){
 if(!MOB){
  fitH1(H1,780);const hb=74+H1.offsetHeight;
  SUB.style.top=px(hb+18);const sb=hb+18+SUB.offsetHeight;
  CTAS.style.top=px(sb+24);const cb=sb+24+CTAS.offsetHeight;
  DESKH.style.top=px(cb+20);const db=cb+20+DESKH.offsetHeight;
  OWN=[[TX,db+14,466]];
  Object.assign(G,{FS:72,PH:[972,22,.78],CARD:[632,hb+22,326],X0:120,X1:1320,ROW:98});
  G.FO=[795,0];G.Y0=0;G.Y1=0;SH.H=G.Y1+112;fit();[web,pul].forEach(s=>s.setAttribute('height',SH.H));MICRO.style.top=px(G.Y1+18);TMK.style.top=px(G.Y1+18+MICRO.offsetHeight+4);
 }else{
  fitH1(H1,354);const hb=64+H1.offsetHeight;
  SUB.style.top=px(hb+14);const sb=hb+14+SUB.offsetHeight;DESKH.style.display='none';
  Object.assign(G,{B1:sb+40,CARD:[16,0,358],FS:48,PH:[(390-417*.72)/2,0,.72],PHH:876*.72,FO:[195,0]});
 }
}
// ---------- layers
const web=document.createElementNS(NS,'svg');web.setAttribute('class','web');stage.appendChild(web);
const pul=document.createElementNS(NS,'svg');pul.setAttribute('class','pul');stage.appendChild(pul);
[web,pul].forEach(s=>{s.setAttribute('width',SH.W);s.setAttribute('height',SH.H)});
const floor=el('div','floor','',{position:'absolute',left:0,top:0});
let FOel,FOL,card,ph,ci,chat,BT=[],FEED,CAP2;
function buildFixed(){
 FOel=el('div','fo',`<img src="${C.foi}">`,{left:px(G.FO[0]-G.FS/2),top:px(G.FO[1]-G.FS/2),width:px(G.FS),height:px(G.FS)});
 if(!MOB)FOL=el('div','fol','<b class="l1">First Officer</b><span class="l2">At the Desk</span>',{left:px(G.FO[0]),top:px(G.FO[1]-G.FS/2-50)});
 else{FOL=el('div','fol b','<b class="l1">First Officer</b><span class="l2">At the Desk</span>',{left:'195px',top:'0px'});
  BT=[1,2,3].map(i=>el('div','beat','',{left:'18px',top:'0px'}));FEED=el('div','feed10','',{left:'18px',top:'0px',width:'330px'});CAP2=el('div','cap2','',{left:'18px',top:'0px',width:'330px'});CAP2.style.display='none'}
 card=el('div','',null,{});card.id='card';
 card.style.left=px(G.CARD[0]);card.style.top=px(G.CARD[1]);card.style.width=px(G.CARD[2]);
 ph=el('div','',C.phone,{left:px(G.PH[0]),top:px(G.PH[1]||0),transform:`scale(${G.PH[2]})`});ph.id='ph';
 ci=$('#ci');chat=$('#chat');
 setView(VIEW);
 $('#sfo').onclick=e=>{rip(e.currentTarget);setView('fo',1)};$('#sbtd').onclick=e=>{rip(e.currentTarget);setView('btd',1)};
 $$('#tabs > div').forEach(d=>d.onclick=()=>{const t=d.dataset.t;rip(d);HOMEV=t==='home';const pool=PS.filter(p=>(t==='home'||p.tab===t)&&p!==CUR);load(PS.indexOf(pool[Math.floor(Math.random()*pool.length)]),0)});
}
let VIEW=Q.get('view')==='btd'?'btd':'fo'; // Oct 22 (approved): opens on First Officer; ?view=btd still opens Behind the desk
function setView(v,anim){ph.classList.toggle('vfo',v==='fo');ph.classList.toggle('vbtd',v!=='fo');$('#sfo').classList.toggle('on',v==='fo');$('#sbtd').classList.toggle('on',v!=='fo');if(anim){chat.classList.add('blink');setTimeout(()=>chat.classList.remove('blink'),260)}VIEW=v}
function rip(e){const r=e.getBoundingClientRect(),s=e.closest('.scr').getBoundingClientRect(),k=s.width/393;const d=document.createElement('div');d.className='rip';d.style.left=(r.left+r.width/2-s.left)/k+'px';d.style.top=(r.top+r.height/2-s.top)/k+'px';e.closest('.scr').appendChild(d);setTimeout(()=>d.remove(),700)}
// ---------- agents
let AG={},POS={},REL=[],LOCK={},CUR=null,SPOT=new Set();
const relSt=(p,n,role)=>({Earn:'Earn plan',Burn:'Quoting',Return:'Value check',Learn:'Briefing'}[role]||'On it');
const WK='<span class="wk"><i></i><i></i><i></i></span>';
function buildFloor(p){floor.innerHTML='';web.innerHTML='';pul.innerHTML='';AG={};POS={};LOCK={};SPOT=new Set();
 REL=p.rel.map(r=>r[0]);REL.forEach(n=>LOCK[n]=1);const acc=C.acc[p.tab][0];let W='';
 if(!MOB){
  const {X0,X1,Y0,ROW}=G,NC=13,cw=(X1-X0)/NC,rows=[0,1,2,3].map(r=>Y0+34+r*ROW);G.cw=cw;
  const groups=[['Banks',[1,2,3,4,5,6,7,8],0,2],['Hotels',[9,10,11,12,13,14,15,16],2,2],['US airlines',[17,18,19,20,21,22,23,24],4,2],['Partner airlines',Array.from({length:26},(_,i)=>i+25),6,7]];
  groups.forEach(([name,ids,c0,nc])=>{const x0=X0+c0*cw+4,x1=X0+(c0+nc)*cw-4;
   floor.insertAdjacentHTML('beforeend',`<div class="pod" style="left:${x0}px;top:${Y0}px;width:${x1-x0}px;height:${G.Y1-Y0}px"><div class="podh"><span class="lv"></span>${name}<i>${ids.length} working</i></div>${nc>=4?'<div class="feed"></div>':''}</div>`);
   const slots=[];for(let r=0;r<4;r++)for(let c=0;c<nc;c++)slots.push([X0+(c0+c+.5)*cw,rows[r]]);
   const rl=ids.filter(i=>REL.includes(i)),free=slots.slice();
   const relCols=nc>=4?shuffle([1,2,3,4,5]).slice(0,rl.length).sort((a,b)=>a-b):[0,1];
   rl.forEach((n,i)=>{const si=i<relCols.length?relCols[i]:nc+i;POS[n]=slots[si];free.splice(free.indexOf(slots[si]),1)});
   shuffle(ids.filter(i=>!REL.includes(i))).forEach((n,i)=>POS[n]=free[i]);
   // quiet neighbour links, drawn under the tiles
   ids.forEach(n=>{const[x,y]=POS[n];ids.forEach(m=>{const q=POS[m];if(Math.abs(q[1]-y)<5&&q[0]-x>0&&q[0]-x<cw*1.2&&rnd()<.45&&!REL.includes(n)&&!REL.includes(m)){W+=`<path class="bw" d="M${x+22},${y} C${x+cw*.4},${y-16} ${q[0]-cw*.4},${q[1]-16} ${q[0]-22},${q[1]}" stroke="#d9d3de" stroke-width="1.2" fill="none"/>`}})})});
  // First Officer to the specialists on this request: one smooth curve each, entering the avatar from above
  const fb=G.FO[1]+G.FS/2;
  REL.forEach(n=>{const[x,y]=POS[n],ty=y-24;const dx=x-G.FO[0];const sx=G.FO[0]+Math.max(-22,Math.min(22,dx*.06));
   W+=`<path id="w${n}" d="M${sx},${fb-4} C${sx},${fb+64} ${x},${ty-44} ${x},${ty}" stroke="${acc}" stroke-width="2.2" stroke-linecap="round" fill="none"/>`});
  // the one pink line: First Officer to the app
  const pxL=G.PH[0]+4,py=Math.min(G.FO[1]-6,G.PH[1]+876*G.PH[2]-110);W+=`<path id="wout" d="M${G.FO[0]+G.FS/2-2},${G.FO[1]} C${G.FO[0]+G.FS/2+60},${G.FO[1]} ${pxL-60},${py} ${pxL},${py}" stroke="#FA1896" stroke-width="2.6" stroke-linecap="round" fill="none"/>`;
  for(let n=1;n<=50;n++){const[x,y]=POS[n],rel=REL.includes(n),s=rel?48:42,w=Math.round(cw)-4;
   const st=rel?relSt(p,n,p.rel.find(r=>r[0]===n)[1]):C.tasks[n][0];
   floor.insertAdjacentHTML('beforeend',`<div class="ag${rel?' rel':''}" data-n="${n}" style="left:${x-w/2}px;top:${y-s/2}px;width:${w}px"><div class="lg" style="width:${s}px;height:${s}px"><img src="${LOGO(n)}"></div><div class="tx"><b${rel&&NAME[n].length>12?' class="lnm"':''}>${NAME[n]}</b>${rel?`<span class="st">${st}</span>`:`<span class="st"></span>${WK}`}</div></div>`)}
 }else{
  // beat 2: a hex field of the whole desk, First Officer in a clearing, a clear vertical spine for the threads in and out
  const cy=G.CY,slots=[],dx=44,dy=41;
  for(let rI=-6;rI<=6;rI++){const yy=cy+rI*dy,off=(rI&1)?dx/2:0;for(let x=195+off-dx*5;x<=380;x+=dx){if(x<24||x>366)continue;const ex=(x-195)/176,ey=(yy-cy)/240;if(ex*ex+ey*ey>1)continue;const d=Math.hypot(x-195,yy-cy);if(d<58)continue;if(yy>cy&&Math.abs(x-195)<20)continue;if(Math.abs(x-195)<114&&yy>cy+10&&yy<cy+100)continue;slots.push({x,y:yy,d})}}
  slots.sort((a,b)=>a.d-b.d);const keep=slots.slice(0,50);G.TOPY=Math.min(...keep.map(q=>q.y));G.BOTY=Math.max(...keep.map(q=>q.y));window.NK=[keep.length,slots.length];
  const ang=q=>Math.atan2(q.y-cy,q.x-195);const ring=keep.filter(q=>q.d<100).sort((a,b)=>ang(a)-ang(b));const o=Math.floor(rnd()*ring.length);
  REL.forEach((n,i)=>{const q=ring[(o+Math.round(i*ring.length/REL.length))%ring.length];q.n=n});
  const pool=shuffle(Array.from({length:50},(_,i)=>i+1).filter(n=>!REL.includes(n)));keep.filter(q=>!q.n).forEach(q=>q.n=pool.shift());
  keep.forEach(q=>POS[q.n]=[q.x,q.y]);
  // quiet links between neighbours, with travelling pulses
  keep.forEach(a=>keep.forEach(b=>{if(a.n<b.n&&!REL.includes(a.n)&&!REL.includes(b.n)){const L=Math.hypot(a.x-b.x,a.y-b.y);if(L<50&&rnd()<.3){const ux=(b.x-a.x)/L,uy=(b.y-a.y)/L;W+=`<path class="bw" d="M${a.x+ux*16},${a.y+uy*16} L${b.x-ux*16},${b.y-uy*16}" stroke="#e4dfe9" stroke-width="1.2" fill="none"/>`}}}));
  REL.forEach(n=>{const[x,y]=POS[n];const a=Math.atan2(y-cy,x-195);W+=`<path id="w${n}" d="M${195+28*Math.cos(a)},${cy+28*Math.sin(a)} L${x-20*Math.cos(a)},${y-20*Math.sin(a)}" stroke="${acc}" stroke-width="2.2" stroke-linecap="round" fill="none"/>`});
  // the thread from the owner's dossier into First Officer, and the one pink line from First Officer into the app
  W+=`<path id="wthr" d="M195,${G.CARD[1]+40} L195,${G.TOPY-30}" stroke="${acc}" stroke-width="2" stroke-linecap="round" fill="none"/><circle cx="195" cy="${G.TOPY-30}" r="3.4" fill="${acc}"/>`;
  const px2=G.PH[0]+417*G.PH[2]-62,py=G.PH[1];
  W+=`<path id="wout" d="M195,${cy+27} L195,${G.BOTY+24} C195,${G.BOTY+60} 372,${G.BOTY+42} 372,${G.BOTY+92} L372,${py-56} C372,${py-18} ${px2},${py-30} ${px2},${py+3}" stroke="#FA1896" stroke-width="2.6" stroke-linecap="round" fill="none"/>`;
  keep.forEach(q=>{const n=q.n,rel=REL.includes(n),sz=rel?32:26;floor.insertAdjacentHTML('beforeend',`<div class="mag${rel?' rel':''}" data-n="${n}" style="left:${q.x-20}px;top:${q.y-sz/2}px;width:40px"><div class="lg" style="width:${sz}px;height:${sz}px"><img src="${LOGO(n)}"></div>${WK}</div>`)});
 }
 web.innerHTML=W;$$('[data-n]',floor).forEach(e=>AG[+e.dataset.n]=e);
 $$('.wk',floor).forEach(c=>c.style.setProperty('--dl',-R(0,1.2).toFixed(2)+'s'));
 BW=$$('path.bw',web).map(p=>({p,L:p.getTotalLength(),ph:rnd(),sp:R(.1,.25)*(rnd()<.5?1:-1),c:null}));
 BW.forEach(b=>{if(rnd()<.55){b.c=document.createElementNS(NS,'circle');b.c.setAttribute('r',MOB?'1.8':'2.3');b.c.setAttribute('fill',rnd()<.5?acc:'#a59fad');b.c.setAttribute('fill-opacity','.85');web.appendChild(b.c)}});
 if(!MOB)initSpot();
}
let BW=[];
function loop(t){BW.forEach(b=>{if(!b.c)return;const k=((b.ph+t/1000*b.sp)%1+1)%1;const q=b.p.getPointAtLength(k*b.L);b.c.setAttribute('cx',q.x.toFixed(1));b.c.setAttribute('cy',q.y.toFixed(1))});requestAnimationFrame(loop)}requestAnimationFrame(loop);
// ---------- status lines: a readable handful at a time, everyone else shows working dots
function showSt(n,t){const e=AG[n];if(!e)return;const s=e.querySelector('.st');if(!s)return;
 if(STOP>=0&&!window.READY){s.textContent=t;e.classList.add('say');return}
 if(e.classList.contains('say')){s.classList.add('out');setTimeout(()=>{s.textContent=t;s.classList.remove('out')},260)}else{s.textContent=t;e.classList.add('say')}}
function hideSt(n){const e=AG[n];if(e)e.classList.remove('say')}
const SHORT=n=>NAME[n].length<=12;const ST1=n=>{const t=C.tasks[n].filter(x=>x.length<=15);return t.length?pick(t):C.tasks[n][0]};
function initSpot(){const ids=Object.keys(POS).map(Number).filter(n=>!REL.includes(n)&&SHORT(n));const pods=[[1,8],[9,16],[17,24],[25,50]];
 pods.forEach(([a,b],k)=>{const inP=shuffle(ids.filter(n=>n>=a&&n<=b));inP.slice(0,k===3?6:2).forEach(n=>{SPOT.add(n);showSt(n,ST1(n))})})}
function spotTick(){if(MOB||!CUR)return;const on=[...SPOT].filter(n=>!LOCK[n]);if(!on.length)return;const out=pick(on);
 const podOf=n=>n<=8?0:n<=16?1:n<=24?2:3;const cand=Object.keys(POS).map(Number).filter(n=>!REL.includes(n)&&!SPOT.has(n)&&!LOCK[n]&&SHORT(n)&&podOf(n)===podOf(out));if(!cand.length)return;
 const inn=pick(cand);SPOT.delete(out);hideSt(out);SPOT.add(inn);showSt(inn,ST1(inn))}
// ---------- mobile: two readable status chips that hop between specialists
let MCH=[];
let FEEDL=0;
function feedSet(a,b,t,own){if(!FEED)return;const now=performance.now();if(!own&&now<FEEDL)return;if(own)FEEDL=now+4800;
 const html=own?`<div class="who"><img src="${LOGO(a)}">${NAME[a]}<em>to</em><img src="${LOGO(b)}">${NAME[b]}<u>${CUR.name}</u></div><div class="tx2">${t}</div>`:`<div class="who"><span class="lv"></span>${NAME[a]}${b?`<em>to</em>${NAME[b]}`:''}</div><div class="tx2">${t}</div>`;
 FEED.classList.add('out');setTimeout(()=>{FEED.innerHTML=html;FEED.classList.toggle('own',!!own);FEED.classList.remove('out')},STOP>=0?0:220)}
function mobChips(){if(!MOB||!CUR)return;const ids=Object.keys(POS).map(Number).filter(n=>!REL.includes(n));const n=ids[Math.floor(rnd()*ids.length)];ping(n,1500);
 const T=C.tasks[n];feedSet(n,0,T[Math.floor(rnd()*T.length)]+'.')}
// ---------- pulses and wires
function pulse(path,col,dur=1000,rev=false,r=3.4){if(!path)return;const L=path.getTotalLength();const c=document.createElementNS(NS,'circle');c.setAttribute('r',MOB?r*.7:r);c.setAttribute('fill',col);pul.appendChild(c);const t0=performance.now();
 (function f(t){let k=(t-t0)/dur;if(k>1){c.remove();return}const e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;const q=path.getPointAtLength((rev?1-e:e)*L);c.setAttribute('cx',q.x);c.setAttribute('cy',q.y);requestAnimationFrame(f)})(t0)}
function burst(path,col,rev,n=3,gap=230,dur=1000){for(let i=0;i<n;i++)setTimeout(()=>pulse(path,col,dur,rev,i?2.6:3.6),i*gap)}
// agent to agent: a soft arc that bows away from the tiles, drawn under them
function tempWire(a,b,col,dash,life=2600){const A=POS[a],B=POS[b];if(!A||!B)return null;let d;
 if(!MOB){const up=REL.includes(a)&&REL.includes(b);const drop=Math.min(G.ROW*.75,34+Math.abs(B[0]-A[0])*.1);const bot=up?Math.min(A[1],B[1])-24-Math.min(40,10+Math.abs(B[0]-A[0])*.05):Math.max(A[1],B[1])+drop;d=`M${A[0]},${A[1]} C${A[0]},${bot} ${B[0]},${bot} ${B[0]},${B[1]}`}
 else{const cy=G.CY,mx=(A[0]+B[0])/2,my=(A[1]+B[1])/2;let vx=mx-195,vy=my-cy;const l=Math.hypot(vx,vy)||1;const k=Math.max(30,110-l);const qx=mx+vx/l*k,qy=my+vy/l*k;d=`M${A[0]},${A[1]} Q${qx},${qy} ${B[0]},${B[1]}`}
 const p=document.createElementNS(NS,'path');p.setAttribute('d',d);p.setAttribute('fill','none');p.setAttribute('stroke',col);p.setAttribute('stroke-width',MOB?'1.4':'1.8');p.setAttribute('stroke-linecap','round');if(dash)p.setAttribute('stroke-dasharray',dash);
 p.style.transition='opacity .4s';p.style.opacity=0;web.appendChild(p);requestAnimationFrame(()=>p.style.opacity=1);if(life)setTimeout(()=>{p.style.opacity=0;setTimeout(()=>p.remove(),450)},life);return p}
function ping(n,ms=1400){const e=AG[n];if(!e)return;e.classList.add('ping');setTimeout(()=>e.classList.remove('ping'),ms)}
// ---------- bubbles
function bubbleEl(a,b,t,tag,oth){const d=document.createElement('div');d.className='a2a'+(oth?' oth':' hot');d.innerHTML=`<div class="who"><img src="${LOGO(a)}">${NAME[a]}<em>to</em><img src="${LOGO(b)}">${NAME[b]}${tag?`<u>${tag}</u>`:''}</div><div class="bt">${t}</div>`;return d}
const SL={};
function showBubble(x,y,w,key,a,b,t,tag,oth,life){if(SL[key])return;SL[key]=1;const d=bubbleEl(a,b,t,tag,oth);Object.assign(d.style,{left:px(x),top:px(y),width:px(w)});stage.appendChild(d);requestAnimationFrame(()=>requestAnimationFrame(()=>d.classList.add('on')));
 if(life)setTimeout(()=>{d.classList.remove('on');setTimeout(()=>{d.remove();SL[key]=0},400)},life);return d}
function sayOwner(a,b,t,life=3800){if(MOB){feedSet(a,b,t,1);return}
 $$('.a2a.hot').forEach(e=>e.remove());SL.o0=0;const s=OWN[0];return showBubble(s[0],s[1],s[2],'o0',a,b,t,CUR.name,false,life)}
// other owners' work: one bubble at a time, kept inside the floor, never over this owner's specialists
function sayOther(a,b,t){if(MOB){feedSet(a,b,t);return}const f=$('.feed',floor);if(!f)return;const set=()=>{f.innerHTML=`<span class="fd"></span><img src="${LOGO(a)}">${NAME[a]}<em>to</em><img src="${LOGO(b)}">${NAME[b]}<span class="ft">${t}</span>`;f.classList.remove('out')};
 if(STOP>=0&&!window.READY){set();return}f.classList.add('out');setTimeout(set,280)}
function chatter(once,tries=0){const c=C.chatter[Math.floor(Math.random()*C.chatter.length)];
 const bad=REL.includes(c[0])||REL.includes(c[1])||!POS[c[0]]||!POS[c[1]]||(!MOB&&POS[c[0]]&&POS[c[1]]&&(Math.abs(POS[c[0]][0]-POS[c[1]][0])>G.cw*3.2||Math.abs(POS[c[0]][1]-POS[c[1]][1])>G.ROW*1.5))||(MOB&&Math.hypot(POS[c[0]][0]-POS[c[1]][0],POS[c[0]][1]-POS[c[1]][1])>110);
 if(bad){if(tries<80)return chatter(once,tries+1);return}
 sayOther(c[0],c[1],c[2]);
 const w=tempWire(c[0],c[1],'#a59fad','3 4',once?0:2600);if(w)burst(w,'#8a8492',false,2,260,1100);ping(c[0]);setTimeout(()=>ping(c[1]),700);
 
 if(!once)setTimeout(chatter,R(2600,4200))}
// ---------- owner card (Desk dossier)
const PAL=[['#ffe2cf','#9a3b0e'],['#dff1e6','#1d6b3c'],['#e4e6ff','#3a3f9e'],['#fde7f3','#b0126c'],['#fff1c9','#7a5a00']];
const est='<span class="etag">est</span>';
function code(){const L='ABCDEFGHJKLMNPQRSTUVWXYZ',d=()=>Math.floor(rnd()*10);return pick(L)+d()+d()+d()+pick(L)+d()+d()}
function countUp(el,to,ms=1400){if(!el)return;if(FF||STOP>=0){el.textContent=to;return}const t0=performance.now();(function f(t){const k=Math.min(1,(t-t0)/ms),e=1-Math.pow(1-k,3);el.textContent=Math.round(to*e);if(k<1)requestAnimationFrame(f)})(t0)}
let SC='',TRK=0,NX=false;
function buildCard(p){SC=code();NX=false;const[bg,fg]=PAL[p.s%5];const ini=p.ini||(p.name[0]+p.biz[0]);
 if(false){card.innerHTML=`<svg class="ring"><rect class="r1" rx="18"/><rect class="r2" rx="18" pathLength="100"/></svg><div class="hd on"><div class="pav6" style="width:36px;height:36px;background:${bg};color:${fg};font-size:13px">${ini}</div><div style="min-width:0;flex:1"><div class="l1"><span class="nm6">${p.name}</span></div><div class="bz l2">${p.biz} · ${p.city}</div></div><div class="sc">Bespoke strategy<span class="code" id="sc"></span></div></div>
  <div class="ml"><b>Next</b><span class="t" id="nx"><span class="plan">Planning with the desk<span class="typ2"><i></i><i></i><i></i></span></span></span></div>
  <div class="ml"><b>Pending</b>${p.pend.slice(0,2).map(x=>`<span class="pc">${x}</span>`).join('')}</div>`;return}
 const cds=p.cards.map(x=>`<i><img src="${C.cardg}" alt="">${x}</i>`).join('');
 card.innerHTML=`<svg class="ring"><rect class="r1" rx="20"/><rect class="r2" rx="20" pathLength="100"/></svg>
 <div class="hd"><div class="pav6" style="width:44px;height:44px;background:${bg};color:${fg}">${ini}<span class="em">${p.emo}</span></div><div><span class="nm6">${p.name}</span><span class="bz">${p.biz} · ${p.city}</span></div></div>
 <div class="pill"><span class="lbl">Bespoke strategy</span><span class="code" id="sc"></span></div>
 <div class="kn"><span>Desk dossier</span><span><span id="trk">0</span> of 50+ tracked</span></div>
 <div class="rw"><span>Cards on file</span><b><div class="cds">${cds}</div></b></div>
 <div class="rw"><span>Card spend</span><b>$<span id="cu1">0</span>k a year${est}<small class="g">${p.top}</small></b></div>
 <div class="rw"><span>Points a year</span><b>${p.before}k today <span class="ar">→</span> <span style="color:var(--ac)"><span id="cu3">0</span>k${est}</span></b></div>
 <div class="rw"><span>Next trip</span><b id="nx"><span class="plan">Planning with the desk<span class="typ2"><i></i><i></i><i></i></span></span></b></div>
 <div class="rw"><span>Requests</span><b><div class="pend" id="pd">${p.pend.slice(0,2).map(x=>`<i>${x}</i>`).join('')}</div></b></div>
 <div class="ppf6">Example owner. Fictional details. Figures are estimates.</div>`}
function trk(){const e=$('#trk');if(e)e.textContent=TRK}
function cardIntro(p){const hd=$('.hd',card);hd&&hd.classList.add('on');const sc=$('#sc');let i=0;
 if(FF||STOP>=0){sc.textContent=SC;$$('.kn,.rw,.ppf6,.pill',card).forEach(r=>r.classList.add('on'));countUp($('#cu1'),p.spend);countUp($('#cu3'),p.after);TRK=p.cards.length;trk();return}
 setTimeout(()=>{const pill=$('.pill',card);pill&&pill.classList.add('on');(function ty(){sc.innerHTML=SC.slice(0,i)+'<span class="cur"></span>';if(i++<SC.length)setTimeout(ty,95);else setTimeout(()=>sc.textContent=SC,900)})()},350);
 TRK=p.cards.length;trk();
 $$('.kn,.rw,.ppf6',card).forEach((r,j)=>setTimeout(()=>{r.classList.add('on');if(r.querySelector('#cu1'))countUp($('#cu1'),p.spend);if(r.querySelector('#cu3'))countUp($('#cu3'),p.after,1700)},1100+j*320))}
function setNext(p){const nx=$('#nx');if(!nx||NX)return;NX=true;nx.innerHTML=`${p.nxt}<small>${p.nxte}${est}</small>`;const row=nx.closest('.rw')||nx.closest('.ml');if(row){row.classList.add('flash');setTimeout(()=>row.classList.remove('flash'),1500)}}
function pendProgress(){const pd=$('#pd');if(!pd)return;const f=pd.children[0];if(f&&!f.classList.contains('ip')){f.classList.add('ip');f.insertAdjacentHTML('beforeend','<em>on it</em>')}}
function pendAdd(p){const pd=$('#pd');if(!pd||pd.children.length>2)return;const t=p.pend[2];if(!t)return;const i=document.createElement('i');i.className='new';i.innerHTML=t+'<em>new</em>';pd.appendChild(i);requestAnimationFrame(()=>requestAnimationFrame(()=>i.classList.remove('new')))}
function pendSent(){const pd=$('#pd');if(!pd)return;const f=pd.children[0];if(f){const em=f.querySelector('em');if(em)em.textContent='sent to desk'}}
// ---------- chat
const SPD=Q.has('spd')?+Q.get('spd'):1;const sleep=ms=>new Promise(r=>setTimeout(r,ms*SPD));
let lastW=null,rc=null,RUN=0,CLK=[9,12],A2AQ=[];
function flip(fn){const h0=ci.offsetHeight;fn();const d=ci.offsetHeight-h0;if(d<=0||FF>99)return;ci.style.transition='none';ci.style.transform=`translateY(${d}px)`;ci.offsetHeight;ci.style.transition='transform .45s cubic-bezier(.2,.7,.2,1)';ci.style.transform='none';while(ci.children.length>60)ci.removeChild(ci.firstChild)}
const who=w=>w==='o'?'o':w==='f'?'f':'s';
function lines(h){return h.split(/(?<=[.!?])\s+(?=[A-Z0-9$"'(])/).map(s=>`<span class="ln">${s}</span>`).join('')}
function richCard(p,kind){const d=p.dest,m=p.mer;
 if(kind==='map')return `<div class="xc"><div class="im" style="background-image:url(${C.photo[d.i]})"><span class="lb">${d.title}</span></div><div class="mp" style="background-image:url(${C.mapd[d.i]})"><i class="pin"></i><span class="tag">Award space not guaranteed</span></div><div class="ft"><b>${p.nxt}</b><span>${d.sub}. Value about ${p.nxte}<i class="e">est</i></span></div><div class="att">Photo: ${C.cred[d.i]} · Map data © OpenStreetMap contributors</div></div>`;
 return `<div class="xc"><div class="mh"><span class="ml"><img src="${C.mlogo[m.k]}"></span><div><b>${m.name}</b><span>Where ${p.name} spends · ${m.cat}</span></div></div><div class="mp" style="background-image:url(${C.mapc[p.s]})"><i class="pin pk"></i><span class="tag">${p.city} · example</span></div><div class="ft"><div class="chips"><i>$${m.k_yr}k a year here<i class="e">est</i></i><i>Routed to ${m.card}</i></div></div><div class="att">Merchant logo shown for identification only · Map data © OpenStreetMap contributors</div></div>`}
function msgEl(b,typing){const k=who(b.w),d=document.createElement('div');d.className='mm '+k+(k==='s'?' sp':'');
 const body=typing?`<div class="b6 typ"><i></i><i></i><i></i></div>`:`<div class="b6">${b.q?`<div class="q">${b.q}</div>`:''}${lines(b.h)}</div>`;
 if(k==='o'){d.innerHTML=body;return d}
 const same=lastW===String(b.w)&&!typing;const avh=k==='f'?`<img class="av avfo" src="${C.foi}">`:`<img class="av" src="${LOGO(b.w)}">`;
 const nm=k==='s'&&!same?`<div class="nm5">${NAME[b.w]} specialist<b>${CUR.rel.find(r=>r[0]===b.w)[1]}</b></div>`:(k==='f'&&!same&&!typing?`<div class="nm5">First Officer</div>`:'');
 const rich=(!typing&&b.card)?richCard(CUR,b.card):'';
 d.innerHTML=avh+`<div class="col">${nm}${body}${rich}</div>`;return d}
function tick(){CLK[1]++;if(CLK[1]>59){CLK[1]=0;CLK[0]++}$('#clk').textContent=CLK[0]+':'+String(CLK[1]).padStart(2,'0')}
const tstr=()=>CLK[0]+':'+String(CLK[1]).padStart(2,'0')+' PM';
function banner(t,b){$('#bt').textContent=t;$('#bb').textContent=b;$('#ban').classList.add('on');setTimeout(()=>$('#ban').classList.remove('on'),3600)}
function speak(n,on){const e=AG[n];if(on){LOCK[n]=1;e&&e.classList.add('spk');const s=e&&e.querySelector('.st');if(s)s.textContent='Briefing now';burst($('#w'+n,web),C.acc[CUR.tab][0],true,3,240,1050);setTimeout(()=>FOel.classList.add('spk'),700);setTimeout(()=>FOel.classList.remove('spk'),1300)}
 else{e&&e.classList.remove('spk');const r=CUR.rel.find(x=>x[0]===n);const s=e&&e.querySelector('.st');if(s)s.textContent=relSt(CUR,n,r?r[1]:'')}}
async function run(p,ff){const my=++RUN;let dsk=null,lastF='',bi=0,prevSpec=null,spoken=new Set(),planSet=false;
 const T=x=>ff>bi?0:x;const[h,m]=p.t0.split(':').map(Number);CLK=[h,m];$('#clk').textContent=p.t0;
 flip(()=>{const t=document.createElement('div');t.className='ts';t.textContent='Tonight '+p.t0+' PM ET';ci.appendChild(t)});
 for(bi=0;bi<p.beats.length;bi++){const b=Object.assign({},p.beats[bi]);if(my!==RUN)return;const k=who(b.w);if(window.BLOG)BLOG.push([Math.round(performance.now()),bi,k,b.ban?1:0]);
  if(bi%4===3)tick();
  if(k!=='s'&&dsk){const d=dsk;dsk=null;flip(()=>d.remove())}
  if(STOP>=0&&bi===STOP){ // freeze for review stills
   if(k==='s'){speak(b.w,true);if(prevSpec){const to=tgt(prevSpec);if(to){tempWire(prevSpec.w,to,C.acc[p.tab][0],'5 4',0);ping(to,99999)}}
    dsk=document.createElement('div');dsk.className='dsk fo-only';dsk.innerHTML=`<div class="typ"><i></i><i></i><i></i></div>First Officer is checking with the desk`;flip(()=>ci.appendChild(dsk));flip(()=>ci.insertBefore(msgEl(b,true),dsk))}
   else if(k==='f'){flip(()=>ci.appendChild(msgEl(b,true)))}
   if(prevSpec){const to=tgt(prevSpec);if(to)A2AQ.push([prevSpec.w,to,prevSpec.f||''])}A2AQ.slice(-2).forEach(x=>sayOwner(x[0],x[1],x[2],0));if(!Q.has('nochat'))chatter(1);mobChips();window.READY=1;return}
  if(k==='o'){await sleep(T(900+b.t.length*12));if(b.re&&lastF)b.q='Replying to First Officer: '+lastF.slice(0,58)+'...';burst($('#wout',web),'#FA1896',true,2,260,1000);
   flip(()=>{const e=msgEl(b);ci.appendChild(e);if(rc)rc.remove();rc=document.createElement('div');rc.className='rcpt';rc.textContent='Delivered';ci.appendChild(rc)});lastW='o';prevSpec=null;await sleep(T(700))}
  else{if(k==='s'){speak(b.w,true);spoken.add(b.w);TRK=p.cards.length+spoken.size;trk();
    if(!dsk){dsk=document.createElement('div');dsk.className='dsk fo-only';dsk.innerHTML=`<div class="typ"><i></i><i></i><i></i></div>First Officer is checking with the desk`;flip(()=>ci.appendChild(dsk))}}
   else{burst($('#wout',web),'#FA1896',false,2,260,1000);FOel.classList.add('spk')}
   if(rc&&rc.textContent==='Delivered')rc.textContent='Read '+tstr();
   const ty=msgEl(b,true);flip(()=>{if(k==='s'&&dsk)ci.insertBefore(ty,dsk);else ci.appendChild(ty)});
   await sleep(T(Math.max(k==='s'?950:1000,Math.min(k==='s'?2300:2700,b.t.length*(k==='s'?15:21)))));if(my!==RUN)return;
   const e=msgEl(b);flip(()=>ty.replaceWith(e));lastW=String(b.w);if(k==='f')lastF=b.t;
   if(b.tap)setTimeout(()=>{const bb=e.querySelector('.b6');const s=document.createElement('span');s.className='tp';s.textContent=b.tap;bb.appendChild(s)},T(900));
   if(b.ban)setTimeout(()=>{banner(b.ban[0],b.ban[1]);setTimeout(pendSent,400)},T(500));
   if(k==='s'){prevSpec=b;const to=tgt(b);if(to){const w=T(1)?tempWire(b.w,to,C.acc[p.tab][0],'5 4',3200):null;if(w)burst(w,C.acc[p.tab][0],false,3,240,1000);ping(to,1800);A2AQ.push([b.w,to,b.f||'']);if(T(1))sayOwner(b.w,to,b.f||'')}}
   if(k==='f'&&spoken.size&&!planSet){planSet=true;setNext(p);pendProgress()}
   if(bi===Math.round(p.beats.length*.55))pendAdd(p);
   await sleep(T(k==='s'?650:750));if(k==='s')speak(b.w,false);else FOel.classList.remove('spk')}
 }
 if(dsk)dsk.remove();await sleep(4500);if(my!==RUN||Q.has('once'))return;load(pickP(),0)}
function pickP(){let q=[];try{q=JSON.parse(localStorage.getItem('fo10_q')||'[]')}catch(e){}const last=+localStorage.getItem('fo9_p');if(!q.length){q=PS.map((_,i)=>i);for(let i=q.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[q[i],q[j]]=[q[j],q[i]]}if(q[0]===last)q.push(q.shift())}const i=q.shift();localStorage.setItem('fo10_q',JSON.stringify(q));return i}
let HOMEV=false; // Home tab shows as selected when Home was tapped (approved Oct 21)
function load(i,ff){CUR=PS[i];localStorage.setItem('fo9_p',i);RUN++;
 ['t-earn','t-burn','t-return','t-learn'].forEach(c=>B.classList.remove(c));B.classList.add('t-'+CUR.tab);
 $$('#tabs > div').forEach(d=>d.classList.toggle('on',d.dataset.t===(HOMEV?'home':CUR.tab)));HOMEV=false;
 const[bg,fg]=PAL[CUR.s%5];$('#pav').innerHTML=`<div class="pav6" style="width:32px;height:32px;background:${bg};color:${fg};font-size:12.5px">${CUR.ini||(CUR.name[0]+CUR.biz[0])}</div>`;
 ci.innerHTML='';ci.style.transform='none';lastW=null;rc=null;A2AQ=[];$$('.a2a').forEach(e=>e.remove());for(const k in SL)SL[k]=0;
 if(MOB)placeDesk();buildFloor(CUR);buildCard(CUR);if(MOB)beats(CUR);
 if(MOB&&STOP<0&&!SEEN.card)PEND.c=CUR;else cardIntro(CUR);mobChips();
 if(MOB&&STOP<0&&!SEEN.desk)PEND.r=[CUR,ff||0];else run(CUR,ff||0)}
const SEEN={},PEND={};
function watch(){if(!MOB||STOP>=0||!window.IntersectionObserver)return;const io=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;
  if(e.target===card&&!SEEN.card){SEEN.card=1;if(PEND.c===CUR)cardIntro(CUR);PEND.c=null}
  if(e.target===FOel&&!SEEN.desk){SEEN.desk=1;if(PEND.r&&PEND.r[0]===CUR)run(PEND.r[0],PEND.r[1]);PEND.r=null}}),{threshold:.6});io.observe(card);io.observe(FOel)}
const ALIN={'Amex':['Membership Rewards'],'Citi':['ThankYou'],'Chase':['Ultimate Rewards'],'Capital One':['Venture'],'Marriott':['Bonvoy'],'Qatar Airways':['Privilege Club','Qsuites'],'British Airways':['Executive Club'],'Air Canada':['Aeroplan'],'Hilton':['Hilton Honors'],'Hyatt':['World of Hyatt']};
function tgt(b){if('to' in b)return b.to;const t=b.t||'';let best=null,bi=1e9;REL.filter(n=>n!==b.w).forEach(n=>{const nm=NAME[n],fw=nm.split(' ')[0];const keys=[nm].concat(fw.length>=4&&!['Virgin','United','Air'].includes(fw)?[fw]:[],ALIN[nm]||[]);keys.forEach(k=>{const i=t.indexOf(k);if(i>=0&&i<bi){bi=i;best=n}})});return best}
const PRON={Ines:'Her',Lucia:'Her',Imani:'Her',Yuki:'Her',Teresa:'Her',Leila:'Her',Anjali:'Her',Marisol:'Her',Joanne:'Her'};
function beats(p){BT[0].innerHTML=`<i>1</i>Meet ${p.name}`;BT[1].innerHTML=`<i>2</i>${PRON[p.name]||'His'} desk`;BT[2].innerHTML=`<i>3</i>What ${p.name} sees<em>in the app</em>`}
function placeDesk(){if(MOB){const keepY=ph&&G.PH[1]&&scrollY>200?ph.getBoundingClientRect().top:null;G.cardMax=measureCards(CUR?[CUR]:PS);if(CUR)beats(CUR);let y=G.B1;
  BT[0].style.top=px(y);y+=BT[0].offsetHeight+16;G.CARD[1]=y;card.style.top=px(y);y+=G.cardMax+44;
  BT[1].style.top=px(y);y+=BT[1].offsetHeight;G.CY=y+256;FOel.style.top=px(G.CY-G.FS/2);FOel.style.left=px(195-G.FS/2);FOel.style.width=FOel.style.height=px(G.FS);
  FOL.style.top=px(G.CY+42);y=G.CY+246+108;
  FEED.style.top=px(G.CY+285);y+=FEED.offsetHeight+44;
  BT[2].style.top=px(y);y+=BT[2].offsetHeight+18;G.PH[1]=y;ph.style.top=px(y);ph.style.left=px(G.PH[0]);y+=G.PHH+34;
  CTAS.style.top=px(y);y+=CTAS.offsetHeight+20;MICRO.style.top=px(y);y+=MICRO.offsetHeight+8;TMK.style.top=px(y);y+=TMK.offsetHeight+30;
  y+=84; // bottom clearance so the live sticky bar (67px) never sits on hero content (approved Oct 21)
  SH.H=y;fit();[web,pul].forEach(s=>s.setAttribute('height',SH.H));if(keepY!=null){const d=ph.getBoundingClientRect().top-keepY;if(Math.abs(d)>1)scrollBy(0,d)}return}const cb=G.CARD[1]+measureCards();G.FO[1]=Math.max(cb+40+G.FS/2+14,680);G.Y0=G.FO[1]+G.FS/2+70;G.Y1=G.Y0+34+3*G.ROW+112;SH.H=G.Y1+112;fit();[web,pul].forEach(s=>s.setAttribute('height',SH.H));MICRO.style.top=px(G.Y1+18);TMK.style.top=px(G.Y1+18+MICRO.offsetHeight+4);
 FOel.style.top=px(G.FO[1]-G.FS/2);FOL.style.top=px(G.FO[1]-G.FS/2-50)}
function measureCards(list){let mx=0;const keep=CUR;(list||PS).forEach(p=>{CUR=p;buildCard(p);$$('.kn,.rw,.ppf6,.pill',card).forEach(r=>r.classList.add('on'));NX=false;setNext(p);pendProgress();pendAdd(p);$$('#pd i',card).forEach(i=>i.classList.remove('new'));mx=Math.max(mx,card.offsetHeight)});CUR=keep;card.innerHTML='';return mx}
window.GO=function(){layout();buildFixed();placeDesk();watch();const i=Q.has('p')?PS.findIndex(x=>x.s===+Q.get('p')):pickP();load(i,FF||(STOP>=0?STOP:0));
 if(STOP<0){setTimeout(chatter,1600);setInterval(spotTick,1300);if(MOB)setInterval(mobChips,2600)}};
FOREADY().then(()=>setTimeout(GO,150));
$$('.micro a').forEach(a=>a.onclick=()=>{const d=document.getElementById('disc');if(!d)return;d.classList.remove('col');d.scrollIntoView({behavior:'smooth'})});
document.querySelectorAll('#disc .more').forEach(a=>a.onclick=()=>document.getElementById('disc').classList.remove('col'));
})();
}else{
(function(){
const C=window.CFG,PS=C.personas,NS='http://www.w3.org/2000/svg';
const Q=new URLSearchParams(location.search);
const host=document.getElementById('fohero');const root=host.attachShadow({mode:'open'});window.HROOT=root;
root.innerHTML=`<style>${C.css}</style><div id="hero"><div class="tint"></div><div id="stage"></div></div>`;
const $=(s,r=root)=>r.querySelector(s),$$=(s,r=root)=>[...r.querySelectorAll(s)];
let seed=Q.has('seed')?+Q.get('seed'):Math.floor(Math.random()*1e9);
function rnd(){seed=(seed*1664525+1013904223)%4294967296;return seed/4294967296}
const R=(a,b)=>a+rnd()*(b-a),pick=a=>a[Math.floor(rnd()*a.length)];
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(rnd()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
const MOB=Q.has('m')?Q.get('m')==='1':innerWidth<760;
const B=$('#hero');B.classList.add(MOB?'M':'D');document.body.classList.add(MOB?'foM':'foD');
const LOGO=n=>C.logos[n],NAME=C.names;
const FF=+(Q.get('ff')||0),STOP=Q.has('stop')?+Q.get('stop'):-1;
const SH=MOB?{W:390,H:1500}:{W:1440,H:1230};
const stage=$('#stage'),hero=$('#hero');
function fit(){const s=Math.min(innerWidth,document.documentElement.clientWidth||innerWidth)/SH.W;stage.style.width=SH.W+'px';stage.style.height=SH.H+'px';stage.style.transform=`scale(${s})`;hero.style.height=SH.H*s+'px'}fit();addEventListener('resize',fit);
// ---------- hero photo: the live page's own rotating pool, never the same twice in a row
(function(){const pool=C.pool;let last=+localStorage.getItem('fo9_bg'),i;do{i=Math.floor(Math.random()*pool.length)}while(i===last&&pool.length>1);if(Q.has('bg'))i=+Q.get('bg')%pool.length;localStorage.setItem('fo9_bg',i);const top=document.getElementById('top');top&&top.style.setProperty('--ph',`url(${pool[i]})`)})();
const H=C.copy;
function el(tag,cls,html,st,par){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;if(st)Object.assign(e.style,st);(par||stage).appendChild(e);return e}
const px=v=>v+'px';
const SUBT=(window.FO_SUBHEAD||H.sub);
function subFill(d){const bl=SUBT.split(/\n\s*\n/).map(x=>x.trim()).filter(Boolean);bl.forEach((t,i)=>{const p=document.createElement('p');p.textContent=t;if(bl.length>1&&i===bl.length-1)p.className='tag';d.appendChild(p)});return d}
function fitH1(h,w){h.style.whiteSpace='nowrap';let f=parseFloat(h.style.fontSize);while(h.scrollWidth>w&&f>12){f-=.5;h.style.fontSize=f+'px'}return h}
// ---------- static copy (positions finalised in layout() once fonts are ready)
const TX=MOB?18:148;
const KICK=el('div','kick','<span class="ld"></span>Earn · Burn · Return · Learn',{left:px(TX),top:px(MOB?22:34)});
const H1=el('h1','',H.h1,{left:px(TX),top:px(MOB?64:74),fontSize:MOB?'30px':'52px'});
const SUB=subFill(el('div','sub',null,MOB?{left:px(TX),width:'354px'}:{left:px(TX),width:'460px'}));
const CTAS=el('div','ctas','<a href="book.html?from=index" style="display:flex;text-decoration:none"><b class="c1">Get your desk</b></a><a href="how.html" style="display:flex;text-decoration:none"><b class="c2">See how it works</b></a>',MOB?{left:'16px',right:'16px',justifyContent:'center'}:{left:px(TX)});
const DESKH=el('div','deskh',MOB?`<span class="k"><img src="${C.foi}" style="height:14px;width:14px;object-fit:contain;flex:none"><span class="lv"></span>First Officer's specialists · 50+ programs, trained on new data nightly</span>`:`<span class="k"><span class="lv"></span><b>First Officer's specialists</b><em>50+ programs, trained on new data nightly</em></span>`,MOB?{left:'0',right:'0',justifyContent:'center'}:{left:px(TX)});
const MICRO=el('div','micro',MOB?H.microM:H.micro,MOB?{left:'18px',width:'354px',textAlign:'center'}:{left:'120px',width:'1200px',textAlign:'center'});
const TMK=el('div','tmk',H.tmk,MOB?{left:'18px',width:'354px',textAlign:'center'}:{left:'120px',width:'1200px',textAlign:'center'});
// ---------- geometry (set in layout)
const G={};
let OWN=[];
function layout(){
 if(!MOB){
  fitH1(H1,780);const hb=74+H1.offsetHeight;
  SUB.style.top=px(hb+18);const sb=hb+18+SUB.offsetHeight;
  CTAS.style.top=px(sb+24);const cb=sb+24+CTAS.offsetHeight;
  DESKH.style.top=px(cb+20);const db=cb+20+DESKH.offsetHeight;
  OWN=[[TX,db+14,466]];
  Object.assign(G,{FS:72,PH:[972,22,.78],CARD:[632,hb+22,326],X0:120,X1:1320,ROW:98});
  G.FO=[795,0];G.Y0=0;G.Y1=0;SH.H=G.Y1+112;fit();[web,pul].forEach(s=>s.setAttribute('height',SH.H));MICRO.style.top=px(G.Y1+18);TMK.style.top=px(G.Y1+18+MICRO.offsetHeight+4);
 }else{
  fitH1(H1,354);const hb=64+H1.offsetHeight;
  SUB.style.top=px(hb+14);const sb=hb+14+SUB.offsetHeight;
  DESKH.style.top=px(sb+22);const db=sb+22+DESKH.offsetHeight;
  const cardY=db+12;Object.assign(G,{CARD:[16,cardY,358],FS:40});
  G.cardH=96;G.FO=[195,cardY+G.cardH+44];G.PH=[70,G.FO[1]+G.FS/2+26,.6];G.PHH=876*.6;
  G.STRIP=G.PH[1]+G.PHH+18;CTAS.style.top=px(G.STRIP+110);MICRO.style.top=px(G.STRIP+110+62);TMK.style.top=px(G.STRIP+110+62+MICRO.offsetHeight+6);
 }
}
// ---------- layers
const web=document.createElementNS(NS,'svg');web.setAttribute('class','web');stage.appendChild(web);
const pul=document.createElementNS(NS,'svg');pul.setAttribute('class','pul');stage.appendChild(pul);
[web,pul].forEach(s=>{s.setAttribute('width',SH.W);s.setAttribute('height',SH.H)});
const floor=el('div','floor','',{position:'absolute',left:0,top:0});
let FOel,FOL,card,ph,ci,chat;
function buildFixed(){
 FOel=el('div','fo',`<img src="${C.foi}">`,{left:px(G.FO[0]-G.FS/2),top:px(G.FO[1]-G.FS/2),width:px(G.FS),height:px(G.FS)});
 if(!MOB)FOL=el('div','fol','<b class="l1">First Officer</b><span class="l2">At the Desk</span>',{left:px(G.FO[0]),top:px(G.FO[1]-G.FS/2-50)});
 else FOL=el('div','fol m','<b class="l1">First Officer</b><span class="l2">At the Desk</span>',{left:px(G.FO[0]+G.FS/2+10),top:px(G.FO[1]-19)});
 card=el('div','',null,{});card.id='card';
 card.style.left=px(G.CARD[0]);card.style.top=px(G.CARD[1]);card.style.width=px(G.CARD[2]);if(MOB)card.className='slim';
 ph=el('div','',C.phone,{left:px(G.PH[0]),top:px(G.PH[1]),transform:`scale(${G.PH[2]})`});ph.id='ph';
 ci=$('#ci');chat=$('#chat');
 setView(VIEW);
 $('#sfo').onclick=e=>{rip(e.currentTarget);setView('fo',1)};$('#sbtd').onclick=e=>{rip(e.currentTarget);setView('btd',1)};
 $$('#tabs > div').forEach(d=>d.onclick=()=>{const t=d.dataset.t;rip(d);HOMEV=t==='home';const pool=PS.filter(p=>(t==='home'||p.tab===t)&&p!==CUR);load(PS.indexOf(pool[Math.floor(Math.random()*pool.length)]),0)});
}
let VIEW=Q.get('view')==='btd'?'btd':'fo'; // Oct 22 (approved): opens on First Officer; ?view=btd still opens Behind the desk
function setView(v,anim){ph.classList.toggle('vfo',v==='fo');ph.classList.toggle('vbtd',v!=='fo');$('#sfo').classList.toggle('on',v==='fo');$('#sbtd').classList.toggle('on',v!=='fo');if(anim){chat.classList.add('blink');setTimeout(()=>chat.classList.remove('blink'),260)}VIEW=v}
function rip(e){const r=e.getBoundingClientRect(),s=e.closest('.scr').getBoundingClientRect(),k=s.width/393;const d=document.createElement('div');d.className='rip';d.style.left=(r.left+r.width/2-s.left)/k+'px';d.style.top=(r.top+r.height/2-s.top)/k+'px';e.closest('.scr').appendChild(d);setTimeout(()=>d.remove(),700)}
// ---------- agents
let AG={},POS={},REL=[],LOCK={},CUR=null,SPOT=new Set();
const relSt=(p,n,role)=>({Earn:'Earn plan',Burn:'Quoting',Return:'Value check',Learn:'Briefing'}[role]||'On it');
const WK='<span class="wk"><i></i><i></i><i></i></span>';
function buildFloor(p){floor.innerHTML='';web.innerHTML='';pul.innerHTML='';AG={};POS={};LOCK={};SPOT=new Set();
 REL=p.rel.map(r=>r[0]);REL.forEach(n=>LOCK[n]=1);const acc=C.acc[p.tab][0];let W='';
 if(!MOB){
  const {X0,X1,Y0,ROW}=G,NC=13,cw=(X1-X0)/NC,rows=[0,1,2,3].map(r=>Y0+34+r*ROW);G.cw=cw;
  const groups=[['Banks',[1,2,3,4,5,6,7,8],0,2],['Hotels',[9,10,11,12,13,14,15,16],2,2],['US airlines',[17,18,19,20,21,22,23,24],4,2],['Partner airlines',Array.from({length:26},(_,i)=>i+25),6,7]];
  groups.forEach(([name,ids,c0,nc])=>{const x0=X0+c0*cw+4,x1=X0+(c0+nc)*cw-4;
   floor.insertAdjacentHTML('beforeend',`<div class="pod" style="left:${x0}px;top:${Y0}px;width:${x1-x0}px;height:${G.Y1-Y0}px"><div class="podh"><span class="lv"></span>${name}<i>${ids.length} working</i></div>${nc>=4?'<div class="feed"></div>':''}</div>`);
   const slots=[];for(let r=0;r<4;r++)for(let c=0;c<nc;c++)slots.push([X0+(c0+c+.5)*cw,rows[r]]);
   const rl=ids.filter(i=>REL.includes(i)),free=slots.slice();
   const relCols=nc>=4?shuffle([1,2,3,4,5]).slice(0,rl.length).sort((a,b)=>a-b):[0,1];
   rl.forEach((n,i)=>{const si=i<relCols.length?relCols[i]:nc+i;POS[n]=slots[si];free.splice(free.indexOf(slots[si]),1)});
   shuffle(ids.filter(i=>!REL.includes(i))).forEach((n,i)=>POS[n]=free[i]);
   // quiet neighbour links, drawn under the tiles
   ids.forEach(n=>{const[x,y]=POS[n];ids.forEach(m=>{const q=POS[m];if(Math.abs(q[1]-y)<5&&q[0]-x>0&&q[0]-x<cw*1.2&&rnd()<.45&&!REL.includes(n)&&!REL.includes(m)){W+=`<path class="bw" d="M${x+22},${y} C${x+cw*.4},${y-16} ${q[0]-cw*.4},${q[1]-16} ${q[0]-22},${q[1]}" stroke="#d9d3de" stroke-width="1.2" fill="none"/>`}})})});
  // First Officer to the specialists on this request: one smooth curve each, entering the avatar from above
  const fb=G.FO[1]+G.FS/2;
  REL.forEach(n=>{const[x,y]=POS[n],ty=y-24;const dx=x-G.FO[0];const sx=G.FO[0]+Math.max(-22,Math.min(22,dx*.06));
   W+=`<path id="w${n}" d="M${sx},${fb-4} C${sx},${fb+64} ${x},${ty-44} ${x},${ty}" stroke="${acc}" stroke-width="2.2" stroke-linecap="round" fill="none"/>`});
  // the one pink line: First Officer to the app
  const pxL=G.PH[0]+4,py=Math.min(G.FO[1]-6,G.PH[1]+876*G.PH[2]-110);W+=`<path id="wout" d="M${G.FO[0]+G.FS/2-2},${G.FO[1]} C${G.FO[0]+G.FS/2+60},${G.FO[1]} ${pxL-60},${py} ${pxL},${py}" stroke="#FA1896" stroke-width="2.6" stroke-linecap="round" fill="none"/>`;
  for(let n=1;n<=50;n++){const[x,y]=POS[n],rel=REL.includes(n),s=rel?48:42,w=Math.round(cw)-4;
   const st=rel?relSt(p,n,p.rel.find(r=>r[0]===n)[1]):C.tasks[n][0];
   floor.insertAdjacentHTML('beforeend',`<div class="ag${rel?' rel':''}" data-n="${n}" style="left:${x-w/2}px;top:${y-s/2}px;width:${w}px"><div class="lg" style="width:${s}px;height:${s}px"><img src="${LOGO(n)}"></div><div class="tx"><b${rel&&NAME[n].length>12?' class="lnm"':''}>${NAME[n]}</b>${rel?`<span class="st">${st}</span>`:`<span class="st"></span>${WK}`}</div></div>`)}
 }else{
  // one tidy column on each side of the phone: this owner's specialists on top, then the rest of the desk, then a status card
  const others=shuffle(Array.from({length:50},(_,i)=>i+1).filter(n=>!REL.includes(n)));
  const L=REL.slice(0,Math.ceil(REL.length/2)),Rr=REL.slice(Math.ceil(REL.length/2));const half=Math.ceil(others.length/2);const left=others.slice(0,half),right=others.slice(half);
  const y0=G.PH[1]+10,yEnd=G.PH[1]+G.PHH;G.MSLOT=yEnd-76;
  const side=(rel,list,cx)=>{let y=y0;rel.forEach(n=>{POS[n]=[cx,y+17];y+=104});y+=4;list.forEach(n=>{if(y+40<=G.MSLOT-6){POS[n]=[cx,y+14];y+=46}else POS[n]=[cx,-999]})};
  side(L,left,35);side(Rr,right,355);
  [L,Rr].forEach((list,k)=>list.forEach((n,i)=>{const[x,y]=POS[n];const sx=k?1:-1;
   if(i===0)W+=`<path id="w${n}" d="M${G.FO[0]+sx*(G.FS/2-2)},${G.FO[1]} C${G.FO[0]+sx*80},${G.FO[1]} ${x},${y-80} ${x},${y-19}" stroke="${acc}" stroke-width="1.8" stroke-linecap="round" fill="none"/>`;
   else{const p=POS[list[i-1]];W+=`<path id="w${n}" d="M${p[0]},${p[1]+64} L${x},${y-19}" stroke="${acc}" stroke-width="1.8" stroke-linecap="round" fill="none"/>`}}));
  W+=`<path id="wout" d="M${G.FO[0]},${G.FO[1]+G.FS/2} L${G.FO[0]},${G.PH[1]+3}" stroke="#FA1896" stroke-width="2.2" stroke-linecap="round" fill="none"/>`;
  for(let n=1;n<=50;n++){const[x,y]=POS[n],rel=REL.includes(n),s=rel?32:28;const hide=y<0;
   const chip=rel?`<div class="chip"><b>${NAME[n]}</b><span class="st">${relSt(p,n,p.rel.find(r=>r[0]===n)[1])}</span></div>`:WK;
   floor.insertAdjacentHTML('beforeend',`<div class="mag${rel?' rel':''}" data-n="${n}" style="left:${x-32}px;top:${y-s/2}px;width:64px${hide?';display:none':''}"><div class="lg" style="width:${s}px;height:${s}px"><img src="${LOGO(n)}"></div>${chip}</div>`)}
 }
 web.innerHTML=W;$$('[data-n]',floor).forEach(e=>AG[+e.dataset.n]=e);
 $$('.wk',floor).forEach(c=>c.style.setProperty('--dl',-R(0,1.2).toFixed(2)+'s'));
 BW=$$('path.bw',web).map(p=>({p,L:p.getTotalLength(),ph:rnd(),sp:R(.1,.25)*(rnd()<.5?1:-1),c:null}));
 BW.forEach(b=>{if(rnd()<.55){b.c=document.createElementNS(NS,'circle');b.c.setAttribute('r',MOB?'1.8':'2.3');b.c.setAttribute('fill',rnd()<.5?acc:'#a59fad');b.c.setAttribute('fill-opacity','.85');web.appendChild(b.c)}});
 if(!MOB)initSpot();
}
let BW=[];
function loop(t){BW.forEach(b=>{if(!b.c)return;const k=((b.ph+t/1000*b.sp)%1+1)%1;const q=b.p.getPointAtLength(k*b.L);b.c.setAttribute('cx',q.x.toFixed(1));b.c.setAttribute('cy',q.y.toFixed(1))});requestAnimationFrame(loop)}requestAnimationFrame(loop);
// ---------- status lines: a readable handful at a time, everyone else shows working dots
function showSt(n,t){const e=AG[n];if(!e)return;const s=e.querySelector('.st');if(!s)return;
 if(STOP>=0&&!window.READY){s.textContent=t;e.classList.add('say');return}
 if(e.classList.contains('say')){s.classList.add('out');setTimeout(()=>{s.textContent=t;s.classList.remove('out')},260)}else{s.textContent=t;e.classList.add('say')}}
function hideSt(n){const e=AG[n];if(e)e.classList.remove('say')}
const SHORT=n=>NAME[n].length<=12;const ST1=n=>{const t=C.tasks[n].filter(x=>x.length<=15);return t.length?pick(t):C.tasks[n][0]};
function initSpot(){const ids=Object.keys(POS).map(Number).filter(n=>!REL.includes(n)&&SHORT(n));const pods=[[1,8],[9,16],[17,24],[25,50]];
 pods.forEach(([a,b],k)=>{const inP=shuffle(ids.filter(n=>n>=a&&n<=b));inP.slice(0,k===3?6:2).forEach(n=>{SPOT.add(n);showSt(n,ST1(n))})})}
function spotTick(){if(MOB||!CUR)return;const on=[...SPOT].filter(n=>!LOCK[n]);if(!on.length)return;const out=pick(on);
 const podOf=n=>n<=8?0:n<=16?1:n<=24?2:3;const cand=Object.keys(POS).map(Number).filter(n=>!REL.includes(n)&&!SPOT.has(n)&&!LOCK[n]&&SHORT(n)&&podOf(n)===podOf(out));if(!cand.length)return;
 const inn=pick(cand);SPOT.delete(out);hideSt(out);SPOT.add(inn);showSt(inn,ST1(inn))}
// ---------- mobile: two readable status chips that hop between specialists
let MCH=[];
function mobChips(){if(!MOB)return;MCH.forEach(c=>c.remove());MCH=[];
 [[0,195],[195,390]].forEach(([a,b])=>{const ids=Object.keys(POS).map(Number).filter(n=>!REL.includes(n)&&POS[n][0]>a&&POS[n][0]<b&&POS[n][1]>0);if(!ids.length)return;
  const n=ids[Math.floor(rnd()*ids.length)];const T=C.tasks[n].filter(t=>t.length<=18);const t=T.length?T[Math.floor(rnd()*T.length)]:C.tasks[n][0];
  const d=document.createElement('div');d.className='mch';d.style.cssText=`left:${a?323:3}px;top:${G.MSLOT}px`;d.innerHTML=`<img src="${LOGO(n)}"><b>${NAME[n]}</b><span>${t}</span>`;floor.appendChild(d);MCH.push(d);ping(n,2600)})}
// ---------- pulses and wires
function pulse(path,col,dur=1000,rev=false,r=3.4){if(!path)return;const L=path.getTotalLength();const c=document.createElementNS(NS,'circle');c.setAttribute('r',MOB?r*.7:r);c.setAttribute('fill',col);pul.appendChild(c);const t0=performance.now();
 (function f(t){let k=(t-t0)/dur;if(k>1){c.remove();return}const e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;const q=path.getPointAtLength((rev?1-e:e)*L);c.setAttribute('cx',q.x);c.setAttribute('cy',q.y);requestAnimationFrame(f)})(t0)}
function burst(path,col,rev,n=3,gap=230,dur=1000){for(let i=0;i<n;i++)setTimeout(()=>pulse(path,col,dur,rev,i?2.6:3.6),i*gap)}
// agent to agent: a soft arc that bows away from the tiles, drawn under them
function tempWire(a,b,col,dash,life=2600){const A=POS[a],B=POS[b];if(!A||!B)return null;let d;
 if(!MOB){const up=REL.includes(a)&&REL.includes(b);const drop=Math.min(G.ROW*.75,34+Math.abs(B[0]-A[0])*.1);const bot=up?Math.min(A[1],B[1])-24-Math.min(40,10+Math.abs(B[0]-A[0])*.05):Math.max(A[1],B[1])+drop;d=`M${A[0]},${A[1]} C${A[0]},${bot} ${B[0]},${bot} ${B[0]},${B[1]}`}
 else{if((A[0]<195)!==(B[0]<195)||A[1]<0||B[1]<0)return null;const mx=A[0]<195?A[0]-60:A[0]+60;d=`M${A[0]},${A[1]} Q${mx},${(A[1]+B[1])/2} ${B[0]},${B[1]}`}
 const p=document.createElementNS(NS,'path');p.setAttribute('d',d);p.setAttribute('fill','none');p.setAttribute('stroke',col);p.setAttribute('stroke-width',MOB?'1.4':'1.8');p.setAttribute('stroke-linecap','round');if(dash)p.setAttribute('stroke-dasharray',dash);
 p.style.transition='opacity .4s';p.style.opacity=0;web.appendChild(p);requestAnimationFrame(()=>p.style.opacity=1);if(life)setTimeout(()=>{p.style.opacity=0;setTimeout(()=>p.remove(),450)},life);return p}
function ping(n,ms=1400){const e=AG[n];if(!e)return;e.classList.add('ping');setTimeout(()=>e.classList.remove('ping'),ms)}
// ---------- bubbles
function bubbleEl(a,b,t,tag,oth){const d=document.createElement('div');d.className='a2a'+(oth?' oth':' hot');d.innerHTML=`<div class="who"><img src="${LOGO(a)}">${NAME[a]}<em>to</em><img src="${LOGO(b)}">${NAME[b]}${tag?`<u>${tag}</u>`:''}</div><div class="bt">${t}</div>`;return d}
const SL={};
function showBubble(x,y,w,key,a,b,t,tag,oth,life){if(SL[key])return;SL[key]=1;const d=bubbleEl(a,b,t,tag,oth);Object.assign(d.style,{left:px(x),top:px(y),width:px(w)});stage.appendChild(d);requestAnimationFrame(()=>requestAnimationFrame(()=>d.classList.add('on')));
 if(life)setTimeout(()=>{d.classList.remove('on');setTimeout(()=>{d.remove();SL[key]=0},400)},life);return d}
function sayOwner(a,b,t,life=3800){if(MOB){const s=$('.strip')||el('div','strip','',{left:'16px',top:px(G.STRIP),width:'358px'});s.innerHTML=`<div class="who"><img src="${LOGO(a)}">${NAME[a]}<em>to</em><img src="${LOGO(b)}">${NAME[b]}<u>${CUR.name}</u></div><div class="tx2">${t}</div>`;return}
 $$('.a2a.hot').forEach(e=>e.remove());SL.o0=0;const s=OWN[0];return showBubble(s[0],s[1],s[2],'o0',a,b,t,CUR.name,false,life)}
// other owners' work: one bubble at a time, kept inside the floor, never over this owner's specialists
function sayOther(a,b,t){if(MOB)return;const f=$('.feed',floor);if(!f)return;const set=()=>{f.innerHTML=`<span class="fd"></span><img src="${LOGO(a)}">${NAME[a]}<em>to</em><img src="${LOGO(b)}">${NAME[b]}<span class="ft">${t}</span>`;f.classList.remove('out')};
 if(STOP>=0&&!window.READY){set();return}f.classList.add('out');setTimeout(set,280)}
function chatter(once,tries=0){const c=C.chatter[Math.floor(Math.random()*C.chatter.length)];
 const bad=REL.includes(c[0])||REL.includes(c[1])||!POS[c[0]]||!POS[c[1]]||(!MOB&&POS[c[0]]&&POS[c[1]]&&(Math.abs(POS[c[0]][0]-POS[c[1]][0])>G.cw*3.2||Math.abs(POS[c[0]][1]-POS[c[1]][1])>G.ROW*1.5))||(MOB&&(POS[c[0]][1]<0||POS[c[1]][1]<0||(POS[c[0]][0]<195)!==(POS[c[1]][0]<195)));
 if(bad){if(tries<80)return chatter(once,tries+1);return}
 sayOther(c[0],c[1],c[2]);
 const w=tempWire(c[0],c[1],'#a59fad','3 4',once?0:2600);if(w)burst(w,'#8a8492',false,2,260,1100);ping(c[0]);setTimeout(()=>ping(c[1]),700);
 
 if(!once)setTimeout(chatter,R(2600,4200))}
// ---------- owner card (Desk dossier)
const PAL=[['#ffe2cf','#9a3b0e'],['#dff1e6','#1d6b3c'],['#e4e6ff','#3a3f9e'],['#fde7f3','#b0126c'],['#fff1c9','#7a5a00']];
const est='<span class="etag">est</span>';
function code(){const L='ABCDEFGHJKLMNPQRSTUVWXYZ',d=()=>Math.floor(rnd()*10);return pick(L)+d()+d()+d()+pick(L)+d()+d()}
function countUp(el,to,ms=1400){if(!el)return;if(FF||STOP>=0){el.textContent=to;return}const t0=performance.now();(function f(t){const k=Math.min(1,(t-t0)/ms),e=1-Math.pow(1-k,3);el.textContent=Math.round(to*e);if(k<1)requestAnimationFrame(f)})(t0)}
let SC='',TRK=0,NX=false;
function buildCard(p){SC=code();NX=false;const[bg,fg]=PAL[p.s%5];const ini=p.ini||(p.name[0]+p.biz[0]);
 if(MOB){card.innerHTML=`<svg class="ring"><rect class="r1" rx="18"/><rect class="r2" rx="18" pathLength="100"/></svg><div class="hd on"><div class="pav6" style="width:36px;height:36px;background:${bg};color:${fg};font-size:13px">${ini}</div><div style="min-width:0;flex:1"><div class="l1"><span class="nm6">${p.name}</span></div><div class="bz l2">${p.biz} · ${p.city}</div></div><div class="sc">Bespoke strategy<span class="code" id="sc"></span></div></div>
  <div class="ml"><b>Next</b><span class="t" id="nx"><span class="plan">Planning with the desk<span class="typ2"><i></i><i></i><i></i></span></span></span></div>
  <div class="ml"><b>Pending</b>${p.pend.slice(0,2).map(x=>`<span class="pc">${x}</span>`).join('')}</div>`;return}
 const cds=p.cards.map(x=>`<i><img src="${C.cardg}" alt="">${x}</i>`).join('');
 card.innerHTML=`<svg class="ring"><rect class="r1" rx="20"/><rect class="r2" rx="20" pathLength="100"/></svg>
 <div class="hd"><div class="pav6" style="width:44px;height:44px;background:${bg};color:${fg}">${ini}<span class="em">${p.emo}</span></div><div><span class="nm6">${p.name}</span><span class="bz">${p.biz} · ${p.city}</span></div></div>
 <div class="pill"><span class="lbl">Bespoke strategy</span><span class="code" id="sc"></span></div>
 <div class="kn"><span>Desk dossier</span><span><span id="trk">0</span> of 50+ tracked</span></div>
 <div class="rw"><span>Cards on file</span><b><div class="cds">${cds}</div></b></div>
 <div class="rw"><span>Card spend</span><b>$<span id="cu1">0</span>k a year${est}<small class="g">${p.top}</small></b></div>
 <div class="rw"><span>Points a year</span><b>${p.before}k today <span class="ar">→</span> <span style="color:var(--ac)"><span id="cu3">0</span>k${est}</span></b></div>
 <div class="rw"><span>Next trip</span><b id="nx"><span class="plan">Planning with the desk<span class="typ2"><i></i><i></i><i></i></span></span></b></div>
 <div class="rw"><span>Requests</span><b><div class="pend" id="pd">${p.pend.slice(0,2).map(x=>`<i>${x}</i>`).join('')}</div></b></div>
 <div class="ppf6">Example owner. Fictional details. Figures are estimates.</div>`}
function trk(){const e=$('#trk');if(e)e.textContent=TRK}
function cardIntro(p){const hd=$('.hd',card);hd&&hd.classList.add('on');const sc=$('#sc');let i=0;
 if(FF||STOP>=0){sc.textContent=SC;$$('.kn,.rw,.ppf6,.pill',card).forEach(r=>r.classList.add('on'));countUp($('#cu1'),p.spend);countUp($('#cu3'),p.after);TRK=p.cards.length;trk();return}
 setTimeout(()=>{const pill=$('.pill',card);pill&&pill.classList.add('on');(function ty(){sc.innerHTML=SC.slice(0,i)+'<span class="cur"></span>';if(i++<SC.length)setTimeout(ty,95);else setTimeout(()=>sc.textContent=SC,900)})()},350);
 TRK=p.cards.length;trk();
 $$('.kn,.rw,.ppf6',card).forEach((r,j)=>setTimeout(()=>{r.classList.add('on');if(r.querySelector('#cu1'))countUp($('#cu1'),p.spend);if(r.querySelector('#cu3'))countUp($('#cu3'),p.after,1700)},1100+j*320))}
function setNext(p){const nx=$('#nx');if(!nx||NX)return;NX=true;nx.innerHTML=MOB?`${p.nxt}${est}`:`${p.nxt}<small>${p.nxte}${est}</small>`;const row=nx.closest('.rw')||nx.closest('.ml');if(row){row.classList.add('flash');setTimeout(()=>row.classList.remove('flash'),1500)}}
function pendProgress(){const pd=$('#pd');if(!pd)return;const f=pd.children[0];if(f&&!f.classList.contains('ip')){f.classList.add('ip');f.insertAdjacentHTML('beforeend','<em>on it</em>')}}
function pendAdd(p){const pd=$('#pd');if(!pd||pd.children.length>2)return;const t=p.pend[2];if(!t)return;const i=document.createElement('i');i.className='new';i.innerHTML=t+'<em>new</em>';pd.appendChild(i);requestAnimationFrame(()=>requestAnimationFrame(()=>i.classList.remove('new')))}
function pendSent(){const pd=$('#pd');if(!pd)return;const f=pd.children[0];if(f){const em=f.querySelector('em');if(em)em.textContent='sent to desk'}}
// ---------- chat
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let lastW=null,rc=null,RUN=0,CLK=[9,12],A2AQ=[];
function flip(fn){const h0=ci.offsetHeight;fn();const d=ci.offsetHeight-h0;if(d<=0||FF>99)return;ci.style.transition='none';ci.style.transform=`translateY(${d}px)`;ci.offsetHeight;ci.style.transition='transform .45s cubic-bezier(.2,.7,.2,1)';ci.style.transform='none';while(ci.children.length>60)ci.removeChild(ci.firstChild)}
const who=w=>w==='o'?'o':w==='f'?'f':'s';
function lines(h){return h.split(/(?<=[.!?])\s+(?=[A-Z0-9$"'(])/).map(s=>`<span class="ln">${s}</span>`).join('')}
function richCard(p,kind){const d=p.dest,m=p.mer;
 if(kind==='map')return `<div class="xc"><div class="im" style="background-image:url(${C.photo[d.i]})"><span class="lb">${d.title}</span></div><div class="mp" style="background-image:url(${C.mapd[d.i]})"><i class="pin"></i><span class="tag">Award space not guaranteed</span></div><div class="ft"><b>${p.nxt}</b><span>${d.sub}. Value about ${p.nxte}<i class="e">est</i></span></div><div class="att">Photo: ${C.cred[d.i]} · Map data © OpenStreetMap contributors</div></div>`;
 return `<div class="xc"><div class="mh"><span class="ml"><img src="${C.mlogo[m.k]}"></span><div><b>${m.name}</b><span>Where ${p.name} spends · ${m.cat}</span></div></div><div class="mp" style="background-image:url(${C.mapc[p.s]})"><i class="pin pk"></i><span class="tag">${p.city} · example</span></div><div class="ft"><div class="chips"><i>$${m.k_yr}k a year here<i class="e">est</i></i><i>Routed to ${m.card}</i></div></div><div class="att">Merchant logo shown for identification only · Map data © OpenStreetMap contributors</div></div>`}
function msgEl(b,typing){const k=who(b.w),d=document.createElement('div');d.className='mm '+k+(k==='s'?' sp':'');
 const body=typing?`<div class="b6 typ"><i></i><i></i><i></i></div>`:`<div class="b6">${b.q?`<div class="q">${b.q}</div>`:''}${lines(b.h)}</div>`;
 if(k==='o'){d.innerHTML=body;return d}
 const same=lastW===String(b.w)&&!typing;const avh=k==='f'?`<img class="av avfo" src="${C.foi}">`:`<img class="av" src="${LOGO(b.w)}">`;
 const nm=k==='s'&&!same?`<div class="nm5">${NAME[b.w]} specialist<b>${CUR.rel.find(r=>r[0]===b.w)[1]}</b></div>`:(k==='f'&&!same&&!typing?`<div class="nm5">First Officer</div>`:'');
 const rich=(!typing&&b.card)?richCard(CUR,b.card):'';
 d.innerHTML=avh+`<div class="col">${nm}${body}${rich}</div>`;return d}
function tick(){CLK[1]++;if(CLK[1]>59){CLK[1]=0;CLK[0]++}$('#clk').textContent=CLK[0]+':'+String(CLK[1]).padStart(2,'0')}
const tstr=()=>CLK[0]+':'+String(CLK[1]).padStart(2,'0')+' PM';
function banner(t,b){$('#bt').textContent=t;$('#bb').textContent=b;$('#ban').classList.add('on');setTimeout(()=>$('#ban').classList.remove('on'),3600)}
function speak(n,on){const e=AG[n];if(on){LOCK[n]=1;e&&e.classList.add('spk');const s=e&&e.querySelector('.st');if(s)s.textContent='Briefing now';burst($('#w'+n,web),C.acc[CUR.tab][0],true,3,240,1050);setTimeout(()=>FOel.classList.add('spk'),700);setTimeout(()=>FOel.classList.remove('spk'),1300)}
 else{e&&e.classList.remove('spk');const r=CUR.rel.find(x=>x[0]===n);const s=e&&e.querySelector('.st');if(s)s.textContent=relSt(CUR,n,r?r[1]:'')}}
async function run(p,ff){const my=++RUN;let dsk=null,lastF='',bi=0,prevSpec=null,spoken=new Set(),planSet=false;
 const T=x=>ff>bi?0:x;const[h,m]=p.t0.split(':').map(Number);CLK=[h,m];$('#clk').textContent=p.t0;
 flip(()=>{const t=document.createElement('div');t.className='ts';t.textContent='Tonight '+p.t0+' PM ET';ci.appendChild(t)});
 for(bi=0;bi<p.beats.length;bi++){const b=Object.assign({},p.beats[bi]);if(my!==RUN)return;const k=who(b.w);
  if(bi%4===3)tick();
  if(k!=='s'&&dsk){const d=dsk;dsk=null;flip(()=>d.remove())}
  if(STOP>=0&&bi===STOP){ // freeze for review stills
   if(k==='s'){speak(b.w,true);if(prevSpec&&prevSpec.w!==b.w){tempWire(prevSpec.w,b.w,C.acc[p.tab][0],'5 4',0);ping(b.w,99999)}
    dsk=document.createElement('div');dsk.className='dsk fo-only';dsk.innerHTML=`<div class="typ"><i></i><i></i><i></i></div>First Officer is checking with the desk`;flip(()=>ci.appendChild(dsk));flip(()=>ci.insertBefore(msgEl(b,true),dsk))}
   else if(k==='f'){flip(()=>ci.appendChild(msgEl(b,true)))}
   if(k==='s'&&prevSpec&&prevSpec.w!==b.w)A2AQ.push([prevSpec.w,b.w,prevSpec.f||'']);A2AQ.slice(-2).forEach(x=>sayOwner(x[0],x[1],x[2],0));if(!Q.has('nochat'))chatter(1);mobChips();window.READY=1;return}
  if(k==='o'){await sleep(T(900+b.t.length*12));if(b.re&&lastF)b.q='Replying to First Officer: '+lastF.slice(0,58)+'...';burst($('#wout',web),'#FA1896',true,2,260,1000);
   flip(()=>{const e=msgEl(b);ci.appendChild(e);if(rc)rc.remove();rc=document.createElement('div');rc.className='rcpt';rc.textContent='Delivered';ci.appendChild(rc)});lastW='o';prevSpec=null;await sleep(T(700))}
  else{if(k==='s'){speak(b.w,true);spoken.add(b.w);TRK=p.cards.length+spoken.size;trk();
    if(prevSpec&&prevSpec.w!==b.w){const a=prevSpec.w,bb=b.w,w=T(1)?tempWire(a,bb,C.acc[p.tab][0],'5 4',3200):null;if(w)burst(w,C.acc[p.tab][0],false,3,240,1000);ping(bb,1800);const t=prevSpec.f||'';A2AQ.push([a,bb,t]);if(T(1))sayOwner(a,bb,t)}
    if(!dsk){dsk=document.createElement('div');dsk.className='dsk fo-only';dsk.innerHTML=`<div class="typ"><i></i><i></i><i></i></div>First Officer is checking with the desk`;flip(()=>ci.appendChild(dsk))}}
   else{burst($('#wout',web),'#FA1896',false,2,260,1000);FOel.classList.add('spk')}
   if(rc&&rc.textContent==='Delivered')rc.textContent='Read '+tstr();
   const ty=msgEl(b,true);flip(()=>{if(k==='s'&&dsk)ci.insertBefore(ty,dsk);else ci.appendChild(ty)});
   await sleep(T(Math.max(k==='s'?950:1000,Math.min(k==='s'?2300:2700,b.t.length*(k==='s'?15:21)))));if(my!==RUN)return;
   const e=msgEl(b);flip(()=>ty.replaceWith(e));lastW=String(b.w);if(k==='f')lastF=b.t;
   if(b.tap)setTimeout(()=>{const bb=e.querySelector('.b6');const s=document.createElement('span');s.className='tp';s.textContent=b.tap;bb.appendChild(s)},T(900));
   if(b.ban)setTimeout(()=>{banner(b.ban[0],b.ban[1]);setTimeout(pendSent,400)},T(500));
   if(k==='s')prevSpec=b;
   if(k==='f'&&spoken.size&&!planSet){planSet=true;setNext(p);pendProgress()}
   if(bi===Math.round(p.beats.length*.55))pendAdd(p);
   await sleep(T(k==='s'?650:750));if(k==='s')speak(b.w,false);else FOel.classList.remove('spk')}
 }
 if(dsk)dsk.remove();await sleep(4500);if(my!==RUN)return;load(pickP(),0)}
function pickP(){const last=+localStorage.getItem('fo9_p');let i;do{i=Math.floor(Math.random()*PS.length)}while(i===last&&PS.length>1);return i}
let HOMEV=false; // Home tab shows as selected when Home was tapped (approved Oct 21)
function load(i,ff){CUR=PS[i];localStorage.setItem('fo9_p',i);RUN++;
 ['t-earn','t-burn','t-return','t-learn'].forEach(c=>B.classList.remove(c));B.classList.add('t-'+CUR.tab);
 $$('#tabs > div').forEach(d=>d.classList.toggle('on',d.dataset.t===(HOMEV?'home':CUR.tab)));HOMEV=false;
 const[bg,fg]=PAL[CUR.s%5];$('#pav').innerHTML=`<div class="pav6" style="width:32px;height:32px;background:${bg};color:${fg};font-size:12.5px">${CUR.ini||(CUR.name[0]+CUR.biz[0])}</div>`;
 ci.innerHTML='';ci.style.transform='none';lastW=null;rc=null;A2AQ=[];$$('.a2a').forEach(e=>e.remove());for(const k in SL)SL[k]=0;
 if(MOB)placeDesk();buildFloor(CUR);buildCard(CUR);cardIntro(CUR);mobChips();run(CUR,ff||0)}
function placeDesk(){if(MOB){if(!CUR)return;const mx=measureCards([CUR]);G.cardH=mx;G.FO[1]=G.CARD[1]+mx+44;G.PH[1]=G.FO[1]+G.FS/2+26;G.STRIP=G.PH[1]+G.PHH+18;
  CTAS.style.top=px(G.STRIP+110);MICRO.style.top=px(G.STRIP+110+62);TMK.style.top=px(G.STRIP+110+62+MICRO.offsetHeight+6);SH.H=G.STRIP+110+62+MICRO.offsetHeight+6+TMK.offsetHeight+22;fit();[web,pul].forEach(s=>s.setAttribute('height',SH.H));
  FOel.style.top=px(G.FO[1]-G.FS/2);FOL.style.top=px(G.FO[1]-19);ph.style.top=px(G.PH[1]);return}const cb=G.CARD[1]+measureCards();G.FO[1]=Math.max(cb+40+G.FS/2+14,680);G.Y0=G.FO[1]+G.FS/2+70;G.Y1=G.Y0+34+3*G.ROW+112;SH.H=G.Y1+112;fit();[web,pul].forEach(s=>s.setAttribute('height',SH.H));MICRO.style.top=px(G.Y1+18);TMK.style.top=px(G.Y1+18+MICRO.offsetHeight+4);
 FOel.style.top=px(G.FO[1]-G.FS/2);FOL.style.top=px(G.FO[1]-G.FS/2-50)}
function measureCards(list){let mx=0;const keep=CUR;(list||PS).forEach(p=>{CUR=p;buildCard(p);$$('.kn,.rw,.ppf6,.pill',card).forEach(r=>r.classList.add('on'));NX=false;setNext(p);pendProgress();pendAdd(p);$$('#pd i',card).forEach(i=>i.classList.remove('new'));mx=Math.max(mx,card.offsetHeight)});CUR=keep;card.innerHTML='';return mx}
window.GO=function(){layout();buildFixed();placeDesk();const i=Q.has('p')?PS.findIndex(x=>x.s===+Q.get('p')):pickP();load(i,FF||(STOP>=0?STOP:0));
 if(STOP<0){setTimeout(chatter,1600);setInterval(spotTick,1300);if(MOB)setInterval(mobChips,3200)}};
FOREADY().then(()=>setTimeout(GO,150));
$$('.micro a').forEach(a=>a.onclick=()=>{const d=document.getElementById('disc');if(!d)return;d.classList.remove('col');d.scrollIntoView({behavior:'smooth'})});
document.querySelectorAll('#disc .more').forEach(a=>a.onclick=()=>document.getElementById('disc').classList.remove('col'));
})();
}
})();
/* Logo-tile containment (Oct 23): a desktop tile's name and status line stay on one line inside the
   label plate. Text is unchanged; only when a line is wider than its plate is its font size stepped down
   to fit (never below 9px). Runs on every re-render and status change. */
(function(){
 function fit(root){root.querySelectorAll('.ag .tx').forEach(tx=>{const a=tx.parentNode;const cs=getComputedStyle(tx);
  const avail=a.clientWidth-8-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);
  tx.querySelectorAll('b,.st').forEach(el=>{if(el.dataset.fitT===el.textContent&&el.dataset.fitA==avail)return;
   el.style.fontSize='';if(getComputedStyle(el).display==='none'){return}
   const w=el.scrollWidth;if(w>avail+0.5){const fs=parseFloat(getComputedStyle(el).fontSize);el.style.fontSize=Math.max(9,Math.floor(fs*avail/w*10)/10)+'px'}
   el.dataset.fitT=el.textContent;el.dataset.fitA=avail})})}
 const go=()=>{const R=window.HROOT;if(!R){setTimeout(go,200);return}
  const run=()=>fit(R);new MutationObserver(run).observe(R,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:['class']});run()};
 go();
})();
