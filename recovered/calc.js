/* calculator-modes.html: live estimate on the home-modes examples (fo-modes-data.js). Mockup only, fictional owners, estimates.
   Points a year = monthly spend x 12 x points per $1, per line. Today uses each line's current rate (or the card mix you pick);
   the desk uses each line's desk rate. Value of the extra points = (desk - today) x 85% used x 1.0c to 1.6c a point.
   Fit gate: about $25K a month on cards, and the value has to clear $550 a month ($6,600 a year). */
(function(){
var P=window.FO_MODES||[],A=window.FO_A||'',$=function(i){return document.getElementById(i)};
var FEE=550*12,GATE=25000,UTIL=.85,LO=.01,HI=.016,GMAX=60000;
var r=function(s){return parseFloat(String(s))||0};
function usd(v){return '$'+Math.round(v).toLocaleString('en-US')}
function k(v){return v>=1e6?(v/1e6).toFixed(2).replace(/\.?0+$/,'')+'M':Math.round(v/1e3)+'k'}
function kd(v){if(Math.abs(v)<1000)return '$'+Math.round(v/50)*50;return v>=1e6?'$'+(v/1e6).toFixed(1)+'M':'$'+(v/1e3).toFixed(1).replace(/\.0$/,'')+'k'}
function rate(x){return (Math.round(x*10)/10)+'x'}
var cur=0,mix='ex',S=[];
var EX=[['Paris in business for 2',280000,'img/fo-paris.jpg','Round trip, saver level'],['A week at a top hotel',175000,'img/hotel.jpg','7 nights, standard room'],['Maui for a family of 4',140000,'img/hero/dest/02.jpg','Economy round trip'],['Maldives, 5 nights',300000,'img/fo-maldives.jpg','Overwater villa, saver level']];
/* examples */
var ex=$('cex');
P.forEach(function(p,i){var b=document.createElement('button');b.type='button';b.setAttribute('role','tab');b.dataset.i=i;
  var m=p.cats.reduce(function(a,c){return a+c[1]},0);
  b.innerHTML='<b>'+p.first+', '+p.short.replace(/&/g,'&amp;')+'</b><small>'+p.ind+'</small><span>$'+Math.round(m)+'K/mo</span>';
  b.onclick=function(){load(i)};ex.appendChild(b)});
function load(i){cur=i;var p=P[i];S=p.cats.map(function(c){return c[1]*1000});
  [].forEach.call(ex.children,function(b,j){b.classList.toggle('on',j===i);b.setAttribute('aria-selected',j===i)});
  $('cwho').textContent='Example: '+p.first+', '+p.biz+', '+p.city+'. Fictional. Move any line to make it yours.';
  var h='';p.cats.forEach(function(c,j){var v=c[1]*1000,mx=Math.max(30000,Math.ceil(v*2.5/5000)*5000);
    h+='<div class="crow"><label class="crn" for="s'+j+'">'+c[0]+' <small>'+c[2]+' → <b>'+c[3]+'</b></small></label>'+
       '<div class="crv"><b id="v'+j+'">'+usd(v)+'</b><small>a month</small></div>'+
       '<input type="range" id="s'+j+'" min="0" max="'+mx+'" step="500" value="'+v+'" aria-label="'+c[0]+', dollars a month"></div>'});
  $('crows').innerHTML=h;
  p.cats.forEach(function(c,j){var el=$('s'+j);el.oninput=function(){S[j]=+el.value;calc()}});
  /* return + learn */
  var tot=0,l='';p.ret.forEach(function(x){tot+=x[1];l+='<li><span>'+x[0]+'</span><b>'+usd(x[1])+'</b></li>'});
  $('retV').textContent=usd(tot);$('retL').innerHTML=l;
  var L=p.learn,f=L[5]||'{v}¢',mxv=Math.max.apply(null,L[3].map(function(x){return x[1]}));
  $('lrnH').textContent=L[0];$('lrnV').textContent=L[1];$('lrnS').textContent=/est\.$/.test(L[2])?L[2]:L[2]+', est.';$('lrnF').textContent=L[4];
  $('lrnB').innerHTML=L[3].map(function(x){return '<div><span>'+x[0]+'</span><u><i style="width:'+(x[1]/mxv*100).toFixed(1)+'%"></i></u><b>'+f.replace('{v}',x[1])+'</b></div>'}).join('');
  calc();
}
[].forEach.call($('cmix').children,function(b){b.onclick=function(){mix=b.dataset.m;[].forEach.call($('cmix').children,function(x){x.classList.toggle('on',x===b);x.setAttribute('aria-checked',x===b)});calc()}});
function calc(){var p=P[cur],spend=0,t=0,d=0,rows='';
  p.cats.forEach(function(c,j){var v=S[j],tr=mix==='ex'?r(c[2]):+mix,dr=r(c[3]),pt=v*12*tr,pd=v*12*dr;spend+=v;t+=pt;d+=pd;
    var el=$('s'+j);el.style.setProperty('--p',(el.value/el.max*100)+'%');$('v'+j).textContent=usd(v);
    rows+='<tr><td>'+c[0]+'</td><td><b>'+rate(tr)+'</b></td><td><b class="d">'+c[3]+'</b></td><td>'+k(t===pt?pt:pt)+' → '+k(pd)+'</td></tr>'});
  $('croute').innerHTML=rows;
  $('ctot').textContent=usd(spend)+' a month';$('ctoty').textContent=k(spend*12).replace('k','k').replace(/^/,'$')+' a year';
  $('rToday').textContent=k(t);$('rDesk').textContent=k(d);
  var mx=Math.max(t,d,1);$('bT').style.width=(t/mx*100)+'%';$('bD').style.width=(d/mx*100)+'%';
  $('rBlend').textContent=spend?('About '+rate(t/spend/12)+' per $1 today, '+rate(d/spend/12)+' with your desk, est.'):'';
  var gain=Math.max(0,d-t)*UTIL,lo=gain*LO,hi=gain*HI;
  $('rVal').textContent=kd(lo)+'–'+kd(hi);
  $('cmini').textContent=k(d)+' a year with your desk, est.';
  var g=$('gFill');g.style.width=Math.min(100,spend/GMAX*100)+'%';g.parentNode.parentNode.classList.toggle('under',spend<GATE);
  var V=$('rV'),T,B;V.classList.remove('meh','no');
  if(spend<GATE){V.classList.add('no');T='Not a fit yet';B='At '+usd(spend)+' a month, you\'re under the ~$25K gate. $550 a month would take most of what a desk could find, so keep your card, use the free tools, and come back when your spend grows. You\'d hear the same from us on the call.'}
  else if(lo>=FEE){T='A fit, by this estimate';B='Your extra points are worth about '+kd(lo-FEE)+' to '+kd(hi-FEE)+' a year more than the $550 fee, est. Your Found Money Call checks it against your real statements.'}
  else if(hi>=FEE){V.classList.add('meh');T='A close call';B='It may clear $550 a month, or it may not. Your 20-minute Found Money Call checks your statements and gives you a straight yes or no.'}
  else{V.classList.add('no');T='Not a fit at this mix';B='By this estimate the extra points don\'t clear $550 a month. Keep what you have. If that changes, the call will tell you so.'}
  $('rVt').textContent=T;$('rVp').textContent=B;
  /* burn */
  var L=[[p.trip,p.need,p.img,p.when?'Example trip, '+p.when:'Example trip']];
  EX.forEach(function(e){if(L.length<4&&e[2]!==p.img&&e[0]!==p.trip)L.push(e)});
  $('cb4').innerHTML=L.map(function(e){var x=d/e[1];
    return '<div class="cbk"><div style="background-image:url('+A+e[2]+')"></div><div class="cbb"><small>Burn · est.</small><h3>'+e[0].replace(/&/g,'&amp;')+'</h3><p>'+e[3]+'. About '+k(e[1])+' points, est.</p>'+
      '<div class="cbx">'+(x>=1?'<b>'+x.toFixed(1)+'×</b><span>times over, from a year of points with your desk</span>':'<b>'+Math.round(x*100)+'%</b><span>of it from one year with your desk</span>')+'</div></div></div>'}).join('');
}
var q=new URLSearchParams(location.search).get('ex'),st=0;P.forEach(function(p,i){if(q&&p.first.toLowerCase()===q.toLowerCase())st=i});
load(st);
})();
