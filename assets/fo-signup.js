/* Newsletter sign-up: posts to the Ghost members endpoint on the live domain; everywhere else it says so instead of pretending. */
(function(){
  var LIVE=/(^|\.)upnonstop\.com$/.test(location.hostname);
  document.querySelectorAll('form[data-fo-signup]').forEach(function(f){
    var i=f.querySelector('input[type=email]'),b=f.querySelector('button'),m=f.querySelector('.cap-msg');
    if(!m){m=document.createElement('p');m.className='cap-msg';m.setAttribute('role','status');m.setAttribute('aria-live','polite');f.appendChild(m)}
    f.addEventListener('submit',function(e){e.preventDefault();var v=(i.value||'').trim();
      if(!v||v.indexOf('@')<1){m.textContent='Please enter a valid email address.';i.focus();return}
      if(!LIVE){m.textContent='Preview only: nothing was sent. On the live site this signs you up for The Daily Redemption.';return}
      b.disabled=true;m.textContent='Sending...';
      fetch(f.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:v,emailType:'signup',labels:(f.dataset.labels||'').split(','),name:''})})
      .then(function(r){if(r.ok){var row=f.querySelector('.cap-row');if(row)row.style.display='none';else{i.style.display='none';b.style.display='none'}m.textContent='Check your inbox for the confirmation link.';if(typeof gtag==='function')gtag('event','newsletter_signup',{page_path:location.pathname})}
        else{b.disabled=false;m.textContent='That did not go through. Try again in a moment.'}})
      .catch(function(){b.disabled=false;m.textContent='That did not go through. Try again in a moment.'})})})
})();
