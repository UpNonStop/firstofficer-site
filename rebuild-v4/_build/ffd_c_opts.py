"""Direction C, five 'more First Officer' options: no black blocks, no circles.
Builds ffd-c-opt-1..5.html and the gallery ffd-c-options.html. Reuses direction C's body, CSS and JS."""
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import ffd_dirs as D
from fosite import page, ROOT, V4_FONTS

CHEV = 'img/fo-chevron-transparent-v2.png'
# an up-pointing chevron, used as a clip-path wherever a dot or ring used to be
CP = 'polygon(50% 0,100% 50%,100% 100%,50% 50%,0 100%,0 50%)'

def body():
    b = D.dir_c()
    assert D.SEAL in b
    b = b.replace(D.SEAL, '')
    av = '<div class="av" aria-hidden="true">O</div>'
    assert av in b
    b = b.replace(av, f'<img class="av mkv" src="{CHEV}" alt="" aria-hidden="true">')
    return b

# ---------------------------------------------------------------- shared: strip the rings, seal, avatar disc and icon tiles
BASE = r'''
§ .sig .av.mkv{width:34px;height:auto;filter:brightness(0) invert(1);flex:0 0 34px;background:none!important;border-radius:0!important;box-shadow:none!important;padding:0;display:block}
§ .pv::after,§ .grp::after{display:none}
§ .feat .ic.big,§ .dk-meta .ic,§ .dk.lead .dk-meta .ic,§ .dk.gold.lead .dk-meta .ic{background:none!important;border:0!important;border-radius:0!important;box-shadow:none!important}
§ .codes .mq-i::after{width:7px;height:7px;border-radius:0;clip-path:CP}
§ .pv b::before{border-radius:0;width:8px;height:7px;clip-path:CP}
§ .eyebrow::before{border-radius:0;width:11px;height:10px;box-shadow:none;clip-path:CP}
html.dir-c.ox [data-cat=checklist],html.dir-c.ox .grp[data-grp=checklist],html.dir-c.ox [data-cat=redflags],html.dir-c.ox .grp[data-grp=redflags]{--c:#A0105F}
html.dir-c.ox .rdr-p{border-color:rgba(20,18,22,.16)}
html.dir-c.ox .mpick{border-bottom-color:rgba(20,18,22,.14)}
§ .deskphoto{background:#E9DFD3}
§ .deskline span{align-self:stretch}
@media(max-width:860px){§ .deskline .ck{padding-top:32px}}
@media(max-width:640px){§ .sig .av.mkv{width:30px;flex-basis:30px}}
'''

# ---------------------------------------------------------------- 1 cream paper + pink chevrons
O1 = r'''
§ .pop-hero::before{background:
  radial-gradient(820px 520px at 80% 18%,rgba(255,255,255,.17),transparent 62%),
  radial-gradient(900px 620px at 4% 104%,rgba(110,0,58,.30),transparent 64%),
  linear-gradient(135deg,rgba(255,255,255,.07) 25%,transparent 25%) -14px 0/28px 28px,
  linear-gradient(225deg,rgba(255,255,255,.07) 25%,transparent 25%) -14px 0/28px 28px}
§ .eyebrow{background:#FBF6EF;color:#B30A68;box-shadow:0 10px 24px -14px rgba(60,0,30,.6)}
§ h1 em{color:#FFF1DC}
§ .lede .hl{background:#FBF6EF;color:#B30A68!important}
§ .sig .sign{color:#FFF1DC}
§ .feat .btnp{background:#FA1896}
§ .feat:hover .btnp{background:#C80E70}
§ .pv{border-radius:14px}
§ .pv2{background:#FBF6EF;color:#3A2531}
§ .pv2 b{color:#B30A68}
§ .pv2::after,§ .pv3::after{display:block;content:"";position:absolute;right:16px;bottom:14px;width:30px;height:26px;border:0;border-radius:0;box-shadow:none;background:currentColor;opacity:.14;clip-path:CP}
§ .pv2::after{background:#FA1896;opacity:.5}
§ .deskline{background:#FBF6EF;box-shadow:none;border:1px solid rgba(120,20,70,.14);border-bottom:0}
§ .deskline span{color:#6B5A63;border-right-color:rgba(120,20,70,.12);padding-top:38px}
§ .deskline span::before{border-radius:0;width:16px;height:12px;top:12px;clip-path:CP}
§ .deskline b,§ .deskline span:first-child b{color:var(--sc)!important}
§ .deskline .ck{color:#B30A68;background:repeating-linear-gradient(135deg,rgba(250,24,150,.07) 0 8px,transparent 8px 16px)}
§ .codes{--bb:#F1E6D6;color:#3A2531;border-top:1px solid rgba(120,20,70,.12);border-bottom:1px solid rgba(120,20,70,.12)}
§ .codes b{background:#fff;border-color:rgba(250,24,150,.4);color:#B30A68}
§ .readfirst{border-left-color:#FA1896;background:#FFFDF8}
§ .filters{border-color:rgba(120,20,70,.18);background:#FFFDF8}
§ .find input{border-color:rgba(120,20,70,.3)}
§ .dk{background:#FFFDF8;border-color:rgba(120,20,70,.12)}
§ .grab{background:#FA1896!important}
§ .grab:hover{background:#C80E70!important}
§ .dk.lead{background:linear-gradient(135deg,rgba(250,24,150,.035) 25%,transparent 25%) -16px 0/32px 32px,linear-gradient(225deg,rgba(250,24,150,.035) 25%,transparent 25%) -16px 0/32px 32px,#FBF3E8;border-color:color-mix(in srgb,var(--c) 30%,#F1E6D6);color:#2A1A22}
§ .dk.lead h3{color:#2A1A22}
§ .dk.lead::after{opacity:.28}
§ .dk.lead .love{color:#4A3842}
§ .dk.lead .dk-meta,§ .dk.lead .dk-meta .kind,§ .dk.lead .dk-meta .src{color:#6B5A63}
§ .dk.lead .dk-meta .ic svg *{stroke:#2A1A22}
§ .dk.lead .dk-meta .time{background:#F1E6D6;color:#2A1A22}
§ .dk.lead .chip{color:inherit}§ .dk.lead .chip.ex{background:rgba(120,20,70,.07);color:#2A1A22}
§ .dk.lead .grab:hover{background:#C80E70!important;color:#fff}
§ .dk.gold.lead .grab{background:#FA1896!important}
§ .more-tile{border-color:#FA1896;color:#B30A68;background:#FFFDF8}
§ .more-tile:hover{background:#FA1896;border-color:#FA1896;color:#fff}
§ .endnote{--bb:#F1E6D6;background:#F1E6D6;border-top:1px solid rgba(120,20,70,.12)}
§ .endnote::before{content:"";position:absolute;inset:0 -100vmax;pointer-events:none;background:linear-gradient(135deg,rgba(250,24,150,.06) 25%,transparent 25%) -18px 0/36px 36px,linear-gradient(225deg,rgba(250,24,150,.06) 25%,transparent 25%) -18px 0/36px 36px}
§ .endnote{position:relative}§ .endnote>*{position:relative}
§ .endnote p{color:#2A1A22}§ .endnote a{color:#2A1A22}
@media(max-width:860px){§ .deskline .ck{border-top-color:rgba(120,20,70,.12)}}
@media(max-width:640px){§ .deskline span{border-bottom-color:rgba(120,20,70,.12)}}
'''

# ---------------------------------------------------------------- 2 boarding pass / flight strip
NOTCH = 'polygon(0 0,100% 0,100% calc(50% - 9px),calc(100% - 9px) 50%,100% calc(50% + 9px),100% 100%,0 100%,0 calc(50% + 9px),9px 50%,0 calc(50% - 9px))'
O2 = r'''
§ .eyebrow{background:#fff;color:#B30A68;border-radius:4px;padding-right:26px;clip-path:polygon(0 0,calc(100% - 14px) 0,100% 50%,calc(100% - 14px) 100%,0 100%);box-shadow:none}
§ h1 em{color:#fff}
§ .lede .hl{background:none;color:#fff;border:1.5px dashed rgba(255,255,255,.85);border-radius:4px}
§ .sig .sign{color:#fff}
§ .feat{border-radius:10px}
§ .feat .btnp{background:#FA1896;border-radius:6px}
§ .feat:hover .btnp{background:#C80E70}
§ .pv{border-radius:10px;padding-right:76px;clip-path:NOTCH}
§ .pv::after{display:block;content:"";position:absolute;top:12px;bottom:12px;right:62px;left:auto;width:0;height:auto;border:0;border-left:1.5px dashed currentColor;border-radius:0;box-shadow:none;opacity:.35}
§ .pv1::after{border-color:#7A5210}
§ .pv2{background:#fff;color:#22303C}
§ .pv2 b{color:#7149C9}
§ .pv b{font-family:var(--mono)}
§ .pv i{position:absolute;right:12px;top:50%;transform:translateY(-50%) rotate(-90deg);transform-origin:center;white-space:nowrap;font:600 10px/1 var(--mono);font-style:normal;letter-spacing:.12em;text-transform:uppercase;width:auto}
§ .deskline{background:#fff;box-shadow:none;border-radius:10px 10px 0 0}
§ .deskline span{color:#5B6874;border-right:1.5px dashed rgba(30,60,90,.22)}
§ .deskline span::before{left:24px;top:14px;width:auto;height:auto;background:none;border-radius:0;content:"FO 0" counter(dl);font:600 10px/1 var(--mono);letter-spacing:.12em;color:var(--sc)}
§ .deskline{counter-reset:dl}§ .deskline span{counter-increment:dl;padding-top:34px}
§ .deskline b,§ .deskline span:first-child b{color:#1C2A36!important}
§ .deskline .ck{background:#FFF0F7;color:#B30A68;border-left:1.5px dashed rgba(250,24,150,.4)}
§ .deskline .ck::before{content:"";background:#FA1896;width:12px;height:11px;top:14px;clip-path:CP}
§ .codes{--bb:#E8EFF5;color:#1C2A36;border-top:1px solid rgba(30,60,90,.16);border-bottom:1px solid rgba(30,60,90,.16);background-image:repeating-linear-gradient(90deg,rgba(30,60,90,.10) 0 1px,transparent 1px 180px)}
§ .codes b{background:#fff;border:1px solid #1E78B8;color:#155E92;border-radius:3px}
§ .codes .mq-i::after{background:#1E78B8}
§ .deskphoto,§ .filters{border-radius:10px}
§ .readfirst{border-left:4px solid #1E78B8;border-radius:6px}
§ .filters{border:1px solid rgba(30,60,90,.2)}
§ .filters::before{height:6px}
§ .find input{border-color:rgba(30,60,90,.35);border-radius:6px}
§ .grp{border-radius:10px}
§ .grp::before{content:"FO " counter(grp,decimal-leading-zero);font:600 13px/1 var(--mono);letter-spacing:.16em;opacity:.85;margin-bottom:18px;padding-bottom:12px;border-bottom:1.5px dashed currentColor;align-self:stretch}
§ .dk{border-radius:8px;border-left:6px solid var(--c)}
§ .dk::before{display:none}
§ .dk-meta{padding-bottom:10px;border-bottom:1.5px dashed rgba(30,60,90,.18)}
§ .dk.lead .dk-meta{border-bottom-color:transparent}
§ .dk .grab{background:#fff!important;color:#B30A68;border:1.5px solid #FA1896;border-radius:6px}
§ .dk .grab:hover{background:#FA1896!important;color:#fff}
§ .dk.lead{background:#fff;border:1px solid color-mix(in srgb,var(--c) 40%,#fff);border-left:8px solid var(--c);color:#1C2A36;clip-path:NOTCH;padding-right:30%}
§ .dk.lead::before{display:block;content:"";position:absolute;left:auto;right:24%;top:14px;bottom:14px;width:0;height:auto;background:none;border-left:2px dashed color-mix(in srgb,var(--c) 45%,#fff)}
§ .dk.lead::after{content:attr(data-n);bottom:auto;left:auto;border:0;right:3%;top:auto;bottom:22px;width:20%;text-align:center;font:400 italic 150px/1 var(--isr);opacity:.9;color:var(--c)}
§ .dk.lead h3{color:#1C2A36}
§ .dk.lead .love{color:#3B4854}
§ .dk.lead .dk-meta,§ .dk.lead .dk-meta .kind,§ .dk.lead .dk-meta .src{color:#5B6874}
§ .dk.lead .dk-meta .ic svg *{stroke:#2A1A22}
§ .dk.lead .dk-meta .time{background:#E8EFF5;color:#1C2A36}
§ .dk.lead .chip{color:inherit}§ .dk.lead .chip.ex{background:#EEF2F6;color:#1C2A36}
§ .dk.lead .grab{background:#FA1896!important;color:#fff;border-color:#FA1896}
§ .dk.lead .grab:hover{background:#C80E70!important;color:#fff}
§ .dk.gold.lead{border-left:8px solid #A87420;clip-path:NOTCH}
§ .dk.gold.lead::before{display:block;border-left-color:rgba(110,70,10,.35)}
§ .dk.gold.lead::after{color:#7A5210;opacity:.35}
§ .dk.gold.lead .grab{background:#FA1896!important}
§ .more-tile{border:1.5px dashed #1E78B8;color:#155E92;border-radius:8px}
§ .more-tile:hover{background:#1E78B8;color:#fff;border-color:#1E78B8}
§ .endnote{--bb:#fff;background:#fff;border-top:1.5px dashed rgba(30,60,90,.22);border-bottom:1.5px dashed rgba(30,60,90,.22)}
§ .endnote p{color:#1C2A36}§ .endnote a{color:#1C2A36}
@media(max-width:1100px){§ .grp::before{border-bottom:0;padding:0;margin:0;font-size:13px}}
@media(max-width:860px){§ .deskline .ck{border-top:1.5px dashed rgba(250,24,150,.3);border-left:0}}
@media(max-width:640px){
 § .deskline span{border-bottom:1.5px dashed rgba(30,60,90,.18);padding-top:30px}
 § .deskline span::before{left:18px}
 § .pv{padding-right:44px}
 § .pv::after{right:34px}
 § .pv i{right:-2px;font-size:9px}
 § .dk.lead{padding-right:20px}
 § .dk.lead::before{display:none}
 § .dk.lead::after{font-size:96px;width:auto;right:16px;top:14px;bottom:auto;opacity:.35}
 § .grp::before{font-size:12px;border-bottom:0;padding-bottom:0}
 § .grp{border-radius:0}
}
'''

