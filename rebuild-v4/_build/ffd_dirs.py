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

# ======================================================================= C · BOLD BRAND POP
C_CSS = r'''
html.dir-c{--pk:#FA1896;--ink:#141216}
html.dir-c body{background:#FFF8F1}
html.dir-c .desk{font-family:'Bricolage Grotesque',system-ui,sans-serif;max-width:1240px;padding-top:0;--isr:'Instrument Serif',Georgia,serif}
html.dir-c .desk .pop-hero{--bb:#FA1896;color:#fff;padding:40px 0 46px;position:relative;overflow:visible}
html.dir-c .desk .pop-hero::before{content:"";position:absolute;inset:0 -100vmax;background:radial-gradient(circle at 1px 1px,rgba(255,255,255,.22) 1.2px,transparent 1.6px) 0 0/22px 22px;pointer-events:none}
html.dir-c .desk .pop-hero>*{position:relative}
html.dir-c .desk .dhero{grid-template-columns:1.3fr 1fr;gap:60px;padding:0;align-items:center}
html.dir-c .desk .eyebrow{display:inline-block;background:#141216;color:#fff;font:800 13px/1 'Bricolage Grotesque',sans-serif;letter-spacing:.08em;text-transform:uppercase;padding:9px 14px;border-radius:99px;transform:rotate(-2deg);margin-bottom:22px}
html.dir-c .desk h1{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:112px;line-height:.86;letter-spacing:-.055em;color:#fff;margin:0 0 26px;font-variation-settings:"opsz" 96}
html.dir-c .desk h1 em{font-family:var(--isr);font-weight:400;font-style:italic;letter-spacing:-.02em;color:#141216;background:none}
html.dir-c .desk .lede{color:#fff;font-size:20px;line-height:1.5;font-weight:500;max-width:620px}
html.dir-c .desk .lede .hl{background:#FFE14D;color:#141216;padding:2px 8px;border-radius:8px;font-weight:800;display:inline-block;transform:rotate(-1.5deg)}
html.dir-c .desk .sig .av{background:#141216;color:#fff}
html.dir-c .desk .sign{color:#141216}
html.dir-c .desk .sig .role{color:#fff}
html.dir-c .desk .stack{position:relative;padding:118px 10px 10px}
html.dir-c .desk .pv{position:absolute;left:8%;right:2%;background:#fff;border:2px solid #141216;border-radius:22px;padding:16px 18px;color:#141216;box-shadow:6px 6px 0 #141216}
html.dir-c .desk .pv b{display:block;font:800 11px/1 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;margin-bottom:8px}
html.dir-c .desk .pv span{font:800 20px/1.1 'Bricolage Grotesque',sans-serif;letter-spacing:-.02em}
html.dir-c .desk .pv1{top:0;left:22%;right:-2%;transform:rotate(5deg);background:#FFE14D}
html.dir-c .desk .pv1 b{color:#7a5a00}
html.dir-c .desk .pv2{top:50px;left:0;right:20%;transform:rotate(-4deg);background:#EAE2FF}
html.dir-c .desk .pv2 b{color:#7149C9}
html.dir-c .desk .feat{position:relative;z-index:2;transform:rotate(1.5deg);border:2px solid #141216;border-radius:24px;box-shadow:10px 10px 0 #141216;background:#fff}
html.dir-c .desk .feat:hover{transform:rotate(0) translate(-3px,-3px);box-shadow:14px 14px 0 #141216}
html.dir-c .desk .feat .ft-k{display:inline-block;background:#FA1896;color:#fff;border-radius:99px;padding:6px 10px;font:800 11px/1 'Bricolage Grotesque',sans-serif;letter-spacing:.1em;text-transform:uppercase}
html.dir-c .desk .feat h2{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:40px;line-height:.95;letter-spacing:-.04em}
html.dir-c .desk .feat .btnp{background:#141216;border-radius:14px;font-family:'Bricolage Grotesque',sans-serif;font-weight:800}
html.dir-c .desk .feat:hover .btnp{background:#FA1896}
html.dir-c .desk .dxstamp{position:absolute;right:-30px;top:60px;width:132px;height:132px;z-index:3;color:#141216;pointer-events:none}
html.dir-c .desk .dxstamp svg{width:100%;height:100%;animation:dxSpin 22s linear infinite}
html.dir-c .desk .dxstamp i{position:absolute;inset:0;display:grid;place-items:center;font:800 30px/1 'Bricolage Grotesque',sans-serif;font-style:normal;color:#FA1896}
@keyframes dxSpin{to{transform:rotate(360deg)}}
html.dir-c .desk .deskphoto{margin:40px 0 0;border:2px solid #141216;border-radius:26px;box-shadow:10px 10px 0 #141216;transform:rotate(-.6deg);background:#fff;padding:12px}
html.dir-c .desk .deskphoto img{height:320px;width:100%;object-fit:cover;border-radius:16px}
html.dir-c .desk .deskphoto figcaption span:first-child{font-family:var(--isr);font-style:italic;font-size:24px;color:#141216}
html.dir-c .desk .deskline{display:grid;grid-template-columns:repeat(4,1fr) 1.1fr;gap:14px;margin:34px 0 0;padding:0}
html.dir-c .desk .deskline span{display:flex;flex-direction:column;justify-content:space-between;gap:10px;border:2px solid #141216;border-radius:22px;padding:16px 18px;font:800 12px/1.2 'Bricolage Grotesque',sans-serif;letter-spacing:.06em;text-transform:uppercase;box-shadow:5px 5px 0 #141216;transition:transform .2s}
html.dir-c .desk .deskline span:hover{transform:translate(-2px,-2px) rotate(-1deg)}
html.dir-c .desk .deskline b{font:800 64px/.85 'Bricolage Grotesque',sans-serif;letter-spacing:-.05em}
html.dir-c .desk .deskline span:nth-child(1){background:#141216;color:#fff}html.dir-c .desk .deskline span:nth-child(1) b{color:#fff!important}
html.dir-c .desk .deskline span:nth-child(2){background:#FFE14D;color:#141216}
html.dir-c .desk .deskline span:nth-child(3){background:#7149C9;color:#fff}html.dir-c .desk .deskline span:nth-child(3) b{color:#fff}
html.dir-c .desk .deskline span:nth-child(4){background:#12834E;color:#fff}html.dir-c .desk .deskline span:nth-child(4) b{color:#fff}
html.dir-c .desk .deskline .ck{align-self:stretch;background:#fff;color:#141216;justify-content:center;font-size:13px}
html.dir-c .desk .codes{--bb:#141216;color:#fff;padding:14px 0;margin-top:34px;font:700 15px/1 'Bricolage Grotesque',sans-serif;transform:rotate(-1deg)}
html.dir-c .desk .codes .mq-i{padding:0 14px}
html.dir-c .desk .codes .mq-i::after{content:"\2726";color:#FA1896;margin-left:14px}
html.dir-c .desk .codes b{font:700 13px/1 'JetBrains Mono',monospace;background:#FFE14D;color:#141216;padding:4px 7px;border-radius:6px}
html.dir-c .desk .readfirst{margin-top:34px;border:2px solid #141216;border-radius:18px;background:#fff}
html.dir-c .desk .filters{margin-top:30px;background:#fff;border:2px solid #141216;border-radius:28px;padding:26px 28px 22px;box-shadow:8px 8px 0 #FA1896}
html.dir-c .desk .madlib{font:800 46px/1.25 'Bricolage Grotesque',sans-serif;letter-spacing:-.04em;color:#141216}
html.dir-c .desk .madlib select{font:800 46px/1.15 'Bricolage Grotesque',sans-serif;letter-spacing:-.04em;color:#141216;background-color:#FFE3F1;border:0;border-bottom:4px solid #FA1896;border-radius:12px 12px 4px 4px;padding:0 34px 0 10px}
html.dir-c .desk .find input{border:2px solid #141216;border-radius:16px;font-family:'Bricolage Grotesque',sans-serif;font-size:17px}
html.dir-c .desk .grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:10px}
html.dir-c .desk .grid .shelf{display:contents}
html.dir-c .desk .grp{--bb:var(--c);display:grid;grid-template-columns:1fr auto;align-items:end;column-gap:20px;color:#fff;padding:34px 0 26px;margin-top:40px;background:var(--c);box-shadow:0 0 0 100vmax var(--c);clip-path:inset(0 -100vmax)}
html.dir-c .desk .grp h2{font:800 64px/.9 'Bricolage Grotesque',sans-serif;letter-spacing:-.05em;color:inherit}
html.dir-c .desk .grp .grp-n{background:#fff;color:#141216;border:2px solid #141216;border-radius:99px;padding:8px 12px;font:800 13px/1 'Bricolage Grotesque',sans-serif;transform:rotate(3deg);white-space:nowrap;box-shadow:3px 3px 0 #141216}
html.dir-c .desk .grp-disc{grid-column:1/-1;color:inherit;opacity:.9;font-size:14px;margin:12px 0 0;font-weight:500}
html.dir-c .desk .dk{background:#fff;border:2px solid #141216;border-radius:22px;box-shadow:6px 6px 0 #141216;padding:20px;gap:9px}
html.dir-c .desk .dk:hover{box-shadow:10px 10px 0 var(--c,#FA1896);transform:translate(-3px,-3px) rotate(-.4deg)}
html.dir-c .desk .dk.gold{background:#FFFBEA}
html.dir-c .desk .dk-meta .ic{background:color-mix(in srgb,var(--c) 18%,#fff);border:1.5px solid #141216}
html.dir-c .desk .dk-meta .kind,html.dir-c .desk .dk.gold .dk-meta .kind{color:#141216;font-weight:800}
html.dir-c .desk .dk-meta .time{background:#141216;color:#fff;border-radius:99px}
html.dir-c .desk .dk h3{font:800 25px/1.02 'Bricolage Grotesque',sans-serif;letter-spacing:-.035em}
html.dir-c .desk .love{font-size:15px;line-height:1.5;color:#2b262e}
html.dir-c .desk .grab{background:#FA1896!important;border:2px solid #141216;border-radius:14px;box-shadow:3px 3px 0 #141216;font-family:'Bricolage Grotesque',sans-serif;font-weight:800}
html.dir-c .desk .grab:hover{box-shadow:5px 5px 0 #141216;transform:translate(-2px,-2px)}
html.dir-c .desk .more-tile{border:2px dashed #141216;border-radius:22px;background:#fff;color:#141216;font:800 16px/1.1 'Bricolage Grotesque',sans-serif}
html.dir-c .desk .more-tile:hover{background:#141216;color:#fff;border-style:solid}
html.dir-c [data-cat=nuggets],html.dir-c .grp[data-grp=nuggets]{--c:#C99A00}
html.dir-c [data-cat=credit],html.dir-c .grp[data-grp=credit],html.dir-c [data-cat=myths],html.dir-c .grp[data-grp=myths]{--c:#1E78B8}
html.dir-c [data-cat=playbook],html.dir-c .grp[data-grp=playbook],html.dir-c [data-cat=deadlines],html.dir-c .grp[data-grp=deadlines]{--c:#7149C9}
html.dir-c [data-cat=gutcheck],html.dir-c .grp[data-grp=gutcheck],html.dir-c [data-cat=travel],html.dir-c .grp[data-grp=travel]{--c:#E8590C}
html.dir-c [data-cat=script],html.dir-c .grp[data-grp=script],html.dir-c [data-cat=decoder],html.dir-c .grp[data-grp=decoder]{--c:#12834E}
html.dir-c [data-cat=checklist],html.dir-c .grp[data-grp=checklist],html.dir-c [data-cat=redflags],html.dir-c .grp[data-grp=redflags]{--c:#141216}
html.dir-c [data-cat=sheet],html.dir-c .grp[data-grp=sheet]{--c:#FA1896}
html.dir-c .desk .grp[data-grp=nuggets]{color:#141216}
html.dir-c .desk .endnote{--bb:#141216;padding:60px 0;margin-top:60px;border:0;border-radius:0;background:#141216}
html.dir-c .desk .endnote p{font:800 38px/1.12 'Bricolage Grotesque',sans-serif;letter-spacing:-.04em;color:#fff;max-width:960px}
html.dir-c .desk .endnote a{color:#141216;background:#FFE14D;padding:0 6px;border-radius:8px;text-decoration:none}
html.dir-c .desk .endnote .sign{color:#FA1896}
html.dir-c .rdr-p{font-family:'Bricolage Grotesque',system-ui,sans-serif;border:2px solid #141216;box-shadow:12px 12px 0 #141216}
html.dir-c .rdr-p h2{font-family:'Bricolage Grotesque',sans-serif!important;font-weight:800!important;letter-spacing:-.04em}
html.dir-c .mpick{background:#FFF8F1;border-bottom:2px solid #141216}
html.dir-c .mp-f,html.dir-c .mp-q{border:2px solid #141216}
html.dir-c .mp-f .mp-sum{font-family:'Bricolage Grotesque',sans-serif;font-weight:800}
@media(max-width:1100px){html.dir-c .desk h1{font-size:84px}}
@media(max-width:860px){
 html.dir-c .desk .dhero{grid-template-columns:1fr;gap:56px}
 html.dir-c .desk .grid{grid-template-columns:repeat(2,minmax(0,1fr))}
 html.dir-c .desk .deskline{grid-template-columns:repeat(2,1fr)}
 html.dir-c .desk .deskline .ck{align-self:stretch;grid-column:1/-1}
}
@media(max-width:640px){
 html.dir-c .desk .pop-hero{padding:26px 0 34px}
 html.dir-c .desk h1{font-size:60px;line-height:.88}
 html.dir-c .desk .lede{font-size:17px}
 html.dir-c .desk .stack{padding:150px 4px 6px}
 html.dir-c .desk .pv1{left:14%;right:-2%}
 html.dir-c .desk .pv2{top:70px;left:-2%;right:12%}
 html.dir-c .desk .pv span{font-size:17px}
 html.dir-c .desk .dxstamp{width:92px;height:92px;top:-62px;right:-6px}
 html.dir-c .desk .dxstamp i{font-size:22px}
 html.dir-c .desk .feat{box-shadow:7px 7px 0 #141216}
 html.dir-c .desk .feat h2{font-size:32px}
 html.dir-c .desk .deskphoto{box-shadow:6px 6px 0 #141216;padding:8px}
 html.dir-c .desk .deskphoto img{height:200px}
 html.dir-c .desk .deskline{gap:10px}
 html.dir-c .desk .deskline span{padding:14px;box-shadow:4px 4px 0 #141216}
 html.dir-c .desk .deskline b{font-size:48px}
 html.dir-c .desk .filters{padding:18px;border-radius:22px;box-shadow:6px 6px 0 #FA1896}
 html.dir-c .desk .madlib,html.dir-c .desk .madlib select{font-size:28px}
 /* Netflix-style shelves */
 html.dir-c .desk .grid{grid-template-columns:minmax(0,1fr);gap:0}
 html.dir-c .desk .grp{padding:24px 0 20px;margin-top:30px;grid-template-columns:1fr}
 html.dir-c .desk .grp h2{font-size:42px}
 html.dir-c .desk .grp .grp-n{justify-self:start;margin-top:12px}
 html.dir-c .desk .grid .shelf{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 calc(50% - 50vw);padding:20px max(18px,calc(50vw - 50% + 0px)) 22px;scroll-padding:0 18px;scrollbar-width:none;overscroll-behavior-x:contain}
 html.dir-c .desk .grid .shelf::-webkit-scrollbar{display:none}
 html.dir-c .desk .shelf>.dk{flex:0 0 80%;scroll-snap-align:start}
 html.dir-c .desk .shelf>.more-tile{flex:0 0 46%;scroll-snap-align:start;align-self:stretch}
 html.dir-c .desk .grp[hidden]+.shelf{display:none}
 html.dir-c .desk .endnote p{font-size:27px}
}
'''
C_JS = r'''<script id="dir-c-js">(function(){
var grid=document.getElementById('desk-grid');if(!grid)return;
/* wrap each group's cards in a shelf (horizontal row on phones, invisible on desktop) */
var heads=[].slice.call(grid.querySelectorAll('.grp'));
heads.forEach(function(h,gi){var sh=document.createElement('div');sh.className='shelf';sh.setAttribute('data-grp',h.getAttribute('data-grp'));sh.style.order=String(gi*10000+1);
 var n=h.nextElementSibling,move=[];while(n&&!n.classList.contains('grp')&&!n.classList.contains('empty')){move.push(n);n=n.nextElementSibling;}
 h.parentNode.insertBefore(sh,h.nextSibling);move.forEach(function(m){sh.appendChild(m);});});
/* keep the head and its shelf together when the head hides */
function sync(){heads.forEach(function(h){var s=h.nextElementSibling;if(s&&s.classList.contains('shelf')&&s.hidden!==h.hidden)s.hidden=h.hidden;});}
new MutationObserver(sync).observe(grid,{subtree:true,attributes:true,attributeFilter:['hidden']});sync();
})();</script>'''

