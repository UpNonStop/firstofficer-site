/* Gate pages (Nov 2, 2026): the 404 board, the hand-off into the app, and the invite status.
   Tokens from app links are read into memory by the inline fo-scrub script and taken out of the address bar
   before analytics loads. They only ever leave this page to open the First Officer app on the phone,
   and an invite token is also used to read the invitation's status (read only). */
(function () {
  var d = document, html = d.documentElement, Q = window.FO_Q || {};
  var WA = 'https://wa.me/16199404040?text=';
  var API = 'https://cuzuzzbezswvejnoskum.supabase.co/functions/v1/fo-api/v1';
  var ua = navigator.userAgent || '';
  var phone = /iPhone|iPad|iPod|Android/.test(ua) || (/Macintosh/.test(ua) && navigator.maxTouchPoints > 1);
  var still = html.classList.contains('fo-still') || (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
  function $(id) { return d.getElementById(id); }
  function each(sel, fn, root) { Array.prototype.forEach.call((root || d).querySelectorAll(sel), fn); }
  function text(id, s) { var el = $(id); if (el) el.textContent = s; }

  /* The 404 sets <base href="/"> so it works at any depth; keep in-page links (the skip link) on this page. */
  if (d.querySelector('base')) d.addEventListener('click', function (e) {
    var path = e.composedPath ? e.composedPath() : [e.target], a = null, i;
    for (i = 0; i < path.length && !a; i++) if (path[i].tagName === 'A' && /^#./.test(path[i].getAttribute('href') || '')) a = path[i];
    if (!a) return;
    var el = $(a.getAttribute('href').slice(1)); e.preventDefault();
    if (el) { if (!el.hasAttribute('tabindex')) el.setAttribute('tabindex', '-1'); el.focus(); el.scrollIntoView(); }
  });

  /* Which copy shows: data-fg-when="phone c t" shows only on a phone with c and t in the link;
     data-fg-unless="..." shows otherwise. Without this script, the "unless" copy shows. */
  function holds(spec) {
    return spec.split(' ').every(function (w) { return !w || (w === 'phone' ? phone : !!Q[w]); });
  }
  each('[data-fg-when]', function (el) { el.hidden = !holds(el.getAttribute('data-fg-when')); });
  each('[data-fg-unless]', function (el) { el.hidden = holds(el.getAttribute('data-fg-unless')); });

  /* Hand-off into the app: firstofficer://<route>?<the link's own query>, the scheme the app registers. */
  var ROUTES = { link: ['c', 't'], invite: ['token'], 'plaid-oauth': ['oauth_state_id'], 'sign-in': [] };
  each('a[data-fg-app]', function (a) {
    var route = a.getAttribute('data-fg-app'), q = [];
    (ROUTES[route] || []).forEach(function (k) { if (Q[k]) q.push(k + '=' + encodeURIComponent(Q[k])); });
    a.href = 'firstofficer://' + route + (q.length ? '?' + q.join('&') : '');
    a.addEventListener('click', function () {
      var miss = $(a.getAttribute('data-fg-miss') || '');
      var t = setTimeout(function () { if (!d.hidden && miss) miss.hidden = false; }, 1800);
      d.addEventListener('visibilitychange', function v() { if (d.hidden) { clearTimeout(t); d.removeEventListener('visibilitychange', v); } });
    });
  });

  /* The 404 board: three split-flap tiles flip once and land on 4 0 4. */
  function flip(tile, next, ms) {
    var top = tile.querySelector('.t i'), bot = tile.querySelector('.b i'), ft = tile.querySelector('.ft'), fb = tile.querySelector('.fb');
    ft.firstChild.textContent = bot.textContent; fb.firstChild.textContent = next; top.textContent = next;
    ft.style.visibility = fb.style.visibility = 'visible';
    return ft.animate([{ transform: 'rotateX(0deg)' }, { transform: 'rotateX(-90deg)' }], { duration: ms, easing: 'ease-in', fill: 'forwards' }).finished
      .then(function () {
        ft.style.visibility = 'hidden';
        return fb.animate([{ transform: 'rotateX(90deg)' }, { transform: 'rotateX(0deg)' }], { duration: ms, easing: 'ease-out', fill: 'forwards' }).finished;
      })
      .then(function () {
        bot.textContent = next; fb.style.visibility = 'hidden';
        ft.getAnimations().concat(fb.getAnimations()).forEach(function (x) { x.cancel(); });
      });
  }
  var tiles = d.querySelectorAll('.fg-f');
  if (tiles.length && !still && typeof Animation !== 'undefined' && 'finished' in Animation.prototype && 'getAnimations' in Element.prototype) {
    Array.prototype.forEach.call(tiles, function (tile, i) {
      var seq = [], n = 5 + i * 3, k, j = 1;
      for (k = 0; k < n; k++) seq.push(String((Math.random() * 10) | 0));
      seq.push(tile.getAttribute('data-c'));
      each('i', function (el) { el.textContent = seq[0]; }, tile);
      setTimeout(function step() { if (j < seq.length) flip(tile, seq[j++], 62).then(step, function () {}); }, 280 + i * 90);
    });
  }

  /* The 404 itself: what was asked for, who is asking, and the closest page. */
  if ($('fg-404')) {
    var path = location.pathname;
    try { path = decodeURIComponent(path); } catch (e) {}
    var direct = path === '/404.html' || path === '/404';
    text('fg-path', direct ? 'firstofficer.upnonstop.com/404' : path);
    var owner = !!window.FO_OWNER || /^\/(link|invite|plaid-oauth|app|desk|sign-?in|log-?in|auth|v1|approve|approvals?|account|join|connect|briefing)(\/|\.|$)/i.test(path);
    if (owner) {
      var lanes = $('fg-lanes'), own = $('fg-own');
      if (lanes && own) lanes.insertBefore(own, lanes.firstChild);
      text('fg-st', 'Link not found');
      text('fg-sub', 'Links from First Officer open the app on your phone. If this one is old, ask for a new one in the app.');
    }
    var wa = $('fg-wa');
    if (wa && !direct) wa.href = WA + encodeURIComponent("Hi First Officer, this link didn't work for me: firstofficer.upnonstop.com" + path);

    var PAGES = [
      ['pricing.html', 'Pricing', 'pricing price prices cost costs fee fees access plans'],
      ['calculator.html', 'the calculator', 'calculator calc calculate numbers estimate estimator savings roi worth value'],
      ['book.html', 'the Found Money Call', 'book booking call calls schedule demo meeting contact found money'],
      ['product.html', 'the product', 'product products desk features pillars service services'],
      ['how.html', 'how it works', 'how works process steps onboarding'],
      ['about.html', 'About', 'about team ohad story company founder'],
      ['trust.html', 'Trust and security', 'trust security secure safety safe plaid'],
      ['industries.html', 'Industries', 'industries industry trades trade verticals'],
      ['field-notes.html', 'Field Notes', 'field notes blog articles article posts post news'],
      ['education.html', 'Lessons', 'education lessons lesson learn course guides guide'],
      ['freebies.html', 'Freebies', 'freebies freebie free gifts perks deals resources'],
      ['the-app.html', 'The App', 'app ios android download iphone mobile'],
      ['upns.html', 'The Intelligence Report', 'upns intelligence report reports dispatch'],
      ['privacy-policy.html', 'the Privacy Policy', 'privacy policy gdpr ccpa'],
      ['terms-of-service.html', 'the Terms of Service', 'terms tos conditions legal'],
      ['disclaimer.html', 'the Disclaimer', 'disclaimer disclosures disclosure'],
      ['for-agencies.html', 'marketing agencies', 'agency agencies marketing advertising'],
      ['for-auto-repair.html', 'auto repair shops', 'auto repair mechanic mechanics garage'],
      ['for-cleaning.html', 'cleaning companies', 'cleaning cleaners janitorial maid'],
      ['for-consulting.html', 'consulting firms', 'consulting consultants consultant'],
      ['for-contractors.html', 'contractors', 'contractors contractor construction builders builder'],
      ['for-cpa-firms.html', 'CPA firms', 'cpa cpas accounting accountants accountant bookkeeping'],
      ['for-dental.html', 'dental practices', 'dental dentist dentists orthodontist'],
      ['for-ecommerce.html', 'e-commerce sellers', 'ecommerce shopify store stores online retail'],
      ['for-fitness.html', 'gyms and studios', 'fitness gym gyms studio studios'],
      ['for-hvac.html', 'HVAC companies', 'hvac heating cooling'],
      ['for-it-services.html', 'IT and MSP', 'msp msps managed tech technology'],
      ['for-landscaping.html', 'landscaping companies', 'landscaping landscapers lawn lawns gardening'],
      ['for-law-firms.html', 'law firms', 'law lawyers lawyer attorneys attorney firms'],
      ['for-medical.html', 'medical practices', 'medical doctors doctor clinic clinics physicians'],
      ['for-property-management.html', 'property managers', 'property properties management landlords rentals'],
      ['for-real-estate.html', 'real estate agents', 'real estate realtors realtor brokers'],
      ['for-restaurants.html', 'restaurants', 'restaurants restaurant cafe cafes food'],
      ['for-salons.html', 'salons', 'salons salon beauty spa barber barbers'],
      ['for-trucking.html', 'trucking companies', 'trucking trucks truck logistics freight fleet'],
      ['for-veterinary.html', 'veterinary practices', 'veterinary vet vets animal']
    ];
    var STOP = ' html htm www for the and page pages index old new fo firstofficer upnonstop com ';
    var toks = function (s) { return s.toLowerCase().replace(/\.html?$/, '').split(/[^a-z0-9]+/).filter(function (w) { return w && STOP.indexOf(' ' + w + ' ') < 0; }); };
    var dist = function (a, b) {
      if (Math.abs(a.length - b.length) > 2) return 9;
      var p = [], c, i, j; for (j = 0; j <= b.length; j++) p[j] = j;
      for (i = 1; i <= a.length; i++) { c = [i]; for (j = 1; j <= b.length; j++) c[j] = Math.min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)); p = c; }
      return p[b.length];
    };
    var want = toks(path), best = null, top = 1;
    if (!owner && !direct && want.length) PAGES.forEach(function (pg) {
      var keys = pg[2].split(' ').concat(toks(pg[0])), s = 0;
      want.forEach(function (w) {
        var v = 0;
        keys.forEach(function (k) {
          var x = w === k ? 3 : (w.length >= 4 && k.length >= 4 && (k.indexOf(w) === 0 || w.indexOf(k) === 0)) ? 2 : (w.length >= 5 && dist(w, k) <= (w.length >= 8 ? 2 : 1)) ? 2 : 0;
          if (x > v) v = x;
        });
        s += v;
      });
      if (s > top) { top = s; best = pg; }
    });
    if (best) {
      var near = $('fg-near'), a = near && near.querySelector('a');
      if (a) { a.href = best[0]; a.textContent = best[1]; near.hidden = false; }
    }
  }

  /* The invite: who invited you, where, and whether it is still open. Read only; joining happens in the app. */
  if ($('fg-invite') && Q.token && window.fetch) {
    var ctl = window.AbortController ? new AbortController() : null;
    if (ctl) setTimeout(function () { ctl.abort(); }, 6000);
    fetch(API + '/invites/' + encodeURIComponent(Q.token), { credentials: 'omit', referrerPolicy: 'no-referrer', signal: ctl ? ctl.signal : undefined })
      .then(function (r) { return r.status === 410 || r.status === 404 ? { status: 'expired' } : r.ok ? r.json() : null; })
      .then(function (v) {
        if (!v) return;
        var company = v.companyName || v.company_name || '', who = (v.invitedBy && v.invitedBy.name) || v.inviterName || v.inviter_name || '';
        var role = { owner: 'an owner', approver: 'an approver', member: 'a member' }[v.role] || '';
        var say = function (s) { var el = $('fg-who'); if (el) { el.textContent = s; el.hidden = false; } };
        if (v.status === 'expired' || v.status === 'used') {
          text('fg-h1', v.status === 'used' ? 'This invitation was already used.' : 'This invitation has expired.');
          text('fg-h2', 'Ask for a new one.');
          say(v.status === 'used'
            ? 'If you still need to join' + (company ? ' ' + company : '') + ', ask ' + (who || 'the person who invited you') + ' to send a new one.'
            : 'Invitations work for 7 days. Ask ' + (who || 'the person who invited you') + ' to send a new one.');
          each('[data-fg-open]', function (el) { el.hidden = true; });
          return;
        }
        if (v.alreadyMember && company) { say('You are already part of ' + company + '. Open First Officer to see the Desk.'); return; }
        if (company && who) {
          var until = '', exp = v.expiresAt || v.expires_at;
          try { if (exp) until = ' It works until ' + new Date(exp).toLocaleDateString('en-US', { month: 'long', day: 'numeric' }) + '.'; } catch (e) {}
          say(who + ' added you to ' + company + (role ? ' as ' + role : '') + '.' + until);
        }
      })
      .catch(function () {});
  }
})();