# ---------------------------------------------------------------- 3 pillar-colour blocks
PIL = ['#12834E', '#E8590C', '#7149C9', '#1E78B8']
O3 = r'''
§ .eyebrow{background:#fff;color:#B30A68;border-bottom:4px solid transparent;border-image:linear-gradient(90deg,#12834E 0 25%,#E8590C 25% 50%,#7149C9 50% 75%,#1E78B8 75%) 1;border-radius:0;box-shadow:none}
§ h1 em{color:#fff}
§ .lede .hl{background:#12834E;color:#fff}
§ .sig .sign{color:#fff}
§ .feat .btnp{background:#12834E}
§ .feat:hover .btnp{background:#FA1896}
§ .pv2{background:#7149C9}
§ .pv{border-radius:12px}
§ .pv2::after,§ .pv3::after{display:block;content:"";position:absolute;right:0;bottom:0;width:64px;height:64px;border:0;border-radius:0;box-shadow:none;background:rgba(255,255,255,.14);clip-path:polygon(100% 0,100% 100%,0 100%)}
§ .deskline{background:none;box-shadow:none;gap:0;border-radius:14px 14px 0 0}
§ .deskline span{background:var(--sc);color:rgba(255,255,255,.85);border-right:0}
§ .deskline span::before{left:24px;top:14px;width:16px;height:12px;background:rgba(255,255,255,.55);border-radius:0;clip-path:CP}
§ .deskline .ck{background:#fff;color:#B30A68}
§ .deskline .ck::before{background:#FA1896}
§ .codes{--bb:#1E78B8;color:#fff;border-top:0;background-image:linear-gradient(90deg,#12834E 0 25%,#E8590C 25% 50%,#7149C9 50% 75%,#1E78B8 75%);background-size:100% 4px;background-repeat:no-repeat;background-position:0 100%}
§ .codes b{background:rgba(255,255,255,.16);border-color:rgba(255,255,255,.4)}
§ .codes .mq-i::after{background:#fff}
§ .readfirst{border-left-color:#7149C9}
§ .filters{border:2px solid #7149C9}
§ .find input{border-color:#7149C9}
§ .dk::before{height:6px}
§ .grab{background:var(--c)!important}
§ .grab:hover{background:#FA1896!important}
§ .dk.lead{background:var(--c);border-color:var(--c);color:#fff}
§ .dk.lead::before{background:rgba(255,255,255,.35);height:6px}
§ .dk.lead::after{color:#fff;opacity:.18}
§ .dk.lead .love{color:rgba(255,255,255,.9)}
§ .dk.lead .dk-meta,§ .dk.lead .dk-meta .kind,§ .dk.lead .dk-meta .src{color:rgba(255,255,255,.85)}
§ .dk.lead .grab{background:#fff!important;color:var(--c)}
§ .dk.lead .grab:hover{background:#FA1896!important;color:#fff}
§ .dk.gold.lead .grab{background:#12834E!important;color:#fff}
§ .more-tile{border:2px solid var(--c);color:var(--c)}
§ .more-tile:hover{background:var(--c);border-color:var(--c);color:#fff}
§ .endnote{--bb:#7149C9;background:#7149C9;border-top:6px solid transparent;border-image:linear-gradient(90deg,#12834E 0 25%,#E8590C 25% 50%,#7149C9 50% 75%,#1E78B8 75%) 1}
§ .endnote .sign{color:#FFD3EA}
@media(max-width:860px){§ .deskline .ck{border-top:0}}
@media(max-width:640px){§ .deskline span{border-bottom:0}}
'''

# ---------------------------------------------------------------- 4 white premium, pink chevron cut corners
def cut(n):
    return f'polygon(0 0,calc(100% - {n}px) 0,100% {n}px,100% 100%,0 100%)'
def cutbg(n, bg='#fff'):
    d = n / 1.4142
    return f'linear-gradient(225deg,transparent 0 {d:.1f}px,#FA1896 {d:.1f}px {d+2.5:.1f}px,{bg} {d+2.5:.1f}px)'
O4 = r'''
§ .pop-hero::before{background:
  radial-gradient(820px 520px at 80% 18%,rgba(255,255,255,.17),transparent 62%),
  radial-gradient(900px 620px at 4% 104%,rgba(110,0,58,.30),transparent 64%),
  repeating-linear-gradient(90deg,rgba(255,255,255,.08) 0 1px,transparent 1px 120px)}
§ .eyebrow{background:#fff;color:#B30A68;border-radius:0;clip-path:CUT10;box-shadow:none}
§ h1 em{color:#fff}
§ .lede .hl{background:#fff;color:#B30A68!important;border-radius:0}
§ .sig .sign{color:#fff}
§ .feat{border-radius:0;clip-path:CUT28;background:BG28}
§ .feat .btnp{background:#FA1896;border-radius:0;clip-path:CUT10}
§ .feat:hover .btnp{background:#C80E70}
§ .feat .ft-k{border-radius:0}
§ .pv{border-radius:0;clip-path:CUT22}
§ .pv1{border:0}
§ .pv2{background:BG22;color:#2A1A2E}
§ .pv2 b{color:#B30A68}
§ .pv3{background:linear-gradient(225deg,transparent 0 15.6px,#FA1896 15.6px 18.1px,#1E78B8 18.1px)}
§ .deskline{background:#fff;box-shadow:none;border-radius:0;clip-path:CUT28}
§ .deskline span{color:#6B6470;border-right-color:rgba(20,18,22,.08)}
§ .deskline span::before{width:16px;height:12px;border-radius:0;top:12px;clip-path:CP}
§ .deskline b,§ .deskline span:first-child b{color:#2A1A2E!important}
§ .deskline .ck{color:#B30A68;background:linear-gradient(225deg,transparent 0 19.8px,#FA1896 19.8px 22.3px,#FFF0F7 22.3px)}
§ .codes{--bb:#fff;color:#2A1A2E;border-top:1px solid rgba(20,18,22,.08);border-bottom:1px solid rgba(20,18,22,.1)}
§ .codes b{background:#fff;border-color:#FA1896;color:#B30A68;border-radius:0}
§ .deskphoto,§ .filters,§ .readfirst{border-radius:0}
§ .deskphoto{clip-path:CUT28}
§ .filters{border:0;clip-path:CUT28;background:BG28}
§ .readfirst{border:1px solid rgba(20,18,22,.1);border-left:3px solid #FA1896}
§ .find input{border-color:rgba(20,18,22,.2);border-radius:0}
§ .madlib select{border-radius:0}
§ .grp{border-radius:0;clip-path:CUT28}
§ .dk{border-radius:0;clip-path:CUT22;background:BG22;border:0;box-shadow:0 0 0 1px rgba(20,18,22,.08) inset}
§ .dk:hover{box-shadow:0 0 0 1px color-mix(in srgb,var(--c) 50%,#fff) inset}
§ .dk.gold{background:linear-gradient(225deg,transparent 0 15.6px,#FA1896 15.6px 18.1px,transparent 18.1px),linear-gradient(180deg,#FFFCF2,#fff 120px)}
§ .grab{background:#fff!important;color:#B30A68;border:1.5px solid #FA1896;border-radius:0}
§ .grab:hover{background:#FA1896!important;color:#fff}
§ .dk.lead{clip-path:CUT40;background:linear-gradient(225deg,transparent 0 28.3px,#FA1896 28.3px 31.3px,transparent 31.3px),linear-gradient(160deg,color-mix(in srgb,var(--c) 7%,#fff),#fff 60%);color:#2A1A2E;box-shadow:0 0 0 1px color-mix(in srgb,var(--c) 25%,#fff) inset}
§ .dk.lead::after{opacity:.22}
§ .dk.lead h3{color:#2A1A2E}
§ .dk.lead .love{color:#4A4350}
§ .dk.lead .dk-meta,§ .dk.lead .dk-meta .kind,§ .dk.lead .dk-meta .src{color:#6B6470}
§ .dk.lead .dk-meta .ic svg *{stroke:#2A1A22}
§ .dk.lead .dk-meta .time{background:#F3EEE8;color:#2A1A2E}
§ .dk.lead .chip{color:inherit}§ .dk.lead .chip.ex{background:#F3EEE8;color:#2A1A2E}
§ .dk.lead .grab{background:#FA1896!important;color:#fff}
§ .dk.lead .grab:hover{background:#C80E70!important;color:#fff}
§ .dk.gold.lead{clip-path:CUT40}
§ .dk.gold.lead .grab{background:#FA1896!important}
§ .more-tile{border:1.5px solid #FA1896;color:#B30A68;border-radius:0}
§ .more-tile:hover{background:#FA1896;color:#fff;border-color:#FA1896}
§ .endnote{--bb:#fff;background:#fff;border-top:1px solid rgba(20,18,22,.08);position:relative}
§ .endnote::after{content:"";position:absolute;right:0;top:-1px;width:120px;height:60px;background:#FA1896;clip-path:CP;opacity:.9}
§ .endnote p{color:#2A1A2E}§ .endnote a{color:#2A1A2E}
@media(max-width:860px){§ .deskline .ck{border-top-color:rgba(20,18,22,.08)}}
@media(max-width:640px){§ .deskline span{border-bottom-color:rgba(20,18,22,.08)}§ .grp{clip-path:inset(0 -100vmax)}§ .endnote::after{width:70px;height:35px}}
'''
O4 = (O4.replace('CUT10', cut(10)).replace('CUT22', cut(22)).replace('CUT28', cut(28)).replace('CUT40', cut(40))
      .replace('BG22', cutbg(22)).replace('BG28', cutbg(28)))

# ---------------------------------------------------------------- 5 pink on pink, deep magenta for ink
MG, MG2 = '#7A0B47', '#5E0836'
O5 = r'''
html.dir-c.o5 body{background:#FFF2F8}
§ .eyebrow{background:MG;box-shadow:0 10px 24px -14px rgba(90,0,45,.8)}
§ .eyebrow::before{background:#FF8FCB}
§ h1 em{color:MG}
§ .lede .hl{background:MG}
§ .sig .sign{color:MG}
§ .feat .btnp{background:MG}
§ .feat:hover .btnp{background:#FA1896}
§ .pv2{background:MG;background:linear-gradient(160deg,#8E0F55,MG2)}
§ .pv2::after,§ .pv3::after{display:block;content:"";position:absolute;right:14px;bottom:12px;width:34px;height:30px;border:0;border-radius:0;box-shadow:none;background:#FF8FCB;opacity:.5;clip-path:CP}
§ .deskline{background:MG}
§ .deskline span{color:#F6C6DF;border-right-color:rgba(255,190,225,.16)}
§ .deskline span::before{border-radius:0;width:16px;height:12px;top:12px;clip-path:CP}
§ .deskline .ck{background:linear-gradient(135deg,rgba(250,24,150,.4),rgba(250,24,150,.08) 70%)}
§ .codes{--bb:MG2;color:#FBD7EA;border-top-color:rgba(255,190,225,.14)}
§ .codes b{background:rgba(255,143,203,.14);border-color:rgba(255,143,203,.4)}
§ .codes .mq-i::after{background:#FF8FCB}
§ .deskphoto{background:MG}
§ .deskphoto figcaption{background:linear-gradient(180deg,transparent,rgba(94,8,54,.85))}
§ .readfirst{border-left-color:MG;background:#fff}
§ .filters{border-color:MG}
§ .madlib,§ .madlib label,§ .madlib select{color:MG}
§ .find input{border-color:MG}
§ #deskcount{color:MG}
§ .grid .lane{border-top-color:rgba(122,11,71,.14)}
§ .dk{border-color:rgba(122,11,71,.12)}
§ .dk-meta .kind,§ .dk.gold .dk-meta .kind{color:MG}
§ .dk-meta .time{background:#FFE3F1;color:MG}
§ .grab{background:MG!important}
§ .grab:hover{background:#FA1896!important}
§ .dk.lead{background:linear-gradient(160deg,#8E0F55,MG2);border-color:MG}
§ .dk.lead .love{color:#FBD7EA}
§ .dk.lead .dk-meta,§ .dk.lead .dk-meta .kind,§ .dk.lead .dk-meta .src{color:#F6C6DF}
§ .dk.lead .dk-meta .time{background:rgba(255,143,203,.16);color:#fff}
§ .dk.lead::after{color:color-mix(in srgb,var(--c) 55%,#fff);opacity:.4}
§ .dk.lead .grab:hover{color:MG}
§ .dk.gold.lead .grab{background:MG!important}
§ .more-tile{border-color:MG;color:MG}
§ .more-tile:hover{background:MG;border-color:MG}
§ .endnote{--bb:MG;background:MG}
§ .endnote .sign{color:#FF8FCB}
§ .grp .grp-n{color:MG}
html.dir-c.o5 .mpick{background:#FFF2F8}
html.dir-c.o5 [data-cat=checklist],html.dir-c.o5 .grp[data-grp=checklist],html.dir-c.o5 [data-cat=redflags],html.dir-c.o5 .grp[data-grp=redflags]{--c:#B4126B}
@media(max-width:860px){§ .deskline .ck{border-top-color:rgba(255,190,225,.16)}}
@media(max-width:640px){§ .deskline span{border-bottom-color:rgba(255,190,225,.16)}}
'''.replace('MG2', MG2).replace('MG', MG)

