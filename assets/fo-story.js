/* The company map (.om) on pricing and enterprise.html: draws the lines from every team to the one desk, and from the desk to
   the Friday number, as an SVG behind the cards. Wide: each team curves into the desk. Narrow: each team joins one trunk on the
   right that runs down into the desk. Redrawn whenever the map changes size. The map and the first-month timeline (.fm) get
   .in when they come into view (the site's reveal observer does the same; this is the fallback). Decorative only: the cards
   carry the words, the SVG is aria-hidden. */
(function(){
  var NS='http://www.w3.org/2000/svg';
  function rel(r,B){return {l:r.left-B.left,t:r.top-B.top,r:r.right-B.left,b:r.bottom-B.top,cx:(r.left+r.right)/2-B.left,cy:(r.top+r.bottom)/2-B.top}}
  function f(n){return Math.round(n*10)/10}
  function path(svg,d,c,cls){var p=document.createElementNS(NS,'path');p.setAttribute('d',d);p.setAttribute('class',cls);if(c)p.style.setProperty('--c',c);svg.appendChild(p);return p}
  function draw(om){
    var box=om.querySelector('.om-in');if(!box)return;
    var desk=box.querySelector('.om-desk'),out=box.querySelector('.om-out');if(!desk)return;
    var svg=box.querySelector('svg.om-lines');
    if(!svg){svg=document.createElementNS(NS,'svg');svg.setAttribute('class','om-lines');svg.setAttribute('aria-hidden','true');svg.setAttribute('focusable','false');box.insertBefore(svg,box.firstChild)}
    var B=box.getBoundingClientRect();if(!B.width||!B.height)return;
    svg.setAttribute('viewBox','0 0 '+f(B.width)+' '+f(B.height));
    while(svg.firstChild)svg.removeChild(svg.firstChild);
    var D=rel(desk.getBoundingClientRect(),B),O=out?rel(out.getBoundingClientRect(),B):null;
    var rows=[].slice.call(box.querySelectorAll('.om-t'));
    var R=rows.map(function(r){return rel(r.getBoundingClientRect(),B)});
    var right=Math.max.apply(null,R.map(function(x){return x.r}));
    var wide=D.l>right+8;
    var made=[];
    rows.forEach(function(row,k){
      var c=getComputedStyle(row).getPropertyValue('--c').trim()||'#141216',r=R[k],d;
      if(wide){
        var x1=r.r,y1=r.cy,x2=D.l+6,y2=D.cy+(k-(rows.length-1)/2)*3,mx=x1+(x2-x1)*.55;
        d='M'+f(x1)+' '+f(y1)+' C'+f(mx)+' '+f(y1)+' '+f(mx)+' '+f(y2)+' '+f(x2)+' '+f(y2);
      }else{
        var tx=B.width-7,ty=D.t-26;
        d='M'+f(r.r)+' '+f(r.cy)+' H'+f(tx-8)+' Q'+f(tx)+' '+f(r.cy)+' '+f(tx)+' '+f(r.cy+8)+' V'+f(ty)+' C'+f(tx)+' '+f(D.t-6)+' '+f(D.cx+40)+' '+f(D.t-14)+' '+f(D.cx)+' '+f(D.t+2);
      }
      made.push(path(svg,d,c,'base'),path(svg,d,c,'flow'));
    });
    if(O){
      var c2=getComputedStyle(om).getPropertyValue('--ret').trim()||'#7149C9',d2;
      d2=wide?('M'+f(D.r-4)+' '+f(D.cy)+' L'+f(O.l-2)+' '+f(D.cy)):('M'+f(D.cx)+' '+f(D.b-4)+' L'+f(D.cx)+' '+f(O.t-2));
      made.push(path(svg,d2,c2,'base out'),path(svg,d2,c2,'flow out'));
    }
    made.forEach(function(p){try{p.style.setProperty('--len',Math.ceil(p.getTotalLength()+2))}catch(e){}});
  }
  function init(){
    var maps=[].slice.call(document.querySelectorAll('.om'));
    maps.forEach(function(om){
      [].forEach.call(om.querySelectorAll('.om-ent,.om-t'),function(e,k){e.style.setProperty('--k',k)});
      draw(om);
      if(window.ResizeObserver){var t;new ResizeObserver(function(){cancelAnimationFrame(t);t=requestAnimationFrame(function(){draw(om)})}).observe(om)}
      else addEventListener('resize',function(){draw(om)});
    });
    if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){maps.forEach(draw)});
    var els=[].slice.call(document.querySelectorAll('.om,.fm'));
    if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return}
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.18,rootMargin:'0px 0px -6% 0px'});
    els.forEach(function(e){io.observe(e)});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
