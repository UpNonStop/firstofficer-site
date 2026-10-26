# -*- coding: utf-8 -*-
# Free From the Desk, rebuild v4.
# Source of truth: _source/ffd-prior.html (Ohad's prior page, committed verbatim). This builder keeps ALL of its
# content and its look, swaps only the old nav/footer for the v4 shell (approved nav, ticker, footer), scopes the
# desk CSS under .desk so it cannot collide with site CSS, and layers the v4 "wow": reading view, live-filter motion,
# search highlights, count-up stats, sticky mobile picker. Everything motion-related honours prefers-reduced-motion.
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from fosite import page, ROOT

SRC = open(os.path.join(ROOT, '_source', 'ffd-prior.html'), encoding='utf-8').read()

# ---- 1. pieces of the prior page -------------------------------------------------------------
m = re.search(r'<main class="desk" id="top"><style>(.*?)</style>', SRC, re.S)
DESK_CSS = m.group(1)
c0 = SRC.index('<section class="dhero">')
c1 = SRC.index('<script id="deskjs">')
CONTENT = SRC[c0:c1].rstrip()
CONTENT = re.sub(r'\s*</main>\s*$', '', CONTENT)
j1 = SRC.index('</script>', c1)
DESKJS = SRC[c1 + len('<script id="deskjs">'):j1]
assert CONTENT.count('<article class="dk') == 109, CONTENT.count('<article class="dk')

# ---- 2. scope desk CSS under .desk -------------------------------------------------------------
def scope(css):
    out, i, n = [], 0, len(css)
    while i < n:
        b = css.find('{', i)
        if b < 0: out.append(css[i:]); break
        sel = css[i:b].strip()
        # matching close brace
        d, k = 1, b + 1
        while d and k < n:
            if css[k] == '{': d += 1
            elif css[k] == '}': d -= 1
            k += 1
        body = css[b + 1:k - 1]
        if sel.startswith('@media') or sel.startswith('@supports'):
            out.append(sel + '{' + scope(body) + '}')
        elif sel.startswith('@'):
            out.append(sel + '{' + body + '}')
        else:
            parts = []
            for s in sel.split(','):
                s = s.strip()
                if not s: continue
                if s.startswith('/*'):  # comment marker glued to a selector
                    cm = s[:s.index('*/') + 2]; s = s[s.index('*/') + 2:].strip(); out.append(cm)
                parts.append(s if (s == '.desk' or s.startswith('.desk ') or s.startswith('.desk[') or s.startswith('.desk.')) else '.desk ' + s)
            out.append(','.join(parts) + '{' + body + '}')
        i = k
    return ''.join(out)

SCOPED = scope(DESK_CSS)

# design-rule edits on the prior CSS (reported): no pink numbers
SCOPED = SCOPED.replace('.desk .deskline span:first-child b{color:var(--pink)}', '.desk .deskline span:first-child b{color:var(--ink)}')
assert '.desk .deskline span:first-child b{color:var(--ink)}' in SCOPED

# resets for site-wide classes that share names with the desk (.src/.chip/.lede/.pill from fo-site.css)
RESETS = '''
.desk{line-height:1.65;-webkit-font-smoothing:antialiased}
.desk .src{margin:0;padding:0;border:0;font:inherit;color:inherit}
.desk .chip{display:inline;border:0;font-family:inherit;line-height:inherit;color:inherit;cursor:auto;white-space:normal}
.desk .lede{margin-top:0;font-family:inherit;color:var(--ink);font-weight:400}
.desk .lede .hl{font-weight:700}
.desk h1,.desk h2,.desk h3{color:var(--ink)}
.desk ul,.desk ol{list-style-position:outside}
.desk ul.dates,.desk ul.mythlist,.desk ul.terms{list-style:none}
.desk .inside ol{list-style:decimal}
.desk a{color:inherit}
.desk img{display:block}
.desk button{font-family:inherit}
'''
# prior-design colour fixes inside the desk (reported): numbers are never pink
NONPINK = '''
.desk .grp-n{color:#6b6470}
.desk .inside ul.dates .date{color:var(--ink)}
'''

