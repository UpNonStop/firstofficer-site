/* First Officer, recovered showcase. Shared behaviour for Home and Product. Mockup only, example data. */
(function(){
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};

/* nav */
var nav=$('.nav');function ns(){nav&&nav.classList.toggle('solid',scrollY>30)}addEventListener('scroll',ns,{passive:true});ns();
window.foNav=function(open){var sh=$('#sheet');if(!sh)return;sh.classList.toggle('open',open);document.body.classList.toggle('nolock',open);sh.setAttribute('aria-hidden',open?'false':'true');var b=$('.burger');b&&b.setAttribute('aria-expanded',open?'true':'false');$$('#sheet nav a').forEach(function(a,i){a.style.transitionDelay=open?(80+i*40)+'ms':'0ms'})};
addEventListener('keydown',function(e){if(e.key==='Escape')foNav(false)});

/* reveal on view */
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);e.target.dispatchEvent(new CustomEvent('inview'))}})},{threshold:.18,rootMargin:'0px 0px -6% 0px'});
$$('.reveal,.brush,[data-io]').forEach(function(el){io.observe(el)});
/* out of view: a section's endless loops pause (.is-off, assets/fo-rules.css), and so does the header ticker */
var off=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('is-off',!e.isIntersecting)})},{rootMargin:'150px 0px'});
$$('main>section').forEach(function(s){off.observe(s)});
function tickOff(){var h=document.getElementById('fo-header'),k=h&&h.shadowRoot&&h.shadowRoot.querySelector('.tick'),tr=k&&k.querySelector('.tr');if(!tr)return;
  new IntersectionObserver(function(es){tr.style.animationPlayState=es[es.length-1].isIntersecting?'':'paused'}).observe(k)}
if(document.readyState==='loading')addEventListener('DOMContentLoaded',tickOff);else tickOff();

/* count-up, easeOutQuart */
function fmt(n,d){return n.toLocaleString('en-US',{minimumFractionDigits:d||0,maximumFractionDigits:d||0})}
function countTo(el,to,ms,delay){if(!el)return;var d=+(el.dataset.dec||0),pre=el.dataset.pre||'',suf=el.dataset.suf||'';
  if(RM){el.textContent=pre+fmt(to,d)+suf;el.classList.add('landed');return}
  el.classList.remove('landed');el.textContent=pre+fmt(0,d)+suf;
  setTimeout(function(){var t0=performance.now();(function s(t){var p=Math.min((t-t0)/ms,1);el.textContent=pre+fmt(to*(1-Math.pow(1-p,4)),d)+suf;if(p<1)requestAnimationFrame(s);else el.classList.add('landed')})(t0)},delay||0)}
window.FOcount=countTo;
$$('[data-count]').forEach(function(el){var host=el.closest('[data-io]')||el;if(host===el)io.observe(el);host.addEventListener('inview',function(){countTo(el,+el.dataset.count,1600,+(el.dataset.delay||0))})});

