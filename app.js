/* ============================================================================
   Your First Officer, the owner's app.

   One fetch, five tabs. This file selects strings out of the payload and puts
   them on screen. It does not add, divide, round or format a single number:
   fo_app_state did that in SQL, so every surface says the same thing and the
   money has one author. Every money value arrives as words: there is no bare
   dollar amount in the payload for this file to put a sign in front of. Search this file for arithmetic and you will not find
   any. That is deliberate, and predeploy_app_state.ts fails the deploy if the
   edge function ever starts doing it either.
   ========================================================================== */
'use strict';

var API  = 'https://cuzuzzbezswvejnoskum.supabase.co/functions/v1/fo-app-state';
var WA   = 'https://wa.me/16199404040?text=';
var TABS = [
  { id:'home',   label:'Earn',   icon:'i-earn'  },
  { id:'burn',   label:'Burn',   icon:'i-burn'  },
  { id:'mid',    label:'',       icon:null      },
  { id:'learn',  label:'Learn',  icon:'i-learn' },
  { id:'return', label:'Return', icon:'i-ret'   }
];
var SECT = { home:'var(--pink)', earn:'var(--green-lift)', burn:'var(--red-lift)',
             'return':'var(--pink)', learn:'var(--blue-lift)' };

var screenEl = document.getElementById('screen');
var tabsEl   = document.getElementById('tabs');
var ruleEl   = document.getElementById('rule');
var STATE = null, NAME = '', TOKEN = '';

/* --- tiny DOM helpers. No innerHTML with payload text, ever. -------------- */
function el(tag, cls, text){
  var n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text !== undefined && text !== null) n.textContent = String(text);
  return n;
}
function icon(id, cls){
  var s = document.createElementNS('http://www.w3.org/2000/svg','svg');
  if (cls) s.setAttribute('class', cls);
  var u = document.createElementNS('http://www.w3.org/2000/svg','use');
  u.setAttribute('href', '#' + id);
  s.appendChild(u);
  return s;
}
function row(parent, opts){
  var r = el('div','rw');
  if (opts.tone) r.appendChild(el('span','bul ' + opts.tone));
  var t = el('span','tx', opts.title);
  if (opts.sub) t.appendChild(el('s', null, opts.sub));
  r.appendChild(t);
  if (opts.badge) r.appendChild(el('span','mult', opts.badge));
  if (opts.value) r.appendChild(el('span','v ' + (opts.vclass || ''), opts.value));
  parent.appendChild(r);
  return r;
}
function zone(parent, label){ parent.appendChild(el('p','zh', label)); }
function card(parent, k, b, s){
  var c = el('div','card');
  c.appendChild(el('p','k', k));
  c.appendChild(el('p','b', b));
  if (s) c.appendChild(el('p','s', s));
  parent.appendChild(c);
  return c;
}
function note(parent, k, body){
  var n = el('div','note');
  if (k) n.appendChild(el('b', null, k));
  n.appendChild(document.createTextNode(body));
  parent.appendChild(n);
}
function action(parent, label, sub, waText){
  var a = el('a','act', label);
  a.href = WA + encodeURIComponent(waText);
  a.rel = 'noopener';
  if (sub) a.appendChild(el('small', null, sub));
  parent.appendChild(a);
}
function hero(parent, kind, kicker, big, say, small){
  var h = el('section','hero ' + kind);
  h.appendChild(icon('chevw','mk'));
  var inn = el('div','in');
  if (kicker) inn.appendChild(el('span','kicker', kicker));
  inn.appendChild(el('span','num' + (small ? ' sm' : ''), big));
  if (say) inn.appendChild(el('p','say', say));
  h.appendChild(inn);
  parent.appendChild(h);
  return h;
}

