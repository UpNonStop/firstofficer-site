/* calculator.html: a sibling of home-modes.html.
   Hero: the landing's rotating background photos (same set, same 5.2s crossfade) behind a landing-style card,
   the Basic calculator: one spend figure, spread over the industry's typical mix (the one picked under Go advanced, else Other) and run
   through FO_CALC (fo-calc-core.js), the same card stack, caps and valuation as Go advanced, so both modes give the same answer.
   Plus a one-time "Watch it run" sweep ($10K -> $80K), stopped by any touch, skipped under reduced motion.
   FO_REDEMPTION_BASIS values, est. Mockup only; every figure is an estimate.
   URL: ?ind=<slug> or ?industry= sets the industry for both modes; ?ex=<first name> and ?m=adv scroll to Go advanced; ?spend=15000 sets Basic. */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],BS=window.FO_REDEMPTION_BASIS,$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var C=window.FO_CALC,FEE=BS.fee/12,GATE=BS.gate,UTIL=BS.util,GMAX=80000;if(!C)return;
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function r10(n){return Math.round(n/10)*10}
function u10(n){return usd(r10(n))}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function c2(n){return (+n).toFixed(2).replace(/0$/,'').replace(/0$/,'').replace(/\.$/,'.0')+'¢'}
function sg(n){n=r10(n);return (n<0?'−':'+')+usd(Math.abs(n))}
function nx(v){return v.toFixed(1)+'×'}
function rng(t){return t.floor===t.ceil?c2(t.floor):c2(t.floor)+' to '+c2(t.ceil)}
var q=location.href,want=((q.match(/[?&#]ex=([a-z]+)/i)||[])[1]||'').toLowerCase(),first=true,inst=false;
/* ---- short tween: from what is on screen to the new value, 200ms; instant while the sweep runs ---- */
function tw(el,to,fmt){if(!el)return;var from=el._c==null?to:el._c;el._v=to;cancelAnimationFrame(el._r);
  if(RM||first||inst||from===to){el._c=to;el.textContent=fmt(to);return}
  var t0=null,dur=200;
  function f(ts){if(t0==null)t0=ts;var p=Math.min(1,(ts-t0)/dur),e=1-Math.pow(1-p,3);el._c=from+(to-from)*e;el.textContent=fmt(el._c);if(p<1)el._r=requestAnimationFrame(f)}
  el._r=requestAnimationFrame(f)}
function K(R,n,to,fmt){$$('[data-k="'+n+'"]',R).forEach(function(e){tw(e,to,fmt)})}
function T(R,n,v){$$('[data-k="'+n+'"]',R).forEach(function(e){e.textContent=v})}
function U(id){for(var i=0;i<BS.types.length;i++)if(BS.types[i].id===id)return BS.types[i];return BS.types[0]}
function pc(v,m){return Math.max(0,Math.min(100,v/m*100))+'%'}
/* ---- the month and the verdict: FO_CALC in fo-calc-core.js, the one model Go advanced uses too (card stack, yearly caps, valuation) ---- */
function say(R,tEl,pEl,v){tEl.textContent=v.t;pEl.innerHTML=v.p+(v.c==='no'?' <a href="freebies.html">Get the Freebies →</a>':'');
  $$('.bvk',R).forEach(function(b){b.textContent=v.c==='fit'?'✓':v.c==='meh'?'≈':'×'})}
/* balance bar: value found fills against the $550 marker; past it is pink, short of it reads as a gap */
function bar(bal,r){var bm=FEE*Math.max(3,Math.ceil(Math.max(0,r.hi)*1.1/FEE)),mid=Math.max(0,r.mid);T(bal,'bmax',usd(bm));
  $('.base',bal).style.width=pc(Math.min(mid,FEE),bm);
  var ov=$('.over',bal);ov.style.left=pc(FEE,bm);ov.style.width=pc(Math.max(0,mid-FEE),bm);
  var sh=$('.short',bal);sh.style.left=pc(Math.min(mid,FEE),bm);sh.style.width=pc(Math.max(0,FEE-mid),bm);
  sh.setAttribute('data-t',mid<FEE?'short '+u10(FEE-mid):'');
  var rg=$('.rng',bal);rg.style.left=pc(Math.max(0,r.lo),bm);rg.style.width=pc(Math.max(0,r.hi)-Math.max(0,r.lo),bm);
  $('.mark',bal).style.left=pc(FEE,bm);$('.mark',bal).classList.toggle('lo',FEE/bm<.12);
  bal.setAttribute('aria-label','Your desk finds about '+u10(mid)+' a month, est., against the $550 a month fee')}
function paint(R,r){var Z=function(v){return Math.max(0,v)},fm=function(v){return '~'+u10(Z(v))};
  K(R,'find',r.mid,fm);K(R,'m-find',r.mid,fm);
  T(R,'findr',r.flat?'at '+c2(r.u.floor)+' a point':u10(Z(r.lo))+' to '+u10(Z(r.hi)));
  K(R,'net',r.mid-FEE,sg);T(R,'netr',(r.flat?'at '+c2(r.u.floor)+' a point':sg(r.lo-FEE)+' to '+sg(r.hi-FEE))+', est.');
  K(R,'rx',Z(r.mid)/FEE,nx);K(R,'m-rx',Z(r.mid)/FEE,nx);T(R,'rxr',(r.flat?'at '+c2(r.u.floor)+' a point':nx(Z(r.lo)/FEE)+' to '+nx(Z(r.hi)/FEE))+', est.');
  K(R,'plus',Math.max(0,r.d-r.t),function(v){return '+'+pts(v)})}
/* ================= BASIC ================= */
var BAS=$('#bas'),bv=$('#bv'),bs=$('#bs'),B=35000;
var sp=(q.match(/[?&#]spend=(\d+)/)||[])[1];if(sp)B=Math.min(2e6,+sp);
function fill(s){s.style.setProperty('--p',Math.min(100,s.value/s.max*100)+'%')}
/* Basic slider: 0..1000 positions on a piecewise scale up to $1M+ a month. $0-20K is 30% of the track, $20-100K 30%, $100-250K 20%, $250K-1M 20%.
   Snaps to $500 under $20K, $1K to $100K, $5K to $250K, $25K above. The typed box takes any figure up to $2M. */
var SEG=[[0,0],[300,20000],[600,100000],[800,250000],[1000,1e6]],STP=[500,1000,5000,25000],SMAX=1e6;
function stepAt(v){return v<20000?500:v<100000?1000:v<250000?5000:25000}
function p2v(p){for(var i=0;i<4;i++){var a=SEG[i],b=SEG[i+1];if(p<=b[0]){var v=a[1]+(p-a[0])/(b[0]-a[0])*(b[1]-a[1]);return Math.min(SMAX,Math.round(v/STP[i])*STP[i])}}return SMAX}
function v2p(v){v=Math.max(0,Math.min(SMAX,v));for(var i=0;i<4;i++){var a=SEG[i],b=SEG[i+1];if(v<=b[1])return a[0]+(v-a[1])/(b[1]-a[1])*(b[0]-a[0])}return 1000}
function kmo(v){return v>=1e6?'$'+(Math.round(v/1e5)/10).toString().replace(/\.0$/,'')+'M':'$'+Math.round(v/1e3)+'K'}
function bcalc(){var r=C.forSpend(C.idx,B,'mix','ex'),v=C.verdict(r);
  bv.value=B.toLocaleString('en-US');if(document.activeElement!==bv){}
  bs.value=Math.round(v2p(B));bs.setAttribute('aria-valuetext',(B>=SMAX?'$1M+':usd(B))+' a month');fill(bs);bv.classList.toggle('lg',bv.value.length>7);
  paint(BAS,r);bar($('#bbal'),r);
  BAS.className='cq '+v.c+(r.mid>=1e4?' big':'');say(BAS,$('#bvt'),$('#bvp'),v);
  $$('a[data-full]',BAS).forEach(function(a){if(!a._b)a._b=a.getAttribute('href').split('#')[0];a.setAttribute('href',a._b.replace(/([?&])m=adv.*$/,'$1m=adv&spend='+B))})}
bs.addEventListener('input',function(){halt();B=p2v(+bs.value);bcalc()});
bs.addEventListener('keydown',function(e){var k=e.key,up=k==='ArrowRight'||k==='ArrowUp',dn=k==='ArrowLeft'||k==='ArrowDown';
  if(k==='Home'||k==='End'){e.preventDefault();B=k==='Home'?0:SMAX;bcalc();return}
  if(!up&&!dn)return;e.preventDefault();var b=Math.min(B,SMAX);
  B=up?Math.min(SMAX,Math.floor(b/stepAt(b))*stepAt(b)+stepAt(b)):Math.max(0,Math.ceil(b/stepAt(b-1))*stepAt(b-1)-stepAt(b-1));bcalc()});
bv.addEventListener('input',function(){halt();var c=bv.selectionStart,l=bv.value.length;B=Math.min(2e6,+(bv.value.replace(/[^0-9]/g,''))||0);bcalc();
  var n=bv.value.length;try{bv.setSelectionRange(Math.max(0,c+n-l),Math.max(0,c+n-l))}catch(e){}});
bv.addEventListener('focus',function(){bv.select()});
/* Watch it run: $10K -> $80K once, ~3.2s, any touch stops it */
var run=$('#brun'),raf=0,running=false;
function stop(){if(!running)return;running=false;inst=false;cancelAnimationFrame(raf);run.classList.remove('on');run.setAttribute('aria-pressed','false');$('span',run).textContent='Watch it run';bcalc()}
/* a typed or slid value wins over a sweep in flight: stop it without repainting the old value */
function halt(){if(!running)return;running=false;inst=false;cancelAnimationFrame(raf);run.classList.remove('on');run.setAttribute('aria-pressed','false');$('span',run).textContent='Watch it run'}
function go(){if(running){stop();return}
  if(RM){B=80000;bcalc();return}
  running=true;inst=true;run.classList.add('on');run.setAttribute('aria-pressed','true');$('span',run).textContent='Running · tap to stop';
  var t0=null,dur=3200,a=10000,b=80000;
  function f(ts){if(!running)return;if(t0==null)t0=ts;var p=Math.min(1,(ts-t0)/dur),e=p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;
    B=Math.round((a+(b-a)*e)/500)*500;bcalc();if(p<1)raf=requestAnimationFrame(f);else{running=false;stop.call();inst=false;run.classList.remove('on');$('span',run).textContent='Run it again';run.setAttribute('aria-pressed','false')}}
  raf=requestAnimationFrame(f)}
run.addEventListener('click',go);
['pointerdown','keydown','wheel','touchstart'].forEach(function(ev){window.addEventListener(ev,function(e){if(running&&!run.contains(e.target))stop()},{capture:true,passive:true})});
/* Go advanced lives in fo-calc-adv.js. When its industry changes, Basic follows (FO_CALC.on, below), so both modes answer for the same mix. */
/* ================= GO ADVANCED: scroll down, no tabs ================= */
function toAdv(sm){stop();var el=$('#advs');if(!el)return;var y=el.getBoundingClientRect().top+scrollY-70;scrollTo({top:y,behavior:sm&&!RM?'smooth':'auto'})}
$$('a[href="#advs"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();toAdv(true)})});
(function(){var g=$('#bgo'),A=$('#advs');if(!g)return;function seen(){g.classList.add('seen')}
g.addEventListener('click',seen);$$('a[href="#advs"]').forEach(function(a){a.addEventListener('click',seen)});
if(!A)setTimeout(seen,8000);
if(A&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){seen();io.disconnect()}})},{threshold:.15});io.observe(A)}})();
/* ================= HERO BACKGROUND: the landing's rotating photos ================= */
/* the hero photos come from pages31.js (phone-sized files on phones); the second rotator that sent desktop photos to phones is gone (QA re-audit item 4) */
bcalc();C.on(function(){bcalc()});
if(want||/[?&#]m=adv/.test(q))setTimeout(function(){toAdv(false)},60);
first=false;
})();
