# -*- coding: utf-8 -*-
# Free From the Desk: three bold design directions (A editorial, B trading desk, C brand pop).
# Same content, wording and functionality as free-from-the-desk.html (filter, search, reader, sticky picker).
# Only presentation changes: fonts, scale, colour, layout, motion. Decorative strips reuse existing content
# (merchant codes and plain descriptions from the cheat sheets, source names from the card meta) and are aria-hidden.
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(__file__))
import freebies as F
from fosite import page, ROOT

BODY = F.BODY
G = BODY[BODY.index('id="desk-grid"'):BODY.index('class="endnote"')]

# merchant codes + the page's own plain description
seen, CODES = set(), []
for code, desc in re.findall(r'<td[^>]*>\s*<b>(\d{4})</b>\s*</td>\s*<td[^>]*>(.*?)</td>', G, re.S):
    d = re.sub(r'<span class="vn">.*?</span>', '', desc); d = re.sub(r'<[^>]+>', '', d).strip()
    if code in seen or not d or len(d) > 34: continue
    seen.add(code); CODES.append((code, d))
CODES = CODES[:44]
# source names from the card meta
SRC = []
for s in re.findall(r'<span class="src">([^<]*)</span>', G):
    s = H.unescape(s).replace('Source:', '').replace('Coding:', '').replace(' and more', '')
    for n in re.split(r',\s*', s):
        n = n.strip()
        if n and n.lower() not in [x.lower() for x in SRC] and n not in ('Issuer pages', 'settlement site', 'Issuer'): SRC.append(n)

def strip(items, cls):
    one = ''.join(items)
    return f'<div class="mq {cls}" aria-hidden="true"><div class="mq-t">{one}{one}</div></div>'

CODE_ITEMS = [f'<span class="mq-i"><b>{c}</b>{H.escape(d)}</span>' for c, d in CODES]
SRC_ITEMS = [f'<span class="mq-i">{H.escape(n)}</span>' for n in SRC]

def fonts(q):
    return ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{q}&display=swap">')

# ---------------------------------------------------------------- shared direction CSS/JS
SHARED = r'''
html[class*=dir-] main{overflow-x:clip}
.desk .mq{overflow:hidden;position:relative}
.desk .mq-t{display:flex;width:max-content;animation:dxMq var(--mqs,90s) linear infinite}
.desk .mq:hover .mq-t{animation-play-state:paused}
.desk .mq-i{display:inline-flex;align-items:baseline;gap:8px;white-space:nowrap}
@keyframes dxMq{to{transform:translateX(-50%)}}
.desk .bleed{box-shadow:0 0 0 100vmax var(--bb);clip-path:inset(0 -100vmax);background:var(--bb)}
.desk h1,.desk .grp h2,.desk .dk h3,.desk .feat h2{text-wrap:balance}
.desk .lede,.desk .love,.desk .grp-disc,.desk .endnote p{text-wrap:pretty}
.desk.js .dk.vis{transition-delay:var(--d,0ms)}
.desk .dk{transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s,opacity .5s,border-color .2s}
@media(hover:hover){.desk .dk:hover{transform:translateY(-4px)}}
@media(prefers-reduced-motion:reduce){
 .desk .mq-t{animation:none}.desk .mq{overflow-x:auto}
 .desk .dk:hover{transform:none}
 .desk *{transition-delay:0s!important}
}
'''
SHARED_JS = r'''<script id="dir-js">(function(){
var grid=document.getElementById('desk-grid');if(!grid)return;
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
/* stagger the reveal: each card waits a beat after its neighbour */
[].forEach.call(grid.querySelectorAll('.dk'),function(c,i){c.style.setProperty('--d',RM?'0ms':((i%4)*80)+'ms');});
setTimeout(function(){[].forEach.call(grid.querySelectorAll('.dk'),function(c){c.style.removeProperty('--d');});},4000);
/* category hook for colour coding */
[].forEach.call(grid.querySelectorAll('.dk'),function(c){c.setAttribute('data-cat',c.getAttribute('data-ty'));});
/* mark the lead (first visible) card of every group, re-run whenever the filter changes */
var heads=[].slice.call(grid.querySelectorAll('.grp'));
function lead(){heads.forEach(function(h){var g=h.getAttribute('data-grp'),best=null,bo=1e9;
 [].forEach.call(grid.querySelectorAll('.dk[data-ty="'+g+'"]'),function(c){c.classList.remove('lead');if(!c.hidden){var o=+c.style.order||0;if(o<bo){bo=o;best=c;}}});
 if(best)best.classList.add('lead');});}
var t;new MutationObserver(function(){cancelAnimationFrame(t);t=requestAnimationFrame(lead);}).observe(grid,{subtree:true,attributes:true,attributeFilter:['hidden','style']});
lead();
})();</script>'''

def head(cls, fq, css, extra=''):
    return (fonts(fq) + f'<script>document.documentElement.classList.add("{cls}");{extra}</script>'
            + F.STYLE + '<style id="dir-css">' + SHARED + css + '</style>')

