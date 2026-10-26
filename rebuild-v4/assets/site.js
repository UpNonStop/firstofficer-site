/* First Officer rebuild v3 · behaviour layer (vanilla, adapted from v2.js for the app-style markup) */
(function(){
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var Q=new URLSearchParams(location.search), SNAP=Q.has('snap');
function $(s,r){return (r||document).querySelector(s)}function $$(s,r){return [].slice.call((r||document).querySelectorAll(s))}
function fmt(n,d){return d?n.toFixed(d):Math.round(n).toLocaleString('en-US')}
/* calm rotating photo layers */
/* time-of-day photo sets: the visitor's local hour picks which existing photos lead (dawn/day/dusk/night) */
var TOD={dawn:'bg-01 bg-07 d-connemara d-santorini e-coffee e-window i-trip-santorini',dusk:'bg-07 d-dubai d-paris d-santorini e-window i-trip-santorini d-rome',night:'d-nyc d-rome d-dubai d-paris'};
var HR=new Date().getHours(),TB=HR>=5&&HR<8?'dawn':HR>=17&&HR<20?'dusk':(HR>=20||HR<5)?'night':'day';document.documentElement.setAttribute('data-tod',TB);
function todSort(list){if(TB==='day'){var nd=(TOD.night+' '+TOD.dusk).split(' ');var a=list.filter(function(s){return nd.indexOf(s.split('/').pop().replace('.webp',''))<0});return a.length>=2?a.concat(list.filter(function(s){return a.indexOf(s)<0})):list}
  var w=TOD[TB].split(' '),m=list.filter(function(s){return w.indexOf(s.split('/').pop().replace('.webp',''))>=0});return m.length>=2?m.concat(list.filter(function(s){return m.indexOf(s)<0})):list}
$$('.phx').forEach(function(box){
  var list=todSort((box.getAttribute('data-ph')||'').split(',').filter(Boolean));if(!list.length)return;
  var imgs=[],i=0,t=null,loaded=false,iv=+(box.getAttribute('data-iv')||8000);
  function load(){if(loaded)return;loaded=true;
    list.forEach(function(src,k){var im=new Image();im.decoding='async';im.alt='';if(k>1)im.loading='lazy';im.src=src;if(k===0)im.className='on';box.appendChild(im);imgs.push(im)});}
  function step(){if(imgs.length<2)return;var a=imgs[i];i=(i+1)%imgs.length;var b=imgs[i];b.classList.remove('on');void b.offsetWidth;b.classList.add('on');setTimeout(function(){a.classList.remove('on')},2300);}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){load();if(!RM&&!SNAP&&!t)t=setInterval(step,iv)}else if(t){clearInterval(t);t=null}})},{rootMargin:'300px 0px'});
  io.observe(box);
});
/* count-ups (app: 1200ms ease-out) */
function countUp(el){if(el._cu)return;el._cu=1;var to=+el.getAttribute('data-cu'),d=+(el.getAttribute('data-d')||0),pre=el.getAttribute('data-pre')||'',suf=el.getAttribute('data-suf')||'',dur=+(el.getAttribute('data-ms')||1200);
  var dg=el.parentElement&&el.parentElement.hasAttribute('data-dg');
  function fin(){var s=pre+fmt(to,d)+suf;if(dg){var m=s.match(/^(.*?),(\d{3})$/);if(m){el.textContent=m[1];var g=document.createElement('span');g.className='dg';g.textContent=',';el.appendChild(g);el.appendChild(document.createTextNode(m[2]));return}}el.textContent=s}
  if(RM||SNAP){fin();return}
  var t0=performance.now();
  (function f(t){var p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);if(p<1){el.textContent=pre+fmt(to*e,d)+suf;requestAnimationFrame(f)}else fin()})(t0);}
window.FOcount=function(root){$$('[data-cu]',root).forEach(function(el){el._cu=0;countUp(el)})};
/* reveal */
var SEL='[data-rv],.ptile,.cmp,.meter,.tl';
var rio=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var el=e.target;el.classList.add('in');$$('[data-cu]',el).forEach(countUp);if(el.hasAttribute('data-cu'))countUp(el);rio.unobserve(el)}})},{threshold:.15,rootMargin:'0px 0px -5% 0px'});
$$(SEL).forEach(function(el){rio.observe(el)});
$$('main [data-cu]').forEach(function(el){rio.observe(el)});
if(SNAP){$$(SEL).forEach(function(el){el.classList.add('in')});$$('[data-cu]').forEach(countUp)}
/* home: what the spend buys */
var dl=$('#dial');if(dl){var r=$('.rng',dl),ms=$$('.meter i',dl);
  function upd(){var v=+r.value,p=(v-10000)/(140000)*100;r.style.setProperty('--p',p+'%');
    var y=v*12*2.1*.85*.026,f=y*.6,h=y*.3,o=y*.1;$('#spv').textContent='$'+fmt(v);$('#yv').textContent='$'+fmt(y);
    $('#fv').textContent='$'+fmt(f);$('#hv').textContent='$'+fmt(h);$('#ov').textContent='$'+fmt(o);}
  r.addEventListener('input',upd);upd();
  if(!RM&&!SNAP){var demo=new IntersectionObserver(function(es){if(es[0].isIntersecting){demo.disconnect();var t0=performance.now(),v0=10000,v1=35000;(function f(t){var p=Math.min(1,(t-t0)/1200),e=1-Math.pow(1-p,3);r.value=Math.round((v0+(v1-v0)*e)/500)*500;upd();if(p<1)requestAnimationFrame(f)})(t0)}},{threshold:.4});demo.observe(dl)}}
