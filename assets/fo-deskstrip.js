/* The hero's desk strip: the specialists at work, one per program, with what they are doing right now and what they just handed back.
   The specialists are our own software agents; a person reviews every booking. Owners named here are the site's fictional examples.
   Program names and logos are shown for identification only. Reduced motion: a still strip. */
(function(){
var host=document.querySelector('.mdesk');if(!host)return;
var A=window.FO_A||'',RM=matchMedia('(prefers-reduced-motion: reduce)').matches||/[?&#]still=1/.test(location.href);
var S=[
 [1,'Amex','01-amex',['Card offers scan','Spend cap watch','Statement credits check']],
 [2,'Chase','02-chase',['Bonus category watch','Transfer bonus watch','Portal pricing check']],
 [12,'Hyatt','12-hyatt',['Night quote','Award space watch','Status review']],
 [18,'Delta','18-delta',['Offer scan','Partner route check','Award pricing watch']],
 [3,'Capital One','03-capital-one',['Transfer bonus watch','Portal pricing check','Miles ledger']],
 [17,'United','17-united',['Saver pricing check','Partner route check','Award space watch']],
 [9,'Marriott','09-marriott',['Award chart check','Free night check','Cash rate compare']],
 [47,'Virgin Atlantic','47-virgin-atlantic',['Partner route check','Transfer bonus watch','Award pricing watch']],
 [4,'Citi','04-citi',['Points ledger','Transfer bonus watch','Card offers scan']],
 [26,'Flying Blue','26-flying-blue',['Promo rewards check','Partner route check','Award pricing watch']],
 [10,'Hilton','10-hilton',['Award chart check','Free night check','Points and cash math']],
 [37,'ANA','37-ana',['Round trip award check','Transfer timing','Award space watch']],
 [20,'Southwest','20-southwest',['Companion pass pace','Fare watch','Points pricing check']],
 [25,'Aeroplan','25-aeroplan',['Partner route check','Stopover math','Award space watch']],
 [19,'American','19-american',['Award chart check','Partner route check','Award pricing watch']],
 [32,'Singapore','32-singapore',['Saver space watch','Transfer timing','Waitlist check']],
 [35,'Turkish','35-turkish',['Partner route check','Award pricing watch','Star partner quote']],
 [50,'JAL','50-jal',['Partner route check','Award space watch','Transfer timing']],
 [48,'TAP','48-tap-air-portugal',['Stopover check','Award space watch','Partner route check']],
 [11,'IHG','11-ihg',['Points and cash math','Free night check','Award chart check']]
];
var SAY=[
 [18,'Partner route checked for Wade’s Istanbul trip.'],
 [12,'Night quote ready for Leila, est.'],
 [1,'Transfer bonus caught for Anjali’s Lisbon plan.'],
 [10,'Free night certificate expiring. Planned for Hector.'],
 [17,'Saver space watch set for Leo’s Tokyo dates.'],
 [20,'Companion pass pace on track for Hector, est.'],
 [26,'Promo rewards checked for Leila’s Paris plan.'],
 [2,'Hotel credit claimed for Anjali, est.'],
 [9,'Cash rate compared for Dustin’s job-site nights.'],
 [37,'Award space watched for Teresa’s Tokyo dates.'],
 [3,'Miles ledger updated for Ines.'],
 [35,'Star partner quote ready for Chidi’s Lagos trip.'],
 [50,'Transfer timing checked for Leo’s Tokyo plan.'],
 [25,'Stopover math done for Anjali.'],
 [4,'Points ledger reconciled for Terrence.'],
 [19,'Award pricing watched for Terrence’s Cancun trip.'],
 [32,'Waitlist checked for Ines, Bali in business.'],
 [47,'Award pricing watched for Chidi’s Lagos trip.']
];
var lg={};S.forEach(function(s){lg[s[0]]=A+'img/hero/prog/'+s[2]+'.jpg'});
function pods(){return S.map(function(s,i){return '<div class="dpod" data-i="'+i+'"><img src="'+lg[s[0]]+'" alt=""><div><b>'+s[1]+'</b><small><span class="dst">'+s[3][0]+'</span><i class="dots"><u></u><u></u><u></u></i></small></div></div>'}).join('')}
host.innerHTML='<div class="dh"><span class="lv"></span><b>First Officer, at work</b><span class="dsub">every program on your file, kept current as the rules change</span><div class="dsay"><img src="'+lg[SAY[0][0]]+'" alt=""><span>'+SAY[0][1]+'</span></div></div>'+
 '<div class="dtrack"><div class="dset">'+pods()+'</div><div class="dset" aria-hidden="true">'+pods()+'</div></div>'+
 '<p class="dfine">A person reviews every booking. Fictional examples; programs shown for identification only.</p>';
if(RM)return;
var st=S.map(function(){return 0}),say=0,sayEl=host.querySelector('.dsay');
function all(i){return [].slice.call(host.querySelectorAll('.dpod[data-i="'+i+'"]'))}
function tick(){var i=Math.floor(Math.random()*S.length),ps=all(i);ps.forEach(function(p){p.classList.add('think')});
  setTimeout(function(){st[i]=(st[i]+1)%S[i][3].length;ps.forEach(function(p){p.querySelector('.dst').textContent=S[i][3][st[i]];p.classList.remove('think');p.classList.add('lit')})},1100);
  setTimeout(function(){ps.forEach(function(p){p.classList.remove('lit')})},2300)}
function speak(){say=(say+1)%SAY.length;sayEl.classList.add('off');setTimeout(function(){sayEl.querySelector('img').src=lg[SAY[say][0]];sayEl.querySelector('span').textContent=SAY[say][1];sayEl.classList.remove('off')},380)}
var on=false,t1,t2;
new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!on){on=true;t1=setInterval(tick,1900);t2=setInterval(speak,3800);tick()}else if(!e.isIntersecting&&on){on=false;clearInterval(t1);clearInterval(t2)}})},{threshold:.2}).observe(host);
})();