OPTS = [
 (1, 'Cream paper', 'Pink hero, but every black block becomes warm cream paper with pink chevron marks, a cream stats tab, a paper code tape and paper lead cards.', O1),
 (2, 'Boarding pass', 'Cards become boarding passes and flight strips: notched edges, dashed tear-off stubs, flight-number labels on the rails and a pale air-traffic-strip code tape.', O2),
 (3, 'Pillar blocks', 'Black is replaced by the four pillar colours: a green, orange, violet and blue stats tab, lead cards in their category colour and a violet endnote.', O3),
 (4, 'White premium', 'Crisp white cards with a 45-degree cut corner traced in pink, hairline borders, square edges throughout and a pink chevron closing the page.', O4),
 (5, 'Pink on pink', 'The same bold layout, toned: deep magenta takes the place of black on the stats tab, code tape, lead cards and buttons, on a blush page.', O5),
]

B = body()
DESC = D.DESC; T = D.T
for n, name, pitch, css in OPTS:
    css = css.replace('.dk.lead', '.dk.lead:not(.gold)')
    full = (BASE + css).replace('§', f'html.dir-c.o{n} .desk').replace('html.dir-c.ox', f'html.dir-c.o{n}').replace('CP', CP).replace('NOTCH', NOTCH)
    page(f'ffd-c-opt-{n}.html', T, B, desc=DESC, src='freebies', tail=D.TAIL_C + D.SHARED_JS,
         headx=D.head('dir-c', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Instrument+Serif:ital@0;1',
                      D.C_CSS + full, f'window.FO_LIMIT=6;document.documentElement.classList.add("o{n}");'))

# ---------------------------------------------------------------- 3b: option 3 matured, colour blocks become tear-off stubs
def vnotch(x, r=8):
    """mask with two half-circle cut-outs on a vertical perforation at x (top and bottom edge)"""
    m = (f'radial-gradient(circle at {x} 0,#0000 {r}px,#000 {r+.6}px) top/100% 51% no-repeat,'
         f'radial-gradient(circle at {x} 100%,#0000 {r}px,#000 {r+.6}px) bottom/100% 51% no-repeat')
    return f'-webkit-mask:{m};mask:{m}'
def hnotch(y, r=8):
    """two cut-outs on a horizontal perforation at y (left and right edge)"""
    m = (f'radial-gradient(circle at 0 {y},#0000 {r}px,#000 {r+.6}px) left/51% 100% no-repeat,'
         f'radial-gradient(circle at 100% {y},#0000 {r}px,#000 {r+.6}px) right/51% 100% no-repeat')
    return f'-webkit-mask:{m};mask:{m}'
def vperf(right, col='rgba(255,255,255,.85)'):
    return f'linear-gradient({col} 0 6px,transparent 6px 12px) right {right} top 4px/2px 12px repeat-y'
def hperf(bottom, col='rgba(255,255,255,.85)'):
    return f'linear-gradient(90deg,{col} 0 6px,transparent 6px 12px) left 4px bottom {bottom}/12px 2px repeat-x'
def lperf(left, col='rgba(255,255,255,.85)'):
    return f'linear-gradient({col} 0 6px,transparent 6px 12px) left {left} top 4px/2px 12px repeat-y'
def tperf(top, col='rgba(255,255,255,.85)'):
    return f'linear-gradient(90deg,{col} 0 6px,transparent 6px 12px) left 4px top {top}/12px 2px repeat-x'

GOLD = 'linear-gradient(115deg,#C99A3E 0%,#E7C676 18%,#F7E3A4 34%,#E3BD62 48%,#C8963A 66%,#DDB35A 84%,#B8862E 100%)'
GOLDSTUB = 'linear-gradient(170deg,#B98526,#9C6A18)'
GOLDLEAD = 'linear-gradient(160deg,#FFF0B8 0%,#F2CF6E 22%,#D9A83F 46%,#F3D27A 64%,#C48F2C 84%,#A87420 100%)'
INK2 = '#221B27'   # dark text, never a block
FOUR = 'linear-gradient(90deg,#12834E 0 25%,#E8590C 25% 50%,#7149C9 50% 75%,#1E78B8 75%)'
SH = '0 1px 2px rgba(20,18,22,.05),0 14px 30px -24px rgba(20,18,22,.38)'
LW, PW, PWm, DS, GH, EW = 136, 46, 34, 40, 52, 200   # lead stub, pv stub, pv stub phone, deskline stub, rail stub, endnote stub