/* desk thread loop */
var SC={'Strategist':'var(--earn)','Optioneer':'var(--burn)','Desk':'var(--gold2)','Capture Report':'var(--s-analyst)'};
var wac=$('.wac');if(wac&&window.FO_CHAT){var C2=window.FO_CHAT,ix=0;
  function bub(l){var d=document.createElement('div');d.className='bub'+(l[0]==='out'?' out':'');if(l[1])d.style.setProperty('--c',SC[l[1]]||'var(--gold2)');d.innerHTML=(l[1]?'<span class="who">'+l[1]+'</span>':'')+l[2];wac.appendChild(d);var bs=$$('.bub',wac);while(bs.length>6){bs.shift().remove()}}
  function conv(){var c=C2[ix%C2.length];ix++;var k=0;(function nx(){if(k>=c.length){setTimeout(conv,2600);return}var l=c[k++];if(l[0]==='in'&&!RM){var ty=document.createElement('div');ty.className='bub typing';ty.innerHTML='<i></i><i></i><i></i>';wac.appendChild(ty);setTimeout(function(){ty.remove();bub(l);setTimeout(nx,1500)},900)}else{bub(l);setTimeout(nx,1300)}})()}
  C2[C2.length-1].forEach(bub);C2[0].forEach(bub);ix=1;if(!RM&&!SNAP)setTimeout(conv,2200);}
/* featured story: cycles cities */
var ft=$('#feat');if(ft&&window.FO_FEAT){var F=window.FO_FEAT,fi=0,ftm=null;var tabs=$$('.ftabs .chip',ft),card=$('.ptile',ft);
  function show(i){fi=i;var d=F[i];tabs.forEach(function(b,k){b.classList.toggle('on',k===i)});
    var img=$('#fimg');card.classList.remove('in');img.style.opacity=0;
    setTimeout(function(){img.src=d.img;img.alt=d.city;$('#fcity').textContent=d.city;$('#ftrip').textContent=d.tag+' · '+d.ks.replace(/, est\.$/,'');
      $('#fpts').setAttribute('data-cu',d.pts);$('#fu').setAttribute('data-cu',d.usual);var fc=$('#fc');if(fc)fc.setAttribute('data-cu',d.cash);
      var b0=$('#fimg0');if(b0)b0.src=d.img;if($('#fbu'))$('#fbu').textContent=fmt(d.usual);if($('#fbk'))$('#fbk').textContent=d.ks;if($('#fbp'))$('#fbp').textContent=fmt(d.pts);$('#fk').setAttribute('data-cu',d.desk);$('#fm').setAttribute('data-cu',d.x);
      $('#fks').textContent=d.ks;$('#ftx').textContent=d.tx;
      var nb=$('.cmp .nos .bar i',card)||$('.cmp .usual .bar i',card);nb.style.setProperty('--w',(d.usual/d.desk*100)+'%');var cb=$('.cmp .cbk .bar i',card);if(cb)cb.style.setProperty('--w',(d.cash/d.desk*100)+'%');
      img.style.opacity=1;void card.offsetWidth;card.classList.add('in');FOcount(card);},SNAP?0:380);}
  tabs.forEach(function(b,k){b.addEventListener('click',function(){clearInterval(ftm);ftm=null;show(k)})});
  var ba=$('.im.ba',ft),br=ba&&$('.bar-r',ba);if(br){var bset=function(){ba.style.setProperty('--pos',br.value+'%')};bset();br.addEventListener('input',function(){clearInterval(ftm);ftm=null;bset()})}
  var fio=new IntersectionObserver(function(es){if(es[0].isIntersecting){fio.disconnect();show(0);if(!RM&&!SNAP)ftm=setInterval(function(){show((fi+1)%F.length)},6500)}},{threshold:.3});fio.observe(ft);}
