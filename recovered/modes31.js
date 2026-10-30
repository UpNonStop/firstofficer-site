/* home-modes.html: persona pick, phone tabs, local clock, hero photos. The four screens come from panes.js. Mockup only. */
(function(){
var A=window.FO_A||'',P=window.FO_MODES||[],Q=new URLSearchParams(location.search.replace(/^\?/,'').replace(/\?/g,'&')),$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
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
/* ---- the phone shows the visitor's local time (H:MM); 9:41 stays as the no-JS fallback. ?h= pins the hour for tests ---- */
var greet='Good evening';
function clock(){var d=new Date(),h=Q.has('h')?+Q.get('h'):d.getHours(),m=Q.has('h')?41:d.getMinutes();
  greet=h<5?'Good evening':h<12?'Good morning':h<17?'Good afternoon':'Good evening';
  var t=(h%12||12)+':'+(m<10?'0':'')+m;k('clock',t);[].forEach.call(document.querySelectorAll('.cel .sb>span'),function(e){e.textContent=t});if(D)k('greet',greet+', '+D.first)}
var D,tab=['earn','burn','return','learn'].indexOf(Q.get('tab'))>=0?Q.get('tab'):'earn';
function k(n,v,html){$$('[data-k="'+n+'"]').forEach(function(e){if(html)e.innerHTML=v;else e.textContent=v})}
function chips(ids){return '<div class="zlgs">'+ids.map(function(i){return '<span><img src="'+lg(i)+'" alt="">'+NM[i]+'</span>'}).join('')+'</div>'}
function render(){
  var p=P[idx-1];D=p;
  try{localStorage.setItem('fo_modes_last',idx)}catch(e){}
  var before=p.spend*1e3*p.from,after=p.spend*1e3*p.to,retSum=p.ret.reduce(function(a,r){return a+r[1]},0);
  var mx=Math.max.apply(null,p.cats.map(function(c){return c[1]}));
  var PN=window.FO_PANES;
  var H={earn:PN.earn(p),burn:PN.burn(p),'return':PN.ret(p),learn:PN.learn(p)};
  $$('.mpane').forEach(function(e){e.innerHTML=H[e.dataset.t]});
  /* page copy, second person; the persona is only the example */
  k('fromx',x(p.from));
  k('spendlab',poss(p.first)+' spend today');  k('spend','$'+p.spend+'k');k('spendsub','a year on cards, earning '+x(p.from));
  k('cats',p.cats.slice(0,3).map(function(c){return '<li><span>'+c[0]+'</span><b>'+x(c[2])+'</b><u><i style="width:'+Math.round(c[1]/mx*100)+'%"></i></u></li>'}).join(''),1);
  k('before',pts(before));k('after',pts(after));
  var bb=$('[data-k="barb"]'),ba=$('[data-k="bara"]');bb.style.width='0';ba.style.width='0';
  setTimeout(function(){bb.style.width=Math.round(before/after*100)+'%';ba.style.width='100%'},RM?0:350);
  k('tripimg','');$('[data-k="tripimg"]').style.backgroundImage='url('+A+p.img+')';
  k('trip',p.trip);k('trippct',p.pct+'% there, est.');
  var lab='Example: '+p.first+', '+p.biz+', '+p.city+'. Fictional. Figures are estimates.';
  k('label',lab);k('h-label',lab);
  k('h-earn','<b>'+x(p.from)+' → '+x(p.to)+'</b>per $1 of card spend, est.',1);
  k('h-burn','<b>'+p.pct+'% there</b>'+p.trip+', est.',1);var bi=document.querySelector('[data-k="h-burnimg"]');if(bi)bi.style.backgroundImage='url('+A+p.img+')';
  k('h-return','<b>'+usd(retSum)+'</b>found in one Friday, est.',1);
  var L=p.learn;k('h-learn','<b>'+L[1]+'</b>'+L[2],1);
  show(tab,1);
}
function show(t,quiet){
  tab=t;var p=D,ph=$('#mphone');
  ph.className='mphone p-'+t;
  k('greet',greet+', '+p.first);
  k('title',t==='learn'?poss(p.first)+' Learn':poss(p.short)+' '+t.charAt(0).toUpperCase()+t.slice(1));
  $$('.mpane').forEach(function(e){e.classList.toggle('on',e.dataset.t===t)});
  $$('.mtb button').forEach(function(b){var on=b.dataset.t===t;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on)});
}
/* ---- the phone's own tabs pulse one at a time and the modes auto-cycle, until the visitor taps a tab ---- */
var T=['earn','burn','return','learn'],DUR=5200,timer=null,held=RM||Q.has('tab');
if(RM)document.documentElement.classList.add('fo-still');
function hold(){held=true;clearInterval(timer);$('.mtb').classList.add('held');$('.mstage').classList.add('tried')}
function cycle(){if(held)return;timer=setInterval(function(){if(document.documentElement.classList.contains('fo-still'))return;show(T[(T.indexOf(tab)+1)%4])},DUR)}
$$('.mtb button').forEach(function(b){b.addEventListener('click',function(){hold();show(b.dataset.t)})});
$$('.wnext').forEach(function(nb){nb.addEventListener('click',function(){idx=idx%P.length+1;render();if(!held){clearInterval(timer);cycle()}})});
render();clock();setTimeout(function(){clock();setInterval(clock,60000)},(60-new Date().getSeconds())*1000);
if(held)$('.mtb').classList.add('held');cycle();
/* ---- hero photos: low opacity, rotating ---- */
var bg=$('.mbg'),N=[],SFX=innerWidth<761?'-m':'';for(var i=0;i<=30;i++)N.push(A+'img/rec/bg/'+(i<10?'0':'')+i+SFX+'.webp');
var off=window.FO_BG0?FO_BG0.k%N.length:Math.floor(Math.random()*N.length),cur=0,els=[0,1].map(function(){var e=document.createElement('i');bg.insertBefore(e,bg.firstChild);return e});
els[0].style.backgroundImage='url('+N[off]+')';els[0].classList.add('on');
if(!RM)setInterval(function(){if(document.documentElement.classList.contains('fo-still'))return;var nx=els[1-cur];off=(off+1)%N.length;nx.style.backgroundImage='url('+N[off]+')';var im=new Image();im.onload=function(){nx.classList.add('on');els[cur].classList.remove('on');cur=1-cur};im.src=N[off]},5200);
})();