# ======================================================================= A · EDITORIAL MAGAZINE
A_CSS = r'''
html.dir-a{--pa:#F5EFE3;--ink:#121014;--rule:#121014}
html.dir-a body{background:var(--pa)}
html.dir-a .desk{--serifA:'Fraunces',Georgia,serif;--grot:'Archivo',system-ui,sans-serif;font-family:var(--grot);max-width:1240px;padding-top:22px}
/* issue bar */
html.dir-a .issue{display:flex;justify-content:space-between;align-items:center;gap:14px;font:600 11px/1 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#121014;border-top:4px solid #121014;border-bottom:1px solid #121014;padding:10px 0;margin-bottom:6px}
html.dir-a .issue span:nth-child(2){color:#5a5260}
html.dir-a .issue+.rule2{height:5px;border-bottom:1px solid #121014;margin-bottom:26px}
/* hero */
html.dir-a .desk .dhero{grid-template-columns:1.55fr 1fr;gap:56px;align-items:start;padding:8px 0 34px;border-bottom:1px solid #121014}
html.dir-a .desk .eyebrow{font:700 12px/1 'JetBrains Mono',monospace;letter-spacing:.18em;text-transform:uppercase;color:#B30A68;margin-bottom:18px;display:flex;align-items:center;gap:12px}
html.dir-a .desk .eyebrow::after{content:"";flex:1;height:1px;background:#121014}
html.dir-a .desk h1{font-family:var(--serifA);font-weight:800;font-size:104px;line-height:.9;letter-spacing:-.035em;font-variation-settings:"opsz" 144;margin:0 0 26px;color:#121014}
html.dir-a .desk h1 em{font-weight:400;font-style:italic;color:#FA1896;letter-spacing:-.02em}
html.dir-a .desk .lede{font-family:var(--grot);font-size:19px;line-height:1.55;color:#2b262e;column-count:2;column-gap:30px;column-rule:1px solid #12101433;max-width:none}
html.dir-a .desk .lede::first-letter{font-family:var(--serifA);font-weight:800;float:left;font-size:74px;line-height:.82;padding:6px 10px 0 0;color:#121014}
html.dir-a .desk .lede .hl{background:#121014;color:#fff;padding:1px 6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
html.dir-a .desk .sig{border-top:1px solid #121014;padding-top:16px}
html.dir-a .desk .feat{transform:none;border:0;border-top:6px solid #FA1896;border-radius:0;background:#fff;box-shadow:12px 12px 0 #121014;padding:26px 26px 28px;position:relative}
html.dir-a .desk .feat:hover{transform:translate(-3px,-3px);box-shadow:15px 15px 0 #121014}
html.dir-a .desk .feat .ft-k{font:700 11px/1 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:#B30A68}
html.dir-a .desk .feat h2{font-family:var(--serifA);font-weight:800;font-size:44px;line-height:.98;letter-spacing:-.02em}
html.dir-a .desk .feat .btnp{background:#121014;color:#fff;border-radius:0;font-family:var(--grot);font-weight:800;letter-spacing:.02em}
html.dir-a .desk .feat:hover .btnp{background:#FA1896}
/* photo as a wide plate */
html.dir-a .desk .deskphoto{margin:30px 0 0;border:0;border-radius:0;padding:0;background:none;box-shadow:none;transform:none;position:relative}
html.dir-a .desk .deskphoto img{width:100%;height:380px;object-fit:cover;border-radius:0;filter:contrast(1.05) saturate(.9)}
html.dir-a .desk .deskphoto figcaption{display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid #121014;padding:8px 0;font:500 12px/1.4 var(--grot);color:#5a5260}
html.dir-a .desk .deskphoto figcaption span:first-child{font-family:var(--serifA);font-style:italic;font-size:17px;color:#121014}
/* big numbered figures */
html.dir-a .desk .deskline{display:grid;grid-template-columns:repeat(4,1fr) auto;gap:0;margin:0;border-bottom:4px solid #121014;padding:0}
html.dir-a .desk .deskline span{display:flex;flex-direction:column;gap:6px;padding:22px 20px 18px;border-right:1px solid #121014;font:700 11px/1.3 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#5a5260}
html.dir-a .desk .deskline span:first-child{padding-left:0}
html.dir-a .desk .deskline b{font-family:var(--serifA);font-weight:800;font-size:76px;line-height:.85;letter-spacing:-.04em;color:#121014;font-variant-numeric:lining-nums tabular-nums}
html.dir-a .desk .deskline .ck{align-self:stretch;border-right:0;justify-content:flex-end;text-align:right}
/* merchant-code strip */
html.dir-a .desk .codes{--bb:#121014;color:#F5EFE3;padding:12px 0;margin:0;font:500 13px/1 var(--grot)}
html.dir-a .desk .codes .mq-i{padding:0 22px;border-right:1px solid #ffffff33}
html.dir-a .desk .codes b{font:700 13px/1 'JetBrains Mono',monospace;color:#FFD84D;letter-spacing:.06em}
html.dir-a .desk .readfirst{margin-top:22px;border-radius:0;border:0;border-left:4px solid #FA1896;background:#fff}
/* filters as a headline sentence */
html.dir-a .desk .filters{margin-top:34px;padding:0 0 22px;border-bottom:1px solid #121014}
html.dir-a .desk .madlib{font-family:var(--serifA);font-weight:700;font-size:44px;line-height:1.25;letter-spacing:-.02em;color:#121014}
html.dir-a .desk .madlib select{font-family:var(--serifA);font-style:italic;font-weight:500;font-size:44px;color:#B30A68;border-bottom:3px solid #FA1896}
html.dir-a .desk .find input{border-radius:0;border:2px solid #121014;background:#fff;font-family:var(--grot);font-size:16px}
/* the grid: 4 columns, open magazine cards with rules */
html.dir-a .desk .grid{grid-template-columns:repeat(4,minmax(0,1fr));gap:30px 28px;grid-auto-flow:row;margin-top:10px;counter-reset:grp}
html.dir-a .desk .grp{counter-increment:grp;display:grid;grid-template-columns:auto 1fr auto;align-items:end;column-gap:20px;border-top:6px double #121014;padding:18px 0 4px;margin-top:26px}
html.dir-a .desk .grp::before{content:counter(grp,decimal-leading-zero);grid-row:1/3;font-family:var(--serifA);font-weight:800;font-size:88px;line-height:.8;letter-spacing:-.05em;color:transparent;-webkit-text-stroke:1.5px #121014}
html.dir-a .desk .grp h2{text-align:left;font-family:var(--serifA);font-weight:800;font-size:54px;line-height:.95;letter-spacing:-.03em}
html.dir-a .desk .grp .grp-n{grid-column:3;grid-row:1;font:700 11px/1 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#121014;background:#FFD84D;padding:6px 8px;align-self:start}
html.dir-a .desk .grp-disc{grid-column:2/4;font-size:13px;color:#5a5260;margin:8px 0 0}
html.dir-a .desk .dk{background:transparent;border:0;border-top:3px solid #121014;border-radius:0;box-shadow:none;padding:14px 0 0;gap:8px}
html.dir-a .desk .dk.gold{background:transparent;border-color:#C99A00}
html.dir-a .desk .dk-meta .ic{display:none}
html.dir-a .desk .dk-meta .src{padding-left:0}
html.dir-a .desk .dk-meta .kind{color:#B30A68}
html.dir-a .desk .dk-meta .time{background:none;border:1px solid #121014;border-radius:0;padding:2px 6px;color:#121014}
html.dir-a .desk .dk h3{font-family:var(--serifA);font-weight:700;font-size:26px;line-height:1.02;letter-spacing:-.015em}
html.dir-a .desk .love{font-size:14.5px;line-height:1.5;color:#2b262e}
html.dir-a .desk .grab{border-radius:0;background:#121014!important;color:#fff;font-family:var(--grot);font-weight:800;letter-spacing:.02em}
html.dir-a .desk .grab:hover{background:#FA1896!important}
/* lead story: spans 2x2, pull-quote, big figure */
html.dir-a .desk .dk.lead{grid-column:span 2;grid-row:span 2;background:#fff;border-top:8px solid #121014;padding:22px 24px 24px;box-shadow:0 30px 60px -45px rgba(18,16,20,.6)}
html.dir-a .desk .dk.lead h3{font-size:46px;line-height:.96;letter-spacing:-.03em}
html.dir-a .desk .dk.lead .love{font-family:var(--serifA);font-style:italic;font-size:24px;line-height:1.3;color:#121014;border-left:4px solid #FA1896;padding-left:16px;margin:4px 0 6px}
html.dir-a .desk .dk.lead::after{content:attr(data-n);position:absolute;right:20px;bottom:6px;font-family:var(--serifA);font-weight:800;font-size:150px;line-height:.8;letter-spacing:-.06em;color:#121014;opacity:.08;pointer-events:none}
html.dir-a .desk .dk{position:relative}
html.dir-a .desk .more-tile{border-radius:0;border:2px solid #121014;background:#FFD84D;color:#121014;font:800 15px/1 var(--grot);letter-spacing:.02em;grid-column:span 2}
html.dir-a .desk .more-tile:hover{background:#121014;color:#fff}
html.dir-a .desk .endnote{--bb:#121014;color:#F5EFE3;padding:56px 0;margin-top:56px;border:0;border-radius:0;background:#121014}
html.dir-a .desk .endnote p{font-family:var(--serifA);font-size:34px;line-height:1.2;letter-spacing:-.015em;color:#F5EFE3;max-width:900px}
html.dir-a .desk .endnote a{color:#FF7BC0}
html.dir-a .desk .endnote .sign{color:#FFD84D}
html.dir-a .rdr-p{border-radius:0;border:0;border-top:8px solid #121014;font-family:'Archivo',system-ui,sans-serif}
html.dir-a .rdr-p h2{font-family:'Fraunces',Georgia,serif!important;font-weight:800!important;letter-spacing:-.02em}
html.dir-a .mpick{background:#F5EFE3;border-bottom:2px solid #121014}
html.dir-a .mp-f,html.dir-a .mp-q,html.dir-a .mp-sheet select,html.dir-a .mp-s input{border-radius:0;border-color:#121014}
@media(max-width:1100px){
 html.dir-a .desk h1{font-size:80px}
 html.dir-a .desk .grid{grid-template-columns:repeat(3,minmax(0,1fr))}
 html.dir-a .desk .dk.lead{grid-row:auto}
}
@media(max-width:860px){
 html.dir-a .desk .dhero{grid-template-columns:1fr;gap:30px}
 html.dir-a .desk .grid{grid-template-columns:repeat(2,minmax(0,1fr))}
 html.dir-a .desk .deskline{grid-template-columns:repeat(2,1fr)}
 html.dir-a .desk .deskline span{border-bottom:1px solid #121014}
 html.dir-a .desk .deskline span:nth-child(2n){border-right:0}
 html.dir-a .desk .deskline span:first-child,html.dir-a .desk .deskline span:nth-child(3){padding-left:0}
 html.dir-a .desk .deskline .ck{align-self:stretch;grid-column:1/-1;text-align:left;justify-content:flex-start;padding-left:0}
}
@media(max-width:640px){
 html.dir-a .desk{padding-top:14px}
 html.dir-a .issue{font-size:9.5px;letter-spacing:.1em;flex-wrap:wrap}
 html.dir-a .issue span:nth-child(2){display:none}
 html.dir-a .desk h1{font-size:56px;line-height:.92}
 html.dir-a .desk .lede{column-count:1;font-size:17px}
 html.dir-a .desk .lede::first-letter{font-size:60px}
 html.dir-a .desk .feat{box-shadow:8px 8px 0 #121014;padding:22px}
 html.dir-a .desk .feat h2{font-size:36px}
 html.dir-a .desk .deskphoto img{height:220px}
 html.dir-a .desk .deskphoto figcaption{flex-direction:column;gap:2px}
 html.dir-a .desk .deskline b{font-size:58px}
 html.dir-a .desk .deskline span{padding:16px 12px 14px}
 html.dir-a .desk .madlib,html.dir-a .desk .madlib select{font-size:30px}
 html.dir-a .desk .grid{grid-template-columns:minmax(0,1fr);gap:22px}
 html.dir-a .desk .grp{grid-template-columns:auto 1fr;column-gap:14px}
 html.dir-a .desk .grp::before{font-size:60px}
 html.dir-a .desk .grp h2{font-size:36px}
 html.dir-a .desk .grp .grp-n{grid-column:2;grid-row:2;justify-self:start;margin-top:8px}
 html.dir-a .desk .grp-disc{grid-column:1/-1}
 html.dir-a .desk .dk.lead,html.dir-a .desk .more-tile{grid-column:auto;grid-row:auto}
 html.dir-a .desk .dk.lead{padding:18px 18px 20px}
 html.dir-a .desk .dk.lead h3{font-size:34px}
 html.dir-a .desk .dk.lead .love{font-size:20px}
 html.dir-a .desk .dk h3{font-size:24px}
 html.dir-a .desk .endnote p{font-size:25px}
}
'''
ISSUE = ('<div class="issue"><span>First Officer &middot; Free From the Desk</span>'
         '<span>490 smart items &middot; 20 trades &middot; 121 merchant codes decoded</span>'
         '<span>Checked October 12, 2026</span></div><div class="rule2"></div>')

def dir_a():
    b = BODY.replace('<section class="dhero">', ISSUE + '<section class="dhero">', 1)
    b = b.replace('<details class="readfirst">', strip(CODE_ITEMS, 'codes bleed') + '<details class="readfirst">', 1)
    b = b.replace('<section class="endnote">', '<section class="endnote bleed">', 1)
    return b

