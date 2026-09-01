/* ============================================================================
   Your First Officer, the owner's app.

   One fetch, five tabs. This file selects strings out of the payload and puts
   them on screen. It does not add, divide, round or format a single number:
   fo_app_state did that in SQL, so every surface says the same thing and the
   money has one author. Search this file for arithmetic and you will not find
   any. That is deliberate, and predeploy_app_state.ts fails the deploy if the
   edge function ever starts doing it either.
   ========================================================================== */
'use strict';

var API  = 'https://cuzuzzbezswvejnoskum.supabase.co/functions/v1/fo-app-state';
var WA   = 'https://wa.me/16199404040?text=';
var TABS = [
  { id:'home',   label:'Earn',   icon:'i-earn'  },
  { id:'burn',   label:'Burn',   icon:'i-burn'  },
  { id:'mid',    label:'Home',   icon:null      },
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
  var e = s.earn || {}, b = s.burn || {};
  var top = (e.lines || [])[0];
  hero(f,'home','Where you stand', e.annual_gain_text || ('$' + (e.annual_gain_usd || 0)),
    'found in bills you were already paying, across ' + (e.months_observed || 0) + ' months of statements.');
  var body = el('div','body');

  zone(body, 'Needs you');
  if (top) row(body, { tone:'a', title:top.label + ' could earn more',
    sub:'you are on the ' + top.using_now + ', the ' + top.use_instead + ' pays more',
    value:'$' + top.annual_gain_usd, vclass:'g' });
  var best = (b.destinations || [])[0];
  if (best) row(body, { tone:'p', title:best.trips + ' trips waiting on a date',
    sub:best.zone + ', ' + best.cabin + ' class', value:'Free', vclass:'p' });

  zone(body, 'Going well');
  row(body, { tone:'g', title:e.already_correct_txns + ' charges already on the right card',
    value:'$' + e.already_correct_spend_usd, vclass:'g' });
  if (b.transferable_text) row(body, { tone:'g', title:'Points that can move to an airline',
    sub:'across the currencies with a live transfer path', value:b.transferable_text, vclass:'d' });

  action(body, 'Pick your dates', 'First one free', 'I want to book a trip');
  f.appendChild(body);
  return f;
}

function screenEarn(){
  var e = STATE.earn || {}, f = document.createDocumentFragment();
  hero(f,'earn','Room to grow', e.annual_gain_text || '', 
    e.switches + ' moves across cards you already hold. Nothing to apply for.');
  var body = el('div','body');

  zone(body, 'Ranked by what they pay');
  (e.lines || []).forEach(function(l){
    row(body, { title:l.label,
      sub:'on the ' + l.using_now + ', move to the ' + l.use_instead +
          (l.condition ? '. ' + l.condition : ''),
      badge:l.rate_better_cpd && l.rate_now_cpd ? null : null,
      value:'$' + l.annual_gain_usd, vclass:'g' });
  });

  if (e.must_state) note(body, 'How to read this', e.must_state);
  if (e.scope) note(body, 'What this covers', e.scope);
  note(body, 'What we cannot do',
    'We read your statements one to three days after a charge and message you. We never touch a card at the register and we never move a card for you. We spot it, you tap the card.');
  action(body, 'Send me the whole map', e.annual_gain_text + ' a year', 'Send me the routing map');
  f.appendChild(body);
  return f;
}