/* confetti: pink and cream, canvas, short */
var PAL=[['#FA1896',6],['#E60F86',4],['#FBD3EA',5],['#FBF4E6',3],['#FFF8E1',2]];
var BAG=[];PAL.forEach(function(p){for(var i=0;i<p[1];i++)BAG.push(p[0])});var CREAM={'#FBF4E6':1,'#FFF8E1':1};
function confetti(host,o){if(RM||!host)return;o=Object.assign({x:.5,y:.36,count:70,spread:70,speed:10,rain:28},o||{});
  var c=document.createElement('canvas');c.className='fx';host.appendChild(c);var W=host.clientWidth,H=host.clientHeight,d=Math.min(devicePixelRatio||1,2);
  c.width=W*d;c.height=H*d;var g=c.getContext('2d');g.scale(d,d);var ox=o.x*W,oy=o.y*H,P=[],sc=W/300;
  function add(n,t0,pow){for(var i=0;i<n;i++){var a=(-90+(Math.random()*2-1)*o.spread)*Math.PI/180,s=o.speed*sc*pow*(.55+Math.random()*.6),r=Math.random();
    P.push({x:ox+(Math.random()-.5)*30,y:oy,vx:Math.cos(a)*s,vy:Math.sin(a)*s,t0:t0,life:1500+Math.random()*700,rot:Math.random()*6.28,vr:(Math.random()-.5)*.18,flip:Math.random()*6.28,vf:.08+Math.random()*.1,shape:r<.6?'r':r<.84?'d':'s',w:(7+Math.random()*4)*sc,h:(2.6+Math.random()*1.6)*sc,col:BAG[(Math.random()*BAG.length)|0],gr:.2*sc})}}
  function rain(n,t0){for(var i=0;i<n;i++){P.push({x:Math.random()*W,y:-12-Math.random()*60,vx:(Math.random()-.5),vy:(1.4+Math.random()*1.4)*sc,t0:t0+Math.random()*320,life:1900+Math.random()*500,rot:Math.random()*6.28,vr:(Math.random()-.5)*.08,flip:Math.random()*6.28,vf:.05+Math.random()*.07,shape:Math.random()<.7?'r':'s',w:(8+Math.random()*4)*sc,h:(3+Math.random()*1.4)*sc,col:BAG[(Math.random()*BAG.length)|0],gr:.035*sc})}}
  rain(o.rain,120);add(o.count,0,1);add(Math.round(o.count*.4),260,.8);var st=performance.now();
  (function tk(now){var t=now-st,alive=0;g.clearRect(0,0,W,H);P.forEach(function(p){var age=t-p.t0;if(age<0){alive++;return}if(age>p.life)return;alive++;
    p.vx*=.982;p.vy=p.vy*.982+p.gr;p.x+=p.vx+Math.sin(age/180+p.flip)*.35;p.y+=p.vy;p.rot+=p.vr;p.flip+=p.vf;var k=age/p.life;
    g.save();g.globalAlpha=k<.65?1:1-(k-.65)/.35;g.translate(p.x,p.y);g.rotate(p.rot);g.fillStyle=p.col;
    if(p.shape==='r'){g.scale(1,Math.cos(p.flip));g.fillRect(-p.w/2,-p.h/2,p.w,p.h)}
    else if(p.shape==='d'){g.beginPath();g.arc(0,0,p.h*.85,0,6.283);g.fill()}
    else{var s=p.h*1.5;g.beginPath();g.moveTo(0,-s);g.quadraticCurveTo(0,0,s,0);g.quadraticCurveTo(0,0,0,s);g.quadraticCurveTo(0,0,-s,0);g.quadraticCurveTo(0,0,0,-s);g.fill()}
    if(CREAM[p.col]){g.strokeStyle='#E3C877';g.lineWidth=.8;g.stroke()}g.restore()});
    if(alive&&t<3400&&document.body.contains(c))requestAnimationFrame(tk);else c.remove()})(st)}
window.FOconfetti=confetti;

/* celebration phones */
$$('.cel').forEach(function(cel){
  var scr=$('.scr',cel),slides=$$('.cs',cel),navb=cel.parentElement.querySelector('.celnav'),btns=navb?$$('button',navb):[],i=-1,tm=null,started=false,dur=+(cel.dataset.dur||6200);
  function show(n){i=(n+slides.length)%slides.length;slides.forEach(function(s,k){s.classList.toggle('on',k===i)});btns.forEach(function(b,k){b.classList.remove('on');void b.offsetWidth;if(k===i){b.style.setProperty('--dur',dur+'ms');b.classList.add('on')}});
    var s=slides[i];$$('[data-to]',s).forEach(function(el){countTo(el,+el.dataset.to,700,120)});if(s.dataset.confetti)setTimeout(function(){confetti(scr,{y:.3})},380);
    clearTimeout(tm);if(cel.dataset.auto!=='0'&&slides.length>1)tm=setTimeout(function w(){if(document.documentElement.classList.contains('fo-still')){tm=setTimeout(w,800);return}show(i+1)},dur)}
  btns.forEach(function(b,k){b.addEventListener('click',function(){show(k)})});
  scr.addEventListener('click',function(){show(slides.length>1?i+1:0)});
  var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!started){started=true;setTimeout(function(){show(0)},+(cel.dataset.delay||0))}})},{threshold:.4});o.observe(cel);
});

/* greeting follows the visitor's time of day */
var hr=new Date().getHours(),q=new URLSearchParams(location.search);if(q.has('h'))hr=+q.get('h');
var part=hr<12?'am':hr<17?'pm':'eve';
$$('img[data-greet]').forEach(function(im){im.src=im.dataset.greet.replace('{p}',part)});