# ======================================================================= B · TRADING DESK / TERMINAL-LUXE
B_CSS = r'''
html.dir-b{--ink0:#0C0B10;--ink1:#16141C;--ink2:#221F2A;--ln:#2E2B37;--earn:#12834E;--burn:#E8590C;--ret:#7149C9;--learn:#1E78B8}
html.dir-b body{background:#F3F0EA}
html.dir-b .desk{font-family:'Geist',system-ui,sans-serif;max-width:1280px;padding-top:0;--mono:'Geist Mono','JetBrains Mono',monospace}
html.dir-b .desk .top{--bb:#0C0B10;color:#ECE8F2;padding:34px 0 0;position:relative}
html.dir-b .desk .top::before{content:"";position:absolute;inset:0 -100vmax;background:radial-gradient(700px 360px at 78% 18%,rgba(250,24,150,.22),transparent 70%),radial-gradient(600px 300px at 10% 90%,rgba(30,120,184,.18),transparent 70%),repeating-linear-gradient(90deg,transparent 0 79px,rgba(255,255,255,.035) 79px 80px),repeating-linear-gradient(0deg,transparent 0 79px,rgba(255,255,255,.035) 79px 80px);pointer-events:none}
html.dir-b .desk .top>*{position:relative}
html.dir-b .desk .dhero{grid-template-columns:1.35fr 1fr;gap:56px;padding:6px 0 34px}
html.dir-b .desk .eyebrow{display:inline-flex;align-items:center;gap:10px;font:600 12px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#7CE0A8;border:1px solid #2E2B37;background:#16141C;border-radius:99px;padding:8px 12px;margin-bottom:22px}
html.dir-b .desk .eyebrow::before{content:"";width:8px;height:8px;border-radius:50%;background:#2BD37F;box-shadow:0 0 0 4px rgba(43,211,127,.18);animation:dxBlink 2.4s ease-in-out infinite}
@keyframes dxBlink{50%{opacity:.35}}
html.dir-b .desk h1{font-family:'Geist',system-ui,sans-serif;font-weight:700;font-size:88px;line-height:.93;letter-spacing:-.05em;color:#fff;margin:0 0 24px}
html.dir-b .desk h1 em{font-style:normal;color:#FA1896;background:none}
html.dir-b .desk .lede{color:#B8B2C4;font-size:18.5px;line-height:1.6;max-width:600px}
html.dir-b .desk .lede .hl{background:#FA1896;color:#fff;padding:1px 6px;border-radius:4px}
html.dir-b .desk .sig .av{background:#FA1896;color:#fff}
html.dir-b .desk .sign{color:#fff}
html.dir-b .desk .sig .role{color:#8E879B}
html.dir-b .desk .feat{transform:none;background:linear-gradient(180deg,#1B1922,#121017);border:1px solid #2E2B37;border-radius:20px;color:#ECE8F2;box-shadow:0 40px 80px -40px rgba(250,24,150,.45),inset 0 1px 0 rgba(255,255,255,.06)}
html.dir-b .desk .feat:hover{transform:translateY(-4px);border-color:#FA1896}
html.dir-b .desk .feat .ft-k{background:#0F2A1D;padding:6px 10px;font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#7CE0A8}
html.dir-b .desk .feat h2{font-family:'Geist',sans-serif;font-weight:700;font-size:36px;letter-spacing:-.035em;color:#fff}
html.dir-b .desk .feat p{color:#B8B2C4}
html.dir-b .desk .feat .ic.big{background:#221F2A}
html.dir-b .desk .feat .time{color:#8E879B}
html.dir-b .desk .feat .btnp{border-radius:12px}
html.dir-b .desk .deskphoto{margin:0;border:1px solid #2E2B37;background:#16141C;border-radius:20px;box-shadow:none;transform:none;display:grid;grid-template-columns:1.4fr 1fr;overflow:hidden;padding:0}
html.dir-b .desk .deskphoto img{height:100%;min-height:230px;max-height:300px;width:100%;object-fit:cover;border-radius:0}
html.dir-b .desk .deskphoto figcaption{display:flex;flex-direction:column;justify-content:space-between;padding:22px;color:#8E879B;font:500 12px/1.4 var(--mono)}
html.dir-b .desk .deskphoto figcaption span:first-child{font-family:'Geist',sans-serif;font-weight:600;font-size:28px;line-height:1.1;letter-spacing:-.03em;color:#fff}
html.dir-b .desk .deskphoto figcaption a{color:#B8B2C4}
html.dir-b .desk .deskline{display:grid;grid-template-columns:repeat(4,1fr) 1.1fr;gap:10px;margin:14px 0 0;padding:0}
html.dir-b .desk .deskline span{display:flex;flex-direction:column;gap:8px;background:#16141C;border:1px solid #2E2B37;border-radius:14px;padding:16px 16px 14px;font:500 11px/1.3 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:#8E879B;position:relative;overflow:hidden}
html.dir-b .desk .deskline span::after{content:"";position:absolute;left:0;right:0;bottom:0;height:3px;background:var(--c,#2BD37F)}
html.dir-b .desk .deskline span:nth-child(1){--c:#12834E}html.dir-b .desk .deskline span:nth-child(2){--c:#E8590C}html.dir-b .desk .deskline span:nth-child(3){--c:#7149C9}html.dir-b .desk .deskline span:nth-child(4){--c:#1E78B8}
html.dir-b .desk .deskline b{font:600 44px/1 'Geist',sans-serif;letter-spacing:-.04em;color:#fff!important;font-variant-numeric:tabular-nums}
html.dir-b .desk .deskline .ck{--c:#FA1896;align-self:stretch;justify-content:flex-end;color:#ECE8F2}
html.dir-b .desk .tape{margin-top:22px;border-top:1px solid #2E2B37}
html.dir-b .desk .codes{padding:11px 0;font:500 12.5px/1 var(--mono);color:#B8B2C4;--mqs:110s}
html.dir-b .desk .codes .mq-i{padding:0 18px;border-right:1px solid #2E2B37}
html.dir-b .desk .codes b{color:#2BD37F;font-weight:600}
html.dir-b .desk .codes .mq-i:nth-child(4n+2) b{color:#FF8A3D}html.dir-b .desk .codes .mq-i:nth-child(4n+3) b{color:#A98BFF}html.dir-b .desk .codes .mq-i:nth-child(4n) b{color:#5CB3F0}
html.dir-b .desk .srcs{padding:10px 0;border-top:1px solid #2E2B37;font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#6F6880;--mqs:70s}
html.dir-b .desk .srcs .mq-t{animation-direction:reverse}
html.dir-b .desk .srcs .mq-i{padding:0 20px}
html.dir-b .desk .srcs .mq-i::before{content:"\25C6";color:#FA1896;font-size:8px;margin-right:6px}
html.dir-b .desk .readfirst{margin-top:26px;background:#fff;border:1px solid #E2DDE6;border-radius:14px}
html.dir-b .desk .filters{position:relative;margin-top:18px;background:#0C0B10;border-radius:20px;padding:22px 24px 20px;color:#ECE8F2;box-shadow:0 30px 60px -40px rgba(12,11,16,.7)}
html.dir-b .desk .madlib{font:600 30px/1.35 'Geist',sans-serif;letter-spacing:-.03em;color:#fff}
html.dir-b .desk .madlib label{color:#8E879B}
html.dir-b .desk .madlib select{font:600 30px/1.2 'Geist',sans-serif;letter-spacing:-.03em;color:#2BD37F;border-bottom:2px solid #2BD37F;background-color:transparent}
html.dir-b .desk .madlib select option{color:#141216}
html.dir-b .desk .find input{background:#16141C;border:1px solid #2E2B37;color:#fff;border-radius:12px;font-family:var(--mono);font-size:14px}
html.dir-b .desk .find input::placeholder{color:#6F6880}
html.dir-b .desk #deskcount{color:#7CE0A8;font-family:var(--mono)}
html.dir-b .desk .find kbd{background:#221F2A;border-color:#2E2B37;color:#B8B2C4}
html.dir-b .desk .grid{grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:22px}
html.dir-b .desk .grp{display:grid;grid-template-columns:auto 1fr auto;align-items:center;column-gap:14px;background:#0C0B10;color:#ECE8F2;border-radius:14px;padding:14px 18px;margin-top:22px;position:relative;overflow:hidden}
html.dir-b .desk .grp::before{content:"";width:12px;height:36px;border-radius:3px;background:var(--c,#FA1896);grid-row:1/3}
html.dir-b .desk .grp h2{font:700 26px/1.05 'Geist',sans-serif;letter-spacing:-.035em;color:#fff}
html.dir-b .desk .grp .grp-n{font:500 12px/1 var(--mono);color:var(--c,#FA1896);filter:brightness(1.6);justify-self:end;white-space:nowrap}
html.dir-b .desk .grp-disc{grid-column:2/4;color:#8E879B;font-size:12.5px;margin:4px 0 0}
html.dir-b .desk .dk{background:#fff;border:1px solid #E2DDE6;border-radius:14px;box-shadow:0 1px 0 #E2DDE6;padding:16px 16px 14px;gap:8px;position:relative;overflow:hidden}
html.dir-b .desk .dk::before{content:"";position:absolute;left:0;top:0;right:0;height:3px;background:var(--c,#FA1896)}
html.dir-b .desk .dk::after{content:attr(data-n) " items";position:absolute;right:14px;bottom:20px;font:600 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--c);background:color-mix(in srgb,var(--c) 10%,#fff);border-radius:6px;padding:5px 7px}
html.dir-b .desk .dk.lead{grid-column:span 2;background:linear-gradient(135deg,#fff 55%,color-mix(in srgb,var(--c) 9%,#fff))}
html.dir-b .desk .dk.lead h3{font-size:30px;line-height:1.02;letter-spacing:-.04em}
html.dir-b .desk .dk.lead .love{font-size:16px}
html.dir-b .desk .dk.lead::after{content:attr(data-n);font:700 64px/1 'Geist',sans-serif;letter-spacing:-.05em;background:none;padding:0;bottom:10px;opacity:.9}
html.dir-b .desk .dk:hover{box-shadow:0 22px 40px -26px rgba(12,11,16,.55);border-color:var(--c)}
html.dir-b .desk .dk.gold{background:#fff}
html.dir-b .desk .dk-meta{font-family:var(--mono)}
html.dir-b .desk .dk-meta .ic{background:color-mix(in srgb,var(--c) 12%,#fff)}
html.dir-b .desk .dk-meta .kind,html.dir-b .desk .dk.gold .dk-meta .kind{color:var(--c)}
html.dir-b .desk .dk-meta .time{border-radius:6px;background:#F3F0EA;color:#3A343D}
html.dir-b .desk .dk h3{font:700 20px/1.12 'Geist',sans-serif;letter-spacing:-.03em;padding-right:4px}
html.dir-b .desk .love{font-size:14px;line-height:1.5;color:#3A343D}
html.dir-b .desk .grab{border-radius:10px;background:#0C0B10!important;color:#fff;font-family:'Geist',sans-serif;font-weight:600}
html.dir-b .desk .grab:hover{background:#FA1896!important}
html.dir-b .desk .more-tile{border-radius:14px;border:1px dashed #0C0B10;background:transparent;color:#0C0B10;font:600 13px/1 var(--mono);letter-spacing:.06em;text-transform:uppercase}
html.dir-b .desk .more-tile:hover{background:#0C0B10;color:#fff}
html.dir-b [data-cat=nuggets],html.dir-b .grp[data-grp=nuggets]{--c:#C99A00}
html.dir-b [data-cat=credit],html.dir-b .grp[data-grp=credit],html.dir-b [data-cat=myths],html.dir-b .grp[data-grp=myths],html.dir-b [data-cat=travel],html.dir-b .grp[data-grp=travel]{--c:#1E78B8}
html.dir-b [data-cat=playbook],html.dir-b .grp[data-grp=playbook],html.dir-b [data-cat=checklist],html.dir-b .grp[data-grp=checklist]{--c:#7149C9}
html.dir-b [data-cat=gutcheck],html.dir-b .grp[data-grp=gutcheck],html.dir-b [data-cat=deadlines],html.dir-b .grp[data-grp=deadlines]{--c:#E8590C}
html.dir-b [data-cat=script],html.dir-b .grp[data-grp=script],html.dir-b [data-cat=sheet],html.dir-b .grp[data-grp=sheet],html.dir-b [data-cat=decoder],html.dir-b .grp[data-grp=decoder]{--c:#12834E}
html.dir-b [data-cat=redflags],html.dir-b .grp[data-grp=redflags]{--c:#C92A2A}
html.dir-b .desk .endnote{--bb:#0C0B10;color:#ECE8F2;padding:54px 0;margin-top:50px;border:0;background:#0C0B10;border-radius:0}
html.dir-b .desk .endnote p{font:600 30px/1.25 'Geist',sans-serif;letter-spacing:-.03em;color:#fff;max-width:900px}
html.dir-b .desk .endnote a{color:#FA1896}
html.dir-b .desk .endnote .sign{color:#fff}
html.dir-b .rdr-p{font-family:'Geist',system-ui,sans-serif;border-radius:20px}
html.dir-b .rdr-p h2{font-family:'Geist',sans-serif!important;font-weight:700!important;letter-spacing:-.035em}
html.dir-b .mpick{background:#0C0B10;border-bottom:1px solid #2E2B37}
html.dir-b .mp-f,html.dir-b .mp-q{background:#16141C;border-color:#2E2B37;color:#fff}
html.dir-b .mp-f.set,html.dir-b .mp-q.set{background:#221F2A;border-color:#2BD37F}
html.dir-b .mp-f .mp-fl{color:#2BD37F}
html.dir-b .mp-sheet{border-color:#2E2B37}
html.dir-b .mp-sheet label{color:#8E879B}
html.dir-b .mp-reset{background:#16141C;color:#fff;border-color:#2E2B37}
html.dir-b .mp-s input{background:#16141C;border-color:#2E2B37;color:#fff}
html.dir-b .mp-n{color:#7CE0A8}
@media(max-width:1100px){html.dir-b .desk .grid{grid-template-columns:repeat(3,minmax(0,1fr))}html.dir-b .desk .dk.lead{grid-column:auto}html.dir-b .desk h1{font-size:70px}}
@media(max-width:860px){
 html.dir-b .desk .dhero{grid-template-columns:1fr;gap:28px}
 html.dir-b .desk .grid{grid-template-columns:repeat(2,minmax(0,1fr))}
 html.dir-b .desk .dk.lead{grid-column:span 2}
 html.dir-b .desk .deskline{grid-template-columns:repeat(2,1fr)}
 html.dir-b .desk .deskline .ck{grid-column:1/-1}
 html.dir-b .desk .deskphoto{grid-template-columns:1fr}
}
@media(max-width:640px){
 html.dir-b .desk .top{padding-top:24px}
 html.dir-b .desk h1{font-size:50px;letter-spacing:-.05em}
 html.dir-b .desk .lede{font-size:16.5px}
 html.dir-b .desk .feat h2{font-size:30px}
 html.dir-b .desk .deskphoto img{max-height:200px;min-height:0}
 html.dir-b .desk .deskphoto figcaption{padding:14px 16px;gap:8px}
 html.dir-b .desk .deskphoto figcaption span:first-child{font-size:22px}
 html.dir-b .desk .deskline b{font-size:36px}
 html.dir-b .desk .filters{padding:18px 16px;border-radius:16px}
 html.dir-b .desk .madlib,html.dir-b .desk .madlib select{font-size:23px}
 html.dir-b .desk .grid{grid-template-columns:minmax(0,1fr);gap:10px}
 html.dir-b .desk .dk.lead{grid-column:auto}
 html.dir-b .desk .dk.lead h3{font-size:25px}
 html.dir-b .desk .dk.lead::after{font-size:48px}
 html.dir-b .desk .grp{grid-template-columns:auto 1fr;padding:12px 14px}
 html.dir-b .desk .grp h2{font-size:22px}
 html.dir-b .desk .grp .grp-n{grid-column:2;justify-self:start;margin-top:6px}
 html.dir-b .desk .grp-disc{grid-column:1/-1;margin-top:8px}
 html.dir-b .desk .endnote p{font-size:23px}
}
'''
def dir_b():
    b = BODY
    a0 = b.index('<section class="dhero">'); a1 = b.index('<details class="readfirst">')
    top = b[a0:a1]
    tape = '<div class="tape">' + strip(CODE_ITEMS, 'codes') + strip(SRC_ITEMS, 'srcs') + '</div>'
    b = b[:a0] + '<div class="top bleed">' + top + tape + '</div>' + b[a1:]
    b = b.replace('<section class="endnote">', '<section class="endnote bleed">', 1)
    return b

