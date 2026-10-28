/* home-modes.html: persona pick, phone tabs, modes box, hero photos, sticky bar. Mockup only. */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],Q=new URLSearchParams(location.search),$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches||Q.get('still')==='1';
var LOGO={1:'01-amex',2:'02-chase',3:'03-capital-one',4:'04-citi',9:'09-marriott',10:'10-hilton',11:'11-ihg',12:'12-hyatt',17:'17-united',18:'18-delta',19:'19-american',20:'20-southwest',25:'25-aeroplan',26:'26-flying-blue',32:'32-singapore',35:'35-turkish',37:'37-ana',47:'47-virgin-atlantic',48:'48-tap-air-portugal',50:'50-jal'};
var NM=(window.CFG&&CFG.names)||{1:'Amex',2:'Chase',3:'Capital One',4:'Citi',9:'Marriott',10:'Hilton',11:'IHG',12:'Hyatt',17:'United',18:'Delta',19:'American',20:'Southwest',25:'Aeroplan',26:'Flying Blue',32:'Singapore',35:'Turkish',37:'ANA',47:'Virgin Atlantic',48:'TAP',50:'JAL'};
function lg(id){return LOGO[id]?A+'img/hero/prog/'+LOGO[id]+'.jpg':''}
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function poss(s){return s+(/s$/.test(s)?'\u2019':'\u2019s')}
function x(n){if(typeof n==='string')return n;return (+n).toFixed(1).replace(/\.0$/,'')+'x'}
/* ---- pick a persona: ?p=1..10, else random with no immediate repeat ---- */
var idx=parseInt(Q.get('p'),10);
if(!(idx>=1&&idx<=P.length)){var last=-1;try{last=+localStorage.getItem('fo_modes_last')}catch(e){}
  do{idx=1+Math.floor(Math.random()*P.length)}while(P.length>1&&idx===last)}
