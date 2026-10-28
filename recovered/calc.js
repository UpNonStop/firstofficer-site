/* calculator-modes.html: two levels.
   Basic (10 seconds): one spend figure -> one blended rate -> what your desk finds a month vs the $550 fee. The slider's
   pink running fill, the live readout and the instant total are the first calculator's slider behaviour; plus a one-time
   "Watch it run" sweep ($10K -> $80K), stopped by any touch, skipped under reduced motion.
   Advanced (2 minutes): example owners, spend by line, cards today, how you'll use the points, points table.
   Same maths as the landing (annual / 12), FO_REDEMPTION_BASIS values, est. Mockup only; every figure is an estimate.
   URL: ?ex=<first name> opens Advanced on that owner; ?m=adv opens Advanced; ?spend=15000 sets Basic. */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],BS=window.FO_REDEMPTION_BASIS,$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var FEE=BS.fee/12,GATE=BS.gate,UTIL=BS.util,GMAX=80000,BT=1.2,BD=3.4;
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var PH='https://cdn.jsdelivr.net/gh/UpNonStop/firstofficer-site@696503d9ba166267a9a219c98b98bcf4c09d74c1/';
var IND={'Insurance agency':'rebuild-mockups/img/ind/cpa-firms.jpg','HVAC':'rebuild-mockups/img/ind/hvac.jpg','Dental practice':'rebuild-v2/img/ph/i-dental2.webp',
  'Marketing agency':'rebuild-mockups/img/ind/agencies.jpg','Law firm':'rebuild-mockups/img/ind/law-firms.jpg','Restaurant':'rebuild-mockups/img/ind/restaurants.jpg',
  'Trucking':'rebuild-mockups/img/ind/trucking.jpg','Real estate':'rebuild-mockups/img/ind/real-estate.jpg','E-commerce':'rebuild-mockups/img/ind/ecommerce.jpg','Contractor':'rebuild-mockups/img/ind/contractors.jpg'};