# ======================================================================= C · BOLD BRAND POP (matured)
# Same pink energy, Bricolage Grotesque + Instrument Serif, but grown-up: no toy tilts, hairline borders,
# layered shadows, a gold bullion bar as the hero object, and a real desktop layout (sticky category rail
# beside a three-column shelf). Phones keep their own layout: stacked hero, colour bands, swipeable shelves.
C_CSS = r'''
html.dir-c{--pk:#FA1896;--pkd:#C80E70;--ink:#141216;--ink2:#1D1A21;--cr:#FBF6EF;--ln:rgba(20,18,22,.12);--mono:'JetBrains Mono',ui-monospace,monospace}
html.dir-c body{background:var(--cr)}
html.dir-c .desk{font-family:'Bricolage Grotesque',system-ui,sans-serif;max-width:1320px;padding-top:0;--isr:'Instrument Serif',Georgia,serif}
/* ---------- hero */
html.dir-c .desk .pop-hero{--bb:#FA1896;color:#fff;padding:46px 0 0;position:relative}
html.dir-c .desk .pop-hero::before{content:"";position:absolute;inset:0 -100vmax;background:
 radial-gradient(820px 520px at 80% 18%,rgba(255,255,255,.17),transparent 62%),
 radial-gradient(900px 620px at 4% 104%,rgba(110,0,58,.34),transparent 64%),
 radial-gradient(circle at 1px 1px,rgba(255,255,255,.16) 1px,transparent 1.4px) 0 0/18px 18px;pointer-events:none}
html.dir-c .desk .pop-hero>*{position:relative}
html.dir-c .desk .dhero{grid-template-columns:minmax(0,1fr) minmax(0,1.04fr);gap:60px;padding:0 0 44px;align-items:start}
html.dir-c .desk .dh-l{padding-top:8px}
html.dir-c .desk .eyebrow{display:inline-flex;align-items:center;gap:10px;background:#141216;color:#fff;font:600 12px/1 var(--mono);letter-spacing:.16em;text-transform:uppercase;padding:10px 14px 10px 12px;border-radius:8px;margin-bottom:26px;box-shadow:0 10px 24px -14px rgba(60,0,30,.7)}
html.dir-c .desk .eyebrow::before{content:"";width:8px;height:8px;border-radius:2px;background:#FA1896;box-shadow:0 0 0 3px rgba(250,24,150,.28)}
html.dir-c .desk h1{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:108px;line-height:.86;letter-spacing:-.055em;color:#fff;margin:0 0 28px;font-variation-settings:"opsz" 96;text-shadow:0 2px 0 rgba(120,0,60,.12)}
html.dir-c .desk h1 em{font-family:var(--isr);font-weight:400;font-style:italic;letter-spacing:-.025em;color:#141216;background:none;text-shadow:none}
html.dir-c .desk .lede{color:#fff;font-size:20px;line-height:1.5;font-weight:500;max-width:560px}
html.dir-c .desk .lede .hl{background:#141216;color:#fff;padding:1px 8px 2px;border-radius:6px;font-weight:700;box-decoration-break:clone;-webkit-box-decoration-break:clone}
html.dir-c .desk .sig{margin-top:30px;padding-top:22px;border-top:1px solid rgba(255,255,255,.32)}
html.dir-c .desk .sig .av{background:#141216;color:#fff;box-shadow:0 0 0 3px rgba(255,255,255,.9)}
html.dir-c .desk .sign{color:#141216}
html.dir-c .desk .sig .role{color:#fff;opacity:.92}
/* ---------- vault: gold bar + two teasers + the calculator */
html.dir-c .desk .vault{position:relative;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:16px;align-items:stretch}
html.dir-c .desk .ingot{grid-column:1/-1;position:relative;display:block;text-decoration:none;color:inherit;margin:0 -6px 2px;-webkit-tap-highlight-color:transparent}
html.dir-c .desk .ingot svg{display:block;width:100%;height:auto;overflow:visible;filter:drop-shadow(0 28px 26px rgba(70,0,36,.42)) drop-shadow(0 6px 6px rgba(70,0,36,.22));transition:transform .45s cubic-bezier(.2,.7,.2,1)}
html.dir-c .desk .ingot:hover svg,html.dir-c .desk .ingot:focus-visible svg{transform:translateY(-4px)}
html.dir-c .desk .ingot:focus-visible{outline:2px solid #fff;outline-offset:6px;border-radius:12px}
html.dir-c .desk .ingot .shine{animation:dxShine 6.5s cubic-bezier(.45,.05,.3,1) infinite}
@keyframes dxShine{0%{transform:translateX(-360px) skewX(-18deg)}55%,100%{transform:translateX(900px) skewX(-18deg)}}
html.dir-c .desk .ingot-go{position:absolute;right:7%;bottom:14%;font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:#141216;background:#fff;border-radius:6px;padding:7px 9px;box-shadow:0 8px 18px -10px rgba(60,0,30,.6)}
html.dir-c .desk .seal{position:absolute;right:-22px;top:-30px;width:104px;height:104px;z-index:3;pointer-events:none;filter:drop-shadow(0 10px 14px rgba(60,0,30,.35))}
html.dir-c .desk .seal svg{width:100%;height:100%;display:block}
html.dir-c .desk .feat{position:relative;z-index:2;transform:none;border:0;border-radius:18px;background:#fff;padding:24px 24px 22px;box-shadow:0 1px 0 rgba(255,255,255,.6) inset,0 30px 50px -30px rgba(60,0,30,.6);display:flex;flex-direction:column}
html.dir-c .desk .feat:hover{transform:translateY(-3px)}
html.dir-c .desk .feat .ft-k{display:inline-block;align-self:flex-start;background:#FA1896;color:#fff;border-radius:6px;padding:6px 9px;font:600 10.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase}
html.dir-c .desk .feat .ic.big{position:absolute;right:20px;top:18px;width:58px;height:58px}
html.dir-c .desk .feat .ic.big svg{width:46px;height:46px}
html.dir-c .desk .feat h2{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:34px;line-height:.95;letter-spacing:-.045em;margin:16px 0 10px;padding-right:56px}
html.dir-c .desk .feat p{font-size:15px;line-height:1.5}
html.dir-c .desk .feat .btnp{margin-top:auto;align-self:flex-start;background:#141216;border-radius:10px;font-family:'Bricolage Grotesque',sans-serif;font-weight:800;transition:background .2s}
html.dir-c .desk .feat:hover .btnp{background:#FA1896}
html.dir-c .desk .pvs{display:grid;gap:16px;grid-template-rows:1fr 1fr}
html.dir-c .desk .pv{position:relative;display:flex;flex-direction:column;justify-content:space-between;gap:14px;text-decoration:none;border-radius:16px;padding:18px 18px 16px;color:#fff;overflow:hidden;box-shadow:0 26px 40px -28px rgba(60,0,30,.7);transition:transform .25s cubic-bezier(.2,.7,.2,1)}
html.dir-c .desk .pv:hover{transform:translateY(-3px)}
html.dir-c .desk .pv b{display:flex;align-items:center;gap:8px;font:600 10.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;opacity:.85}
html.dir-c .desk .pv b::before{content:"";width:6px;height:6px;border-radius:2px;background:currentColor}
html.dir-c .desk .pv span{font:800 21px/1.05 'Bricolage Grotesque',sans-serif;letter-spacing:-.03em}
html.dir-c .desk .pv i{font:400 italic 15px/1 var(--isr);opacity:.85}
html.dir-c .desk .pv::after{content:"";position:absolute;right:-30px;bottom:-30px;width:110px;height:110px;border-radius:50%;border:1px solid rgba(255,255,255,.18);box-shadow:0 0 0 18px rgba(255,255,255,.04)}
html.dir-c .desk .pv2{background:#141216}
html.dir-c .desk .pv3{background:#1E78B8}
/* ---------- stats tab, attached to the code tape */
html.dir-c .desk .deskline{display:grid;grid-template-columns:repeat(4,minmax(0,1fr)) minmax(0,1.25fr);gap:0;margin:0;padding:0;background:#141216;border-radius:18px 18px 0 0;overflow:hidden;box-shadow:0 -1px 0 rgba(255,255,255,.12) inset}
html.dir-c .desk .deskline span{position:relative;display:flex;flex-direction:column;justify-content:flex-end;gap:8px;padding:22px 24px 18px;border-right:1px solid rgba(255,255,255,.09);font:600 11px/1.3 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#BDB5C4}
html.dir-c .desk .deskline span::before{content:"";position:absolute;left:24px;top:0;width:34px;height:3px;border-radius:0 0 3px 3px;background:var(--sc,#FA1896)}
html.dir-c .desk .deskline span:nth-child(1){--sc:#12834E}html.dir-c .desk .deskline span:nth-child(2){--sc:#E8590C}html.dir-c .desk .deskline span:nth-child(3){--sc:#7149C9}html.dir-c .desk .deskline span:nth-child(4){--sc:#1E78B8}
html.dir-c .desk .deskline b,html.dir-c .desk .deskline span:first-child b{font:800 60px/.85 'Bricolage Grotesque',sans-serif;letter-spacing:-.05em;color:#fff!important;margin:0}
html.dir-c .desk .deskline .ck{align-self:stretch;margin:0;border-radius:0;display:flex;flex-direction:column;justify-content:flex-end;align-items:flex-start;padding:24px 26px 22px;border-right:0;color:#fff;font-size:11.5px;line-height:1.5;background:linear-gradient(135deg,rgba(250,24,150,.22),rgba(250,24,150,0) 70%)}
html.dir-c .desk .deskline .ck::before{background:#FA1896}
html.dir-c .desk .codes{--bb:#141216;color:#E9E4EE;padding:13px 0 14px;margin:0;font:600 14px/1 'Bricolage Grotesque',sans-serif;border-top:1px solid rgba(255,255,255,.08);--mqs:120s}
html.dir-c .desk .codes .mq-i{padding:0 16px}
html.dir-c .desk .codes .mq-i::after{content:"";width:4px;height:4px;border-radius:50%;background:#FA1896;margin-left:16px;align-self:center}
html.dir-c .desk .codes b{font:600 12px/1 var(--mono);background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);color:#fff;padding:4px 6px;border-radius:5px}
/* ---------- desk band: photo beside the picker */
html.dir-c .desk .deskband{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:22px;margin-top:30px;align-items:stretch}
html.dir-c .desk .deskphoto{position:relative;margin:0;border:0;border-radius:18px;overflow:hidden;background:#141216;box-shadow:0 30px 50px -36px rgba(20,18,22,.6);transform:none;padding:0;min-height:100%}
html.dir-c .desk .deskphoto picture{display:block;height:100%}
html.dir-c .desk .deskphoto img{display:block;width:100%;height:100%;min-height:380px;object-fit:cover;border-radius:0;filter:saturate(.92) contrast(1.04)}
html.dir-c .desk .deskphoto figcaption{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;align-items:flex-end;gap:12px;padding:60px 20px 16px;background:linear-gradient(180deg,transparent,rgba(20,18,22,.82));color:#E9E4EE;font-size:12px}
html.dir-c .desk .deskphoto figcaption span:first-child{font-family:var(--isr);font-style:italic;font-size:30px;line-height:1;color:#fff}
html.dir-c .desk .deskphoto figcaption a{color:#fff}
html.dir-c .desk .db-r{display:flex;flex-direction:column;gap:14px;min-width:0}
html.dir-c .desk .readfirst{margin:0;border:1px solid var(--ln);border-left:4px solid #141216;border-radius:12px;background:#fff;font-size:14px}
html.dir-c .desk .filters{flex:1;margin:0;position:relative;background:#fff;border:1px solid #141216;border-radius:18px;padding:28px 30px 24px;box-shadow:0 30px 50px -36px rgba(20,18,22,.55);overflow:hidden}
html.dir-c .desk .filters::before{content:"";position:absolute;left:0;top:0;right:0;height:5px;background:linear-gradient(90deg,#FA1896 0 40%,#12834E 40% 55%,#E8590C 55% 70%,#7149C9 70% 85%,#1E78B8 85%)}
html.dir-c .desk .madlib{font:800 40px/1.32 'Bricolage Grotesque',sans-serif;letter-spacing:-.04em;color:#141216}
html.dir-c .desk .madlib label{color:#141216}
html.dir-c .desk .madlib select{font:800 40px/1.15 'Bricolage Grotesque',sans-serif;letter-spacing:-.04em;color:#141216;background-color:#FFE3F1;border:0;border-bottom:3px solid #FA1896;border-radius:8px 8px 2px 2px;padding:0 32px 0 10px}
html.dir-c .desk .madlib select:hover,html.dir-c .desk .madlib select:focus{background-color:#FFD0E8}
html.dir-c .desk .find{margin-top:18px}
html.dir-c .desk .find input{border:1px solid #141216;border-radius:12px;font-family:'Bricolage Grotesque',sans-serif;font-size:17px;padding:12px 16px 12px 42px;min-width:min(420px,100%)}
html.dir-c .desk #deskcount{font:600 12px/1.4 var(--mono);color:#7a1450}
/* ---------- the grid: category rail + shelf */
html.dir-c .desk .grid{display:grid;grid-template-columns:minmax(0,1fr);gap:0;margin-top:44px;counter-reset:grp}
html.dir-c .desk .grid .lane{display:grid;grid-template-columns:290px minmax(0,1fr);gap:24px;align-items:start;padding:30px 0;border-top:1px solid var(--ln)}
html.dir-c .desk .grid .lane:first-of-type{border-top:0;padding-top:0}
html.dir-c .desk .grid .lane>.grp{grid-column:1;grid-row:1}html.dir-c .desk .grid .lane>.shelf{grid-column:2;grid-row:1}
html.dir-c .desk .grid .lane[hidden],html.dir-c .desk .grid .shelf[hidden]{display:none}
html.dir-c .desk .grp{counter-increment:grp;position:sticky;top:88px;display:flex;flex-direction:column;align-items:flex-start;gap:0;margin:0;padding:24px 22px 22px;border-radius:18px;background:var(--c);color:#fff;overflow:hidden;box-shadow:0 26px 40px -30px rgba(20,18,22,.6)}
html.dir-c .desk .grp::before{content:counter(grp,decimal-leading-zero);font:400 italic 64px/.8 var(--isr);letter-spacing:-.02em;opacity:.5;margin-bottom:14px}
html.dir-c .desk .grp::after{content:"";position:absolute;right:-40px;top:-40px;width:150px;height:150px;border-radius:50%;border:1px solid rgba(255,255,255,.2);box-shadow:0 0 0 22px rgba(255,255,255,.05),0 0 0 44px rgba(255,255,255,.035)}
html.dir-c .desk .grp h2{font:800 40px/.92 'Bricolage Grotesque',sans-serif;letter-spacing:-.045em;color:inherit;text-align:left;margin:0}
html.dir-c .desk .grp .grp-n{order:3;margin-top:16px;background:rgba(255,255,255,.96);color:#141216;border:0;border-radius:6px;padding:7px 9px;font:600 11px/1 var(--mono);letter-spacing:.06em;white-space:nowrap}
html.dir-c .desk .grp-disc{order:4;color:inherit;opacity:.9;font-size:13px;line-height:1.45;margin:14px 0 0;font-weight:500}
html.dir-c .desk .grid .shelf{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;align-items:stretch;grid-auto-flow:row dense}
html.dir-c .desk .dk{position:relative;overflow:hidden;background:#fff;border:1px solid var(--ln);border-radius:16px;box-shadow:0 1px 0 rgba(20,18,22,.05),0 18px 34px -26px rgba(20,18,22,.42);padding:20px 20px 18px;gap:9px}
html.dir-c .desk .dk::before{content:"";position:absolute;left:0;top:0;right:0;height:3px;background:var(--c,#FA1896)}
html.dir-c .desk .dk:hover{border-color:color-mix(in srgb,var(--c) 60%,#fff);box-shadow:0 1px 0 rgba(20,18,22,.05),0 28px 44px -26px color-mix(in srgb,var(--c) 55%,transparent);transform:translateY(-4px)}
html.dir-c .desk .dk-meta .ic{background:color-mix(in srgb,var(--c) 12%,#fff);border:0;border-radius:8px}
html.dir-c .desk .dk-meta .kind,html.dir-c .desk .dk.gold .dk-meta .kind{color:#141216;font-weight:800}
html.dir-c .desk .dk-meta .time{background:#F3EEE8;color:#141216;border-radius:6px}
html.dir-c .desk .dk h3{font:800 23px/1.04 'Bricolage Grotesque',sans-serif;letter-spacing:-.035em}
html.dir-c .desk .love{font-size:14.5px;line-height:1.5;color:#3a343d}
html.dir-c .desk .grab{background:#141216!important;color:#fff;border:0;border-radius:10px;box-shadow:none;font-family:'Bricolage Grotesque',sans-serif;font-weight:800;transition:background .2s,transform .2s}
html.dir-c .desk .grab:hover{background:#FA1896!important;transform:translateX(2px)}
/* lead card of each shelf: 2x2, ink block with a ghost count */
html.dir-c .desk .dk.lead{grid-column:span 2;grid-row:span 2;background:#141216;border-color:#141216;color:#fff;padding:28px 28px 24px;justify-content:flex-end}
html.dir-c .desk .dk.lead::before{height:5px}
html.dir-c .desk .dk.lead::after{content:attr(data-n);position:absolute;right:22px;top:40px;font:400 italic 260px/1 var(--isr);letter-spacing:-.04em;color:var(--c);opacity:.55;pointer-events:none}
html.dir-c .desk .dk.lead>*{position:relative;z-index:1}
html.dir-c .desk .dk.lead h3{margin-top:auto;font-size:52px;line-height:.95;letter-spacing:-.045em;color:#fff;max-width:520px}
html.dir-c .desk .dk.lead .love{font:400 24px/1.3 var(--isr);color:#E9E4EE;max-width:520px}
html.dir-c .desk .dk.lead .dk-meta,html.dir-c .desk .dk.lead .dk-meta .kind,html.dir-c .desk .dk.lead .dk-meta .src{color:#CFC8D6}
html.dir-c .desk .dk.lead .dk-meta .ic{background:rgba(255,255,255,.1)}
html.dir-c .desk .dk.lead .dk-meta .ic svg *{stroke:#fff}
html.dir-c .desk .dk.lead .dk-meta .time{background:rgba(255,255,255,.12);color:#fff}
html.dir-c .desk .dk.lead .grab{background:#FA1896!important}
html.dir-c .desk .dk.lead .grab:hover{background:#fff!important;color:#141216}
html.dir-c .desk .dk.lead .chip{color:#fff}
html.dir-c .desk .dk.lead .chip.ex{background:rgba(255,255,255,.14);color:#fff}
/* gold: the nuggets lead is a bullion bar, the other nugget cards carry a gold-leaf edge */
html.dir-c .desk .dk.gold{background:linear-gradient(180deg,#FFFCF2,#fff 120px)}
html.dir-c .desk .dk.gold::before{height:4px;background:linear-gradient(90deg,#8C5E12,#E9C065 18%,#FFF1BE 32%,#C9922E 52%,#F4D680 74%,#9A6A18)}
html.dir-c .desk .dk.gold.lead{border:0;color:#3B2604;background:
 linear-gradient(115deg,transparent 30%,rgba(255,255,255,.38) 42%,transparent 52%) 0 0/250% 100% no-repeat,
 repeating-linear-gradient(0deg,rgba(255,255,255,.05) 0 1px,transparent 1px 3px),
 linear-gradient(160deg,#FFF0B8 0%,#F2CF6E 22%,#D9A83F 46%,#F3D27A 64%,#C48F2C 84%,#A87420 100%);
 box-shadow:inset 0 2px 0 rgba(255,250,225,.9),inset 0 -3px 0 rgba(110,70,10,.45),inset 3px 0 0 rgba(255,240,190,.5),inset -3px 0 0 rgba(120,80,15,.35),0 30px 46px -26px rgba(110,70,10,.65);animation:dxFoil 7s ease-in-out infinite}
@keyframes dxFoil{0%,40%{background-position:120% 0,0 0,0 0}80%,100%{background-position:-120% 0,0 0,0 0}}
html.dir-c .desk .dk.gold.lead::before{display:none}
html.dir-c .desk .dk.gold.lead::after{color:#7A5210;opacity:.22;text-shadow:0 2px 0 rgba(255,245,210,.6)}
html.dir-c .desk .dk.gold.lead h3{color:#3B2604;text-shadow:0 1px 0 rgba(255,246,214,.75),0 -1px 0 rgba(110,70,10,.25)}
html.dir-c .desk .dk.gold.lead .love{color:#4A3108}
html.dir-c .desk .dk.gold.lead .dk-meta,html.dir-c .desk .dk.gold.lead .dk-meta .kind,html.dir-c .desk .dk.gold.lead .dk-meta .src{color:#5A3C0A}
html.dir-c .desk .dk.gold.lead .dk-meta .ic{background:rgba(255,248,220,.5)}
html.dir-c .desk .dk.gold.lead .dk-meta .ic svg *{stroke:#5A3C0A}
html.dir-c .desk .dk.gold.lead .dk-meta .time{background:rgba(90,60,10,.14);color:#3B2604}
html.dir-c .desk .dk.gold.lead .grab{background:#141216!important;color:#fff}
html.dir-c .desk .dk.gold.lead .grab:hover{background:#FA1896!important;color:#fff}
html.dir-c .desk .more-tile{grid-column:1/-1;border:1px solid #141216;border-radius:12px;background:#fff;color:#141216;font:800 15px/1.1 'Bricolage Grotesque',sans-serif;padding:14px 18px;transition:background .2s,color .2s}
html.dir-c .desk .more-tile:hover{background:#141216;color:#fff;border-color:#141216}
html.dir-c [data-cat=nuggets],html.dir-c .grp[data-grp=nuggets]{--c:#C99A00}
html.dir-c [data-cat=credit],html.dir-c .grp[data-grp=credit],html.dir-c [data-cat=myths],html.dir-c .grp[data-grp=myths]{--c:#1E78B8}
html.dir-c [data-cat=playbook],html.dir-c .grp[data-grp=playbook],html.dir-c [data-cat=deadlines],html.dir-c .grp[data-grp=deadlines]{--c:#7149C9}
html.dir-c [data-cat=gutcheck],html.dir-c .grp[data-grp=gutcheck],html.dir-c [data-cat=travel],html.dir-c .grp[data-grp=travel]{--c:#E8590C}
html.dir-c [data-cat=script],html.dir-c .grp[data-grp=script],html.dir-c [data-cat=decoder],html.dir-c .grp[data-grp=decoder]{--c:#12834E}
html.dir-c [data-cat=checklist],html.dir-c .grp[data-grp=checklist],html.dir-c [data-cat=redflags],html.dir-c .grp[data-grp=redflags]{--c:#2A2530}
html.dir-c [data-cat=sheet],html.dir-c .grp[data-grp=sheet]{--c:#FA1896}
html.dir-c .desk .grp[data-grp=nuggets]{color:#3B2604;background:linear-gradient(160deg,#FFF0B8 0%,#F2CF6E 26%,#D9A83F 52%,#F3D27A 72%,#C48F2C 100%);box-shadow:inset 0 2px 0 rgba(255,250,225,.9),inset 0 -3px 0 rgba(110,70,10,.4),0 26px 40px -30px rgba(110,70,10,.7)}
html.dir-c .desk .grp[data-grp=nuggets] h2{text-shadow:0 1px 0 rgba(255,246,214,.7)}
html.dir-c .desk .grp[data-grp=nuggets]::after{border-color:rgba(110,70,10,.18)}
html.dir-c .desk .grp[data-grp=checklist] .grp-n,html.dir-c .desk .grp[data-grp=redflags] .grp-n{background:#FA1896;color:#fff}
html.dir-c .desk .endnote{--bb:#141216;padding:64px 0;margin-top:56px;border:0;border-radius:0;background:#141216}
html.dir-c .desk .endnote p{font:800 40px/1.12 'Bricolage Grotesque',sans-serif;letter-spacing:-.04em;color:#fff;max-width:980px}
html.dir-c .desk .endnote a{color:#fff;text-decoration:underline;text-decoration-color:#FA1896;text-decoration-thickness:4px;text-underline-offset:6px}
html.dir-c .desk .endnote .sign{color:#FA1896}
html.dir-c .rdr-p{font-family:'Bricolage Grotesque',system-ui,sans-serif;border:1px solid #141216;border-radius:20px;box-shadow:0 50px 100px -40px rgba(20,18,22,.7)}
html.dir-c .rdr-p h2{font-family:'Bricolage Grotesque',sans-serif!important;font-weight:800!important;letter-spacing:-.04em}
html.dir-c .rdr-p.gold{background:linear-gradient(170deg,#FFF3C9,#fff 300px);border-color:#C99A00}
html.dir-c .mpick{background:var(--cr);border-bottom:1px solid #141216}
html.dir-c .mp-f,html.dir-c .mp-q{border:1px solid #141216}
html.dir-c .mp-f .mp-sum{font-family:'Bricolage Grotesque',sans-serif;font-weight:800}
@media(prefers-reduced-motion:reduce){html.dir-c .desk .ingot .shine{animation:none;opacity:0}html.dir-c .desk .dk.gold.lead{animation:none}}
@media(max-width:1240px){html.dir-c .desk h1{font-size:92px}html.dir-c .desk .grid .lane{grid-template-columns:250px minmax(0,1fr)}html.dir-c .desk .dk.lead h3{font-size:38px}html.dir-c .desk .feat .ic.big{width:44px;height:44px;padding:6px}html.dir-c .desk .feat .ic.big svg{width:32px;height:32px}html.dir-c .desk .feat h2{font-size:30px;padding-right:44px}html.dir-c .desk .feat .btnp{white-space:nowrap;font-size:15px;padding-left:18px;padding-right:18px}}
@media(max-width:1100px){
 html.dir-c .desk h1{font-size:80px}
 html.dir-c .desk .dhero{gap:40px}
 html.dir-c .desk .grid .lane{grid-template-columns:minmax(0,1fr);gap:18px}
 html.dir-c .desk .grid .lane>.shelf{grid-column:1;grid-row:2}
 html.dir-c .desk .grp{position:relative;top:auto;display:grid;grid-template-columns:auto 1fr auto;align-items:center;column-gap:18px}
 html.dir-c .desk .grp::before{grid-row:1/3;margin:0;font-size:56px}
 html.dir-c .desk .grp .grp-n{margin-top:0;grid-column:3;grid-row:1}
 html.dir-c .desk .grp-disc{grid-column:2/4;margin-top:6px}
}
@media(max-width:860px){
 html.dir-c .desk .dhero{grid-template-columns:minmax(0,1fr);gap:40px}
 html.dir-c .desk .deskband{grid-template-columns:minmax(0,1fr)}
 html.dir-c .desk .deskphoto img{min-height:0;height:300px}
 html.dir-c .desk .grid .shelf{grid-template-columns:repeat(2,minmax(0,1fr))}
 html.dir-c .desk .dk.lead{grid-row:auto}
 html.dir-c .desk .deskline{grid-template-columns:repeat(4,minmax(0,1fr))}
 html.dir-c .desk .deskline .ck{grid-column:1/-1;border-top:1px solid rgba(255,255,255,.09);padding:14px 24px}
}
@media(max-width:640px){
 html.dir-c .desk .pop-hero{padding:24px 0 0}
 html.dir-c .desk .eyebrow{font-size:11px;margin-bottom:20px}
 html.dir-c .desk h1{font-size:60px;line-height:.88;margin-bottom:20px}
 html.dir-c .desk .lede{font-size:17px}
 html.dir-c .desk .sig{margin-top:22px;padding-top:18px}
 html.dir-c .desk .dhero{gap:30px;padding-bottom:30px}
 html.dir-c .desk .vault{grid-template-columns:minmax(0,1fr);gap:12px}
 html.dir-c .desk .ingot{margin:0 -4px 6px}
 html.dir-c .desk .ingot-go{right:8px;bottom:-8px;font-size:10px;padding:6px 8px}
 html.dir-c .desk .seal{width:74px;height:74px;right:-8px;top:-30px}
 html.dir-c .desk .pvs{grid-template-columns:1fr 1fr;grid-template-rows:auto;gap:12px;order:2}
 html.dir-c .desk .pv{padding:14px 14px 13px;gap:10px;border-radius:14px}
 html.dir-c .desk .pv span{font-size:16.5px}
 html.dir-c .desk .pv b{font-size:9.5px;letter-spacing:.1em}
 html.dir-c .desk .feat{padding:20px 20px 18px}
 html.dir-c .desk .feat h2{font-size:30px}
 html.dir-c .desk .deskline{grid-template-columns:1fr 1fr;border-radius:16px 16px 0 0}
 html.dir-c .desk .deskline span{padding:18px 18px 14px;border-bottom:1px solid rgba(255,255,255,.09)}
 html.dir-c .desk .deskline span::before{left:18px}
 html.dir-c .desk .deskline span:nth-child(2n){border-right:0}
 html.dir-c .desk .deskline b,html.dir-c .desk .deskline span:first-child b{font-size:46px}
 html.dir-c .desk .deskline .ck{padding:14px 18px;border-bottom:0}
 html.dir-c .desk .deskband{margin-top:22px;gap:14px}
 html.dir-c .desk .deskphoto img{height:210px}
 html.dir-c .desk .deskphoto figcaption{flex-direction:column;align-items:flex-start;gap:6px;padding:40px 14px 12px}
 html.dir-c .desk .deskphoto figcaption span:first-child{font-size:24px}
 html.dir-c .desk .filters{padding:22px 18px 18px;border-radius:16px}
 html.dir-c .desk .madlib,html.dir-c .desk .madlib select{font-size:28px}
 html.dir-c .desk .find input{min-width:0;width:100%}
 /* phones: colour bands + swipeable shelves */
 html.dir-c .desk .grid{margin-top:30px}
 html.dir-c .desk .grid .lane{display:block;padding:0;border:0}
 html.dir-c .desk .grp{--bb:var(--c);display:flex;border-radius:0;padding:24px 0 20px;margin-top:26px;box-shadow:0 0 0 100vmax var(--c);clip-path:inset(0 -100vmax);overflow:visible}
 html.dir-c .desk .grp[data-grp=nuggets]{box-shadow:0 0 0 100vmax #E2B754;background:linear-gradient(90deg,#E9C165,#F6DA86 50%,#D9A83F)}
 html.dir-c .desk .grp::before{font-size:44px;margin-bottom:8px}
 html.dir-c .desk .grp::after{display:none}
 html.dir-c .desk .grp h2{font-size:40px}
 html.dir-c .desk .grp .grp-n{margin-top:12px}
 html.dir-c .desk .grid .shelf{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 calc(50% - 50vw);padding:18px max(18px,calc(50vw - 50%)) 20px;scroll-padding:0 18px;scrollbar-width:none;overscroll-behavior-x:contain;align-items:stretch}
 html.dir-c .desk .grid .shelf::-webkit-scrollbar{display:none}
 html.dir-c .desk .shelf>.dk{flex:0 0 82%;scroll-snap-align:start}
 html.dir-c .desk .dk.lead{grid-column:auto;padding:22px 20px 18px}
 html.dir-c .desk .dk.lead::after{font-size:120px;right:14px}
 html.dir-c .desk .dk.lead h3{font-size:30px}
 html.dir-c .desk .dk.lead .love{font-size:19px}
 html.dir-c .desk .shelf>.more-tile{flex:0 0 46%;scroll-snap-align:start;align-self:stretch}
 html.dir-c .desk .endnote{padding:46px 0}
 html.dir-c .desk .endnote p{font-size:28px}
}
'''
C_JS = r'''<script id="dir-c-js">(function(){
var grid=document.getElementById('desk-grid');if(!grid)return;
/* wrap each group into a row: category rail + shelf (desktop), band + swipeable shelf (phones) */
var heads=[].slice.call(grid.querySelectorAll('.grp')),rows=[];
heads.forEach(function(h,gi){var g=h.getAttribute('data-grp');
 var row=document.createElement('div');row.className='lane';row.setAttribute('data-grp',g);row.style.order=String(gi*10000);
 var sh=document.createElement('div');sh.className='shelf';sh.setAttribute('data-grp',g);
 var n=h.nextElementSibling,move=[];while(n&&!n.classList.contains('grp')&&!n.classList.contains('empty')){move.push(n);n=n.nextElementSibling;}
 grid.insertBefore(row,h);row.appendChild(h);row.appendChild(sh);move.forEach(function(m){sh.appendChild(m);});rows.push(row);});
function sync(){rows.forEach(function(r){var h=r.querySelector('.grp');if(r.hidden!==h.hidden)r.hidden=h.hidden;});}
new MutationObserver(sync).observe(grid,{subtree:true,attributes:true,attributeFilter:['hidden']});sync();
/* hero teasers open their card in the reading view */
[].forEach.call(document.querySelectorAll('.desk [data-open]'),function(a){a.addEventListener('click',function(e){var c=document.getElementById(a.getAttribute('data-open'));
 if(c&&window.foReader){e.preventDefault();if(c.hidden){var y=document.getElementById('typesel');if(y){y.value='all';y.dispatchEvent(new Event('change',{bubbles:true}));}}window.foReader(c);}});});
})();</script>'''

