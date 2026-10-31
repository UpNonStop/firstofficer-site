/* The phone's four screens (Earn, Burn, Return, Learn), shared by the home hero (modes.js) and the calculator (calc.js).
   Chat bubbles carry avatars; spend lines carry a glyph; the trip carries a route; the findings carry their colours; the lesson carries a coin.
   Every owner is a fictional example and every figure is an estimate. No program logos beyond identification. */
window.FO_PANES=(function(){
var A=window.FO_A||'';
var LOGO={1:'01-amex',2:'02-chase',3:'03-capital-one',4:'04-citi',9:'09-marriott',10:'10-hilton',11:'11-ihg',12:'12-hyatt',17:'17-united',18:'18-delta',19:'19-american',20:'20-southwest',25:'25-aeroplan',26:'26-flying-blue',32:'32-singapore',35:'35-turkish',37:'37-ana',47:'47-virgin-atlantic',48:'48-tap-air-portugal',50:'50-jal'};
var NM={1:'Amex',2:'Chase',3:'Capital One',4:'Citi',9:'Marriott',10:'Hilton',11:'IHG',12:'Hyatt',17:'United',18:'Delta',19:'American',20:'Southwest',25:'Aeroplan',26:'Flying Blue',32:'Singapore',35:'Turkish',37:'ANA',47:'Virgin Atlantic',48:'TAP',50:'JAL'};
function lg(id){return LOGO[id]?A+'img/hero/prog/'+LOGO[id]+'.jpg':''}
function pts(n){n=Math.round(n);return n>=1e6?(Math.round(n/1e4)/100).toFixed(2).replace(/0$/,'').replace(/\.0$/,'')+'M':n>=1e3?Math.round(n/1e3)+'k':''+n}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function x(n){if(typeof n==='string')return n;return (+n).toFixed(1).replace(/\.0$/,'')+'x'}
function chips(ids){return '<div class="zlgs">'+ids.map(function(i){return '<span><img src="'+lg(i)+'" alt="">'+NM[i]+'</span>'}).join('')+'</div>'}
/* small line glyphs, one per kind of spend */
var SVG='<svg viewBox="0 0 24 24" aria-hidden="true">';
var G={
 ads:SVG+'<path d="M3 10v4h3l6 4V6l-6 4H3z"/><path d="M16 9a4 4 0 0 1 0 6"/></svg>',
 laptop:SVG+'<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/></svg>',
 box:SVG+'<path d="M3 8l9-4 9 4-9 4-9-4z"/><path d="M3 8v8l9 4 9-4V8"/><path d="M12 12v8"/></svg>',
 plane:SVG+'<path d="M3 14l18-7-6 13-3-6-9 0z"/></svg>',
 wrench:SVG+'<path d="M14.5 6.5a4 4 0 0 1 5 5L8 23l-3-3L16.5 8.5"/><path d="M14.5 6.5L17 4l3 3-2.5 2.5"/></svg>',
 pump:SVG+'<rect x="4" y="3" width="10" height="18" rx="1.5"/><path d="M6 7h6"/><path d="M14 10h2a2 2 0 0 1 2 2v5a1.5 1.5 0 0 0 3 0V9l-3-3"/></svg>',
 truck:SVG+'<path d="M3 7h11v9H3z"/><path d="M14 10h4l3 3v3h-7z"/><circle cx="7" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/></svg>',
 wifi:SVG+'<path d="M4 10a11 11 0 0 1 16 0"/><path d="M8 13.5a6 6 0 0 1 8 0"/><circle cx="12" cy="17.5" r="1"/></svg>',
 flask:SVG+'<path d="M9 3h6"/><path d="M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3"/></svg>',
 basket:SVG+'<path d="M3 10h18l-2 10H5z"/><path d="M8 10l4-6 4 6"/></svg>',
 building:SVG+'<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2"/></svg>',
 hotel:SVG+'<path d="M3 20V9l9-5 9 5v11"/><path d="M9 20v-6h6v6"/></svg>',
 people:SVG+'<circle cx="12" cy="8" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg>',
 gift:SVG+'<rect x="3" y="9" width="18" height="12" rx="1.5"/><path d="M12 9v12M3 14h18"/><path d="M12 9c-2-4-6-4-6-1s4 1 6 1zm0 0c2-4 6-4 6-1s-4 1-6 1z"/></svg>',
 print:SVG+'<path d="M7 8V3h10v5"/><rect x="3" y="8" width="18" height="9" rx="1.5"/><path d="M7 14h10v7H7z"/></svg>',
 road:SVG+'<path d="M5 21L9 3h6l4 18"/><path d="M12 7v2M12 12v2M12 17v2"/></svg>',
 scale:SVG+'<path d="M12 3v18M5 21h14"/><path d="M4 8h16"/><path d="M7 8l-3 6a3 3 0 0 0 6 0l-3-6zM17 8l-3 6a3 3 0 0 0 6 0l-3-6z"/></svg>',
 receipt:SVG+'<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/></svg>'
};
var K=[[/ads|marketing|listing|meta|google|delivery app/i,'ads'],[/software|license|filing|subscription|cloud/i,'laptop'],[/fuel|vans/i,'pump'],[/fleet|shipping|freight|tolls/i,'truck'],[/tires|repair|parts|equipment|maintenance/i,'wrench'],[/phone|internet|utilities/i,'wifi'],[/lab fee/i,'flask'],[/food|supplier|dining|meals|wholesale/i,'basket'],[/hotel|nights|lodging/i,'hotel'],[/travel|carrier|shoot|deposition|flight/i,'plane'],[/gift/i,'gift'],[/signage|print/i,'print'],[/contractor|staff|payroll|agent|driver/i,'people'],[/firm|office|rent|expenses/i,'building'],[/supplies|packaging|materials|inventory|vendors/i,'box'],[/permit|legal/i,'scale']];
function glyph(name){for(var i=0;i<K.length;i++)if(K[i][0].test(name))return G[K[i][1]];return G.receipt}
/* chat bubbles with avatars: the owner's initials on the right, the chevron on the left */
function bub(who,text,p){var av=who==='f'?'<i class="zav zaf"><img src="'+A+'img/rec/chev.png" alt=""></i>':'<i class="zav zao">'+(p&&p.ini||'')+'</i>';
  return '<div class="zrow '+(who==='f'?'zrf':'zro')+'">'+(who==='f'?av:'')+'<div class="zbu '+(who==='f'?'zf':'zo')+'">'+(who==='f'?'<small>First Officer</small>':'')+text+'</div>'+(who==='o'?av:'')+'</div>'}
/* ---- Earn: lines of spend with glyphs, points a year, the move waiting for an OK ---- */
function earn(p,o){o=o||{};var cats=o.cats||p.cats.slice(0,3).map(function(c){var mx=Math.max.apply(null,p.cats.map(function(c){return c[1]}));return [c[0],'$'+c[1]+'k/mo',c[2],c[3],Math.round(c[1]/mx*100)]});
  var from=o.from!=null?o.from:p.from,before=o.before!=null?o.before:p.spend*1e3*p.from,after=o.after!=null?o.after:p.spend*1e3*p.to;
  return bub('o',p.qE,p)+bub('f','Most of it earns '+x(from)+'. That is the gap. Here is what the desk found.',p)+
    '<div class="zkc"><div class="zkh">Spend by line<b>per $1, est.</b></div><div class="zsp zsp2">'+cats.map(function(c){return '<div class="zln"><i class="zg">'+glyph(c[0])+'</i><span>'+c[0]+'</span><em>'+c[1]+'</em><span class="zx"><s>'+x(c[2])+'</s>→ <b>'+x(c[3])+'</b></span><u><i style="width:'+c[4]+'%"></i></u></div>'}).join('')+'</div></div>'+
    '<div class="zkc"><div class="zkh">Points a year<b>est.</b></div><div class="zba"><div><small>Today</small><b>'+pts(before)+'</b></div><span>→</span><div><small>With the desk</small><b>'+pts(after)+'</b></div></div>'+chips(p.earnL)+'</div>'+
    '<div class="zkc zmv"><i class="zcard"><b>'+((p.move[0].match(/(\d+(?:\.\d)?x)/)||[])[1]||x(p.cats[0][3]))+'</b><u></u></i><div><small>Waiting for '+p.first+'\'s OK</small><b>'+p.move[0]+'</b><em>+'+usd(p.move[1])+' a year, est.</em></div><span class="zok">Approve</span></div>'}
/* ---- Burn: the trip, the route, the points, the vetted requirements, the desk's note ---- */
function burn(p){var from=(p.city||'').split(',')[0],to=p.trip.split(/ in | for | honeymoon/)[0];
  /* Oct 29 (Ohad): the trip reads like a boarding pass, and the flight path is the progress: the plane sits where the points are */
  var IATA={'Columbus':'CMH','Phoenix':'PHX','Charlotte':'CLT','Denver':'DEN','Atlanta':'ATL','Austin':'AUS','Dallas':'DFW','Portland':'PDX','Kansas City':'MCI',
    'Tokyo':'HND','Maui':'OGG','Paris':'CDG','Lisbon':'LIS','Lagos':'LOS','Istanbul':'IST','Cancun':'CUN','Bali':'DPS','Cabo':'SJD','London':'LHR','Rome':'FCO'};
  function code(c){return IATA[c]||c.replace(/[^A-Za-z]/g,'').slice(0,3).toUpperCase()}
  var n=(p.trip.match(/(\d+)/)||[])[1]||(/honeymoon/.test(p.trip)?'2':''),bits=[];
  if(/business/i.test(p.trip))bits.push('Business');
  bits.push(n?n+' travelers':(/family/.test(p.trip)?'Family':''));
  var lab=bits.filter(Boolean).join(' · '),pc=Math.max(4,Math.min(96,p.pct))/100;
  var plane='<svg viewBox="0 0 24 24" aria-hidden="true"><path transform="rotate(90 12 12)" d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z"/></svg>';
  return bub('o',p.qB,p)+
    '<div class="zkc"><div class="ztr" style="background-image:url('+A+p.img+')"><div><small>'+p.when+'</small><b>'+p.trip+'</b></div></div>'+
    '<div class="zbp" style="--p:'+pc+'" role="img" aria-label="'+from+' to '+to+', '+p.pct+'% of the points there, est."><div class="zbp-r">'+
      '<div class="zbp-c"><b>'+code(from)+'</b><small>'+from+'</small></div>'+
      '<div class="zbp-p"><em>'+lab+'</em><i class="zbp-t"></i><i class="zbp-f"></i><span class="zbp-pl">'+plane+'</span></div>'+
      '<div class="zbp-c to"><b>'+code(to)+'</b><small>'+to+'</small></div></div>'+
      '<div class="zbp-n"><span>'+pts(p.have)+' of '+pts(p.need)+' points</span><b>'+p.pct+'% there, est.</b></div></div>'+chips(p.burnL)+'</div>'+
    '<div class="zkc"><div class="zkh">Requirements vetted<b>'+p.reqs.length+' of '+p.reqs.length+'</b></div><ul class="zck">'+p.reqs.map(function(r){return '<li><b>✓</b>'+r+'</li>'}).join('')+'</ul></div>'+
    '<div class="zsd"><img src="'+A+'img/rec/chev.png" alt=""><div><small>Sent to the desk</small><b>Dates next. The desk books after '+p.first+' approves.</b></div></div>'}
/* ---- Return: Friday findings in dollars, each finding in its colour; the weeks rise into this Friday (no confetti, Oct 29) ---- */
function ret(p){var retSum=p.ret.reduce(function(a,r){return a+r[1]},0),wk=[38,52,30,64,46,58,72,100];
  return bub('o','What did this week bring in?',p)+
    '<div class="zkc"><div class="zkh">Friday findings<b>this week</b></div><div class="zrt"><div class="zrtn"><b>'+usd(retSum)+'</b><small>found this week, est.</small></div><div class="zwkb">'+wk.map(function(h){return '<i style="height:'+h+'%"></i>'}).join('')+'</div></div>'+
    p.ret.map(function(r,i){return '<div class="zrl"><i class="zdot s'+i+'"></i><span>'+r[0]+'</span><b>'+usd(r[1])+'</b></div>'}).join('')+'</div>'+
    '<div class="zkc"><div class="zkh">Where it came from<b>est.</b></div><div class="zst">'+p.ret.map(function(r,i){return '<i class="s'+i+'" style="flex:'+r[1]+'"></i>'}).join('')+'</div><div class="zleg">'+p.ret.map(function(r,i){return '<span><i class="s'+i+'"></i>'+Math.round(r[1]/retSum*100)+'%</span>'}).join('')+'</div></div>'+
    bub('f','All three are in the Friday scorecard. One number, in dollars.',p)+
    '<div class="zby"><span>✓</span>Checked against the statements</div>'}
/* ---- Learn: one short lesson, the coin, the bars, the lesson count ---- */
function learn(p){var L=p.learn,u=L[5]||'{v}¢',lm=Math.max.apply(null,L[3].map(function(b){return b[1]}));
  var coin='<i class="zcoin" aria-hidden="true"><svg viewBox="0 0 40 40"><ellipse cx="20" cy="30" rx="13" ry="5"/><path d="M7 30v-5c0 2.8 5.8 5 13 5s13-2.2 13-5v5"/><ellipse cx="20" cy="24" rx="13" ry="5"/><path d="M7 24v-5c0 2.8 5.8 5 13 5s13-2.2 13-5v5"/><ellipse cx="20" cy="18" rx="13" ry="5"/><path d="M7 18v-5c0 2.8 5.8 5 13 5s13-2.2 13-5v5"/><ellipse cx="20" cy="12" rx="13" ry="5"/></svg></i>';
  return bub('o','Teach me one thing this week.',p)+
    '<div class="zkc zls"><div class="zlt">This week\'s 2 minute lesson</div><div class="mh5">'+L[0]+'</div><div class="zlb"><b>'+L[1]+'</b><small>'+L[2]+'</small>'+coin+'</div><div class="zlbars">'+L[3].map(function(b){return '<div><span>'+b[0]+'</span><u><i style="width:'+Math.round(b[1]/lm*100)+'%"></i></u><b>'+u.replace('{v}',b[1])+'</b></div>'}).join('')+'</div></div>'+
    bub('f',L[4],p)+
    '<div class="zkc"><div class="zkh">Lessons<b>3 of 12</b></div><div class="zseg">'+[1,1,1,0,0,0,0,0,0,0,0,0].map(function(v){return '<i'+(v?' class="on"':'')+'></i>'}).join('')+'</div>'+
    '<ul class="zup">'+(window.FO_MODES||[]).filter(function(o){return o!==p&&o.learn[0]!==L[0]}).slice(0,2).map(function(o,i){return '<li><i>'+(4+i)+'</i><span>'+o.learn[0]+'</span><small>Friday</small></li>'}).join('')+'</ul></div>'+
    '<div class="zqz"><span>Show me my numbers</span><span>Next lesson Friday</span></div>'}
return {earn:earn,burn:burn,ret:ret,learn:learn,bub:bub,chips:chips,glyph:glyph,lg:lg,NM:NM,LOGO:LOGO};
})();