/* share card toggle */
$$('.tgl').forEach(function(t){t.addEventListener('click',function(){t.classList.toggle('on');var c=t.closest('.wc');$$('[data-amt]',c).forEach(function(a){a.textContent=t.classList.contains('on')?a.dataset.hid:a.dataset.amt})})});

/* home: Leo arc rail */
var beats=$$('.beat');if(beats.length){var rl=$$('.rail a'),ml=$$('.mrail a'),prog=$('.rail .prog i');
  function act(id){rl.concat(ml).forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+id)});var m=$('.mrail a.on');if(m&&m.parentElement){var p=m.parentElement;p.scrollTo({left:m.offsetLeft-20,behavior:'smooth'})}}
  var bo=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)act(e.target.id)})},{rootMargin:'-45% 0px -50% 0px'});beats.forEach(function(b){bo.observe(b)});
  addEventListener('scroll',function(){if(!prog)return;var a=beats[0].getBoundingClientRect().top,z=beats[beats.length-1].getBoundingClientRect().bottom,h=innerHeight*.5;prog.style.width=Math.max(0,Math.min(100,(h-a)/(z-a)*100))+'%'},{passive:true});}

/* mobile sticky CTA after the hero */
var mc=$('.mcta'),top=$('#top')||$('.phead');if(mc&&top){var up=function(){var b=top.getBoundingClientRect().bottom,f=$('.ctab');var nearEnd=f&&f.getBoundingClientRect().top<innerHeight;mc.classList.toggle('show',!nearEnd)};addEventListener('scroll',up,{passive:true});up()}

/* product: pillar tour */
var tt=$('.ttabs');if(tt){var tb=$$('button',tt),panes=$$('.tpane'),imgs=$$('.tour .scr img'),ti=0,tto=null,TD=7000,tstarted=false;
  function tshow(n){ti=(n+tb.length)%tb.length;tb.forEach(function(b,k){b.classList.remove('on');void b.offsetWidth;b.setAttribute('aria-selected',k===ti?'true':'false');b.tabIndex=k===ti?0:-1;if(k===ti){b.style.setProperty('--dur',TD+'ms');b.classList.add('on')}});
    panes.forEach(function(p,k){p.classList.toggle('on',k===ti)});imgs.forEach(function(im,k){im.style.opacity=k===ti?1:0;im.style.transform=k===ti?'none':'scale(1.03)'});
    $$('[data-to]',panes[ti]).forEach(function(el){countTo(el,+el.dataset.to,1200,100)});clearTimeout(tto);if(!tt.classList.contains('held'))tto=setTimeout(function w(){if(document.documentElement.classList.contains('fo-still')){tto=setTimeout(w,800);return}tshow(ti+1)},TD)}
  tb.forEach(function(b,k){b.addEventListener('click',function(){tt.classList.add('held');tshow(k)});b.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:e.key==='Home'?-k:e.key==='End'?tb.length-1-k:0;if(!d)return;e.preventDefault();tt.classList.add('held');tshow(k+d);tb[ti].focus()})});
  new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!tstarted){tstarted=true;tshow(0)}})},{threshold:.3}).observe(tt.closest('section'));}