O3B = r'''
html.dir-c.ox{--cd:color-mix(in srgb,var(--c) 84%,#1a1014)}
html.dir-c.ox .desk [data-cat],html.dir-c.ox .desk .grp{--cd:color-mix(in srgb,var(--c) 84%,#1a1014)}
/* hero: fine chart grid in place of the dot screen */
§ .pop-hero::before{background:
  radial-gradient(820px 520px at 80% 18%,rgba(255,255,255,.16),transparent 62%),
  radial-gradient(900px 620px at 4% 104%,rgba(110,0,58,.28),transparent 64%),
  linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px) 0 0/32px 32px,
  linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px) 0 0/32px 32px}
§ .eyebrow{background:#fff;color:#B30A68;border-radius:6px 6px 0 0;box-shadow:none;border-bottom:3px solid transparent;border-image:FOUR 1}
§ .eyebrow::before{background:#FA1896}
§ h1 em{color:#fff}
§ .lede .hl{background:#FBF6EF;color:#0F6E41!important;border-radius:4px}
/* signature: a small cream pass, the pink chevron on its stub */
§ .sig{display:inline-flex;align-items:stretch;gap:0;margin-top:30px;padding:0;border:0;background:#FBF6EF;border-radius:10px;SIGMASK}
§ .sig .av.mkv{filter:none;width:30px;flex:0 0 auto;box-sizing:content-box;padding:0 18px;align-self:center;border-right:1.5px dashed rgba(179,10,104,.35)!important;height:auto}
§ .sig .av.mkv{border-right:0!important}
§ .sig>div{padding:12px 24px 12px 20px;background:linear-gradient(rgba(179,10,104,.4) 0 5px,transparent 5px 10px) left 0 top 4px/1.5px 10px repeat-y}
§ .sig .sign{color:#C80E70}
§ .sig .role{color:#5B4A55;opacity:1}
/* calculator card */
§ .feat{border-radius:14px}
§ .feat .btnp{background:#FA1896;border-radius:8px}
§ .feat:hover .btnp{background:#C80E70}
/* hero passes: white or gold body, coloured stub carries Grab it */
§ .pvs{filter:drop-shadow(0 18px 18px rgba(90,0,45,.22))}
§ .pv{border-radius:12px;padding-right:calc(PWpx + 16px);box-shadow:none;PVMASK}
§ .pv b::before{background:#FA1896}
§ .pv span{color:INK2}
§ .pv i{position:absolute;right:0;top:0;bottom:0;width:PWpx;display:flex;align-items:center;justify-content:center;writing-mode:vertical-rl;transform:rotate(180deg);font:600 10px/1 var(--mono);font-style:normal;letter-spacing:.14em;text-transform:uppercase;color:#fff;opacity:1}
§ .pv2{background:PVPERF,linear-gradient(#7149C9,#7149C9) right 0 top 0/PWpx 100% no-repeat,#fff;color:INK2}
§ .pv2 b{color:#5A35B0;opacity:1}
§ .pv3{background:PVPERF,linear-gradient(#1E78B8,#1E78B8) right 0 top 0/PWpx 100% no-repeat,#fff;color:INK2}
§ .pv3 b{color:#155E92;opacity:1}
§ .pv1{background:PVPERFG,GOLDSTUB right 0 top 0/PWpx 100% no-repeat,GOLD;box-shadow:inset 0 1px 0 rgba(255,249,224,.75)}
§ .pv1 span{color:#2E1D04}
§ .pv1 i{color:#FFF3D0}
/* stats: four boarding-pass stubs, then the checked tab */
§ .deskline{background:none;box-shadow:none;border-radius:0;gap:10px;padding:0 0 22px;overflow:visible;counter-reset:dl;filter:drop-shadow(0 16px 16px rgba(90,0,45,.2))}
§ .deskline span{border:0;border-radius:10px;background:DLPERF,linear-gradient(var(--sc),var(--sc)) left 0 top 0/DSpx 100% no-repeat,#fff;color:#6B5F68;padding:20px 20px 16px calc(DSpx + 20px);DLMASK}
§ .deskline span:not(.ck){counter-increment:dl}
§ .deskline span:not(.ck)::before{content:"FO 0" counter(dl);left:0;top:0;bottom:0;width:DSpx;height:auto;border-radius:0;background:none;clip-path:none;display:flex;align-items:center;justify-content:center;writing-mode:vertical-rl;transform:rotate(180deg);font:600 10px/1 var(--mono);letter-spacing:.16em;color:#fff}
§ .deskline b,§ .deskline span:first-child b{color:INK2!important}
§ .deskline .ck{background:#FBF6EF;color:#B30A68;border-radius:10px;-webkit-mask:none;mask:none;padding:20px 22px 16px}
§ .deskline .ck::before{content:"";left:22px;top:18px;width:14px;height:12px;background:#FA1896;border-radius:0;clip-path:CP}
/* code tape: a white flight strip */
§ .codes{--bb:#fff;color:#2A2230;border-top:1px solid rgba(20,18,22,.08);background-image:FOUR;background-size:100% 3px;background-repeat:no-repeat;background-position:0 100%}
§ .codes b{background:#FBF6EF;border:1px solid rgba(20,18,22,.14);color:#155E92;border-radius:4px}
§ .codes .mq-i::after{background:#FA1896}
/* desk band */
§ .deskphoto{border-radius:14px}
§ .readfirst{border:1px solid rgba(20,18,22,.1);border-left:3px solid #7149C9;border-radius:10px}
§ .filters{border:1px solid rgba(20,18,22,.12);border-radius:14px;box-shadow:SH}
§ .filters::before{height:3px;background:linear-gradient(90deg,#FA1896 0 40%,#12834E 40% 55%,#E8590C 55% 70%,#7149C9 70% 85%,#1E78B8 85%)}
§ .find input{border:1px solid rgba(20,18,22,.22);border-radius:10px}
/* rail: a pass with a coloured stub on top */
§ .grp{background:tperfG,linear-gradient(var(--c),var(--c)) left 0 top 0/100% GHpx no-repeat,#fff;color:INK2;border:0;border-radius:12px;box-shadow:none;padding-top:19px;GRPMASK}
§ .grp::before{content:"FO " counter(grp,decimal-leading-zero);font:600 12px/14px var(--mono);letter-spacing:.16em;color:#fff;opacity:1;margin:0 0 41px}
§ .grp h2{color:INK2}
§ .grp .grp-n{background:color-mix(in srgb,var(--c) 11%,#fff);color:var(--cd)}
§ .grp-disc{color:#5B5160;opacity:1}
§ .grid .lane{border-top-color:rgba(20,18,22,.08)}
§ .lane{filter:drop-shadow(0 12px 14px rgba(20,18,22,.07))}
§ .grp[data-grp=nuggets]{background:tperfG,linear-gradient(160deg,#F2CF6E,#C48F2C) left 0 top 0/100% GHpx no-repeat,#FFF9E6;color:#3B2604;box-shadow:none}
§ .grp[data-grp=nuggets]::before{color:#3B2604}
§ .grp[data-grp=nuggets] h2{text-shadow:none}
§ .grp[data-grp=checklist] .grp-n,§ .grp[data-grp=redflags] .grp-n{background:#FFE3F1;color:#A0105F}
/* cards */
§ .dk{border-radius:12px;border:1px solid rgba(20,18,22,.09);box-shadow:none}
§ .dk::before{height:3px}
§ .dk:hover{transform:translateY(-2px);box-shadow:none;border-color:color-mix(in srgb,var(--c) 45%,#fff)}
§ .dk-meta .time{border-radius:4px}
§ .grab{background:#fff!important;color:var(--cd);box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--c) 55%,#fff);border-radius:8px}
§ .grab:hover{background:var(--c)!important;color:#fff}
§ .dk details[open]>.grab{background:#fff!important;color:var(--cd)}
/* lead: white pass, coloured stub with flight tag, count and Grab it */
§ .dk.lead{background:LDPERF,linear-gradient(var(--c),var(--c)) right 0 top 0/LWpx 100% no-repeat,#fff;border:1px solid color-mix(in srgb,var(--c) 22%,#fff);color:INK2;padding-right:calc(LWpx + 30px);LDMASK}
§ .dk.lead::before{content:"FO " counter(grp,decimal-leading-zero);left:auto;right:0;top:24px;width:LWpx;height:auto;background:none;text-align:center;font:600 11px/1 var(--mono);letter-spacing:.16em;color:#fff;opacity:.92;z-index:1}
§ .dk.lead::after{right:0;left:auto;top:50%;bottom:auto;transform:translateY(-58%);width:LWpx;text-align:center;font:400 italic 104px/1 var(--isr);color:#fff;opacity:.95}
§ .dk.lead>details{position:static}
§ .dk.lead .grab{position:absolute;right:0;bottom:22px;width:calc(LWpx - 30px);margin-right:15px;justify-content:center;background:#fff!important;color:var(--cd);box-shadow:none}
§ .dk.lead .grab:hover{background:#FBF6EF!important;color:var(--cd)}
§ .dk.lead details[open]>.grab{background:#fff!important}
§ .dk.lead h3{color:INK2}
§ .dk.lead .love{color:#4A4350}
§ .dk.lead .dk-meta,§ .dk.lead .dk-meta .kind,§ .dk.lead .dk-meta .src{color:#6B6470}
§ .dk.lead .dk-meta .kind{color:var(--cd)}
§ .dk.lead .dk-meta .ic svg *{stroke:#2A1A22}
§ .dk.lead .dk-meta .time{background:#F3EEE8;color:INK2}
§ .dk.lead .chip{color:inherit}§ .dk.lead .chip.ex{background:#F3EEE8;color:INK2}
§ .dk.lead:hover{border-color:color-mix(in srgb,var(--c) 45%,#fff)}
§ .dk.gold.lead{animation:none;border:0;background:LDPERFG,GOLDSTUB right 0 top 0/LWpx 100% no-repeat,GOLDLEAD;padding-right:calc(LWpx + 30px);box-shadow:inset 0 2px 0 rgba(255,250,225,.9);LDMASK}
§ .dk.gold.lead::before{display:block;content:"FO " counter(grp,decimal-leading-zero);position:absolute;left:auto;right:0;top:24px;width:LWpx;height:auto;background:none;text-align:center;font:600 11px/1 var(--mono);letter-spacing:.16em;color:#FFF3D0;z-index:1}
§ .dk.gold.lead::after{right:0;left:auto;top:50%;bottom:auto;transform:translateY(-58%);width:LWpx;text-align:center;font:400 italic 104px/1 var(--isr);color:#FFF3D0;opacity:.95;text-shadow:none}
§ .dk.gold.lead>details{position:static}
§ .dk.gold.lead .grab{position:absolute;right:0;bottom:22px;width:calc(LWpx - 30px);margin-right:15px;justify-content:center;background:#FFF8E6!important;color:#5A3B08;box-shadow:none}
§ .dk.gold.lead .grab:hover{background:#fff!important;color:#5A3B08}
§ .dk.gold .grab{color:#7A5210;box-shadow:inset 0 0 0 1px #D9B45A}
§ .dk.gold .grab:hover{background:#C99A00!important;color:#fff}
§ .more-tile{border:1px dashed color-mix(in srgb,var(--c) 60%,#fff);color:var(--cd);border-radius:12px;background:#fff}
§ .more-tile:hover{background:var(--c);border-color:var(--c);color:#fff}
/* endnote: one wide pass, violet stub carries the signature */
§ .endnote{--bb:transparent;box-shadow:none;clip-path:none;border:0;border-image:none;max-width:1120px;margin:56px auto 0;padding:0;display:grid;grid-template-columns:minmax(0,1fr) EWpx;align-items:stretch;border-radius:14px;background:ENPERF,linear-gradient(#7149C9,#7149C9) right 0 top 0/EWpx 100% no-repeat,#fff;ENMASK}
§ .endnote p{color:INK2;text-align:left;margin:0;padding:44px 48px;max-width:none}
§ .endnote a{color:INK2}
§ .endnote .sign{color:#fff;align-self:center;justify-self:center;margin:0;padding:14px 12px 10px;line-height:1.15}
html.dir-c.ox .rdr-p{border-color:rgba(20,18,22,.14);border-radius:16px}
@media(max-width:1240px){§ .dk.lead h3{font-size:38px}}
@media(max-width:1100px){
 § .grp{background:lperfG,linear-gradient(var(--c),var(--c)) left 0 top 0/96px 100% no-repeat,#fff;padding:20px 22px 20px 0;GRPMASK2}
 § .grp[data-grp=nuggets]{background:lperfG,linear-gradient(160deg,#F2CF6E,#C48F2C) left 0 top 0/96px 100% no-repeat,#FFF9E6}
 § .grp::before{width:96px;text-align:center;margin:0;font-size:12px}
}
@media(max-width:860px){
 § .deskline .ck{border-top:0}
 § .dk.lead,§ .dk.gold.lead{padding-right:20px;padding-bottom:84px;LDMASKM}
 § .dk.lead{background:LDPERFM,linear-gradient(var(--c),var(--c)) left 0 bottom 0/100% 64px no-repeat,#fff}
 § .dk.gold.lead{background:LDPERFMG,GOLDSTUB left 0 bottom 0/100% 64px no-repeat,GOLDLEAD}
 § .dk.lead::before,§ .dk.gold.lead::before{top:auto;bottom:25px;right:auto;left:20px;width:auto;text-align:left}
 § .dk.lead::after,§ .dk.gold.lead::after{top:auto;bottom:12px;transform:none;right:auto;left:78px;width:auto;font-size:40px;text-align:left}
 § .dk.lead .grab,§ .dk.gold.lead .grab{bottom:14px;right:14px;margin:0;width:auto}
}
@media(max-width:640px){
 § .sig .av.mkv{width:26px;padding:0 14px}
 § .sig{SIGMASKM}
 § .sig>div{padding:10px 18px 10px 16px}
 § .pv{padding-right:calc(PWmpx + 12px);PVMASKM}
 § .pv2{background:PVPERFM,linear-gradient(#7149C9,#7149C9) right 0 top 0/PWmpx 100% no-repeat,#fff}
 § .pv3{background:PVPERFM,linear-gradient(#1E78B8,#1E78B8) right 0 top 0/PWmpx 100% no-repeat,#fff}
 § .pv1{background:PVPERFMG,GOLDSTUB right 0 top 0/PWmpx 100% no-repeat,GOLD}
 § .pv i{width:PWmpx;font-size:9px;letter-spacing:.1em}
 § .deskline{gap:8px}
 § .deskline span{padding:16px 14px 12px calc(30px + 14px);background:DLPERFM,linear-gradient(var(--sc),var(--sc)) left 0 top 0/30px 100% no-repeat,#fff;DLMASKM}
 § .deskline .ck{background:#FBF6EF;padding:30px 16px 12px}
 § .deskline .ck::before{left:16px;top:12px}
 § .deskline span:not(.ck)::before{width:30px;font-size:9px;letter-spacing:.12em}
 § .grp{-webkit-mask:none;mask:none;background:var(--c);color:#fff;border-radius:0;padding:22px 0 22px;border-bottom:0;box-shadow:0 0 0 100vmax var(--c)}
 § .grp::before{width:auto;text-align:left;margin:0 0 10px;color:#fff;opacity:.9}
 § .grp h2{color:#fff}
 § .grp .grp-n{background:rgba(255,255,255,.96);color:var(--cd)}
 § .grp-disc{color:#fff;opacity:.92}
 § .grp::after{display:block;content:"";position:absolute;left:0;right:0;bottom:0;top:auto;width:auto;height:2px;border:0;border-radius:0;box-shadow:none;background:linear-gradient(90deg,rgba(255,255,255,.7) 0 6px,transparent 6px 12px) 0 0/12px 2px repeat-x}
 § .grp[data-grp=nuggets]{background:#EDCB74;box-shadow:0 0 0 100vmax #EDCB74;color:#3B2604}
 § .grp[data-grp=nuggets]::before,§ .grp[data-grp=nuggets] h2,§ .grp[data-grp=nuggets] .grp-disc{color:#3B2604}
 § .grp[data-grp=nuggets]::after{background:linear-gradient(90deg,rgba(90,60,10,.45) 0 6px,transparent 6px 12px) 0 0/12px 2px repeat-x}
 § .lane{filter:none}
 § .endnote{grid-template-columns:minmax(0,1fr);margin:40px 0 0;background:ENPERFM,linear-gradient(#7149C9,#7149C9) left 0 bottom 0/100% 76px no-repeat,#fff;ENMASKM}
 § .endnote p{padding:30px 22px 26px;font-size:26px}
 § .endnote .sign{height:76px;display:flex;align-items:center;font-size:40px}
}
'''
SUB3B = {
 'SIGMASKM': vnotch('54px', 6), 'SIGMASK': vnotch('66px', 6),
 'PVMASKM': vnotch(f'calc(100% - {PWm}px)', 7), 'PVMASK': vnotch(f'calc(100% - {PW}px)', 8),
 'PVPERFMG': vperf(f'{PWm-2}px', 'rgba(255,243,208,.75)'), 'PVPERFM': vperf(f'{PWm-2}px'),
 'PVPERFG': vperf(f'{PW-2}px', 'rgba(255,243,208,.75)'), 'PVPERF': vperf(f'{PW-2}px'),
 'DLMASKM': vnotch('30px', 6), 'DLMASK': vnotch(f'{DS}px', 7),
 'DLPERFM': lperf('28px'), 'DLPERF': lperf(f'{DS-2}px'),
 'LDMASKM': hnotch('calc(100% - 64px)', 10), 'LDMASK': vnotch(f'calc(100% - {LW}px)', 11),
 'LDPERFMG': hperf('62px', 'rgba(255,243,208,.75)'), 'LDPERFM': hperf('62px'),
 'LDPERFG': vperf(f'{LW-2}px', 'rgba(255,243,208,.75)'), 'LDPERF': vperf(f'{LW-2}px'),
 'GRPMASK2': vnotch('96px', 8), 'GRPMASK': hnotch(f'{GH}px', 8),
 'tperfG': tperf(f'{GH-2}px'), 'lperfG': lperf('94px'),
 'ENMASKM': hnotch('calc(100% - 76px)', 11), 'ENMASK': vnotch(f'calc(100% - {EW}px)', 12),
 'ENPERFM': hperf('74px'), 'ENPERF': vperf(f'{EW-2}px'),
 'GOLDSTUB': GOLDSTUB, 'GOLDLEAD': GOLDLEAD, 'GOLD': GOLD, 'INK2': INK2, 'FOUR': FOUR,
 'PWmpx': f'{PWm}px', 'PWpx': f'{PW}px', 'DSpx': f'{DS}px', 'GHpx': f'{GH}px', 'LWpx': f'{LW}px', 'EWpx': f'{EW}px',
 'SH': SH,
}
for k in sorted(SUB3B, key=len, reverse=True):
    O3B = O3B.replace(k, SUB3B[k])
css3b = O3B.replace('.dk.lead', '.dk.lead:not(.gold)')
full3b = (BASE + css3b).replace('§', 'html.dir-c.o3b .desk').replace('html.dir-c.ox', 'html.dir-c.o3b').replace('CP', CP)
page('ffd-c-opt-3b.html', T, B, desc=DESC, src='freebies', tail=D.TAIL_C + D.SHARED_JS,
     headx=D.head('dir-c', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Instrument+Serif:ital@0;1',
                  D.C_CSS + full3b, 'window.FO_LIMIT=6;document.documentElement.classList.add("o3b");'))

