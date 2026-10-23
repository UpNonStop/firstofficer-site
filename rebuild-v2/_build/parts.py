import sys, json, html as H
sys.path.insert(0,'/workspace/fo-rebuild-mockups/_build')
import common as C
C.HERO_FONTS=C.HERO_FONTS.replace('&family=Inter:wght@400;500;600;700','')  # v2: no Inter (locked fonts)
WA=C.WA
APPROVED=C.APPROVED
TICK_HTML=open('/workspace/fo-rebuild-v2/_build/ticker.html').read().strip()
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
def ph(names, cls='', iv=7000):
    return f'<div class="phx {cls}" data-iv="{iv}" data-ph="{",".join("img/ph/"+n+".webp" for n in names)}" aria-hidden="true"></div>'
def rail(n, t):
    return f'<div class="rail"><b>{n}</b> {t}</div>'
def kk(t): return f'<div class="kk">{t}</div>'
def page(title, body, desc='', hero=False, src='site', extra_head='', tail=''):
    fonts = C.HERO_FONTS if hero else C.FONTS
    head_hero = ''
    if hero:
        head_hero = '<script>window.FO_SUBHEAD='+json.dumps(HERO_SUB)+';</script><style id="fo9hero">#top.dhero{padding:0!important;display:block}\n#top>#fohero{max-width:none!important;width:100%!important;margin:0!important;padding:0!important;position:relative!important;left:auto!important}</style>'
    scripts = '<script src="assets/fo.js"></script>' + ('<script src="hero/fo-hero-data.js"></script><script src="hero/fo-hero.js"></script>' if hero else '') + tail + '<script src="assets/v2.js"></script>'
    foot = C.footer('', True, src)
    # photo behind the newsletter capture
    foot = foot.replace('<section class="focap" id="focap">', '<section class="focap ps" id="focap">'+ph(['d-bali','bg-05','d-maldives'],'c'))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{H.escape(desc)}"><meta name="robots" content="noindex">
{FONTS}{fonts}<link rel="icon" href="img/fo-chevron-alpha.png"><link rel="stylesheet" href="assets/fo.css"><link rel="stylesheet" href="assets/v2.css">{head_hero}{extra_head}</head><body>
<!-- MOCKUP · First Officer rebuild v2 (showstopper pass) · static HTML, not production -->
{C.nav('', '')}
{TICK_HTML}
<main id="main">{body}</main>
{foot}
{scripts}</body></html>'''
HERO_SUB="Every loyalty program has their team constantly rewriting the rules. While you're busy running your business, your spend earns less than it should, and your points and miles buy less than they could.\n\nFirstOfficer by UpNonStop runs a desk of specialists across 50+ programs, each an expert in its niche. They all work for you, so you skip those rookie mistakes. Your Bespoke Strategy is reviewed weekly and optimized continuously, so every dollar you spend works harder.\n\nSame spend. More points. Better trips, for fewer points."
def seal_svg(size=150, idp='s'):
    return f'''<svg class="seal" viewBox="0 0 150 150" aria-label="$550 a month flat fee, cancel anytime"><defs><path id="{idp}c" d="M75,75 m-56,0 a56,56 0 1,1 112,0 a56,56 0 1,1 -112,0"/></defs>