/* product: the desk. No lines. Programs think, rise toward the chevron, light up, settle back */
var desk=$('.desk');if(desk){
  var SP=[['Cards','e'],['Airlines','b'],['Hotels','b'],['Transfers','b'],['Award charts','b'],['The ledger','r'],['Program watch','l'],['Trips','b']];
  var core=$('.core',desk),qel=$('.q',desk),ael=$('.a',desk),steps=$$('.steps li');
  var els=SP.map(function(s){var d=document.createElement('div');d.className='sp';d.innerHTML='<div class="dots"><u></u><u></u><u></u></div><div class="t"><i></i>'+s[0]+'</div>';desk.appendChild(d);return d});
  function layout(){var W=desk.clientWidth,H=desk.clientHeight,mob=W<560;
    els.forEach(function(d,k){var x,y;
      if(!mob){var a=(-180+k*(360/SP.length)+22.5)*Math.PI/180;x=W/2+Math.cos(a)*W*.36;y=H/2+Math.sin(a)*H*.3}
      else{var col=k%2,row=Math.floor(k/2);x=W*(col?.78:.22);y=H*[.25,.37,.63,.75][row]}
      d.dataset.x=x;d.dataset.y=y;d.style.left=x+'px';d.style.top=y+'px'})}
  layout();addEventListener('resize',layout);
  var Q=window.FO_DESK_Q||[
    {s:0,q:['Leo, Linden Row','Which card should our ad spend go on?'],who:[0,6,5],a:['First Officer','Move lead-gen ads to the 4x card. About $7,200 a year, est. Want me to set it up?']},
    {s:4,q:['Leo, Linden Row','Can we get to Tokyo in business next spring?'],who:[1,4,3],a:['First Officer','You are 32% there. On pace for March 2027, est. When you pick dates, the desk vets them and books after you approve.']},
    {s:3,q:['Leo, Linden Row','What did last week bring in?'],who:[5,0,2],a:['First Officer','$1,860 across 3 findings, checked against your statements. Est.']},
    {s:1,q:['Leo, Linden Row','What is one of my points actually worth?'],who:[6,3,4],a:['First Officer','About 1¢ as cash back. On your Tokyo flights, 5¢ or more. Your 2 minute lesson is ready. Est.']}
  ];
  var qi=0,timers=[];function T(f,ms){timers.push(setTimeout(f,ms))}
  function clear(){timers.forEach(clearTimeout);timers=[];els.forEach(function(d){d.className='sp';d.style.transform='translate(-50%,-50%)'});core.classList.remove('lit');qel.classList.remove('on');ael.classList.remove('on')}
  function run(){clear();var c=Q[qi%Q.length];qi++;steps.forEach(function(s,k){s.classList.toggle('on',k===c.s)});
    qel.innerHTML='<small>'+c.q[0]+'</small>'+c.q[1];ael.innerHTML='<small>'+c.a[0]+'</small>'+c.a[1];
    T(function(){qel.classList.add('on')},200);
    T(function(){els.forEach(function(d,k){if(c.who.indexOf(k)<0)d.classList.add('dim')})},900);
    c.who.forEach(function(k,j){var d=els[k];
      T(function(){d.classList.add('think')},1100+j*350);
      T(function(){var cx=desk.clientWidth/2,cy=desk.clientHeight/2,f=desk.clientWidth<560?.2:.42,dx=(cx-d.dataset.x)*f,dy=(cy-d.dataset.y)*f;d.classList.remove('think');d.classList.add('lit');d.style.transform='translate(calc(-50% + '+dx+'px),calc(-50% + '+dy+'px))'},2700+j*450);
      T(function(){d.classList.remove('lit');d.style.transform='translate(-50%,-50%)'},4700+j*250)});
    T(function(){core.classList.add('lit')},3300);
    T(function(){ael.classList.add('on')},4500);
    T(function(){core.classList.remove('lit');els.forEach(function(d){d.classList.remove('dim')})},6400);
    T(function w(){if(document.documentElement.classList.contains('fo-still')){T(w,800);return}run()},8600)}
  steps.forEach(function(s,k){s.addEventListener('click',function(){var n=Q.findIndex(function(c){return c.s===k});if(n>=0){qi=n;run()}})});
  var dstarted=false;new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!dstarted){dstarted=true;run()}})},{threshold:.3}).observe(desk);
}
})();

/* hero photo field: dozens of low-opacity photos crossfading behind the approved hero */
(function(){var top=document.getElementById('top');if(!top||top.querySelector('.mbg'))return;var N=31,box=document.createElement('div');box.className='rbg';box.setAttribute('aria-hidden','true');
  var a=document.createElement('i'),b=document.createElement('i');box.appendChild(a);box.appendChild(b);top.insertBefore(box,top.firstChild);
  var order=[];for(var k=0;k<N;k++)order.push(k);order.sort(function(){return Math.random()-.5});var n=0,cur=a;
  function src(k){return (window.FO_A||'')+'img/rec/bg/'+(k<10?'0':'')+k+'.webp'}
  function next(){var k=order[n%N];n++;var im=new Image();im.onload=function(){var nx=cur===a?b:a;nx.style.backgroundImage='url('+im.src+')';nx.classList.add('on');cur.classList.remove('on');cur=nx};im.src=src(k)}
  next();setInterval(next,5200);
})();
