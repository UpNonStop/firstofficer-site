/* Pages that drop WhatsApp (Ohad, 31 Oct): on the page that loads this, the shared header, its phone menu and the footer
   hide their wa.me links. Nothing else changes; every other page keeps them. */
(function () {
  var CSS = 'a[href*="wa.me"]{display:none!important}';
  function add(id) { var h = document.getElementById(id); if (!h || !h.shadowRoot) return false;
    if (!h.shadowRoot.getElementById('fo-nowa')) { var s = document.createElement('style'); s.id = 'fo-nowa'; s.textContent = CSS; h.shadowRoot.appendChild(s); }
    return true; }
  function run() { var a = add('fo-header'), b = add('fo-footer'); return a && b; }
  if (!run()) { var n = 0, t = setInterval(function () { if (run() || ++n > 50) clearInterval(t); }, 100); }
})();