# the bullion bar: ingot silhouette with a bevelled top face, metallic faces, stamped wording, shine sweep
INGOT = r'''<a class="ingot" href="#nug-cards" data-open="nug-cards" aria-label="Golden Nugget Pack. Every business: 11 card nuggets. Grab it"><svg viewBox="0 0 640 286" role="img" aria-hidden="true">
<defs>
<linearGradient id="gTop" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF6CF"/><stop offset=".16" stop-color="#FAE08C"/><stop offset=".42" stop-color="#E8BA4C"/><stop offset=".6" stop-color="#F7DA80"/><stop offset=".82" stop-color="#D4A03A"/><stop offset="1" stop-color="#B9852A"/></linearGradient>
<linearGradient id="gFront" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F1C762"/><stop offset=".45" stop-color="#C99230"/><stop offset="1" stop-color="#8C5D14"/></linearGradient>
<linearGradient id="gFrontX" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset=".35" stop-color="#fff" stop-opacity="0"/><stop offset=".7" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#3a2000" stop-opacity=".22"/></linearGradient>
<linearGradient id="gLeft" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#D9A540"/><stop offset="1" stop-color="#F6D57A"/></linearGradient>
<linearGradient id="gRight" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B07A1E"/><stop offset="1" stop-color="#76490A"/></linearGradient>
<linearGradient id="gInk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9A6814"/><stop offset="1" stop-color="#6B4306"/></linearGradient>
<linearGradient id="gShine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".75"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<pattern id="gBrush" width="6" height="3" patternUnits="userSpaceOnUse"><rect width="6" height="1" fill="#fff" opacity=".10"/></pattern>
<clipPath id="gClip"><path d="M104 24H536L574 152H66Z M66 152H574L626 238H14Z"/></clipPath>
<filter id="gBlur" x="-20%" y="-200%" width="140%" height="500%"><feGaussianBlur stdDeviation="9"/></filter>
</defs>
<ellipse cx="320" cy="262" rx="300" ry="13" fill="#3a001c" opacity=".35" filter="url(#gBlur)"/>
<path d="M14 238H626L622 250H18Z" fill="#6E4508"/>
<path d="M104 24L40 98L14 238L66 152Z" fill="url(#gLeft)"/>
<path d="M536 24L600 98L626 238L574 152Z" fill="url(#gRight)"/>
<path d="M66 152H574L626 238H14Z" fill="url(#gFront)"/>
<path d="M66 152H574L626 238H14Z" fill="url(#gFrontX)"/>
<path d="M104 24H536L574 152H66Z" fill="url(#gTop)"/>
<path d="M104 24H536L574 152H66Z" fill="url(#gBrush)"/>
<path d="M66 152H574" stroke="#FFF4C8" stroke-width="2" opacity=".95"/>
<path d="M104 24H536" stroke="#FFFBEA" stroke-width="1.6" opacity=".9"/>
<path d="M104 24L66 152M536 24L574 152" stroke="#FFF1C0" stroke-width="1.2" opacity=".55"/>
<path d="M14 238H626" stroke="#FFE7A0" stroke-width="1" opacity=".5"/>
<path d="M136 42H504L534 136H106Z" fill="none" stroke="#8E5F14" stroke-width="1.6" opacity=".55"/>
<path d="M136 43.5H504L534 137.5H106Z" fill="none" stroke="#FFF6D2" stroke-width="1" opacity=".55" transform="translate(0 1.4)"/>
<g font-family="Bricolage Grotesque,system-ui,sans-serif" text-anchor="middle">
<g font-size="17" font-weight="700" letter-spacing="5.5"><text x="320" y="76" fill="#FFF7D6" opacity=".85" dy="1.3">GOLDEN NUGGET PACK</text><text x="320" y="76" fill="#5E3A05" opacity=".55" dy="-1">GOLDEN NUGGET PACK</text><text x="320" y="76" fill="url(#gInk)">GOLDEN NUGGET PACK</text></g>
<g transform="translate(320 90)"><path d="M-112 0H-22M22 0H112" stroke="#8E5F14" stroke-width="1.2" opacity=".6"/><path d="M-112 1.3H-22M22 1.3H112" stroke="#FFF6D2" stroke-width="1" opacity=".6"/>
<path d="M-9 4L0 -4L9 4M-9 11L0 3L9 11" fill="none" stroke="#FFF6D2" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" opacity=".8" transform="translate(0 -2.4) scale(.78)"/>
<path d="M-9 4L0 -4L9 4M-9 11L0 3L9 11" fill="none" stroke="url(#gInk)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 -3.6) scale(.78)"/></g>
<g font-size="25" font-weight="800" letter-spacing="-.2"><text x="320" y="129" fill="#FFF7D6" opacity=".85" dy="1.4">Every business: 11 card nuggets</text><text x="320" y="129" fill="#5E3A05" opacity=".5" dy="-1.1">Every business: 11 card nuggets</text><text x="320" y="129" fill="url(#gInk)">Every business: 11 card nuggets</text></g>
<g font-size="11" font-weight="700" letter-spacing="6"><text x="320" y="204" fill="#FFE9A8" opacity=".55" dy="1.1">FREE FROM THE DESK</text><text x="320" y="204" fill="#5A3705" opacity=".75">FREE FROM THE DESK</text></g>
</g>
<g clip-path="url(#gClip)"><rect class="shine" x="0" y="0" width="120" height="260" fill="url(#gShine)" opacity=".7"/></g>
</svg><span class="ingot-go">Grab it &rarr;</span></a>'''