# ---- 3. v4 wow layer: CSS ------------------------------------------------------------------------
WOW_CSS = r'''
/* hero: pink hand-drawn underline draws under "over coffee.", Ohad's name writes itself in */
.desk h1 em{background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 14' preserveAspectRatio='none'%3E%3Cpath d='M3 9 C60 4 140 3 200 6 S280 9 297 5' fill='none' stroke='%23FA1896' stroke-opacity='.45' stroke-width='5' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat 0 92%/100% .16em;padding-bottom:.04em}
.desk.js h1 em{background-size:0% .16em;animation:dUl .9s cubic-bezier(.6,.05,.3,1) .45s forwards}
@keyframes dUl{to{background-size:100% .16em}}
.desk.js .dhero .sign,.desk.js .endnote.vis .sign{clip-path:inset(0 100% 0 0);animation:dSign 1.2s cubic-bezier(.5,0,.2,1) .35s forwards}
.desk.js .endnote:not(.vis) .sign{clip-path:inset(0 100% 0 0)}
@keyframes dSign{to{clip-path:inset(0 0 0 0)}}
.desk.js .dhero>*{animation:dUp .7s cubic-bezier(.2,.7,.2,1) both}
.desk.js .dhero>*:nth-child(2){animation-delay:.12s}
@keyframes dUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.desk.js .deskphoto{transition:transform .9s cubic-bezier(.2,.7,.2,1)}
/* cards: rise in as they enter, re-flow smoothly when the filter changes */
.desk.js .dk:not(.vis){opacity:0;transform:translateY(12px)}
.desk.js .dk{transition:opacity .45s cubic-bezier(.2,.7,.2,1),transform .45s cubic-bezier(.2,.7,.2,1),box-shadow .2s,border-color .2s}
.desk.js .dk.pop{animation:dPop .38s cubic-bezier(.2,.7,.2,1) both;animation-delay:var(--d,0ms)}
@keyframes dPop{from{opacity:0;transform:translateY(10px) scale(.985)}to{opacity:1;transform:none}}
.desk .dk:hover{border-color:#f1d6e5}
.desk .grp{transition:opacity .3s}
.desk .grab{transition:background .15s,color .15s,transform .15s,box-shadow .15s}
.desk .grab:hover{background:#e60f86}
.desk .grab:active{transform:scale(.97)}
.desk .dk details[open] > .grab:hover{background:#fff5fa}
.desk #deskcount{transition:opacity .2s}
.desk .find kbd{font-family:'JetBrains Mono',monospace;font-size:11px;color:#8a8190;border:1px solid #e5dbe1;border-radius:6px;padding:1px 6px;background:#fff}
@media(max-width:760px){.desk .find kbd{display:none}}
::highlight(deskq){background-color:#FFE3F1;color:#141216}
/* ---- reading view ---- */
.rdr{position:fixed;inset:0;z-index:200;display:grid;place-items:center;padding:24px}
.rdr[hidden]{display:none}
.rdr-bg{position:absolute;inset:0;background:rgba(20,18,22,.42);opacity:0;transition:opacity .28s}
.rdr.on .rdr-bg{opacity:1}
.rdr-p{position:relative;width:min(720px,100%);max-height:min(86vh,900px);overflow:auto;overscroll-behavior:contain;background:#fff;border:1.5px solid #f1d6e5;border-radius:26px;box-shadow:0 1px 0 #eadfe6,0 40px 90px -30px rgba(20,18,22,.5);padding:0 34px 26px;font-family:'DM Sans',system-ui,sans-serif;color:#141216;line-height:1.6;opacity:0;transform:translateY(18px) scale(.98);transition:opacity .28s cubic-bezier(.2,.7,.2,1),transform .34s cubic-bezier(.2,.7,.2,1)}
.rdr.on .rdr-p{opacity:1;transform:none}
.rdr-p.gold{background:linear-gradient(170deg,#fff9e3,#fff 340px);border-color:#efd98a}
.rdr-bar{position:sticky;top:0;z-index:2;display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 -34px;padding:16px 20px 12px 34px;background:inherit;background:rgba(255,255,255,.96);border-bottom:1px solid transparent;transition:border-color .2s}
.rdr-p.gold .rdr-bar{background:rgba(255,251,236,.97)}
.rdr-p.scrolled .rdr-bar{border-bottom-color:#f1eaee}
.rdr-grip{display:none}
.rdr-meta{display:flex;align-items:center;gap:8px;min-width:0;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:#8a8190;white-space:nowrap;overflow:hidden}
.rdr-meta .ic{width:28px;height:28px;border-radius:8px;background:#fbf3f7;display:grid;place-items:center;flex:none}
.rdr-p.gold .rdr-meta .ic{background:#fff3c4}
.rdr-meta .ic svg{width:19px;height:19px}
.rdr-meta .kind{color:#e60f86;font-weight:600;letter-spacing:.12em}
.rdr-p.gold .rdr-meta .kind{color:#9a7400}
.rdr-meta .src{margin:0;padding:0;border:0;font:inherit;color:inherit;overflow:hidden;text-overflow:ellipsis;min-width:0;text-transform:none;letter-spacing:.02em}
.rdr-meta .time{background:#f4eff3;border-radius:99px;padding:4px 9px;flex:none}
.rdr-meta .chip.ex{font-family:'DM Sans',sans-serif;font-size:10px;font-weight:600;letter-spacing:0;text-transform:none;padding:1px 6px;border-radius:7px;background:#fff1c9;color:#6d5300;flex:none}
.rdr-x{flex:none;width:40px;height:40px;border-radius:50%;border:1.5px solid #e5dbe1;background:#fff;color:#141216;font:400 22px/1 'DM Sans',sans-serif;cursor:pointer;display:grid;place-items:center;transition:border-color .15s}
.rdr-x:hover{border-color:#FA1896}
.rdr-p h2{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:32px;line-height:1.05;letter-spacing:-.01em;margin:10px 0 10px;text-wrap:balance}
.rdr-love{margin:0 0 6px;line-height:1.55;color:#3a343d;text-wrap:pretty}
.rdr-p .inside{margin-top:16px;font-size:15px;line-height:1.55}
.rdr-p .inside [hidden]{display:revert}
.rdr-p .inside ol{padding-left:20px;margin:0;list-style:decimal}
.rdr-p .inside li{margin:0 0 10px;text-wrap:pretty}
.rdr-p .inside table{border-collapse:collapse;width:100%}
.rdr-p .inside td,.rdr-p .inside th{text-align:left;padding:7px 4px;border-bottom:1px solid #eee;font-size:14px;vertical-align:top}
.rdr-p .inside td:first-child{white-space:nowrap;padding-right:10px}
.rdr-p .inside td .vn{display:block;font-size:11.5px;color:#8a8190;margin-top:1px;line-height:1.35}
.rdr-p .inside blockquote{margin:8px 0;padding:12px 16px;border-left:4px solid #FA1896;background:#fff5fa;border-radius:0 12px 12px 0;font-style:italic}
.rdr-p .inside ul.dates,.rdr-p .inside ul.mythlist,.rdr-p .inside ul.terms{list-style:none;padding:0;margin:0}
.rdr-p .inside ul.dates li{display:grid;grid-template-columns:110px 1fr;gap:10px;padding:8px 0;margin:0;border-bottom:1px solid #f1eaee}
.rdr-p .inside ul.dates .date{font-family:'JetBrains Mono',monospace;font-size:11.5px;font-weight:600;color:#141216;padding-top:3px}
.rdr-p .inside ul.mythlist li,.rdr-p .inside ul.terms li{padding:8px 0;margin:0;border-bottom:1px solid #f1eaee}
.rdr-p .inside .myth{font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:#8a8190;margin-right:4px}
.rdr-p .inside .fact{display:block;margin-top:4px}
.rdr-p .inside .fact b{color:#145c35}
.rdr-p .inside .why{color:#4a4450}
.rdr .chip{display:inline;border:0;line-height:inherit;font-family:inherit;cursor:auto;color:inherit}
.rdr-p .inside .chip{font-size:10.5px;font-weight:600;border-radius:7px;padding:1px 6px;margin-left:2px;background:#f3eef2;white-space:nowrap}
.rdr-p .inside .chip.a{background:#e3f5ea;color:#145c35;text-decoration:none}
.rdr-p .inside .chip.ex{background:#fff1c9;color:#6d5300}
.rdr-p .inside a.chip:hover{text-decoration:underline}
.rdr-p .inside .fine{font-size:12.5px;color:#6b6470;margin:14px 0 0}
.rdr-p .inside .fine a{color:#b30a68}
.rdr-p .inside .fine .disc{display:block;margin-top:5px;color:#8a8190}
.rdr-p .inside .copylink{display:none}
.rdr-foot{position:sticky;bottom:-26px;display:flex;align-items:center;justify-content:space-between;gap:10px;margin:22px -34px -26px;padding:14px 34px 18px;background:rgba(255,255,255,.97);border-top:1px solid #f1eaee}
.rdr-p.gold .rdr-foot{background:rgba(255,251,236,.97)}
.rdr-foot button{font:600 14px/1 'DM Sans',sans-serif;border-radius:99px;padding:11px 16px;cursor:pointer;white-space:nowrap;transition:border-color .15s,background .15s}
.rdr-nav{border:1.5px solid #e5dbe1;background:#fff;color:#141216}
.rdr-nav:hover:not(:disabled){border-color:#FA1896}
.rdr-nav:disabled{opacity:.35;cursor:default}
.rdr-copy{border:0;background:#FA1896;color:#fff;font-weight:700!important}
.rdr-copy:hover{background:#e60f86}
.rdr-pos{font-family:'JetBrains Mono',monospace;font-size:11px;color:#8a8190;letter-spacing:.06em}
html.rdr-lock,html.rdr-lock body{overflow:hidden}
@media(max-width:640px){
 .rdr{padding:0;place-items:end stretch}
 .rdr-p{width:100%;max-height:90vh;max-height:90dvh;border-radius:22px 22px 0 0;border-bottom:0;padding:0 18px 18px;transform:translateY(100%)}
 .rdr.on .rdr-p{transform:translateY(var(--drag,0px))}
 .rdr-p.dragging{transition:none}
 .rdr-bar{margin:0 -18px;padding:22px 14px 10px 18px;touch-action:none}
 .rdr-grip{display:block;position:absolute;left:50%;top:8px;width:40px;height:4px;margin-left:-20px;border-radius:4px;background:#e5dbe1}
 .rdr-p h2{font-size:26px}
 .rdr-p .inside ul.dates li{grid-template-columns:1fr;gap:1px}
 .rdr-foot{bottom:-18px;margin:18px -18px -18px;padding:12px 18px calc(14px + env(safe-area-inset-bottom))}
 .rdr-foot button{padding:11px 13px}
 .rdr-pos{display:none}
}
/* ---- sticky mobile picker ---- */
.mpick{position:fixed;left:0;right:0;top:var(--navh,60px);z-index:40;background:rgba(250,246,238,.97);border-bottom:1px solid #ece4e9;box-shadow:0 10px 24px -20px rgba(20,18,22,.45);transform:translateY(-110%);opacity:0;visibility:hidden;transition:transform .3s cubic-bezier(.2,.7,.2,1),opacity .2s,visibility 0s .3s}
.mpick.on{transform:none;opacity:1;visibility:visible;transition:transform .3s cubic-bezier(.2,.7,.2,1),opacity .2s}
.mp-row{display:flex;align-items:center;gap:8px;overflow-x:auto;scrollbar-width:none;padding:9px 18px}
.mp-row::-webkit-scrollbar{display:none}
.mp-row select{flex:none;-webkit-appearance:none;appearance:none;font:600 14px/1.2 'DM Sans',sans-serif;color:#141216;padding:8px 28px 8px 13px;border-radius:99px;border:1.5px solid #e5dbe1;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' fill='none' stroke='%23b30a68' stroke-width='2'/%3E%3C/svg%3E") right 11px center/10px no-repeat;max-width:62vw}
.mp-row select.set{background-color:#FFE3F1;border-color:#FA1896}
.mp-q{flex:none;width:38px;height:38px;border-radius:50%;border:1.5px solid #e5dbe1;background:#fff;display:grid;place-items:center;cursor:pointer;color:#b30a68}
.mp-q.set{background:#FFE3F1;border-color:#FA1896}
.mp-s{display:none;padding:0 18px 10px}
.mpick.sq .mp-s{display:flex;align-items:center;gap:10px}
.mp-s input{flex:1;min-width:0;font:400 15px/1.2 'DM Sans',sans-serif;color:#141216;padding:9px 14px;border-radius:99px;border:1.5px solid #e5dbe1;background:#fff}
.mp-s input:focus{outline:none;border-color:#FA1896;box-shadow:0 0 0 3px rgba(250,24,150,.14)}
.mp-n{font-family:'JetBrains Mono',monospace;font-size:11px;color:#6b6470;white-space:nowrap}
@media(min-width:761px){.mpick{display:none}}
@media(prefers-reduced-motion:reduce){
 .desk.js h1 em{animation:none;background-size:100% .16em}
 .desk.js .dhero .sign,.desk.js .endnote .sign,.desk.js .endnote:not(.vis) .sign{animation:none;clip-path:none}
 .desk.js .dhero>*{animation:none}
 .desk.js .dk,.desk.js .dk:not(.vis){opacity:1;transform:none;transition:none}
 .desk.js .dk.pop{animation:none}
 .rdr-bg,.rdr-p,.mpick,.mpick.on{transition:none}
}
'''

