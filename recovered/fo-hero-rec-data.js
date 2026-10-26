/* Recovered showcase overrides for hero/fo-hero-data.js (Oct 27).
   One persona (Leo, Linden Row Insurance) so the hero matches the story below it; the First Officer mark
   points at the brand chevron; the second app tab is "Your plan" (one voice); no wires or nodes on the desk floor. */
(function(){var C=window.CFG;if(!C)return;
var bg=[];for(var k=0;k<31;k++)bg.push('img/rec/bg/'+(k<10?'0':'')+k+'.webp');C.pool=bg;
C.phone=C.phone.split('img/hero/fo-avatar.png').join('img/rec/fo-mark.png').replace('>Behind the desk<','>Your plan<');
C.personasD={};
function B(w,t,x){var o={w:w,t:t,h:t};if(x)for(var k in x)o[k]=x[k];return o}
function E(h){return h.replace(/(\$[\d,]+|\d+%)( a year)?(?=[ .,])/g,function(m){return m+'<i class="e">est</i>'})}
var leo={s:3,name:'Leo',ini:'LR',biz:'Linden Row Insurance',ind:'Insurance agency',city:'Columbus, OH',emo:'🛡️',tab:'earn',emp:'',
 cards:['Everyday business card','Business travel card'],top:'Lead-gen ads, agency software, carrier visits',spend:420,before:504,after:1428,
 nxt:'Tokyo in business for 2',nxte:'32% there, on pace for Mar 2027',win:'Mar 2027',
 pend:['Software to the 4x card','Ads to the 4x card','Tokyo seat watch, spring 2027','Unused travel credit','Carrier visits through the portal'],
 rel:[[1,'Earn'],[2,'Earn'],[47,'Burn'],[37,'Burn'],[50,'Burn']],t0:'8:15',pre:['Yesterday 4:02 PM ET',{w:'o',t:'Renewal season. Can you look at our cards before we renew?'},{w:'f',t:'Yes. Send me last month\'s statements and I will have the desk read every line.'},{w:'o',t:'Sent all three.'},{w:'f',t:'Got them. I will come back tonight with what we found.'}],buckets:[1],bucket:1,bucketL:'Owner',
 smart:'Ads and software moved to 4x, Tokyo in business for 2 on pace',
 dest:{i:1,title:'Tokyo, Japan',sub:'Trip idea for 2, business class'},
 mer:{k:'amazon',name:'Amazon',cat:'Office supplies',k_yr:6,card:'the everyday business card'},
 plan:{rows:[['Software to 4x','Moved. Confirmed on statements','+$2,880','ok'],['Ads to 4x','Waiting for your OK','+$7,200','wait'],['Unused travel credit','Claimed this month','$530','ok']],
  goal:['Tokyo, business for 2','32%',32,'On pace for March 2027. Seats not guaranteed.'],foot:['Found this year','$15,120 est.'],note:'Earn goes from 1.2x to 3.4x. All figures are estimates.'},
 beats:[
  B('o','We put about $35k a month on cards. Ads, software, carrier visits. Are we doing this right?'),
  B('f','Most of it earns 1x today. That is the gap. Give me a minute with the desk.'),
  B(1,'Checking which card in your wallet fits ads and software best, est.',{f:'Checking which card fits ads and software, est.'}),
  B(2,'Checking how your points could move toward a Tokyo trip, est.',{f:'Checking how points could move toward Tokyo, est.',to:47}),
  B('f','Ads are your biggest line, about $12,500 a month. Moving them to the 4x card is worth about $7,200 a year.',{h:E('Ads are your biggest line, about $12,500 a month. Moving them to the 4x card is worth about $7,200 a year.')}),
  B('o','And the software?'),
  B('f','Same move. About $2,880 a year. It renews monthly, so it can switch today.',{h:E('Same move. About $2,880 a year. It renews monthly, so it can switch today.')}),
  B('o','Could all this get us to Tokyo?',{re:1}),
  B(47,'Comparing partner options for business class to Tokyo, est. Pricing can change.',{f:'Comparing options for Tokyo, est.',to:37}),
  B(37,'Business seats to Tokyo open in small numbers. We watch spring dates.',{f:'Watching spring dates for Tokyo.'}),
  B(50,'Comparing a second option for Tokyo, est.',{f:'Comparing a second option, est.',to:37}),
  B('f','Yes. Business for 2, round trip. You are 32% there today, on pace for March 2027.',{h:E('Yes. Business for 2, round trip. You are 32% there today, on pace for March 2027.'),card:'map'}),
  B('o','Seats are not guaranteed, right?'),
  B('f','Right. I watch spring dates and tell you the moment good seats open.'),
  B('o','Do it. Move the software today.'),
  B('f','Software is moved. Ads are ready for your OK. Found so far: $15,120 a year.',{h:E('Software is moved. Ads are ready for your OK. Found so far: $15,120 a year.'),ban:['First Officer','Ads to 4x is ready for your OK. Est. $7,200 a year.']}),
  B('o','🙌',{tap:'👍'})
 ]};
C.personas=[leo];
C.css+=`
/* Oct 27: no wires, pulses or nodes on the desk floor */
svg.web,svg.pul{display:none!important}
/* specialists rise toward First Officer, light up, then settle */
.ag,.mag{transition:translate .9s cubic-bezier(.2,.8,.2,1)}
.ag .lg,.mag .lg{transition:transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .5s}
.ag.rel.lit .lg{box-shadow:0 0 0 2px #fff,0 0 0 4px var(--ac),0 0 22px -2px var(--act)}
.ag.rel .st .wk{display:inline-flex;padding:0 0 0 4px;vertical-align:middle}
.ag.rel .st .wk i{background:var(--ac)}
/* one voice in the app: specialists never post in the chat */
.mm.sp{display:none!important}
.vbtd .dsk{display:none}
.vbtd .chat{opacity:0;pointer-events:none}
.plan6{position:absolute;left:0;right:0;top:150px;bottom:86px;padding:14px 18px 0;display:none;z-index:4;background:#fff;font-family:Inter,sans-serif;color:#141216;overflow:hidden}
.vbtd .plan6{display:block}
.plan6 .pk{display:flex;justify-content:space-between;align-items:center;font:700 12px Inter,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#E60F86}
.plan6 .pk span{font-weight:500;letter-spacing:0;text-transform:none;color:#7d7884}
.plan6 .pt{font:400 26px/1.15 'DM Serif Display',serif;margin:6px 0 12px}
.plan6 .pr{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:16px;background:#faf7f2;margin-bottom:8px}
.plan6 .pr .pl{flex:1;min-width:0}
.plan6 .pr b{display:block;font:600 15.5px Inter,sans-serif}
.plan6 .pr small{display:block;font:400 13px Inter,sans-serif;color:#6d6874;margin-top:2px}
.plan6 .pr .pv{font:700 15px Inter,sans-serif;color:var(--ac)}
.plan6 .pr.wait{background:#fff0f8;box-shadow:inset 0 0 0 1.5px #FA1896}
.plan6 .pr.wait .pv{color:#E60F86}
.plan6 .pg{margin-top:12px;padding:14px;border-radius:16px;background:#fff7e0}
.plan6 .pgh{display:flex;justify-content:space-between;font:600 15px Inter,sans-serif}
.plan6 .pgh span{color:#9a6b00;font-weight:700}
.plan6 .pgb{height:8px;border-radius:8px;background:#f1e3b8;margin:10px 0 8px;overflow:hidden}
.plan6 .pgb i{display:block;height:100%;border-radius:8px;background:linear-gradient(90deg,#d9a520,#FA1896)}
.plan6 .pg small{font:400 12.5px Inter,sans-serif;color:#6d6874}
.plan6 .pf{display:flex;justify-content:space-between;align-items:baseline;margin-top:14px;padding:0 2px}
.plan6 .pf span{font:500 13.5px Inter,sans-serif;color:#6d6874}
.plan6 .pf b{font:400 26px 'DM Serif Display',serif;color:#141216}
.plan6 .pn{font:400 12px Inter,sans-serif;color:#8e8a95;margin-top:6px;padding:0 2px}
.seg img{border-radius:0!important;object-fit:contain}
.ban6 .ai img{object-fit:contain}
`;
})();

