/* calculator-modes.html: standalone editorial calculator. Same data (fo-modes-data.js) and the same per-line math
   the landing uses, so every example owner lands on the landing's today -> with-desk figures.
   Mockup only; every figure is an estimate. ?ex=<first name> picks an example owner (default Leo). */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var FEE=6600,GATE=25000,UTIL=.85,LO=.01,HI=.016,GMAX=80000;
var EX=[['Paris for two','Business class, round trip',280000,'img/fo-paris.jpg'],['A week at a top hotel','Seven nights, points only',175000,'img/hotel.jpg'],['The Maldives','Business for two, plus five nights',300000,'img/fo-maldives.jpg']];
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function kusd(n){return n>=1e3?'$'+(n/1e3).toFixed(1).replace(/\.0$/,'')+'k':usd(n)}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function k(n,v,html){$$('[data-k="'+n+'"]').forEach(function(e){if(html)e.innerHTML=v;else e.textContent=v})}
var want=((location.href.match(/[?&#]ex=([a-z]+)/i)||[])[1]||'leo').toLowerCase(),idx=0;
P.forEach(function(p,i){if(p.first.toLowerCase()===want)idx=i});
var D,S=[],mix='ex';
/* ---- example selector: compact text tabs ---- */
$('#cex').innerHTML=P.map(function(p,i){var m=p.cats.reduce(function(a,c){return a+c[1]},0);
  return '<button type="button" role="tab" data-i="'+i+'"><b>'+p.first+'</b><span>'+p.ind+'</span><small>$'+(Math.round(m*10)/10)+'K/mo</small></button>'}).join('');
$$('#cex button').forEach(function(b){b.addEventListener('click',function(){idx=+b.dataset.i;load()})});
/* ---- spend rows: typed value + hairline slider ---- */
function rows(){var p=D;
  $('#crows').innerHTML=p.cats.map(function(c,i){var mx=Math.max(20,Math.ceil(c[1]*3/5)*5)*1000;
    return '<div class="crow"><div class="crl"><label for="cv'+i+'">'+c[0]+'</label><span class="crt"><s data-r="'+i+'">'+c[2]+'</s><i aria-hidden="true">→</i><b>'+c[3]+'</b></span></div>'+
    '<div class="cri"><span>$</span><input id="cv'+i+'" type="text" inputmode="numeric" autocomplete="off" value="'+(c[1]*1000).toLocaleString('en-US')+'" aria-label="'+c[0]+', dollars a month"><small>a month</small></div>'+
    '<div class="crp"><span>Today <b data-t="'+i+'"></b></span><span>Desk <b data-d="'+i+'"></b></span></div>'+
    '<input class="crs" type="range" min="0" max="'+mx+'" step="100" value="'+c[1]*1000+'" aria-label="'+c[0]+', slider" tabindex="-1"></div>'}).join('');
  $$('#crows .crow').forEach(function(r,i){var t=$('input[type=text]',r),s=$('.crs',r);
    s.addEventListener('input',function(){S[i]=+s.value;t.value=S[i].toLocaleString('en-US');calc()});
    t.addEventListener('input',function(){var v=Math.min(2e6,+(t.value.replace(/[^0-9]/g,''))||0);S[i]=v;if(v>+s.max)s.max=Math.ceil(v/5000)*5000;s.value=v;calc()});
    t.addEventListener('blur',function(){t.value=S[i].toLocaleString('en-US')});
    t.addEventListener('focus',function(){t.select()})});
}
function load(){D=P[idx];S=D.cats.map(function(c){return c[1]*1000});
  $$('#cex button').forEach(function(b,i){var on=i===idx;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});
  $('#cwho').textContent='Example: '+D.first+', '+D.biz+'. Fictional.';
  rows();calc()}
function rateT(c){return mix==='ex'?parseFloat(c[2]):+mix}
/* ---- the math: per line, a year (same as the landing's figures) ---- */
var R={};
function calc(){var p=D,mo=0,t=0,d=0;
  p.cats.forEach(function(c,i){var a=S[i],rt=rateT(c),rd=parseFloat(c[3]);mo+=a;t+=a*12*rt;d+=a*12*rd;
    var r=$$('#crows .crs')[i];r.style.setProperty('--p',Math.min(100,r.value/r.max*100)+'%');
    $('[data-t="'+i+'"]').textContent=pts(a*12*rt);$('[data-d="'+i+'"]').textContent=pts(a*12*rd);
    $('[data-r="'+i+'"]').textContent=x(rt)});
  var G=p.cats.map(function(c,i){return {n:c[0],g:Math.max(0,S[i]*12*(parseFloat(c[3])-rateT(c)))}}),gs=G.reduce(function(a,b){return a+b.g},0),gm=Math.max.apply(null,G.map(function(o){return o.g}))||1;
  $('#cgap').innerHTML=G.map(function(o){return '<div class="cgr"><span>'+o.n+'</span><u><i style="width:'+(o.g/gm*100)+'%"></i></u><b>+'+pts(o.g)+'</b><em>'+(gs?Math.round(o.g/gs*100):0)+'%</em></div>'}).join('');
  R={mo:mo,t:t,d:d};var gain=Math.max(0,d-t)*UTIL,lo=gain*LO,hi=gain*HI;
  $('#ctot').textContent=usd(mo);$('#ctoty').textContent='$'+Math.round(mo*12/1e3)+'k';$('#cbl').textContent=x(mo?Math.round(t/mo/12*100)/100:0);
  k('today',pts(t));k('desk',pts(d));k('plus','+'+pts(Math.max(0,d-t)));
  k('range',kusd(lo)+'–'+kusd(hi));k('gatev','You: $'+Math.round(mo/1e3)+'K');
  function sg(n){return (n<0?'−':'+')+kusd(Math.abs(n))}
  k('net',sg(lo-FEE)+' to '+sg(hi-FEE));
  $('#cbT').style.width=(d?Math.round(t/d*100):0)+'%';$('#cbD').style.width=d?'100%':'0';
  /* value range vs fee scale */
  var mx=Math.max(hi,FEE)*1.2,vs=$('#cvs');
  $('.band',vs).style.left=(lo/mx*100)+'%';$('.band',vs).style.width=Math.max(.8,(hi-lo)/mx*100)+'%';
  $('.fee',vs).style.left=(FEE/mx*100)+'%';$('.feel',vs).style.left=(FEE/mx*100)+'%';
  var gt=$('#cgt');$('.fill',gt).style.width=Math.min(100,mo/GMAX*100)+'%';$('.fee',gt).style.left=(GATE/GMAX*100)+'%';$('.feel',gt).style.left=(GATE/GMAX*100)+'%';gt.classList.toggle('under',mo<GATE);
  var v=$('#cv'),c1=$('#cc1'),cls,t1,t2,sh;
  if(mo<GATE){cls='no';t1='Not a fit yet. Here is what to do instead.';sh='Under';t2='At '+usd(mo)+' a month on cards, $550 a month would cost you more than it finds.'}
  else if(lo>=FEE){cls='fit';t1='Clears the fee.';sh='Clears';t2='Even the low end beats the $6,600 a year, est. Your Found Money Call checks it on your real statements.'}
  else if(hi>=FEE){cls='meh';t1='Close call.';sh='Top end only';t2='It clears at the top of the range, not the bottom. Your Found Money Call settles it on your real statements, free.'}
  else{cls='no';t1='Not a fit yet. Here is what to do instead.';sh='Under';t2='The extra points are worth about '+kusd(lo)+' to '+kusd(hi)+' a year, est., under the $6,600.'}
  v.className='cv '+cls;$('#cvt').textContent=t1;$('#cvp').textContent=t2;k('vsh',sh);
  var L3=cls==='no'?['Keep the card you have. It is doing an honest job at this spend.','Use the <a href="freebies.html">Freebies</a>. Free guides, no desk needed.','Come back when you pass ~$25K a month on cards.']:cls==='meh'?['Book your Found Money Call. 20 minutes, free.','Your desk checks the range on your real statements.','If it does not clear, you will hear that on the call.']:['Book your Found Money Call. 20 minutes, free.','Your desk checks the numbers on your real statements.','Every move waits for your OK before it happens.'];
  $('#cvo').innerHTML=L3.map(function(t,i){return '<li><b>0'+(i+1)+'</b><span>'+t+'</span></li>'}).join('');
  if(cls==='no'){c1.href='freebies.html';c1.innerHTML='Get the Freebies <span class="ar">→</span>'}else{c1.href='book.html';c1.innerHTML='Book your Found Money Call <span class="ar">→</span>'}
  trips();
}
/* ---- Burn: what a year of points with your desk buys ---- */
function trips(){var use=R.d*UTIL,p=D,L=[[p.trip,p.when+' · your example goal',p.need,p.img,1]].concat(EX);
  $('#ctrips').innerHTML=L.map(function(e){var n=use/e[2];
    return '<article class="ctr"><div class="cti" style="background-image:url('+A+e[3]+')">'+(e[4]?'<span>'+p.first+'\u2019s goal</span>':'')+'</div><div class="ctb"><small>~'+pts(e[2])+' points, est.</small><h3>'+e[0]+'</h3><p>'+e[1]+'</p>'+
    '<div class="ctx"><b>'+(n>=1?(Math.floor(n*10)/10).toFixed(1).replace(/\.0$/,'')+'×':Math.round(n*100)+'%')+'</b><span>'+(n>=1?'a year with your desk, est.':'of the way in a year with your desk, est.')+'</span></div></div></article>'}).join('')}
$$('#cmix button').forEach(function(b){b.addEventListener('click',function(){mix=b.dataset.m;$$('#cmix button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});calc()})});
load();
})();
