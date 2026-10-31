/* calculator.html · the one model behind Basic and Go advanced (31 Oct 2026).
   Ohad: the two modes must agree. Basic runs the industry's typical mix, scaled to the slider's spend, through the same card stack,
   the same yearly caps and the same redemption values as Go advanced, so the same industry and the same spend give the same answer
   in both. Found money is the extra points only (today's points are taken off), every one counted, at about 1.6¢ a point (1.3¢ to
   1.9¢), with card annual fees left out, as in the site's examples (Ohad, 31 Oct 2026). The fees still decide whether a card is used. Loaded after FO_REDEMPTION_BASIS and before calc31.js (Basic) and fo-calc-adv.js (Go advanced).
   Every figure is an estimate; terms as understood Oct 2026; example mixes are fictional.
   window.FO_CALC: the data (cards, lines, industries), model(A,T,use,mix), verdict(r), mixOf(i,spend), forSpend(i,spend), and the
   industry both modes share (idx, set, on). */
(function(){
'use strict';
var BS=window.FO_REDEMPTION_BASIS;if(!BS)return;
var FEE=BS.fee/12,GATE=BS.gate,UTIL=BS.util,BIG=250000;
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function r10(n){return Math.round(n/10)*10}
function u10(n){return usd(r10(n))}
function slug(t){return String(t||'').toLowerCase().replace(/[^a-z]+/g,'-').replace(/^-|-$/g,'')}
function U(id){for(var i=0;i<BS.types.length;i++)if(BS.types[i].id===id)return BS.types[i];return BS.types[0]}

/* ---------------- the card stack, as modelled (terms as understood Oct 2026, est.) ---------------- */
var CARD={
  ibc:{n:'Ink Business Cash',fee:0,t:'5x at office supply stores and on internet, cable and phone, up to $25K a year combined; 2x at gas stations and restaurants, up to $25K a year combined; then 1x. Counted as points alongside Ink Business Preferred.'},
  abg:{n:'Amex Business Gold',fee:375,t:'4x on the 2 categories it is used for most each month, from 6 eligible, up to $150K a year combined; then 1x.'},
  ibp:{n:'Ink Business Preferred',fee:95,t:'3x on travel, shipping, internet, cable and phone, and search and social ads, up to $150K a year combined; then 1x.'},
  bbp:{n:'Blue Business Plus',fee:0,t:'2x on everyday business purchases, up to $50K a year; then 1x.'},
  /* the uncapped 2x card (Ohad, 19 Sep: "Capital One also gets them 2x"; Spark Miles became Venture Business in spring 2026): spend past
     the caps above earns 2x here, only when its points cover its fee (best() tries every stack with and without it) */
  cap:{n:'Capital One Venture Business',fee:95,t:'2x on every purchase, with no yearly cap. In the stack only for spend past the caps above, and only when its points cover its fee.'}};
var BK=[{id:'ibc5',c:'ibc',r:5,cap:25000},{id:'abg4',c:'abg',r:4,cap:150000},{id:'ibp3',c:'ibp',r:3,cap:150000},
        {id:'ibc2',c:'ibc',r:2,cap:25000},{id:'bbp2',c:'bbp',r:2,cap:50000},{id:'cap2',c:'cap',r:2,cap:Infinity},{id:'base',c:'',r:1,cap:Infinity}];
var ABGC={ads:'advertising',tech:'electronics, software and cloud',dining:'restaurants',gas:'gas stations',transit:'transit, parking and tolls',wireless:'wireless phone service'};

/* ---------------- every line, in ten groups. [id, label, how it typically codes, eligibility, ibp3/ibc5 wording] ---------------- */
var G=[
 {id:'mk',n:'Marketing and ads',L:[
  ['adsOn','Online ads: search and social','Ad platforms typically code as advertising, 7311',{abg:'ads',ibp3:'search and social ads'}],
  ['adsTv','TV, radio and streaming ads','Media sellers typically code as advertising, 7311',{abg:'ads'}],
  ['adsPrint','Print, signage and direct mail','Typically codes as printing or advertising, 2741 or 7311',{}],
  ['adsAgency','Agencies and marketing freelancers','Typically codes as advertising or business services, 7311 or 7392',{}]]},
 {id:'tc',n:'Technology',L:[
  ['soft','Software and subscriptions','Typically codes as software, 5734, or data processing, 7372',{abg:'tech'}],
  ['cloud','Cloud, hosting and domains','Typically codes as network services, 4816, or data processing, 7372',{abg:'tech'}],
  ['net','Internet and cable','Typically codes as cable and telecom services, 4899 or 4814',{ibc5:'internet, cable and phone',ibp3:'internet, cable and phone'}],
  ['phone','Mobile phone service','Carriers typically code as telecom services, 4814',{ibc5:'internet, cable and phone',abg:'wireless',ibp3:'internet, cable and phone'}]]},
 {id:'tv',n:'Travel',L:[
  ['air','Airfare','Airlines typically code as 3000 to 3299, or 4511',{ibp3:'travel'}],
  ['hotel','Hotels and lodging','Hotels typically code as 3501 to 3999, or 7011',{ibp3:'travel'}],
  ['car','Car rental, taxis and rideshare','Typically codes as car rental, 7512, or taxis and rideshare, 4121',{ibp3:'travel'}],
  ['transit','Parking, tolls and trains','Typically codes as parking, 7523, tolls, 4784, or passenger rail, 4112',{abg:'transit',ibp3:'travel'}]]},
 {id:'vh',n:'Vehicles and fuel',L:[
  ['fuel','Fuel at gas stations','Gas stations typically code as 5541 or 5542',{abg:'gas',ibc2:1}],
  ['ev','EV charging','Typically codes as EV charging, 5552, outside gas stations',{}],
  ['fleet','Repairs, tires and parts','Typically codes as auto parts, 5533, or auto service, 7538',{}]]},
 {id:'sh',n:'Shipping and freight',L:[
  ['ship','Couriers and postage','Couriers typically code as 4215; the postal service as 9402',{ibp3:'shipping'}],
  ['freight','Freight and trucking carriers','Typically codes as motor freight, 4214, outside shipping on most cards',{}],
  ['pack','Packaging and shipping supplies','Typically codes as industrial or business supplies, 5085 or 5111',{}]]},
 {id:'of',n:'Office and equipment',L:[
  ['office','Office supply stores','Typically codes as office and stationery stores, 5943 or 5111',{ibc5:'office supply stores'}],
  ['elec','Computers and electronics','Typically codes as electronics stores, 5732, or computer equipment, 5045',{abg:'tech'}],
  ['furn','Furniture, tools and equipment','Typically codes as office furniture, 5021, or the dealer\'s own code',{}],
  ['rentEq','Equipment rental','Typically codes as equipment rental, 7394',{}]]},
 {id:'iv',n:'Inventory and supplies',L:[
  ['whole','Wholesale and food distributors','Typically codes as wholesale, 5099 or 5199: 1x on most bonus cards',{}],
  ['build','Building and trade supply','Typically codes as building materials, 5211, or home supply warehouses, 5200',{}],
  ['indsup','Professional and shop supplies','Medical, dental, salon and parts suppliers typically code as 5047, 5085 or 5533',{}],
  ['online','Online marketplaces','Typically codes as general merchandise, 5399, or the marketplace\'s own code',{}]]},
 {id:'me',n:'Meals and entertainment',L:[
  ['meals','Restaurants and client meals','Restaurants typically code as 5812 or 5814',{abg:'dining',ibc2:1}],
  ['events','Client events and gifts','Typically codes as the venue\'s or store\'s own category',{}]]},
 {id:'sv',n:'Services and overhead',L:[
  ['pro','Legal, accounting and consulting','Typically codes as professional services, 8111, 8931 or 8999',{}],
  ['labs','Labs and outside services','Labs typically code as 8071; other services use their own trade codes',{}],
  ['contr','Contractors and freelancers','Typically codes as the contractor\'s trade, or a payment platform',{}],
  ['ins','Insurance premiums','Insurers typically code as 6300; some add a card fee',{}],
  ['util','Utilities: power, gas and water','Utilities typically code as 4900; many add a card fee',{}],
  ['payr','Payroll and HR platform fees','Typically codes as software or business services; wages rarely go on a card',{}],
  ['dues','Dues, licenses and memberships','Typically codes as membership organizations, 8641 or 8699',{}],
  ['maint','Cleaning, repairs and upkeep','Typically codes as building services, 7349, or the trade\'s own code',{}]]},
 {id:'nc',n:'Often not on a card',L:[
  ['rent','Rent and leases','Landlords rarely take cards; when they do, a fee usually applies',{}],
  ['tax','Taxes, permits and filing fees','Typically codes as tax payments, 9311, or government services, 9399, with a processing fee',{}],
  ['loan','Loan and finance payments','Lenders rarely take cards for loan payments',{}]]}];
var LN=[],LI={};G.forEach(function(g){g.L.forEach(function(l){var o={id:l[0],n:l[1],h:l[2],e:l[3],g:g.id};LI[o.id]=LN.length;LN.push(o)})});
var TODAY=[['1','1x card',1],['1.5','1.5x card',1.5],['2','2x card',2],['3','3x or more',3],['c1','1% cash back',1],['c15','1.5% cash back',1.5],['c2','2% cash back',2],['none','Not on a card',0]];
var TR={};TODAY.forEach(function(t){TR[t[0]]=t});

/* ---------------- the 21 industries the site covers, in the Industries page's order and names: the 20 trades, then Other, a general small-business mix.
   Each: [slug, name, example owner's first name, $ a month and how each line is paid today (est., fictional), things to consider, how the sentence names it] ---------------- */
var IND=[
 ['marketing-agency','Agencies','Anjali',{adsOn:[12000],adsTv:[1500],soft:[6000,'2'],cloud:[1500,'1.5'],contr:[6000,'1.5'],air:[3500,'1.5'],hotel:[2500,'1.5'],car:[800,'1.5'],meals:[1500,'1.5'],events:[500],elec:[1200],office:[300],net:[400],phone:[600],pro:[800],dues:[300],payr:[400],rent:[6000,'none']},
  ['Client ad spend that runs through your cards','Software seats that grow with the team','Contractors, and which ones take cards','Shoot and client travel'],'agencies'],
 ['auto-repair','Auto repair','Marco',{indsup:[18000],furn:[1000],elec:[500],soft:[900],adsOn:[2000],util:[1200],phone:[400],net:[200],ins:[1500],rentEq:[400],fuel:[600],office:[200],dues:[200],pro:[600],meals:[300],maint:[600],rent:[7000,'none']},
  ['Parts orders, often from a few suppliers','Shop software and diagnostic subscriptions','Tools and equipment, and how they are paid for','Which suppliers take cards without a surcharge'],'auto repair shops'],
 ['cleaning','Cleaning','Rosa',{indsup:[7000],fuel:[4500],fleet:[1500],adsOn:[2500],soft:[600],phone:[900],ins:[1800],contr:[4500],rentEq:[300],office:[200],meals:[200],payr:[400],dues:[100],online:[600],rent:[3000,'none']},
  ['Supplies and chemicals, often on repeat orders','Fuel and vans','Subcontractors, and which ones take cards','Insurance and bonding, and whether a card fee applies'],'cleaning companies'],
 ['consulting','Consulting','Priya',{air:[6000,'1.5'],hotel:[5000,'1.5'],car:[1500,'1.5'],transit:[400],meals:[2500,'1.5'],events:[600],soft:[3000],cloud:[600],phone:[500],net:[300],elec:[800],office:[200],contr:[4000],pro:[1500],dues:[500],adsOn:[1500],ins:[600],rent:[5000,'none']},
  ['Client travel, often the biggest line','Software seats that grow with the team','Subcontractors and their payment terms','Client meals and events'],'consulting firms'],
 ['contractor','Contractors','Dustin',{build:[42400],rentEq:[10000,'1.5'],fuel:[5000],fleet:[1500],hotel:[6000],meals:[1500],phone:[600],net:[200],soft:[600],ins:[3000],tax:[600],office:[200],adsOn:[1500],dues:[200],loan:[4000,'none']},
  ['Materials, often the biggest line','Job-site hotels and travel','Fuel and equipment rental','Supplier terms versus paying by card'],'contractors'],
 ['cpa-firm','CPA firms','Martin',{soft:[6500],cloud:[800],pro:[2000],dues:[1200],adsOn:[1500],office:[1200,'1.5'],elec:[1000],furn:[400],phone:[500],net:[300],ins:[1200],meals:[900,'1.5'],events:[400],air:[1200],hotel:[1000],payr:[400],util:[400],contr:[4500],rent:[6000,'none']},
  ['Tax and audit software renewals','Licenses and continuing education','Seasonal staff and contractors','Which vendors take cards without fees'],'CPA firms'],
 ['dental-practice','Dental','Leila',{indsup:[13000],labs:[6000],soft:[3500,'1.5'],cloud:[500,'1.5'],adsOn:[4000,'2'],adsPrint:[800],net:[400],phone:[500],office:[700,'1.5'],elec:[600],furn:[300],ins:[900],util:[600],dues:[400],meals:[300,'1.5'],payr:[300],rent:[7000,'none']},
  ['Supply orders, often from a few large vendors','Practice and imaging software','Lab fees, and whether your labs take cards','Patient marketing and ads'],'dental practices'],
 ['e-commerce','E-commerce','Ines',{adsOn:[9000],whole:[8000],ship:[3000],pack:[1200],soft:[1500],cloud:[300],online:[800],elec:[300],office:[100],contr:[800],phone:[200],net:[150],pro:[400]},
  ['Ad spend on search and social','Shipping and packaging','Inventory from your suppliers','Seasonal peaks around the holidays'],'e-commerce'],
 ['fitness','Fitness','Jordan',{furn:[4000],adsOn:[5000],soft:[1500],util:[4500],maint:[1500],contr:[3000],ins:[900],phone:[300],net:[300],office:[200],dues:[300],whole:[1500],indsup:[1000],online:[600],meals:[200],payr:[400],rent:[9000,'none']},
  ['Equipment purchases and repairs','Booking software and music licenses','Utilities, often a large monthly line','Instructors and how they are paid'],'gyms and studios'],
 ['hvac','HVAC','Hector',{build:[17000],indsup:[2000],fuel:[6500],fleet:[1500],rentEq:[800,'1.5'],phone:[900,'1.5'],net:[300,'1.5'],soft:[900,'1.5'],adsOn:[3000,'1.5'],adsPrint:[600],office:[300,'1.5'],elec:[400],ins:[1200],meals:[400,'1.5'],dues:[200],util:[300],payr:[200],tax:[200],loan:[2500,'none']},
  ['Fuel and fleet costs','Supplier and equipment purchases','Seasonal swings in what you spend','Vendors who take cards without fees'],'HVAC'],
 ['it-services','IT services','Samir',{elec:[12000],soft:[8000],cloud:[6000],net:[600],phone:[900],contr:[3000],air:[1500,'1.5'],hotel:[1200,'1.5'],car:[800,'1.5'],meals:[800],office:[300],adsOn:[1500],ins:[700],dues:[300],fuel:[600],rent:[5000,'none']},
  ['Hardware bought for clients','Software licenses resold or managed','Cloud bills that grow with clients','Subcontractors and their payment terms'],'IT services'],
 ['landscaping','Landscaping','Gus',{build:[9000],fuel:[5000],fleet:[2000],rentEq:[3000],indsup:[2000],adsOn:[1500],adsPrint:[500],phone:[600],soft:[400],ins:[1500],meals:[400],office:[100],dues:[200],tax:[300],loan:[3000,'none']},
  ['Plants, stone and supply yards','Fuel and trucks','Equipment rental and repairs','Seasonal swings in what you spend'],'landscaping companies'],
 ['law-firm','Law firms','Chidi',{air:[2500],hotel:[2000],car:[800],transit:[400],soft:[3500],cloud:[400],pro:[5000],tax:[2000],office:[900,'1.5'],elec:[600],furn:[400],meals:[1200,'1.5'],events:[400],dues:[600],ins:[1500],net:[400],phone:[600],adsOn:[2500,'1.5'],rent:[9000,'none']},
  ['Client costs you pay up front','Travel to depositions and court','Filing fees and research software','Which fees can be paid by card at all'],'law firms'],
 ['medical-practice','Medical','Elena',{indsup:[12000],labs:[4000],soft:[4000,'1.5'],cloud:[600],adsOn:[2500],office:[800,'1.5'],elec:[800],furn:[400],ins:[2000],util:[900],phone:[600],net:[400],dues:[800],pro:[1500],meals:[400],payr:[400],rent:[8000,'none']},
  ['Medical supplies, often from a few large vendors','Records and billing software','Labs, and whether they take cards','Insurance premiums, and whether a card fee applies'],'medical practices'],
 ['property-management','Property management','Nadia',{maint:[12000],build:[6000],util:[5000],ins:[3000],soft:[1500],adsOn:[1500],adsPrint:[300],phone:[500],net:[300],office:[300],fuel:[800],pro:[1200],dues:[300],tax:[500,'none']},
  ['Repairs and upkeep across properties','Supply runs for maintenance','Utilities you pay for tenants','Which vendors take cards without fees'],'property management'],
 ['real-estate','Real estate','Terrence',{adsOn:[10700,'1.5'],adsPrint:[7000],car:[2000],fuel:[1500],events:[4000,'1.5'],meals:[1500,'1.5'],soft:[1500],phone:[500],net:[200],office:[300],dues:[800],pro:[1000],ins:[500],elec:[300],air:[1500],hotel:[1500],transit:[200],rent:[4000,'none']},
  ['Listing ads and portals','Signage and print','Travel to showings','Closing gifts and client events'],'real estate'],
 ['restaurant','Restaurants','Teresa',{whole:[16000],adsOn:[3000,'2'],soft:[800],net:[300],phone:[300],util:[1800],indsup:[1500],pack:[600],office:[100],maint:[800],ins:[900],dues:[100],rent:[8000,'none'],tax:[1500,'none']},
  ['Food suppliers, and whether they take cards','Delivery apps and ads','Phone, internet and utilities','Card surcharges, where margins are thin'],'restaurants'],
 ['salon-or-spa','Salons','Camille',{indsup:[9000],whole:[5000],adsOn:[3500],soft:[1200],util:[2000],maint:[800],ins:[900],phone:[400],net:[200],furn:[800],office:[200],dues:[300],online:[600],meals:[200],payr:[400],rent:[7000,'none']},
  ['Professional products, often on repeat orders','Retail stock for resale','Booking software and payment fees','Seasonal promotions and ads'],'salons and spas'],
 ['trucking','Trucking','Wade',{fuel:[45000],fleet:[8000],transit:[4000],tax:[1300],ins:[2500],phone:[500],net:[200],soft:[900],meals:[500],hotel:[300],office:[100],loan:[6000,'none']},
  ['Fleet fuel, usually most of the spend','Tires, repairs and parts','Tolls and permits','Where fuel is bought, and how it is paid for'],'trucking'],
 ['veterinary-clinic','Veterinary','Owen',{indsup:[14000],labs:[3000],soft:[2500,'1.5'],cloud:[300],adsOn:[2000],util:[1200],ins:[1200],phone:[500],net:[300],office:[500,'1.5'],elec:[600],furn:[300],dues:[500],pro:[1000],meals:[300],maint:[600],rent:[7000,'none']},
  ['Medical supplies and pharmacy orders','Reference labs and outside services','Practice software','Which distributors take cards without a surcharge'],'veterinary clinics'],
 ['other','Other','',{adsOn:[3000],adsPrint:[400],soft:[2500],cloud:[400],net:[250],phone:[450],air:[1500],hotel:[1200],car:[500],transit:[150],fuel:[900],fleet:[300],ship:[700],pack:[200],office:[400],elec:[600],furn:[300],indsup:[3000],whole:[2500],online:[800],meals:[900],events:[300],pro:[900],contr:[1500],ins:[1000],util:[700],payr:[250],dues:[200],maint:[400],rent:[5000,'none'],tax:[600,'none']},
  ['Your biggest monthly lines, and which card each one goes on','Software and subscriptions that renew every month','Suppliers and vendors, and which take cards without a surcharge','Travel and meals, and which card each one goes on'],'your business']];
/* every name and slug that reaches this page: the trade pages' file names (for-*.html, also read from the referrer), the Industries page, Book's list */
var ALIAS={restaurants:'restaurant',dental:'dental-practice',agencies:'marketing-agency',agency:'marketing-agency','marketing-agencies':'marketing-agency',law:'law-firm','law-firms':'law-firm',realestate:'real-estate',ecommerce:'e-commerce',contractors:'contractor',
  'cpa-firms':'cpa-firm',cpa:'cpa-firm',medical:'medical-practice',salons:'salon-or-spa',salon:'salon-or-spa',spa:'salon-or-spa',veterinary:'veterinary-clinic',vet:'veterinary-clinic','it':'it-services','it-and-msp':'it-services','it-msp':'it-services',msp:'it-services',gym:'fitness',
  'other-industries':'other',general:'other',insurance:'other','insurance-agency':'other'};


/* ---------------- the router: every line on a card, inside each card's yearly cap (#71: a card only takes a line it improves; past every cap
   a line stays on the card it is on today, never under 1x) ---------------- */
function okB(l,b,pair,ibp,cp){var e=l.e;if(b.id==='cap2')return !!cp;
  if(b.id==='ibc5')return ibp&&!!e.ibc5;if(b.id==='abg4')return !!e.abg&&pair.indexOf(e.abg)>-1;
  if(b.id==='ibp3')return ibp&&!!e.ibp3;if(b.id==='ibc2')return !!e.ibc2;return true}
/* exact allocation (min-cost flow): each card's capped space goes to the lines that gain the most per dollar on it, so what the desk
   finds can only grow as spend grows. A card only takes a line it improves (#71); what no card takes stays on the card it is on today,
   never under 1x. Lines alike in what they qualify for and in today's rate are pooled, routed, then shared back by size. */
function route(rows,pair,ibp,cp){var B=BK.filter(function(b){return b.id!=='base'}),m=B.length,gk={},P=[];
  rows.forEach(function(o,i){var c=Math.max(1,o.tr),mk='';B.forEach(function(b){mk+=okB(o.l,b,pair,ibp,cp)&&b.r>o.tr?'1':'0'});var k=mk+'|'+c;
    if(gk[k]==null){gk[k]=P.length;P.push({c:c,mk:mk,a:0,ix:[]})}var g=P[gk[k]];g.a+=o.a;g.ix.push(i)});
  var N=P.length,V=N+m+2,S=0,T=V-1,E=[],adj=[],v,i;for(v=0;v<V;v++)adj.push([]);
  function add(u,w,cap,cost){adj[u].push(E.length);E.push({u:u,v:w,cap:cap,cost:cost});adj[w].push(E.length);E.push({u:w,v:u,cap:0,cost:-cost})}
  var GB=[];P.forEach(function(g,j){add(S,1+j,g.a,0);GB.push([]);B.forEach(function(b,k){if(g.mk[k]==='1'){GB[j][k]=E.length;add(1+j,1+N+k,g.a,-(b.r-g.c))}})});
  B.forEach(function(b,k){add(1+N+k,T,b.cap,0)});
  for(var guard=0;guard<500;guard++){var d=[],pe=[],iq=[],q=[S];for(v=0;v<V;v++){d.push(Infinity);pe.push(-1);iq.push(false)}d[S]=0;iq[S]=true;
    while(q.length){var u=q.shift();iq[u]=false;adj[u].forEach(function(ei){var e=E[ei];if(e.cap>1e-9&&d[u]+e.cost<d[e.v]-1e-12){d[e.v]=d[u]+e.cost;pe[e.v]=ei;if(!iq[e.v]){iq[e.v]=true;q.push(e.v)}}})}
    if(!(d[T]<-1e-12))break;
    var f=Infinity;for(v=T;v!==S;v=E[pe[v]].u)f=Math.min(f,E[pe[v]].cap);
    for(v=T;v!==S;v=E[pe[v]].u){E[pe[v]].cap-=f;E[pe[v]^1].cap+=f}}
  var al=rows.map(function(){return {}}),cu={},pa=0;BK.forEach(function(b){cu[b.id]=b.id==='base'?Infinity:0});
  P.forEach(function(g,j){B.forEach(function(b,k){var ei=GB[j][k];if(ei==null)return;var fl=E[ei^1].cap;if(fl<=1e-9)return;cu[b.id]+=fl;
    g.ix.forEach(function(ii){var t=fl*rows[ii].a/g.a;al[ii][b.id]=(al[ii][b.id]||0)+t;pa+=t*b.r})})});
  rows.forEach(function(o,ii){var s=0;for(var k in al[ii])s+=al[ii][k];var rest=o.a-s;if(rest>1e-6){al[ii].base=rest;pa+=rest*Math.max(1,o.tr)}});
  var used={abg:(cu.abg4||0)>0,ibp:(cu.ibp3||0)>0||(cu.ibc5||0)>0,cap:(cu.cap2||0)>0};
  var fee=(used.abg?CARD.abg.fee:0)+(used.ibp?CARD.ibp.fee:0)+(used.cap?CARD.cap.fee:0);
  return {al:al,cu:cu,pa:pa,fee:fee,pair:pair,ibp:ibp,cp:cp,used:used}}
function best(rows,cpp){var cats=[];rows.forEach(function(o){var c=o.l.e.abg;if(c&&cats.indexOf(c)<0)cats.push(c)});
  var pairs=[[]];cats.forEach(function(c,i){pairs.push([c]);for(var j=i+1;j<cats.length;j++)pairs.push([c,cats[j]])});
  /* every Business Gold pair, with and without Ink Business Preferred, with and without Venture Business: the stack that finds the most after fees */
  var top=null;pairs.forEach(function(pr){[true,false].forEach(function(ib){[false,true].forEach(function(cp){var r=route(rows,pr,ib,cp);r.v=r.pa*UTIL*cpp/100-r.fee;if(!top||r.v>top.v+1e-9)top=r})})});
  return top}

/* ---------------- the month ---------------- */
/* ---------------- the month: A = $ a month per line, T = how each line is paid today, use = how the points are used,
   mix = 'ex' (each line as set) or one rate for every card line ---------------- */
function model(A,T,use,mix){var u=U(use),rows=[],mo=0,off=0,t=0;
  LN.forEach(function(l){var m=A[l.id]||0;if(!m)return;var k=mix==='ex'?T[l.id]:(T[l.id]==='none'?'none':mix);
    if(k==='none'){off+=m;return}mo+=m;var tr=TR[k][2];t+=m*tr;rows.push({l:l,a:m*12,m:m,tr:tr})});
  var R=best(rows,u.mid),d=R.pa/12,cf=R.fee/12,gain=Math.max(0,d-t)*UTIL;
  /* found money: the extra points at the use's floor, middle and top. Card annual fees (cf) are shown, not taken off (Ohad, 31 Oct 2026) */
  return {u:u,rows:rows,R:R,mo:mo,off:off,t:t,d:d,cf:cf,lo:gain*u.floor/100,mid:gain*u.mid/100,hi:gain*u.ceil/100,flat:u.floor===u.ceil}}
function verdict0(r){var f=r.flat;
  if(r.mo<GATE)return {c:'no',t:'Not a fit yet.',p:'At '+usd(r.mo)+' a month on cards, $550 a month would cost you more than it finds. The fee starts to make sense past ~$25K a month, est.'};
  if(r.lo>=FEE)return {c:'fit',t:'Clears the fee.',p:'Even at the floor, the extra points beat $550 a month, est. Your Found Money Call checks it on your real statements.'};
  if(r.hi>=FEE)return {c:'meh',t:'Close call.',p:'It clears at the top of the range, not the floor. Your Found Money Call settles it on your real statements, free.'};
  return {c:'no',t:'Not a fit yet.',p:'The extra points find about '+(f?u10(Math.max(0,r.lo)):u10(Math.max(0,r.lo))+' to '+u10(Math.max(0,r.hi)))+' a month, est., under the $550.'}}
function verdict(r){var v=verdict0(r);
  if(r.mo>BIG)v.p+=' Above $250K a month, the desk sizes it on the call: bigger spend often runs on more than one card per category.';
  return v}

/* ---------------- an industry's typical mix, as is (spend null) or scaled so its card lines add up to the spend exactly, in $100 steps;
   lines not on a card stay as they are. The steps are shared out by Webster's method, one $100 at a time to the line furthest below its
   share, so the lines always add up to the spend (a $25K question is judged at $25K, not $24,700) and no line ever shrinks as the spend
   grows (so what the desk finds can only grow) ---------------- */
function apportion(w,H){var n=w.length,s=[],j,k,b,top;for(j=0;j<n;j++)s.push(0);
  for(k=0;k<H;k++){top=-1;b=-1;for(j=0;j<n;j++){var pr=w[j]/(2*s[j]+1);if(pr>top){top=pr;b=j}}if(b<0)break;s[b]++}
  return s}
function mixOf(i,spend){var p=IND[i],m0=p[3],A={},T={},on=[];
  LN.forEach(function(l){var v=m0[l.id];A[l.id]=v?v[0]:0;T[l.id]=v&&v[1]?v[1]:(l.g==='nc'?'none':'1');if(v&&T[l.id]!=='none')on.push(l.id)});
  if(spend!=null&&spend>=0&&on.length){var u=apportion(on.map(function(id){return A[id]}),Math.round(spend/100));on.forEach(function(id,j){A[id]=u[j]*100})}
  return {A:A,T:T}}
function forSpend(i,spend,use,mix){var m=mixOf(i,spend);return model(m.A,m.T,use||'mix',mix||'ex')}

/* ---------------- the starting point: the industry asked for (?ind=, ?industry=, ?ex=), else the trade page the visitor just came
   from, else Other ---------------- */
var idx=0;
var q=location.search,qp={};q.replace(/^\?/,'').split('&').forEach(function(kv){if(!kv)return;var p=kv.split('=');try{qp[decodeURIComponent(p[0])]=decodeURIComponent((p[1]||'').replace(/\+/g,' '))}catch(e){}});
/* the starting point: the industry asked for (?ind=, ?industry=, ?ex=), else the trade page the visitor just came from, else Other */
var VIA=false;
(function(){var want=slug(qp.industry||qp.ind||''),ex=(qp.ex||'').toLowerCase();
  if(!want&&!ex){var rf=document.referrer||'',rm=rf.indexOf(location.origin)===0&&rf.match(/\/for-([a-z-]+)\.html/);if(rm){want=slug(rm[1]);VIA=true}}
  if(ALIAS[want])want=ALIAS[want];
  IND.forEach(function(p,i){if(p[0]==='other')idx=i});
  IND.forEach(function(p,i){if((want&&(p[0]===want||slug(p[1])===want))||(ex&&p[2]&&p[2].toLowerCase()===ex))idx=i})})();
var SP=+(qp.spend||0)||0;

var subs=[];
window.FO_CALC={BS:BS,FEE:FEE,GATE:GATE,UTIL:UTIL,BIG:BIG,CARD:CARD,BK:BK,ABGC:ABGC,G:G,LN:LN,LI:LI,TODAY:TODAY,TR:TR,IND:IND,ALIAS:ALIAS,
  slug:slug,U:U,model:model,verdict:verdict,mixOf:mixOf,forSpend:forSpend,qp:qp,via:VIA,sp:SP,idx:idx,
  set:function(i){this.idx=i;subs.forEach(function(f){try{f(i)}catch(e){}})},
  on:function(f){subs.push(f)}};
})();