# ---------------------------------------------------------------- 3c: option 3 matured v2, solid pillar-colour tickets
DK = lambda c, p=74: f'color-mix(in srgb,{c} {p}%,#1a0f1a)'
WP = 'rgba(255,255,255,.55)'
FH = 100  # calculator stub height
O3C = r'''
html.dir-c.ox .desk [data-cat],html.dir-c.ox .desk .grp{--cs:DKC}
/* eyebrow: a small blue ticket, pink chevron on the deep stub */
§ .eyebrow{background:LPEB,linear-gradient(#155A8C,#155A8C) left 0 top 0/39px 100% no-repeat,#1E78B8;color:#fff;border:0;border-image:none;border-radius:6px;padding:10px 16px 10px 0;gap:0;box-shadow:0 10px 22px -16px rgba(60,0,30,.8);EBMASK}
§ .eyebrow::before{width:14px;height:12px;margin:0 25px 0 12px;background:#FA1896;box-shadow:none;border-radius:0;clip-path:CP}
/* signature: violet ticket, pink chevron on the deep stub */
§ .sig{background:linear-gradient(#4A2896,#4A2896) left 0 top 0/66px 100% no-repeat,#7149C9;box-shadow:0 12px 24px -18px rgba(60,0,30,.8)}
§ .sig>div{background:linear-gradient(WP 0 5px,transparent 5px 10px) left 0 top 4px/1.5px 10px repeat-y}
§ .sig .sign{color:#fff}
§ .sig .role{color:#E4DAFF}
§ .lede .hl{background:#12834E;color:#fff!important}
/* calculator: green ticket, the button rides the deep stub */
§ .feat{background:FPERF,linear-gradient(#0D6A3E,#0D6A3E) left 0 bottom 0/100% FHpx no-repeat,#12834E;color:#fff;border-radius:14px;padding-bottom:23px;box-shadow:none;FMASK}
§ .feat h2,§ .feat p{color:#fff}
§ .feat p{color:rgba(255,255,255,.9)}
§ .feat .ic.big svg *{stroke:#fff}
§ .feat .ic.big{background:none!important}
§ .feat .ic.big svg rect{fill:rgba(255,255,255,.1)}
§ .feat .ic.big svg circle{fill:#fff}
§ .feat .ic.big svg circle[fill="#FA1896"]{fill:#FA1896;stroke:#FA1896}
§ .feat .chip,§ .feat .time{background:rgba(255,255,255,.14);color:#fff;border-color:rgba(255,255,255,.3)}
§ .feat .chip.ex,§ .feat .est{background:#FFE9A8;color:#4A3300}
§ .feat>*:has(+ .btnp){margin-bottom:48px}
§ .feat .btnp{background:#FA1896}
§ .feat:hover .btnp{background:#fff;color:#C80E70}
§ .vault{filter:drop-shadow(0 18px 18px rgba(90,0,45,.22))}
/* hero passes: solid colour bodies, deeper stubs */
§ .pv2{background:PVPERF,linear-gradient(#4E2C9E,#4E2C9E) right 0 top 0/PWpx 100% no-repeat,#7149C9;color:#fff}
§ .pv3{background:PVPERF,linear-gradient(#155A8C,#155A8C) right 0 top 0/PWpx 100% no-repeat,#1E78B8;color:#fff}
§ .pv2 b,§ .pv3 b{color:rgba(255,255,255,.88)}
§ .pv2 span,§ .pv3 span{color:#fff}
/* stats: solid pillar tickets, deeper stub, white type */
§ .deskline span{background:DLPERFW,linear-gradient(DKSC,DKSC) left 0 top 0/DSpx 100% no-repeat,var(--sc);color:rgba(255,255,255,.88)}
§ .deskline b,§ .deskline span:first-child b{color:#fff!important}
§ .deskline .ck{background:DLPERFW,linear-gradient(#4E0833,#4E0833) left 0 top 0/DSpx 100% no-repeat,#6E0F4A;color:#FFD3EA;padding-left:calc(DSpx + 20px);DLMASK}
§ .deskline .ck::before{left:13px;top:50%;margin-top:-6px}
/* code tape: blue, as in option 3 */
§ .codes{--bb:#1E78B8;color:#fff;border-top:0;background-image:FOUR;background-size:100% 3px}
§ .codes b{background:#155A8C;border:1px solid rgba(255,255,255,.28);color:#fff}
§ .codes .mq-i::after{background:#FA1896}
§ .filters{border:1px solid rgba(113,73,201,.4)}
/* rail: whole card colour, deeper top stub */
§ .grp{background:tperfW,linear-gradient(var(--cs),var(--cs)) left 0 top 0/100% GHpx no-repeat,var(--c);color:#fff}
§ .grp h2{color:#fff}
§ .grp .grp-n{background:#fff;color:var(--cd)}
§ .grp-disc{color:rgba(255,255,255,.88)}
§ .grp[data-grp=nuggets]{background:tperfG,linear-gradient(#A97A1E,#A97A1E) left 0 top 0/100% GHpx no-repeat,linear-gradient(160deg,#F2CF6E,#D9A83F 60%,#C9962E);color:#3B2604}
§ .grp[data-grp=nuggets]::before{color:#FFF3D0}
§ .grp[data-grp=nuggets] h2{color:#2E1D04}
§ .grp[data-grp=nuggets] .grp-disc{color:#3B2604}
§ .grp[data-grp=nuggets] .grp-n{background:#FFF8E6;color:#6B4808}
§ .grp[data-grp=checklist] .grp-n,§ .grp[data-grp=redflags] .grp-n{background:#fff;color:#A0105F}
/* cards: white content cards, filled pillar Grab it */
§ .dk::before{height:4px}
§ .grab{background:var(--c)!important;color:#fff;box-shadow:none}
§ .grab:hover{background:var(--cs)!important;color:#fff}
§ .dk details[open]>.grab{background:var(--cs)!important;color:#fff}
§ .dk.gold .grab{background:#B8862E!important;color:#fff;box-shadow:none}
§ .dk.gold .grab:hover{background:#946A1C!important}
/* lead: whole card colour, deeper stub with tag, count and Grab it */
§ .dk.lead{background:LDPERFW,linear-gradient(var(--cs),var(--cs)) right 0 top 0/LWpx 100% no-repeat,var(--c);border:0;color:#fff}
§ .dk.lead h3{color:#fff}
§ .dk.lead .love{color:rgba(255,255,255,.9)}
§ .dk.lead .dk-meta,§ .dk.lead .dk-meta .kind,§ .dk.lead .dk-meta .src{color:rgba(255,255,255,.85)}
§ .dk.lead .dk-meta .kind{color:#fff}
§ .dk.lead .dk-meta .ic svg *{stroke:#fff}
§ .dk.lead .dk-meta .ic svg rect,§ .dk.lead .dk-meta .ic svg path{fill:transparent}
§ .dk.lead .dk-meta .time{background:rgba(255,255,255,.16);color:#fff}
§ .dk.lead .chip,§ .dk.lead .chip.ex{background:rgba(255,255,255,.16);color:#fff}
§ .dk.lead .grab{background:#fff!important;color:var(--cs)}
§ .dk.lead .grab:hover{background:#FBF6EF!important;color:var(--cs)}
§ .dk.lead details[open]>.grab{background:#fff!important;color:var(--cs)}
§ .dk.lead:hover{border:0}
§ .more-tile{border:1.5px solid var(--c);color:var(--cd)}
/* endnote: violet ticket, deeper stub carries the signature */
§ .endnote{background:ENPERFW,linear-gradient(#4E2C9E,#4E2C9E) right 0 top 0/EWpx 100% no-repeat,#7149C9;filter:drop-shadow(0 18px 20px rgba(60,20,90,.22))}
§ .endnote p,§ .endnote a{color:#fff}
§ .endnote a{text-decoration-color:#FFB3DA}
@media(max-width:1100px){
 § .grp{background:lperfW,linear-gradient(var(--cs),var(--cs)) left 0 top 0/96px 100% no-repeat,var(--c)}
 § .grp[data-grp=nuggets]{background:lperfG,linear-gradient(#A97A1E,#A97A1E) left 0 top 0/96px 100% no-repeat,linear-gradient(160deg,#F2CF6E,#D9A83F 60%,#C9962E)}
}
@media(max-width:860px){
 § .dk.lead{background:LDPERFMW,linear-gradient(var(--cs),var(--cs)) left 0 bottom 0/100% 64px no-repeat,var(--c)}
}
@media(max-width:640px){
 § .pv2{background:PVPERFM,linear-gradient(#4E2C9E,#4E2C9E) right 0 top 0/PWmpx 100% no-repeat,#7149C9}
 § .pv3{background:PVPERFM,linear-gradient(#155A8C,#155A8C) right 0 top 0/PWmpx 100% no-repeat,#1E78B8}
 § .sig{background:linear-gradient(#4A2896,#4A2896) left 0 top 0/54px 100% no-repeat,#7149C9}
 § .deskline span{background:DLPERFMW,linear-gradient(DKSC,DKSC) left 0 top 0/30px 100% no-repeat,var(--sc)}
 § .deskline .ck{background:DLPERFMW,linear-gradient(#4E0833,#4E0833) left 0 top 0/30px 100% no-repeat,#6E0F4A;padding:16px 14px 14px 44px;DLMASKM}
 § .deskline .ck::before{left:8px}
 § .grp{background:var(--c)}
 § .grp[data-grp=nuggets]{background:#EDCB74}
 § .endnote{background:ENPERFMW,linear-gradient(#4E2C9E,#4E2C9E) left 0 bottom 0/100% 76px no-repeat,#7149C9}
}
'''
SUB3C = dict(SUB3B)
SUB3C.update({
 'DKSC': DK('var(--sc)'), 'DKC': DK('var(--c)'),
 'LPEB': lperf('38px', WP), 'EBMASK': vnotch('39px', 5),
 'FPERF': hperf(f'{FH-2}px', WP), 'FMASK': hnotch(f'calc(100% - {FH}px)', 10), 'FHpx': f'{FH}px',
 'PVPERF': vperf(f'{PW-2}px', WP), 'PVPERFM': vperf(f'{PWm-2}px', WP),
 'DLPERFW': lperf(f'{DS-2}px', WP), 'DLPERFMW': lperf('28px', WP),
 'tperfW': tperf(f'{GH-2}px', WP), 'lperfW': lperf('94px', WP),
 'LDPERFW': vperf(f'{LW-2}px', WP), 'LDPERFMW': hperf('62px', WP),
 'ENPERFW': vperf(f'{EW-2}px', WP), 'ENPERFMW': hperf('74px', WP),
})
for k in sorted(SUB3C, key=len, reverse=True):
    O3C = O3C.replace(k, SUB3C[k])
css3c = (O3B + O3C).replace('.dk.lead', '.dk.lead:not(.gold)')
full3c = (BASE + css3c).replace('§', 'html.dir-c.o3c .desk').replace('html.dir-c.ox', 'html.dir-c.o3c').replace('CP', CP)
page('ffd-c-opt-3c.html', T, B, desc=DESC, src='freebies', tail=D.TAIL_C + D.SHARED_JS,
     headx=D.head('dir-c', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Instrument+Serif:ital@0;1',
                  D.C_CSS + full3c, 'window.FO_LIMIT=6;document.documentElement.classList.add("o3c");'))

# ---------------------------------------------------------------- 3d/3e/3f: palette discipline variants of 3c
PILLAR = {'credit': '#1E78B8', 'myths': '#1E78B8', 'playbook': '#7149C9', 'deadlines': '#7149C9', 'gutcheck': '#E8590C',
          'travel': '#E8590C', 'script': '#12834E', 'decoder': '#12834E', 'checklist': '#A0105F', 'redflags': '#A0105F', 'sheet': '#FA1896'}
