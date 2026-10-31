/* First Officer deeper -modes pages: hero photos, swipe rails with rectangle progress, tap-to-expand on phones, local-time phone clock. Mockup only. */
(function(){
var A=window.FO_A||'',RM=matchMedia('(prefers-reduced-motion: reduce)').matches,$=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
/* hero photos: low opacity, rotating, same pool as home */
var bg=$('.mbg');if(bg&&!bg.classList.contains('tbg')){var N=[],SFX=innerWidth<761?'-m':'';for(var i=0;i<=30;i++)N.push(A+'img/rec/bg/'+(i<10?'0':'')+i+SFX+'.webp');
var off=window.FO_BG0?FO_BG0.k%N.length:Math.floor(Math.random()*N.length),cur=0,els=[0,1].map(function(){var e=document.createElement('i');bg.insertBefore(e,bg.firstChild);return e});
els[0].style.backgroundImage='url('+N[off]+')';els[0].classList.add('on');
if(!RM)setInterval(function(){if(document.documentElement.classList.contains('fo-still'))return;var nx=els[1-cur];off=(off+1)%N.length;var u=N[off],im=new Image();im.onload=function(){nx.style.backgroundImage='url('+u+')';nx.classList.add('on');els[cur].classList.remove('on');cur=1-cur};im.src=u},5200)}
/* rails: rectangle progress, synced to scroll */
$$('.srail').forEach(function(r){var d=r.nextElementSibling;if(!d||!d.classList.contains('sdots'))return;var n=r.children.length;
  d.innerHTML=Array(n+1).join('<i></i>');var dots=$$('i',d);
  function upd(){var w=r.children[0].getBoundingClientRect().width+12,e=r.scrollWidth-r.clientWidth,k=e>4&&r.scrollLeft>=e-4?n-1:Math.min(n-1,Math.round(r.scrollLeft/w));dots.forEach(function(e,j){e.classList.toggle('on',j===k)})}
  r.addEventListener('scroll',upd,{passive:true});upd();
  dots.forEach(function(e,j){e.addEventListener('click',function(){r.scrollTo({left:r.children[j].offsetLeft-r.children[0].offsetLeft,behavior:RM?'auto':'smooth'})})})});
/* tap-to-expand on phones, open on desktop */
var mq=matchMedia('(min-width:761px)');function tx(){$$('details.tx').forEach(function(d){if(mq.matches)d.open=true})}tx();
/* local-time clock on the phone mockups */
function clock(){var d=new Date(),t=(d.getHours()%12||12)+':'+(d.getMinutes()<10?'0':'')+d.getMinutes();$$('.cel .sb>span').forEach(function(e){e.textContent=t})}
clock();setInterval(clock,30000);
})();