# ---- 4. v4 wow layer: JS ---------------------------------------------------------------------------
WOW_JS = r'''<script id="desk-v4">(function(){
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var desk=document.querySelector('.desk'),grid=document.getElementById('desk-grid');if(!desk||!grid)return;
desk.classList.add('js');
var cards=[].slice.call(grid.querySelectorAll('.dk'));
var IO='IntersectionObserver' in window;
/* 1. cards rise in as they enter the viewport */
if(IO&&!RM){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('vis');io.unobserve(e.target);}});},{rootMargin:'0px 0px -6% 0px'});cards.forEach(function(c){io.observe(c);});}
else cards.forEach(function(c){c.classList.add('vis');});
var en=desk.querySelector('.endnote');
if(en){if(IO&&!RM){var eo=new IntersectionObserver(function(es){if(es[0].isIntersecting){en.classList.add('vis');eo.disconnect();}},{threshold:.4});eo.observe(en);}else en.classList.add('vis');}
/* 2. live filter motion: cards that (re)appear after a filter or search change pop in, lightly staggered */
var was=new Map();cards.forEach(function(c){was.set(c,!c.hidden);});
var batch=0,raf=0;
function settle(){raf=0;batch=0;var k=0;
 cards.forEach(function(c){var now=!c.hidden;if(now&&!was.get(c)&&!RM){c.classList.remove('pop');void c.offsetWidth;c.style.setProperty('--d',Math.min(k++*28,280)+'ms');c.classList.add('vis','pop');}was.set(c,now);});
 syncPick();paintHL();}
new MutationObserver(function(){if(!raf)raf=requestAnimationFrame(settle);}).observe(grid,{subtree:true,attributes:true,attributeFilter:['hidden','style','open']});
grid.addEventListener('animationend',function(e){if(e.target.classList.contains('pop'))e.target.classList.remove('pop');});
/* 3. search highlight (CSS Custom Highlight API; silently skipped where unsupported) */
var q=document.getElementById('deskq');
function paintHL(){if(!(window.CSS&&CSS.highlights&&window.Highlight))return;CSS.highlights.delete('deskq');
 var t=(q&&q.value||'').trim().toLowerCase();if(t.length<2)return;var rs=[];
 cards.forEach(function(c){if(c.hidden)return;var w=document.createTreeWalker(c,NodeFilter.SHOW_TEXT),n;
  while((n=w.nextNode())){var p=n.parentNode;if(p.closest('[hidden]')||p.closest('summary'))continue;var s=n.nodeValue.toLowerCase(),i=s.indexOf(t);
   while(i>-1&&rs.length<1500){var r=new Range();r.setStart(n,i);r.setEnd(n,i+t.length);rs.push(r);i=s.indexOf(t,i+t.length);}}});
 if(rs.length)CSS.highlights.set('deskq',new Highlight(...rs));}
if(q){q.addEventListener('input',function(){setTimeout(paintHL,160);});
 addEventListener('keydown',function(e){if(e.key==='/'&&!/INPUT|SELECT|TEXTAREA/.test((document.activeElement||{}).tagName||'')&&!rdr.classList.contains('on')){e.preventDefault();q.focus();q.scrollIntoView({block:'center',behavior:RM?'auto':'smooth'});}});}
/* 4. count-up on the desk line */
var nums=[].slice.call(desk.querySelectorAll('.deskline b'));
function countUp(b){var tx=b.textContent,v=parseInt(tx.replace(/[^0-9]/g,''),10);if(!v||RM)return;var t0=null,D=1100;
 function f(ts){if(!t0)t0=ts;var p=Math.min(1,(ts-t0)/D),e=1-Math.pow(1-p,3);b.textContent=String(Math.round(v*e));if(p<1)requestAnimationFrame(f);else b.textContent=tx;}requestAnimationFrame(f);}
if(nums.length&&IO&&!RM){nums.forEach(function(b){b.style.display='inline-block';b.style.minWidth=b.offsetWidth+'px';});
 var no=new IntersectionObserver(function(es){if(es[0].isIntersecting){nums.forEach(countUp);no.disconnect();}},{threshold:.6});no.observe(nums[0].parentNode.parentNode);}
/* 5. reading view */
var rdr=document.createElement('div');rdr.className='rdr';rdr.hidden=true;rdr.setAttribute('role','dialog');rdr.setAttribute('aria-modal','true');rdr.setAttribute('aria-labelledby','rdr-h');
rdr.innerHTML='<div class="rdr-bg" data-x></div><article class="rdr-p" tabindex="-1"><div class="rdr-bar"><span class="rdr-grip" aria-hidden="true"></span><div class="rdr-meta"></div><button type="button" class="rdr-x" data-x aria-label="Close">&times;</button></div><h2 id="rdr-h"></h2><p class="rdr-love"></p><div class="inside"></div><div class="rdr-foot"><button type="button" class="rdr-nav" data-go="-1" aria-label="Previous card">&larr; Prev</button><span class="rdr-pos"></span><button type="button" class="rdr-copy">Copy link</button><button type="button" class="rdr-nav" data-go="1" aria-label="Next card">Next &rarr;</button></div></article>';
document.body.appendChild(rdr);
var P=rdr.querySelector('.rdr-p'),cur=null,back=null,prevHash='';
function visible(){return cards.filter(function(c){return !c.hidden;}).sort(function(a,b){return (+a.style.order||0)-(+b.style.order||0);});}
function fill(c){cur=c;var m=c.querySelector('.dk-meta');rdr.querySelector('.rdr-meta').innerHTML=m?m.innerHTML:'';
 rdr.querySelector('#rdr-h').textContent=c.querySelector('h3').textContent;
 var lv=c.querySelector('.love');rdr.querySelector('.rdr-love').textContent=lv?lv.textContent:'';
 var ins=c.querySelector('.inside'),box=rdr.querySelector('.inside');box.innerHTML=ins?ins.innerHTML:'';
 [].forEach.call(box.querySelectorAll('[hidden]'),function(x){x.hidden=false;});
 [].forEach.call(box.querySelectorAll('[id]'),function(x){x.removeAttribute('id');});
 P.classList.toggle('gold',c.classList.contains('gold'));P.scrollTop=0;P.classList.remove('scrolled');
 var v=visible(),i=v.indexOf(c);rdr.querySelector('[data-go="-1"]').disabled=i<=0;rdr.querySelector('[data-go="1"]').disabled=i<0||i>=v.length-1;
 rdr.querySelector('.rdr-pos').textContent=i>-1?(i+1)+' / '+v.length:'';
 rdr.querySelector('.rdr-copy').textContent='Copy link';
 try{history.replaceState(null,'','#'+c.id);}catch(e){}}
function open(c,from){if(!c)return;if(rdr.hidden){prevHash=location.hash;back=from||document.activeElement;}fill(c);
 if(rdr.hidden){rdr.hidden=false;document.documentElement.classList.add('rdr-lock');void P.offsetWidth;rdr.classList.add('on');}
 P.focus({preventScroll:true});}
function close(){if(rdr.hidden)return;rdr.classList.remove('on');document.documentElement.classList.remove('rdr-lock');P.style.removeProperty('--drag');
 var done=function(){rdr.hidden=true;};RM?done():setTimeout(done,300);
 try{history.replaceState(null,'',prevHash&&prevHash!=='#'+(cur&&cur.id)?prevHash:location.pathname+location.search);}catch(e){}
 if(cur&&!cur.hidden){var r=cur.getBoundingClientRect();if(r.top<70||r.bottom>innerHeight)cur.scrollIntoView({block:'center'});}
 if(back&&back.focus)back.focus({preventScroll:true});}
window.foReader=function(c){open(c,c.querySelector('summary'));};
grid.addEventListener('click',function(e){var s=e.target.closest('summary.grab');if(!s||!grid.contains(s))return;e.preventDefault();open(s.closest('.dk'),s);});
rdr.addEventListener('click',function(e){if(e.target.closest('[data-x]')){close();return;}
 var g=e.target.closest('[data-go]');if(g&&!g.disabled){var v=visible(),i=v.indexOf(cur)+(+g.getAttribute('data-go'));if(v[i])fill(v[i]);return;}
 if(e.target.closest('.rdr-copy')){var b=e.target.closest('.rdr-copy'),u=location.href.split('#')[0]+'#'+cur.id;
  var ok=function(){b.textContent='Link copied';setTimeout(function(){b.textContent='Copy link';},1800);};
  if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(ok,function(){prompt('Copy this link',u);});else prompt('Copy this link',u);}});
P.addEventListener('scroll',function(){P.classList.toggle('scrolled',P.scrollTop>4);},{passive:true});
document.addEventListener('keydown',function(e){if(rdr.hidden)return;
 if(e.key==='Escape'){e.preventDefault();close();}
 else if((e.key==='ArrowRight'||e.key==='ArrowLeft')&&!/INPUT|TEXTAREA/.test(e.target.tagName)){var v=visible(),i=v.indexOf(cur)+(e.key==='ArrowRight'?1:-1);if(v[i]){e.preventDefault();fill(v[i]);}}
 else if(e.key==='Tab'){var f=[].slice.call(P.querySelectorAll('a[href],button:not(:disabled)'));if(!f.length)return;var a=f[0],z=f[f.length-1];
  if(e.shiftKey&&(document.activeElement===a||document.activeElement===P)){e.preventDefault();z.focus();}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus();}}});
/* swipe the sheet down to close (phones) */
var bar=rdr.querySelector('.rdr-bar'),y0=null,dy=0;
bar.addEventListener('touchstart',function(e){if(innerWidth>640)return;y0=e.touches[0].clientY;dy=0;P.classList.add('dragging');},{passive:true});
bar.addEventListener('touchmove',function(e){if(y0===null)return;dy=Math.max(0,e.touches[0].clientY-y0);P.style.setProperty('--drag',dy+'px');},{passive:true});
bar.addEventListener('touchend',function(){if(y0===null)return;P.classList.remove('dragging');y0=null;if(dy>90)close();else P.style.removeProperty('--drag');});
/* 6. sticky mobile picker: mirrors the sentence picker once it scrolls away */
var sels=['tradesel','stagesel','typesel'].map(function(id){return document.getElementById(id);}).filter(Boolean);
var mp=document.createElement('div');mp.className='mpick';mp.setAttribute('aria-label','Filter the desk');
var row=document.createElement('div');row.className='mp-row';
var qb=document.createElement('button');qb.type='button';qb.className='mp-q';qb.setAttribute('aria-label','Search the desk');
qb.innerHTML='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>';row.appendChild(qb);
var mirrors=sels.map(function(s){var m=document.createElement('select');m.innerHTML=s.innerHTML;m.value=s.value;m.setAttribute('aria-label',(s.labels&&s.labels[0]?s.labels[0].textContent:s.id));
 m.addEventListener('change',function(){s.value=m.value;s.dispatchEvent(new Event('change',{bubbles:true}));var top=grid.getBoundingClientRect().top+scrollY-(navh()+mp.offsetHeight+8);if(scrollY>top)scrollTo({top:top,behavior:RM?'auto':'smooth'});});row.appendChild(m);return m;});
var srow=document.createElement('div');srow.className='mp-s';srow.innerHTML='<input type="search" placeholder="Search the desk" aria-label="Search the desk"><span class="mp-n"></span>';
mp.appendChild(row);mp.appendChild(srow);document.body.appendChild(mp);
var mq=srow.querySelector('input'),mn=srow.querySelector('.mp-n'),out=document.getElementById('deskcount');
qb.addEventListener('click',function(){mp.classList.toggle('sq');if(mp.classList.contains('sq'))mq.focus();});
mq.addEventListener('input',function(){if(q){q.value=mq.value;q.dispatchEvent(new Event('input',{bubbles:true}));}});
function syncPick(){sels.forEach(function(s,i){var m=mirrors[i];if(m.value!==s.value)m.value=s.value;m.classList.toggle('set',s.value!=='all');});
 if(q&&mq.value!==q.value&&document.activeElement!==mq)mq.value=q.value;qb.classList.toggle('set',!!(q&&q.value));
 var n=visible().length;mn.textContent=(out&&out.textContent&&q&&q.value)?out.textContent.replace(/ matching lines? in /,' in '):n+(n===1?' card':' cards');}
function navh(){var n=document.querySelector('.nav');return n?Math.max(0,n.getBoundingClientRect().bottom):0;}
var fl=desk.querySelector('.filters'),above=false,inGrid=false;
function upd(){mp.style.setProperty('--navh',navh()+'px');var on=above&&inGrid;mp.classList.toggle('on',on);if(!on&&document.activeElement===mq)mq.blur();}
if(fl&&IO){new IntersectionObserver(function(es){var e=es[0];above=!e.isIntersecting&&e.boundingClientRect.top<0;upd();},{rootMargin:'-64px 0px 0px 0px'}).observe(fl);
 new IntersectionObserver(function(es){inGrid=es[0].isIntersecting;upd();},{rootMargin:'-120px 0px -30% 0px'}).observe(grid);}
addEventListener('resize',upd);
/* hint: "/" to search on desktop */
var fd=desk.querySelector('.find');if(fd&&q){var k=document.createElement('kbd');k.textContent='/';k.title='Press / to search';fd.insertBefore(k,q.nextSibling);}
syncPick();
})();</script>'''

