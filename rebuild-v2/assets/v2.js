/* First Officer rebuild v2 · motion layer (vanilla, no deps) */
(function(){
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var Q=new URLSearchParams(location.search), SNAP=Q.has('snap');
function $(s,r){return (r||document).querySelector(s)}function $$(s,r){return [].slice.call((r||document).querySelectorAll(s))}
function fmt(n,d){return d?n.toFixed(d):Math.round(n).toLocaleString('en-US')}
/* rotating photo layers */
$$('.phx').forEach(function(box){
  var list=(box.getAttribute('data-ph')||'').split(',').filter(Boolean);if(!list.length)return;
  var imgs=[],i=0,t=null,loaded=false,iv=+(box.getAttribute('data-iv')||7000);
  function load(){if(loaded)return;loaded=true;
    list.forEach(function(src,k){var im=new Image();im.decoding='async';im.alt='';if(k>1)im.loading='lazy';im.src=src;if(k===0)im.className='on';box.appendChild(im);imgs.push(im)});}
  function step(){if(imgs.length<2)return;var a=imgs[i];i=(i+1)%imgs.length;var b=imgs[i];b.classList.remove('on');void b.offsetWidth;b.classList.add('on');setTimeout(function(){a.classList.remove('on')},2300);}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){load();if(!RM&&!SNAP&&!t)t=setInterval(step,iv)}else if(t){clearInterval(t);t=null}})},{rootMargin:'300px 0px'});
  io.observe(box);
});
/* count-ups */
function countUp(el){if(el._cu)return;el._cu=1;var to=+el.getAttribute('data-cu'),d=+(el.getAttribute('data-d')||0),pre=el.getAttribute('data-pre')||'',suf=el.getAttribute('data-suf')||'',dur=+(el.getAttribute('data-ms')||1600);
  if(RM||SNAP){el.textContent=pre+fmt(to,d)+suf;return}
  var from=+(el.getAttribute('data-from')||0),t0=performance.now();
  (function f(t){var p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);el.textContent=pre+fmt(from+(to-from)*e,d)+suf;if(p<1)requestAnimationFrame(f)})(t0);}
window.FOcount=function(root){$$('[data-cu]',root).forEach(function(el){el._cu=0;countUp(el)})};
/* reveal */
var rio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var el=e.target;el.classList.add('in');if(el.classList.contains('sc')||el.hasAttribute('data-go'))el.classList.add('go');$$('[data-cu]',el).forEach(countUp);if(el.hasAttribute('data-cu'))countUp(el);rio.unobserve(el)}})},{threshold:.18,rootMargin:'0px 0px -6% 0px'});
$$('[data-rv],[data-io],.sc,[data-go]').forEach(function(el){rio.observe(el)});
if(SNAP){$$('[data-rv],[data-io],.sc,[data-go]').forEach(function(el){el.classList.add('in');if(el.classList.contains('sc')||el.hasAttribute('data-go'))el.classList.add('go');$$('[data-cu]',el).forEach(countUp)})}
/* spend dial */
var dl=$('#dial');if(dl){var r=$('.rng',dl),C=2*Math.PI*92;
  function upd(){var v=+r.value,p=(v-10000)/(140000)*100;r.style.setProperty('--p',p+'%');
    var y=v*12*2.1*.85*.026,f=y*.6,h=y*.3,o=y*.1;$('#spv').textContent='$'+fmt(v);$('#yv').textContent='$'+fmt(y);
    $('#fv').textContent='$'+fmt(f);$('#hv').textContent='$'+fmt(h);$('#ov').textContent='$'+fmt(o);
    var full=Math.min(1,y/84000)*.999,segs=[[f,'#a1'],[h,'#a2'],[o,'#a3']],acc=0;
    segs.forEach(function(s){var len=s[0]/y*full*C;var a=$(s[1],dl);a.setAttribute('stroke-dasharray',len+' '+(C-len));a.setAttribute('stroke-dashoffset',-acc);acc+=len});
    $('#b1',dl).style.width=(f/y*100)+'%';$('#b2',dl).style.width=(h/y*100)+'%';$('#b3',dl).style.width=(o/y*100)+'%';}
  r.addEventListener('input',upd);upd();
  if(!RM&&!SNAP){var demo=new IntersectionObserver(function(es){if(es[0].isIntersecting){demo.disconnect();var t0=performance.now(),v0=10000,v1=35000;(function f(t){var p=Math.min(1,(t-t0)/1600),e=1-Math.pow(1-p,3);r.value=Math.round((v0+(v1-v0)*e)/500)*500;upd();if(p<1)requestAnimationFrame(f)})(t0)}},{threshold:.4});demo.observe(dl)}}
