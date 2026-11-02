/* calculator.html · Go advanced (31 Oct 2026). Ohad: "if we do advanced - then advance and sophisticated it is".
   Every line of a business's spend, in ten groups, each with its own monthly amount and how it is paid today. No catch-all line.
   The desk side: every line on a card goes through the universal card stack, inside each card's yearly cap:
     Ink Business Cash      5x office supply stores + internet, cable and phone, $25K a year combined; 2x gas stations + restaurants, $25K a year combined
     Amex Business Gold     4x on its top 2 of 6 categories each month, $150K a year combined (the desk tries every pair and keeps the best)
     Ink Business Preferred 3x travel, shipping, internet, cable and phone, search and social ads, $150K a year combined
     Blue Business Plus     2x everyday purchases, $50K a year;  past every cap, a line stays on the card it is on today (never under 1x)
   A card only takes a line it improves: the desk never moves spend to a card that earns less than it does today.
   Value: FO_REDEMPTION_BASIS (every extra point counted, cents a point by use), card annual fees shown but not taken off, against the $550 a month fee.
   Lines not on a card are not counted. Nothing typed here is stored or sent from this script. Every figure is an estimate; terms as understood Oct 2026.
   URL: ?ind=<slug> or ?industry=<name or slug> picks the industry, ?ex=<first name> its example's industry, ?spend=<n> scales the mix to n a month. */