/* deck carousel */
var tr=$('#track');if(tr){var cnt=$('#dcnt'),pr=$('#dprog');var n=$$('.ptile',tr).length;
  function gap(){return parseFloat(getComputedStyle(tr).columnGap)||12}
  function pos(){var w=tr.firstElementChild.getBoundingClientRect().width+gap();var i=Math.round(tr.scrollLeft/w);if(cnt)cnt.textContent=String(Math.min(n,i+1)).padStart(2,'0')+' / '+n;if(pr){var vis=Math.max(1,Math.round(tr.clientWidth/w));pr.style.setProperty('--w',(Math.min(n,i+vis)/n*100)+'%')}}
  tr.addEventListener('scroll',pos,{passive:true});pos();
  $$('[data-dir]').forEach(function(b){b.addEventListener('click',function(){var w=tr.firstElementChild.getBoundingClientRect().width+gap();tr.scrollBy({left:w*(+b.getAttribute('data-dir')),behavior:'smooth'})})});
  var mb=$('#dmore');if(mb)mb.addEventListener('click',function(){$('#deck').classList.add('deck-open');mb.remove()});}
/* book console */
var bc=$('#console');if(bc){var opts=$$('.door[data-p]',bc);
  function setStep(n){$$('.steps i',bc).forEach(function(s,k){s.classList.toggle('on',k<n)});var sl=$('#stepl');if(sl)sl.textContent='Step '+n+' of 3'}
  opts.forEach(function(o){o.addEventListener('click',function(){if(o.classList.contains('soon'))return;opts.forEach(function(x){x.classList.toggle('on',x===o);x.setAttribute('aria-pressed',x===o)});$$('.pane',bc).forEach(function(p){p.classList.toggle('on',p.id===o.getAttribute('data-p'))});setStep(2)})});
  $$('.mode .door',bc).forEach(function(o){o.addEventListener('click',function(){$$('.mode .door',bc).forEach(function(x){x.classList.toggle('on',x===o)});$$('.mnote',bc).forEach(function(m){m.style.display=m.getAttribute('data-m')===o.getAttribute('data-m')?'block':'none'});setStep(3);var ph=$('#phf');if(ph)ph.style.display=o.getAttribute('data-m')==='phone'?'block':'none'})});}
/* boarding-pass notches line up with the tear line */
$$('.card.bp').forEach(function(c){var tr=$('.tear',c);if(!tr)return;function s(){c.style.setProperty('--ty',(tr.getBoundingClientRect().top-c.getBoundingClientRect().top)+'px')}s();addEventListener('resize',s);if(document.fonts)document.fonts.ready.then(s)});
/* dental calculator */
var dc=$('#dcalc');if(dc){var rs=$$('input[type=range]',dc);
  function cu(){var pts=0,sp=0,pl=[];rs.forEach(function(r){var v=+r.value,x=+r.getAttribute('data-x');pts+=v*x;sp+=v;pl.push(v*x);r.style.setProperty('--p',((v-r.min)/(r.max-r.min)*100)+'%');r.closest('.cl').querySelector('.cv').textContent='$'+fmt(v)});
    rs.forEach(function(r,k){var b=r.closest('.cl').querySelector('.meter i');if(b){b.style.setProperty('--w',(pts?pl[k]/pts*100:0)+'%')}var pp=r.closest('.cl').querySelector('.cp');if(pp)pp.textContent=fmt(pl[k])+' pts'});
    /* monthly net = points x 0.01836 - 550 (3.0 cents x 85% redeemed x 72% honest discount, minus the fee) */
    var net=pts*0.01836-550;$('#dpts').textContent=fmt(pts);$('#dnet').textContent=(net<0?'-$':'$')+fmt(Math.abs(net));$('#dyr').textContent=(net<0?'-$':'$')+fmt(Math.abs(net*12));$('#dsp').textContent='$'+fmt(sp);var bl=$('#dbl');if(bl)bl.textContent=(sp?pts/sp:0).toFixed(1)+'x';
    var cbk=sp*12*0.02,ms=net*12,top=Math.max(cbk,ms,1),a1=$('#a1'),a2=$('#a2');if(a1){a1.textContent='$'+fmt(cbk);a2.textContent=(ms<0?'-$':'$')+fmt(Math.abs(ms));
      $('.alt3.live .a1 .bar i').style.setProperty('--w',(cbk/top*100)+'%');$('.alt3.live .a2 .bar i').style.setProperty('--w',(Math.max(ms,0)/top*100)+'%')}}
  rs.forEach(function(r){r.addEventListener('input',cu)});cu();}
/* generic show-all lists */
$$('[data-showall]').forEach(function(b){b.addEventListener('click',function(){var t=$(b.getAttribute('data-showall'));if(t)t.classList.add('all');b.remove()})});
})();
