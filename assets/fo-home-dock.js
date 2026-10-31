/* Home page only (index.html), Ohad's landing brief, 31 Oct.
   Phones: one slim docked "Book the free Found Money Call" button. It shows only while no other pink button is on
   screen, and steps aside near the footer. Desktop: the shared header's nav stays on screen on this page (the ticker
   under it still scrolls away). Every other page keeps the nav scrolling away and nothing docked.
   No WhatsApp links on this page (Ohad, 31 Oct): the header, menu and footer ones are hidden here. */
(function () {
  /* the desk is reached by the Found Money Call, text, call or email here: the shared header, its phone menu and the
     footer drop their WhatsApp links on this page only */
  var NOWA = 'a[href*="wa.me"]{display:none!important}';
  function add(root, id, css) { if (!root.getElementById(id)) { var st = document.createElement('style'); st.id = id; st.textContent = css; root.appendChild(st); } }
  function stick() {
    var h = document.getElementById('fo-header'), f = document.getElementById('fo-footer'); if (!h || !h.shadowRoot) return false;
    add(h.shadowRoot, 'fo-home-stick', '@media (min-width:901px){.nav{position:sticky!important;top:0!important;z-index:300!important}}' + NOWA);
    if (!f || !f.shadowRoot) return false;
    add(f.shadowRoot, 'fo-home-nowa', NOWA);
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
