/* Home page only (index.html), Ohad's landing brief, 31 Oct.
   Phones: a slim bar docked flush to the bottom edge with the page's two buttons side by side, "Found Money Call" in pink
   and "Run your numbers" in blue (Ohad, 31 Oct). It comes up once you have scrolled past the hero's two buttons, steps
   aside while any of the page's own pairs is on screen (Ohad's note, the $550 price), so the same two buttons never show
   twice at once, and stays down once the closing band and the footer come up. Desktop: the shared header's nav stays on screen
   on this page (the ticker under it still scrolls away). Every other page keeps the nav scrolling away and nothing docked.
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
  var hero = document.getElementById('mctas');
  var live = [], nearEnd = false, pastHero = !hero;
  function update() { dock.classList.toggle('on', phone.matches && pastHero && live.length === 0 && !nearEnd); }
  /* the page's own pink and blue buttons: while any of them is on screen the dock stays down */
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { var i = live.indexOf(e.target); if (e.isIntersecting && i < 0) live.push(e.target); else if (!e.isIntersecting && i > -1) live.splice(i, 1); });
    update();
  }, { threshold: 0 });
  [].forEach.call(document.querySelectorAll('main .btn.pk, main .btn.lb'), function (b) { io.observe(b); });
  /* the dock waits until the hero's two buttons have gone off the top of the screen */
  if (hero) new IntersectionObserver(function (es) { var e = es[es.length - 1]; pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; update(); }, { threshold: 0 }).observe(hero);
  /* and it stays down from the moment the closing band (the pair again, then the footer) comes up, so it does not pop up for a
     moment between the price and the end */
  var end = document.getElementById('go') || document.getElementById('fo-footer');
  if (end) new IntersectionObserver(function (es) { var e = es[es.length - 1]; nearEnd = e.isIntersecting || e.boundingClientRect.top < 0; update(); }, { rootMargin: '0px 0px 35% 0px' }).observe(end);
  if (phone.addEventListener) phone.addEventListener('change', update);
})();