var TIER=[PH+'rebuild-mockups/img/ind/desk.jpg',PH+'rebuild-v2/img/ph/e-window.webp',PH+'rebuild-v2/img/ph/e-seat.webp',A+'img/rec/bg/09.webp'];
var TALT=['A notebook and pen on a clean desk','Golden-hour light through an aircraft window','Wide leather seats in a premium cabin','An overwater villa on a turquoise lagoon'];
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function r10(n){return Math.round(n/10)*10}
function u10(n){return usd(r10(n))}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function c2(n){return (+n).toFixed(2).replace(/0$/,'').replace(/0$/,'').replace(/\.$/,'.0')+'¢'}
function sg(n){n=r10(n);return (n<0?'−':'+')+usd(Math.abs(n))}
function nx(v){return v.toFixed(1)+'×'}
function rng(t){return t.floor===t.ceil?c2(t.floor):c2(t.floor).replace('¢','')+'–'+c2(t.ceil)}
var q=location.href,want=((q.match(/[?&#]ex=([a-z]+)/i)||[])[1]||'').toLowerCase(),idx=0;
P.forEach(function(p,i){if(p.first.toLowerCase()===want)idx=i});
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
  if(r.mo<GATE)return {c:'no',t:'Not a fit yet.',p:'At '+usd(r.mo)+' a month on cards, $550 a month would cost you more than it finds. Keep the card you have, use the Freebies, and come back past ~$25K a month.'};
  if(r.lo>=FEE)return {c:'fit',t:'Clears the fee.',p:'Even at the floor, the extra points beat $550 a month, est. Your Found Money Call checks it on your real statements.'};
  if(r.hi>=FEE)return {c:'meh',t:'Close call.',p:'It clears at the top of the range, not the floor. Your Found Money Call settles it on your real statements, free.'};
  return {c:'no',t:'Not a fit yet.',p:'The extra points find about '+(f?u10(r.lo):u10(r.lo)+' to '+u10(r.hi))+' a month, est., under the $550. Keep the card you have and use the Freebies.'}}
function cta(el,v){if(v.c==='no'){el.href='freebies.html';el.innerHTML='Get the Freebies <span class="ar">→</span>'}else{el.href='book.html';el.innerHTML='Book your Found Money Call <span class="ar">→</span>'}}
/* balance bar: value found fills against the $550 marker; past it is pink, short of it reads as a gap */
function bar(bal,r){var bm=FEE*Math.max(3,Math.ceil(r.hi*1.1/FEE)),mid=r.mid;T(bal,'bmax',usd(bm));
  $('.base',bal).style.width=pc(Math.min(mid,FEE),bm);
  var ov=$('.over',bal);ov.style.left=pc(FEE,bm);ov.style.width=pc(Math.max(0,mid-FEE),bm);
  var sh=$('.short',bal);sh.style.left=pc(Math.min(mid,FEE),bm);sh.style.width=pc(Math.max(0,FEE-mid),bm);
  sh.setAttribute('data-t',mid<FEE?'short '+u10(FEE-mid):'');
  var rg=$('.rng',bal);rg.style.left=pc(r.lo,bm);rg.style.width=pc(r.hi-r.lo,bm);
  $('.mark',bal).style.left=pc(FEE,bm);
  bal.setAttribute('aria-label','Your desk finds about '+u10(mid)+' a month, est., against the $550 a month fee')}
/* photo that answers the result: the tier the month reaches, never a list of redemptions */
function tierInit(fig){$('.ctp',fig).innerHTML=TIER.map(function(s,i){return '<img src="'+s+'" alt="'+TALT[i]+'" loading="'+(i<2?'eager':'lazy')+'" data-t="'+i+'">'}).join('')}
function tier(fig,r,v){var rx=r.mid/FEE,i=v.c==='no'?0:rx<2?1:rx<3?2:3;
  if(fig._t!==i){$$('img',fig).forEach(function(m){m.classList.toggle('on',+m.dataset.t===i)});fig._t=i}
  T(fig,'tier',i===0?'Not yet':i===1?(v.c==='meh'?'Close to paying for itself':'Pays for itself'):i===2?'Twice the fee, est.':'Three times the fee and up');
  T(fig,'tierx','Return '+nx(rx)+', est.'+(i===0?' Keep your card; use the Freebies.':''));
  fig.className='ctier t'+i}
function paint(R,r){
  K(R,'find',r.mid,function(v){return '~'+u10(v)});K(R,'m-find',r.mid,function(v){return '~'+u10(v)});
  T(R,'findr',r.flat?'at '+c2(r.u.floor)+' a point':u10(r.lo)+'–'+u10(r.hi));
  K(R,'net',r.mid-FEE,sg);T(R,'netr',r.flat?'at '+c2(r.u.floor)+' a point, est.':sg(r.lo-FEE)+' to '+sg(r.hi-FEE)+', est.');
  K(R,'rx',r.mid/FEE,nx);K(R,'m-rx',r.mid/FEE,nx);T(R,'rxr',r.flat?'at '+c2(r.u.floor)+' a point, est.':nx(r.lo/FEE)+' to '+nx(r.hi/FEE)+', est.');
  K(R,'plus',Math.max(0,r.d-r.t),function(v){return '+'+pts(v)})}
/* ================= BASIC ================= */
var BAS=$('#bas'),bv=$('#bv'),bs=$('#bs'),B=35000,bt=$('#btier');tierInit(bt);
var sp=(q.match(/[?&#]spend=(\d+)/)||[])[1];if(sp)B=Math.min(2e6,+sp);
function fill(s){s.style.setProperty('--p',Math.min(100,s.value/s.max*100)+'%')}
function bcalc(){var r=month([[B,BT,BD]],'mix'),v=verdict(r);
  bv.value=B.toLocaleString('en-US');if(document.activeElement!==bv){}
  if(+bs.value!==B&&B<=+bs.max)bs.value=B;if(B>+bs.max)bs.value=bs.max;fill(bs);
  paint(BAS,r);bar($('#bbal'),r);tier(bt,r,v);
  BAS.className='cbas '+v.c;$('#bvt').textContent=v.t;$('#bvp').textContent=v.p;cta($('#bc1'),v)}
bs.addEventListener('input',function(){B=+bs.value;bcalc()});
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
var ADV=$('#adv'),at=$('#atier');tierInit(at);
$('#cex').innerHTML=P.map(function(p,i){var m=p.cats.reduce(function(a,c){return a+c[1]},0);
  return '<button type="button" role="tab" data-i="'+i+'"><b>'+p.first+'</b><small>$'+(Math.round(m*10)/10)+'K/mo</small></button>'}).join('');
$$('#cex button').forEach(function(b){b.addEventListener('click',function(){idx=+b.dataset.i;load()})});
$('.cip').innerHTML=P.map(function(p,i){var s=IND[p.ind]||'rebuild-mockups/img/ind/desk.jpg';return '<img src="'+PH+s+'" alt="'+p.ind+' at work" loading="lazy" data-i="'+i+'">'}).join('');
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
function load(){D=P[idx];S=D.cats.map(function(c){return c[1]*1000});
  $$('#cex button').forEach(function(b,i){var on=i===idx;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});
  $$('.cip img').forEach(function(m){var on=+m.dataset.i===idx;m.classList.toggle('on',on);if(on)m.loading='eager'});
  $('#cinb').textContent=D.first;$('#cins').textContent=D.biz+' · '+D.ind+' · fictional';
  $('#cwho').textContent='Ten fictional owners';
  rows();calc()}
function rateT(c){return mix==='ex'?parseFloat(c[2]):+mix}
function calc(){var L=D.cats.map(function(c,i){return [S[i],rateT(c),parseFloat(c[3])]}),r=month(L,use),v=verdict(r);
  L.forEach(function(l,i){tw($('[data-et="'+i+'"]'),l[0]*l[1],pts);tw($('[data-ed="'+i+'"]'),l[0]*l[2],pts);
    var s=$$('#crows .crs')[i];fill(s);$('[data-r="'+i+'"]').textContent=x(l[1])});
  K(ADV,'mo',r.mo,usd);K(ADV,'bl',r.mo?r.t/r.mo:0,x);K(ADV,'vt',r.t,pts);K(ADV,'vd',r.d,pts);
  T(ADV,'who',D.first+' · at '+rng(r.u)+' a point');
  paint(ADV,r);bar($('#cbal'),r);tier(at,r,v);
  T(ADV,'gatev','You: $'+Math.round(r.mo/1e3)+'K');
  var gt=$('#cgt');$('.fill',gt).style.width=pc(r.mo,GMAX);$('.fee',gt).style.left=pc(GATE,GMAX);gt.classList.toggle('under',r.mo<GATE);
  $('#cv').className='cv '+v.c;$('.cres').className='cres '+v.c;$('.cmini').className='cmini '+v.c;
  $('#cvt').textContent=v.t;$('#cvp').textContent=v.p;cta($('#cc1'),v)}
/* ================= LEVEL SWITCH ================= */
function mode(m,scroll){var a=m==='a';stop();
  $$('.cmode button').forEach(function(b){var on=b.dataset.m===m;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});
  BAS.hidden=a;ADV.hidden=!a;document.body.classList.toggle('adv',a);
  if(scroll){var y=$('.cmode').getBoundingClientRect().top+scrollY-90;if(Math.abs(scrollY-y)>40)scrollTo({top:y,behavior:RM?'auto':'smooth'})}}
$$('.cmode button').forEach(function(b){b.addEventListener('click',function(){mode(b.dataset.m,false)})});
$('#bgo').addEventListener('click',function(){mode('a',true)});
bcalc();load();
mode(want||/[?&#]m=adv/.test(q)?'a':'b',false);
first=false;
})();
