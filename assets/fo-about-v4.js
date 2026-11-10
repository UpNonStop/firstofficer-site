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
/* what's on your table: Return = Earn × Burn, only when both are known */
var sp=$('#v4spend');if(!sp)return;var rate=1,burn=null,stk=$$('.v4stk'),TH=[80,200,450,800,1400,2800];
function cents(n){return n.toFixed(2).replace(/0+$/,'').replace(/\.$/,'')}
function earnWords(r){if(r===0)return '0 points per $1';return (r%1?String(r):String(r))+' '+(r===1?'point':'points')+' per $1'}
function calc(){var s=+sp.value;$('#v4spo').textContent='$'+fmt(s);sp.style.setProperty('--f',((s-sp.min)/(sp.max-sp.min)*100)+'%');
var big=$('#v4big'),now=$('#v4now'),unit=$('#v4unit'),mo=$('#v4mo'),ver=$('#v4ver');
if(burn==null){big.classList.add('wait');now.textContent='Unknown';unit.textContent='Earn is '+earnWords(rate)+'. Burn is still unknown, so Return cannot be calculated yet. Unknown is not zero.';mo.textContent='';
ver.textContent='No return figure yet. An unknown input is not zero, and the $550 fee is not a savings figure.';
stk.forEach(function(im){im.classList.add('off')});return}
var per=rate*burn,monthly=s*rate*burn/100;
big.classList.remove('wait');now.textContent=cents(per)+'¢';
unit.textContent=earnWords(rate)+' × '+cents(burn)+'¢ a point = '+cents(per)+'¢ per $1';
mo.textContent='On this spend, that is about $'+fmt(monthly)+' a month, est. The whole slider amount, at this earn and this burn.';
ver.textContent='Illustrated return is about $'+fmt(monthly)+' a month, est., next to a $550 fee. Your statements decide. Not a promise.';
stk.forEach(function(im,k){im.classList.toggle('off',!(monthly>=TH[k]))})}
sp.addEventListener('input',calc);
$$('.v4seg.earn button').forEach(function(b){b.addEventListener('click',function(){rate=+b.dataset.r;$$('.v4seg.earn button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});calc()})});
$$('.v4seg.burn button').forEach(function(b){b.addEventListener('click',function(){burn=b.dataset.b===''?null:+b.dataset.b;$$('.v4seg.burn button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});calc()})});
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
var ci=$('#v4c'),pi=$('#v4pp'),fi=$('#v4f'),nd=$('#v4needle'),cv=$('#v4cv'),vd=$('#v4vd'),ern=$('#v4ern'),ros=$('#v4ros');
function money(n){return n.toFixed(2).replace(/0+$/,'').replace(/\.$/,'')}
function dial(){var c=+ci.value||0,p=+pi.value||0,f=+fi.value||0,raw=ern?ern.value.trim():'',earn=raw===''?null:Number(raw);
if(!(p>0)){cv.textContent='Unknown';if(nd)nd.style.transform='rotate(-90deg)';vd.className='v4vd b';vd.textContent='The points price is unknown, so Burn is unknown. Return cannot be calculated yet. Unknown is not zero.';
if(ros)ros.textContent='Burn is unknown, so Return cannot be calculated yet. Unknown is not zero.';return}
var v=Math.max(0,(c-f)/p*100),show=(v<10?v.toFixed(2):v.toFixed(1)).replace(/\.?0+$/,'');
cv.textContent=show+'¢';
if(nd)nd.style.transform='rotate('+(Math.min(3,v)/3*180-90).toFixed(1)+'deg)';
if(v<1){vd.className='v4vd b';vd.textContent='Burn under 1¢ a point, est. A plain cash out usually beats it.'}
else if(v<=1.6){vd.className='v4vd l';vd.textContent='Burn in the fair band, est. About 1¢ to 1.6¢ a point.'}
else{vd.className='v4vd e';vd.textContent='Burn over 1.6¢ a point, est.'}
if(!ros)return;
if(earn==null||!isFinite(earn)||earn<0){ros.textContent='Burn is known. Earn is still unknown, so Return cannot be calculated yet. Unknown is not zero.';return}
var shown=parseFloat(show);
ros.textContent=money(earn)+' points per $1 × '+show+'¢ a point = '+money(earn*shown)+'¢ per $1, est.'}
if(ci&&pi&&fi&&cv&&vd){[ci,pi,fi].forEach(function(i){i.addEventListener('input',function(){$$('.v4pre button').forEach(function(x){x.setAttribute('aria-pressed','false')});dial()})});
if(ern)ern.addEventListener('input',dial);
$$('.v4pre button').forEach(function(b){b.addEventListener('click',function(){ci.value=b.dataset.c;pi.value=b.dataset.p;fi.value=b.dataset.f;$$('.v4pre button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});dial()})});dial()}
/* four questions */
$$('.v4rev').forEach(function(b){b.addEventListener('click',function(){var on=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',on?'true':'false');b.textContent=on?'Hide our answer':'See our answer'})});
/* jargon translator */
var jt=$('#v4jt');
$$('.v4jw button').forEach(function(b){b.addEventListener('click',function(){$$('.v4jw button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
if(jt){jt.textContent=b.dataset.t;if(!rm){jt.classList.remove('pop');void jt.offsetWidth;jt.classList.add('pop')}}})});
})();
