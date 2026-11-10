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
  'return':['Return','Points per dollar times cents per point. 3 × 1.6¢ is 4.8¢ per $1, est., because both are known. Unknown is not zero.'],
  learn:['Learn','Two minutes a week. One short lesson from the owner\'s own data: what changed in the programs, and what it means for the goal.']};
var TITLE={earn:p.short+'’s Earn',burn:p.short+'’s Burn','return':p.short+'’s Return',learn:p.first+'’s Learn'};
function greet(){var h=new Date().getHours();return h<5?'Good evening':h<12?'Good morning':h<17?'Good afternoon':'Good evening'}
function clock(){var d=new Date(),h=d.getHours(),m=d.getMinutes();var c=$('.mclk',root);if(c)c.textContent=(h%12||12)+':'+(m<10?'0':'')+m}
/* Return on this page: Leo's desk earn (points per $1) times the 1.6¢ example already printed on the Learn card.
   Both have to be known. Unknown is not zero, and it is not a gift, a freebie, or a statement credit. */
var EARN_PTS=p.to,BURN_CENTS=1.6,retKnown=EARN_PTS>0&&BURN_CENTS>0,retCents=retKnown?Math.round(EARN_PTS*BURN_CENTS*10)/10:null;
function cents(n){return (Math.round(n*10)/10).toString().replace(/\.0$/,'')+'¢'}
function retPane(){
  var rows=retKnown
    ? '<div class="zrl"><i class="zdot ze"></i><span>Earn</span><b>'+EARN_PTS+' pts / $1</b></div>'
     +'<div class="zrl"><i class="zdot zb"></i><span>Burn</span><b>'+cents(BURN_CENTS)+' / point</b></div>'
     +'<div class="zrl"><i class="zdot zr"></i><span>Return</span><b>'+cents(retCents)+' / $1</b></div>'
     +'<p class="znote">Both known, so it calculates. Est. Not a gift, a freebie, or a statement credit.</p>'
    : '<p class="znote">Earn or Burn is unknown, so Return stays blank. Unknown is not zero.</p>';
  return F.bub('o','What is the return on a dollar?',p)+
    '<div class="zkc"><div class="zkh">Return<b>cents per $1</b></div>'+rows+'</div>'+
    F.bub('f',retKnown?'Earn times burn is '+cents(retCents)+' per dollar, est.':'Return stays blank until both are known.',p)}
function desk(){
  /* Leo's numbers, the same ones the home page and the product page use, except Return, which is the rate */
  var t=[['earn','Earn','#107B49','$12,240','found per year, est.'],
         ['burn','Burn','#BB4401',p.pct+'%','of the Tokyo goal, '+Math.round(p.have/1000)+'k points'],
         ['return','Return','#7149C9',retKnown?cents(retCents):'Blank',retKnown?'per $1, est.':'needs earn and burn'],
         ['learn','Learn','#085884','1.6¢','per point, est.']];
  return '<div class="zdk-on"><i></i>The desk is online<span>Updated 8:14 AM</span></div>'+
    '<div class="zdk-g">'+t.map(function(x){return '<button type="button" class="zdk" data-go="'+x[0]+'" style="--c:'+x[2]+'"><small>'+x[1]+'</small><b>'+x[3]+'</b><span>'+x[4]+'</span></button>'}).join('')+'</div>'+
    '<div class="zkc zdk-t"><div class="zkh">The desk<b>Since Friday</b></div><div class="zdk-cons"><i></i><i></i><i></i>Checked 3 programs · 6s</div>'+
    F.bub('o','Anything waiting for me?',p)+F.bub('f',greet()+', '+p.first+'. One move is confirmed. One more waits for approval.',p)+'</div>'+
    '<div class="zdk-ask"><span>Ask First Officer</span><i aria-hidden="true">↑</i></div>'}
var H={desk:desk(),earn:F.earn(p),burn:F.burn(p),'return':retPane(),learn:F.learn(p)};
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