var hr=Q.has('h')?+Q.get('h'):new Date().getHours();
var greet=hr<5?'Good evening':hr<12?'Good morning':hr<17?'Good afternoon':'Good evening';
var D,tab=['earn','burn','return','learn'].indexOf(Q.get('tab'))>=0?Q.get('tab'):'earn';
var LINES={earn:'More points from the same spend',burn:'Better trips for your points',return:'Money found, every Friday',learn:'Know what your points are worth'};
function k(n,v,html){$$('[data-k="'+n+'"]').forEach(function(e){if(html)e.innerHTML=v;else e.textContent=v})}
function chips(ids){return '<div class="zlgs">'+ids.map(function(i){return '<span><img src="'+lg(i)+'" alt="">'+NM[i]+'</span>'}).join('')+'</div>'}
function render(){
  var p=P[idx-1];D=p;
  try{localStorage.setItem('fo_modes_last',idx)}catch(e){}
  var before=p.spend*1e3*p.from,after=p.spend*1e3*p.to,retSum=p.ret.reduce(function(a,r){return a+r[1]},0);
  var mx=Math.max.apply(null,p.cats.map(function(c){return c[1]}));
  var earn='<div class="zbu zo">'+p.qE+'</div>'+
    '<div class="zbu zf"><small>First Officer</small>Most of it earns '+x(p.from)+'. That is the gap. Here is what your desk found.</div>'+
    '<div class="zkc"><div class="zkh">Your spend by line<b>per $1, est.</b></div><div class="zsp">'+p.cats.slice(0,3).map(function(c){return '<span>'+c[0]+'</span><em>$'+c[1]+'k/mo</em><span class="zx"><s>'+x(c[2])+'</s>→ <b>'+x(c[3])+'</b></span><u><i style="width:'+Math.round(c[1]/mx*100)+'%"></i></u>'}).join('')+'</div></div>'+
    '<div class="zkc"><div class="zkh">Points a year<b>est.</b></div><div class="zba"><div><small>Today</small><b>'+pts(before)+'</b></div><span>→</span><div><small>With your desk</small><b>'+pts(after)+'</b></div></div>'+chips(p.earnL)+'</div>'+
    '<div class="zkc zmv"><div><small>Waiting for your OK</small><b>'+p.move[0]+'</b><em>+'+usd(p.move[1])+' a year, est.</em></div><span class="zok">Approve</span></div>';
  var burn='<div class="zbu zo">'+p.qB+'</div>'+
    '<div class="zkc"><div class="ztr" style="background-image:url('+A+p.img+')"><div><small>'+p.when+'</small><b>'+p.trip+'</b></div></div>'+
    '<div class="zpg"><div class="zr"><span>'+pts(p.have)+' of '+pts(p.need)+' points</span><b>'+p.pct+'% there, est.</b></div><u><i style="width:'+p.pct+'%"></i></u></div>'+chips(p.burnL)+'</div>'+
    '<div class="zkc"><div class="zkh">Requirements vetted<b>'+p.reqs.length+' of '+p.reqs.length+'</b></div><ul class="zck">'+p.reqs.map(function(r){return '<li><b>✓</b>'+r+'</li>'}).join('')+'</ul></div>'+
    '<div class="zsd"><img src="'+A+'img/rec/chev.png" alt=""><div><small>Sent to the desk</small><b>Pick your dates. The desk books after you approve.</b></div></div>';
  var wk=[38,52,30,64,46,58,72,100];
  var ret='<div class="zbu zo">What did this week bring in?</div>'+
    '<div class="zkc"><div class="zkh">Friday findings<b>this week</b></div><div class="zrt"><div><b>'+usd(retSum)+'</b><small>found this week, est.</small></div><div class="zwkb">'+wk.map(function(h){return '<i style="height:'+h+'%"></i>'}).join('')+'</div></div>'+
    p.ret.map(function(r){return '<div class="zrl"><span>'+r[0]+'</span><b>'+usd(r[1])+'</b></div>'}).join('')+'</div>'+
    '<div class="zkc"><div class="zkh">Where it came from<b>est.</b></div><div class="zst">'+p.ret.map(function(r,i){return '<i class="s'+i+'" style="flex:'+r[1]+'"></i>'}).join('')+'</div><div class="zleg">'+p.ret.map(function(r,i){return '<span><i class="s'+i+'"></i>'+Math.round(r[1]/retSum*100)+'%</span>'}).join('')+'</div></div>'+'<div class="zbu zf"><small>First Officer</small>All three are in your Friday scorecard. One number, in dollars.</div>'+
    '<div class="zby"><span>✓</span>Checked against your statements</div>';
  var L=p.learn,u=L[5]||'{v}\u00a2',lm=Math.max.apply(null,L[3].map(function(b){return b[1]}));
  var learn='<div class="zbu zo">Teach me one thing this week.</div>'+
    '<div class="zkc zls"><div class="zlt">Your 2 minute lesson</div><h5>'+L[0]+'</h5><div class="zlb"><b>'+L[1]+'</b><small>'+L[2]+'</small></div><div class="zlbars">'+L[3].map(function(b){return '<div><span>'+b[0]+'</span><u><i style="width:'+Math.round(b[1]/lm*100)+'%"></i></u><b>'+u.replace('{v}',b[1])+'</b></div>'}).join('')+'</div></div>'+
    '<div class="zbu zf"><small>First Officer</small>'+L[4]+'</div>'+
    '<div class="zkc"><div class="zkh">Your lessons<b>3 of 12</b></div><div class="zseg">'+[1,1,1,0,0,0,0,0,0,0,0,0].map(function(v){return '<i'+(v?' class="on"':'')+'></i>'}).join('')+'</div></div>'+'<div class="zqz"><span>Show me my numbers</span><span>Next lesson Friday</span></div>';
  var H={earn:earn,burn:burn,'return':ret,learn:learn};
  $$('.mpane').forEach(function(e){e.innerHTML=H[e.dataset.t]});
  /* page copy, second person; the persona is only the example */
  k('fromx',x(p.from));
  k('spend','$'+p.spend+'k');k('spendsub','a year on cards, earning '+x(p.from));
  k('cats',p.cats.slice(0,3).map(function(c){return '<li><span>'+c[0]+'</span><b>'+x(c[2])+'</b></li>'}).join(''),1);
  k('before',pts(before));k('after',pts(after));
  var bb=$('[data-k="barb"]'),ba=$('[data-k="bara"]');bb.style.width='0';ba.style.width='0';
  setTimeout(function(){bb.style.width=Math.round(before/after*100)+'%';ba.style.width='100%'},RM?0:350);
  k('tripimg','');$('[data-k="tripimg"]').style.backgroundImage='url('+A+p.img+')';
  k('trip',p.trip);k('trippct',p.pct+'% there, est.');
  var lab='Example: '+p.first+', '+p.biz+', '+p.city+'. Fictional. Figures are estimates.';
  k('label',lab);k('h-label',lab);
  k('h-earn','<b>'+x(p.from)+' → '+x(p.to)+'</b>per $1 on your spend, est.',1);
  k('h-burn','<b>'+p.pct+'% there</b>'+p.trip+', est.',1);
  k('h-return','<b>'+usd(retSum)+'</b>found in one Friday, est.',1);
  k('h-learn','<b>'+L[1]+'</b>'+L[2],1);
  show(tab,1);
}
function show(t,quiet){
  tab=t;var p=D,ph=$('#mphone');
  ph.className='mphone p-'+t;
  k('greet',greet+', '+p.first);
  k('title',t==='learn'?poss(p.first)+' Learn':poss(p.short)+' '+t.charAt(0).toUpperCase()+t.slice(1));
  k('mline',LINES[t]);
  $$('.mpane').forEach(function(e){e.classList.toggle('on',e.dataset.t===t)});
  $$('.mtb button,.mchips button').forEach(function(b){var on=b.dataset.t===t;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on)});
  /* restart the progress fill on the active chip */
  var c=$('.mchips button.on');if(c){c.classList.remove('on');void c.offsetWidth;c.classList.add('on')}
}
/* ---- auto-cycle until the user touches the modes or the tabs ---- */
var T=['earn','burn','return','learn'],DUR=5200,timer=null,held=RM||Q.has('tab');
function hold(){held=true;clearInterval(timer);$('.mmodes').classList.add('held')}
function cycle(){if(held)return;timer=setInterval(function(){show(T[(T.indexOf(tab)+1)%4])},DUR)}
$$('.mtb button,.mchips button').forEach(function(b){b.addEventListener('click',function(){hold();show(b.dataset.t)})});
$('.mmodes').style.setProperty('--dur',DUR+'ms');
$$('.wnext').forEach(function(nb){nb.addEventListener('click',function(){idx=idx%P.length+1;render();if(!held){clearInterval(timer);cycle()}})});
render();if(held)$('.mmodes').classList.add('held');cycle();
/* ---- hero photos: low opacity, rotating ---- */
var bg=$('.mbg'),N=[];for(var i=0;i<=30;i++)N.push(A+'img/rec/bg/'+(i<10?'0':'')+i+'.webp');
var off=Math.floor(Math.random()*N.length),cur=0,els=[0,1].map(function(){var e=document.createElement('i');bg.insertBefore(e,bg.firstChild);return e});
els[0].style.backgroundImage='url('+N[off]+')';els[0].classList.add('on');
if(!RM)setInterval(function(){var nx=els[1-cur];off=(off+1)%N.length;nx.style.backgroundImage='url('+N[off]+')';var im=new Image();im.onload=function(){nx.classList.add('on');els[cur].classList.remove('on');cur=1-cur};im.src=N[off]},5200);
/* ---- mobile sticky bar: hidden until the hero CTAs leave, hidden again near the closing CTA ---- */
var m=$('.mcta'),ctas=$('#mctas'),end=$('.ctab');
if(m&&ctas&&'IntersectionObserver' in window){var past=false,near=false;function up(){m.classList.toggle('show',past&&!near)}
  new IntersectionObserver(function(es){es.forEach(function(e){past=!e.isIntersecting&&e.boundingClientRect.top<0;up()})}).observe(ctas);
  if(end)new IntersectionObserver(function(es){es.forEach(function(e){near=e.isIntersecting;up()})}).observe(end);}
})();