/* Oct 27 sweep: generic, est.-labelled desk chatter and tile tasks (no specific program facts) */
(function(){var C=window.CFG;var G=['Checking current terms','Logging new rules','Comparing points and cash','Watching for bonuses','Nightly data sync','Reviewing award pricing','Strategy review','Checking credits'];
for(var k in C.tasks){var n=+k;C.tasks[k]=[0,1,2,3,4].map(function(j){return G[(n+j*3)%G.length]})}
var T=['Checking current terms.','Comparing points and cash, est.','Reviewing award pricing, est.','Watching for a bonus.','Logging new rules.','Checking a trip quote, est.','Reviewing a spend split, est.','Nightly data sync.'];
C.chatter=C.chatter.map(function(c,i){return [c[0],c[1],T[i%T.length]]});})();
/* Oct 27 fold round: no circles (rounded squares), chevron on transparent, no chip */
window.CFG.css+=`
.pav6{border-radius:14px!important}.pav6 .em{border-radius:6px!important}
#pav>div,#pav div{border-radius:9px!important}
.beat i{border-radius:8px!important}
.fo,#hero.M .fo{border-radius:0!important;box-shadow:none!important;background:transparent!important}
.fo img{border-radius:0!important;padding:6%!important;filter:drop-shadow(0 8px 14px rgba(230,15,134,.3))}
.mm .av{border-radius:8px!important}.mm .av.avfo{border-radius:0!important;box-shadow:none!important;background:transparent!important;object-fit:contain}
.a2a{display:none!important}
.kick .ld,.lv,.feed .fd,.feed10 .who .lv,.pend i:before{border-radius:2px!important}
`;
/* Oct 27 insights round: the specialists' dots resolve into example insights that rise to First Officer */
window.CFG.css+=`
.mm.f .b6{background:#FFF0F7!important;color:#141216!important;box-shadow:inset 0 0 0 1px rgba(250,24,150,.22)!important}
.mm.f .b6 .e{background:rgba(250,24,150,.12)!important;color:#b30d6a!important}
.mm.f .typ i{background:#FA1896!important}
.fol .l1{color:#141216!important}
.kick{color:#4A4550!important}
.mm .av.avfo{display:none!important}
.wk i{border-radius:1.5px!important}
.find .wk i{animation-duration:.6s!important;background:#FA1896!important}
.ins .wk{opacity:0!important;transition:opacity .3s}
.ins6{position:absolute;z-index:40;width:180px;transform:translate(-50%,-100%) scale(.86);transform-origin:50% 100%;opacity:0;background:#fff;border-radius:12px;padding:8px 11px 9px;box-shadow:0 0 0 1px rgba(20,18,22,.08),0 12px 26px -14px rgba(20,18,22,.35);transition:opacity .45s ease,transform .45s cubic-bezier(.2,.8,.2,1),translate 1s cubic-bezier(.2,.8,.2,1),box-shadow .4s ease;pointer-events:none;text-align:left}
.ins6 small{display:flex;align-items:center;gap:5px;font:600 9px/1 'JetBrains Mono',ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;color:#8e8a95}
.ins6 small:before{content:'';width:6px;height:6px;border-radius:2px;background:#FA1896;flex:none}
.ins6 b{display:block;font:600 12.5px/1.3 'DM Sans',sans-serif;color:#141216;margin-top:4px;text-wrap:balance}
.ins6.on{opacity:1;transform:translate(-50%,-100%) scale(1)}
.ins6.up{box-shadow:0 0 0 1.5px #FA1896,0 16px 30px -12px rgba(250,24,150,.45)}
.ins6.settle{opacity:.2;box-shadow:0 0 0 1px rgba(20,18,22,.08);transition:opacity .9s ease,box-shadow .6s ease}
.ins6.gone{opacity:0;transition:opacity .6s ease}
.ins6.m{width:166px;padding:7px 10px 8px}.ins6.m b{font-size:12px}
.fo{transition:scale .5s cubic-bezier(.2,.8,.2,1)}
.fo.glow{scale:1.08}
.fo.glow img{filter:drop-shadow(0 0 16px rgba(250,24,150,.8))!important}
`;
(function(){
var IN=['Ad spend could earn more on another card, est.','Two cards overlap on the same spend.','An unused travel credit is worth claiming.','Points may go further through a partner, est.','Cash may beat points on a short trip, est.','Software spend fits a bonus category, est.','Fees may be covered by credits, est.','Off-peak dates may price lower, est.','Points pooling could speed up the goal, est.','Carrier visits could earn travel points, est.','This bonus is worth a second look.'];
var qi=Math.floor(Math.random()*IN.length),live=[],started=0;
function W(ms){return new Promise(function(r){setTimeout(r,ms)})}
function ready(){var R=window.HROOT;if(!R)return null;var f=R.querySelector('.floor');var fo=R.querySelector('.fo');if(!f||!fo||!f.querySelector('[data-n] .wk'))return null;return {R:R,f:f,st:f.parentElement,fo:fo}}
function pick(E,mob){var vh=innerHeight,c=[].slice.call(E.f.querySelectorAll('[data-n]')).filter(function(t){
 if(/\b(rel|say|spk|ping|ins|find|lit)\b/.test(t.className)||!t.querySelector('.wk'))return false;
 var r=t.getBoundingClientRect();if(r.width<1||r.top<(mob?90:150)||r.bottom>vh-30)return false;
 var x=parseFloat(t.style.left)+r.width/2,y=parseFloat(t.style.top);
 for(var i=0;i<live.length;i++){if(Math.abs(live[i].x-x)<210&&Math.abs(live[i].y-y)<120)return false}
 var fx=parseFloat(E.fo.style.left),fy=parseFloat(E.fo.style.top);if(Math.abs(fx-x)<(mob?150:60)&&Math.abs(fy-y)<(mob?110:70))return false;
 return true});
 return c.length?c[Math.floor(Math.random()*c.length)]:null}
async function one(E,mob){var t=pick(E,mob);if(!t)return;var r=t.getBoundingClientRect();
 var x=parseFloat(t.style.left)+r.width/2,y=parseFloat(t.style.top)-6,SW=E.st.clientWidth||innerWidth,hw=(mob?166:180)/2+6;
 var cx=Math.max(hw,Math.min(SW-hw,x));var rec={x:x,y:y};live.push(rec);
 t.classList.add('find');await W(900);
 var c=document.createElement('div');c.className='ins6'+(mob?' m':'');c.innerHTML='<small>Example insight</small><b></b>';c.querySelector('b').textContent=IN[qi++%IN.length];
 c.style.left=cx+'px';c.style.top=y+'px';E.st.appendChild(c);t.classList.add('ins');
 await W(30);c.classList.add('on');await W(mob?1900:1700);
 var fs=E.fo.offsetWidth||60,fx=parseFloat(E.fo.style.left)+fs/2,fy=parseFloat(E.fo.style.top)+fs/2,dx=fx-cx,dy=fy-(y-30),L=Math.hypot(dx,dy)||1,m=Math.min(L*(mob?.45:.55),mob?70:150);
 c.style.translate=(dx/L*m).toFixed(1)+'px '+(dy/L*m).toFixed(1)+'px';c.classList.add('up');
 await W(650);E.fo.classList.add('glow');await W(700);E.fo.classList.remove('glow');
 c.classList.add('settle');t.classList.remove('find','ins');await W(mob?1400:1800);
 c.classList.add('gone');await W(650);c.remove();live.splice(live.indexOf(rec),1)}
async function loop(){var E;while(!(E=ready()))await W(300);await W(1200);
 while(true){var mob=innerWidth<760;E=ready()||E;
  if(!document.hidden&&live.length<(mob?2:3))one(E,mob);
  await W(mob?3600:1900)}}
loop();
})();
/* Oct 27 round 3: the desk-centre chevron is the hub of the desk, a white rounded-square tile (not a loose mark) */
window.CFG.css+=`
.fo{background:#fff!important;border-radius:24%!important;box-shadow:0 0 0 1.5px #F6C6DF,0 16px 30px -16px rgba(230,15,134,.5)!important}
.fo img{padding:20% 20% 18%!important;filter:none!important}
.fo.glow{box-shadow:0 0 0 2px #FA1896,0 0 26px rgba(250,24,150,.45)!important}
.fo.glow img{filter:none!important}
.seg img{display:none!important}
`;

/* Oct 27 round 4: the desk is its own band below the hero fold; the hub sits in the clearing at the centre of the program pods */
window.CFG.css+=`
.dband{position:absolute;z-index:0;border-radius:32px;background:rgba(255,253,249,.82);box-shadow:0 30px 60px -40px rgba(20,18,22,.35),0 0 0 1px rgba(250,24,150,.08);backdrop-filter:blur(6px)}
#hero.D h1{line-height:1.02}
#hero.M h1{line-height:1.04}
`;
