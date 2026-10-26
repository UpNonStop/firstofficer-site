# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from fosite import ROOT, V4_FONTS
PAGES = [
 ('free-from-the-desk.html','Free From the Desk','Freebies','The prior desk, all 490 items, 20 trades and 121 merchant codes, plus the reading view, live filter and search, and the sticky picker on phones.'),
 ('ffd-directions.html','Free From the Desk: three directions','Design directions','Editorial magazine, trading desk and bold brand pop: three bolder, busier takes on the same desk, filter and reader.'),
 ('home.html','Home','Product','The full home page in the prior design language: serif headlines, clear cards, solid pink buttons.'),
 ('for-dental.html','Dental practices','Specialized Industries','The industry page template, shown with dental.'),
 ('book.html','The Found Money Call','Book','The 20 minute call request page.'),
]
cards = ''.join(f'''<a class="g{' first' if i==0 else ''}" href="{h}"><span class="k">{k}</span><b>{t}</b><span class="d">{d}</span><span class="go">Open page <span aria-hidden="true">&rarr;</span></span></a>''' for i,(h,t,k,d) in enumerate(PAGES))
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>First Officer · rebuild v4 · mockup gallery</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{V4_FONTS}
<link rel="icon" href="img/fo-chevron-transparent-v2.png">
<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#FAF6EE;color:#141216;font-family:'DM Sans',system-ui,sans-serif;line-height:1.55;-webkit-font-smoothing:antialiased}}
.w{{max-width:1080px;margin:0 auto;padding:44px 22px 70px}}
.brand{{display:inline-flex;align-items:center;gap:10px;text-decoration:none;color:#141216}}.brand img{{width:26px;height:auto}}.brand b{{display:block;font-weight:700;font-size:16px;line-height:1.1}}.brand small{{display:block;font-size:11.5px;color:#6b6470}}
.ey{{margin-top:34px;font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#e60f86;font-weight:600}}
h1{{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:clamp(38px,5vw,60px);line-height:1.02;letter-spacing:-.02em;margin:12px 0 14px;text-wrap:balance}}h1 em{{color:#FA1896}}
p.l{{font-size:17px;color:#3a343d;max-width:640px;text-wrap:pretty}}
.gr{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:30px}}
.g{{display:flex;flex-direction:column;gap:8px;text-decoration:none;color:#141216;background:#fff;border:1.5px solid #ece4e9;border-radius:22px;padding:24px;box-shadow:0 14px 34px -26px rgba(20,18,22,.35);transition:transform .2s,border-color .2s}}
.g:hover{{transform:translateY(-3px);border-color:#f1d6e5}}
.g.first{{grid-column:1/-1;border-color:#f1d6e5;box-shadow:0 1px 0 #eadfe6,0 24px 60px -28px rgba(230,15,134,.32)}}
.g .k{{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#b30a68;font-weight:600}}
.g b{{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:28px;line-height:1.1}}
.g .d{{color:#3a343d;text-wrap:pretty;margin-bottom:10px}}
.g .go{{margin-top:auto;align-self:flex-start;background:#FA1896;color:#fff;font-weight:700;padding:10px 18px;border-radius:99px;font-size:15px}}
.n{{margin-top:30px;font-size:13px;color:#6b6470}}
@media(max-width:700px){{.gr{{grid-template-columns:minmax(0,1fr)}}.w{{padding:30px 18px 50px}}}}
@media(prefers-reduced-motion:reduce){{.g{{transition:none}}.g:hover{{transform:none}}}}</style></head><body><div class="w">
<a class="brand" href="home.html"><img src="img/fo-chevron-transparent-v2.png" alt=""><span><b>First Officer</b><small>by UpNonStop&trade;</small></span></a>
<p class="ey">Rebuild v4 &middot; mockups</p>
<h1>The prior look, <em>turned up.</em></h1>
<p class="l">Static mockups on a branch. Nothing here is live. Free From the Desk comes first.</p>
<div class="gr">{cards}</div>
<p class="n">Mockup gallery &middot; branch mockups/rebuild-v4 &middot; not production.</p>
</div></body></html>'''
open(f'{ROOT}/index-gallery.html','w').write(html); print('index-gallery.html', len(html))
