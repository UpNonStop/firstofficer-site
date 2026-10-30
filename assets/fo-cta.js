/* Home page only: CTA reach (the Oct 30 landing brief). Loaded after assets/fo-chrome.js.
   Desktop: once the chrome has drawn the header, html.fo-stick lets the header stay at the top (assets/fo-cta.css).
   Phones and tablets: the docked bar shows whenever none of the page's own pink buttons is on screen
   (the hero, the stop after 05, the price, the final band) and the footer is not either, so one pink
   button is in view at a time. No timers, no popups, nothing to dismiss. */
(function(){
  var H=document.documentElement,hh=document.getElementById('fo-header'),sr=hh&&hh.shadowRoot;
  /* the chrome pins its nav with .nav{position:relative!important} for every page; this page alone lets it stick above 900px */
  if(sr&&sr.querySelector('.nav')){var st=document.createElement('style');st.textContent='@media (min-width:901px){.nav{position:sticky!important;top:0!important}}';sr.appendChild(st);H.classList.add('fo-stick')}
  var dock=document.getElementById('fo-dock');if(!dock)return;
  var mq=window.matchMedia?matchMedia('(max-width:900px)'):{matches:innerWidth<=900};
  var watch=['#mctas','#b5 .fo-inl','#b7 .ctas','#go .ctas','#fo-footer'].map(function(s){return document.querySelector(s)}).filter(Boolean);
  var on=null,raf=0;
  function seen(e){var r=e.getBoundingClientRect();return r.height>0&&r.bottom>0&&r.top<innerHeight}
  function set(v){if(v===on)return;on=v;dock.classList.toggle('show',v);if(v)dock.removeAttribute('inert');else dock.setAttribute('inert','')}
  function check(){raf=0;set(!!mq.matches&&!watch.some(seen))}
  function soon(){if(!raf)raf=requestAnimationFrame(check)}
  addEventListener('scroll',soon,{passive:true});addEventListener('resize',soon);addEventListener('load',soon);check();
})();