SEAL = ('<div class="seal" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="stc" d="M60,60 m-45,0 a45,45 0 1,1 90,0 a45,45 0 1,1 -90,0"/></defs>'
        '<circle cx="60" cy="60" r="58" fill="#141216"/><circle cx="60" cy="60" r="54" fill="none" stroke="#FA1896" stroke-width="1.2"/><circle cx="60" cy="60" r="31" fill="none" stroke="#ffffff" stroke-opacity=".25" stroke-width="1"/>'
        '<text font-family="JetBrains Mono,monospace" font-weight="600" font-size="9.5" letter-spacing="1" fill="#fff"><textPath href="#stc" textLength="280" lengthAdjust="spacing">FREE &#183; NO EMAIL &#183; NO CATCH &#183; FREE &#183; NO EMAIL &#183;</textPath></text>'
        '<text x="60" y="68" text-anchor="middle" font-family="Instrument Serif,Georgia,serif" font-style="italic" font-size="25" fill="#FA1896">Free</text></svg></div>')

def dir_c():
    b = BODY
    a0 = b.index('<section class="dhero">'); a1 = b.index('<figure class="deskphoto">')
    hero = b[a0:a1]
    f0 = hero.index('<a class="feat"'); f1 = hero.index('</a>', f0) + 4
    pvs = ('<div class="pvs">'
           '<a class="pv pv2" href="#credit-personal" data-open="credit-personal"><b>Credit insight</b><span>Your score and your business card</span><i>Grab it &rarr;</i></a>'
           '<a class="pv pv3" href="#codes-everyday" data-open="codes-everyday"><b>Cheat sheet</b><span>The everyday code sheet</span><i>Grab it &rarr;</i></a></div>')
    hero = hero[:f0] + '<div class="vault">' + INGOT + SEAL + hero[f0:f1] + pvs + '</div>' + hero[f1:]
    # the stat line moves into the hero as a tab that sits on the code tape
    p0 = b.index('<figure class="deskphoto">'); p1 = b.index('</figure>', p0) + len('</figure>')
    photo = b[p0:p1]
    l0 = b.index('<p class="deskline"'); l1 = b.index('</p>', l0) + 4
    line = b[l0:l1]
    r0 = b.index('<details class="readfirst">'); r1 = b.index('</section>', b.index('<section class="filters"')) + len('</section>')
    picker = b[r0:r1]
    assert p1 <= l0 and l1 <= r0
    b = (b[:a0] + '<div class="pop-hero bleed">' + hero + line + '</div>' + strip(CODE_ITEMS, 'codes bleed')
         + '<div class="deskband">' + photo + '<div class="db-r">' + picker + '</div></div>' + b[r1:])
    b = b.replace('<section class="endnote">', '<section class="endnote bleed">', 1)
    return b


