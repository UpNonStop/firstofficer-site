/* calculator-modes.html: monthly. Spend by line -> points a month today vs with your desk -> what the extra points
   are worth a month (FO_REDEMPTION_BASIS, est.) against the $550 a month fee -> Return of N x and an honest verdict.
   Same data (fo-modes-data.js) and per-line math as the landing (annual / 12). Mockup only; every figure is an estimate.
   ?ex=<first name> picks an owner (default Leo). Updates on every input event; numbers tween ~200ms. */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],BS=window.FO_REDEMPTION_BASIS,$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var FEE=BS.fee/12,GATE=BS.gate,UTIL=BS.util,GMAX=80000;
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function r10(n){return Math.round(n/10)*10}
function u10(n){return usd(r10(n))}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function c2(n){return (+n).toFixed(2).replace(/0$/,'').replace(/0$/,'').replace(/\.$/,'.0')+'¢'}
function sg(n){n=r10(n);return (n<0?'−':'+')+usd(Math.abs(n))}
function nx(v){return v.toFixed(1)+'×'}
var want=((location.href.match(/[?&#]ex=([a-z]+)/i)||[])[1]||'leo').toLowerCase(),idx=0;
P.forEach(function(p,i){if(p.first.toLowerCase()===want)idx=i});
var D,S=[],mix='ex',use='mix',first=true;
/* ---- short tween: from whatever is on screen to the new value, 200ms ---- */
function tw(el,to,fmt){if(!el)return;var from=el._c==null?to:el._c;el._v=to;cancelAnimationFrame(el._r);
  if(RM||first||from===to){el._c=to;el.textContent=fmt(to);return}
  var t0=null,dur=200;
  function f(ts){if(t0==null)t0=ts;var p=Math.min(1,(ts-t0)/dur),e=1-Math.pow(1-p,3);el._c=from+(to-from)*e;el.textContent=fmt(el._c);if(p<1)el._r=requestAnimationFrame(f)}
  el._r=requestAnimationFrame(f)}
function K(n,to,fmt){$$('[data-k="'+n+'"]').forEach(function(e){tw(e,to,fmt)})}
function T(n,v){$$('[data-k="'+n+'"]').forEach(function(e){e.textContent=v})}
/* ---- example selector ---- */
$('#cex').innerHTML=P.map(function(p,i){var m=p.cats.reduce(function(a,c){return a+c[1]},0);
  return '<button type="button" role="tab" data-i="'+i+'"><b>'+p.first+'</b><small>$'+(Math.round(m*10)/10)+'K/mo</small></button>'}).join('');
$$('#cex button').forEach(function(b){b.addEventListener('click',function(){idx=+b.dataset.i;load()})});
/* ---- how you'll use the points ---- */
function rng(t){return t.floor===t.ceil?c2(t.floor):c2(t.floor).replace('¢','')+'–'+c2(t.ceil)}
$('#cuse').innerHTML=BS.types.map(function(t){return '<button type="button" role="radio" data-u="'+t.id+'" aria-checked="'+(t.id===use)+'"'+(t.id===use?' class="on"':'')+'><b>'+t.name+'</b><small>'+rng(t)+'</small></button>'}).join('');
$$('#cuse button').forEach(function(b){b.addEventListener('click',function(){use=b.dataset.u;$$('#cuse button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});calc()})});
$$('#cmix button').forEach(function(b){b.addEventListener('click',function(){mix=b.dataset.m;$$('#cmix button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});calc()})});
/* ---- spend rows: typed value + hairline slider ---- */
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
    '<div class="cer tot" role="row"><span>Total</span><span data-k="vt">–</span><span class="d" data-k="vd">–</span></div>';
}
function load(){D=P[idx];S=D.cats.map(function(c){return c[1]*1000});
  $$('#cex button').forEach(function(b,i){var on=i===idx;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});
  $('#cwho').textContent=D.first+', '+D.biz+' · fictional';
  rows();calc()}
function rateT(c){return mix==='ex'?parseFloat(c[2]):+mix}
function U(){for(var i=0;i<BS.types.length;i++)if(BS.types[i].id===use)return BS.types[i];return BS.types[0]}
function pc(v,m){return Math.max(0,Math.min(100,v/m*100))+'%'}
/* ---- the month ---- */
function calc(){var mo=0,t=0,d=0;
  D.cats.forEach(function(c,i){var a=S[i],rt=rateT(c),rd=parseFloat(c[3]);mo+=a;t+=a*rt;d+=a*rd;
    tw($('[data-et="'+i+'"]'),a*rt,pts);tw($('[data-ed="'+i+'"]'),a*rd,pts);
    var r=$$('#crows .crs')[i];r.style.setProperty('--p',Math.min(100,r.value/r.max*100)+'%');$('[data-r="'+i+'"]').textContent=x(rt)});
  /* t, d: points a month (annual / 12, same as the landing) */
  var u=U(),gain=Math.max(0,d-t)*UTIL,lo=gain*u.floor/100,hi=gain*u.ceil/100,mid=gain*u.mid/100,flat=u.floor===u.ceil;
  K('mo',mo,usd);K('bl',mo?t/mo:0,x);K('vt',t,pts);K('vd',d,pts);
  K('find',mid,function(v){return '~'+u10(v)});K('m-find',mid,function(v){return '~'+u10(v)});
  T('findr',flat?'at '+c2(u.floor)+' a point':u10(lo)+'–'+u10(hi));
  T('who',D.first+' · at '+rng(u)+' a point');
  K('net',mid-FEE,sg);T('netr',flat?'at '+c2(u.floor)+' a point, est.':sg(lo-FEE)+' to '+sg(hi-FEE)+', est.');
  K('rx',mid/FEE,nx);K('m-rx',mid/FEE,nx);T('rxr',flat?'at '+c2(u.floor)+' a point, est.':nx(lo/FEE)+' to '+nx(hi/FEE)+', est.');
  K('plus',Math.max(0,d-t),function(v){return '+'+pts(v)});
  /* balance bar: value found fills against the $550 marker; past it is pink, short of it reads as a gap */
  var bm=FEE*Math.max(3,Math.ceil(hi*1.1/FEE)),bal=$('#cbal');T('bmax',usd(bm));
  $('.base',bal).style.width=pc(Math.min(mid,FEE),bm);
  var ov=$('.over',bal);ov.style.left=pc(FEE,bm);ov.style.width=pc(Math.max(0,mid-FEE),bm);
  var sh=$('.short',bal);sh.style.left=pc(Math.min(mid,FEE),bm);sh.style.width=pc(Math.max(0,FEE-mid),bm);
  sh.setAttribute('data-t',mid<FEE?'short '+u10(FEE-mid):'');
  var rg=$('.rng',bal);rg.style.left=pc(lo,bm);rg.style.width=pc(hi-lo,bm);
  $('.mark',bal).style.left=pc(FEE,bm);
  bal.setAttribute('aria-label','Your desk finds about '+u10(mid)+' a month, est., against the $550 a month fee');
  /* fit gate */
  T('gatev','You: $'+Math.round(mo/1e3)+'K');
  var gt=$('#cgt');$('.fill',gt).style.width=pc(mo,GMAX);$('.fee',gt).style.left=pc(GATE,GMAX);gt.classList.toggle('under',mo<GATE);
  /* verdict */
  var c1=$('#cc1'),cls,t1,t2;
  if(mo<GATE){cls='no';t1='Not a fit yet.';t2='At '+usd(mo)+' a month on cards, $550 a month would cost you more than it finds. Keep the card you have, use the Freebies, and come back past ~$25K a month.'}
  else if(lo>=FEE){cls='fit';t1='Clears the fee.';t2='Even at the floor, the extra points beat $550 a month, est. Your Found Money Call checks it on your real statements.'}
  else if(hi>=FEE){cls='meh';t1='Close call.';t2='It clears at the top of the range, not the floor. Your Found Money Call settles it on your real statements, free.'}
  else{cls='no';t1='Not a fit yet.';t2='The extra points find about '+(flat?u10(lo):u10(lo)+' to '+u10(hi))+' a month, est., under the $550. Keep the card you have and use the Freebies.'}
  $('#cv').className='cv '+cls;$('.cres').className='cres '+cls;$('.cmini').className='cmini '+cls;
  $('#cvt').textContent=t1;$('#cvp').textContent=t2;
  if(cls==='no'){c1.href='freebies.html';c1.innerHTML='Get the Freebies <span class="ar">→</span>'}else{c1.href='book.html';c1.innerHTML='Book your Found Money Call <span class="ar">→</span>'}
  first=false}
load();
})();
