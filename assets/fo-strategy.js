/* The desk, thinking: a small strategy board for the home page (Oct 28). Tiles are generic desk signals in the site's own
   words (no issuer or card names; MCC claims say "typically codes as"); each path lights five of them in order, draws the
   connections, and reads the move out in plain words. Paths rotate; the board rests when off screen or under reduced motion. */
(function(){
var T=[["Route","Lead-gen ads to the 4x card"],["Route","Agency software to the 4x card"],["Route","Carrier travel through the portal, 3x"],["Route","Everything else to the flat 2x card"],
 ["Vendor","Ad platforms typically code as 7311, advertising"],["Vendor","Shipping carriers typically code as 4215"],["Vendor","Wholesale food typically codes as 5099, 1x on most bonus cards"],["Vendor","Software typically codes as 5734"],
 ["Earn","4x on the top two categories, first $150k a year"],["Earn","3x on travel booked through the portal"],["Earn","2x flat on everything else"],["Cap","4x cap reached in November: reroute"],
 ["Transfer","Points to an airline partner, 1:1"],["Transfer","Transfer only once award space is confirmed"],["Bonus","30% transfer bonus open this month"],["Rules","Award chart repricing announced for Q2"],
 ["Trip","Tokyo in business for 2: about 320k points, est."],["Trip","5 hotel nights on points for carrier visits, est."],["Credit","Unused travel credit, $530, claimed"],["Credit","Statement credit resets January 1"],
 ["Fee","Annual fee posts in 14 days: review it"],["Fee","Premium card fee: net positive with 3 travellers, est."],["Learn","What one point is worth: about 1.6 cents, est."],["Learn","Expiry clock: 24 months without activity"]];
var P=[{n:"Earn",t:[0,4,8,11,3],r:"Leo's lead-gen ads move to the 4x card. Ad platforms typically code as advertising, which the card's top two categories cover up to the yearly cap; when the cap hits in November, the overflow reroutes to the flat 2x card. Worth about $7,200 a year, est. Waiting for Leo's OK."},
 {n:"Burn",t:[16,12,14,13,15],r:"Tokyo in business for 2 needs about 320k points, est. The desk maps the airline partner at 1:1, catches the 30% bonus that is open this month, and transfers only once award space is confirmed, with the Q2 repricing in view. Leo picks the dates. The desk books after he approves."},
 {n:"Return",t:[18,20,21,19,17],r:"The unused travel credit is claimed, $530. The annual fee posting in 14 days is reviewed against what the card earned; with three travellers it is net positive, est. The statement credit resets January 1, so the hotel nights for carrier visits go on points first. All of it lands in Friday's report, in dollars."},
 {n:"Learn",t:[22,23,6,1,9],r:"One point on Leo's plan is worth about 1.6 cents, est., and points in some programs expire after 24 months without activity. Wholesale food typically codes as 5099 and earns 1x on most bonus cards, so software goes to the 4x card and travel through the portal at 3x. Two minutes, once a week."}];
var g=document.getElementById('sbGrid'),rd=document.getElementById('sbRead'),lb=document.querySelector('[data-sb="label"]');if(!g||!rd)return;
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches,NS='http://www.w3.org/2000/svg';
var svg=document.createElementNS(NS,'svg');svg.setAttribute('class','sb-svg');g.appendChild(svg);
T.forEach(function(t,i){var d=document.createElement('div');d.className='sb-t';d.dataset.i=i;d.innerHTML='<small>'+t[0]+'</small>'+t[1];g.appendChild(d)});
var tiles=[].slice.call(g.querySelectorAll('.sb-t')),cur=-1,timers=[],live=false;
function clear(){timers.forEach(clearTimeout);timers=[];tiles.forEach(function(t){t.className='sb-t'});svg.innerHTML='';rd.classList.remove('vis')}
function conn(a,b){var gr=g.getBoundingClientRect(),ar=a.getBoundingClientRect(),br=b.getBoundingClientRect();
 var x1=ar.left+ar.width/2-gr.left,y1=ar.top+ar.height/2-gr.top,x2=br.left+br.width/2-gr.left,y2=br.top+br.height/2-gr.top,dx=x2-x1,dy=y2-y1;
 var p=document.createElementNS(NS,'path');p.setAttribute('d','M'+x1+' '+y1+' Q'+((x1+x2)/2-dy*.18)+' '+((y1+y2)/2+dx*.18)+' '+x2+' '+y2);svg.appendChild(p);
 var len=p.getTotalLength();p.style.strokeDasharray=len;p.style.strokeDashoffset=len;requestAnimationFrame(function(){p.classList.add('vis');p.style.strokeDashoffset=0});
 var c=document.createElementNS(NS,'circle');c.setAttribute('cx',x2);c.setAttribute('cy',y2);c.setAttribute('r',4);svg.appendChild(c)}
function run(){clear();cur=(cur+1)%P.length;var path=P[cur];if(lb)lb.textContent='Path '+(cur+1)+' of '+P.length+' · '+path.n;
 var step=RM?0:520;
 path.t.forEach(function(ti,si){timers.push(setTimeout(function(){var t=tiles[ti];t.classList.add('on');if(si>0)conn(tiles[path.t[si-1]],t);
  if(si===path.t.length-1){timers.push(setTimeout(function(){rd.querySelector('p').textContent=path.r;rd.classList.add('vis')},RM?0:260))}},si*step))});
 if(!RM){var amb=[];while(amb.length<6){var r=Math.floor(Math.random()*T.length);if(path.t.indexOf(r)<0&&amb.indexOf(r)<0)amb.push(r)}
  amb.forEach(function(ri,ai){timers.push(setTimeout(function(){if(!tiles[ri].classList.contains('on'))tiles[ri].classList.add('lit')},300+ai*240))});
  timers.push(setTimeout(function(){if(live)run()},path.t.length*step+6200))}}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!live){live=true;run()}else if(!e.isIntersecting&&live){live=false;clear()}})},{threshold:.25});
io.observe(g);
addEventListener('resize',function(){if(live){clear();run()}});
})();
