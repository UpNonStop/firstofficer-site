/* The App page (the-app.html): the three threads under "Where the desk lives" (WhatsApp, Messages, the app) play the same short
   conversation in the background, each a beat apart, until the visitor taps one of the questions; then that thread answers what was
   tapped and stops playing on its own. The landing's "Try it yourself" cue points at them and at the hero phone, and fades once the
   visitor has tried. Nothing plays off screen, in a hidden tab or under reduced motion.
   Leo and Linden Row Insurance are the site's fictional example; every figure is an estimate. */
(function(){
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
function greet(){var h=new Date().getHours();return h<5?'Good evening':h<12?'Good morning':h<17?'Good afternoon':'Good evening'}
function clock(){var d=new Date(),h=d.getHours(),m=d.getMinutes();return (h%12||12)+':'+(m<10?'0':'')+m}
var Q=['Anything waiting for me?','What did Friday find?','Tokyo in business next spring?'];
function A(i){return [greet()+', Leo. One move is confirmed. One more waits for approval.',
  'Friday count: $1,860 found this week, est. Checked against the statements.',
  'On pace for spring 2027: 102,400 of about 320,000 points, est. Nothing is booked before an OK.'][i]}
function esc(t){return t.replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}

/* the hero phone: the cue fades once the visitor taps the phone or the list beside it (assets/fo-theapp.js runs the tab tour) */
var stage=document.querySelector('.tah .tstage');
if(stage){var tried=function(){stage.classList.add('tried')};
  var tp=document.getElementById('tphone');if(tp)tp.addEventListener('click',tried);
  $$('.tlist button').forEach(function(b){b.addEventListener('click',tried)})}

var sec=document.getElementById('options');
var phones=$$('.cv[data-ch]');
if(!phones.length)return;

function Thread(el,lag){
  var th=el.querySelector('.cv-th'),sr=el.querySelector('.cv-sr'),qs=$$('.cv-q',el),ch=el.getAttribute('data-ch');
  var next=1,timers=[],held=false,vis=false,busy=false,started=false;
  function later(fn,ms){var t=setTimeout(function(){timers=timers.filter(function(x){return x!==t});fn()},ms);timers.push(t)}
  function cancel(){timers.forEach(clearTimeout);timers=[];busy=false}
  function stamp(){return ch==='wa'?'<i class="cv-t">'+clock()+'</i>':''}
  function add(kind,html){var b=document.createElement('div');b.className='cv-b '+kind;b.innerHTML=html;
    var dl=th.querySelector('.cv-dl');if(dl)dl.parentNode.removeChild(dl);
    th.appendChild(b);
    if(ch==='im'&&kind==='me'){var d=document.createElement('span');d.className='cv-dl';d.textContent='Delivered';th.appendChild(d)}
    var all=$$('.cv-b',th);for(var k=0;k<all.length-5;k++)all[k].parentNode.removeChild(all[k]);
    return b}
  function settle(){var ty=th.querySelector('.cv-b.ty');if(ty)ty.parentNode.removeChild(ty);
    var last=$$('.cv-b',th).pop();if(last&&last.classList.contains('me')&&last.dataset.i)add('fo',esc(A(+last.dataset.i))+stamp())}
  function exchange(i,user,done){
    busy=true;var q=qs[i];if(q){q.classList.add('pr');later(function(){q.classList.remove('pr')},260)}
    var me=add('me',esc(Q[i])+stamp());me.dataset.i=i;
    var answer=function(){var ty=th.querySelector('.cv-b.ty');if(ty)ty.parentNode.removeChild(ty);delete me.dataset.i;
      add('fo',esc(A(i))+stamp());if(user&&sr)sr.textContent=A(i);busy=false;if(done)done()};
    if(RM){answer();return}
    later(function(){add('fo ty','<u></u><u></u><u></u>')},520);
    later(answer,1500)}
  function reset(done){th.classList.add('out');later(function(){$$('.cv-b,.cv-dl',th).forEach(function(b){b.parentNode.removeChild(b)});th.classList.remove('out');next=0;done(700)},380)}
  function play(d){
    if(held||!vis||RM||document.hidden||busy||timers.length)return;
    later(function(){exchange(next,false,function(){next=(next+1)%Q.length;
      if(next===0)later(function(){reset(play)},4200);else play()})},d!=null?d:(started?2700:lag));
    started=true}
  function pause(){cancel();settle()}
  qs.forEach(function(q){q.addEventListener('click',function(){
    held=true;cancel();settle();if(sec)sec.classList.add('tried');exchange(+q.getAttribute('data-i'),true)})});
  /* the first answer greets by the visitor's local time, as the hero phone does */
  var first=th.querySelector('.cv-b.fo');if(first){var tail=first.querySelector('.cv-t');first.innerHTML=esc(A(0))+(tail?'<i class="cv-t">'+clock()+'</i>':'')}
  $$('.cv-t',th).forEach(function(t){t.textContent=clock()});
  var ck=el.querySelector('.cv-clk');if(ck)ck.textContent=clock();
  return {see:function(v){vis=v;if(v)play();else pause()},wake:function(){if(document.hidden)pause();else play()}}
}
var T=phones.map(function(el,k){return Thread(el,600+k*1700)});
if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(en){en.forEach(function(x){var k=phones.indexOf(x.target);if(k>-1)T[k].see(x.isIntersecting)})},{threshold:.45});
  phones.forEach(function(p){io.observe(p)})}
document.addEventListener('visibilitychange',function(){T.forEach(function(t){t.wake()})});
setInterval(function(){$$('.cv-clk').forEach(function(c){c.textContent=clock()})},30000);
})();