STAMP = ('<div class="dxstamp" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="stc" d="M60,60 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>'
         '<circle cx="60" cy="60" r="58" fill="#FFE14D" stroke="#141216" stroke-width="2.5"/>'
         '<text font-family="Bricolage Grotesque,sans-serif" font-weight="800" font-size="11" letter-spacing="1" fill="#141216"><textPath href="#stc" textLength="286" lengthAdjust="spacing">FREE &#183; NO EMAIL &#183; NO CATCH &#183; FREE &#183; NO EMAIL &#183;</textPath></text></svg><i>&#10022;</i></div>')

def dir_c():
    b = BODY
    a0 = b.index('<section class="dhero">'); a1 = b.index('<figure class="deskphoto">')
    # 0 emails asked for: echoed in the stamp centre, the stamp ring reuses "Free" and "No email. No catch."
    hero = b[a0:a1]
    f0 = hero.index('<a class="feat"'); f1 = hero.index('</a>', f0) + 4
    pv = ('<div class="pv pv1" aria-hidden="true"><b>Golden Nugget pack</b><span>Every business: 11 card nuggets</span></div>'
          '<div class="pv pv2" aria-hidden="true"><b>Credit insight</b><span>Your score and your business card</span></div>')
    hero = hero[:f0] + '<div class="stack">' + pv + STAMP + hero[f0:f1] + '</div>' + hero[f1:]
    b = b[:a0] + '<div class="pop-hero bleed">' + hero + '</div>' + b[a1:]
    b = b.replace('<details class="readfirst">', strip(CODE_ITEMS, 'codes bleed') + '<details class="readfirst">', 1)
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
 ('ffd-dir-c.html', 'C', 'Bold brand pop', 'Loud and confident: a full pink hero, sticker badges, a spinning stamp, colour-blocked category bands and swipeable shelves on phones.',
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
