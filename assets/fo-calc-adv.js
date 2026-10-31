/* calculator.html · Go advanced (31 Oct 2026). Ohad: "if we do advanced - then advance and sophisticated it is".
   Every line of a business's spend, in ten groups, each with its own monthly amount and how it is paid today. No catch-all line.
   The desk side: every line on a card goes through the universal card stack, inside each card's yearly cap:
     Ink Business Cash      5x office supply stores + internet, cable and phone, $25K a year combined; 2x gas stations + restaurants, $25K a year combined
     Amex Business Gold     4x on its top 2 of 6 categories each month, $150K a year combined (the desk tries every pair and keeps the best)
     Ink Business Preferred 3x travel, shipping, internet, cable and phone, search and social ads, $150K a year combined
     Blue Business Plus     2x everyday purchases, $50K a year
     Capital One Venture Business  2x on every purchase, no cap, $95 a year: spend past the caps above earns 2x here, but only when it
                            covers its fee (the desk tries the stack with and without it). Without it, past every cap a line stays on the
                            card it is on today (never under 1x). Ohad, 19 Sep: "Capital One also gets them 2x". Spark Miles became Venture
                            Business in spring 2026.
   A card only takes a line it improves: the desk never moves spend to a card that earns less than it does today.
   Value: FO_REDEMPTION_BASIS (85% of the extra points counted, cents a point by use), less the stack's annual card fees, against the $550 a month fee.
   Lines not on a card are not counted. Nothing typed here is stored or sent from this script. Every figure is an estimate; terms as understood Oct 2026.
   URL: ?ind=<slug> or ?industry=<name or slug> picks the industry, ?ex=<first name> its example's industry, ?spend=<n> scales the mix to n a month. */
