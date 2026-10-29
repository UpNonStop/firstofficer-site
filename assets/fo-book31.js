/* The Found Money Call request form (book.html). Posts JSON to window.FO_BOOK_ENDPOINT when the site sets one;
   until then it packs the answers into a WhatsApp message (and an email link) so nothing a visitor types is lost,
   and says plainly that one tap is left: nothing has been sent until they tap.
   Arriving from the calculator, pricing or a trade page (book.html?industry=HVAC&spend=40000&from=calculator), the
   trade and the spend range are filled in already.
   Nothing is stored in the page or in any third-party script. */
(function(){
  var f=document.getElementById('bookform');if(!f)return;
  var msg=f.querySelector('.bk-msg'),btn=f.querySelector('button[type=submit]'),done=document.getElementById('bookdone');
  var WA='https://wa.me/16199404040?text=',MAIL='mailto:desk@upnonstop.com';
  function val(n){var e=f.querySelector('[name="'+n+'"]');return e?(e.value||'').trim():''}

  /* ---- what the visitor brought with them ---- */
  var q=new URLSearchParams(location.search),from=(q.get('from')||'').replace(/[^\w-]/g,'').slice(0,30);
  var ind=(q.get('industry')||'').replace(/[^\w &,.-]/g,'').slice(0,40).trim(),sp=parseInt((q.get('spend')||'').replace(/[^0-9]/g,''),10);
  var ALIAS={'dental practice':'Dental','marketing agency':'Agencies','agency':'Agencies','contractor':'Contractors','cpa firms':'CPA firm','law firms':'Law firm','restaurants':'Restaurant','salons':'Salon','it services':'IT and MSP','ecommerce':'E-commerce'};
  var si=f.querySelector('[name=industry]');
  if(ind&&si){var want=(ALIAS[ind.toLowerCase()]||ind).toLowerCase(),hit=null;
    [].forEach.call(si.options,function(o){if(!hit&&o.textContent.trim().toLowerCase()===want)hit=o});
    if(!hit){hit=document.createElement('option');hit.textContent=ind;var other=[].filter.call(si.options,function(o){return o.textContent==='Other'})[0];si.insertBefore(hit,other||null)}
    si.value=hit.value||hit.textContent}
  var ss=f.querySelector('[name=spend]');
  if(sp>0&&ss){var lab=sp<10000?'Under $10K':sp<25000?'$10K to $25K':sp<50000?'$25K to $50K':sp<=100000?'$50K to $100K':sp<=250000?'$100K to $250K':sp<=1000000?'$250K to $1M':'Over $1M';
    [].forEach.call(ss.options,function(o){if(o.textContent===lab)ss.value=o.value||o.textContent})}
  var exact=sp>0?'$'+sp.toLocaleString('en-US')+' a month':'';

  function lines(){var L=['First Officer Found Money Call request'];
    [['name','Name'],['email','Email'],['industry','Industry'],['spend','Card spend a month'],['phone','Phone'],['when','Good time'],['notes','Notes']].forEach(function(p){var v=val(p[0]);if(v)L.push(p[1]+': '+v)});
    if(exact&&from)L.push('From the '+(from==='calculator'?'calculator':from.replace(/-/g,' ')+' page')+': about '+exact);
    return L}
  f.addEventListener('submit',function(e){e.preventDefault();
    var name=val('name'),email=val('email');
    if(!name){msg.textContent='Your first name, so we know who to ask for.';f.querySelector('[name=name]').focus();return}
    if(!email||email.indexOf('@')<1){msg.textContent='A business email we can reply to.';f.querySelector('[name=email]').focus();return}
    var L=lines(),body=L.join('\n');
    if(window.FO_BOOK_ENDPOINT){btn.disabled=true;msg.textContent='Sending...';
      var data={};['name','email','industry','spend','phone','when','notes'].forEach(function(n){data[n]=val(n)});data.page=location.pathname;data.sent=new Date().toISOString();
      if(from)data.from=from;if(exact)data.spend_exact=exact;
      fetch(window.FO_BOOK_ENDPOINT,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
      .then(function(r){if(!r.ok)throw 0;finish(true)}).catch(function(){btn.disabled=false;msg.textContent='That did not go through. Use WhatsApp or email below, the answers are already in the message.';fallback(body)});
      return}
    fallback(body);finish(false)});
  function fallback(body){var wa=document.getElementById('bookwa'),em=document.getElementById('bookmail');
    if(wa)wa.href=WA+encodeURIComponent(body);if(em)em.href=MAIL+'?subject='+encodeURIComponent('Found Money Call request')+'&body='+encodeURIComponent(body)}
  /* sent: say so. Not sent (no endpoint yet): one tap left, and say that instead */
  function finish(sent){f.hidden=true;if(!done)return;
    if(!sent){var k=done.querySelector('.kick'),h=done.querySelector('h3'),p=done.querySelector('p');
      if(k)k.textContent='One tap left';if(h)h.textContent='Send it, and it is on its way.';
      if(p)p.textContent='Your answers are already in the message. Send it on WhatsApp or by email, and the desk replies within one business day.'}
    done.hidden=false;done.scrollIntoView({block:'nearest'})}
})();
