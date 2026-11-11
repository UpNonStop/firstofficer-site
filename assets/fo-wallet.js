/* Book form, "Cards in the wallet today" (Ohad, 11 Nov: tap a bank, see its business and personal lines, toggle the cards).
   The bank chips are in the page (name="cards"). Ticking a bank adds its panel below them, built from window.FO_WALLET
   (assets/fo-wallet-cards.js, the desk's card catalog). One panel is open at a time; the others fold into a one-line
   summary. A bank with a single card (Apple Card, Robinhood) needs no panel: ticking it picks the card.
   fo-callback.js reads window.FOWallet on send:
     lines(): one line per bank, e.g. "Amex (business: Business Platinum, Business Gold / personal: Gold Card)",
              then "Other" and "Not sure" if ticked. This goes in the sheet's Cards column as it is today.
     items(): [{issuer, line, card}] per pick; line is business, personal, other (a card not in the list) or unsure. */
(function(){
  var W=window.FO_WALLET,root=document.getElementById('wallet');
  if(!W||!root)return;
  var box=root.querySelector('.wl-panels'),banks=root.querySelector('.wl-banks');
  if(!box||!banks)return;
  var by={};W.issuers.forEach(function(i){by[i.n]=i});
  var picks={};   /* bank name -> {"business|Gold": true, ...} */
  var FIND_AT=15; /* banks with this many cards or more get a "Find a card" box */

  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  function slug(s){return String(s).toLowerCase().replace(/[^a-z0-9]+/g,'-')}
  function total(i){return i.b.length+i.p.length}
  function single(i){return total(i)===1}
  function chip(bank,line,card,label){
    var v=bank+'|'+line+'|'+card;
    return '<label class="chip" data-name="'+esc((label||card).toLowerCase())+'"><input type="checkbox" name="wallet" value="'+esc(v)+'"><span>'+esc(label||card)+'</span></label>'}
  function lineHtml(i,key,title){
    var cards=i[key];if(!cards.length)return '';
    var line=key==='b'?'business':'personal',h='',sep=false;
    cards.forEach(function(c){
      if(c[1]&&!sep&&cards.some(function(x){return !x[1]})){sep=true;h+='<span class="wl-sep" aria-hidden="true">Airline, hotel and store cards</span>'}
      h+=chip(i.n,line,c[0])});
    return '<div class="wl-line" data-line="'+line+'"><span class="wl-lt">'+title+'</span><div class="chips">'+h+'</div></div>'}
  function panelHtml(i){
    var id='wl-'+slug(i.n),find=total(i)>=FIND_AT?
      '<label class="wl-find"><span class="wl-vh">Find '+(/^[AEIOU]/.test(i.n)?'an ':'a ')+esc(i.n)+' card</span><input type="search" placeholder="Find '+(/^[AEIOU]/.test(i.n)?'an ':'a ')+esc(i.n)+' card" autocomplete="off" enterkeyhint="search"></label>':'';
    return '<section class="wl-p" data-bank="'+esc(i.n)+'" aria-label="'+esc(i.n)+' cards">'+
      '<button type="button" class="wl-sum" aria-expanded="true" aria-controls="'+id+'"><b>'+esc(i.n)+'</b><span class="wl-pk"></span><span class="wl-ed">Done</span></button>'+
      '<div class="wl-body" id="'+id+'">'+find+lineHtml(i,'b','Business cards')+lineHtml(i,'p','Personal cards')+
      '<div class="wl-line wl-more"><div class="chips">'+chip(i.n,'other','','Another '+i.n+' card')+chip(i.n,'unsure','','Not sure which')+'</div></div>'+
      '</div></section>'}
  function panel(n){return box.querySelector('.wl-p[data-bank="'+n.replace(/"/g,'\\"')+'"]')}
  function bankChip(n){return banks.querySelector('input[name="cards"][value="'+n.replace(/"/g,'\\"')+'"]')}

  function parts(n){
    var p=picks[n]||{},b=[],s=[],o=false,u=false;
    Object.keys(p).forEach(function(k){var a=k.split('|');if(a[0]==='business')b.push(a[1]);else if(a[0]==='personal')s.push(a[1]);else if(a[0]==='other')o=true;else if(a[0]==='unsure')u=true});
    var order=function(line){var i=by[n],list=i?(line==='business'?i.b:i.p):[];return function(x,y){return idx(list,x)-idx(list,y)}};
    function idx(list,c){for(var j=0;j<list.length;j++)if(list[j][0]===c)return j;return 99}
    b.sort(order('business'));s.sort(order('personal'));
    return {b:b,s:s,o:o,u:u,count:b.length+s.length+(o?1:0)}}
  function summary(n){
    var x=parts(n),out=x.b.concat(x.s);
    if(x.o)out.push('another '+n+' card');
    if(x.u)out.push(out.length?'not sure about others':'not sure which');
    return out.length?out.join(', '):'Pick the cards you hold'}
  function refresh(n){
    var el=panel(n),x=parts(n),c=bankChip(n);
    if(el){el.querySelector('.wl-pk').textContent=summary(n);el.classList.toggle('has',x.count>0||x.u)}
    if(c){var sp=c.nextElementSibling;if(!sp.getAttribute('data-label'))sp.setAttribute('data-label',sp.textContent);
      sp.textContent=sp.getAttribute('data-label')+(by[n]&&!single(by[n])&&x.count?' · '+x.count:'')}}
  function setOpen(el,on){
    var b=el.querySelector('.wl-sum'),body=el.querySelector('.wl-body');
    el.classList.toggle('open',on);b.setAttribute('aria-expanded',on?'true':'false');body.hidden=!on;
    b.querySelector('.wl-ed').textContent=on?'Done':'Edit'}
  function openOnly(el){[].forEach.call(box.querySelectorAll('.wl-p'),function(p){setOpen(p,p===el)});
    var r=el.getBoundingClientRect();if(r.top>innerHeight-120||r.top<0){try{el.scrollIntoView({behavior:'smooth',block:'nearest'})}catch(e){}}}

  function addBank(n){
    var i=by[n];if(!i)return;
    if(single(i)){picks[n]={};picks[n][(i.b.length?'business':'personal')+'|'+(i.b[0]||i.p[0])[0]]=true;refresh(n);return}
    if(panel(n))return openOnly(panel(n));
    picks[n]=picks[n]||{};
    var tmp=document.createElement('div');tmp.innerHTML=panelHtml(i);var el=tmp.firstChild;
    /* panels keep the banks' order on the page, not the order they were ticked */
    var after=null,seen=false;[].forEach.call(banks.querySelectorAll('input[name="cards"]'),function(c){
      if(c.value===n){seen=true;return}if(seen&&!after&&panel(c.value))after=panel(c.value)});
    box.insertBefore(el,after);refresh(n);openOnly(el)}
  function dropBank(n){var el=panel(n);if(el)el.parentNode.removeChild(el);delete picks[n];refresh(n)}

  banks.addEventListener('change',function(e){var t=e.target;if(t.name!=='cards'||!by[t.value])return;if(t.checked)addBank(t.value);else dropBank(t.value)});
  box.addEventListener('change',function(e){var t=e.target;if(t.name!=='wallet')return;
    var a=t.value.split('|'),n=a[0],k=a[1]+'|'+a[2];picks[n]=picks[n]||{};if(t.checked)picks[n][k]=true;else delete picks[n][k];refresh(n)});
  box.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.wl-sum');if(!b)return;
    var el=b.parentNode;if(el.classList.contains('open'))setOpen(el,false);else openOnly(el)});
  box.addEventListener('input',function(e){var t=e.target;if(!t.closest||!t.closest('.wl-find'))return;
    var q=t.value.trim().toLowerCase(),el=t.closest('.wl-p');
    [].forEach.call(el.querySelectorAll('.wl-line:not(.wl-more) .chip'),function(c){
      c.hidden=!!q&&c.getAttribute('data-name').indexOf(q)<0&&!c.querySelector('input').checked});
    [].forEach.call(el.querySelectorAll('.wl-line:not(.wl-more)'),function(l){
      var any=[].some.call(l.querySelectorAll('.chip'),function(c){return !c.hidden});l.hidden=!any;
      var s=l.querySelector('.wl-sep');if(s)s.hidden=!!q})});
  /* Enter in the find box searches; it must not send the form */
  box.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.closest&&e.target.closest('.wl-find'))e.preventDefault()});
  /* a bank ticked before this script ran (back button, autofill) still gets its panel */
  [].forEach.call(banks.querySelectorAll('input[name="cards"]:checked'),function(c){if(by[c.value])addBank(c.value)});

  window.FOWallet={
    items:function(){var out=[];[].forEach.call(banks.querySelectorAll('input[name="cards"]:checked'),function(c){var n=c.value,p=picks[n];if(!by[n]||!p)return;
      Object.keys(p).forEach(function(k){var a=k.split('|');out.push({issuer:n,line:a[0],card:a[1]||''})})});return out},
    lines:function(){return [].map.call(banks.querySelectorAll('input[name="cards"]:checked'),function(c){var n=c.value,i=by[n];
      if(!i)return n;var x=parts(n),seg=[];
      if(single(i))return (i.b[0]||i.p[0])[0];
      if(x.b.length)seg.push('business: '+x.b.join(', '));
      if(x.s.length)seg.push('personal: '+x.s.join(', '));
      if(x.o)seg.push('another '+n+' card');
      if(x.u)seg.push(x.b.length||x.s.length||x.o?'not sure about others':'not sure which');
      return seg.length?n+' ('+seg.join(' / ')+')':n})}
  };
})();
