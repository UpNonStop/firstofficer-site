/* calculator-modes.html: a sibling of home-modes.html.
   Hero: the landing's rotating background photos (same set, same 5.2s crossfade) behind a landing-style card,
   the Basic calculator: one spend figure -> one blended rate -> what your desk finds a month vs the $550 fee,
   plus a one-time "Watch it run" sweep ($10K -> $80K), stopped by any touch, skipped under reduced motion.
   Go advanced (below): example owners, spend by line, cards today, how you'll use the points, points table.
   Same maths as the landing (annual / 12), FO_REDEMPTION_BASIS values, est. Mockup only; every figure is an estimate.
   URL: ?ex=<first name> scrolls to Advanced on that owner; ?m=adv scrolls to Advanced; ?spend=15000 sets Basic. */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],BS=window.FO_REDEMPTION_BASIS,$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var FEE=BS.fee/12,GATE=BS.gate,UTIL=BS.util,GMAX=80000,BT=1.2,BD=3.4;
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function r10(n){return Math.round(n/10)*10}
function u10(n){return usd(r10(n))}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function c2(n){return (+n).toFixed(2).replace(/0$/,'').replace(/0$/,'').replace(/\.$/,'.0')+'¢'}
function sg(n){n=r10(n);return (n<0?'−':'+')+usd(Math.abs(n))}
function nx(v){return v.toFixed(1)+'×'}
function rng(t){return t.floor===t.ceil?c2(t.floor):c2(t.floor).replace('¢','')+'–'+c2(t.ceil)}
/* Advanced starts from an industry, not a person: each industry reuses one example's line data, so the numbers stay identical.
   Things to consider are general, plain prompts, not advice. ?ex=<first name> still maps to that example's industry; ?ind=<slug> works too. */