# ---- 5. content edits (all reported) ------------------------------------------------------------------
body = CONTENT
# photo: same image, served from this branch instead of the old preview CDN branch
body = body.replace('https://cdn.jsdelivr.net/gh/UpNonStop/firstofficer-site@home-v2-preview/img/ind/desk.webp', 'img/ind/desk.webp')
body = body.replace('https://cdn.jsdelivr.net/gh/UpNonStop/firstofficer-site@home-v2-preview/img/ind/desk.jpg', 'img/ind/desk.jpg')
# links: point at the v4 mockup pages that exist
body = body.replace('href="connect.html"', 'href="book.html"')
body = body.replace('href="for-dental-v2.html"', 'href="for-dental.html"')

DESKJS = DESKJS.replace("setTimeout(function(){var d=el.querySelector('details');if(d)d.open=true;el.scrollIntoView({block:'start'});},80);",
                        "setTimeout(function(){el.scrollIntoView({block:'start'});if(window.foReader)window.foReader(el);else{var d=el.querySelector('details');if(d)d.open=true;}},80);")
assert 'foReader' in DESKJS

STYLE = '<style id="desk-css">' + RESETS + SCOPED + NONPINK + WOW_CSS + '</style>'
BODY = '<div class="desk" id="desk-top">' + body + '</div>'
TAIL = '<script id="deskjs">' + DESKJS + '</script>' + WOW_JS

page('free-from-the-desk.html', 'Free From the Desk · First Officer by UpNonStop',
     BODY, desc="Everything I'd tell you over coffee: 490 smart items for business owners, free. No email. No catch.",
     src='freebies', tail=TAIL, headx=STYLE)