/* --- the five screens ----------------------------------------------------- */
function screenHome(){
  var s = STATE, f = document.createDocumentFragment();
  var e = s.earn || {}, b = s.burn || {}, plan = e.plan || {};
  var top = (e.lines || [])[0];

  // The landing screen is the strategy and how far through it we are, not a
  // list of findings. Every figure below is composed in SQL, including the
  // percentage: the page never counts or divides.
  var heroEl = hero(f,'home','Where we stand',
    (plan.on_plan_pct != null ? plan.on_plan_pct + '%' : e.annual_gain_text),
    'of spending already goes on the card we planned for it. ' +
    (plan.moves_left || 0) + ' moves left, worth ' + (e.annual_gain_text || '') + ' a year.');

  // the meter sits inside the hero so the progress reads against the section colour
  var hero_el = heroEl.querySelector('.in');
  if (plan.on_plan_pct != null && hero_el) {
    var m = el('div','meter');
    var tr = el('div','track'), fi = el('div','fill');
    fi.style.width = plan.on_plan_pct + '%';
    tr.appendChild(fi); m.appendChild(tr);
    var ends = el('div','ends');
    var a = el('span'); a.textContent = plan.on_plan_text + ' charges';
    var z = el('span'); z.textContent = plan.basis || '';
    ends.appendChild(a); ends.appendChild(z); m.appendChild(ends);
    hero_el.appendChild(m);
  }

  var body = el('div','body');

  zone(body, 'Running as designed');
  // the meter above already gives the count, so this row carries the money
  row(body, { tone:'g', title:'Already on the right card',
    sub:'no change needed, this is the plan working',
    value:e.already_correct_spend_text, vclass:'g' });
  if (b.transferable_text) row(body, { tone:'g', title:'Points ready to move to an airline',
    sub:'across the currencies with a live transfer path', value:b.transferable_text, vclass:'d' });

  zone(body, 'Still to put in place');
  (e.lines || []).slice(0,3).forEach(function(l){
    row(body, { tone:'a', title:l.label,
      sub:(l.misrouted_monthly_text || '') + ' a month on the ' + l.using_now +
          ', the ' + l.use_instead + ' pays more',
      value:l.annual_gain_text, vclass:'g' });
  });

  var find = b.find;
  if (find && find.saved_usd_text) {
    zone(body, 'What it buys');
    row(body, { tone:'p', title:find.origin + ' to ' + find.destination + ' and back',
      sub:find.points_text + ' points on ' + find.program + ' plus ' + find.taxes_text +
          ', against ' + find.chart_points_text + ' published',
      value:find.saved_usd_text, vclass:'p' });
  }

  action(body, 'Pick your dates', 'First one free', 'I want to book a trip');
  f.appendChild(body);
  return f;
}

/* --- Earn, drilled down ------------------------------------------------------
   Every string here arrives composed from SQL: the badge word, the sentence
   that counts months, the action, the worth. The page decides only what is
   open and what is closed. A category line with merchants behind it is a
   button; tapping it shows each merchant with its badge (Recurring, red;
   One time or One month, amber; Unmatched, grey), what happened, and what
   to do. Nothing is computed here, so nothing here can be wrong on its own. */
function subFor(l){
  var s = l.using_now ? 'on the ' + l.using_now + ', move to the ' + l.use_instead
                      : 'move to the ' + l.use_instead;
  return s + (l.condition ? '. ' + l.condition : '');
}
/* --- What we have flown --------------------------------------------------
   One card per award on the ledger. when_text, say, cpp_text and tier_text are
   composed by fo_app_flown; the tier word picks the colour in app.html and the
   page never works out a cent of its own. A row without a cash fare on record
   says so in the reader's words and gets the 'none' badge. */
