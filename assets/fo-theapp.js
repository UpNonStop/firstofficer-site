/* The App page (the-app.html): one phone, five tabs, for Leo, the site's fictional example owner.
   Earn, Burn, Return and Learn are the same panes the home phone draws (recovered/panes.js, fo-modes-data.js); the Desk
   screen is drawn here. The phone's own tab bar, the list beside it and the Desk tiles all switch tabs.
   The clock and the greeting follow the visitor's local time. Every figure is an estimate. */
(function(){
var P=window.FO_MODES||[],F=window.FO_PANES,root=document.getElementById('tphone');
if(!root||!F||!P.length)return;
var p=P[0],A=window.FO_A||'',RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var CAP={
  desk:['Desk','The four pillars at a glance and the thread with the desk underneath. Ask anything, any time.'],
  earn:['Earn','Which card for which spend. Each move shows what it is worth a year, and waits for the owner\'s OK.'],
  burn:['Burn','Points into trips. A goal, a pace and a strategy. The desk vets the requirements and books after the owner approves.'],
  'return':['Return','Friday, in dollars. What the desk found, counted in dollars and checked against the owner\'s statements.'],
  learn:['Learn','Two minutes a week. One short lesson from the owner\'s own data: what changed in the programs, and what it means for the goal.']};
var TITLE={earn:p.short+'’s Earn',burn:p.short+'’s Burn','return':p.short+'’s Return',learn:p.first+'’s Learn'};
function greet(){var h=new Date().getHours();return h<5?'Good evening':h<12?'Good morning':h<17?'Good afternoon':'Good evening'}
function clock(){var d=new Date(),h=d.getHours(),m=d.getMinutes();var c=$('.mclk',root);if(c)c.textContent=(h%12||12)+':'+(m<10?'0':'')+m}
var retSum=p.ret.reduce(function(a,r){return a+r[1]},0);
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function desk(){
  /* Leo's numbers, the same ones the home page, the product page and the Friday report use */
  var t=[['earn','Earn','#107B49','$15,120','found per year, est.'],
         ['burn','Burn','#BB4401',p.pct+'%','of the Tokyo goal, '+Math.round(p.have/1000)+'k points'],
         ['return','Return','#7149C9',usd(retSum),'last Friday, est.'],
         ['learn','Learn','#085884',p.learn[1],p.learn[2]]];
  return '<div class="zdk-on"><i></i>The desk is online<span>Updated 8:14 AM</span></div>'+
    '<div class="zdk-g">'+t.map(function(x){return '<button type="button" class="zdk" data-go="'+x[0]+'" style="--c:'+x[2]+'"><small>'+x[1]+'</small><b>'+x[3]+'</b><span>'+x[4]+'</span></button>'}).join('')+'</div>'+
    '<div class="zkc zdk-t"><div class="zkh">The desk<b>Since Friday</b></div><div class="zdk-cons"><i></i><i></i><i></i>Checked 3 programs · 6s</div>'+
    F.bub('o','Anything waiting for me?',p)+F.bub('f',greet()+', '+p.first+'. One move is confirmed. One more waits for approval.',p)+'</div>'+
    '<div class="zdk-ask"><span>Ask First Officer</span><i aria-hidden="true">↑</i></div>'}
var H={desk:desk(),earn:F.earn(p),burn:F.burn(p),'return':F.ret(p),learn:F.learn(p)};
$$('.mpane',root).forEach(function(e){e.innerHTML=H[e.dataset.t]||''});
var cur='desk';
function show(t,fromUser){
  if(!H[t])return;cur=t;
  root.className='mphone p-'+t;
  $$('.mpane',root).forEach(function(e){e.classList.toggle('on',e.dataset.t===t)});
  $$('.mtb button',root).forEach(function(b){var on=b.dataset.t===t;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on?'true':'false')});
  $$('.tlist button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.t===t?'true':'false')});
  var sub=$('[data-tk="sub"]',root),ti=$('[data-tk="title"]',root);
  if(t==='desk'){sub.textContent='Today · Week 9 with the desk';ti.innerHTML=greet()+', <em>'+p.first+'.</em>'}
  else{sub.textContent=greet()+', '+p.first;ti.textContent=TITLE[t]}
  var ch=$('[data-tk="caph"]'),cp=$('[data-tk="capp"]');if(ch)ch.textContent=CAP[t][0];if(cp)cp.textContent=CAP[t][1];
  if(fromUser){var bar=$('.mtb',root);if(bar)bar.classList.add('held');stop()}
}
root.addEventListener('click',function(e){var b=e.target.closest('.mtb button,[data-go]');if(!b)return;show(b.dataset.t||b.dataset.go,1)});
$$('.tlist button').forEach(function(b){b.addEventListener('click',function(){show(b.dataset.t,1)})});
/* a slow tour until the visitor touches anything, only while the phone is on screen */
var order=['desk','earn','burn','return','learn'],timer=null,seen=false;
function step(){show(order[(order.indexOf(cur)+1)%order.length])}
function start(){if(RM||timer)return;timer=setInterval(step,4200)}
function stop(){if(timer){clearInterval(timer);timer=null}seen=true}
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){if(!seen)start()}else if(timer){clearInterval(timer);timer=null}})},{threshold:.5});io.observe(root)}
clock();setInterval(clock,30000);show('desk');
})();