(function(){
'use strict';
var BS=window.FO_REDEMPTION_BASIS,root=document.getElementById('adx');if(!BS||!root)return;var sec=document.getElementById('advs')||root;
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

/* ---------------- the card stack, as modelled (terms as understood Oct 2026, est.) ---------------- */
var CARD={
  ibc:{n:'Ink Business Cash',fee:0,t:'5x at office supply stores and on internet, cable and phone, up to $25K a year combined; 2x at gas stations and restaurants, up to $25K a year combined; then 1x. Counted as points alongside Ink Business Preferred.'},
  abg:{n:'Amex Business Gold',fee:375,t:'4x on the 2 categories it is used for most each month, from 6 eligible, up to $150K a year combined; then 1x.'},
  ibp:{n:'Ink Business Preferred',fee:95,t:'3x on travel, shipping, internet, cable and phone, and search and social ads, up to $150K a year combined; then 1x.'},
  bbp:{n:'Blue Business Plus',fee:0,t:'2x on everyday business purchases, up to $50K a year; then 1x.'},
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
function tShort(k){return k==='none'?'Not on a card':/^c/.test(k)?TR[k][1].replace(' cash back',' back'):x(TR[k][2])}

/* ---------------- the 21 industries the site covers, in the Industries page's order and names: the 20 trades, then Other, a general small-business mix.
   Each: [slug, name, example owner's first name, $ a month and how each line is paid today (est., fictional), things to consider, how the sentence names it].
   Every trade page's example owner runs here: calculator.html?ind=<slug>&ex=<name>&spend=<their spend> scales this mix to their spend. ---------------- */
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

/* ---------------- state ---------------- */
var A={},T={},use='mix',mix='ex',idx=0,first=true;
var q=location.search,qp={};q.replace(/^\?/,'').split('&').forEach(function(kv){if(!kv)return;var p=kv.split('=');try{qp[decodeURIComponent(p[0])]=decodeURIComponent((p[1]||'').replace(/\+/g,' '))}catch(e){}});
/* the starting point: the industry asked for (?ind=, ?industry=, ?ex=), else the trade page the visitor just came from, else Other */
var VIA=false;
(function(){var want=slug(qp.industry||qp.ind||''),ex=(qp.ex||'').toLowerCase();
  if(!want&&!ex){var rf=document.referrer||'',rm=rf.indexOf(location.origin)===0&&rf.match(/\/for-([a-z-]+)\.html/);if(rm){want=slug(rm[1]);VIA=true}}
  if(ALIAS[want])want=ALIAS[want];
  IND.forEach(function(p,i){if(p[0]==='other')idx=i});
  IND.forEach(function(p,i){if((want&&(p[0]===want||slug(p[1])===want))||(ex&&p[2]&&p[2].toLowerCase()===ex))idx=i})})();
var SP=+(qp.spend||0)||0;

/* ---------------- the router: every line on a card, inside each card's yearly cap ---------------- */
function okB(l,b,pair,ibp,cp){var e=l.e;if(b.id==='cap2')return !!cp;
  if(b.id==='ibc5')return ibp&&!!e.ibc5;if(b.id==='abg4')return !!e.abg&&pair.indexOf(e.abg)>-1;
  if(b.id==='ibp3')return ibp&&!!e.ibp3;if(b.id==='ibc2')return !!e.ibc2;return true}
function alt(l,k,pair,ibp,cp){var r=0;for(var j=k+1;j<BK.length;j++)if(okB(l,BK[j],pair,ibp,cp))r=Math.max(r,BK[j].r);return r}
function route(rows,pair,ibp,cp){var rem=rows.map(function(o){return o.a}),al=rows.map(function(){return {}}),cu={},pa=0;
  BK.forEach(function(b,k){var el=[],put=0;rows.forEach(function(o,i){if(rem[i]>0&&okB(o.l,b,pair,ibp,cp)&&(b.id==='base'||b.r>o.tr))el.push(i)});
    el.sort(function(p,s){return (alt(rows[p].l,k,pair,ibp,cp)-alt(rows[s].l,k,pair,ibp,cp))||(rem[s]-rem[p])});
    var left=b.cap;el.forEach(function(i){if(left<=0)return;var t=Math.min(rem[i],left);al[i][b.id]=t;rem[i]-=t;left-=t;put+=t;pa+=t*(b.id==='base'?Math.max(b.r,rows[i].tr):b.r)});
    cu[b.id]=b.id==='base'?b.cap:put});
  var used={abg:(cu.abg4||0)>0,ibp:(cu.ibp3||0)>0||(cu.ibc5||0)>0,cap:(cu.cap2||0)>0};
  var fee=(used.abg?CARD.abg.fee:0)+(used.ibp?CARD.ibp.fee:0)+(used.cap?CARD.cap.fee:0);
  return {al:al,cu:cu,pa:pa,fee:fee,pair:pair,ibp:ibp,cp:cp,used:used}}
function best(rows,cpp){var cats=[];rows.forEach(function(o){var c=o.l.e.abg;if(c&&cats.indexOf(c)<0)cats.push(c)});
  var pairs=[[]];cats.forEach(function(c,i){pairs.push([c]);for(var j=i+1;j<cats.length;j++)pairs.push([c,cats[j]])});
  /* every Business Gold pair, with and without Ink Business Preferred, with and without Venture Business: the stack that finds the most after fees */
  var top=null;pairs.forEach(function(pr){[true,false].forEach(function(ib){[false,true].forEach(function(cp){var r=route(rows,pr,ib,cp);r.v=r.pa*UTIL*cpp/100-r.fee;if(!top||r.v>top.v+1e-9)top=r})})});
  return top}

/* ---------------- the month ---------------- */
function model(){var u=U(use),rows=[],mo=0,off=0,t=0;
  LN.forEach(function(l){var m=A[l.id]||0;if(!m)return;var k=mix==='ex'?T[l.id]:(T[l.id]==='none'?'none':mix);
    if(k==='none'){off+=m;return}mo+=m;var tr=TR[k][2];t+=m*tr;rows.push({l:l,a:m*12,m:m,tr:tr})});
  var R=best(rows,u.mid),d=R.pa/12,cf=R.fee/12,gain=Math.max(0,d-t)*UTIL;
  return {u:u,rows:rows,R:R,mo:mo,off:off,t:t,d:d,cf:cf,lo:gain*u.floor/100-cf,mid:gain*u.mid/100-cf,hi:gain*u.ceil/100-cf,flat:u.floor===u.ceil}}
function verdict(r){var f=r.flat;
  if(r.mo<GATE)return {c:'no',t:'Not a fit yet.',p:'At '+usd(r.mo)+' a month on cards, $550 a month would cost you more than it finds. The fee starts to make sense past ~$25K a month, est.'};
  if(r.lo>=FEE)return {c:'fit',t:'Clears the fee.',p:'Even at the floor, after the card fees, the extra points beat $550 a month, est. Your Found Money Call checks it on your real statements.'};
  if(r.hi>=FEE)return {c:'meh',t:'Close call.',p:'It clears at the top of the range, not the floor. Your Found Money Call settles it on your real statements, free.'};
  return {c:'no',t:'Not a fit yet.',p:'After the card fees, the extra points find about '+(f?u10(Math.max(0,r.lo)):u10(Math.max(0,r.lo))+' to '+u10(Math.max(0,r.hi)))+' a month, est., under the $550.'}}

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
  bal.setAttribute('aria-label','Your desk finds about '+u10(mid)+' a month, est., after card fees, against the $550 a month fee')}
function bname(b,l){if(b==='abg4')return {c:'abg',r:4,w:'Amex Business Gold',k:ABGC[l.e.abg]};if(b==='ibp3')return {c:'ibp',r:3,w:'Ink Business Preferred',k:l.e.ibp3};
  if(b==='ibc5')return {c:'ibc',r:5,w:'Ink Business Cash',k:l.e.ibc5};if(b==='ibc2')return {c:'ibc',r:2,w:'Ink Business Cash',k:'gas and restaurants'};
  if(b==='bbp2')return {c:'bbp',r:2,w:'Blue Business Plus',k:'everyday purchases'};if(b==='cap2')return {c:'cap',r:2,w:'Capital One Venture Business',k:'every purchase'};return {c:'',r:1,w:'1x past the caps',k:''}}
function bnameO(b,o){var n=bname(b,o.l);if(b==='base'&&o.tr>1){n.r=o.tr;n.w='the card it is on today';n.k=''}return n}
function parts(r,i){var al=r.R.al[i],o=r.rows[i],out=[];BK.forEach(function(b){if(al[b.id]>0)out.push({b:b.id,a:al[b.id]/12,n:bnameO(b.id,o)})});return out}
function desc(ps){if(ps.length===1){var p=ps[0];return p.n.c?'on '+p.n.w+(p.n.k?' ('+p.n.k+')':''):(p.n.r>1?'stays on the card it is on today':'past the yearly caps')}
  return 'from '+ps.map(function(p,j){var s=p.n.c?p.n.r+'x '+p.n.w+(p.n.k?' ('+p.n.k+')':''):(p.n.r>1?p.n.r+'x on the card it is on today':'1x past the caps');return (j?'then ':'')+s+' on '+ks(p.a)}).join(', ')}

function paint(){var r=model(),v,G2=r.mo>BIG;v=verdict(r);
  if(G2)v.p+=' Above $250K a month, the desk sizes it on the call: bigger spend often runs on more than one card per category.';
  var fm=function(n){return '~'+u10(Math.max(0,n))};
  K('find',r.mid,fm);K('m-find',r.mid,fm);
  S('findr',r.flat?'at '+c2(r.u.floor)+' a point':u10(Math.max(0,r.lo))+' to '+u10(Math.max(0,r.hi)));
  S('cfees',r.cf>0?'After about '+usd(r.cf)+' a month in card annual fees, est.':'No card annual fees in this stack, est.');
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
  html+='<div class="xc xfees"><div class="xch"><b>Card annual fees</b><small>Taken off what the desk finds</small></div><p class="xct">'+(R.fee?(function(){var f=[];if(R.used.abg)f.push('Amex Business Gold $375');if(R.used.ibp)f.push('Ink Business Preferred $95');if(R.used.cap)f.push('Capital One Venture Business $95');return f.length>1?f.slice(0,-1).join(', ')+' and '+f[f.length-1]:f[0]})()+' a year, est. A card is left out when its points would not cover its fee.':'This mix needs no card with an annual fee, est.')+'</p><p class="xcp"><b>'+usd(R.fee/12)+'</b> a month, est.</p></div>';
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
function load(scale){var p=IND[idx],mix0=p[3],sum=0;
  LN.forEach(function(l){var v=mix0[l.id];A[l.id]=v?v[0]:0;T[l.id]=v&&v[1]?v[1]:(l.g==='nc'?'none':'1');if(v&&T[l.id]!=='none')sum+=v[0]});
  if(scale&&SP>0&&sum>0){var k=SP/sum;LN.forEach(function(l){if(A[l.id]&&T[l.id]!=='none')A[l.id]=Math.round(A[l.id]*k/100)*100})}
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
SEL.addEventListener('change',function(){idx=+SEL.value;SP=0;SEL.setAttribute('data-picked','1');load(false)});
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