function flownCard(parent, x){
  var c = el('div','fc');
  var head = el('div','mh');
  head.appendChild(el('span','fw', x.when_text));
  head.appendChild(el('span','flag ' + (x.tier || 'none'), x.cpp_text || 'no fare on record'));
  c.appendChild(head);
  c.appendChild(el('p','ft', x.provider + (x.sub ? ', ' + x.sub : '')));
  c.appendChild(el('p','ms', x.say));
  if (x.travel_text) c.appendChild(el('p','md', 'Travel ' + x.travel_text + '.'));
  if (x.confirmation_ref) c.appendChild(el('p','fr', 'Confirmation ' + x.confirmation_ref));
  if (x.booking_ref) c.appendChild(el('p','md', 'Desk reference ' + x.booking_ref));
  parent.appendChild(c);
}
function merchantRow(parent, m){
  var d = el('div','mr ' + (m.flag || ''));
  var head = el('div','mh');
  head.appendChild(el('span','flag ' + (m.flag || ''), m.badge));
  if (m.worth_text) head.appendChild(el('span','mw', m.worth_text));
  d.appendChild(head);
  d.appendChild(el('p','ms', m.say));
  if (m['do']) d.appendChild(el('p','md', m['do']));
  parent.appendChild(d);
}
function screenEarn(){
  var e = STATE.earn || {}, sm = e.summary || {}, f = document.createDocumentFragment();
  hero(f,'earn','Room to grow', e.annual_gain_text || '',
    (e.switches === 1 ? '1 move' : (e.switches || 0) + ' moves') + ' across cards already in the wallet. Nothing to apply for.');
  var body = el('div','body');

  if (sm.say){
    zone(body, 'Where we can do better');
    note(body, null, sm.say);
  }

  zone(body, 'Ranked by what they pay');
  (e.lines || []).forEach(function(l){
    var ms = l.merchants || [];
    var r = row(body, { title:l.label, sub:subFor(l),
      badge: ms.length ? (ms.length === 1 ? '1 merchant' : ms.length + ' merchants') : null,
      value:l.annual_gain_text, vclass:'g' });
    if (!ms.length) return;
    r.classList.add('exp');
    r.setAttribute('role','button'); r.tabIndex = 0; r.setAttribute('aria-expanded','false');
    var dd = el('div','dd'); dd.hidden = true;
    ms.forEach(function(m){ merchantRow(dd, m); });
    body.appendChild(dd);
    var toggle = function(){
      var open = dd.hidden;
      dd.hidden = !open;
      r.classList.toggle('open', open);
      r.setAttribute('aria-expanded', String(open));
    };
    r.addEventListener('click', toggle);
    r.addEventListener('keydown', function(ev){
      if (ev.key === 'Enter' || ev.key === ' '){ ev.preventDefault(); toggle(); }
    });
  });

  if (sm.basis) note(body, 'What the badges mean', sm.basis);
  if (e.must_state) note(body, 'How to read this', e.must_state);
  if (e.scope) note(body, 'What this covers', e.scope);
  note(body, 'What we cannot do',
    'We read the statements one to three days after a charge and send word. We never touch a card at the register and never move a card on anyone\'s behalf. We spot it; the tap is the one step that stays in hand.');
  action(body, 'Send me the whole map', e.annual_gain_text + ' a year', 'Send me the routing map');
  f.appendChild(body);
  return f;
}

function screenBurn(){
  var b = STATE.burn || {}, f = document.createDocumentFragment();
  var find = b.find;
  hero(f,'burn','What the balance buys', b.transferable_text,
    'transferable points, across the currencies with a live path to an airline.', true);
  var body = el('div','body');

  if (find){
    zone(body, 'The find');
    // One string, composed in SQL beside the query that ranked it. This used
    // to be assembled here and claimed the cheapest chart outright, which the
    // destinations list three rows below contradicted. A superlative is a claim
    // about every other row and only the query that ranked them can make it.
    card(body, find.origin + ' to ' + find.destination + ', ' + find.program,
      find.points_text, find.basis_text || '');
    var p = el('div','pair');
    [['We would pay', find.points_text + ' pts'],
     ['Taxes', find.taxes_text],
     ['Points saved', find.saved_points_text],
     ['Worth', find.saved_usd_text]].forEach(function(kv){
      var d = el('div'); d.appendChild(el('p','k',kv[0])); d.appendChild(el('p','v2',kv[1]));
      p.appendChild(d);
    });
    body.appendChild(p);
  }

  zone(body, 'Where we can go');
  (b.destinations || []).forEach(function(d){
    row(body, { title:d.zone + ', ' + d.cabin, sub:d.points_text + ' points each round trip',
      value:String(d.trips), vclass:'p' });
  });

  zone(body, 'What we hold');
  (b.balances || []).forEach(function(x){
    row(body, { tone:x.transferable ? 'g' : null, title:x.program,
      sub:(function(){
        var parts = [x.freshness + ', read ' + x.days_old + ' days ago'];
        if (!x.transferable) parts.push('No transfer path from this one');
        if (x.since_text) parts.push(x.since_text);
        return parts.join('. ') + (parts.length > 1 ? '.' : '');
      })(),
      value:x.balance_text, vclass:'d' });
  });

  zone(body, 'What we have flown');
  var ft = b.flown_totals;
  if (ft) {
    var pf = el('div','pair');
    [['Trips', ft.trips_text],
     ['Points used', ft.points_text],
     ['Taxes and fees', ft.taxes_text],
     ['Fares replaced', ft.cash_text || 'none on record']].forEach(function(kv){
      var d = el('div'); d.appendChild(el('p','k',kv[0])); d.appendChild(el('p','v2',kv[1]));
      pf.appendChild(d);
    });
    body.appendChild(pf);
    if (ft.cpp_text) {
      var tr = row(body, { title:'Each point returned', sub:ft.cpp_basis || '', value:ft.cpp_text, vclass:'p' });
      tr.appendChild(el('span','flag ' + (ft.tier || 'none'), ft.tier_text));
    } else if (ft.cpp_basis) {
      note(body, 'No figure claimed', ft.cpp_basis);
    }
  }
  (b.flown || []).forEach(function(x){ flownCard(body, x); });
  if (b.flown_note) note(body, 'Nothing flown yet', b.flown_note);
  action(body, 'Ask for these dates', 'First one free', 'I want to use my points');
  f.appendChild(body);
  return f;
}