<circle cx="75" cy="75" r="72" fill="#FA1896"/><circle cx="75" cy="75" r="66" fill="none" stroke="#fff" stroke-opacity=".35" stroke-dasharray="2 4"/>
<g class="ring"><text style="font:700 10.2px 'JetBrains Mono',monospace;letter-spacing:2.1px" fill="#fff"><textPath href="#{idp}c">CANCEL ANYTIME · TRAVEL PAID BY YOUR SPEND · </textPath></text></g>
<circle cx="75" cy="75" r="40" fill="#fff"/><text x="75" y="80" text-anchor="middle" style="font:400 30px 'DM Serif Display',serif" fill="#141216">$550</text><text x="75" y="96" text-anchor="middle" style="font:700 7.5px 'JetBrains Mono',monospace;letter-spacing:1.4px" fill="#c30d74">/ MO FLAT FEE</text></svg>'''
def miniseal():
    return '<svg class="miniseal" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" fill="#FA1896"/><circle cx="20" cy="20" r="13" fill="#fff"/><g fill="#fff">'+''.join(f'<circle cx="{20+16*__import__("math").cos(k*0.5236):.2f}" cy="{20+16*__import__("math").sin(k*0.5236):.2f}" r="1.3"/>' for k in range(12))+'</g><path d="M14 22l6-6 6 6M14 27l6-6 6 6" fill="none" stroke="#FA1896" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

DEST=[ # city, img, tag, pts, usual, desk, x, desk trip, taxes
 ('Lisbon','d-lisbon','Flights',120000,1200,7400,'6.2','Business class for 2','+$118'),
 ('Paris','d-paris','Combined',145000,1450,8900,'6.1','Flights and 4 nights','+$142'),
 ('Maldives','d-maldives','Hotels',120000,1200,6200,'5.2','5 nights, overwater villa','$0'),
 ('Rome','d-rome','Flights',140000,1400,5600,'4.0','Economy plus for 4','+$224'),
 ('Kyoto','d-kyoto','Hotels',150000,1500,5400,'3.6','6 nights, ryokan and city','$0'),
 ('Bali','d-bali','Hotels',105000,1050,4900,'4.7','7 nights, Ubud pool villa','$0'),
 ('New York','d-nyc','Hotels',60000,600,2850,'4.8','3 nights, Midtown, peak week','$0'),
 ('Barcelona','d-barcelona','Flights',102000,1020,6100,'6.0','Business class for 2','+$154'),
 ('Santorini','d-santorini','Combined',172000,1720,9400,'5.5','Flights and 6 nights','+$168'),
 ('Iceland','d-iceland','Combined',98000,980,4300,'4.4','Flights and 5 nights','+$96'),
 ('Dubai','d-dubai','Combined',168000,1680,8700,'5.2','Flights and 4 nights','+$204'),
 ('Connemara','d-connemara','Combined',88000,880,3900,'4.4','Flights and a week in the west','+$88'),
 ('The Alps','d-alps','Hotels',200000,2000,6800,'3.4','4 nights, chalet in peak week','$0'),
 ('Costa Rica','d-costarica','Hotels',96000,960,3900,'4.1','6 nights, jungle lodge and coast','$0'),
 ('Los Cabos','d-cabo','Combined',118000,1180,5700,'4.8','Flights and 5 nights','+$92'),
]
def story_card(d, more=False):
    city,img,tag,pts,us,dk,x,trip,tx=d
    w=us/dk*100
    return f'''<article class="sc{' more' if more else ''}" aria-label="{city}: {pts:,} points, about ${us:,} the usual way or about ${dk:,} estimated with your desk">
<div class="ph"><img src="img/ph/{img}.webp" alt="{city}" loading="lazy" decoding="async"><span class="tag">{tag}</span><div class="city"><b>{city}</b><span>{trip}</span></div></div>
<div class="bd"><div class="same">Same points</div><div class="ptsbig tnum"><span data-cu="{pts}">{pts:,}</span><i>pts</i></div>
<div class="fork">
<div class="way"><div class="wl"><span class="wn">The usual way</span><span class="wv tnum">≈ $<span data-cu="{us}">{us:,}</span></span></div><div class="ws">Statement credit, at 1¢ a point</div><div class="mt"><i style="--w:{w:.1f}%"></i></div></div>
<div class="way d"><div class="wl"><span class="wn">With your desk</span><span class="wv tnum">≈ $<span data-cu="{dk}" data-ms="2100">{dk:,}</span></span></div><div class="ws">{trip}, est.</div><div class="mt"><i style="--w:100%"></i></div></div>
</div>
<div class="mult"><b class="tnum"><span data-cu="{x}" data-d="1" data-ms="2300">{x}</span>x</b><span class="ml">more trip</span></div>
<div class="ft"><span class="estl">Estimated, illustrative</span><small>est. taxes {tx}</small></div></div></article>'''
