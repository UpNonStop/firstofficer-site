# Builds img/rec/app/strategy.webp: the Desk tab's strategy screen for Linden Row (Leo, the fictional example owner).
# The screen is the HTML below, rendered at 319x697 CSS px at 2x and set into img/rec/app/bezel.webp at (41,39),
# under a rounded mask, then saved as WebP at quality 88. Change a figure in the HTML, then run:
#   python3 recovered/build_strategy.py
# Needs Playwright with Chromium, and Pillow. JetBrains Mono loads from Google Fonts; Inter and the chevron are local.
import asyncio, os, tempfile
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'img/rec/app/strategy.webp')
BEZEL = os.path.join(ROOT, 'img/rec/app/bezel.webp')

HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&display=swap">
<style>
@font-face{font-family:Inter;src:url(%FONT%) format('woff2');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:319px;height:697px;overflow:hidden;background:#FAF7EF;font-family:Inter,system-ui,sans-serif;color:#2F2B33;-webkit-font-smoothing:antialiased}
.sb{height:40px;display:flex;align-items:center;justify-content:space-between;padding:6px 24px 0 26px;font-weight:600;font-size:15px}
.sb .ic{display:flex;align-items:center;gap:5px}
.sb svg{display:block}
.hd{display:flex;align-items:center;gap:9px;padding:8px 14px 0 14px;height:62px}
.hd img{width:30px;height:40px;object-fit:contain}
.hd b{display:block;font-size:21px;font-weight:800;letter-spacing:-.02em;line-height:1.05;color:#2F2B33}
.hd small{display:block;font-family:'JetBrains Mono',monospace;font-size:10.5px;font-weight:500;letter-spacing:.02em;color:#6B6672;margin-top:2px}
.hd .bt{margin-left:auto;display:flex;gap:8px}
.hd .bt i{width:30px;height:30px;border-radius:9px;background:#fff;box-shadow:0 0 0 1px rgba(47,43,51,.09),0 2px 6px rgba(47,43,51,.08);display:grid;place-items:center}
.hd .bt svg{width:16px;height:16px;fill:none;stroke:#2F2B33;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.st{display:flex;align-items:center;justify-content:space-between;padding:0 14px;height:28px;font-size:12.5px;color:#4A4550;background:#F6F2E8;border-top:1px solid rgba(47,43,51,.06);border-bottom:1px solid rgba(47,43,51,.06);margin-top:6px}
.st span{display:flex;align-items:center;gap:6px}
.st i{width:8px;height:8px;border-radius:2px;background:#16A06A;display:block}
.st em{font-style:normal;color:#8A8492}
.ct{padding:14px 14px 0}
.kk{display:flex;align-items:center;gap:7px;font-size:10.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#E3158A}
.kk i{width:14px;height:18px;display:grid;place-items:center}
.kk i img{width:11px;height:14px;object-fit:contain}
h1{font-size:26px;font-weight:800;letter-spacing:-.025em;line-height:1.1;margin:8px 0 2px}
h1 b{color:#FA1896;font-weight:800}
.sub{font-size:14.5px;font-weight:500;color:#4A4550;margin-bottom:10px}
.card{background:#fff;border-radius:14px;padding:9px 11px 10px;box-shadow:0 0 0 1px rgba(47,43,51,.07),0 6px 16px -10px rgba(47,43,51,.25);margin-bottom:8px}
.ch{display:flex;align-items:center;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#8A8492;margin-bottom:8px}
.ch b{color:#E3158A}
.ex{font-size:9.5px;font-weight:600;letter-spacing:.02em;text-transform:none;color:#8A6A12;background:#FFF7DB;border:1px solid #EAD48A;border-radius:999px;padding:2px 8px}
.grid{position:relative;display:grid;grid-template-columns:repeat(3,1fr);gap:4px}
.t{background:#F6F2E8;border-radius:9px;padding:5px 6px 6px;font-size:8.5px;line-height:1.25;color:#4A4550;min-height:40px}
.t small{display:block;font-size:7px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A8492;margin-bottom:2px}
.t.on{background:#FDE7F2;box-shadow:0 0 0 1.5px #FA1896;color:#2F2B33}
.t.on small{color:#E3158A}
.t.lit{background:#fff;box-shadow:0 0 0 1px #F7B6D8}
svg.ln{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible}
svg.ln path{fill:none;stroke:#FA1896;stroke-width:1.6;stroke-linecap:round;opacity:.9}
svg.ln circle{fill:#FA1896;stroke:#fff;stroke-width:1.5}
.rd{margin-top:7px;background:#FDE7F2;border-radius:10px;padding:7px 10px}
.rd small{display:block;font-size:8px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#E3158A}
.rd p{font-size:11px;line-height:1.4;color:#2F2B33;margin-top:2px;font-weight:500}
.sig{list-style:none}
.sig li{display:flex;align-items:center;gap:8px;padding:6px 0;border-top:1px solid rgba(47,43,51,.06);font-size:11px;color:#2F2B33;font-weight:500}
.sig li:first-child{border-top:0;padding-top:0}
.sig li b{flex:none;width:16px;height:16px;border-radius:5px;background:#E3F3EA;color:#12834E;display:grid;place-items:center;font-size:10px}
.sig li span{flex:1}
.sig li em{font-style:normal;font-size:9.5px;color:#8A8492}
.rv{display:flex;align-items:center;gap:9px}
.rv i{flex:none;width:28px;height:28px;border-radius:8px;background:#F6F2E8;display:grid;place-items:center}
.rv i svg{width:15px;height:15px;fill:none;stroke:#2F2B33;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.rv b{display:block;font-size:11.5px;font-weight:700}
.rv p{font-size:10.5px;line-height:1.35;color:#4A4550}
.lab{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#8A8492;margin:12px 0 7px}
.dn{display:flex;gap:9px;align-items:flex-start;padding:8px 0;border-top:1px solid rgba(47,43,51,.06)}
.dn:first-of-type{border-top:0;padding-top:0}
.dn i{flex:none;width:24px;height:24px;border-radius:7px;background:#FDE7F2;display:grid;place-items:center;color:#12834E;font-size:12px;font-weight:800;margin-top:2px}
.dn b{display:block;font-size:11.5px;font-weight:700;line-height:1.25}
.dn small{display:block;font-size:10px;color:#6B6672;margin-top:2px}
.dn em{flex:none;font-style:normal;font-size:8.5px;font-weight:700;letter-spacing:.06em;color:#12834E;background:#E3F3EA;border-radius:999px;padding:3px 7px;margin-top:3px}
.tb{position:absolute;left:0;right:0;bottom:0;height:62px;background:#FFFDF9;border-top:1px solid rgba(47,43,51,.08);display:flex;padding:7px 6px 0}
.tb div{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;font-size:10.5px;font-weight:500;color:#6F6A73}
.tb div svg{width:22px;height:22px;fill:none;stroke:#6F6A73;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.tb div img{width:19px;height:24px;object-fit:contain;margin-top:-1px}
.tb div.on{color:#FA1896;font-weight:700}
.hm{position:absolute;left:50%;bottom:5px;width:104px;height:4px;margin-left:-52px;border-radius:3px;background:#2F2B33}
</style></head><body>
<div class="sb"><span>9:41</span><span class="ic"><svg width="17" height="11" viewBox="0 0 17 11"><g fill="#2F2B33"><rect x="0" y="7" width="3" height="4" rx="1"/><rect x="4.5" y="5" width="3" height="6" rx="1"/><rect x="9" y="2.5" width="3" height="8.5" rx="1"/><rect x="13.5" y="0" width="3" height="11" rx="1"/></g></svg><svg width="16" height="11" viewBox="0 0 16 11"><path d="M1 3.5a10 10 0 0 1 14 0" fill="none" stroke="#2F2B33" stroke-width="1.6" stroke-linecap="round"/><path d="M4 6.5a6 6 0 0 1 8 0" fill="none" stroke="#2F2B33" stroke-width="1.6" stroke-linecap="round"/><circle cx="8" cy="9.5" r="1.3" fill="#2F2B33"/></svg><svg width="25" height="12" viewBox="0 0 25 12"><rect x="0.75" y="0.75" width="21" height="10.5" rx="3" fill="none" stroke="rgba(47,43,51,.5)" stroke-width="1.2"/><rect x="2.5" y="2.5" width="17.5" height="7" rx="1.5" fill="#34C759"/><path d="M23.3 4v4a2 2 0 0 0 0-4z" fill="rgba(47,43,51,.5)"/></svg></span></div>
<div class="hd"><img src="%CHEV%" alt=""><div><b>First Officer</b><small>by UpNonStop™</small></div><div class="bt"><i><svg viewBox="0 0 24 24"><path d="M6 17V11a6 6 0 0 1 12 0v6l2 2H4z"/><path d="M10 21h4"/></svg></i><i><svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg></i></div></div>
<div class="st"><span><i></i>Your desk is online</span><em>Updated 8:14 AM</em></div>
<div class="ct">
<div class="kk"><i><img src="%CHEV%" alt=""></i>Your strategy · behind the thread</div>
<h1>Linden Row’s strategy.</h1>
<p class="sub">What the desk is working on</p>
<div class="card"><div class="ch"><span>Strategy path · <b>Earn</b></span><span class="ex">Example</span></div>
<div class="grid">
<div class="t on"><small>Route</small>Lead-gen ads to the 4x card</div>
<div class="t on"><small>Vendor</small>Ad platforms typically code as 7311</div>
<div class="t on"><small>Cap</small>4x cap shared with software: rest to 3x</div>
<div class="t lit"><small>Earn</small>4x on the top two categories, first $150k a year</div>
<div class="t"><small>Rules</small>Award chart repricing announced for Q2</div>
<div class="t lit"><small>Transfer</small>Points to an airline partner, 1:1</div>
<svg class="ln" viewBox="0 0 297 84" preserveAspectRatio="none"><path d="M49 40 C 70 44, 78 44, 99 40 M99 40 C 130 44, 140 44, 148 40 M148 40 C 170 44, 190 44, 247 40"/><circle cx="49" cy="40" r="2.6"/><circle cx="148" cy="40" r="2.6"/><circle cx="247" cy="40" r="2.6"/></svg>
</div>
<div class="rd"><small>Waiting for your OK</small><p>Ads to the 4x card: about +$6,240 a year, est.</p></div></div>
<div class="card"><div class="ch"><span>Signals the desk reads</span><span>3 of 3</span></div>
<ul class="sig"><li><b>✓</b><span>Merchant codes, line by line</span><em>your statements</em></li><li><b>✓</b><span>Transfer bonuses this month</span><em>checked daily</em></li><li><b>✓</b><span>Statement cycle and caps</span><em>on a schedule</em></li></ul></div>
<div class="card"><div class="rv"><i><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg></i><div><b>Reviewed by a person, weekly</b><p>Every strategy change is approved by a person before it reaches your thread.</p></div></div></div>
<div class="lab"><span>Done</span><span>3</span></div>
<div class="dn"><i>✓</i><div><b>Agency software moved to the business points card</b><small>+$2,880 a year, confirmed by your statements</small></div><em>SEP 18</em></div>
<div class="dn"><i>✓</i><div><b>Carrier travel moved to the 3x card</b><small>+$1,920 a year, confirmed by your statements</small></div><em>OCT 2</em></div>
</div>
<div class="tb"><div class="on"><img src="%CHEV%" alt="">Desk</div><div><svg viewBox="0 0 24 24"><ellipse cx="12" cy="7" rx="7" ry="3"/><path d="M5 7v10c0 1.7 3.1 3 7 3s7-1.3 7-3V7"/><path d="M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/></svg>Earn</div><div><svg viewBox="0 0 24 24"><path d="M3 15l18-7-6 13-3-6-9 0z"/></svg>Burn</div><div><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h3.5a1.5 1.5 0 0 1 0 3h-2a1.5 1.5 0 0 0 0 3h3.5"/></svg>Return</div><div><svg viewBox="0 0 24 24"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.8.8 1 1.5 1 2.5h6c0-1 .2-1.7 1-2.5A6 6 0 0 0 12 3z"/></svg>Learn</div></div>
<div class="hm"></div>
</body></html>
'''

async def main():
    page = HTML.replace('%FONT%', 'file://' + os.path.join(ROOT, 'recovered/fonts/InterVariable.woff2')).replace('%CHEV%', 'file://' + os.path.join(ROOT, 'img/fo-chevron-alpha.png'))
    with tempfile.TemporaryDirectory() as d:
        src, shot = os.path.join(d, 'screen.html'), os.path.join(d, 'inner.png')
        open(src, 'w', encoding='utf-8').write(page)
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={'width': 319, 'height': 697}, device_scale_factor=2)
            await pg.goto('file://' + src, wait_until='load'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(1500)
            await pg.screenshot(path=shot); await b.close()
        inner = Image.open(shot).convert('RGBA')
    bez = Image.open(BEZEL).convert('RGBA')
    out = Image.new('RGBA', bez.size, (0, 0, 0, 0))
    mask = Image.new('L', inner.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, inner.size[0] - 1, inner.size[1] - 1), radius=96, fill=255)
    out.paste(inner, (41, 39), mask); out.alpha_composite(bez)
    out.save(OUT, quality=88, method=6)
    print('saved', os.path.relpath(OUT, ROOT), out.size)

asyncio.run(main())
