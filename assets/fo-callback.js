/* "Call me back" on book.html (option four). The card's button opens the form in place, no overlay.
   On send, the answers and a short technical note go to the desk's Google Apps Script web app, which adds a row to the
   Google Sheet "First Officer - Call-me-back requests" and emails the desk every detail (backend/apps-script/, DEPLOY.md there).
   With Do Not Track or Global Privacy Control on, the technical note is cut to the page, time zone and language.
   No answer from this form ever goes to Google Analytics: GA gets only the event name, the trade and a spend band.
   If the endpoint is not set yet, or cannot be reached, the same answers are ready to send on WhatsApp or by email,
   so nothing typed is lost. */
(function(){
  /* The one setting: the Apps Script web app URL (Deploy > Web app, ends in /exec). Empty = WhatsApp and email only. */
  var CALLBACK_ENDPOINT='';
  var sec=document.getElementById('callback'),f=document.getElementById('cbform'),done=document.getElementById('cbdone');
  if(!sec||!f)return;
  var msg=f.querySelector('.bk-msg'),btn=f.querySelector('button[type=submit]');
  var loadedAt=Date.now(),openedAt=0,firstInput=0,sending=false;
  var reduce=!!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches);
  var rid=(window.crypto&&crypto.randomUUID)?crypto.randomUUID():'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,function(c){var r=Math.random()*16|0;return(c==='x'?r:(r&3|8)).toString(16)});
  var openers=[].slice.call(document.querySelectorAll('[data-cb-open]'));
  function q(n){return f.querySelector('[name="'+n+'"]')}
  function val(n){var e=q(n);return e?String(e.value||'').trim():''}
  function all(n){return [].map.call(f.querySelectorAll('input[name="'+n+'"]:checked'),function(i){return i.value})}
  function ga(name,p){if(typeof window.gtag==='function'){p=p||{};p.transport_type='beacon';try{window.gtag('event',name,p)}catch(e){}}}

  /* ---- open in place ---- */
  function open(focus){
    if(sec.hidden){sec.hidden=false;openedAt=Date.now();ga('callback_open',{page_path:location.pathname})}
    openers.forEach(function(a){a.setAttribute('aria-expanded','true')});
    sec.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});
    if(focus!==false){var first=q('first_name');if(first)setTimeout(function(){try{first.focus({preventScroll:true})}catch(e){first.focus()}},reduce?0:420)}
  }
  openers.forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();open();try{history.replaceState(null,'','#callback')}catch(err){}})});
  if(location.hash==='#callback')open(false);
  f.addEventListener('focusin',function(){if(!firstInput)firstInput=Date.now()});

  /* ---- what the visitor brought with them ---- */
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
  var sp=new URLSearchParams(location.search);
  var ind=(sp.get('industry')||'').replace(/[^\w &,.-]/g,'').slice(0,40).trim().toLowerCase();
  var si=q('industry');if(ind&&si)[].forEach.call(si.options,function(o){if(o.textContent.trim().toLowerCase()===ind)si.value=o.value||o.textContent});
  var n=parseInt((sp.get('spend')||'').replace(/[^0-9]/g,''),10),ss=q('spend');
  if(n>0&&ss){var lab=n<10000?'Under $10K':n<25000?'$10K to $25K':n<50000?'$25K to $50K':n<=100000?'$50K to $100K':n<=250000?'$100K to $250K':n<=1000000?'$250K to $1M':'Over $1M';
    [].forEach.call(ss.options,function(o){if(o.textContent===lab)ss.value=o.value||o.textContent})}

  /* ---- the technical note ---- */
  function cookie(k){var m=document.cookie.match(new RegExp('(?:^|; )'+k+'=([^;]*)'));return m?decodeURIComponent(m[1]):''}
  function utm(search){var p=new URLSearchParams(search||''),o={};['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','fbclid','ref','from'].forEach(function(k){var v=p.get(k);if(v)o[k]=v.slice(0,120)});return o}
  function meta(){
    var limited=navigator.doNotTrack==='1'||window.doNotTrack==='1'||navigator.globalPrivacyControl===true;
    var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}
    var m={form:'callback-v1',page:location.origin+location.pathname,tz_browser:tz,lang:navigator.language||'',limited:limited};
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

  /* ---- checks, in the order the form asks ---- */
  function bad(name,text){var e=q(name);msg.textContent=text;if(e){e.setAttribute('aria-invalid','true');try{e.focus()}catch(x){}}return true}
  function check(){
    [].forEach.call(f.querySelectorAll('[aria-invalid]'),function(e){e.removeAttribute('aria-invalid')});
    if(!val('first_name'))return bad('first_name','Your first name, so we know who to ask for.');
    if(!val('business'))return bad('business','The business name, so we can prepare.');
    if(val('phone').replace(/\D/g,'').length<10)return bad('phone','A mobile number we can call, with the area code.');
    if(!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(val('email')))return bad('email','A business email, so we can reach you if the call drops.');
    if(!val('tz'))return bad('tz','Your time zone, so we call at the right hour.');
    if(!q('consent').checked)return bad('consent','Tick the box so we can call or text this number.');
    return false}

  function list(a){return a.length<2?a.join(''):a.slice(0,-1).join(', ')+' or '+a[a.length-1]}
  function tzLabel(v){var o=tzSel&&[].filter.call(tzSel.options,function(x){return x.value===v})[0];return o?o.textContent.replace(/\s*\(.*\)$/,''):''}
  function whenLine(d){
    var days=d.days.length?'on '+list(d.days):'',times=d.times.length?list(d.times.map(function(t){return t.split(',')[0].toLowerCase()})):'';
    var parts=[days,times].filter(Boolean).join(', ');
    return 'We will call '+d.phone+' '+(parts?parts+', ':'at a time that suits you, ')+tzLabel(d.tz)+' time. We confirm it first by '+(d.confirm_by||'text message').toLowerCase()+'.'}
  function waText(d){var L=['First Officer callback request','Name: '+d.first_name+(d.last_name?' '+d.last_name:''),'Business: '+d.business,'Phone: '+d.phone,'Email: '+d.email,'Time zone: '+tzLabel(d.tz)];
    if(d.days.length)L.push('Days: '+d.days.join(', '));if(d.times.length)L.push('Time: '+d.times.join('; '));
    if(d.industry)L.push('Industry: '+d.industry);if(d.spend)L.push('Card spend a month: '+d.spend);if(d.notes)L.push('Notes: '+d.notes);
    return 'https://wa.me/16199404040?text='+encodeURIComponent(L.join('\n'))}
  function mailText(d){var u=decodeURIComponent(waText(d).split('?text=')[1]);return 'mailto:desk@upnonstop.com?subject='+encodeURIComponent('Callback request: '+d.first_name+', '+d.business)+'&body='+encodeURIComponent(u)}
  function fallback(d,lead){msg.textContent=lead;
    var a=document.createElement('a');a.href=waText(d);a.target='_blank';a.rel='noopener';a.textContent='💬 Send on WhatsApp';msg.appendChild(a);
    msg.appendChild(document.createTextNode(' or '));
    var m=document.createElement('a');m.href=mailText(d);m.textContent='✉️ send by email';msg.appendChild(m);msg.appendChild(document.createTextNode('.'))}
  function set(k,v){[].forEach.call(done.querySelectorAll('[data-cb="'+k+'"]'),function(e){e.textContent=v})}
  var BAND={'Under $10K':'under 10K','$10K to $25K':'10K to 25K','$25K to $50K':'25K to 50K','$50K to $100K':'50K to 100K','$100K to $250K':'100K to 250K','$250K to $1M':'250K and up','Over $1M':'250K and up'};

  f.addEventListener('submit',function(e){e.preventDefault();if(sending)return;msg.textContent='';if(check())return;
    var d={request_id:rid,first_name:val('first_name'),last_name:val('last_name'),business:val('business'),role:val('role'),
      phone:val('phone'),email:val('email'),confirm_by:(all('confirm_by')[0]||''),tz:val('tz'),urgency:val('urgency'),
      days:all('days'),times:all('times'),industry:val('industry'),spend:val('spend'),cardholders:val('cardholders'),points:val('points'),
      cards:all('cards'),spend_lines:all('spend_lines'),goals:all('goals'),trip:val('trip'),notes:val('notes'),heard:val('heard'),
      consent:true,consent_text:(f.querySelector('.cbconsent span')||{}).textContent||'',company_site:val('company_site'),
      fill_ms:Date.now()-(firstInput||openedAt||loadedAt),meta:meta()};
    if(!CALLBACK_ENDPOINT){fallback(d,'One tap to send these answers to the desk: ');ga('callback_handoff',{page_path:location.pathname});return}
    sending=true;btn.disabled=true;btn.setAttribute('aria-busy','true');msg.textContent='Sending...';
    /* text/plain and no-cors: a "simple" request, so the browser sends it straight to Apps Script with no preflight.
       The reply cannot be read (opaque), so a request that leaves the browser counts as sent; only a network failure falls back. */
    var ctl=window.AbortController?new AbortController():null,timer=setTimeout(function(){if(ctl)ctl.abort()},20000);
    fetch(CALLBACK_ENDPOINT,{method:'POST',mode:'no-cors',headers:{'Content-Type':'text/plain;charset=utf-8'},body:JSON.stringify(d),keepalive:true,signal:ctl?ctl.signal:undefined})
    .then(function(){clearTimeout(timer);sending=false;msg.textContent='';
      f.hidden=true;set('name',d.first_name);set('ref','FO-'+rid.replace(/[^a-z0-9]/gi,'').slice(0,8).toUpperCase());set('line',whenLine(d));
      done.hidden=false;try{done.focus({preventScroll:true})}catch(x){}done.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});
      ga('generate_lead',{page_path:location.pathname,method:'callback_form',industry:(d.industry||'not given').slice(0,40),spend_band:BAND[d.spend]||'unknown'})})
    .catch(function(){clearTimeout(timer);sending=false;btn.disabled=false;btn.removeAttribute('aria-busy');
      fallback(d,'That did not go through. Try again, or send the same answers in one tap: ')});
  });
})();
