/* calculator-modes.html: a live chain. Spend -> Earn (velocity, 12-month accrual) -> Timeline (milestones)
   -> Burn (cents a point by redemption type, FO_REDEMPTION_BASIS) -> Return (N x on the $6,600 fee).
   Same data (fo-modes-data.js) and per-line math as the landing, so every example owner lands on the landing's
   today -> with-desk points. Mockup only; every figure is an estimate. ?ex=<first name> picks an owner (default Leo). */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],BS=window.FO_REDEMPTION_BASIS,$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var FEE=BS.fee,GATE=BS.gate,UTIL=BS.util,GMAX=80000;
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var EX=[['A week at a top hotel','Seven nights, points only',175000,'img/hotel.jpg'],['Paris for two','Business class, round trip',280000,'img/fo-paris.jpg'],['The Maldives','Business for two, plus five nights',300000,'img/fo-maldives.jpg']];
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function kusd(n){n=Math.abs(n);return n>=1e3?'$'+(n/1e3).toFixed(1).replace(/\.0$/,'')+'k':usd(n)}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function c2(n){return (+n).toFixed(2).replace(/0$/,'')+'¢'}
function sg(n){return (n<0?'−':'+')+kusd(n)}
var want=((location.href.match(/[?&#]ex=([a-z]+)/i)||[])[1]||'leo').toLowerCase(),idx=0;
P.forEach(function(p,i){if(p.first.toLowerCase()===want)idx=i});
var D,S=[],mix='ex',use='mix',unit='pts',first=true;
/* ---- tweening: every number counts to its new value; stages are staggered down the chain ---- */
function tw(el,to,fmt,delay){if(!el)return;var from=el._v==null?to:el._v;el._v=to;
  if(RM||first||from===to){el.textContent=fmt(to);return}
  var t0=null,dur=650;cancelAnimationFrame(el._r);
  function f(ts){if(t0==null)t0=ts+(delay||0);var p=Math.max(0,Math.min(1,(ts-t0)/dur)),e=1-Math.pow(1-p,3);el.textContent=fmt(from+(to-from)*e);if(p<1)el._r=requestAnimationFrame(f)}
  el._r=requestAnimationFrame(f)}
function K(n,to,fmt,delay){$$('[data-k="'+n+'"]').forEach(function(e){tw(e,to,fmt,delay)})}
function T(n,v){$$('[data-k="'+n+'"]').forEach(function(e){e.textContent=v})}
function pulse(stage,delay){if(RM||first)return;var li=$('.crail .s'+stage);if(!li)return;setTimeout(function(){li.classList.remove('go');void li.offsetWidth;li.classList.add('go')},delay)}
var ST=[0,110,220,330,440];
/* ---- example selector ---- */
$('#cex').innerHTML=P.map(function(p,i){var m=p.cats.reduce(function(a,c){return a+c[1]},0);
  return '<button type="button" role="tab" data-i="'+i+'"><b>'+p.first+'</b><small>$'+(Math.round(m*10)/10)+'K/mo</small></button>'}).join('');
$$('#cex button').forEach(function(b){b.addEventListener('click',function(){idx=+b.dataset.i;load()})});
/* ---- redemption types ---- */
$('#cuse').innerHTML=BS.types.map(function(t){return '<button type="button" role="radio" data-u="'+t.id+'" aria-checked="'+(t.id===use)+'"'+(t.id===use?' class="on"':'')+'><b>'+t.short+'</b><small>'+(t.floor===t.ceil?t.floor.toFixed(1)+'¢':t.floor.toFixed(1)+'–'+t.ceil.toFixed(1)+'¢')+'</small></button>'}).join('');
var AX0=.5,AX1=2.5;function ax(c){return (c-AX0)/(AX1-AX0)*100}
$('#cbasis').innerHTML='<div class="cbh" role="row"><span>Redemption</span><span class="cbsc"><i style="left:'+ax(1)+'%">1¢</i><i style="left:'+ax(1.5)+'%">1.5¢</i><i style="left:'+ax(2)+'%">2¢</i></span><span>Cents a point</span><span>Extra points worth</span></div>'+
  BS.types.map(function(t){return '<div class="cbr" role="row" data-u="'+t.id+'"><span><b>'+t.name+'</b><small>'+t.note+'</small></span><span class="cbsc"><u style="left:'+ax(t.floor)+'%;width:'+Math.max(.9,ax(t.ceil)-ax(t.floor))+'%"></u><s style="left:'+ax(t.mid)+'%"></s></span><span class="cbv">'+(t.floor===t.ceil?c2(t.floor):c2(t.floor)+'–'+c2(t.ceil))+'</span><span class="cbw" data-w="'+t.id+'">–</span></div>'}).join('');
function setUse(id){use=id;$$('#cuse button').forEach(function(o){var on=o.dataset.u===id;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});$$('#cbasis .cbr').forEach(function(r){r.classList.toggle('on',r.dataset.u===id)});calc()}
$$('#cuse button').forEach(function(b){b.addEventListener('click',function(){setUse(b.dataset.u)})});
$$('#cbasis .cbr').forEach(function(r){r.addEventListener('click',function(){setUse(r.dataset.u)})});
$$('#cunit button').forEach(function(b){b.addEventListener('click',function(){unit=b.dataset.u;$$('#cunit button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});chart(true)})});
/* ---- spend rows: typed value + hairline slider ---- */
function rows(){var p=D;
  $('#crows').innerHTML=p.cats.map(function(c,i){var mx=Math.max(20,Math.ceil(c[1]*3/5)*5)*1000;
    return '<div class="crow"><label for="cv'+i+'">'+c[0]+'</label>'+
    '<div class="cri"><span>$</span><input id="cv'+i+'" type="text" inputmode="numeric" autocomplete="off" value="'+(c[1]*1000).toLocaleString('en-US')+'" aria-label="'+c[0]+', dollars a month"></div>'+
    '<input class="crs" type="range" min="0" max="'+mx+'" step="100" value="'+c[1]*1000+'" aria-label="'+c[0]+', slider"></div>'}).join('');
  $$('#crows .crow').forEach(function(r,i){var t=$('input[type=text]',r),s=$('.crs',r);
    s.addEventListener('input',function(){S[i]=+s.value;t.value=S[i].toLocaleString('en-US');calc()});
    t.addEventListener('input',function(){var v=Math.min(2e6,+(t.value.replace(/[^0-9]/g,''))||0);S[i]=v;if(v>+s.max)s.max=Math.ceil(v/5000)*5000;s.value=v;calc()});
    t.addEventListener('blur',function(){t.value=S[i].toLocaleString('en-US')});
    t.addEventListener('focus',function(){t.select()})});
  $('#cet').innerHTML='<div class="ceh" role="row"><span>Line</span><span>Per $1</span><span>Today</span><span>Desk</span><span>Points a month, today vs desk</span></div>'+
    p.cats.map(function(c,i){return '<div class="cer" role="row"><span>'+c[0]+'</span><span class="cxr"><s data-r="'+i+'">'+c[2]+'</s> → <b>'+c[3]+'</b></span><span data-et="'+i+'">–</span><span class="d" data-ed="'+i+'">–</span><span class="cbar"><u><i data-eb="'+i+'"></i><em data-ebt="'+i+'"></em></u></span></div>'}).join('');
}
function load(){D=P[idx];S=D.cats.map(function(c){return c[1]*1000});
  $$('#cex button').forEach(function(b,i){var on=i===idx;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});
  $('#cwho').textContent=D.first+', '+D.biz+' · fictional';
  rows();calc()}
function rateT(c){return mix==='ex'?parseFloat(c[2]):+mix}
function U(){for(var i=0;i<BS.types.length;i++)if(BS.types[i].id===use)return BS.types[i];return BS.types[0]}
/* ---- the chain ---- */
var R={};
function calc(){var p=D,mo=0,t=0,d=0,L=[];
  p.cats.forEach(function(c,i){var a=S[i],rt=rateT(c),rd=parseFloat(c[3]);mo+=a;t+=a*12*rt;d+=a*12*rd;L.push([a*rt,a*rd]);
    var r=$$('#crows .crs')[i];r.style.setProperty('--p',Math.min(100,r.value/r.max*100)+'%');$('[data-r="'+i+'"]').textContent=x(rt)});
  var u=U(),gain=Math.max(0,d-t)*UTIL,lo=gain*u.floor/100,hi=gain*u.ceil/100,mid=gain*u.mid/100;
  R={mo:mo,t:t,d:d,gain:gain,lo:lo,hi:hi,mid:mid,u:u};
  /* 01 spend */
  K('mo',mo,usd,ST[0]);K('yr',mo*12,function(v){return '$'+Math.round(v/1e3)+'k'},ST[0]);K('bl',mo?t/mo/12:0,x,ST[0]);
  K('r-spend',mo,usd,ST[0]);pulse(0,ST[0]);
  /* 02 earn */
  var mx=Math.max.apply(null,L.map(function(l){return l[1]}))||1;
  L.forEach(function(l,i){tw($('[data-et="'+i+'"]'),l[0],pts,ST[1]);tw($('[data-ed="'+i+'"]'),l[1],pts,ST[1]);
    $('[data-eb="'+i+'"]').style.width=(l[1]/mx*100)+'%';$('[data-ebt="'+i+'"]').style.width=(l[0]/mx*100)+'%'});
  K('vt',t/12,pts,ST[1]);K('vd',d/12,pts,ST[1]);K('vx',t?d/t:0,function(v){return v.toFixed(1)+'×'},ST[1]);
  K('r-vel',d/12,pts,ST[1]);T('r-vel-s','points a month with your desk, vs '+pts(t/12)+' today');pulse(1,ST[1]);
  /* 03 timeline */
  chart(false);pulse(2,ST[2]);
  /* 04 burn */
  BS.types.forEach(function(ty){var w=$('[data-w="'+ty.id+'"]');var a=gain*ty.floor/100,b=gain*ty.ceil/100;w.textContent=ty.floor===ty.ceil?kusd(a):kusd(a)+'–'+kusd(b)});
  $$('#cbasis .cbr').forEach(function(r){r.classList.toggle('on',r.dataset.u===use)});
  var tr=trips(),ct=$('#ctr'),tk=tr.map(function(g){return g[0]}).join('|');
  if(ct.dataset.k!==tk){ct.dataset.k=tk;ct.innerHTML=tr.map(function(g,i){return '<div class="ctx'+(g[4]?' goal':'')+'"><i style="background-image:url('+A+g[3]+')"></i><span><b>'+g[0]+'</b><small>'+pts(g[2])+' points, est.</small></span><strong data-tr="'+i+'">0×</strong></div>'}).join('')}
  tr.forEach(function(g,i){tw($('[data-tr="'+i+'"]'),gain/g[2],function(v){return v.toFixed(1)+'×'},ST[3])});
  T('r-cpp',u.floor===u.ceil?c2(u.floor):c2(u.floor)+'–'+c2(u.ceil));T('r-cpp-s','a point, '+u.short.toLowerCase()+', est.');pulse(3,ST[3]);
  /* 05 return */
  var rx=mid/FEE;K('rx',rx,function(v){return v.toFixed(1)+'×'},ST[4]);K('r-ret',rx,function(v){return v.toFixed(1)+'×'},ST[4]);
  T('rxr',u.floor===u.ceil?'at '+c2(u.floor)+' a point, est.':(lo/FEE).toFixed(1)+'× to '+(hi/FEE).toFixed(1)+'× est.');
  K('plus',Math.max(0,d-t),function(v){return '+'+pts(v)},ST[4]);
  T('rangel','Worth, est. at '+(u.floor===u.ceil?c2(u.floor):c2(u.floor)+' to '+c2(u.ceil)));
  T('range',u.floor===u.ceil?kusd(lo):kusd(lo)+'–'+kusd(hi));
  T('net',u.floor===u.ceil?sg(lo-FEE):sg(lo-FEE)+' to '+sg(hi-FEE));
  T('gatev','You: $'+Math.round(mo/1e3)+'K');
  var gt=$('#cgt');$('.fill',gt).style.width=Math.min(100,mo/GMAX*100)+'%';$('.fee',gt).style.left=(GATE/GMAX*100)+'%';gt.classList.toggle('under',mo<GATE);
  var v=$('#cv'),c1=$('#cc1'),cls,t1,t2;
  if(mo<GATE){cls='no';t1='Not a fit yet. Here is what to do instead.';t2='At '+usd(mo)+' a month on cards, $550 a month would cost you more than it finds.'}
  else if(lo>=FEE){cls='fit';t1='Clears the fee.';t2='Even at the floor, the extra points beat the $6,600 a year, est. Your Found Money Call checks it on your real statements.'}
  else if(hi>=FEE){cls='meh';t1='Close call.';t2='It clears at the top of the range, not the floor. Your Found Money Call settles it on your real statements, free.'}
  else{cls='no';t1='Not a fit yet. Here is what to do instead.';t2='The extra points are worth about '+(lo===hi?kusd(lo):kusd(lo)+' to '+kusd(hi))+' a year, est., under the $6,600.'}
  v.className='cv '+cls;$('.cret').classList.toggle('no',cls==='no');$('.crail .s4').className='s4 '+cls+($('.crail .s4').classList.contains('go')?' go':'');
  $('#cvt').textContent=t1;$('#cvp').textContent=t2;T('r-ret-s',cls==='fit'?'on the $6,600 fee · clears':cls==='meh'?'on the $6,600 fee · close call':'on the $6,600 fee · not a fit yet');pulse(4,ST[4]);
  var L3=cls==='no'?['Keep the card you have. It is doing an honest job at this spend.','Use the <a href="freebies.html">Freebies</a>. Free guides, no desk needed.','Come back when you pass ~$25K a month on cards.']:cls==='meh'?['Book your Found Money Call. 20 minutes, free.','Your desk checks the range on your real statements.','If it does not clear, you will hear that on the call.']:['Book your Found Money Call. 20 minutes, free.','Your desk checks the numbers on your real statements.','Every move waits for your OK before it happens.'];
  $('#cvo').innerHTML=L3.map(function(t,i){return '<li><b>0'+(i+1)+'</b><span>'+t+'</span></li>'}).join('');
  if(cls==='no'){c1.href='freebies.html';c1.innerHTML='Get the Freebies <span class="ar">→</span>'}else{c1.href='book.html';c1.innerHTML='Book your Found Money Call <span class="ar">→</span>'}
  first=false}
/* ---- 12-month accrual chart (monthly steps, like statements) + milestones ---- */
var CH={},NS='http://www.w3.org/2000/svg';
function trips(){var g=[[D.trip,D.when+' · your example goal',D.need,D.img,1]].concat(EX.map(function(e){return [e[0],e[1],e[2],e[3],0]}));return g.sort(function(a,b){return a[2]-b[2]})}
function mon(need,rate){if(rate<=0)return 99;return Math.ceil(need/rate-1e-9)}
function chart(unitOnly){var mt=R.t/12,md=R.d/12,u=R.u,cpp=u.mid/100,TP=trips(),goal=D.need;
  function cv(p){return unit==='usd'?p*UTIL*cpp:unit==='trip'?p/goal:p}
  function fm(v){return unit==='usd'?kusd(v):unit==='trip'?(Math.round(v*10)/10)+(v>=1.95||v<.05?' trips':' trip'):pts(v)}
  var tA=[],dA=[];for(var m=0;m<=12;m++){tA.push(cv(mt*m));dA.push(cv(md*m))}
  var prev=CH.d&&CH.unit===unit?{t:CH.t,d:CH.d,ymax:CH.ymax}:null;
  /* y scale: nice max */
  var top=dA[12]||1,mag=Math.pow(10,Math.floor(Math.log10(top))),ymax=Math.ceil(top/mag*1.08*2)/2*mag;if(ymax<=0)ymax=1;
  CH.unit=unit;CH.t=tA;CH.d=dA;CH.ymax=ymax;
  /* milestones */
  var ms=TP.map(function(tp){return {n:tp[0],sub:tp[1],need:tp[2],img:tp[3],own:tp[4],md:mon(tp[2],md),mt:mon(tp[2],mt)}});
  var mg=(md-mt)*UTIL*cpp,fm2=mg>0?mon(FEE,mg):99;
  var fst=ms.filter(function(o){return o.md<=12})[0];
  T('r-first',fst?'Month '+fst.md:'12+ months');T('r-first-s',fst?fst.n.replace(/^A week at a /,'a week at a ').replace(/^The /,'the ')+', est.':'to your first example trip');
  $('#cms').innerHTML=ms.map(function(o,i){return '<li'+(o.md>12?' class="far"':'')+'><span class="cmn">'+(i+1)+'</span><span class="cmi" style="background-image:url('+A+o.img+')"></span><span class="cmt"><b>'+(o.md>12?'Beyond 12 months':'Month '+o.md)+'</b><small>'+(o.mt>12?'Today: beyond 12 months':'Today: month '+o.mt)+'</small></span><span class="cmd"><b>'+o.n+(o.own?' <em>'+D.first+'\'s goal</em>':'')+'</b><small>'+pts(o.need)+' points, est. · '+o.sub+'</small></span></li>'}).join('')+
    '<li class="fee'+(fm2>12?' far':'')+'"><span class="cmn">$</span><span class="cmi none"></span><span class="cmt"><b>'+(fm2>12?'Beyond 12 months':'Month '+fm2)+'</b><small>at '+c2(u.mid)+' a point, est.</small></span><span class="cmd"><b>The extra points cover the $6,600 fee</b><small>Your desk pays for itself from here, est.</small></span></li>';
  draw(prev,ms,fm2,fm,unitOnly)}
function draw(prev,ms,fm2,fm,instant){var svg=$('#csvg'),W=svg.parentNode.clientWidth||600,H=W<500?210:250,pl=W<500?40:54,pr=12,pt=14,pb=26;
  svg.setAttribute('viewBox','0 0 '+W+' '+H);svg.setAttribute('width',W);svg.setAttribute('height',H);
  var tA=CH.t,dA=CH.d,ym=CH.ymax;
  function X(m){return pl+(W-pl-pr)*m/12}
  function build(t,d,y){function Y(v){return pt+(H-pt-pb)*(1-v/y)}
    function step(a){var s='M'+X(0)+','+Y(a[0]);for(var m=1;m<=12;m++)s+='H'+X(m)+'V'+Y(a[m]);return s}
    var gap=step(d)+'V'+Y(t[12]);for(var m=12;m>=1;m--)gap+='V'+Y(t[m])+'H'+X(m-1);gap+='Z';
    return {Y:Y,t:step(t),d:step(d),g:gap}}
  var g='';var b0=build(tA,dA,ym);
  for(var i=0;i<=4;i++){var v=ym*i/4,y=b0.Y(v);g+='<line class="gl" x1="'+pl+'" x2="'+(W-pr)+'" y1="'+y+'" y2="'+y+'"/><text class="yl" x="'+(pl-8)+'" y="'+(y+3.5)+'" text-anchor="end">'+(i?fm(v):'0')+'</text>'}
  for(var m=0;m<=12;m+=(W<500?3:1))g+='<text class="xl" x="'+X(m)+'" y="'+(H-8)+'" text-anchor="middle">'+(m===0?'Now':m===12?'12 mo':m)+'</text>';
  /* fee marker */
  if(fm2<=12)g+='<line class="fl" x1="'+X(fm2)+'" x2="'+X(fm2)+'" y1="'+pt+'" y2="'+(H-pb)+'"/><text class="flt" x="'+(X(fm2)-5)+'" y="'+(pt+10)+'" text-anchor="end">Fee covered</text>';
  g+='<path class="ga" d="'+b0.g+'"/><path class="lt" d="'+b0.t+'"/><path class="ld" d="'+b0.d+'"/>';
  /* milestone markers on the desk line: small squares, numbered */
  var seen={};ms.forEach(function(o,i){if(o.md>12)return;var k=o.md,off=(seen[k]||0);seen[k]=off+1;var xx=X(o.md),yy=b0.Y(dA[o.md]);
    g+='<g class="mk" transform="translate('+xx+','+(yy-12-off*17)+')"><rect x="-7" y="-7" width="14" height="14" rx="2"/><text y="3.5" text-anchor="middle">'+(i+1)+'</text></g>'});
  svg.innerHTML=g;
  if(prev&&!RM&&!instant){var t0=null,pa=$('.ga',svg),pt_=$('.lt',svg),pd=$('.ld',svg);
    (function f(ts){if(t0==null)t0=ts+ST[2];var p=Math.max(0,Math.min(1,(ts-t0)/700)),e=1-Math.pow(1-p,3);
      var tt=tA.map(function(v,i){return prev.t[i]+(v-prev.t[i])*e}),dd=dA.map(function(v,i){return prev.d[i]+(v-prev.d[i])*e}),yy=prev.ymax+(ym-prev.ymax)*e;
      var bb=build(tt,dd,ym);pa.setAttribute('d',bb.g);pt_.setAttribute('d',bb.t);pd.setAttribute('d',bb.d);
      if(p<1)requestAnimationFrame(f)})(performance.now())}
  else if(!prev&&!RM){svg.classList.remove('in');void svg.offsetWidth;svg.classList.add('in')}}
$$('#cmix button').forEach(function(b){b.addEventListener('click',function(){mix=b.dataset.m;$$('#cmix button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});calc()})});
var rz;addEventListener('resize',function(){clearTimeout(rz);rz=setTimeout(function(){chart(true)},120)});
load();
})();