function screenReturn(){
  var r = STATE['return'] || {}, f = document.createDocumentFragment();
  hero(f,'return','Since we started', r.found_annual_text,
    'found in bills that were already being paid. This number only goes up.');
  var body = el('div','body');

  zone(body, 'What we have found');
  row(body, { tone:'g', title:'Every year, from the switches',
    sub:r.switches + ' moves across cards already in the wallet', value:r.found_annual_text, vclass:'g' });
  row(body, { tone:'g', title:'Every trip, on top of that',
    sub:r.per_trip_basis || '', value:r.per_trip_text, vclass:'g' });
  row(body, { tone:'g', title:'What the next seat is worth',
    sub:'at the top of the band for these points', value:r.seat_text, vclass:'g' });

  if (r.flown_trips_text) {
    zone(body, 'What we have flown');
    row(body, { tone:'p', title:'Cash fares replaced',
      sub:r.flown_trips_text + ' on the ledger, ' + r.flown_points_text + ' points, ' +
          r.flown_taxes_text + ' in taxes and fees',
      value:r.flown_cash_text || 'not on record', vclass:'p' });
    if (r.flown_cpp_text) row(body, { tone:'p', title:'Each point returned',
      sub:r.flown_basis || '', value:r.flown_cpp_text, vclass:'p' });
  }

  note(body, 'Two different units', r.units_note +
    '. The first is a year of bills. The second happens each time we fly.');
  note(body, 'Reading since', 'We started counting on ' + r.reading_since +
    ' and have never counted down from a fee. Everything above is what was found, not what is owed.');
  action(body, 'See the full report', 'Sent to the thread', 'Send me my return report');
  f.appendChild(body);
  return f;
}

function screenLearn(){
  var l = STATE.learn || {}, sh = l.shape || {}, bk = l.book || {};
  var f = document.createDocumentFragment();
  var m = sh.matched;
  hero(f,'learn','Businesses like yours', m ? m.display_name : 'No match yet',
    m ? m.tease : (sh.no_match_reason || ''), true);
  var body = el('div','body');

  if (m){
    zone(body, 'Why this one');
    (sh.derived_from || []).forEach(function(w){ row(body, { tone:'g', title:w }); });
    // The match used to appear in this list, under a heading saying these are
    // the alternatives, beside the scorer's own tally as owner copy. SQL now
    // excludes it and answers in sentences. When nothing else had a fact behind
    // it, one true line replaces a column of zeroes pretending to be diligence.
    if (sh.considered_note){
      note(body, 'What else was considered', sh.considered_note);
    } else if ((sh.considered || []).length){
      zone(body, 'What else was considered');
      sh.considered.forEach(function(c){
        row(body, { title:c.name, sub:c.why, value:String(c.score), vclass:'d' });
      });
    }
  } else {
    note(body, 'Nothing claimed', sh.no_match_reason ||
      'We do not have enough proven facts to place us against a shape yet.');
  }

  zone(body, 'What the desk watches');
  row(body, { title:'Currencies tracked', value:String(bk.currencies || 0), vclass:'d' });
  row(body, { title:'Transfer paths mapped', value:String(bk.paths || 0), vclass:'d' });
  row(body, { title:'Award prices checked', value:String(bk.prices || 0), vclass:'d' });
  row(body, { title:'Business shapes in the book', value:String(bk.shapes || 0), vclass:'d' });

  action(body, 'Ask First Officer anything', 'In your thread', 'I have a question');
  f.appendChild(body);
  return f;
}

