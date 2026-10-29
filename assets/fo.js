/* mockup helpers: dropdown on tap, carousels, tabs */
document.querySelectorAll('.dd>button').forEach(b=>b.addEventListener('click',e=>{b.parentNode.classList.toggle('open');e.stopPropagation()}));
document.addEventListener('click',()=>document.querySelectorAll('.dd.open').forEach(d=>d.classList.remove('open')));
document.querySelectorAll('[data-tabs]').forEach(g=>{const bs=g.querySelectorAll('[data-t]');bs.forEach(b=>b.addEventListener('click',()=>{bs.forEach(x=>x.classList.toggle('on',x===b));g.querySelectorAll('[data-p]').forEach(p=>p.hidden=p.dataset.p!==b.dataset.t)}))});
document.querySelectorAll('select[data-go]').forEach(s=>s.addEventListener('change',()=>{if(s.value)location.href=s.value}));
