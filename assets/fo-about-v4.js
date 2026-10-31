/* About v4: reveals, parallax, count-up, and the "what's on your table" estimate. */
(function(){
var d=document.documentElement;d.classList.add('v4js');
var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function $(s,c){return (c||document).querySelector(s)}function $$(s,c){return [].slice.call((c||document).querySelectorAll(s))}
function fmt(n){return Math.round(n).toLocaleString('en-US')}
/* reveals */
var els=$$('[data-anim]');
if(rm||!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')})}
else{var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.12});els.forEach(function(e){io.observe(e)})}
$$('.v4bars i').forEach(function(i,k){i.style.setProperty('--n',k)});
/* count-up */
$$('[data-count]').forEach(function(el){var to=+el.dataset.count,suf=el.dataset.suf||'';if(rm||!('IntersectionObserver' in window))return;
var o=new IntersectionObserver(function(es){if(!es[0].isIntersecting)return;o.disconnect();var t0=performance.now();(function f(t){var p=Math.min(1,(t-t0)/1400),e=1-Math.pow(1-p,3);el.textContent=fmt(to*e)+suf;if(p<1)requestAnimationFrame(f)})(t0)},{threshold:.4});o.observe(el)});
/* parallax: gentle, transform only */
var par=$$('[data-par]');
if(!rm&&par.length){var tick=false;function upd(){tick=false;var vh=innerHeight;par.forEach(function(el){var r=el.getBoundingClientRect();if(r.bottom<-200||r.top>vh+200)return;var c=(r.top+r.height/2-vh/2);el.style.transform='translate3d(0,'+(c*-(+el.dataset.par)).toFixed(1)+'px,0)'})}
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});addEventListener('resize',upd);upd()}
/* what's on your table */
var sp=$('#v4spend');if(!sp)return;var rate=1,stk=$$('.v4stk'),TH=[1,150,320,550,850,1250];
function calc(){var s=+sp.value;$('#v4spo').textContent='$'+fmt(s);sp.style.setProperty('--f',((s-sp.min)/(sp.max-sp.min)*100)+'%');
var gap=Math.max(0,3-rate)*s*.85,lo=gap*.01,hi=gap*.016,mid=(lo+hi)/2;
$('#v4lo').textContent='$'+fmt(lo);$('#v4hi').textContent='$'+fmt(hi);$('#v4pt').textContent=fmt(gap);
var v=$('#v4ver');if(hi<550){v.textContent="Likely not a fit yet. We'd tell you that on the call, and point you to the free tools.";v.className='v4ver n'}
else if(lo>=550){v.textContent='Clears the $550 fee, est. Your real statements decide the rest.';v.className='v4ver y'}
else{v.textContent="Close call. Your real statements decide, and we'll tell you either way.";v.className='v4ver c'}
stk.forEach(function(im,k){im.classList.toggle('off',!(mid>=TH[k]))})}
sp.addEventListener('input',calc);
$$('.v4seg button').forEach(function(b){b.addEventListener('click',function(){rate=+b.dataset.r;$$('.v4seg button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});calc()})});
calc();
})();
/* round 3: the week, the dial, the four questions, the jargon translator */
(function(){
function $(s,c){return (c||document).querySelector(s)}function $$(s,c){return [].slice.call((c||document).querySelectorAll(s))}
var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
/* a week in the programs */
var wb=$('.v4wk-b'),wl=$('#v4wk'),ws=$('#v4wk-s');
if(wb&&wl&&ws){var full=ws.textContent;ws.textContent='Four alerts to read, decode and act on, on top of the actual job.';
wb.addEventListener('click',function(){var on=wb.getAttribute('aria-expanded')!=='true';wb.setAttribute('aria-expanded',on?'true':'false');wl.classList.toggle('on',on);
ws.textContent=on?full:'Four alerts to read, decode and act on, on top of the actual job.';wb.firstChild.textContent=on?'Show the raw rules ':'Hand it to the desk '})}
/* points or cash dial */
var ci=$('#v4c'),pi=$('#v4pp'),fi=$('#v4f'),nd=$('#v4needle'),cv=$('#v4cv'),vd=$('#v4vd');
function dial(){var c=+ci.value||0,p=+pi.value||0,f=+fi.value||0,v=p>0?Math.max(0,(c-f)/p*100):0;
cv.textContent=(v<10?v.toFixed(2):v.toFixed(1)).replace(/\.?0+$/,'')+'¢';
if(nd)nd.style.transform='rotate('+(Math.min(3,v)/3*180-90).toFixed(1)+'deg)';
if(v<1){vd.className='v4vd b';vd.textContent='A plain cash out usually beats this, est.'}
else if(v<=1.6){vd.className='v4vd l';vd.textContent='A fair use, est.'}
else{vd.className='v4vd e';vd.textContent='A strong use, est. Better than a plain cash out.'}}
if(ci&&pi&&fi&&cv&&vd){[ci,pi,fi].forEach(function(i){i.addEventListener('input',function(){$$('.v4pre button').forEach(function(x){x.setAttribute('aria-pressed','false')});dial()})});
$$('.v4pre button').forEach(function(b){b.addEventListener('click',function(){ci.value=b.dataset.c;pi.value=b.dataset.p;fi.value=b.dataset.f;$$('.v4pre button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});dial()})});dial()}
/* four questions */
$$('.v4rev').forEach(function(b){b.addEventListener('click',function(){var on=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',on?'true':'false');b.textContent=on?'Hide our answer':'See our answer'})});
/* jargon translator */
var jt=$('#v4jt');
$$('.v4jw button').forEach(function(b){b.addEventListener('click',function(){$$('.v4jw button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
if(jt){jt.textContent=b.dataset.t;if(!rm){jt.classList.remove('pop');void jt.offsetWidth;jt.classList.add('pop')}}})});
})();