var SCREENS = { home:screenHome, earn:screenEarn, burn:screenBurn,
                'return':screenReturn, learn:screenLearn };

/* --- chrome --------------------------------------------------------------- */
function show(id){
  var kind = (id === 'mid') ? 'home' : id;
  document.documentElement.style.setProperty('--sect', SECT[kind] || SECT.home);
  ruleEl.style.background = 'var(--sect)';
  screenEl.textContent = '';
  screenEl.appendChild(SCREENS[kind]());
  window.scrollTo(0, 0);
  Array.prototype.forEach.call(tabsEl.children, function(b){
    b.setAttribute('aria-current', String(b.dataset.id === id));
  });
  try { history.replaceState(null, '', '#' + kind); } catch (e) {}
}
function buildTabs(){
  tabsEl.textContent = '';
  TABS.forEach(function(t){
    var b = el('button', 'tab' + (t.id === 'mid' ? ' mid' : ''));
    b.type = 'button';
    b.dataset.id = (t.id === 'home') ? 'earn' : t.id;
    if (t.id === 'mid'){
      var hb = el('span','hb'); hb.appendChild(icon('chevw')); b.appendChild(hb);
    } else {
      b.appendChild(icon(t.icon));
    }
    if (t.label) b.appendChild(document.createTextNode(t.label));
    b.addEventListener('click', function(){ show(b.dataset.id); });
    tabsEl.appendChild(b);
  });
  tabsEl.hidden = false;
}
var SPLASH_AT = 0, SPLASH_MIN = 1500;

/* The read usually answers in well under a second, which makes the mark flash
   and look like a glitch rather than a moment. Hold it long enough to register,
   and never longer: if the answer takes two seconds the wait is already spent
   and nothing is added on top. */
function afterSplash(fn){
  var waited = Date.now() - SPLASH_AT;
  if (waited >= SPLASH_MIN) { fn(); return; }
  setTimeout(fn, SPLASH_MIN - waited);
}

function splash(){
  SPLASH_AT = Date.now();
  screenEl.textContent = '';
  var d = el('div','splash');
  var h = el('h2');
  h.appendChild(document.createTextNode('Talking to Your'));
  h.appendChild(document.createElement('br'));
  h.appendChild(document.createTextNode('First Officer'));
  d.appendChild(h);
  var mk = document.createElement('img');
  mk.className = 'mk'; mk.src = 'img/chev-silver.png'; mk.alt = '';
  d.appendChild(mk);
  screenEl.appendChild(d);
}

function stateScreen(title, body, cta, waText){
  screenEl.textContent = '';
  var s = el('div','state');
  s.appendChild(icon('chev','mk'));
  s.appendChild(el('h2', null, title));
  s.appendChild(el('p', null, body));
  if (cta){
    var a = el('a', null, cta);
    a.href = WA + encodeURIComponent(waText || 'Send me my app link');
    a.rel = 'noopener';
    s.appendChild(a);
  }
  screenEl.appendChild(s);
}

/* --- the hand-off ---------------------------------------------------------
   The app registers firstofficer:// and its onOpenURL already knows both
   credentials: a ?k= is stored as-is, a ?t= is spent once at fo-app-grant for
   a thirty day one. Every part of that wire existed except the part that emits
   the link. Nothing, anywhere, ever produced a firstofficer:// URL.

   So a fresh TestFlight install had an empty Keychain, opened this page with
   app=1 and no key, and got the state screen telling it to ask its thread for
   a link, which is the screen it was already stuck on. The link the thread
   sends is https, and https reaches Safari and stops there until Universal
   Links are wired at all three ends: the AASA file, the entitlement, and the
   App ID capability.

   This is the wire, and it needs none of those three. The page the https link
   opens hands the app the same credential it is itself holding. One tap, on
   the build already on the phone.

   Web only: in the app this page already has the session. And it promises
   nothing, because tapping a scheme no app claims is Safari refusing an
   address, and we cannot install an app for anyone. */
function handoff(cred, kind){
  var old = document.getElementById('handoff');
  if (old) old.parentNode.removeChild(old);
  var w = el('div','handoff'); w.id = 'handoff';
  var a = el('a', null, 'Open in the app');
  a.href = 'firstofficer://open?' + kind + '=' + encodeURIComponent(cred);
  w.appendChild(a);
  w.appendChild(el('p', null,
    'Only if the app is already on this phone. Safari refuses the address if it is not.'));
  var wrap = document.querySelector('.wrap');
  if (wrap) wrap.appendChild(w);
}