function screenBurn(){
  var b = STATE.burn || {}, f = document.createDocumentFragment();
  var find = b.find;
  hero(f,'burn','What the balance buys', b.transferable_text || '0',
    'transferable points, across the currencies with a live path to an airline.', true);
  var body = el('div','body');

  if (find){
    zone(body, 'The find');
    card(body, find.origin + ' to ' + find.destination + ', ' + find.program,
      find.points_text, 'The cheapest chart this wallet can reach wants ' +
      find.chart_points_text + '. Verified ' + find.last_verified + '.');
    var p = el('div','pair');
    [['You would pay', find.points_text + ' pts'],
     ['Taxes', '$' + find.taxes_usd],
     ['Points saved', find.saved_points_text],
     ['Worth', find.saved_usd_text]].forEach(function(kv){
      var d = el('div'); d.appendChild(el('p','k',kv[0])); d.appendChild(el('p','v2',kv[1]));
      p.appendChild(d);
    });
    body.appendChild(p);
  }

  zone(body, 'Where you can go');
  (b.destinations || []).forEach(function(d){
    row(body, { title:d.zone + ', ' + d.cabin, sub:d.points_text + ' points each round trip',
      value:String(d.trips), vclass:'p' });
  });

  zone(body, 'What you hold');
  (b.balances || []).forEach(function(x){
    row(body, { tone:x.transferable ? 'g' : null, title:x.program,
      sub:x.freshness + ', read ' + x.days_old + ' days ago' +
          (x.transferable ? '' : '. No transfer path from this one.'),
      value:x.balance_text, vclass:'d' });
  });

  if (b.flown_note) note(body, 'Nothing flown yet', b.flown_note);
  action(body, 'Ask for these dates', 'First one free', 'I want to use my points');
  f.appendChild(body);
  return f;
}

function screenReturn(){
  var r = STATE['return'] || {}, f = document.createDocumentFragment();
  hero(f,'return','Since you joined', r.found_annual_text || '$0',
    'found in bills you were already paying. This number only goes up.');
  var body = el('div','body');

  zone(body, 'What we have found');
  row(body, { tone:'g', title:'Every year, from the switches',
    sub:r.switches + ' moves across cards you already hold', value:r.found_annual_text, vclass:'g' });
  row(body, { tone:'g', title:'Every trip, on top of that',
    sub:'against the cheapest published price this wallet can reach', value:r.per_trip_text, vclass:'g' });
  row(body, { tone:'g', title:'What the next seat is worth',
    sub:'at the top of the band for these points', value:r.seat_text, vclass:'g' });

  note(body, 'Two different units', r.units_note +
    '. The first is a year of bills. The second happens each time you fly.');
  note(body, 'Reading since', 'We started counting on ' + r.reading_since +
    ' and have never counted down from a fee. Everything above is what was found, not what is owed.');
  action(body, 'See the full report', 'Sent to you', 'Send me my return report');
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
    zone(body, 'What else was considered');
    (sh.considered || []).forEach(function(c){
      row(body, { title:c.name, sub:c.why, value:String(c.score), vclass:'d' });
    });
  } else {
    note(body, 'Nothing claimed', sh.no_match_reason ||
      'We do not have enough proven facts to place you against a shape yet.');
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
    b.appendChild(document.createTextNode(t.label));
    b.addEventListener('click', function(){ show(b.dataset.id); });
    tabsEl.appendChild(b);
  });
  tabsEl.hidden = false;
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

/* --- boot ----------------------------------------------------------------- */
function boot(){
  TOKEN = new URLSearchParams(location.search).get('t') || '';
  if (!TOKEN){
    stateScreen('This link needs to come from your thread',
      'Your app opens from a link First Officer sends you, so nobody else can read your numbers. Ask for a fresh one and it opens straight to this page.',
      'Send me a link', 'Send me my app link');
    return;
  }
  stateScreen('Reading your statements', 'One moment.');
  fetch(API + '?t=' + encodeURIComponent(TOKEN), { cache:'no-store' })
    .then(function(r){
      return r.json().then(function(j){ return { ok:r.ok, status:r.status, j:j }; });
    })
    .then(function(res){
      if (res.status === 401){
        stateScreen('That link has expired',
          'App links last a few minutes on purpose, because anyone holding one can read your numbers. Ask in your thread and a fresh one arrives straight away.',
          'Send me a new link', 'Send me my app link');
        return;
      }
      if (!res.ok || !res.j || !res.j.state){
        stateScreen('We cannot read your numbers right now',
          'Nothing is wrong with your account. Try again in a minute, or say so in your thread and a person will look.',
          'Tell First Officer', 'The app is not loading for me');
        return;
      }
      STATE = res.j.state;
      NAME  = res.j.first_name || '';
      buildTabs();
      var want = (location.hash || '').replace('#','');
      show(SCREENS[want] ? want : 'earn');
    })
    .catch(function(){
      stateScreen('We cannot reach First Officer',
        'That is usually the connection rather than your account. Try again in a minute.',
        'Tell First Officer', 'The app is not loading for me');
    });
}
boot();