SCP = ['#12834E', '#E8590C', '#7149C9', '#1E78B8']
def pal_css(hb, hs, steps, ckb, cks, tape, chip, enb, ens, grid=None, pv3=None, pt=WP):
    """hero body/stub, stats body steps, check cell, codes tape, endnote, optional mono grid (body, stub)"""
    c = []
    a = c.append
    def tk(perf, stub, pos, body): return f'{perf},linear-gradient({stub},{stub}) {pos} no-repeat,{body}'
    a(f'§ .eyebrow{{background:{tk(lperf("38px", pt), hs, "left 0 top 0/39px 100%", hb)}}}')
    a(f'§ .sig{{background:linear-gradient({hs},{hs}) left 0 top 0/66px 100% no-repeat,{hb}}}')
    a(f'§ .lede .hl{{background:{hb}}}')
    a(f'§ .readfirst{{border-left-color:{hb}}}')
    a('§ .grp:not([data-grp=nuggets]) .grp-n,§ .grp:not([data-grp=nuggets]) .grp-n *{background:rgba(255,255,255,.1);color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.38)}')
    a('§ .grp:not([data-grp=nuggets]) .grp-n *{background:none;box-shadow:none}')
    a(f'§ .feat{{background:{tk(hperf(f"{FH-2}px", pt), hs, f"left 0 bottom 0/100% {FH}px", hb)}}}')
    p3b, p3s = pv3 or (hb, hs)
    a(f'§ .pv2{{background:{tk(vperf(f"{PW-2}px", pt), hs, f"right 0 top 0/{PW}px 100%", hb)}}}')
    a(f'§ .pv3{{background:{tk(vperf(f"{PW-2}px", pt), p3s, f"right 0 top 0/{PW}px 100%", p3b)}}}')
    for i, (s, pc) in enumerate(zip(steps, SCP), 1):
        a(f'§ .deskline span:nth-child({i}){{--sc:{s};--pc:{pc}}}')
    a(f'§ .deskline span{{background:{tk(lperf(f"{DS-2}px", pt), DK("var(--sc)", 70), f"left 0 top 0/{DS}px 100%", "var(--sc)")}}}')
    a('§ .deskline span:not(.ck)::before{text-decoration:underline 2px var(--pc);text-underline-offset:4px}')
    a(f'§ .deskline .ck{{background:{tk(lperf(f"{DS-2}px", pt), cks, f"left 0 top 0/{DS}px 100%", ckb)}}}')
    a(f'§ .codes{{--bb:{tape};background-image:linear-gradient(rgba(255,255,255,.14),rgba(255,255,255,.14));background-size:100% 1px}}')
    a(f'§ .codes b{{background:{chip}}}')
    a(f'§ .endnote{{background:{tk(vperf(f"{EW-2}px", pt), ens, f"right 0 top 0/{EW}px 100%", enb)}}}')
    a('§ .dk.lead::before,§ .grp::before{text-decoration:underline 2px var(--pc,transparent);text-underline-offset:6px}')
    m1100, m860, m640 = [], [], []
    if grid:
        gb, gs = grid
        for k, v in PILLAR.items():
            a(f'§ [data-cat={k}],§ .grp[data-grp={k}]{{--c:{gb};--cs:{gs};--pc:{v};--cd:{gb}}}')
        a('§ .dk-meta .kind{color:color-mix(in srgb,var(--pc,var(--c)) 86%,#1a0f1a)}')
        a('§ .dk.lead .dk-meta .kind{color:#fff}')
    else:
        for k, v in PILLAR.items():
            a(f'§ [data-cat={k}],§ .grp[data-grp={k}]{{--pc:transparent}}')
    m640 += [f'§ .pv2{{background:{tk(vperf(f"{PWm-2}px", pt), hs, f"right 0 top 0/{PWm}px 100%", hb)}}}',
             f'§ .pv3{{background:{tk(vperf(f"{PWm-2}px", pt), p3s, f"right 0 top 0/{PWm}px 100%", p3b)}}}',
             f'§ .sig{{background:linear-gradient({hs},{hs}) left 0 top 0/54px 100% no-repeat,{hb}}}',
             f'§ .deskline span{{background:{tk(lperf("28px", pt), DK("var(--sc)", 70), "left 0 top 0/30px 100%", "var(--sc)")}}}',
             f'§ .deskline .ck{{background:{tk(lperf("28px", pt), cks, "left 0 top 0/30px 100%", ckb)}}}',
             f'§ .endnote{{background:{tk(hperf("74px", pt), ens, "left 0 bottom 0/100% 76px", enb)}}}']
    return '\n'.join(c) + '\n@media(max-width:640px){\n' + '\n'.join(m640) + '\n}\n'

PALS = [
 ('3d', 'Palette A', 'One deep partner', 'Pink hero plus one deep aubergine for every solid block, tonal stubs, gold as the single accent; pillar colours shrink to the kind labels and the FO-number underline.',
  pal_css('#4A1A47', '#33102F', ['#3E1440', '#4A1A47', '#57214F', '#642A5C'], '#3E1440', '#2C0D2A', '#4A1A47', '#33102F', '#4A1A47', '#33102F', grid=('#4A1A47', '#33102F'))),
 ('3e', 'Palette B', 'Section-coded', 'Each section owns one pillar colour in tonal shades only: the hero and stats in deep violet, each desk lane in its own pillar from rail to lead, never two pillars side by side.',
  pal_css('#5B36B0', '#43248C', ['#3F2286', '#4A2A99', '#5531AA', '#6139BB'], '#371D78', '#2B165F', '#4A2A99', '#371D78', '#5B36B0', '#43248C')),
 ('3f', 'Palette C', 'Pink tonal + one pillar', 'Blocks in deep raspberry and wine drawn from the hero pink, stubs a shade deeper, with Learn blue as the one sparing secondary on the code tape and cheat sheet, plus gold.',
  pal_css('#7C0B45', '#5A0732', ['#640939', '#740A42', '#850C4B', '#960E55'], '#5A0732', '#430526', '#1E78B8', '#155A8C', '#8E0D50', '#650838', grid=('#A3105C', '#7C0B45'), pv3=('#1E78B8', '#155A8C'))),
]
for n, k, name, pitch, extra in PALS:
    css = (O3B + O3C + extra).replace('.dk.lead', '.dk.lead:not(.gold)')
    full = (BASE + css).replace('§', f'html.dir-c.o{n} .desk').replace('html.dir-c.ox', f'html.dir-c.o{n}').replace('CP', CP)
    page(f'ffd-c-opt-{n}.html', T, B, desc=DESC, src='freebies', tail=D.TAIL_C + D.SHARED_JS,
         headx=D.head('dir-c', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Instrument+Serif:ital@0;1',
                      D.C_CSS + full, f'window.FO_LIMIT=6;document.documentElement.classList.add("o{n}");'))

# ---------------------------------------------------------------- 3g: Palette A refined (full mark only, benefit-led cheat sheet, balanced shelves)
MARK = 'img/fo-chevron-transparent.png'
MK = f'url({MARK}) center/contain no-repeat'
O3G = f'''
/* the full First Officer mark wherever a single cut chevron used to sit */
§ .eyebrow::before{{clip-path:none;background:{MK};width:13px;height:18px}}
§ .pv b::before{{clip-path:none;background:{MK};width:8px;height:11px}}
§ .deskline .ck::before{{clip-path:none;background:{MK};width:14px;height:19px}}
§ .codes .mq-i::after{{clip-path:none;background:{MK};width:8px;height:11px;opacity:1}}
§ .dk.lead .dk-meta .ic svg circle{{fill:transparent}}
/* between phone and wide desktop the side tickets wrap tall and stretched the calculator, leaving a hole above its button:
   stack the calculator on top at its natural height, the nugget pack full width under it, the other two side by side */
@media(min-width:641px) and (max-width:1240px){{
 § .vault{{grid-template-columns:1fr 1fr;gap:14px;align-items:start}}
 § .vault>.feat{{grid-column:1/-1;order:0}}
 § .vault>.pvs{{display:contents}}
 § .vault .pv1{{grid-column:1/-1;order:1}}
 § .vault .pv2,§ .vault .pv3{{order:2;align-self:stretch}}
}}
/* shelves with one or two cards, or a short last row, close up instead of leaving a hole */
@media(min-width:861px){{
 § .grid .shelf[data-vis="1"]>.dk.lead{{grid-column:1/-1;grid-row:auto}}
 § .grid .shelf[data-vis="2"]>.dk.lead{{grid-row:auto}}
 § .grid .shelf[data-r3="1"]>.dk.lastvis{{grid-column:1/-1}}
 § .grid .shelf[data-r3="2"]>.dk.lastvis{{grid-column:span 2}}
}}
@media(min-width:641px) and (max-width:860px){{
 § .grid .shelf[data-r2="1"]>.dk.lastvis{{grid-column:1/-1}}
}}
'''
FILL_JS = r'''<script id="fo-fill">(function(){
function fill(){[].forEach.call(document.querySelectorAll('.desk .grid .shelf'),function(sh){
 var v=[].filter.call(sh.children,function(e){return e.classList.contains('dk')&&!e.hidden;});
 [].forEach.call(sh.querySelectorAll('.lastvis'),function(e){e.classList.remove('lastvis');});
 var n=v.length,lead=v.length&&v[0].classList.contains('lead');sh.setAttribute('data-vis',String(n));
 var r3='',r2='';if(n){if(lead){if(n>=4)r3=String((n-3)%3);r2=String((n-1)%2);}else{r3=String(n%3);r2=String(n%2);}v[n-1].classList.add('lastvis');}
 if(lead&&n<3)r3='';sh.setAttribute('data-r3',r3);sh.setAttribute('data-r2',r2);});}
var g=document.getElementById('desk-grid');if(!g)return;fill();
new MutationObserver(function(){clearTimeout(fill.t);fill.t=setTimeout(fill,30);}).observe(g,{subtree:true,attributes:true,attributeFilter:['hidden'],childList:true});
})();</script>'''
# the everyday cheat sheet leads with why an owner cares
CS_HERO_OLD = '<b>Cheat sheet</b><span>The everyday code sheet</span>'
CS_HERO_NEW = '<b>Cheat sheet</b><span>Spot the buys that miss your card&#8217;s bonus</span>'
CS_CARD_OLD = '<h3>The everyday code sheet</h3><p class="love">Twenty codes almost every business card meets in a year.</p>'
CS_CARD_NEW = ('<h3>Spot the buys that miss your card&#8217;s bonus</h3><p class="love">Your card pays its bonus on the code a store runs under, '
               'not on what you bought. The twenty codes almost every business card meets in a year, in plain words.</p>')
assert B.count(CS_HERO_OLD) == 1 and B.count(CS_CARD_OLD) == 1
B3G = B.replace(CS_HERO_OLD, CS_HERO_NEW).replace(CS_CARD_OLD, CS_CARD_NEW).replace(f'src="{CHEV}"', f'src="{MARK}"')
# sheet cards hold a table, so their item count came out as 0; count the code rows instead
import re as _re
def _fixn(h):
    out, i = [], 0
    for m in _re.finditer(r'data-n="0"', h):
        nxt = h.find('data-n="', m.end()); seg = h[m.end(): nxt if nxt > 0 else len(h)]
        k = seg.count('<tr><td')
        out.append(h[i:m.start()] + (f'data-n="{k}"' if k else m.group(0))); i = m.end()
    return ''.join(out) + h[i:]
B3G = _fixn(B3G)
CS_GRP_OLD = "<p class=\"grp-disc\">Codes and names from Visa's April 2026 manual. Each store's code is set by its processor.</p>"
CS_GRP_NEW = "<p class=\"grp-disc\">Your card's bonus follows the code a store runs under, not its name. Each store's code is set by its processor.</p>"
assert B3G.count(CS_GRP_OLD) == 1
B3G = B3G.replace(CS_GRP_OLD, CS_GRP_NEW)
pal3g = pal_css('#5A2257', '#43173F', ['#4D1B4A', '#57214F', '#612855', '#6B2F5E'], '#4D1B4A', '#3A1236', '#5A2257', '#43173F',
                '#5A2257', '#43173F', grid=('#5A2257', '#43173F'))
css3g = (O3B + O3C + pal3g + O3G).replace('.dk.lead', '.dk.lead:not(.gold)')
full3g = (BASE + css3g).replace('§', 'html.dir-c.o3g .desk').replace('html.dir-c.ox', 'html.dir-c.o3g').replace('CP', CP)
page('ffd-c-opt-3g.html', T, B3G, desc=DESC, src='freebies', tail=D.TAIL_C + D.SHARED_JS + FILL_JS,
     headx=D.head('dir-c', 'family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Instrument+Serif:ital@0;1',
                  D.C_CSS + full3g, 'window.FO_LIMIT=6;document.documentElement.classList.add("o3g");'))
_p = f'{ROOT}/ffd-c-opt-3g.html'; _s = open(_p, encoding='utf-8').read()
open(_p, 'w', encoding='utf-8').write(_s.replace(CHEV, MARK))