(function(){
'use strict';
var BS=window.FO_REDEMPTION_BASIS,C=window.FO_CALC,root=document.getElementById('adx');if(!BS||!C||!root)return;var sec=document.getElementById('advs')||root;
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var FEE=BS.fee/12,GATE=BS.gate,UTIL=BS.util,GMAX=80000,BIG=250000;
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function pts(n){n=Math.round(n);var a=Math.abs(n),s=n<0?'−':'';return s+(a>=1e6?(Math.round(a/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':a>=1e3?Math.round(a/1e3)+'k':''+a)}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function r10(n){return Math.round(n/10)*10}
function u10(n){return usd(r10(n))}
function x(n){return (+n).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'x'}
function c2(n){return (+n).toFixed(2).replace(/0$/,'').replace(/0$/,'').replace(/\.$/,'.0')+'¢'}
function sg(n){n=r10(n);return (n<0?'−':'+')+usd(Math.abs(n))}
function nx(v){return (v<0?0:v).toFixed(1)+'×'}
function kmo(v){return v>=1e6?'$'+(Math.round(v/1e5)/10).toString().replace(/\.0$/,'')+'M':'$'+Math.round(v/1e3)+'K'}
function ks(v){v=Math.round(v);return v<1000?usd(v):v<1e4?'$'+(v/1000).toFixed(1).replace(/\.0$/,'')+'K':v<1e6?'$'+Math.round(v/1000)+'K':'$'+(Math.round(v/1e5)/10).toString().replace(/\.0$/,'')+'M'}
function rng(t){return t.floor===t.ceil?c2(t.floor):c2(t.floor)+' to '+c2(t.ceil)}
function slug(t){return String(t||'').toLowerCase().replace(/[^a-z]+/g,'-').replace(/^-|-$/g,'')}
function U(id){for(var i=0;i<BS.types.length;i++)if(BS.types[i].id===id)return BS.types[i];return BS.types[0]}
function pc(v,m){return Math.max(0,Math.min(100,m?v/m*100:0))+'%'}

/* ---------------- the card stack, every line in ten groups, and how lines are paid today: in fo-calc-core.js, shared with Basic ---------------- */
var CARD=C.CARD,BK=C.BK,ABGC=C.ABGC,G=C.G,LN=C.LN,LI=C.LI,TODAY=C.TODAY,TR=C.TR;
function tShort(k){return k==='none'?'Not on a card':/^c/.test(k)?TR[k][1].replace(' cash back',' back'):x(TR[k][2])}

/* ---------------- the 21 industries and every name that reaches this page: in fo-calc-core.js ---------------- */
var IND=C.IND,ALIAS=C.ALIAS;
/* ---------------- state: the industry both modes share starts where fo-calc-core.js put it (?ind=, ?industry=, ?ex=, the trade page the visitor came from, else Other) ---------------- */
var A={},T={},use='mix',mix='ex',idx=C.idx,first=true;
var q=location.search,qp=C.qp,VIA=C.via,SP=C.sp;

/* ---------------- the month and the verdict: the one model in fo-calc-core.js, the same one Basic uses ---------------- */
function model(){return C.model(A,T,use,mix)}
var verdict=C.verdict;

/* ---------------- painting ---------------- */
function tw(el,to,fmt){if(!el)return;var from=el._c==null?to:el._c;cancelAnimationFrame(el._r);
  if(RM||first||from===to){el._c=to;el.textContent=fmt(to);return}
  var t0=null;function f(ts){if(t0==null)t0=ts;var p=Math.min(1,(ts-t0)/200),e=1-Math.pow(1-p,3);el._c=from+(to-from)*e;el.textContent=fmt(el._c);if(p<1)el._r=requestAnimationFrame(f)}
  el._r=requestAnimationFrame(f)}
function K(n,to,fmt){$$('[data-k="'+n+'"]',sec).forEach(function(e){tw(e,to,fmt)})}
function S(n,v){$$('[data-k="'+n+'"]',sec).forEach(function(e){e.textContent=v})}
function bar(bal,r){var mid=Math.max(0,r.mid),bm=FEE*Math.max(3,Math.ceil(Math.max(0,r.hi)*1.1/FEE));S('bmax',usd(bm));
  $('.base',bal).style.width=pc(Math.min(mid,FEE),bm);
  var ov=$('.over',bal);ov.style.left=pc(FEE,bm);ov.style.width=pc(Math.max(0,mid-FEE),bm);
  var sh=$('.short',bal);sh.style.left=pc(Math.min(mid,FEE),bm);sh.style.width=pc(Math.max(0,FEE-mid),bm);sh.setAttribute('data-t',mid<FEE?'short '+u10(FEE-mid):'');
  var rg=$('.rng',bal),lo=Math.max(0,r.lo),hi=Math.max(0,r.hi);rg.style.left=pc(lo,bm);rg.style.width=pc(hi-lo,bm);
  $('.mark',bal).style.left=pc(FEE,bm);$('.mark',bal).classList.toggle('lo',FEE/bm<.12);
  bal.setAttribute('aria-label','Your desk finds about '+u10(mid)+' a month, est., against the $550 a month fee')}
function bname(b,l){if(b==='abg4')return {c:'abg',r:4,w:'Amex Business Gold',k:ABGC[l.e.abg]};if(b==='ibp3')return {c:'ibp',r:3,w:'Ink Business Preferred',k:l.e.ibp3};
  if(b==='ibc5')return {c:'ibc',r:5,w:'Ink Business Cash',k:l.e.ibc5};if(b==='ibc2')return {c:'ibc',r:2,w:'Ink Business Cash',k:'gas and restaurants'};
  if(b==='bbp2')return {c:'bbp',r:2,w:'Blue Business Plus',k:'everyday purchases'};if(b==='cap2')return {c:'cap',r:2,w:'Capital One Venture Business',k:'every purchase'};return {c:'',r:1,w:'1x past the caps',k:''}}
function bnameO(b,o){var n=bname(b,o.l);if(b==='base'&&o.tr>1){n.r=o.tr;n.w='the card it is on today';n.k=''}return n}
function parts(r,i){var al=r.R.al[i],o=r.rows[i],out=[];BK.forEach(function(b){if(al[b.id]>0)out.push({b:b.id,a:al[b.id]/12,n:bnameO(b.id,o)})});return out}
function desc(ps){if(ps.length===1){var p=ps[0];return p.n.c?'on '+p.n.w+(p.n.k?' ('+p.n.k+')':''):(p.n.r>1?'stays on the card it is on today':'past the yearly caps')}
  return 'from '+ps.map(function(p,j){var s=p.n.c?p.n.r+'x '+p.n.w+(p.n.k?' ('+p.n.k+')':''):(p.n.r>1?p.n.r+'x on the card it is on today':'1x past the caps');return (j?'then ':'')+s+' on '+ks(p.a)}).join(', ')}

function paint(){var r=model(),v=verdict(r);
  var fm=function(n){return '~'+u10(Math.max(0,n))};
  K('find',r.mid,fm);K('m-find',r.mid,fm);
  S('findr',r.flat?'at '+c2(r.u.floor)+' a point':u10(Math.max(0,r.lo))+' to '+u10(Math.max(0,r.hi)));
  S('cfees',r.cf>0?'Before about '+usd(r.cf)+' a month in card annual fees, est.':'No card annual fees in this stack, est.');
  K('net',r.mid-FEE,sg);S('netr',r.flat?'at '+c2(r.u.floor)+' a point':sg(r.lo-FEE)+' to '+sg(r.hi-FEE)+', est.');
  K('rx',Math.max(0,r.mid)/FEE,nx);K('m-rx',Math.max(0,r.mid)/FEE,nx);S('rxr',r.flat?'at '+c2(r.u.floor)+' a point':nx(Math.max(0,r.lo)/FEE)+' to '+nx(Math.max(0,r.hi)/FEE)+', est.');
  K('plus',Math.max(0,r.d-r.t),function(n){return '+'+pts(n)});
  K('mo',r.mo,usd);K('bl',r.mo?r.t/r.mo:0,x);K('vt',r.t,pts);K('dl',r.mo?r.d/r.mo:0,x);
  S('off',r.off?usd(r.off)+' a month marked not on a card is not counted.':'');
  S('who',(IND[idx][0]==='other'?'Your mix':IND[idx][1])+' · at '+rng(r.u)+' a point');S('gatev','You: '+kmo(r.mo));
  var gt=$('#xgt');$('.fill',gt).style.width=pc(r.mo,GMAX);$('.fee',gt).style.left=pc(GATE,GMAX);gt.classList.toggle('under',r.mo<GATE);
  bar($('#xbal'),r);
  $('#xv').className='cv '+v.c;$('.cres',root).className='cres '+v.c+(r.mid>=1e4?' big':'');$('.cmini',root).className='cmini '+v.c;
  $('#xvt').textContent=v.t;$('#xvp').innerHTML=v.p+(v.c==='no'?' <a href="freebies.html">Get the Freebies →</a>':'');
  $$('.bvk',root).forEach(function(b){b.textContent=v.c==='fit'?'✓':v.c==='meh'?'≈':'×'});
  /* group totals and per-line answers */
  G.forEach(function(g){var s=0,n=0;g.L.forEach(function(l){var m=A[l[0]]||0;s+=m;if(m)n++});var e=$('[data-gt="'+g.id+'"]',root);if(e)e.textContent=usd(s);var c=$('[data-gn="'+g.id+'"]',root);if(c)c.textContent=n?n+(n>1?' lines':' line'):'none yet'});
  var map={};r.rows.forEach(function(o,i){map[o.l.id]=i});
  LN.forEach(function(l){var el=$('[data-lr="'+l.id+'"]',root);if(!el)return;var m=A[l.id]||0;
    if(!m){el.textContent='';el.className='xlr';return}
    if(map[l.id]==null){el.textContent='Not on a card: not counted.';el.className='xlr off';return}
    var i=map[l.id],ps=parts(r,i),o=r.rows[i],dp=0;ps.forEach(function(p){dp+=p.a*p.n.r});var ex=Math.max(0,dp-o.m*o.tr);
    el.innerHTML='With the desk: <b>'+x(dp/o.m)+'</b> '+desc(ps)+' · <em>'+(ex>0?'+'+pts(ex)+' points a month':'no extra points')+', est.</em>';el.className='xlr'});
  stack(r);table(r,map);first=false}

/* the card stack: what each card carries, and how much of its yearly cap */
function stack(r){var R=r.R,rows=r.rows,box=$('#xcards'),html='';
  function who(b){var n=[];rows.forEach(function(o,i){if(R.al[i][b]>0)n.push(o.l.n)});return n}
  function meter(b,cap,lab){var used=R.cu[b]||0;return '<div class="xcm"><span>'+lab+'</span><i role="img" aria-label="'+ks(used/12)+' a month, '+Math.round(used/cap*100)+'% of the yearly cap"><b style="width:'+pc(used,cap)+'"></b></i><small>'+ks(used)+' of '+ks(cap)+' a year</small></div>'}
  function tile(c,body,on,ptsM){return '<div class="xc'+(on?'':' idle')+'" data-c="'+c+'"><div class="xch"><b>'+CARD[c].n+'</b><small>'+(CARD[c].fee?'$'+CARD[c].fee+' a year':'No annual fee')+', est.</small></div><p class="xct">'+CARD[c].t+'</p>'+body+'<p class="xcp">'+(on?'<b>'+pts(ptsM)+'</b> points a month, est.':'Not needed for this mix.')+'</p></div>'}
  function pm(bs){var s=0;bs.forEach(function(b){var bk=BK.filter(function(z){return z.id===b})[0];s+=(R.cu[b]===Infinity?0:R.cu[b]||0)*bk.r});return s/12}
  var abgW=who('abg4'),ibpW=who('ibp3'),i5=who('ibc5'),i2=who('ibc2'),bbW=who('bbp2'),cpW=who('cap2');
  /* only the Business Gold categories that carry a line in this mix (the pair can include one the cap leaves no room for) */
  var abgC=R.pair.filter(function(c){return rows.some(function(o,i){return o.l.e.abg===c&&R.al[i].abg4>0})});
  html+=tile('abg',(abgW.length?'<p class="xcl"><span>This mix:</span> '+abgC.map(function(c){return ABGC[c]}).join(' and ')+' ('+abgW.join(', ')+')</p>':'')+meter('abg4',150000,'4x'),R.used.abg,pm(['abg4']));
  html+=tile('ibp',(ibpW.length?'<p class="xcl"><span>This mix:</span> '+ibpW.join(', ')+'</p>':R.used.ibp?'<p class="xcl"><span>This mix:</span> here so Ink Business Cash earns points, not cash back</p>':'')+meter('ibp3',150000,'3x'),R.used.ibp,pm(['ibp3']));
  html+=tile('ibc',((i5.length||i2.length)?'<p class="xcl"><span>This mix:</span> '+i5.concat(i2).join(', ')+'</p>':'')+meter('ibc5',25000,'5x')+meter('ibc2',25000,'2x'),(R.cu.ibc5||0)+(R.cu.ibc2||0)>0,pm(['ibc5','ibc2']));
  html+=tile('bbp',(bbW.length?'<p class="xcl"><span>This mix:</span> '+bbW.join(', ')+'</p>':'')+meter('bbp2',50000,'2x'),(R.cu.bbp2||0)>0,pm(['bbp2']));
  html+=tile('cap',(cpW.length?'<p class="xcl"><span>This mix:</span> '+cpW.join(', ')+'</p><p class="xcl"><span>No cap:</span> '+ks(R.cu.cap2/12)+' a month at 2x, est.</p>':''),R.used.cap,pm(['cap2']));
  var over=0;rows.forEach(function(o,i){over+=(R.al[i].base||0)/12});
  html+='<div class="xc xbase'+(over>0?'':' idle')+'"><div class="xch"><b>Past every cap</b><small>Any card in the stack</small></div><p class="xct">Spend beyond the yearly caps above goes to Capital One Venture Business at 2x when its points cover its fee. Otherwise it stays on the card it is on today, or counts at 1x. The desk never moves a line to a card that earns less; bigger spend often runs on more than one card per category, sized on the call.</p><p class="xcp">'+(over>0?'<b>'+usd(over)+'</b> a month past the caps, est.':'Nothing past the caps in this mix.')+'</p></div>';
  html+='<div class="xc xfees"><div class="xch"><b>Card annual fees</b><small>Not taken off what the desk finds</small></div><p class="xct">'+(R.fee?(function(){var f=[];if(R.used.abg)f.push('Amex Business Gold $375');if(R.used.ibp)f.push('Ink Business Preferred $95');if(R.used.cap)f.push('Capital One Venture Business $95');return f.length>1?f.slice(0,-1).join(', ')+' and '+f[f.length-1]:f[0]})()+' a year, est. A card is left out when its points would not cover its fee.':'This mix needs no card with an annual fee, est.')+'</p><p class="xcp"><b>'+usd(R.fee/12)+'</b> a month, est.</p></div>';
  box.innerHTML=html}

/* every line, a month */
function table(r,map){var rows=[],tot={m:0,t:0,d:0};
  LN.forEach(function(l){var m=A[l.id]||0;if(!m)return;var i=map[l.id];
    if(i==null){rows.push('<div class="xtr off" role="row"><span role="rowheader">'+l.n+'</span><span role="cell" data-l="A month">'+usd(m)+'</span><span role="cell" data-l="Today">Not on a card</span><span role="cell" data-l="With the desk">Not counted</span><span role="cell" data-l="Extra points">0</span></div>');return}
    var o=r.rows[i],ps=parts(r,i),dp=0;ps.forEach(function(p){dp+=p.a*p.n.r});var ex=Math.max(0,dp-o.m*o.tr);tot.m+=m;tot.t+=o.m*o.tr;tot.d+=dp;
    rows.push('<div class="xtr" role="row"><span role="rowheader">'+l.n+'<small>'+l.h+'</small></span><span role="cell" data-l="A month">'+usd(m)+'</span><span role="cell" data-l="Today">'+tShort(mix==='ex'?T[l.id]:mix)+'</span><span role="cell" data-l="With the desk"><b>'+x(dp/m)+'</b><small>'+desc(ps)+'</small></span><span role="cell" class="d" data-l="Extra points">'+(ex>0?'+'+pts(ex):'0')+'</span></div>')});
  $('#xrows').innerHTML=rows.join('')||'<div class="xtr none" role="row"><span role="cell">Put an amount on any line above to see it here.</span></div>';
  S('tm',usd(tot.m));S('tt',tot.m?x(tot.t/tot.m):'0x');S('td',tot.m?x(tot.d/tot.m):'0x');S('tx','+'+pts(Math.max(0,tot.d-tot.t)))}

/* ---------------- building the lines ---------------- */
function opts(sel){return TODAY.map(function(t){return '<option value="'+t[0]+'"'+(t[0]===sel?' selected':'')+'>'+t[1]+'</option>'}).join('')}
function build(){var p=IND[idx][3],open={},ph=window.matchMedia&&matchMedia('(max-width:760px)').matches;
  if(!ph)G.forEach(function(g){g.L.forEach(function(l){if(p[l[0]])open[g.id]=1})});
  $('#xgs').innerHTML=G.map(function(g){return '<details class="xg" data-g="'+g.id+'"'+(open[g.id]?' open':'')+'><summary><span class="xgn">'+g.n+'<small data-gn="'+g.id+'"></small></span><span class="xgt"><b data-gt="'+g.id+'">$0</b> a month</span></summary><div class="xls">'+
    g.L.map(function(l){var id=l[0];return '<div class="xl" data-l="'+id+'"><div class="xlh"><label for="xa-'+id+'">'+l[1]+'</label><small id="xh-'+id+'">'+l[2]+'</small></div>'+
      '<div class="xla"><span aria-hidden="true">$</span><input id="xa-'+id+'" type="text" inputmode="numeric" autocomplete="off" value="0" aria-describedby="xh-'+id+'"></div>'+
      '<div class="xlt"><select id="xt-'+id+'" aria-label="'+l[1]+': how it is paid today">'+opts('1')+'</select></div>'+
      '<p class="xlr" data-lr="'+id+'" aria-live="off"></p></div>'}).join('')+'</div></details>'}).join('');
  LN.forEach(function(l){var t=$('#xa-'+l.id),s=$('#xt-'+l.id);
    t.addEventListener('input',function(){var c=t.selectionStart,n0=t.value.length,v=Math.min(2e6,+(t.value.replace(/[^0-9]/g,''))||0);A[l.id]=v;t.value=v?v.toLocaleString('en-US'):'';var n1=t.value.length;try{t.setSelectionRange(Math.max(0,c+n1-n0),Math.max(0,c+n1-n0))}catch(e){}paint()});
    t.addEventListener('blur',function(){t.value=(A[l.id]||0).toLocaleString('en-US')});
    t.addEventListener('focus',function(){t.select()});
    s.addEventListener('change',function(){T[l.id]=s.value;paint()})})}
function load(scale){var p=IND[idx],m=C.mixOf(idx,scale&&SP>0?SP:null);
  LN.forEach(function(l){A[l.id]=m.A[l.id];T[l.id]=m.T[l.id]});
  $('#cind').value=String(idx);
  var on=0;LN.forEach(function(l){if(A[l.id]&&T[l.id]!=='none')on+=A[l.id]});
  var gm=p[0]==='other'?'General small-business mix':'Typical mix';
  $('#cwho').textContent=(scale&&SP>0?gm+', scaled to '+kmo(SP)+' a month, est.':gm+': '+kmo(on)+' a month on cards, est.');
  $('#ccth').textContent='Things to consider for '+p[5];
  $('#ccul').innerHTML=p[4].map(function(t){return '<li>'+t+'</li>'}).join('');
  build();LN.forEach(function(l){$('#xa-'+l.id).value=(A[l.id]||0).toLocaleString('en-US');$('#xt-'+l.id).value=T[l.id]});
  paint()}

/* ---------------- controls ---------------- */
var SEL=$('#cind');
SEL.innerHTML=IND.map(function(p,i){return '<option value="'+i+'">'+p[1]+'</option>'}).join('');
SEL.addEventListener('change',function(){idx=+SEL.value;SP=0;SEL.setAttribute('data-picked','1');C.set(idx);load(false)});
if(VIA)SEL.setAttribute('data-picked','1');
$('#cuse').innerHTML=BS.types.map(function(t){return '<button type="button" role="radio" data-u="'+t.id+'" aria-checked="'+(t.id===use)+'"'+(t.id===use?' class="on"':'')+'><b>'+t.name+'</b><small>'+rng(t)+'</small></button>'}).join('');
$$('#cuse button').forEach(function(b){b.addEventListener('click',function(){use=b.dataset.u;$$('#cuse button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});paint()})});
$$('#cmix button').forEach(function(b){b.addEventListener('click',function(){mix=b.dataset.m;$$('#cmix button').forEach(function(o){var on=o===b;o.classList.toggle('on',on);o.setAttribute('aria-checked',on)});
  $$('.xlt select',root).forEach(function(s){s.disabled=mix!=='ex'&&s.value!=='none'});root.classList.toggle('xall',mix!=='ex');paint()})});
$('#xopen').addEventListener('click',function(){var ds=$$('.xg',root),all=ds.every(function(d){return d.open});ds.forEach(function(d){d.open=!all});this.textContent=all?'Open every group':'Close every group'});
$('#xzero').addEventListener('click',function(){LN.forEach(function(l){A[l.id]=0;$('#xa-'+l.id).value='0'});$('#cwho').textContent='Every line at $0: type your own, est.';paint();var f=$('#xa-adsOn');var d=f&&f.closest('details');if(d)d.open=true;if(f)f.focus()});
$('#xreset').addEventListener('click',function(){load(false)});
load(true);
if(window.matchMedia&&matchMedia('(max-width:760px)').matches){var td=$('#xtd');if(td)td.open=false}
})();