var TH={'Insurance agency':['Lead-gen and ad spend is often the biggest line','Agency software and subscriptions billed every month','Travel to carriers and conferences','Which vendors take cards without a surcharge'],
'HVAC':['Fuel and fleet costs','Supplier and equipment purchases','Seasonal swings in what you spend','Vendors who take cards without fees'],
'Dental practice':['Supply orders, often from a few large vendors','Practice and imaging software','Lab fees, and whether your labs take cards','Patient marketing and ads'],
'Marketing agency':['Client ad spend that runs through your cards','Software seats that grow with the team','Contractors, and which ones take cards','Shoot and client travel'],
'Law firm':['Client costs you pay up front','Travel to depositions and court','Filing fees and research software','Which fees can be paid by card at all'],
'Restaurant':['Food suppliers, and whether they take cards','Delivery apps and ads','Phone, internet and utilities','Card surcharges, where margins are thin'],
'Trucking':['Fleet fuel, usually most of the spend','Tires, repairs and parts','Tolls and permits','Where fuel is bought, and how it is paid for'],
'Real estate':['Listing ads and portals','Signage and print','Travel to showings','Closing gifts and client events'],
'E-commerce':['Ad spend on Meta and Google','Shipping and packaging','Inventory from your suppliers','Seasonal peaks around the holidays'],
'Contractor':['Materials, often the biggest line','Job-site hotels and travel','Fuel and equipment rental','Supplier terms versus paying by card'],
'Other':['Your biggest monthly lines first','Software, phone and internet billed each month','Travel for the business','Vendors who take cards without fees']};
var BLANK={first:'',ind:'Other',cats:[['Ads and marketing',0,'1x','4x'],['Software and phone',0,'1.5x','4x'],['Travel',0,'1x','3x'],['Everything else',0,'1x','2x']]};
var IN=P.concat([BLANK]);
function slug(t){return t.toLowerCase().replace(/[^a-z]+/g,'-').replace(/^-|-$/g,'')}
var q=location.href,want=((q.match(/[?&#]ex=([a-z]+)/i)||[])[1]||'').toLowerCase(),wi=((q.match(/[?&#]ind=([a-z-]+)/i)||[])[1]||'').toLowerCase(),idx=0;
IN.forEach(function(p,i){if((want&&p.first.toLowerCase()===want)||(wi&&slug(p.ind)===wi))idx=i});
function moK(p){return p.cats.reduce(function(a,c){return a+c[1]},0)}
var D,S=[],mix='ex',use='mix',first=true,inst=false;
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
/* ---- the shared month: lines of [spend, rate today, rate with desk] ---- */
function month(L,uid){var mo=0,t=0,d=0;L.forEach(function(l){mo+=l[0];t+=l[0]*l[1];d+=l[0]*l[2]});
  var u=U(uid),gain=Math.max(0,d-t)*UTIL;
  return {mo:mo,t:t,d:d,u:u,lo:gain*u.floor/100,mid:gain*u.mid/100,hi:gain*u.ceil/100,flat:u.floor===u.ceil}}
function verdict(r){var f=r.flat;
  if(r.mo<GATE)return {c:'no',t:'Not a fit yet.',p:'At '+usd(r.mo)+' a month on cards, $550 a month would cost you more than it finds. The fee starts to make sense past ~$25K a month, est.'};
  if(r.lo>=FEE)return {c:'fit',t:'Clears the fee.',p:'Even at the floor, the extra points beat $550 a month, est. Your Found Money Call checks it on your real statements.'};
  if(r.hi>=FEE)return {c:'meh',t:'Close call.',p:'It clears at the top of the range, not the floor. Your Found Money Call settles it on your real statements, free.'};
  return {c:'no',t:'Not a fit yet.',p:'The extra points find about '+(f?u10(r.lo):u10(r.lo)+' to '+u10(r.hi))+' a month, est., under the $550.'}}
function say(R,tEl,pEl,v){tEl.textContent=v.t;pEl.innerHTML=v.p+(v.c==='no'?' <a href="freebies-modes.html">Get the Freebies →</a>':'');
  $$('.bvk',R).forEach(function(b){b.textContent=v.c==='fit'?'✓':v.c==='meh'?'≈':'×'})}
/* balance bar: value found fills against the $550 marker; past it is pink, short of it reads as a gap */
function bar(bal,r){var bm=FEE*Math.max(3,Math.ceil(r.hi*1.1/FEE)),mid=r.mid;T(bal,'bmax',usd(bm));
  $('.base',bal).style.width=pc(Math.min(mid,FEE),bm);
  var ov=$('.over',bal);ov.style.left=pc(FEE,bm);ov.style.width=pc(Math.max(0,mid-FEE),bm);
  var sh=$('.short',bal);sh.style.left=pc(Math.min(mid,FEE),bm);sh.style.width=pc(Math.max(0,FEE-mid),bm);
  sh.setAttribute('data-t',mid<FEE?'short '+u10(FEE-mid):'');
  var rg=$('.rng',bal);rg.style.left=pc(r.lo,bm);rg.style.width=pc(r.hi-r.lo,bm);
  $('.mark',bal).style.left=pc(FEE,bm);$('.mark',bal).classList.toggle('lo',FEE/bm<.12);
  bal.setAttribute('aria-label','Your desk finds about '+u10(mid)+' a month, est., against the $550 a month fee')}
function paint(R,r){
  K(R,'find',r.mid,function(v){return '~'+u10(v)});K(R,'m-find',r.mid,function(v){return '~'+u10(v)});
  T(R,'findr',r.flat?'at '+c2(r.u.floor)+' a point':u10(r.lo)+'–'+u10(r.hi));
  K(R,'net',r.mid-FEE,sg);T(R,'netr',r.flat?'at '+c2(r.u.floor)+' a point, est.':sg(r.lo-FEE)+' to '+sg(r.hi-FEE)+', est.');
  K(R,'rx',r.mid/FEE,nx);K(R,'m-rx',r.mid/FEE,nx);T(R,'rxr',r.flat?'at '+c2(r.u.floor)+' a point, est.':nx(r.lo/FEE)+' to '+nx(r.hi/FEE)+', est.');
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
function bcalc(){var r=month([[B,BT,BD]],'mix'),v=verdict(r);
  bv.value=B.toLocaleString('en-US');if(document.activeElement!==bv){}
  bs.value=Math.round(v2p(B));bs.setAttribute('aria-valuetext',(B>=SMAX?'$1M+':usd(B))+' a month');fill(bs);bv.classList.toggle('lg',bv.value.length>7);
  paint(BAS,r);bar($('#bbal'),r);
  BAS.className='cq '+v.c+(r.mid>=1e4?' big':'');say(BAS,$('#bvt'),$('#bvp'),v);
  $$('a[data-full]',BAS).forEach(function(a){if(!a._b)a._b=a.getAttribute('href').split('#')[0];a.setAttribute('href',a._b.replace(/([?&])m=adv.*$/,'$1m=adv&spend='+B))})}
bs.addEventListener('input',function(){B=p2v(+bs.value);bcalc()});
bs.addEventListener('keydown',function(e){var k=e.key,up=k==='ArrowRight'||k==='ArrowUp',dn=k==='ArrowLeft'||k==='ArrowDown';
  if(k==='Home'||k==='End'){e.preventDefault();B=k==='Home'?0:SMAX;bcalc();return}
  if(!up&&!dn)return;e.preventDefault();var b=Math.min(B,SMAX);
  B=up?Math.min(SMAX,Math.floor(b/stepAt(b))*stepAt(b)+stepAt(b)):Math.max(0,Math.ceil(b/stepAt(b-1))*stepAt(b-1)-stepAt(b-1));bcalc()});
bv.addEventListener('input',function(){var c=bv.selectionStart,l=bv.value.length;B=Math.min(2e6,+(bv.value.replace(/[^0-9]/g,''))||0);bcalc();
  var n=bv.value.length;try{bv.setSelectionRange(Math.max(0,c+n-l),Math.max(0,c+n-l))}catch(e){}});
bv.addEventListener('focus',function(){bv.select()});
/* Watch it run: $10K -> $80K once, ~3.2s, any touch stops it */
var run=$('#brun'),raf=0,running=false;
function stop(){if(!running)return;running=false;inst=false;cancelAnimationFrame(raf);run.classList.remove('on');run.setAttribute('aria-pressed','false');$('span',run).textContent='Watch it run';bcalc()}
function go(){if(running){stop();return}
  if(RM){B=80000;bcalc();return}
  running=true;inst=true;run.classList.add('on');run.setAttribute('aria-pressed','true');$('span',run).textContent='Running · tap to stop';
  var t0=null,dur=3200,a=10000,b=80000;
  function f(ts){if(!running)return;if(t0==null)t0=ts;var p=Math.min(1,(ts-t0)/dur),e=p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;
    B=Math.round((a+(b-a)*e)/500)*500;bcalc();if(p<1)raf=requestAnimationFrame(f);else{running=false;stop.call();inst=false;run.classList.remove('on');$('span',run).textContent='Run it again';run.setAttribute('aria-pressed','false')}}
  raf=requestAnimationFrame(f)}
run.addEventListener('click',go);
['pointerdown','keydown','wheel','touchstart'].forEach(function(ev){window.addEventListener(ev,function(e){if(running&&!run.contains(e.target))stop()},{capture:true,passive:true})});
/* ================= ADVANCED ================= */
var ADV=$('#adv');
if(ADV){
var SEL=$('#cind');
SEL.innerHTML=IN.map(function(p,i){return '<option value="'+i+'">'+(p.ind==='Other'?'Other / start blank':p.ind)+'</option>'}).join('');
SEL.addEventListener('change',function(){idx=+SEL.value;load()});
$('#cuse').innerHTML=BS.types.map(function(t){return '<button type="button" role="radio" data-u="'+t.id+'" aria-checked="'+(t.id===use)+'"'+(t.id===use?' class="on"':'')+'><b>'+t.name+'</b><small>'+rng(t)+'</small></button>'}).join('');
$$('#cuse button').forEach(function(b){b.addEventListener('click',function(){use=b.dataset.u;$$('#cuse button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});calc()})});
$$('#cmix button').forEach(function(b){b.addEventListener('click',function(){mix=b.dataset.m;$$('#cmix button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});calc()})});
function rows(){var p=D;
  $('#crows').innerHTML=p.cats.map(function(c,i){var mx=Math.max(20,Math.ceil(c[1]*3/5)*5)*1000;
    return '<div class="crow"><label for="cv'+i+'">'+c[0]+'<small><s data-r="'+i+'">'+c[2]+'</s> → <b>'+c[3]+'</b> per $1</small></label>'+
    '<div class="cri"><span>$</span><input id="cv'+i+'" type="text" inputmode="numeric" autocomplete="off" value="'+(c[1]*1000).toLocaleString('en-US')+'" aria-label="'+c[0]+', dollars a month"></div>'+
    '<input class="crs" type="range" min="0" max="'+mx+'" step="100" value="'+c[1]*1000+'" aria-label="'+c[0]+', slider"></div>'}).join('');
  $$('#crows .crow').forEach(function(r,i){var t=$('input[type=text]',r),s=$('.crs',r);
    s.addEventListener('input',function(){S[i]=+s.value;t.value=S[i].toLocaleString('en-US');calc()});
    t.addEventListener('input',function(){var v=Math.min(2e6,+(t.value.replace(/[^0-9]/g,''))||0);S[i]=v;if(v>+s.max)s.max=Math.ceil(v/5000)*5000;s.value=v;calc()});
    t.addEventListener('blur',function(){t.value=S[i].toLocaleString('en-US')});
    t.addEventListener('focus',function(){t.select()})});
  $('#cet').innerHTML='<div class="ceh" role="row"><span>Points a month</span><span>Today</span><span>With desk</span></div>'+
    p.cats.map(function(c,i){return '<div class="cer" role="row"><span>'+c[0]+'</span><span data-et="'+i+'">–</span><span class="d" data-ed="'+i+'">–</span></div>'}).join('')+
    '<div class="cer tot" role="row"><span>Total</span><span data-k="vt">–</span><span class="d" data-k="vd">–</span></div>'}
function load(){D=IN[idx];S=D.cats.map(function(c){return c[1]*1000});SEL.value=idx;
  var o=D.ind==='Other',m=moK(D);
  $('#cwho').textContent=o?'Start blank, type your own':'Typical mix: $'+(Math.round(m*10)/10)+'K a month, est.';
  $('#ccth').textContent=o?'Things to consider for your business':'Things to consider for '+(D.ind==='HVAC'?'HVAC':D.ind.toLowerCase());
  $('#ccul').innerHTML=(TH[D.ind]||TH.Other).map(function(t){return '<li>'+t+'</li>'}).join('');
  rows();calc()}
function rateT(c){return mix==='ex'?parseFloat(c[2]):+mix}
function calc(){var L=D.cats.map(function(c,i){return [S[i],rateT(c),parseFloat(c[3])]}),r=month(L,use),v=verdict(r);
  L.forEach(function(l,i){tw($('[data-et="'+i+'"]'),l[0]*l[1],pts);tw($('[data-ed="'+i+'"]'),l[0]*l[2],pts);
    var s=$$('#crows .crs')[i];fill(s);$('[data-r="'+i+'"]').textContent=x(l[1])});
  K(ADV,'mo',r.mo,usd);K(ADV,'bl',r.mo?r.t/r.mo:0,x);K(ADV,'vt',r.t,pts);K(ADV,'vd',r.d,pts);
  T(ADV,'who',(D.ind==='Other'?'Your mix':D.ind)+' · at '+rng(r.u)+' a point');
  paint(ADV,r);bar($('#cbal'),r);
  T(ADV,'gatev','You: '+kmo(r.mo));
  var gt=$('#cgt');$('.fill',gt).style.width=pc(r.mo,GMAX);$('.fee',gt).style.left=pc(GATE,GMAX);gt.classList.toggle('under',r.mo<GATE);
  $('#cv').className='cv '+v.c;$('.cres').className='cres '+v.c+(r.mid>=1e4?' big':'');$('.cmini').className='cmini '+v.c;
  say(ADV,$('#cvt'),$('#cvp'),v)}
}
/* ================= GO ADVANCED: scroll down, no tabs ================= */
function toAdv(sm){stop();var el=$('#advs');if(!el)return;var y=el.getBoundingClientRect().top+scrollY-70;scrollTo({top:y,behavior:sm&&!RM?'smooth':'auto'})}
$$('a[href="#advs"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();toAdv(true)})});
(function(){var g=$('#bgo'),A=$('#advs');if(!g)return;function seen(){g.classList.add('seen')}
g.addEventListener('click',seen);$$('a[href="#advs"]').forEach(function(a){a.addEventListener('click',seen)});
if(!A)setTimeout(seen,8000);
if(A&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){seen();io.disconnect()}})},{threshold:.15});io.observe(A)}})();
/* ================= HERO BACKGROUND: the landing's rotating photos ================= */
(function(){var bg=$('.mbg');if(!bg)return;var N=[];for(var i=0;i<=30;i++)N.push(A+'img/rec/bg/'+(i<10?'0':'')+i+'.webp');
  var off=Math.floor(Math.random()*N.length),cur=0,els=[0,1].map(function(){var e=document.createElement('i');bg.insertBefore(e,bg.firstChild);return e});
  els[0].style.backgroundImage='url('+N[off]+')';els[0].classList.add('on');
  if(!RM)setInterval(function(){var nx=els[1-cur];off=(off+1)%N.length;nx.style.backgroundImage='url('+N[off]+')';var im=new Image();im.onload=function(){nx.classList.add('on');els[cur].classList.remove('on');cur=1-cur};im.src=N[off]},5200)})();
bcalc();if(ADV)load();
if(want||/[?&#]m=adv/.test(q))setTimeout(function(){toAdv(false)},60);
first=false;
})();