/* whatsapp phone loop */
var wac=$('.wac');if(wac&&window.FO_CHAT){var C2=window.FO_CHAT,ix=0;
  function bub(l){var d=document.createElement('div');d.className='bub'+(l[0]==='out'?' out':'');d.innerHTML=(l[1]?'<span class="who">'+l[1]+'</span>':'')+l[2];wac.appendChild(d);var bs=$$('.bub',wac);while(bs.length>5){bs.shift().remove()}}
  function conv(){var c=C2[ix%C2.length];ix++;var k=0;(function nx(){if(k>=c.length){setTimeout(conv,2600);return}var l=c[k++];if(l[0]==='in'&&!RM){var ty=document.createElement('div');ty.className='bub typing';ty.innerHTML='<i></i><i></i><i></i>';wac.appendChild(ty);setTimeout(function(){ty.remove();bub(l);setTimeout(nx,1500)},900)}else{bub(l);setTimeout(nx,1300)}})()}
  C2[C2.length-1].forEach(bub);C2[0].forEach(bub);ix=1;if(!RM&&!SNAP)setTimeout(conv,2200);}
/* featured fomo story: cycles cities */
var ft=$('#feat');if(ft&&window.FO_FEAT){var F=window.FO_FEAT,fi=0,ftm=null;var tabs=$$('.ftabs button',ft);
  function show(i){fi=i;var d=F[i];tabs.forEach(function(b,k){b.classList.toggle('on',k===i)});
    var img=$('.fsp img',ft);ft.classList.remove('go');img.style.opacity=.0;
    setTimeout(function(){img.src=d.img;img.alt=d.city;$('.fcity b',ft).textContent=d.city;$('.fcity span',ft).textContent=d.tag;
      var pts=$('#fpts'),u=$('#fu'),k=$('#fk'),m=$('#fm');pts.setAttribute('data-cu',d.pts);u.setAttribute('data-cu',d.usual);k.setAttribute('data-cu',d.desk);m.setAttribute('data-cu',d.x);
      $('#fus').textContent=d.us;$('#fks').textContent=d.ks;$('#ftx').textContent=d.tx;
      $('#fub').style.setProperty('--w',(d.usual/d.desk*100)+'%');
      img.style.opacity=1;void ft.offsetWidth;ft.classList.add('go');FOcount(ft);},SNAP?0:420);}
  tabs.forEach(function(b,k){b.addEventListener('click',function(){clearInterval(ftm);ftm=null;show(k)})});
  var fio=new IntersectionObserver(function(es){if(es[0].isIntersecting){fio.disconnect();show(0);if(!RM&&!SNAP)ftm=setInterval(function(){show((fi+1)%F.length)},6500)}},{threshold:.3});fio.observe(ft);}
/* deck carousel */
var tr=$('#track');if(tr){var cnt=$('#dcnt'),pr=$('#dprog');var n=$$('.sc',tr).length;
  function pos(){var w=tr.firstElementChild.getBoundingClientRect().width+22;var i=Math.round(tr.scrollLeft/w);if(cnt)cnt.textContent=String(Math.min(n,i+1)).padStart(2,'0')+' / '+n;if(pr){var vis=tr.clientWidth/w;pr.style.width=(vis/n*100)+'%';pr.style.transform='translateX('+(tr.scrollLeft/(tr.scrollWidth)*100/(vis/n*100)*100)+'%)'}}
  tr.addEventListener('scroll',pos,{passive:true});pos();
  $$('[data-dir]').forEach(function(b){b.addEventListener('click',function(){var w=tr.firstElementChild.getBoundingClientRect().width+22;tr.scrollBy({left:w*(+b.getAttribute('data-dir')),behavior:'smooth'})})});
  var mb=$('#dmore');if(mb)mb.addEventListener('click',function(){$('#deck').classList.add('deck-open');mb.remove();$$('.sc.more').forEach(function(s){rio.observe(s)})});}
/* pillars orbit */
var orb=$('#orb');if(orb){var P=$$('.pc2',orb),T=$$('.ptabs button',orb),N=$$('.node',orb),pi=0,pt=null;
  function ps(i){pi=i;P.forEach(function(p,k){p.classList.toggle('on',k===i)});T.forEach(function(b,k){b.classList.toggle('on',k===i);b.style.animation='none';void b.offsetWidth;b.style.animation=''});
    N.forEach(function(nd,k){var c=nd.querySelector('circle');c.setAttribute('r',k===i?58:44);c.setAttribute('fill',k===i?nd.getAttribute('data-c'):'#fff');nd.querySelector('text').setAttribute('fill',k===i?'#fff':nd.getAttribute('data-c'))});
    var arc=$('#oarc');if(arc){var L=2*Math.PI*170;arc.setAttribute('stroke-dasharray',(L*(i+1)/4)+' '+L);arc.setAttribute('stroke',N[i].getAttribute('data-c'))}}
  function go(i){clearInterval(pt);ps(i);if(!RM&&!SNAP)pt=setInterval(function(){ps((pi+1)%4)},6000)}
  T.forEach(function(b,k){b.addEventListener('click',function(){go(k)})});N.forEach(function(nd,k){nd.addEventListener('click',function(){go(k)})});go(0);}
