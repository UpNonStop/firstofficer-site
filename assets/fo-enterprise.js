/* "Talk to our team" on enterprise.html (Nov 2, 2026). Pricing's enterprise panel links here (#talk).
   The answers go to the same Google Apps Script web app as the Book page's call-me-back form (assets/fo-callback.js,
   backend/apps-script/): one row in the sheet "First Officer - Call-me-back requests" and one email to the desk with every
   answer. Each request is marked as enterprise three ways: the form name in the technical note ("enterprise-v1"), the page
   it came from, and the first line of the notes. The fields the sheet has no column for (entities, what runs the expenses)
   ride in the notes too.
   Required, as on Book, because the endpoint checks them again: first name, company, a phone with 10+ digits, email, time zone,
   consent. With Do Not Track or Global Privacy Control on, the technical note is cut to the page, time zone and language.
   No answer ever goes to Google Analytics: GA gets only the event name and two bands. If the endpoint cannot be reached,
   the same answers are ready to send by email in one tap, so nothing typed is lost. */
(function(){
  var ENDPOINT='https://script.google.com/macros/s/AKfycbxwvezX9s-79MevLMxzt_v6t7BRVEnvE3eMovBqiLOkETxt_sDivR5EUdpLd0dfEt5n/exec';
  var f=document.getElementById('entform'),done=document.getElementById('entdone');
  if(!f||!done)return;
  var msg=f.querySelector('.bk-msg'),btn=f.querySelector('button[type=submit]');
  var loadedAt=Date.now(),firstInput=0,opened=false,sending=false;
  var reduce=!!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
  var rid=(window.crypto&&crypto.randomUUID)?crypto.randomUUID():'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,function(c){var r=Math.random()*16|0;return(c==='x'?r:(r&3|8)).toString(16)});
  function q(n){return f.querySelector('[name="'+n+'"]')}
  function val(n){var e=q(n);return e?String(e.value||'').trim():''}
  function all(n){return [].map.call(f.querySelectorAll('input[name="'+n+'"]:checked'),function(i){return i.value})}
  function ga(name,p){if(typeof window.gtag==='function'){p=p||{};p.transport_type='beacon';try{window.gtag('event',name,p)}catch(e){}}}
  function open(){if(!opened){opened=true;ga('enterprise_form_open',{page_path:location.pathname})}}
  f.addEventListener('focusin',function(){if(!firstInput)firstInput=Date.now();open()});
  [].forEach.call(document.querySelectorAll('[data-ent-open]'),function(a){a.addEventListener('click',function(e){
    e.preventDefault();var t=document.getElementById('talk');if(!t)return;t.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});
    try{history.replaceState(null,'','#talk')}catch(x){}
    var first=q('first_name');if(first)setTimeout(function(){try{first.focus({preventScroll:true})}catch(x){first.focus()}},reduce?0:450)})});

  /* the visitor's time zone, picked for them when it is a US one */
  var tzSel=q('tz');
  try{var z=Intl.DateTimeFormat().resolvedOptions().timeZone||'',pick='';
    if(/^America\/Indiana\/(Knox|Tell_City)/.test(z))pick='America/Chicago';
    else if(/^America\/(New_York|Detroit|Indiana|Kentucky|Toronto|Nassau)/.test(z))pick='America/New_York';
    else if(/^America\/(Chicago|Menominee|North_Dakota|Winnipeg)/.test(z))pick='America/Chicago';
    else if(/^America\/(Denver|Boise|Edmonton)/.test(z))pick='America/Denver';
    else if(/^America\/Phoenix/.test(z))pick='America/Phoenix';
    else if(/^America\/(Los_Angeles|Vancouver|Tijuana)/.test(z))pick='America/Los_Angeles';
    else if(/^America\/(Anchorage|Juneau|Sitka|Nome|Yakutat|Metlakatla)/.test(z))pick='America/Anchorage';
    else if(/^Pacific\/Honolulu/.test(z))pick='Pacific/Honolulu';
    if(pick&&tzSel&&!tzSel.value)tzSel.value=pick}catch(e){}

  /* the technical note, the same keys as the Book form's */
  function cookie(k){var m=document.cookie.match(new RegExp('(?:^|; )'+k+'=([^;]*)'));return m?decodeURIComponent(m[1]):''}
  function utm(search){var p=new URLSearchParams(search||''),o={};['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','fbclid','ref','from'].forEach(function(k){var v=p.get(k);if(v)o[k]=v.slice(0,120)});return o}
  function meta(){
    var limited=navigator.doNotTrack==='1'||window.doNotTrack==='1'||navigator.globalPrivacyControl===true;
    var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}
    var m={form:'enterprise-v1',page:location.origin+location.pathname,tz_browser:tz,lang:navigator.language||'',limited:limited};
    if(limited)return m;
    var ft={},pv=0;try{ft=JSON.parse(sessionStorage.getItem('fo_ft')||'{}');pv=parseInt(sessionStorage.getItem('fo_pv'),10)||0}catch(e){}
    var nv=navigator,c=nv.connection||{},gid=cookie('_ga').match(/GA\d\.\d+\.(\d+\.\d+)$/);
    m.url=location.href.split('#')[0].slice(0,400);
    m.referrer=(document.referrer||'').slice(0,400);
    m.first_touch=ft;m.pages_this_visit=pv;m.utm=utm(location.search);
    m.languages=(nv.languages||[]).slice(0,5);
    m.local_time=new Date().toString().slice(0,64);
    m.screen=(screen.width||0)+'x'+(screen.height||0);m.viewport=innerWidth+'x'+innerHeight;m.dpr=window.devicePixelRatio||1;
    m.platform=(nv.userAgentData&&nv.userAgentData.platform)||nv.platform||'';
    m.mobile=!!((nv.userAgentData&&nv.userAgentData.mobile)||/Mobi|Android|iPhone/.test(nv.userAgent));
    m.touch_points=nv.maxTouchPoints||0;m.network=c.effectiveType||'';
    m.ga_client_id=gid?gid[1]:'';
    m.seconds_on_page=Math.round((Date.now()-loadedAt)/1000);
    return m}

  /* checks, in the order the form asks */
  function bad(name,text){var e=q(name);msg.textContent=text;if(e){e.setAttribute('aria-invalid','true');try{e.focus()}catch(x){}}return true}
  function check(){
    [].forEach.call(f.querySelectorAll('[aria-invalid]'),function(e){e.removeAttribute('aria-invalid')});
    if(!val('first_name'))return bad('first_name','Your first name, so we know who to ask for.');
    if(!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(val('email')))return bad('email','A work email, so we can reply.');
    if(val('phone').replace(/\D/g,'').length<10)return bad('phone','A phone number we can call, with the area code.');
    if(!val('tz'))return bad('tz','Your time zone, so we call at the right hour.');
    if(!val('business'))return bad('business','The company name, so we can prepare.');
    if(!q('consent').checked)return bad('consent','Tick the box so we can call, text or email you about this.');
    return false}

  function notesText(){
    var head=['Enterprise inquiry'],ent=val('entities'),stack=val('stack');
    if(ent)head.push('Entities: '+ent);if(stack)head.push('Expenses run on: '+stack);
    var n=val('notes');return head.join(' · ')+(n?'\n'+n:'')}
  function bodyText(d){var L=['Enterprise inquiry','Name: '+d.first_name+(d.last_name?' '+d.last_name:''),'Company: '+d.business];if(d.role)L.push('Role: '+d.role);L.push('Phone: '+d.phone,'Email: '+d.email,'Reply by: '+d.confirm_by);
    if(d.cardholders)L.push('People with company cards: '+d.cardholders);if(d.spend)L.push('Card spend a month: '+d.spend);
    if(d.industry)L.push('Industry: '+d.industry);if(d.cards.length)L.push('Card issuers: '+d.cards.join(', '));
    if(d.goals.length)L.push('Wants: '+d.goals.join(', '));if(d.urgency)L.push('Start: '+d.urgency);L.push('Notes: '+d.notes);
    return L.join('\n')}
  function mailText(d){return 'mailto:desk@upnonstop.com?subject='+encodeURIComponent('Enterprise inquiry: '+d.first_name+', '+d.business)+'&body='+encodeURIComponent(bodyText(d))}
  function fallback(d,lead){msg.textContent=lead;var m=document.createElement('a');m.href=mailText(d);m.textContent='Send them by email';msg.appendChild(m);msg.appendChild(document.createTextNode('.'))}
  function set(k,v){[].forEach.call(done.querySelectorAll('[data-ent="'+k+'"]'),function(e){e.textContent=v})}
  var CH={'Under 10':'under 10','10 to 25':'10 to 25','26 to 100':'26 to 100','101 to 500':'101 to 500','501 to 2,000':'501 to 2000','Over 2,000':'over 2000'};
  var SP={'Under $100K':'under 100K','$100K to $250K':'100K to 250K','$250K to $1M':'250K to 1M','$1M to $5M':'1M to 5M','Over $5M':'over 5M','Not sure':'not sure'};

  f.addEventListener('submit',function(e){e.preventDefault();if(sending)return;msg.textContent='';if(check())return;
    var d={request_id:rid,first_name:val('first_name'),last_name:val('last_name'),business:val('business'),role:val('role'),
      phone:val('phone'),email:val('email'),confirm_by:(all('confirm_by')[0]||'Email'),tz:val('tz'),urgency:val('urgency'),
      days:[],times:[],industry:val('industry'),spend:val('spend'),cardholders:val('cardholders'),points:'',
      cards:all('cards'),spend_lines:[],goals:all('goals'),trip:'',notes:notesText(),heard:val('heard'),
      consent:true,consent_text:(f.querySelector('.cbconsent span')||{}).textContent||'',company_site:val('company_site'),
      fill_ms:Date.now()-(firstInput||loadedAt),meta:meta()};
    sending=true;btn.disabled=true;btn.setAttribute('aria-busy','true');msg.textContent='Sending...';
    /* text/plain and no-cors: a "simple" request, so the browser sends it straight to Apps Script with no preflight.
       The reply cannot be read (opaque), so a request that leaves the browser counts as sent; only a network failure falls back. */
    var ctl=window.AbortController?new AbortController():null,timer=setTimeout(function(){if(ctl)ctl.abort()},20000);
    fetch(ENDPOINT,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(d),signal:ctl?ctl.signal:undefined})
    .then(function(){clearTimeout(timer);sending=false;msg.textContent='';
      f.hidden=true;set('name',d.first_name);set('by',d.confirm_by==='WhatsApp'?'WhatsApp':d.confirm_by.toLowerCase());set('ref','FO-'+rid.replace(/[^a-z0-9]/gi,'').slice(0,8).toUpperCase());
      done.hidden=false;try{done.focus({preventScroll:true})}catch(x){}done.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});
      ga('generate_lead',{page_path:location.pathname,method:'enterprise_form',cardholders_band:CH[d.cardholders]||'unknown',spend_band:SP[d.spend]||'unknown'})})
    .catch(function(){clearTimeout(timer);sending=false;btn.disabled=false;btn.removeAttribute('aria-busy');
      fallback(d,'That did not go through. Try again, or send the same answers in one tap: ')});
  });
})();
