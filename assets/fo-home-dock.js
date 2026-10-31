/* Home page only (index.html), Ohad's landing brief, 31 Oct.
   Phones: one slim docked "Book the free Found Money Call" button. It shows only while no other pink button is on
   screen, and steps aside near the footer. Desktop: the shared header's nav stays on screen on this page (the ticker
   under it still scrolls away). Every other page keeps the nav scrolling away and nothing docked. */
(function () {
  function stick() {
    var h = document.getElementById('fo-header'); if (!h || !h.shadowRoot) return false;
    if (!h.shadowRoot.getElementById('fo-home-stick')) {
      var st = document.createElement('style'); st.id = 'fo-home-stick';
      st.textContent = '@media (min-width:901px){.nav{position:sticky!important;top:0!important;z-index:300!important}}';
      h.shadowRoot.appendChild(st);
    }
    return true;
  }
  if (!stick()) { var n = 0, t = setInterval(function () { if (stick() || ++n > 50) clearInterval(t); }, 100); }

  var dock = document.getElementById('hdock');
  if (!dock || !('IntersectionObserver' in window)) return;
  var phone = window.matchMedia ? matchMedia('(max-width:760px)') : { matches: false };
  var seen = 0, nearEnd = false, live = [];
  function update() { dock.classList.toggle('on', phone.matches && seen === 0 && !nearEnd); }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { var i = live.indexOf(e.target); if (e.isIntersecting && i < 0) live.push(e.target); else if (!e.isIntersecting && i > -1) live.splice(i, 1); });
    seen = live.length; update();
  }, { threshold: 0 });
  [].forEach.call(document.querySelectorAll('main .btn.pk'), function (b) { io.observe(b); });
  var foot = document.getElementById('fo-footer');
  if (foot) new IntersectionObserver(function (es) { nearEnd = es[0].isIntersecting; update(); }, { rootMargin: '0px 0px 35% 0px' }).observe(foot);
  if (phone.addEventListener) phone.addEventListener('change', update);
})();