# ---------------------------------------------------------------- 3h: brand palette (cream canvas, First Officer pink tickets, flat gold, ink type)
# every colour below is a token from assets/fo-site-tokens.css or assets/fo-v4.css; no purple anywhere
BP, BPS, BPK = '#E60F86', '#B30A68', '#FA1896'          # --pink2 block, --pinkdeep stub, --pink accent
BCR, BCR2, BTR, BPL = '#FAF6EE', '#FBF4E6', '#F1EADB', '#F1D6E5'   # --bg, --cream2, --track, --pinkLine
BG, BG2, BINK, BINK2 = '#E8C547', '#F5B700', '#141216', '#3A343D'  # --gold, --gold2, --ink, --ink2
EYEBROW = (BPK, '#fff')  # wide pink brush (shape D), white text; see EB_BRUSH
GP = 'rgba(255,255,255,.7)'      # perforation on gold
# the site's existing hand-painted highlighter brush (the 'No affiliate links' trust line), reused verbatim
import re as _re3h
HLB = _re3h.search(r'\.desk \.hl\{background:(url\("[^"]+"\))', D.F.SRC).group(1)
assert '%23FA1896' in HLB
import desk_clean as _dc
BRUSH = _dc.brush(BPK)
CPF = 'rgba(230,15,134,.42)'     # perforation on cream
def _tk(perf, stub, pos, body): return f'{perf},linear-gradient({stub},{stub}) {pos} no-repeat,{body}'
O3H = f'''
html.dir-c.o3h{{--isr:'DM Serif Display',Georgia,serif}}
/* canvas: the approved pages' cream with a hairline grid, ink type, pink second line */
html.dir-c.o3h .desk .pop-hero{{--bb:{BCR};color:{BINK}}}
html.dir-c.o3h .desk .pop-hero::before{{background:linear-gradient(rgba(20,18,22,.045) 1px,transparent 1px) 0 0/44px 44px,linear-gradient(90deg,rgba(20,18,22,.045) 1px,transparent 1px) 0 0/44px 44px,{BCR}}}
§ h1{{font-family:'DM Serif Display',Georgia,serif;font-weight:400;color:{BINK};text-shadow:none;letter-spacing:-.025em;line-height:.92}}
§ h1 em{{font-family:'DM Serif Display',Georgia,serif;font-style:normal;color:{BPK}}}
/* brand rule: serif headlines, two lines, pink second line, NO italics anywhere (h1, caption, big counts, quotes) */
§ *,§ *::before,§ *::after,html.dir-c.o3h .rdr-p,html.dir-c.o3h .rdr-p *{{font-style:normal!important}}
§ .lede{{color:{BINK2}}}
/* one bold brush swipe (Ohad, Oct 26): solid #FA1896, ink text on top;
   padding = -margin so the swipe overhangs the words instead of adding a gap */
§ .hl,§ .lede .hl{{background:{BRUSH}!important;color:{BINK}!important;border-radius:0;padding:.1em .28em .12em;margin:0 -.28em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
html.dir-c.o3h .fzmk{{display:none}}
html.dir-c.o3h .fz>span{{background:{BRUSH};padding:.1em .28em .12em;margin:0 -.28em}}
/* no Checked cell any more: four even stats, two by two on phones */
§ .deskline{{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media(max-width:640px){{§ .deskline{{grid-template-columns:1fr 1fr}}}}
/* the mark only ever sits on ticket-stock cream: eyebrow stub, signature stub, code tape */
§ .eyebrow{{background:{_tk(lperf("38px", CPF), BCR2, "left 0 top 0/39px 100%", BP)};color:#fff;box-shadow:inset 0 0 0 1px {BPL},0 10px 22px -16px rgba(179,10,104,.55)}}
§ .sig{{background:linear-gradient({BCR2},{BCR2}) left 0 top 0/66px 100% no-repeat,{BP};box-shadow:inset 0 0 0 1px {BPL};border-top:0}}
§ .sig .av{{background:none;box-shadow:none}}
§ .sig .sign,§ .sig .role{{color:#fff}}
§ .deskline .ck{{background:{_tk(lperf(f"{DS-2}px", CPF), BTR, f"left 0 top 0/{DS}px 100%", BCR2)};box-shadow:inset 0 0 0 1px {BPL}}}
§ .deskline .ck,§ .deskline .ck *{{color:{BINK}}}
§ .deskline span:not(.ck){{background:{_tk(lperf(f"{DS-2}px", WP), BPS, f"left 0 top 0/{DS}px 100%", BP)}}}
§ .deskline span:not(.ck)::before{{text-decoration-color:rgba(255,255,255,.75)}}
§ .codes{{--bb:{BTR};color:{BINK};background-image:linear-gradient({BPL},{BPL});background-size:100% 1px}}
§ .codes b{{background:transparent;border:1px solid rgba(20,18,22,.24);color:{BINK}}}
/* calculator: pink ticket, white action like the pink band on the approved pages */
§ .feat .btnp{{background:#fff;color:{BPS}}}
§ .feat:hover .btnp{{background:{BCR2};color:{BPS}}}
§ .feat .ft-k{{background:transparent;color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.7)}}
/* the two side tickets are pink, so they carry no mark */
§ .pv2 b::before,§ .pv3 b::before{{display:none}}
/* Golden Nugget Pack: flat brand gold, no metal gradient, no sheen */
§ .pv1{{background:{_tk(vperf(f"{PW-2}px", GP), BG2, f"right 0 top 0/{PW}px 100%", BG)};border:0;box-shadow:none}}
§ .pv1::before{{display:none;animation:none}}
§ .pv1 b,§ .pv1 span{{color:{BINK}}}
§ .pv1 i{{color:{BINK};opacity:.85}}
§ .dk.gold.lead{{background:{_tk(vperf(f"{LW-2}px", GP), BG2, f"right 0 top 0/{LW}px 100%", BG)};box-shadow:none}}
§ .dk.gold.lead::before,§ .dk.gold.lead::after{{color:{BINK}}}
§ .dk.gold.lead::after{{opacity:.8}}
§ .dk.gold.lead h3,§ .dk.gold.lead .love,§ .dk.gold.lead .dk-meta,§ .dk.gold.lead .dk-meta .kind,§ .dk.gold.lead .dk-meta .src{{color:{BINK}}}
§ .dk.gold.lead .dk-meta .time{{background:transparent;color:{BINK};box-shadow:inset 0 0 0 1px rgba(20,18,22,.3)}}
§ .grp[data-grp=nuggets] .grp-n *{{color:{BINK}}}
§ .dk.gold.lead .grab{{background:{BCR2}!important;color:{BINK}}}
§ .dk.gold.lead .grab:hover{{background:#fff!important;color:{BINK}}}
§ .dk.gold:not(.lead) .grab,§ .dk.gold:not(.lead) details[open]>.grab{{background:{BG2}!important;color:{BINK};box-shadow:none}}
§ .dk.gold:not(.lead) .grab:hover{{background:{BG}!important;color:{BINK}}}
§ .dk.gold:not(.lead)::before{{background:{BG}}}
§ .grp[data-grp=nuggets]{{background:{_tk(tperf(f"{GH-2}px", GP), BG2, f"left 0 top 0/100% {GH}px", BG)};color:{BINK}}}
§ .grp[data-grp=nuggets]::before,§ .grp[data-grp=nuggets] h2,§ .grp[data-grp=nuggets] .grp-disc{{color:{BINK}}}
§ .grp[data-grp=nuggets] .grp-n{{background:transparent;color:{BINK};box-shadow:inset 0 0 0 1px rgba(20,18,22,.35)}}
/* FO numbers and stat labels underline in white, not a pillar colour */
§ .dk.lead::before,§ .grp::before{{text-decoration-color:rgba(255,255,255,.7)}}
§ .grp[data-grp=nuggets]::before{{text-decoration-color:rgba(20,18,22,.5)}}
§ .filters::before{{background:{BPK}}}
§ .filters{{border-color:{BPL}}}
§ .endnote p,§ .endnote a,§ .endnote .sign{{color:#fff}}
§ .endnote a{{text-decoration-color:#fff}}
@media(max-width:1100px){{
 § .grp[data-grp=nuggets]{{background:{_tk(lperf("94px", GP), BG2, "left 0 top 0/96px 100%", BG)}}}
}}
@media(max-width:860px){{
 § .dk.gold.lead{{background:{_tk(hperf("62px", GP), BG2, "left 0 bottom 0/100% 64px", BG)}}}
}}
@media(max-width:640px){{
 § .sig{{background:linear-gradient({BCR2},{BCR2}) left 0 top 0/54px 100% no-repeat,{BP}}}
 § .deskline span:not(.ck){{background:{_tk(lperf("28px", WP), BPS, "left 0 top 0/30px 100%", BP)}}}
 § .deskline .ck{{background:{_tk(lperf("28px", CPF), BTR, "left 0 top 0/30px 100%", BCR2)}}}
 § .pv1{{background:{_tk(vperf(f"{PWm-2}px", GP), BG2, f"right 0 top 0/{PWm}px 100%", BG)}}}
 § .grp[data-grp=nuggets]{{background:{BG};box-shadow:0 0 0 100vmax {BG}}}
}}
'''
# ---------------------------------------------------------------- 3h final pass (Ohad, Oct 26): eyebrow tag, no chevron reuse, email capture
EB_BG, EB_FG = EYEBROW
EB_BRUSH = _dc.brush(BPK, cap='26px', full=True)  # Ohad pt189u: wide pink brush swipe behind the eyebrow, white text, no tag box
O3H2 = f'''
/* eyebrow: its own colour, a plain tag, no stub and no mark */
§ .eyebrow{{background:{EB_BRUSH}!important;color:#fff!important;-webkit-mask:none;mask:none;border:0;border-image:none;clip-path:none;border-radius:0;box-shadow:none;font:800 17px/20px 'DM Sans',system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;padding:18px 58px 19px 50px;margin:0 0 26px -10px;transform:rotate(-1.2deg);transform-origin:left center;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}}§ .lede .tl{{color:{BINK};font-weight:700;padding:0;margin:0;background:none}}
§ .eyebrow::before{{display:none}}
/* signature: Ohad and the role on a plain pink tag, no stub */
§ .sig{{background:{BP}!important;-webkit-mask:none!important;mask:none!important;padding:12px 22px 12px 20px;border-radius:10px;box-shadow:none}}
§ .sig>div{{padding:0!important;margin:0!important;background:none!important;border:0!important}}
/* kicker bullet and code-tape separator: a small square, never a chevron */
§ .pv b::before{{clip-path:none!important;background:{BPS}!important;width:6px!important;height:6px!important;border-radius:0!important;opacity:1}}
§ .codes .mq-i::after{{clip-path:none!important;background:{BPK}!important;width:5px!important;height:5px!important;border-radius:0!important;opacity:.85}}
/* email capture (mockup: the form posts nowhere) */
§ .cap{{margin:18px 0 0;max-width:480px}}
§ .cap-l{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
§ .cap-row{{display:flex;gap:8px}}
§ .cap input{{flex:1 1 auto;min-width:0;font:500 16px/1.2 'DM Sans',system-ui,sans-serif;color:{BINK};background:#fff;border:1.5px solid #E5DBE1;border-radius:12px;padding:13px 14px}}
§ .cap input:focus{{outline:2px solid {BPK};outline-offset:1px;border-color:{BPK}}}
§ .cap button{{flex:0 0 auto;font:700 15px/1 'DM Sans',system-ui,sans-serif;color:#fff;background:{BPK};border:0;border-radius:12px;padding:0 18px;cursor:pointer;white-space:nowrap}}
§ .cap button:hover{{background:{BPS}}}
§ .cap-m{{margin:8px 0 0;font-size:13px;line-height:1.4;color:{BINK2}}}
§ .cap-msg{{margin:8px 0 0;font-size:13px;font-weight:600;color:{BPS}}}§ .cap-msg:empty{{display:none}}
§ .cap.sent .cap-m{{display:none}}
html.dir-c.o3h #band{{background:var(--bg,#FAF6EE);padding-top:24px;padding-bottom:64px}}
html.dir-c.o3h #band .dr{{display:grid;grid-template-columns:220px minmax(0,1fr);max-width:1120px;margin:0 auto;border-radius:14px;overflow:hidden;background:rgba(250,24,150,.07);box-shadow:inset 0 0 0 1.5px rgba(250,24,150,.22)}}
html.dir-c.o3h #band .dr-stub{{background:{BP};color:#fff;padding:28px 22px;display:flex;flex-direction:column;justify-content:center;gap:10px;border-right:2px dashed rgba(255,255,255,.6)}}
html.dir-c.o3h #band .dr-k{{font:700 22px/1.1 'DM Sans',system-ui,sans-serif;letter-spacing:-.01em}}
html.dir-c.o3h #band .dr-f{{font:600 11px/1 'JetBrains Mono',monospace;letter-spacing:.18em;text-transform:uppercase;opacity:.9}}
html.dir-c.o3h #band .dr-main{{padding:30px 36px 32px}}
html.dir-c.o3h #band .dr-h{{font:800 26px/1.15 'DM Sans',system-ui,sans-serif;letter-spacing:-.02em;color:{BINK};margin:0}}
html.dir-c.o3h #band .dr-s{{margin:8px 0 0;font-size:15px;line-height:1.55;color:{BINK2};max-width:620px}}
html.dir-c.o3h #band .cap{{margin:16px 0 0;max-width:520px}}
html.dir-c.o3h #band .cap-l{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
html.dir-c.o3h #band .cap-row{{display:flex;gap:8px}}
html.dir-c.o3h #band .cap input{{flex:1 1 auto;min-width:0;font:500 16px/1.2 'DM Sans',system-ui,sans-serif;color:{BINK};background:#fff;border:1.5px solid rgba(250,24,150,.35);border-radius:12px;padding:13px 14px}}
html.dir-c.o3h #band .cap input:focus{{outline:2px solid {BPK};outline-offset:1px}}
html.dir-c.o3h #band .cap button{{flex:0 0 auto;font:700 15px/1 'DM Sans',system-ui,sans-serif;color:#fff;background:{BPK};border:0;border-radius:12px;padding:0 20px;cursor:pointer;white-space:nowrap}}
html.dir-c.o3h #band .cap button:hover{{background:{BPS}}}
html.dir-c.o3h #band .cap-msg{{margin:8px 0 0;font-size:13px;font-weight:600;color:{BPS}}}html.dir-c.o3h #band .cap-msg:empty{{display:none}}
@media(max-width:760px){{html.dir-c.o3h #band .dr{{grid-template-columns:1fr}}html.dir-c.o3h #band .dr-stub{{border-right:0;border-bottom:2px dashed rgba(255,255,255,.6);padding:18px 20px;flex-direction:row;align-items:baseline;justify-content:space-between;flex-wrap:wrap}}html.dir-c.o3h #band .dr-main{{padding:22px 20px 24px}}html.dir-c.o3h #band .dr-h{{font-size:22px}}}}
@media(max-width:420px){{html.dir-c.o3h #band .cap-row{{flex-direction:column}}html.dir-c.o3h #band .cap button{{padding:14px 18px}}}}
@media(max-width:420px){{§ .cap-row{{flex-direction:column}}§ .cap button{{padding:14px 18px}}}}
/* phone: the eyebrow is the page's header under the nav, sized for the phone, not shrunk; a painted stroke, never a button */
@media(max-width:640px){{§ .eyebrow{{font-size:15px;line-height:18px;letter-spacing:.08em;padding:16px 46px 17px 38px;margin:10px 0 22px -6px}}}}
/* hero photos: the Freebies hero's own rotating set (v3 #fftop), slow crossfade, low opacity, cream and pink tint */
§ .pop-hero>.phx{{display:block;position:absolute;top:-28px;bottom:0;left:50%;width:100vw;transform:translateX(-50%);z-index:0;background:transparent}}
§ .pop-hero>.phx img{{transform:scale(1);transition:opacity 1.4s ease-in-out,transform 8s linear;will-change:opacity,transform}}
§ .pop-hero>.phx img.on{{opacity:.52;transform:scale(1.07)}}
§ .pop-hero>.phx img[src$='i-desk.webp']{{object-position:62% 50%}}§ .pop-hero>.phx img[src$='e-coffee.webp']{{object-position:50% 38%}}§ .pop-hero>.phx img[src$='e-laptop.webp']{{object-position:55% 32%}}§ .pop-hero>.phx img[src$='e-tablet.webp']{{object-position:70% 40%}}
§ .pop-hero>.phx::after{{background:linear-gradient(90deg,rgba(250,246,238,.62) 0%,rgba(250,246,238,.46) 38%,rgba(255,227,241,.28) 70%,rgba(255,227,241,.20) 100%),linear-gradient(180deg,rgba(250,246,238,.7) 0,rgba(250,246,238,0) 80px,rgba(250,246,238,0) calc(100% - 120px),{BCR} 100%)}}
§ .pop-hero>.dhero,§ .pop-hero>.deskline{{position:relative;z-index:1}}
@media(max-width:760px){{§ .pop-hero>.phx{{bottom:auto;height:860px}}§ .pop-hero>.phx img.on{{opacity:.56}}§ .pop-hero>.phx img[src$='i-desk.webp']{{object-position:30% 50%}}§ .pop-hero>.phx img[src$='e-coffee.webp']{{object-position:40% 30%}}§ .pop-hero>.phx img[src$='e-laptop.webp']{{object-position:54% 30%}}§ .pop-hero>.phx img[src$='e-tablet.webp']{{object-position:68% 40%}}§ .pop-hero>.phx::after{{background:linear-gradient(180deg,rgba(250,246,238,.55) 0%,rgba(250,246,238,.42) 40%,rgba(250,246,238,.5) 70%,{BCR} 100%)}}}}
@media(prefers-reduced-motion:reduce){{§ .pop-hero>.phx img{{transition:none;transform:none}}§ .pop-hero>.phx img.on{{transform:none}}}}
/* the sign-off sits on the page: script name in pink, role in ink. No tile, no mark */
§ .sig{{display:block!important;background:none!important;box-shadow:none!important;-webkit-mask:none!important;mask:none!important;clip-path:none!important;border:0!important;border-radius:0!important;padding:0!important;margin-top:26px}}§ .sig::before,§ .sig::after{{display:none!important}}§ .sig>div{{background:none!important;padding:0!important;display:flex;flex-direction:column;gap:2px}}§ .sig .sign{{color:{BP}!important}}§ .sig .role{{color:{BINK}!important;opacity:1}}
html.dir-c.o3h #band{{position:relative;isolation:isolate}}html.dir-c.o3h #band>.phx{{display:block}}
/* Golden Nugget imagery: the desk's faceted nugget, flat */
§ .pv1 .nugart{{position:absolute!important;right:calc(var(--pw,46px) + 12px);bottom:14px;width:54px;height:54px;z-index:1;pointer-events:none}}
§ .pv1 span{{padding-right:58px}}
§ .grp[data-grp=nuggets]{{position:relative}}§ .grp[data-grp=nuggets] .nugart{{position:absolute;right:16px;top:44px;width:64px;height:64px;pointer-events:none}}§ .grp[data-grp=nuggets] h2{{padding-right:64px}}
§ #nug-cards .nugart{{display:none}}§ #nug-cards.lead .nugart{{display:block;position:absolute;right:164px;top:62px;width:104px;height:104px;pointer-events:none;z-index:1}}
@media(max-width:640px){{§ .pv1 .nugart{{width:52px;height:52px;top:14px;bottom:auto}}§ .pv1 span{{padding-right:0}}§ .grp[data-grp=nuggets] .nugart{{width:50px;height:50px;top:12px;right:12px}}§ #nug-cards.lead .nugart{{right:110px;top:auto;bottom:9px;width:48px;height:48px;z-index:2}}}}
'''
pal3h = pal_css(BP, BPS, [BP] * 4, BCR2, BTR, BTR, 'transparent', BP, BPS, grid=(BP, BPS))
css3h = (O3B + O3C + pal3h + O3G.replace(MK, 'none') + O3H + O3H2).replace('.dk.lead', '.dk.lead:not(.gold)')
# 3h: no chevron outside the logo, so the cut-chevron clip-path becomes none
full3h = (BASE + css3h).replace('§', 'html.dir-c.o3h .desk').replace('html.dir-c.ox', 'html.dir-c.o3h').replace('CP', 'none')
# brand type: DM Sans for display and body, DM Serif Display upright for headlines; sizes unchanged
full3h = full3h.replace("'Bricolage Grotesque',sans-serif", "'DM Sans',system-ui,sans-serif")
C3H = D.C_CSS.replace("'Bricolage Grotesque',sans-serif", "'DM Sans',system-ui,sans-serif").replace("--isr:'Instrument Serif',Georgia,serif", "--isr:'DM Serif Display',Georgia,serif")
B3H = B3G
page('ffd-c-opt-3h.html', T, B3H, desc=DESC, src='freebies', tail=D.TAIL_C + D.SHARED_JS + FILL_JS,
     headx=D.head('dir-c', 'family=DM+Serif+Display:ital@0;1', C3H + full3h, 'window.FO_LIMIT=6;document.documentElement.classList.add("o3h");'))