/* book console */
var bc=$('#console');if(bc){var opts=$$('.opt[data-p]',bc);
  function setStep(n){$$('.steps .s',bc).forEach(function(s,k){s.classList.toggle('on',k===n-1);s.classList.toggle('done',k<n-1)});$$('.steps .ln',bc).forEach(function(l,k){l.classList.toggle('on',k<n-1)})}
  opts.forEach(function(o){o.addEventListener('click',function(){opts.forEach(function(x){x.classList.toggle('on',x===o);x.setAttribute('aria-pressed',x===o)});$$('.pane',bc).forEach(function(p){p.classList.toggle('on',p.id===o.getAttribute('data-p'))});setStep(o.getAttribute('data-p')==='p-wa'?2:2)})});
  $$('.mode .opt',bc).forEach(function(o){o.addEventListener('click',function(){$$('.mode .opt',bc).forEach(function(x){x.classList.toggle('on',x===o)});$$('.mnote',bc).forEach(function(m){m.style.display=m.getAttribute('data-m')===o.getAttribute('data-m')?'block':'none'});setStep(3);var ph=$('#phf');if(ph)ph.style.display=o.getAttribute('data-m')==='phone'?'block':'none'})});}
/* dental calculator */
var dc=$('#dcalc');if(dc){var rs=$$('input[type=range]',dc);
  function cu(){var pts=0,sp=0,pl=[];rs.forEach(function(r){var v=+r.value,x=+r.getAttribute('data-x');pts+=v*x;sp+=v;pl.push(v*x);r.style.setProperty('--p',((v-r.min)/(r.max-r.min)*100)+'%');r.closest('.cl').querySelector('.v').textContent='$'+fmt(v)});
    rs.forEach(function(r,k){var b=r.closest('.cl').querySelector('.pb i');if(b)b.style.width=(pts?pl[k]/pts*100:0)+'%'});
    /* live formula: monthly net = points x 0.01836 - 550 (3.0 cents x 85% redeemed x 72% honest discount, minus the fee) */
    var net=pts*0.01836-550;$('#dpts').textContent=fmt(pts);$('#dnet').textContent=(net<0?'-$':'$')+fmt(Math.abs(net));$('#dyr').textContent=(net<0?'-$':'$')+fmt(Math.abs(net*12));$('#dsp').textContent='$'+fmt(sp);var bl=$('#dbl');if(bl)bl.textContent=(sp?pts/sp:0).toFixed(1)+'x'}
  rs.forEach(function(r){r.addEventListener('input',cu)});cu();}
})();
/* sticky mobile CTA: never sits on top of content. It shows only over empty
   section space and hides while any text, figure, card, image or control is under it. */
(function(){var m=document.querySelector('.mcta');if(!m)return;
  if(/book\.html/.test(location.pathname)){m.classList.add('mhide');return}
  var W=function(){return window.innerWidth},pend=false;
  function own(e){for(var n=e.firstChild;n;n=n.nextSibling)if(n.nodeType===3&&n.textContent.trim())return true;return false}
  function solid(e){var s=getComputedStyle(e);if(s.backgroundImage!=='none')return true;var c=s.backgroundColor.match(/[\d.]+/g);return c&&(c.length<4||+c[3]>0.05)}
  function hit(x,y){var st=document.elementsFromPoint(x,y);
    for(var i=0;i<st.length;i++){var e=st[i];if(m.contains(e)||e.closest('.phx,header'))continue;
      if(/^(HTML|BODY|MAIN|SECTION)$/.test(e.tagName))continue;
      if(own(e))return true;
      if(e.getBoundingClientRect().width>=W()*.96)continue;
      if(/^(IMG|SVG|svg|CANVAS|INPUT|BUTTON|VIDEO|path|rect|circle|text)$/.test(e.tagName)||solid(e))return true}
    return false}
  function chk(){pend=false;if(W()>760){m.classList.remove('mhide');return}
    var h=m.offsetHeight,H=window.innerHeight,r={left:12,width:W()-24,top:H-12-h,height:h,bottom:H-12};
    var cov=false,xs=[.08,.3,.5,.7,.92],ys=[r.top-6,r.top+r.height/2,r.bottom];
    for(var a=0;a<xs.length&&!cov;a++)for(var b=0;b<ys.length&&!cov;b++)cov=hit(r.left+r.width*xs[a],ys[b]);
    m.classList.toggle('mhide',cov)}
  function q(){if(!pend){pend=true;requestAnimationFrame(chk)}}
  addEventListener('scroll',q,{passive:true});addEventListener('resize',q);setInterval(q,700);q();
})();
