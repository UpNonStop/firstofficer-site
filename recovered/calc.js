/* calculator-modes.html: live calculator. The phone's Earn screen and the result card read the same numbers.
   Mockup only; every figure is an estimate. ?ex=<first name> picks an example owner (default Leo). */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches||/[?&#]still=1/.test(location.href);
var FEE=6600,GATE=25000,UTIL=.85,LO=.01,HI=.016,GMAX=60000;
var LOGO={1:'01-amex',2:'02-chase',3:'03-capital-one',4:'04-citi',9:'09-marriott',10:'10-hilton',11:'11-ihg',12:'12-hyatt',17:'17-united',18:'18-delta',19:'19-american',20:'20-southwest',25:'25-aeroplan',26:'26-flying-blue',32:'32-singapore',35:'35-turkish',37:'37-ana',47:'47-virgin-atlantic',48:'48-tap-air-portugal',50:'50-jal'};
var NM={1:'Amex',2:'Chase',3:'Capital One',4:'Citi',9:'Marriott',10:'Hilton',11:'IHG',12:'Hyatt',17:'United',18:'Delta',19:'American',20:'Southwest',25:'Aeroplan',26:'Flying Blue',32:'Singapore',35:'Turkish',37:'ANA',47:'Virgin Atlantic',48:'TAP',50:'JAL'};
var EX=[['Paris for two','Business class, round trip',280000,'img/fo-paris.jpg'],['A week at a top hotel','Seven nights, points only',175000,'img/hotel.jpg'],['Maui for the family','Four seats, economy',140000,'img/hero/dest/02.jpg'],['The Maldives','Business class for two, plus five nights',300000,'img/fo-maldives.jpg']];
function lg(id){return LOGO[id]?A+'img/hero/prog/'+LOGO[id]+'.jpg':''}
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function kusd(n){return n>=1e3?'$'+(n/1e3).toFixed(1).replace(/\.0$/,'')+'k':usd(n)}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function poss(s){return s+(/s$/.test(s)?'\u2019':'\u2019s')}
function k(n,v,html){$$('[data-k="'+n+'"]').forEach(function(e){if(html)e.innerHTML=v;else e.textContent=v})}
function chips(ids){return '<div class="zlgs">'+ids.map(function(i){return '<span><img src="'+lg(i)+'" alt="">'+NM[i]+'</span>'}).join('')+'</div>'}
var want=((location.href.match(/[?&#]ex=([a-z]+)/i)||[])[1]||'leo').toLowerCase(),idx=0;
P.forEach(function(p,i){if(p.first.toLowerCase()===want)idx=i});
var D,S=[],mix='ex',tab='earn',greet='Good evening';
/* ---- example owner tiles ---- */
$('#qtiles').innerHTML=P.map(function(p,i){var m=p.cats.reduce(function(a,c){return a+c[1]},0);
  return '<button type="button" role="tab" data-i="'+i+'" style="background-image:url('+A+p.img+')" aria-label="'+p.first+', '+p.ind+'"><span><b>'+p.first+'</b><small>$'+(Math.round(m*10)/10)+'K/mo</small></span></button>'}).join('');
$$('#qtiles button').forEach(function(b){b.addEventListener('click',function(){idx=+b.dataset.i;load()})});
/* ---- spend blocks ---- */
function blocks(){var p=D;
  $('#qblocks').innerHTML=p.cats.map(function(c,i){var mx=Math.max(20,Math.ceil(c[1]*3/5)*5);
    return '<div class="qb"><div class="qbh"><label for="qs'+i+'">'+c[0]+'</label><span data-r="'+i+'">'+c[2]+' → '+c[3]+'</span></div><div class="qbn"><b data-v="'+i+'">$0</b><small>a month</small></div><input id="qs'+i+'" type="range" min="0" max="'+mx*1000+'" step="500" value="'+c[1]*1000+'" aria-label="'+c[0]+', dollars a month"><div class="qbf"><span>Today <b data-t="'+i+'"></b></span><span>Desk <b data-d="'+i+'"></b></span></div></div>'}).join('');
  $$('#qblocks input').forEach(function(r,i){r.addEventListener('input',function(){S[i]=+r.value;calc()})});
}
function load(){D=P[idx];S=D.cats.map(function(c){return c[1]*1000});
  $$('#qtiles button').forEach(function(b,i){var on=i===idx;b.classList.toggle('on',on);b.setAttribute('aria-selected',on)});
  $('#qwho').textContent='Example: '+D.first+', '+D.biz+'. Fictional.';
  blocks();panes();calc();show(tab)}
function rateT(c){return mix==='ex'?parseFloat(c[2]):+mix}
/* ---- the math: per line, a year. Phone and result card both read R ---- */
var R={};
function calc(){var p=D,mo=0,t=0,d=0,mxs=Math.max.apply(null,S.concat([1]));
  p.cats.forEach(function(c,i){var a=S[i],rt=rateT(c),rd=parseFloat(c[3]);mo+=a;t+=a*12*rt;d+=a*12*rd;
    var r=$$('#qblocks input')[i];r.style.setProperty('--p',(r.value/r.max*100)+'%');
    $('[data-v="'+i+'"]').textContent=usd(a);$('[data-t="'+i+'"]').textContent=pts(a*12*rt);$('[data-d="'+i+'"]').textContent=pts(a*12*rd);
    $('[data-r="'+i+'"]').textContent=x(rt)+' → '+c[3]});
  R={mo:mo,t:t,d:d};var gain=Math.max(0,d-t)*UTIL,lo=gain*LO,hi=gain*HI;
  $('#qtot').textContent=usd(mo);$('#qtoty').textContent='$'+Math.round(mo*12/1e3)+'k';$('#qbl').textContent=x(mo?Math.round(t/mo/12*100)/100:0);
  k('today',pts(t));k('desk',pts(d));k('plus','+'+pts(d-t)+' more points a year, est.');
  k('range',kusd(lo)+'–'+kusd(hi));k('gatev','$'+Math.round(mo/1e3)+'K');
  $('#qbT').style.width=(d?Math.round(t/d*100):0)+'%';$('#qbD').style.width=d?'100%':'0';
  $('#qgf').style.width=Math.min(100,mo/GMAX*100)+'%';$('.qgm').classList.toggle('under',mo<GATE);
  var v=$('#qv'),q=$('.qqf'),c1=$('#qc1'),cls,t1,t2,sh;
  if(mo<GATE){cls='no';t1='Not a fit yet.';sh='Not a fit yet';t2='At '+usd(mo)+' a month, $550 a month would cost you more than it finds. Here is what to do instead.'}
  else if(lo>=FEE){cls='';t1='Clears the fee.';sh='Clears the fee';t2='By about '+kusd(lo-FEE)+' to '+kusd(hi-FEE)+' a year after the $6,600, est. Your Found Money Call checks it on your real statements.'}
  else if(hi>=FEE){cls='meh';t1='Close call.';sh='Close call';t2='It clears at the top of the range, not the bottom. Your Found Money Call settles it on your real statements, free.'}
  else{cls='no';t1='Not a fit yet.';sh='Not a fit yet';t2='The extra points are worth about '+kusd(lo)+' to '+kusd(hi)+' a year, under the $6,600. Here is what to do instead.'}
  v.className='qv '+cls;$('#qvt').textContent=t1;$('#qvp').textContent=t2;q.className='qqf '+cls;q.textContent=sh;
  $('#qvl').innerHTML=cls==='no'?'<li><b>1</b><span>Keep the card you have. It is doing an honest job at this spend.</span></li><li><b>2</b><span>Use the <a href="freebies.html">Freebies</a>. Free guides, no desk needed.</span></li><li><b>3</b><span>Come back when you pass ~$25K a month on cards.</span></li>':'';
  if(cls==='no'){c1.href='freebies.html';c1.innerHTML='Get the Freebies <span class="ar">→</span>'}else{c1.href='book.html';c1.innerHTML='Get your desk <span class="ar">→</span>'}
  earn();burn();
}
/* ---- the phone: Earn is live, the other tabs show the same example ---- */
function earn(){var p=D,mxs=Math.max.apply(null,S.concat([1])),fr=R.mo?Math.round(R.t/R.mo/12*100)/100:0;
  $('.mpane[data-t="earn"]').innerHTML='<div class="zbu zo">'+p.qE+'</div>'+
  '<div class="zbu zf"><small>First Officer</small>Most of it earns '+x(fr)+'. That is the gap. Here is what your desk found.</div>'+
  '<div class="zkc"><div class="zkh">Your spend by line<b>per $1, est.</b></div><div class="zsp">'+p.cats.map(function(c,i){return '<span>'+c[0]+'</span><em>$'+(Math.round(S[i]/100)/10)+'k/mo</em><span class="zx"><s>'+x(rateT(c))+'</s>→ <b>'+c[3]+'</b></span><u><i style="width:'+Math.round(S[i]/mxs*100)+'%"></i></u>'}).join('')+'</div></div>'+
  '<div class="zkc"><div class="zkh">Points a year<b>est.</b></div><div class="zba"><div><small>Today</small><b>'+pts(R.t)+'</b></div><span>→</span><div><small>With your desk</small><b>'+pts(R.d)+'</b></div></div>'+chips(p.earnL)+'</div>'+
  '<div class="zkc zmv"><div><small>Waiting for your OK</small><b>'+p.move[0]+'</b><em>+'+usd(p.move[1])+' a year, est.</em></div><span class="zok">Approve</span></div>'}
function panes(){var p=D,retSum=p.ret.reduce(function(a,r){return a+r[1]},0);
  $('.mpane[data-t="burn"]').innerHTML='<div class="zbu zo">'+p.qB+'</div>'+
    '<div class="zkc"><div class="ztr" style="background-image:url('+A+p.img+')"><div><small>'+p.when+'</small><b>'+p.trip+'</b></div></div>'+
    '<div class="zpg"><div class="zr"><span>'+pts(p.have)+' of '+pts(p.need)+' points</span><b>'+p.pct+'% there, est.</b></div><u><i style="width:'+p.pct+'%"></i></u></div>'+chips(p.burnL)+'</div>'+
    '<div class="zkc"><div class="zkh">Requirements vetted<b>'+p.reqs.length+' of '+p.reqs.length+'</b></div><ul class="zck">'+p.reqs.map(function(r){return '<li><b>✓</b>'+r+'</li>'}).join('')+'</ul></div>'+
    '<div class="zsd"><img src="'+A+'img/rec/chev.png" alt=""><div><small>Sent to the desk</small><b>Pick your dates. The desk books after you approve.</b></div></div>';
  var wk=[38,52,30,64,46,58,72,100];
  $('.mpane[data-t="return"]').innerHTML='<div class="zbu zo">What did this week bring in?</div>'+
    '<div class="zkc"><div class="zkh">Friday findings<b>this week</b></div><div class="zrt"><div><b>'+usd(retSum)+'</b><small>found this week, est.</small></div><div class="zwkb">'+wk.map(function(h){return '<i style="height:'+h+'%"></i>'}).join('')+'</div></div>'+
    p.ret.map(function(r){return '<div class="zrl"><span>'+r[0]+'</span><b>'+usd(r[1])+'</b></div>'}).join('')+'</div>'+
    '<div class="zbu zf"><small>First Officer</small>All three are in your Friday scorecard. One number, in dollars.</div><div class="zby"><span>✓</span>Checked against your statements</div>';
  var L=p.learn,u=L[5]||'{v}\u00a2',lm=Math.max.apply(null,L[3].map(function(b){return b[1]}));
  $('.mpane[data-t="learn"]').innerHTML='<div class="zbu zo">Teach me one thing this week.</div>'+
    '<div class="zkc zls"><div class="zlt">Your 2 minute lesson</div><h5>'+L[0]+'</h5><div class="zlb"><b>'+L[1]+'</b><small>'+L[2]+'</small></div><div class="zlbars">'+L[3].map(function(b){return '<div><span>'+b[0]+'</span><u><i style="width:'+Math.round(b[1]/lm*100)+'%"></i></u><b>'+u.replace('{v}',b[1])+'</b></div>'}).join('')+'</div></div>'+
    '<div class="zbu zf"><small>First Officer</small>'+L[4]+'</div>';
  /* page strip: Return and Learn */
  $('#qretV').textContent=usd(retSum);$('#qretL').innerHTML=p.ret.map(function(r){return '<li><span>'+r[0]+'</span><b>'+usd(r[1])+'</b></li>'}).join('');
  $('#qlrnH').textContent=L[0];$('#qlrnV').textContent=L[1];$('#qlrnS').textContent=L[2];$('#qlrnF').textContent=L[4];
  $('#qlrnB').innerHTML=L[3].map(function(b){return '<div><span>'+b[0]+'</span><u><i style="width:'+Math.round(b[1]/lm*100)+'%"></i></u><b>'+u.replace('{v}',b[1])+'</b></div>'}).join('');
}
function burn(){var use=R.d*UTIL;
  $('#qb4').innerHTML=EX.map(function(e){var n=use/e[2];
    return '<div class="qtr" style="background-image:url('+A+e[3]+')"><div><small>~'+pts(e[2])+' points, est.</small><h3>'+e[0]+'</h3><p>'+e[1]+'</p><div class="qx"><b>'+(n>=1?Math.floor(n)+'×':Math.round(n*100)+'%')+'</b><span>'+(n>=1?'a year with your desk, est.':'of the way there in a year with your desk, est.')+'</span></div></div></div>'}).join('')}
function show(t){tab=t;var p=D;$('#mphone').className='mphone p-'+t;
  k('greet',greet+', '+p.first);k('title',t==='learn'?poss(p.first)+' Learn':poss(p.short)+' '+t.charAt(0).toUpperCase()+t.slice(1));
  $$('.mpane').forEach(function(e){e.classList.toggle('on',e.dataset.t===t)});
  $$('.mtb button').forEach(function(b){var on=b.dataset.t===t;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on)})}
$$('.mtb button').forEach(function(b){b.addEventListener('click',function(){$('.mtb').classList.add('held');show(b.dataset.t)})});
$$('#qmix button').forEach(function(b){b.addEventListener('click',function(){mix=b.dataset.m;$$('#qmix button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});calc();earn()})});
function clock(){var d=new Date(),h=d.getHours(),m=d.getMinutes();greet=h<5?'Good evening':h<12?'Good morning':h<17?'Good afternoon':'Good evening';
  k('clock',(h%12||12)+':'+(m<10?'0':'')+m);if(D)k('greet',greet+', '+D.first)}
$('.mtb').classList.add('held');clock();load();setInterval(clock,30000);
/* ---- hero photos: low opacity, rotating (same as the landing) ---- */
var bg=$('.mbg'),N=[];for(var i=0;i<=30;i++)N.push(A+'img/rec/bg/'+(i<10?'0':'')+i+'.webp');
var off=Math.floor(Math.random()*N.length),cur=0,els=[0,1].map(function(){var e=document.createElement('i');bg.insertBefore(e,bg.firstChild);return e});
els[0].style.backgroundImage='url('+N[off]+')';els[0].classList.add('on');
if(!RM)setInterval(function(){var nx=els[1-cur];off=(off+1)%N.length;nx.style.backgroundImage='url('+N[off]+')';var im=new Image();im.onload=function(){nx.classList.add('on');els[cur].classList.remove('on');cur=1-cur};im.src=N[off]},5200);
})();