TAIL_C_JS = C_JS
DESKJS_C = F.DESKJS.replace('LIMIT=3', 'LIMIT=(window.FO_LIMIT||3)')
assert DESKJS_C != F.DESKJS
TAIL_C = '<script id="deskjs">' + DESKJS_C + '</script>' + C_JS + F.WOW_JS

DESC = "Everything I'd tell you over coffee: 490 smart items for business owners, free. No email. No catch."
T = 'Free From the Desk · First Officer by UpNonStop'
page('ffd-dir-a.html', T, dir_a(), desc=DESC, src='freebies', tail=F.TAIL + SHARED_JS,
     headx=head('dir-a', 'family=Fraunces:ital,opsz,wght@0,9..144,400..900;1,9..144,400..700&family=Archivo:wght@400..900', A_CSS))
page('ffd-dir-b.html', T, dir_b(), desc=DESC, src='freebies', tail=F.TAIL + SHARED_JS,
     headx=head('dir-b', 'family=Geist:wght@400..800&family=Geist+Mono:wght@400..700', B_CSS))
page('ffd-dir-c.html', T, dir_c(), desc=DESC, src='freebies', tail=TAIL_C + SHARED_JS,
     headx=head('dir-c', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Instrument+Serif:ital@0;1', C_CSS, 'window.FO_LIMIT=6;'))
print(len(CODES), 'codes', len(SRC), 'sources')

# ======================================================================= directions index
from fosite import V4_FONTS
DIRS = [
 ('ffd-dir-a.html', 'A', 'Editorial magazine', 'An issue of a business magazine: towering Fraunces headlines, numbered sections, pull-quote lead stories and a running tape of merchant codes.',
  'a', 'Fraunces &middot; Archivo &middot; JetBrains Mono'),
 ('ffd-dir-b.html', 'B', 'Trading desk', 'Terminal-luxe: a deep-ink desk with KPI tiles, a scrolling merchant-code tape, a dark command-bar filter and colour-coded cards in Earn, Burn, Return and Learn hues.',
  'b', 'Geist &middot; Geist Mono'),
 ('ffd-dir-c.html', 'C', 'Bold brand pop', 'Loud, grown up: a full pink hero with a gold bullion bar, an ink stats tab on a merchant-code tape, a sticky category rail beside a three-column shelf on desktop, and colour bands with swipeable shelves on phones.',
  'c', 'Bricolage Grotesque &middot; Instrument Serif'),
]
dcards = ''.join(f'''<a class="d d-{c}" href="{h}"><div class="sw" aria-hidden="true"><span class="sw-k">Direction {L}</span><span class="sw-h">Everything I'd tell you <em>over coffee.</em></span><span class="sw-r"><i>490</i><i>20</i><i>121</i><i>0</i></span></div>
<div class="tx"><span class="k">Direction {L} &middot; {f}</span><b>{t}</b><span class="p">{p}</span><span class="go">Open direction {L} <span aria-hidden="true">&rarr;</span></span></div></a>''' for h, L, t, p, c, f in DIRS)
dhtml = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Free From the Desk · three directions · First Officer by UpNonStop</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{V4_FONTS}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..900;1,9..144,400..700&family=Archivo:wght@400..900&family=Geist:wght@400..800&family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Instrument+Serif:ital@0;1&display=swap">
<link rel="icon" href="img/fo-chevron-transparent-v2.png">
<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#FAF6EE;color:#141216;font-family:'DM Sans',system-ui,sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}}
.w{{max-width:1180px;margin:0 auto;padding:40px 22px 70px}}
.brand{{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:#141216}}.brand img{{width:26px;height:auto}}.brand b{{display:block;font-weight:700;font-size:16px;line-height:1.1}}.brand small{{display:block;font-size:11.5px;color:#6b6470}}
.ey{{margin-top:30px;font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#b30a68;font-weight:600}}
h1{{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:clamp(38px,5vw,62px);line-height:1.02;letter-spacing:-.02em;margin:12px 0 14px;text-wrap:balance}}h1 em{{color:#FA1896}}
p.l{{font-size:17px;color:#3a343d;max-width:680px;text-wrap:pretty}}
.gr{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:30px}}
.d{{display:flex;flex-direction:column;text-decoration:none;color:#141216;background:#fff;border:1.5px solid #ece4e9;border-radius:22px;overflow:hidden;box-shadow:0 14px 34px -26px rgba(20,18,22,.35);transition:transform .2s,box-shadow .2s}}
.d:hover{{transform:translateY(-4px);box-shadow:0 30px 50px -30px rgba(20,18,22,.5)}}
.sw{{height:230px;padding:20px;display:flex;flex-direction:column;justify-content:space-between;gap:10px}}
.sw-k{{font:600 11px/1 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase}}
.sw-h{{font-size:34px;line-height:.95;text-wrap:balance}}
.sw-r{{display:flex;gap:6px}}.sw-r i{{font-style:normal;flex:1;padding:8px 6px;font-weight:800;font-size:20px;line-height:1}}
.d-a .sw{{background:#F5EFE3;border-bottom:4px solid #121014}}.d-a .sw-k{{color:#b30a68;border-bottom:1px solid #121014;padding-bottom:8px}}.d-a .sw-h{{font-family:'Fraunces',serif;font-weight:800;letter-spacing:-.03em}}.d-a .sw-h em{{font-weight:400;color:#FA1896}}.d-a .sw-r i{{font-family:'Fraunces',serif;border-right:1px solid #121014;color:#121014}}
.d-b .sw{{background:#0C0B10;color:#fff}}.d-b .sw-k{{color:#7CE0A8}}.d-b .sw-h{{font-family:'Geist',sans-serif;font-weight:700;letter-spacing:-.05em}}.d-b .sw-h em{{font-style:normal;color:#FA1896}}.d-b .sw-r i{{font-family:'Geist',sans-serif;background:#16141C;border-radius:8px;border-bottom:3px solid}}
.d-b .sw-r i:nth-child(1){{border-color:#12834E}}.d-b .sw-r i:nth-child(2){{border-color:#E8590C}}.d-b .sw-r i:nth-child(3){{border-color:#7149C9}}.d-b .sw-r i:nth-child(4){{border-color:#1E78B8}}
.d-c .sw{{background:#FA1896;color:#fff}}.d-c .sw-k{{align-self:flex-start;background:#141216;padding:6px 9px;border-radius:99px}}.d-c .sw-h{{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;letter-spacing:-.05em}}.d-c .sw-h em{{font-family:'Instrument Serif',serif;font-weight:400;color:#141216}}.d-c .sw-r i{{font-family:'Bricolage Grotesque',sans-serif;border:2px solid #141216;border-radius:12px;box-shadow:3px 3px 0 #141216;background:#141216}}.d-c .sw-r i:nth-child(2){{background:#FFE14D;color:#141216}}.d-c .sw-r i:nth-child(3){{background:#7149C9}}.d-c .sw-r i:nth-child(4){{background:#12834E}}
.tx{{display:flex;flex-direction:column;gap:8px;padding:20px 22px 22px;flex:1}}
.tx .k{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6b6470;font-weight:600}}
.tx b{{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:28px;line-height:1.1}}
.tx .p{{color:#3a343d;text-wrap:pretty;margin-bottom:10px}}
.go{{margin-top:auto;align-self:flex-start;background:#FA1896;color:#fff;font-weight:700;padding:10px 18px;border-radius:99px;font-size:15px}}
.n{{margin-top:30px;font-size:13px;color:#6b6470}}.n a{{color:#141216}}
@media(max-width:900px){{.gr{{grid-template-columns:minmax(0,1fr)}}.w{{padding:30px 18px 50px}}}}
@media(prefers-reduced-motion:reduce){{.d{{transition:none}}.d:hover{{transform:none}}}}</style></head><body><div class="w">
<a class="brand" href="home.html"><img src="img/fo-chevron-transparent-v2.png" alt=""><span><b>First Officer</b><small>by UpNonStop&trade;</small></span></a>
<p class="ey">Free From the Desk &middot; design directions</p>
<h1>Three ways to make the desk <em>feel full.</em></h1>
<p class="l">Same 490 items, same filter, search, reading view and sticky picker on phones. Only the type, colour, density and motion change.</p>
<div class="gr">{dcards}</div>
<p class="n">Mockups on branch mockups/rebuild-v4, not production. The current version is <a href="free-from-the-desk.html">Free From the Desk</a>; all pages are in the <a href="index-gallery.html">gallery</a>.</p>
</div></body></html>'''
open(f'{ROOT}/ffd-directions.html', 'w').write(dhtml); print('ffd-directions.html', len(dhtml))