/* A page with nothing to read says so, once, instead of five tabs of blanks.
   Months observed is Earn's count of months with analysed transactions;
   balances is Burn's list of programs on file. Either one is something. */
function hasData(st){
  var months = (st && st.meta && st.meta.months_observed) || 0;
  var bal = (st && st.burn && st.burn.balances) || [];
  var flown = (st && st.meta && st.meta.flown_count) || 0;
  return months > 0 || bal.length > 0 || flown > 0;
}

/* --- boot ----------------------------------------------------------------- */
function boot(){
  // Two credentials, because two surfaces. The web page arrives with the
  // thread's fifteen minute ?t=; the native app loads this file from its own
  // bundle and passes ?k=, an owner_app read token that lasts thirty days.
  var qs = new URLSearchParams(location.search);
  var KEY = qs.get('k') || '';
  // The app has no browser chrome, so the top rule has nothing to sit under.
  // This asked for KEY, which meant a keyless cold open in the app got the
  // web page's rule and its zoomable viewport. Being in the app is the fact
  // that matters here, and the app says so with app=1.
  // And app=1 is now the whole of it. `|| !!KEY` also called a browser tab
  // holding a thirty day key the app, which is exactly backwards: it is the
  // one page in a browser that has a credential worth handing over, and it
  // was the one page the hand-off below was hidden from. Nothing is lost:
  // OwnerAppView builds app=1 unconditionally, key or no key.
  var INAPP = qs.get('app') === '1';
  if (INAPP) {
    document.documentElement.classList.add('inapp');
    // the web page keeps pinch zoom; the app is a fixed layout and should not
    // be scalable at all
    var vp = document.querySelector('meta[name=viewport]');
    if (vp) vp.setAttribute('content',
      'width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover');
  }
  TOKEN = qs.get('t') || '';
  if (!TOKEN && !KEY){
    stateScreen('This link needs to come from your thread',
      'This opens from a link we send, so it stays between us. Ask for a fresh one and we open straight back to this page.',
      'Send me a link', 'Send me my app link');
    return;
  }
  splash();
  fetch(API + (KEY ? '?k=' + encodeURIComponent(KEY)
                   : '?t=' + encodeURIComponent(TOKEN)), { cache:'no-store' })
    .then(function(r){
      return r.json().then(function(j){ return { ok:r.ok, status:r.status, j:j }; });
    })
    .then(function(res){ afterSplash(function(){
      if (res.status === 401){
        stateScreen('That link has expired',
          'App links last a few minutes on purpose, because anyone holding one could open this. Ask in your thread and a fresh one arrives straight away.',
          'Send me a new link', 'Send me my app link');
        return;
      }
      if (!res.ok || !res.j || !res.j.state){
        stateScreen('We cannot get through right now',
          'Nothing is wrong with your account. Try again in a minute, or say so in your thread and a person will look.',
          'Tell First Officer', 'The app is not loading for me');
        return;
      }
      STATE = res.j.state;
      NAME  = res.j.first_name || '';
      // Nothing to read yet. Thirty-nine of forty clients have no analysed
      // spend and no balance on file, and for them the five tabs rendered
      // blank heroes and the word undefined, which is a sentence the rows
      // never said. One honest screen instead, until there is a row to show.
      if (!hasData(STATE)){
        stateScreen('Nothing to read yet',
          'We have no transactions or balances for this business on file, so there is nothing here to show. Connect spend or send a statement in the thread and every tab fills in from it.',
          'Tell First Officer', 'I want to connect my spend to First Officer');
        return;
      }
      buildTabs();
      var want = (location.hash || '').replace('#','');
      // The landing screen is the plan and how far through it we are.
      // Earn is where the detail lives; it is not where an owner starts.
      show(SCREENS[want] ? want : 'home');
      if (!INAPP) handoff(KEY || TOKEN, KEY ? 'k' : 't');
    }); })
    .catch(function(){ afterSplash(function(){
      stateScreen('We cannot reach First Officer',
        'That is usually the connection rather than your account. Try again in a minute.',
        'Tell First Officer', 'The app is not loading for me');
    }); });
}
boot();
