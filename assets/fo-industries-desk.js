/* Industries: one trade at a time. Figures are the ones already published on the trade pages and this page. */
(function(){
var WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call';
var T={
hvac:{name:'HVAC',href:'for-hvac.html',img:'img/ind/hvac-800.webp',calc:'hvac',line:'Equipment, refrigerant, fuel',
 who:'Hector, Desert Breeze Heating & Air',place:'Phoenix, AZ',spend:'about $36,700 a month on cards',
 note:'Parts and equipment were earning 1x. The desk matches them to Blue Business Plus, then Capital One Venture Business at 2x. That catch is about $4,100 a year, est. Fictional owner.',
 lines:[['Parts and equipment','$21,800/mo','1x to 2x, Blue Business Plus, then Capital One Venture Business'],['Fleet fuel','$6,600/mo','1x to 4x, Amex Business Gold at gas stations'],['Online ads','$3,000/mo','1.5x to 4x, Amex Business Gold on advertising'],['Everything else','$5,300/mo','1.3x to 2.9x, Capital One Venture Business, Ink Business Cash and others']],
 earn:'1.1 points per dollar now. 2.7 with the desk, est.',
 burn:'Maui for a family of 4, spring break. 41% of the points are there.',
 ret:'2.7 points per dollar times 1.6 cents a point is 4.3 cents per dollar of spend, est. This example states both numbers. A gift, a freebie, or a Friday tally is not Return.',
 learn:'One short lesson a week, from this example. The cents per point used here are the 1.6 cents already stated.'},
dental:{name:'Dental',href:'for-dental.html',img:'img/ind/dental-800.webp',calc:'dental-practice',line:'Supplies, labs, patient ads',
 who:'Leila, Brightside Family Dental',place:'Charlotte, NC',spend:'about $32,000 a month on cards',
 note:'Dental supplies were earning 1x. The desk matches them to Blue Business Plus, then Capital One Venture Business at 2x. That catch is about $2,400 a year, est. Fictional owner.',
 lines:[['Dental supplies','the largest line','1x to 2x']],
 earn:'1.2 points per dollar now. 2.7 with the desk, est.',
 burn:'Paris in business for 2, in June, her 10th year. 46% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'},
agencies:{name:'Agencies',href:'for-agencies.html',img:'img/ind/agencies-800.webp',calc:'marketing-agency',line:'Client ad spend, software, contractors',
 who:'Anjali, Bright Hour Creative',place:'Denver, CO',spend:'about $38,000 a month on cards',
 note:'Client ad spend was earning 1x. The desk matches it to Amex Business Gold, then Ink Business Preferred at 3.5x. That catch is about $6,300 a year, est. Fictional owner.',
 lines:[['Client ad spend','the largest line','1x to 3.5x']],
 earn:'1.4 points per dollar now. 3.1 with the desk, est.',
 burn:'Lisbon in business for 2, this fall. 58% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'},
law:{name:'Law firms',href:'for-law-firms.html',img:'img/ind/law-firms-800.webp',calc:'law-firm',line:'Research, filing fees, travel',
 who:'Chidi, Okafor & Lane Law',place:'Atlanta, GA',spend:'about $25,000 a month on cards',
 note:'Research software was earning 1x. The desk matches it to Amex Business Gold at 4x. That catch is about $2,400 a year, est. Fictional owner.',
 lines:[['Research software','the catch line','1x to 4x']],
 earn:'1.1 points per dollar now. 3.1 with the desk, est.',
 burn:'Lagos in business for 4, next summer. 37% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'},
restaurants:{name:'Restaurants',href:'for-restaurants.html',img:'img/ind/restaurants-800.webp',calc:'restaurant',line:'Food suppliers, delivery apps, utilities',
 who:'Teresa, Little Fig Trattoria',place:'Austin, TX',spend:'about $26,000 a month on cards',
 note:'Food suppliers were earning 1x. The desk matches them to Blue Business Plus, then Capital One Venture Business at 2x. That catch is about $3,000 a year, est. Fictional owner.',
 lines:[['Food suppliers','the catch line','1x to 2x']],
 earn:'1.1 points per dollar now. 2.4 with the desk, est.',
 burn:'Tokyo in business for 2, next spring. 44% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'},
trucking:{name:'Trucking',href:'for-trucking.html',img:'img/ind/trucking-800.webp',calc:'trucking',line:'Fuel, tires, tolls',
 who:'Wade, Ridgeway Freight Lines',place:'Columbus, OH',spend:'about $63,000 a month on cards, about $46,000 of it fuel',
 note:'Fleet fuel was earning 1x. The desk matches it to Amex Business Gold, then Ink Business Cash, then Blue Business Plus, then Capital One Venture Business at 2.5x. That catch is about $13,300 a year, est. Fictional owner.',
 lines:[['Fleet fuel','about $46,000/mo','1x to 2.5x']],
 earn:'1 point per dollar now. 2.5 with the desk, est.',
 burn:'Istanbul in business for 4, for a family wedding. 52% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'},
realestate:{name:'Real estate',href:'for-real-estate.html',img:'img/ind/real-estate-800.webp',calc:'real-estate',line:'Listing ads, signage, travel',
 who:'Terrence, Keystone Realty Group',place:'Dallas, TX',spend:'about $35,000 a month on cards',
 note:'Listing ads were earning 1.5x. The desk matches them to Amex Business Gold at 4x. That catch is about $5,100 a year, est. Fictional owner.',
 lines:[['Listing ads','the catch line','1.5x to 4x']],
 earn:'1.2 points per dollar now. 3 with the desk, est.',
 burn:'Cancun for the top 6 agents, the contest prize. 39% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'},
ecommerce:{name:'E-commerce',href:'for-ecommerce.html',img:'img/ind/ecommerce-800.webp',calc:'e-commerce',line:'Ads, shipping, packaging',
 who:'Ines, Maple & Moss Candle Co.',place:'Portland, OR',spend:'about $30,000 a month on cards',
 note:'Meta and Google ads were earning 1x on a 1% cash back card. The desk matches them to Amex Business Gold, then Ink Business Preferred at 4x. That catch is about $6,000 a year, est. Fictional owner.',
 lines:[['Meta and Google ads','the catch line','1x to 4x']],
 earn:'1 point per dollar now. 3 with the desk, est.',
 burn:'Bali in business, a December honeymoon. 34% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'},
contractors:{name:'Contractors',href:'for-contractors.html',img:'img/ind/contractors-800.webp',calc:'contractor',line:'Materials, rentals, job-site hotels',
 who:'Dustin, Ironclad Commercial Roofing',place:'Kansas City, MO',spend:'about $73,000 a month on cards',
 note:'Roofing materials were earning 1x. The desk matches them to Blue Business Plus, then Capital One Venture Business at 2x. That catch is about $8,200 a year, est. Fictional owner.',
 lines:[['Roofing materials','the catch line','1x to 2x']],
 earn:'1.1 points per dollar now. 2.3 with the desk, est.',
 burn:'Cabo for the family, in January. 61% of the points are there.',
 ret:'Not calculated. The earn rate is here. What a point is worth in cents is not in this example, so Return stays blank. Unknown is not zero.',
 learn:'One short lesson a week, from this example. It does not add a cents-per-point figure the example does not state.'}
};
var PLAIN={
'auto-repair':{name:'Auto repair',href:'for-auto-repair.html',img:'img/ind/auto-repair-shop-800.webp',calc:'auto-repair',line:'Parts, tools, towing'},
cleaning:{name:'Cleaning',href:'for-cleaning.html',img:'img/ind/cleaning-800.webp',calc:'cleaning',line:'Supplies, laundry, vehicles'},
consulting:{name:'Consulting',href:'for-consulting.html',img:'img/ind/consulting-800.webp',calc:'consulting',line:'Client travel, software, research'},
cpa:{name:'CPA firms',href:'for-cpa-firms.html',img:'img/ind/cpa-firms-800.webp',calc:'cpa-firm',line:'Software, research, filing fees'},
fitness:{name:'Fitness',href:'for-fitness.html',img:'img/ind/fitness-800.webp',calc:'fitness',line:'Equipment, software, ads'},
it:{name:'IT services',href:'for-it-services.html',img:'img/ind/it-services-800.webp',calc:'it-services',line:'Hardware, licenses, cloud'},
landscaping:{name:'Landscaping',href:'for-landscaping.html',img:'img/ind/landscaping-800.webp',calc:'landscaping',line:'Plants, fuel, equipment'},
medical:{name:'Medical',href:'for-medical.html',img:'img/ind/medical-exam-800.webp',calc:'medical-practice',line:'Supplies, labs, software'},
property:{name:'Property management',href:'for-property-management.html',img:'img/ind/property-management-800.webp',calc:'property-management',line:'Repairs, utilities, software'},
salons:{name:'Salons',href:'for-salons.html',img:'img/ind/salons-800.webp',calc:'salon-or-spa',line:'Product, booking software, ads'},
veterinary:{name:'Veterinary',href:'for-veterinary.html',img:'img/ind/veterinary-800.webp',calc:'veterinary-clinic',line:'Pharmacy, labs, supplies'}
};
function esc(s){return String(s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function story(id){
  var s=T[id];
  if(!s){var p=PLAIN[id]; if(!p) return '';
    return '<figure class="idk-photo"><img src="'+p.img+'" alt=""></figure><div class="idk-body"><p class="idk-who">'+esc(p.name)+'</p><h3>'+esc(p.line)+'</h3><p class="idk-note">The example owner and the line-by-line mix for '+esc(p.name.toLowerCase())+' stay on that trade page. Figures there are estimates. The owner is fictional.</p><div class="idk-actions"><a class="btn pk" href="'+p.href+'">Open the '+esc(p.name.toLowerCase())+' page <span class="ar">→</span></a><a class="btn lb" href="calculator.html?ind='+encodeURIComponent(p.calc)+'">Run your numbers</a></div></div>';
  }
  var lines=s.lines.map(function(r){return '<li><span>'+esc(r[0])+'</span><b>'+esc(r[1])+'</b><span>'+esc(r[2])+'</span></li>'}).join('');
  return '<figure class="idk-photo"><img src="'+s.img+'" alt=""></figure><div class="idk-body"><p class="idk-who">Example, fictional</p><h3>'+esc(s.who)+'</h3><p class="idk-meta">'+esc(s.place)+'. '+esc(s.spend)+'.</p><p class="idk-note">'+esc(s.note)+'</p><ul class="idk-lines">'+lines+'</ul><dl class="idk-pillars"><div class="idk-earn"><dt>Earn</dt><dd>'+esc(s.earn)+'</dd></div><div class="idk-burn"><dt>Burn</dt><dd>'+esc(s.burn)+'</dd></div><div class="idk-return"><dt>Return</dt><dd>'+esc(s.ret)+'</dd></div><div class="idk-learn"><dt>Learn</dt><dd>'+esc(s.learn)+'</dd></div></dl><div class="idk-actions"><a class="btn pk" href="book.html">Get Your Desk <span class="ar">→</span></a><a class="btn wa" href="'+WA+'">Message your First Officer</a><a class="btn lb" href="calculator.html?ind='+encodeURIComponent(s.calc)+'">Run your numbers</a></div><p class="idk-fine">Illustrative estimate. Not a testimonial and not a promise. <a href="'+s.href+'">The full '+esc(s.name.toLowerCase())+' page</a>.</p></div>';
}
var root=document.getElementById('idk-story');
var tabs=document.querySelectorAll('.idk-tab');
if(!root||!tabs.length) return;
function show(id){
  if(!T[id]&&!PLAIN[id]) return;
  root.innerHTML=story(id);
  tabs.forEach(function(b){if(b.getAttribute('data-trade')===id)b.setAttribute('aria-current','true');else b.removeAttribute('aria-current')});
}
tabs.forEach(function(b){
  b.addEventListener('click',function(e){e.preventDefault(); show(b.getAttribute('data-trade'))});
});
show('hvac');
})();