_p = f'{ROOT}/ffd-c-opt-3h.html'; _s = open(_p, encoding='utf-8').read()
_s = _s.replace(CHEV, MARK).replace("'Bricolage Grotesque',system-ui,sans-serif", "'DM Sans',system-ui,sans-serif").replace("'Bricolage Grotesque',sans-serif", "'DM Sans',system-ui,sans-serif")
assert 'Bricolage' not in _s and 'Founder, First Officer' not in _s
# no source names and no checked dates on 3h (Ohad, Oct 26); check() fails the build if any return
_s = _dc.check(_dc.desource(_s))
# signature without the chevron stub; then the email capture; then the chevron check
_s = _s.replace('<div class="sig"><img class="av mkv" src="img/fo-chevron-transparent.png" alt="" aria-hidden="true"><div>', '<div class="sig"><div>')
_s = _dc.nochev(_dc.capture(_s))
_s = _dc.hero_photos(_dc.nug_art(_s))
open(_p, 'w', encoding='utf-8').write(_s)

# ---------------------------------------------------------------- gallery
GAL = [('3h', 'Brand palette', 'Cream desk, First Officer pink tickets', 'Matured to the brand: the cream canvas, ink type and pink second line of the approved pages, every solid block in First Officer pink with a deeper pink tear-off stub, a flat brand-gold Golden Nugget Pack, a wide pink brush eyebrow, Daily Redemption sign-ups, and the mark only in the logo. No purple.'), ('3g', 'Palette A, refined', 'One deep partner, refined', 'Palette A taken further: a lifted aubergine that never reads as black, the full First Officer mark wherever a chevron appears, a cheat sheet that leads with why an owner cares, and shelves that close up with no holes.')] + [(n, k, name, pitch) for n, k, name, pitch, _ in PALS] + [('3c', 'Option 3, matured v2', 'Pillar blocks, matured v2', 'Solid pillar-colour blocks again, each cut as a tear-off ticket: notched perforation, a deeper stub with the flight-number tag and Grab it, white type on green, orange, violet and blue.'),
       ('3b', 'Option 3, matured', 'Pillar blocks, matured', 'The pillar colours move into tear-off stubs: notched boarding-pass cards with a dashed perforation, a flight-number tag and the Grab it action on a green, orange, violet or blue stub.')] + \
      [(n, f'Option {n}', name, pitch) for n, name, pitch, _ in OPTS]
cards = ''.join(f'''<article class="o"><a class="sh" href="ffd-c-opt-{n}.html"><img class="dt" src="img/ffd-opts/opt-{n}-1440.jpg" alt="{k} on desktop" loading="lazy"><img class="ph" src="img/ffd-opts/opt-{n}-390.jpg" alt="{k} on a phone" loading="lazy"></a>
<div class="tx"><span class="k">{k}</span><b>{name}</b><p>{pitch}</p><a class="go" href="ffd-c-opt-{n}.html">Open {k[0].lower()+k[1:]} <span aria-hidden="true">&rarr;</span></a></div></article>''' for n, k, name, pitch in GAL)
g = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Free From the Desk · direction C, five options · First Officer by UpNonStop</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{V4_FONTS}
<link rel="icon" href="{CHEV}">
<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#FAF6EE;color:#141216;font-family:'DM Sans',system-ui,sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}}
.w{{max-width:1240px;margin:0 auto;padding:40px 22px 70px}}
.brand{{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:#141216}}.brand img{{width:26px;height:auto}}.brand b{{display:block;font-weight:700;font-size:16px;line-height:1.1}}.brand small{{display:block;font-size:11.5px;color:#6b6470}}
.ey{{margin-top:30px;font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#b30a68;font-weight:600}}
h1{{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:clamp(36px,4.6vw,58px);line-height:1.02;letter-spacing:-.02em;margin:12px 0 14px;text-wrap:balance}}h1 em{{color:#FA1896}}
p.l{{font-size:17px;color:#3a343d;max-width:720px}}
.g{{display:grid;gap:22px;margin-top:30px}}
.o{{display:grid;grid-template-columns:minmax(0,1.9fr) minmax(0,1fr);background:#fff;border:1px solid #ece4e9;border-radius:18px;overflow:hidden}}
.sh{{position:relative;display:block;background:#F1E9EE;padding:18px 150px 18px 18px;min-height:300px}}
.sh .dt{{display:block;width:100%;border-radius:8px;box-shadow:0 14px 30px -20px rgba(20,18,22,.5)}}
.sh .ph{{position:absolute;right:18px;top:18px;width:120px;border-radius:14px;border:4px solid #fff;box-shadow:0 14px 30px -16px rgba(20,18,22,.55)}}
.tx{{display:flex;flex-direction:column;gap:8px;padding:24px}}
.k{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6b6470;font-weight:600}}
.tx b{{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:30px;line-height:1.1}}
.tx p{{color:#3a343d}}
.go{{margin-top:auto;align-self:flex-start;background:#FA1896;color:#fff;font-weight:700;padding:10px 18px;border-radius:99px;font-size:15px;text-decoration:none}}
.n{{margin-top:30px;font-size:13px;color:#6b6470}}.n a{{color:#141216}}
@media(max-width:900px){{.o{{grid-template-columns:minmax(0,1fr)}}.sh{{padding-right:110px;min-height:0}}.sh .ph{{width:84px}}}}</style></head><body><div class="w">
<a class="brand" href="home.html"><img src="{CHEV}" alt=""><span><b>First Officer</b><small>by UpNonStop&trade;</small></span></a>
<p class="ey">Free From the Desk &middot; direction C &middot; five options</p>
<h1>Same desk, no black, <em>five ways.</em></h1>
<p class="l">Same 490 items, search, filters, reading view, rail and shelves, and the same gold Golden Nugget card. Only the surfaces change.</p>
<div class="g">{cards}</div>
<p class="n">Mockups on branch mockups/rebuild-v4, not production. Direction C as it was: <a href="ffd-dir-c.html">ffd-dir-c</a>.</p>
</div></body></html>'''
open(f'{ROOT}/ffd-c-options.html', 'w').write(g); print('ffd-c-options.html', len(g))
