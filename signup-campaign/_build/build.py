# The Found Money Drop: two mockup versions (A dark cinematic, B light brand) + gallery.
# Mockup only. SIGNUP_LIVE stays False: the form never makes a network call, it shows a mockup notice.
import json, re, html, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
SIGNUP_LIVE = False

# hero photos: the landing page's own 31-photo vacation pool (same list as rebuild-v4/_build/desk_clean.py
# LANDING_POOL, read from there so the two never drift). Referenced by URL, nothing copied.
src = (ROOT.parent / 'rebuild-v4/_build/desk_clean.py').read_text()
POOL_IDS = re.search(r'LANDING_POOL = .*?"""(.*?)"""', src, re.S).group(1).split()
assert len(POOL_IDS) == 31
POOL = ['https://images.unsplash.com/photo-%s?w=1600&q=75&auto=format' % i for i in POOL_IDS]
CHEV = '../rebuild-v4/img/fo-chevron-transparent-v2.png'
CABIN = '../rebuild-v4/img/ph/e-seat.webp'
MALDIVES = '../rebuild-v4/img/ph/d-maldives.webp'
SANTORINI = '../rebuild-v4/img/ph/d-santorini.webp'
SUNSET = '../rebuild-v4/img/ph/bg-01.webp'

NUG = json.loads((pathlib.Path(__file__).parent / 'nuggets.json').read_text())
PICK = ['nug-cards', 'nug-tax', 'nug-marketing', 'nug-software', 'nug-fleet', 'nug-contractors', 'nug-dental',
        'nug-restaurants', 'nug-hvac', 'nug-law-firms', 'nug-ecommerce', 'nug-trucking', 'nug-fitness', 'nug-shipping']
NUGS = [next(n for n in NUG if n['id'] == p) for p in PICK]

NUGART = ('<svg class="nugart" viewBox="0 0 64 64" aria-hidden="true" focusable="false"><path d="M9 37 L15 23 L27 15 L41 16 L53 25 L56 39 L46 50 L28 53 L14 47 Z" fill="#E8C547"/><path d="M15 23 L27 15 L41 16 L35 28 L22 30 Z" fill="#FBE9A6"/><path d="M41 16 L53 25 L56 39 L44 36 L35 28 Z" fill="#D7AA2E"/><path d="M22 30 L35 28 L44 36 L34 44 L20 42 Z" fill="#F2D266"/><path d="M9 37 L15 23 L22 30 L20 42 L14 47 Z" fill="#DDB73E"/><path d="M20 42 L34 44 L44 36 L56 39 L46 50 L28 53 L14 47 Z" fill="#B98A1E"/><path d="M15 23 L22 30 L35 28 L41 16 M22 30 L20 42 L34 44 L44 36 L35 28 M44 36 L56 39 M20 42 L14 47 M34 44 L28 53" fill="none" stroke="#141216" stroke-opacity=".28" stroke-width="1.3" stroke-linejoin="round"/><path d="M9 37 L15 23 L27 15 L41 16 L53 25 L56 39 L46 50 L28 53 L14 47 Z" fill="none" stroke="#141216" stroke-width="2.4" stroke-linejoin="round"/><path d="M50 9 l1.6 -5 M55.5 14 l5 -1.2 M46 6.5 l-1 -4" stroke="#FA1896" stroke-width="2.4" stroke-linecap="round"/></svg>')

PROGRAMS = ['Ultimate Rewards', 'Membership Rewards', 'ThankYou Points', 'Capital One Miles', 'Bilt Rewards',
            'World of Hyatt', 'Hilton Honors', 'Marriott Bonvoy', 'IHG One Rewards', 'Wyndham Rewards',
            'Choice Privileges', 'ALL Accor', 'Flying Blue', 'Aeroplan', 'British Airways Avios', 'Iberia Plus',
            'Aer Lingus AerClub', 'AAdvantage', 'MileagePlus', 'SkyMiles', 'Rapid Rewards', 'TrueBlue',
            'Virgin Atlantic', 'KrisFlyer', 'Asia Miles', 'LifeMiles', 'Emirates Skywards', 'Etihad Guest',
            'Qatar Privilege Club', 'Turkish Miles&Smiles', 'ANA Mileage Club', 'JAL Mileage Bank',
            'Qantas Frequent Flyer']

CTA = 'Claim my Found Money Call'
E = html.escape

def brk(t, cls=''):
    return f'<span class="brk {cls}">{t}</span>'

def pills(row, rev=False):
    items = PROGRAMS[row::2] if not rev else PROGRAMS[1::2][::-1]
    out = []
    for i, p in enumerate(items):
        k = ('pk' if i % 5 == 1 else 'gd' if i % 7 == 3 else '')
        out.append(f'<span class="pill {k}" style="--i:{i}">{E(p)}</span>')
    one = ''.join(out)
    return (f'<div class="wave{" rev" if rev else ""}"><div class="wtrack" data-mq>'
            f'<div class="wset">{one}</div><div class="wset" aria-hidden="true">{one}</div></div></div>')

def nugcard(n):
    return (f'<article class="ncard">{NUGART}<div class="nmeta"><span>{E(n["kind"])}</span><span>{E(n["time"])}</span></div>'
            f'<h3>{E(n["h"])}</h3><p>{E(n["love"])}</p>'
            f'<div class="nfirst"><b>Inside:</b> {E(n["first"])}</div><div class="nfoot"><span>{n["n"]} nuggets</span><span>Free</span></div></article>')

def carousel():
    one = ''.join(nugcard(n) for n in NUGS)
    return (f'<div class="car" data-car><div class="ctrack" data-mq><div class="cset">{one}</div>'
            f'<div class="cset" aria-hidden="true">{one}</div></div></div>')

FAQ = [
    ('What does First Officer cost?', 'The Found Money Call is free. If you keep the desk after it, First Officer is $550 a month, flat.'),
    ('Is there a contract or an exit fee?', 'No. It is month to month, with no exit fee. Leave whenever you like.'),
    ('Does the desk book trips for me?', 'Burn vets your requirements and the desk books them as an ad hoc service. Every decision stays yours.'),
    ('Which programs are covered?', '50+ programs across business cards, airlines and hotels. On the call we only talk about the ones your spend actually touches.'),
    ('What happens on the Found Money Call?', 'Twenty minutes, free. We look at where your business spend goes on cards and show you what it could be collecting. Every dollar figure is labelled est. There is nothing to buy on the call.'),
    ('Who is it for?', 'Business owners who put real spend on cards: suppliers, software, ads, fuel, travel. If the business runs on a card, the points are already piling up.'),
    ('What happens to my data?', 'We use it to prepare your call and your estimate. Ask and we delete your data within 30 days.'),
    ('Is this tax, legal or financial advice?', 'No. Everything on this page is general information, and every dollar figure is an estimate, not a promise.'),
]

def faq():
    return ''.join(f'<details class="fq"><summary><span>{E(q)}</span><i aria-hidden="true"></i></summary><p>{E(a)}</p></details>' for q, a in FAQ)

PILLARS = [('01', 'Earn', 'You already do this', 'Every dollar your business spends on cards and vendors quietly earns points.'),
           ('02', 'Burn', 'Spending points is the skill', 'Burn is the industry word for spending points, and it is where all the value lives or dies.'),
           ('03', 'Return', 'In dollars, every Friday', 'A written report every Friday with the dollar value of what we captured that week.'),
           ('04', 'Learn', 'You get sharper, for free', 'Every recommendation arrives with its math in plain language.')]

def pillars():
    return ''.join(f'<div class="pl"><span class="pn">Pillar {n}</span><b>{w}.</b><span class="pt">{t}</span><p>{d}</p></div>' for n, w, t, d in PILLARS)

GOOGLE_G = ('<svg viewBox="0 0 48 48" width="20" height="20" aria-hidden="true" focusable="false"><path fill="#FFC107" d="M43.6 20.1H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.6-.4-3.9z"/><path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-7.9l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.1H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.6-.4-3.9z"/></svg>')

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;overflow-x:clip}
body{font-family:'DM Sans',system-ui,sans-serif;background:var(--bg);color:var(--fg);line-height:1.5;overflow-x:clip}
img{display:block;max-width:100%}
em,i,cite{font-style:normal}
a{color:inherit}
:focus-visible{outline:3px solid var(--glow);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:-999px;top:8px;background:#fff;color:#141216;padding:8px 12px;border-radius:8px;z-index:99}
.skip:focus{left:8px}
.mono{font-family:'JetBrains Mono',ui-monospace,monospace}
.wrap{width:min(1200px,100% - 32px);margin-inline:auto}
.serif{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-style:normal}

/* top bar: logo only, no nav */
.bar{position:absolute;inset:0 0 auto 0;z-index:5;display:flex;align-items:center;justify-content:space-between;padding:16px clamp(16px,3vw,36px)}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--barfg)}
.logo img{width:22px;height:auto}
.logo b{font-family:'DM Serif Display',serif;font-weight:400;font-size:21px;letter-spacing:.2px;display:block;line-height:1}
.logo small{display:block;font-family:'JetBrains Mono',monospace;font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;opacity:.8;margin-top:3px}
.bar .tag{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--barfg);opacity:.9}

/* hero stage: slow crossfade through the landing page's vacation pool */
.stage{position:relative;overflow:hidden;background:#0b0a0c}
.stage .ph{position:absolute;inset:0;background-size:cover;background-position:center;opacity:0;transform:scale(1.04);transition:opacity 1.6s ease,transform 7s linear}
.stage .ph.on{opacity:1;transform:scale(1.12)}
.stage .tint{position:absolute;inset:0;pointer-events:none}
.ctl{position:absolute;z-index:4;right:clamp(12px,3vw,32px);top:clamp(64px,6vw,76px);display:flex;gap:8px;align-items:center}
.ctl button{appearance:none;border:1px solid rgba(255,255,255,.55);background:rgba(0,0,0,.35);color:#fff;border-radius:999px;height:36px;padding:0 14px;font:600 12px/1 'JetBrains Mono',monospace;letter-spacing:.08em;text-transform:uppercase;cursor:pointer;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.ctl .cnt{font:500 11px/1 'JetBrains Mono',monospace;color:#fff;letter-spacing:.1em;text-shadow:0 1px 3px rgba(0,0,0,.6)}

/* the wordmark: CSS 3D, two stacked layers (extrusion behind, finish in front) */
.mark{display:block;width:clamp(54px,6vw,78px);height:auto;margin:0 auto 6px;filter:drop-shadow(0 10px 26px var(--chevglow))}
.wm{position:relative;display:grid;justify-items:center;text-align:center;font-family:'DM Serif Display',Georgia,serif;font-weight:400;text-transform:uppercase;line-height:.86;letter-spacing:.01em;font-size:clamp(76px,12.6vw,188px)}
.wm>span{grid-area:1/1;display:block;white-space:nowrap}
.wm .w2{display:inline}
.wm .x{color:var(--ex1);text-shadow:var(--exsh)}
.wm .f .w{display:inline-block;-webkit-background-clip:text;background-clip:text;color:transparent;background-image:var(--chrome);padding:0 .02em}
.wm .f .w.two{background-image:var(--chrome2)}
.wm .x .w{display:inline-block;padding:0 .02em}
.wm .x .w.two{color:var(--ex2);text-shadow:var(--exsh2)}
.brk{position:relative;display:inline-flex;align-items:center;gap:.6em;padding:6px 14px;font-family:'JetBrains Mono',monospace;font-size:11.5px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--brkfg)}
.brk::before,.brk::after{content:'';position:absolute;top:0;bottom:0;width:8px;border:1.5px solid var(--brkln)}
.brk::before{left:0;border-right:0}
.brk::after{right:0;border-left:0}
.brk.big{font-family:'DM Serif Display',serif;font-weight:400;font-size:clamp(30px,4.4vw,54px);letter-spacing:0;text-transform:none;line-height:1.05;padding:12px clamp(18px,3vw,34px);color:var(--fg);display:inline-block;text-align:center}
.brk.big::before,.brk.big::after{width:14px;border-width:2.5px}
.brk.big .p{color:var(--pinkt);display:block}

.lead{font-family:'DM Serif Display',serif;font-weight:400;font-size:clamp(25px,2.6vw,34px);line-height:1.12;text-align:center;max-width:22ch;margin:18px auto 0}
.lead .p{color:var(--pinkt);display:block}
.sub{max-width:56ch;margin:14px auto 0;text-align:center;color:var(--mute);font-size:17px}
.pillbtn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:0 28px;border-radius:999px;background:#E60F86;color:#fff;font:800 16.5px/1.1 'DM Sans',sans-serif;text-decoration:none;border:0;cursor:pointer;box-shadow:var(--pillsh);transition:transform .18s ease,box-shadow .18s ease;text-align:center}
.pillbtn:hover{transform:translateY(-2px)}
.pillbtn .ar{font-size:20px;line-height:0}
.ctarow{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;justify-content:center;margin-top:24px}
.txtlink{font-weight:700;font-size:15px;color:var(--fg);text-decoration:underline;text-decoration-color:var(--glow);text-underline-offset:4px;text-decoration-thickness:2px}
.facts{display:grid;grid-template-columns:repeat(4,auto);justify-content:center;gap:0;margin:28px auto 0;border:1px solid var(--line);border-radius:16px;overflow:hidden;width:max-content;max-width:100%}
.facts div{padding:12px 20px;border-left:1px solid var(--line);text-align:center}
.facts div:first-child{border-left:0}
.facts b{display:block;font-size:17px;font-weight:800;color:var(--fg)}
.facts span{font-family:'JetBrains Mono',monospace;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}

section{position:relative}
.sec{padding:clamp(64px,8vw,112px) 0}
.sh{text-align:center}
.sh h2{font-family:'DM Serif Display',serif;font-weight:400;font-size:clamp(36px,5vw,64px);line-height:1.02;margin-top:14px}
.sh h2 .p{color:var(--pinkt);display:block}
.sh p{max-width:60ch;margin:14px auto 0;color:var(--mute);font-size:17px}

/* spend slider */
.calc{display:grid;grid-template-columns:1.05fr .95fr;gap:20px;margin-top:40px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:26px;padding:clamp(20px,2.6vw,34px);position:relative;overflow:hidden}
.exflag{position:absolute;top:16px;right:16px;font:700 10.5px/1 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;padding:7px 10px;border-radius:999px;background:var(--flagbg);color:var(--flagfg)}
.rk{font:600 11px/1.3 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);display:block;padding-right:130px}
.big{font-family:'DM Serif Display',serif;font-size:clamp(64px,8.4vw,116px);line-height:.95;margin-top:10px;color:var(--fg);font-variant-numeric:tabular-nums;letter-spacing:-.01em;white-space:nowrap}
.big .est{font-family:'JetBrains Mono',monospace;font-size:.2em;letter-spacing:.08em;color:var(--pinkt);vertical-align:.55em;margin-left:.25em;font-weight:700}
.bigsub{color:var(--mute);margin-top:8px;font-size:15.5px}
.bars{margin-top:24px;display:grid;gap:12px}
.br .bl{display:flex;justify-content:space-between;font-size:14px;font-weight:700;margin-bottom:6px;gap:10px}
.br .bl span:last-child{font-variant-numeric:tabular-nums}
.br .bt{height:16px;border-radius:999px;background:var(--track);overflow:hidden}
.br .bf{height:100%;border-radius:999px;width:0;transition:width .7s cubic-bezier(.2,.8,.2,1)}
.br.fo .bf{background:linear-gradient(90deg,#E60F86,#FA1896);box-shadow:0 0 18px var(--glowsoft)}
.br.cb .bf{background:var(--cbbar)}
.delta{margin-top:16px;display:inline-flex;gap:8px;align-items:center;font-weight:800;font-size:15px;padding:9px 14px;border-radius:12px;background:var(--deltabg);color:var(--fg)}
.ctlbox label,.ctlbox .lbl{display:flex;justify-content:space-between;align-items:baseline;gap:10px;font-weight:700;font-size:15px}
.ctlbox output{font-family:'DM Serif Display',serif;font-size:34px;font-weight:400;color:var(--pinkt);font-variant-numeric:tabular-nums}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:44px;background:transparent;cursor:pointer;margin-top:4px}
input[type=range]::-webkit-slider-runnable-track{height:10px;border-radius:999px;background:linear-gradient(90deg,#E60F86 0 var(--pct,30%),var(--track) var(--pct,30%) 100%)}
input[type=range]::-moz-range-track{height:10px;border-radius:999px;background:var(--track)}
input[type=range]::-moz-range-progress{height:10px;border-radius:999px;background:#E60F86}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:30px;height:30px;border-radius:50%;background:#fff;border:4px solid #E60F86;margin-top:-10px;box-shadow:0 0 0 6px var(--glowsoft)}
input[type=range]::-moz-range-thumb{width:24px;height:24px;border-radius:50%;background:#fff;border:4px solid #E60F86}
.ticks{display:flex;justify-content:space-between;font:500 11px/1 'JetBrains Mono',monospace;color:var(--mute);margin-top:2px}
.seg{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px}
.seg button{appearance:none;border:1.5px solid var(--line2);background:transparent;color:var(--fg);border-radius:12px;min-height:46px;font:800 16px/1 'DM Sans',sans-serif;cursor:pointer}
.seg button small{display:block;font:500 10px/1.2 'JetBrains Mono',monospace;letter-spacing:.06em;color:var(--mute);margin-top:4px;text-transform:uppercase}
.seg button[aria-pressed=true]{border-color:#E60F86;background:#E60F86;color:#fff}
.seg button[aria-pressed=true] small{color:#ffe1f1}
.ledger{margin-top:20px;border-top:1px dashed var(--line2)}
.ledger div{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px dashed var(--line2);font-size:14.5px}
.ledger div span:first-child{color:var(--mute)}
.ledger div span:last-child{font-weight:800;font-variant-numeric:tabular-nums;white-space:nowrap}
.ledger .tot span{color:var(--fg)!important;font-weight:800}
.ledger .tot span:last-child{color:var(--pinkt)!important}
.fine{font-size:12.5px;color:var(--mute);margin-top:14px;line-height:1.5}
.plrow{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:20px}
.pl{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:18px 18px 20px}
.pl .pn{font:600 10.5px/1 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--mute)}
.pl b{display:block;font-family:'DM Serif Display',serif;font-weight:400;font-size:34px;line-height:1;margin-top:10px;color:var(--fg)}
.pl .pt{display:block;font-weight:800;margin-top:6px;color:var(--pinkt)}
.pl p{font-size:14px;color:var(--mute);margin-top:6px}

/* wavy program-pill marquee */
.mqsec{padding:clamp(56px,7vw,96px) 0 clamp(40px,5vw,72px);overflow:hidden}
.waves{margin-top:34px;display:grid;gap:clamp(18px,3vw,34px)}
.wave{transform:rotate(-3.2deg);padding:26px 0}
.wave.rev{transform:rotate(2.4deg)}
.wtrack{display:flex;width:max-content;animation:mq 90s linear infinite}
.wave.rev .wtrack{animation-direction:reverse;animation-duration:110s}
.wset{display:flex;gap:14px;padding-right:14px}
.pill{--y:calc(sin(var(--i) * 0.62rad) * 14px);--r:calc(cos(var(--i) * 0.62rad) * 5deg);transform:translateY(var(--y)) rotate(var(--r));white-space:nowrap;padding:12px 22px;border-radius:999px;font:700 16px/1 'JetBrains Mono',monospace;letter-spacing:.06em;text-transform:uppercase;border:1.5px solid var(--pillln);color:var(--pillfg);background:var(--pillbg)}
.pill.pk{background:#E60F86;border-color:#E60F86;color:#fff}
.pill.gd{background:var(--goldpill);border-color:var(--goldpill);color:#141216}
@keyframes mq{to{transform:translateX(-50%)}}

/* Golden Nugget carousel */
.car{margin-top:36px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent);mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent)}
.ctrack{display:flex;width:max-content;animation:mq 120s linear infinite}
.car:hover .ctrack,.car:focus-within .ctrack,.wave:hover .wtrack{animation-play-state:paused}
.cset{display:flex;gap:18px;padding-right:18px}
.ncard{width:300px;flex:none;border-radius:22px;padding:20px;background:var(--ncbg);border:1px solid var(--ncln);position:relative;display:flex;flex-direction:column;min-height:330px;color:var(--ncfg)}
.ncard .nugart{width:58px;height:58px}
.nmeta{display:flex;justify-content:space-between;font:600 10.5px/1 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--ncmute);margin-top:12px}
.ncard h3{font-family:'DM Serif Display',serif;font-weight:400;font-size:25px;line-height:1.06;margin-top:10px}
.ncard p{font-size:14.5px;color:var(--ncmute);margin-top:8px}
.nfirst{margin-top:auto;padding-top:12px;font-size:14px;border-top:1px dashed var(--ncln)}
.nfirst b{color:var(--pinkt)}
.nfoot{display:flex;justify-content:space-between;margin-top:12px;font:700 11px/1 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase}
.nfoot span:last-child{background:#E60F86;color:#fff;padding:6px 9px;border-radius:999px}

/* entry */
.entry{display:grid;grid-template-columns:1fr minmax(0,460px) 1fr;gap:28px;align-items:center;margin-top:40px}
.post{position:relative;height:440px}
.post figure{position:absolute;width:210px;border-radius:16px;overflow:hidden;background:#fff;padding:8px 8px 10px;box-shadow:0 22px 50px rgba(0,0,0,.35)}
.post figure img{width:100%;height:200px;object-fit:cover;border-radius:10px}
.post figcaption{font:700 10.5px/1 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#141216;padding:9px 4px 0}
.post.l figure:nth-child(1){left:6%;top:10px;transform:rotate(-7deg)}
.post.l figure:nth-child(2){left:26%;top:170px;transform:rotate(5deg)}
.post.r figure:nth-child(1){right:8%;top:40px;transform:rotate(6deg)}
.post.r figure:nth-child(2){right:28%;top:200px;transform:rotate(-4deg)}
.ecard{background:var(--ecbg);color:#141216;border-radius:28px;overflow:hidden;box-shadow:var(--ecsh);border:1px solid var(--ecln)}
.ehead{position:relative;height:150px;background:#0b0a0c center/cover no-repeat;display:flex;align-items:flex-end;padding:16px 20px}
.ehead::before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,.72))}
.ehead span{position:relative;font-family:'DM Serif Display',serif;color:#fff;font-size:30px;line-height:1}
.ehead span small{display:block;font:700 10.5px/1 'JetBrains Mono',monospace;letter-spacing:.18em;text-transform:uppercase;margin-bottom:8px;color:#ffd1ea}
.ebody{padding:22px 22px 24px}
.ebody h3{font-family:'DM Serif Display',serif;font-weight:400;font-size:28px;line-height:1.08;text-align:center}
.erow{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid #ece6dc;border-bottom:1px solid #ece6dc;margin:16px 0 18px}
.erow div{text-align:center;padding:10px 4px;border-left:1px solid #ece6dc}
.erow div:first-child{border-left:0}
.erow b{display:block;font-size:16px;font-weight:800}
.erow span{font:600 9.5px/1.2 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:#6f6875}
.field{position:relative}
.field input{width:100%;height:54px;border-radius:14px;border:1.5px solid #cfc7bb;padding:0 16px 0 46px;font:500 16px 'DM Sans',sans-serif;background:#fff;color:#141216}
.field input:focus{outline:none;border-color:#E60F86;box-shadow:0 0 0 4px rgba(250,24,150,.18)}
.field svg{position:absolute;left:15px;top:50%;transform:translateY(-50%);width:20px;height:20px;stroke:#8a8492}
.ecard .pillbtn{width:100%;margin-top:10px;box-shadow:0 10px 26px rgba(230,15,134,.35)}
.or{display:flex;align-items:center;gap:10px;margin:14px 0;font:600 11px/1 'JetBrains Mono',monospace;letter-spacing:.16em;text-transform:uppercase;color:#8a8492}
.or::before,.or::after{content:'';flex:1;height:1px;background:#e5ded2}
.gbtn{width:100%;min-height:52px;border-radius:999px;border:1.5px solid #141216;background:#fff;color:#141216;display:flex;align-items:center;justify-content:center;gap:10px;font:700 16px 'DM Sans',sans-serif;cursor:pointer}
.nl{margin-top:16px;padding:14px;border-radius:16px;background:#FFF6D6;border:1px solid #F1DE96;display:flex;gap:12px;align-items:center;justify-content:space-between}
.nl p{font-size:13.5px;line-height:1.35;color:#3d3842}
.nl p b{display:block;color:#141216;font-size:14.5px}
.nl button{flex:none;appearance:none;border:1.5px solid #141216;background:transparent;border-radius:999px;min-height:42px;padding:0 14px;font:800 13.5px 'DM Sans',sans-serif;cursor:pointer;color:#141216}
.efine{font-size:12px;color:#6f6875;text-align:center;margin-top:14px;line-height:1.45}
.notice{display:none;margin-top:12px;padding:12px 14px;border-radius:12px;background:#141216;color:#fff;font-size:14px;line-height:1.4}
.notice.on{display:block}
.after{text-align:center;margin-top:44px}

/* FAQ */
.faq{max-width:780px;margin:40px auto 0;display:grid;gap:10px}
.fq{border-radius:16px;background:var(--fqbg);border:1px solid var(--line)}
.fq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 22px;font-weight:800;font-size:17px}
.fq summary::-webkit-details-marker{display:none}
.fq summary i{position:relative;width:16px;height:16px;flex:none}
.fq summary i::before,.fq summary i::after{content:'';position:absolute;left:0;right:0;top:7px;height:2px;background:currentColor;transition:transform .25s}
.fq summary i::after{transform:rotate(90deg)}
.fq[open] summary i::after{transform:rotate(0)}
.fq p{padding:0 22px 20px;color:var(--mute);font-size:16px;max-width:64ch}

footer{border-top:1px solid var(--line);padding:30px 0 40px;background:var(--footbg)}
.fwrap{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;justify-content:space-between}
.faddr{font-size:14px;font-weight:600;color:var(--fg)}
.fnote{font-size:12px;color:var(--mute);margin-top:10px;max-width:90ch}

/* ---------- phone: designed, not shrunk ---------- */
@media (max-width:760px){
  .bar{padding:12px 16px}
  .bar .tag{display:none}
  .wm{font-size:clamp(70px,21.5vw,104px);line-height:.84}
  .wm .w2{display:block}
  .wm>span{white-space:normal}
  .lead{font-size:26px;max-width:15ch}
  .sub{font-size:16px}
  .facts{grid-template-columns:1fr 1fr;width:100%}
  .facts div{border-left:0;border-top:1px solid var(--line);padding:12px 8px}
  .facts div:nth-child(-n+2){border-top:0}
  .facts div:nth-child(even){border-left:1px solid var(--line)}
  .facts b{font-size:16px}
  .pillbtn{width:100%;min-height:58px;font-size:17px}
  .ctarow{flex-direction:column}
  .calc{grid-template-columns:1fr}
  .plrow{grid-template-columns:1fr 1fr;gap:10px}
  .pl{padding:14px}
  .pl b{font-size:28px}
  .pl p{font-size:13px}
  .big{font-size:clamp(58px,18vw,80px)}
  .pill{font-size:13.5px;padding:10px 16px}
  .wset{gap:10px;padding-right:10px}
  .ncard{width:262px;min-height:316px;padding:18px}
  .ncard h3{font-size:23px}
  .entry{grid-template-columns:1fr}
  .post{display:none}
  .ehead{height:130px}
  .ebody{padding:18px 16px 20px}
  .nl{flex-direction:column;align-items:stretch;text-align:left}
  .nl button{width:100%}
  .fq summary{padding:18px 16px;font-size:16px}
  .fq p{padding:0 16px 18px;font-size:15px}
  .brk.big{font-size:32px}
  .fwrap{flex-direction:column;align-items:flex-start}
  .phstrip{display:flex}
}
@media (min-width:761px) and (max-width:1100px){
  .entry{grid-template-columns:1fr}
  .post{display:none}
  .ecard{max-width:480px;margin:0 auto;width:100%}
  .plrow{grid-template-columns:1fr 1fr}
}
.phstrip{display:none;gap:10px;margin:22px -16px 0;padding:0 16px;overflow-x:auto;scrollbar-width:none}
.phstrip figure{flex:none;width:150px;border-radius:14px;overflow:hidden;background:#fff;padding:6px 6px 8px;transform:rotate(var(--r))}
.phstrip img{width:100%;height:104px;object-fit:cover;border-radius:9px}
.phstrip figcaption{font:700 9.5px/1 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:#141216;padding:7px 2px 0}

html.still .wtrack,html.still .ctrack{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .stage .ph{transition:none;transform:none!important}
  .wtrack,.ctrack{animation:none!important}
  .wset[aria-hidden],.cset[aria-hidden]{display:none}
  .wave{overflow-x:auto}
  .car{overflow-x:auto;-webkit-mask-image:none;mask-image:none}
  .br .bf{transition:none}
  .pillbtn{transition:none}
}
"""

THEME_A = r"""
:root{--bg:#000;--fg:#fff;--mute:#a7a1ab;--line:#26222a;--line2:#3a343f;--card:#0d0c0f;--glow:#FA1896;--glowsoft:rgba(250,24,150,.35);--pinkt:#FF4FAE;
--barfg:#fff;--chevglow:rgba(250,24,150,.55);
--chrome:linear-gradient(180deg,#ffffff 0%,#f3f2f6 22%,#b9b7c2 44%,#5d5a66 50%,#d6d4dc 58%,#ffffff 74%,#a9a6b2 100%);
--chrome2:linear-gradient(180deg,#ffffff 0%,#f3f2f6 22%,#b9b7c2 44%,#5d5a66 50%,#d6d4dc 58%,#ffffff 74%,#a9a6b2 100%);
--ex1:#2b2830;--ex2:#2b2830;--exsh:1px 1px 0 #3c3842,2px 2px 0 #36323c,3px 3px 0 #302d35,4px 4px 0 #2a272f,5px 5px 0 #24212a,6px 6px 0 #1e1c22,7px 7px 0 #18161b,0 0 60px rgba(250,24,150,.55),0 0 140px rgba(250,24,150,.35);
--exsh2:1px 1px 0 #3c3842,2px 2px 0 #36323c,3px 3px 0 #302d35,4px 4px 0 #2a272f,5px 5px 0 #24212a,6px 6px 0 #1e1c22,7px 7px 0 #18161b,0 0 60px rgba(250,24,150,.55),0 0 140px rgba(250,24,150,.35);
--brkfg:#fff;--brkln:#fff;--pillsh:0 0 0 1px rgba(255,255,255,.08),0 12px 40px rgba(250,24,150,.55);
--flagbg:#FA1896;--flagfg:#fff;--track:#2a262e;--cbbar:#6e6876;--deltabg:rgba(250,24,150,.16);
--pillln:#e9e6ec;--pillfg:#fff;--pillbg:#000;--goldpill:#E8C547;
--ncbg:#111014;--ncln:#2b2730;--ncfg:#fff;--ncmute:#b1abb5;
--ecbg:#fff;--ecln:#fff;--ecsh:0 0 0 1px rgba(250,24,150,.4),0 30px 90px rgba(250,24,150,.32);
--fqbg:#111013;--footbg:#000}
.stage{height:min(84vh,820px);min-height:520px}
.stage .tint{background:radial-gradient(120% 80% at 50% 30%,rgba(0,0,0,0) 40%,rgba(0,0,0,.55) 100%),linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 22%,rgba(0,0,0,0) 52%,rgba(0,0,0,.85) 82%,#000 100%)}
.hero-copy{position:relative;z-index:3;margin-top:clamp(-300px,-19vw,-150px);text-align:center}
.glowfloor{position:absolute;left:50%;top:-40px;width:min(1100px,100%);height:420px;transform:translateX(-50%);background:radial-gradient(50% 50% at 50% 50%,rgba(250,24,150,.32),rgba(250,24,150,0) 70%);pointer-events:none;z-index:-1}
.sec.calcsec{background:radial-gradient(60% 40% at 50% 0%,rgba(250,24,150,.16),transparent 70%)}
.panel.readout{background:linear-gradient(180deg,#120d12,#0a090b);box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 0 80px rgba(250,24,150,.14)}
.entrysec{background:radial-gradient(50% 45% at 50% 55%,rgba(250,24,150,.22),transparent 72%)}
.ncard{box-shadow:0 0 0 1px rgba(232,197,71,.06)}
.ncard:nth-child(3n+1){border-color:rgba(232,197,71,.55)}
@media (max-width:760px){.stage{height:72svh;min-height:470px}.hero-copy{margin-top:-170px}}
"""

THEME_B = r"""
:root{--bg:#FAF6EE;--fg:#141216;--mute:#5e5864;--line:#e7dfd2;--line2:#d9cfbf;--card:#fff;--glow:#FA1896;--glowsoft:rgba(250,24,150,.22);--pinkt:#E60F86;
--barfg:#fff;--chevglow:rgba(230,15,134,.28);
--chrome:linear-gradient(180deg,#4a4550 0%,#141216 46%,#2c2830 54%,#141216 100%);
--chrome2:linear-gradient(180deg,#FF5DB6 0%,#FA1896 40%,#E60F86 56%,#C70C74 100%);
--ex1:#E60F86;--ex2:#141216;
--exsh:1px 1px 0 #E60F86,2px 2px 0 #E60F86,3px 3px 0 #E60F86,4px 4px 0 #E60F86,5px 5px 0 #E60F86,6px 6px 0 #d40d7b,7px 7px 0 #c20b71,8px 8px 0 #b00a66,14px 18px 30px rgba(20,18,22,.18);
--exsh2:1px 1px 0 #141216,2px 2px 0 #141216,3px 3px 0 #141216,4px 4px 0 #141216,5px 5px 0 #141216,6px 6px 0 #141216,7px 7px 0 #141216,8px 8px 0 #141216,14px 18px 30px rgba(20,18,22,.2);
--brkfg:#141216;--brkln:#141216;--pillsh:0 12px 30px rgba(230,15,134,.32);
--flagbg:#141216;--flagfg:#FFD84D;--track:#efe7da;--cbbar:#bdb4a6;--deltabg:#FFF1C2;
--pillln:#141216;--pillfg:#141216;--pillbg:#fff;--goldpill:#F5B700;
--ncbg:#fff;--ncln:#e7dfd2;--ncfg:#141216;--ncmute:#5e5864;
--ecbg:#fff;--ecln:#141216;--ecsh:10px 10px 0 #141216;
--fqbg:#fff;--footbg:#F3EDE2}
.stagewrap{padding:12px 12px 0}
.stage{height:min(76vh,760px);min-height:500px;border-radius:30px}
.stage .tint{background:linear-gradient(180deg,rgba(20,18,22,.42) 0%,rgba(20,18,22,0) 24%,rgba(20,18,22,0) 70%,rgba(20,18,22,.38) 100%)}
.hero-copy{position:relative;z-index:3;margin-top:clamp(-150px,-8.6vw,-90px);text-align:center}
.hero-copy .mark{filter:drop-shadow(0 8px 16px rgba(20,18,22,.25))}
.panel{box-shadow:6px 6px 0 #141216;border-color:#141216}
.panel.readout{background:#141216;color:#fff;--fg:#fff;--mute:#c9c1cc;--track:#2c2830;--line2:#3a343f;--deltabg:rgba(255,216,77,.16);--pinkt:#FF4FAE}
.panel.readout .delta{color:#FFD84D}
.calcsec{background:linear-gradient(180deg,#FAF6EE,#F6EFE2)}
.mqsec{background:#E60F86;color:#fff;--fg:#fff;--mute:#ffd7ec;--brkfg:#fff;--brkln:#fff;--pinkt:#FFE07A;--pillbg:#fff;--pillfg:#141216;--pillln:#141216}
.mqsec .pill.pk{background:#141216;border-color:#141216}
.nugsec{background:#141216;color:#fff;--fg:#fff;--mute:#c9c1cc;--brkfg:#fff;--brkln:#fff;--pinkt:#FF4FAE}
.nugsec .txtlink{color:#fff}
.ncard{background:#FAF6EE;color:#141216;border:2px solid #141216;--pinkt:#E60F86}
.ncard:nth-child(3n+2){background:#FFE9A3}
.ncard:nth-child(3n){background:#fff}
.pl{border:2px solid #141216;box-shadow:4px 4px 0 #141216}
.pl:nth-child(1){background:#fff}
.pl:nth-child(2){background:#FFF1C2}
.pl:nth-child(3){background:#fff}
.pl:nth-child(4){background:#FFE1F0}
.fq{border:2px solid #141216}
.entrysec{background:radial-gradient(60% 50% at 50% 50%,rgba(250,24,150,.10),transparent 70%)}
.post figure{box-shadow:6px 6px 0 #141216;border:2px solid #141216}
.facts{border:2px solid #141216;background:#fff}
.facts div{border-color:#141216}
@media (max-width:760px){.stagewrap{padding:8px 8px 0}.stage{height:62svh;min-height:420px;border-radius:22px}.hero-copy{margin-top:-74px}.facts div{border-color:#141216}}
"""

JS = r"""
(function(){
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var root=document.documentElement;
/* hero crossfade: loads only the photo on screen and the next */
var st=document.querySelector('.stage'),urls=st.dataset.ph.split('|'),iv=+st.dataset.iv||6600,i=0,layers=[],cnt=document.querySelector('.cnt');
function layer(n){if(layers[n])return layers[n];var d=document.createElement('div');d.className='ph';d.style.backgroundImage='url("'+urls[n]+'")';st.insertBefore(d,st.querySelector('.tint'));layers[n]=d;return d;}
function show(n){layers.forEach(function(l){if(l)l.classList.remove('on')});var l=layer(n);void l.offsetWidth;l.classList.add('on');if(cnt)cnt.textContent=String(n+1).padStart(2,'0')+' / '+urls.length;var nx=(n+1)%urls.length;var im=new Image();im.src=urls[nx];}
show(0);
var timer=null,paused=RM;
function play(){if(timer)clearInterval(timer);timer=setInterval(function(){i=(i+1)%urls.length;show(i);},iv);}
if(!RM)play();
var pb=document.getElementById('pausebtn');
function setP(p){paused=p;pb.textContent=p?'Play':'Pause';pb.setAttribute('aria-pressed',p?'true':'false');root.classList.toggle('still',p);if(p){clearInterval(timer);timer=null;}else if(!RM){play();}}
pb.addEventListener('click',function(){setP(!paused)});
if(RM){pb.textContent='Play';pb.setAttribute('aria-pressed','true');pb.addEventListener('click',function(){i=(i+1)%urls.length;show(i);},true);}
document.addEventListener('visibilitychange',function(){if(document.hidden){clearInterval(timer);timer=null;}else if(!paused&&!RM)play();});

/* spend slider: same math as the site calculator (calculator.html calc()), single blended earn rate */
var CPP=0.03,UTIL=0.85,REAL=0.60,ALT=0.30,FEE=550,CASH=0.02,earn=2.2;
var sp=document.getElementById('spend'),out=document.getElementById('spendout'),big=document.getElementById('bignum'),shown=0,anim=null;
function money(v){var s=v<0?'-':'';return s+'$'+Math.round(Math.abs(v)).toLocaleString('en-US');}
function set(id,v){document.getElementById(id).textContent=v;}
function tween(to){if(anim)cancelAnimationFrame(anim);if(RM){shown=to;big.firstChild.nodeValue=money(to);return;}var from=shown,t0=performance.now(),d=650;function f(t){var k=Math.min(1,(t-t0)/d);k=1-Math.pow(1-k,3);shown=from+(to-from)*k;big.firstChild.nodeValue=money(shown);if(k<1)anim=requestAnimationFrame(f);}anim=requestAnimationFrame(f);}
function calc(first){
  var m=+sp.value,pct=(m-sp.min)/(sp.max-sp.min)*100;sp.style.setProperty('--pct',pct+'%');
  out.textContent=money(m);
  var pts=m*earn,used=pts*UTIL,sticker=used*CPP,honest=sticker*REAL+sticker*(1-REAL)*ALT,net=honest-FEE;
  var yNet=net*12,yCash=m*CASH*12;
  set('lPts',Math.round(pts*12).toLocaleString('en-US'));set('lUsed',Math.round(used*12).toLocaleString('en-US'));
  set('lSticker',money(sticker*12));set('lHonest',money(honest*12));set('lNet',money(yNet)+' est.');set('lEarn',earn.toFixed(1)+'x');
  set('foV',money(yNet)+' est.');set('cbV',money(yCash));
  var mx=Math.max(yNet,yCash,1);document.getElementById('foBar').style.width=Math.max(0,yNet/mx*100)+'%';document.getElementById('cbBar').style.width=(yCash/mx*100)+'%';
  var d=yNet-yCash,dl=document.getElementById('delta');
  dl.textContent=d>=0?('+'+money(d)+' a year vs 2% cash back, est.'):('At this spend, 2% cash back comes out ahead by '+money(-d)+' a year, est.');
  if(!first)tween(yNet);
}
sp.addEventListener('input',function(){calc()});
document.querySelectorAll('.seg button').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.seg button').forEach(function(x){x.setAttribute('aria-pressed','false')});b.setAttribute('aria-pressed','true');earn=+b.dataset.e;calc();});});
calc(true);
var rd=document.querySelector('.readout');
if('IntersectionObserver' in window&&!RM){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){calc();io.disconnect();}})},{threshold:.35});io.observe(rd);}else{calc();}

/* CTA pills: jump to the one entry card and focus the email field */
document.querySelectorAll('a[href="#entry"]').forEach(function(a){a.addEventListener('click',function(){setTimeout(function(){var e=document.getElementById('em');if(e)e.focus({preventScroll:true});},RM?0:550);});});

/* MOCKUP GUARD: LIVE is false in the preview, so nothing is sent anywhere */
var LIVE=__LIVE__;
var f=document.getElementById('entryform'),note=document.getElementById('notice');
function mock(kind){note.classList.add('on');note.textContent=kind==='google'?'Mockup only, nothing was sent. On the live site this signs you in with Google and books your Found Money Call.':kind==='news'?'Mockup only, nothing was sent. On the live site this adds you to The Daily Redemption.':'Mockup only, nothing was sent. On the live site this books your Found Money Call and adds you to The Daily Redemption.';}
f.addEventListener('submit',function(ev){ev.preventDefault();var k=(ev.submitter&&ev.submitter.value)||'call';if(k!=='google'&&!f.em.checkValidity()){f.em.reportValidity();return;}if(!LIVE){mock(k);return;}});
document.getElementById('gbtn').addEventListener('click',function(){if(!LIVE){mock('google');return;}});
})();
"""

def page(theme):
    A = theme == 'A'
    title = 'The Found Money Drop | First Officer' + (' (mockup A, dark)' if A else ' (mockup B, light)')
    ph = '|'.join(POOL)
    hero_stage = (f'<div class="stage" data-iv="6600" data-ph="{E(ph)}">'
                  f'<div class="tint"></div>'
                  f'<div class="ctl"><span class="cnt mono" aria-hidden="true">01 / 31</span><button type="button" id="pausebtn" aria-pressed="false">Pause</button></div></div>')
    bar = ('<header class="bar"><a class="logo" href="#top" aria-label="First Officer"><img src="' + CHEV + '" alt="" width="22" height="29">'
           '<span><b>First Officer</b><small>by UpNonStop™</small></span></a><span class="tag">[ The Found Money Drop ]</span></header>')
    wm_words = '<span class="w">Found</span> <span class="w two w2">Money</span>'
    hero = f"""<section id="top" class="hero">{'' if A else '<div class="stagewrap">'}<div style="position:relative">{bar}{hero_stage}</div>{'' if A else '</div>'}
<div class="hero-copy">{'<div class="glowfloor" aria-hidden="true"></div>' if A else ''}
<img class="mark" src="{CHEV}" alt="" width="78" height="104">
<h1 class="wm" aria-label="Found Money"><span class="x" aria-hidden="true">{wm_words}</span><span class="f" aria-hidden="true">{wm_words}</span></h1>
<div style="margin-top:18px">{brk('The Found Money Drop · First Officer')}</div>
<div class="wrap">
<p class="lead">Your card spend is already paying for trips. <span class="p">Most owners never collect.</span></p>
<p class="sub">Claim a free 20-minute Found Money Call. The desk looks at where your business spend goes and shows you what it could be collecting, every figure labelled est.</p>
<div class="ctarow"><a class="pillbtn" href="#entry">{CTA} <span class="ar" aria-hidden="true">→</span></a><a class="txtlink" href="#calc">Or slide your spend first</a></div>
<div class="facts"><div><b>Free</b><span>20-min call</span></div><div><b>50+</b><span>programs</span></div><div><b>$550/mo</b><span>if you stay</span></div><div><b>No</b><span>exit fee</span></div></div>
</div></div></section>"""

    calc = f"""<section class="sec calcsec" id="calc"><div class="wrap">
<div class="sh">{brk('Example data · est.')}<h2>Slide your spend. <span class="p">Watch it count.</span></h2>
<p>The same math as our calculator, on one slider. Example data: a blended earn rate, points at about 3 cents, 85% redeemed, and an honest discount for trips you would not have bought anyway. Net of our fee.</p></div>
<div class="calc">
<div class="panel readout" aria-live="polite"><span class="exflag">Example data</span>
<span class="rk">What your spend could collect, a year</span>
<div class="big" id="bignum">$0<span class="est">est.</span></div>
<p class="bigsub">Net of the $550 a month fee ($6,600 a year). Card annual fees not deducted.</p>
<div class="bars"><div class="br fo"><div class="bl"><span>First Officer, est.</span><span id="foV">$0</span></div><div class="bt"><div class="bf" id="foBar"></div></div></div>
<div class="br cb"><div class="bl"><span>2% cash back</span><span id="cbV">$0</span></div><div class="bt"><div class="bf" id="cbBar"></div></div></div></div>
<div class="delta" id="delta">&nbsp;</div>
</div>
<div class="panel ctlbox">
<label for="spend"><span>Monthly card spend</span><output id="spendout" for="spend">$50,000</output></label>
<input type="range" id="spend" min="10000" max="300000" step="5000" value="50000" aria-describedby="spendhint">
<div class="ticks" id="spendhint"><span>$10K</span><span>$100K</span><span>$200K</span><span>$300K</span></div>
<div class="lbl" style="margin-top:16px"><span>Blended earn rate</span><span class="rk">Example</span></div>
<div class="seg" role="group" aria-label="Blended earn rate"><button type="button" data-e="2.0" aria-pressed="false">2.0x<small>flat card</small></button><button type="button" data-e="2.2" aria-pressed="true">2.2x<small>typical mix</small></button><button type="button" data-e="2.5" aria-pressed="false">2.5x<small>heavy bonus</small></button></div>
<div class="ledger">
<div><span>Points a year (spend × <span id="lEarn">2.2x</span>)</span><span id="lPts">0</span></div>
<div><span>Redeemed, 85%</span><span id="lUsed">0</span></div>
<div><span>Travel value at about 3¢ a point</span><span id="lSticker">$0</span></div>
<div><span>Honest value: 60% you would have bought anyway, the rest at 30%</span><span id="lHonest">$0</span></div>
<div><span>Less our fee, $550 × 12</span><span>-$6,600</span></div>
<div class="tot"><span>Net, a year</span><span id="lNet">$0</span></div>
</div>
<p class="fine">Estimate only, not a guarantee. Built from common redemption benchmarks; actual value depends on how and when you redeem. Compared with 2% cash back on the same spend. General information, not tax, legal or financial advice.</p>
</div></div>
<div class="plrow">{pillars()}</div>
</div></section>"""

    mq = f"""<section class="mqsec" id="programs"><div class="wrap sh">{brk('50+ programs')}<h2>Cards, airlines, hotels. <span class="p">One desk for all of it.</span></h2></div>
<div class="waves" aria-label="Some of the 50+ programs the desk works with">{pills(0)}{pills(1, rev=True)}</div></section>"""

    nug = f"""<section class="sec nugsec" id="nuggets"><div class="wrap sh">{brk('Free from the desk')}<h2>Golden Nugget packs. <span class="p">Free, and new ones keep coming.</span></h2>
<p>Short packs of the rules nobody explains: how suppliers get coded, what moved in taxes, where the points hide. The Daily Redemption brings the new ones to your inbox.</p></div>
{carousel()}
<div class="wrap after" style="margin-top:30px"><a class="txtlink" href="#entry">Get new packs in The Daily Redemption</a></div></section>"""

    entry = f"""<section class="sec entrysec" id="entry"><div class="wrap">
<div class="sh"><span class="brk big">One call. <span class="p">Found money.</span></span>
<p>Twenty minutes with the desk, free. We look at how your business spends on cards and show you what it could be collecting across Earn, Burn, Return and Learn. Every dollar figure labelled est.</p></div>
<div class="phstrip" aria-hidden="true"><figure style="--r:-3deg"><img src="{CABIN}" alt=""><figcaption>Business class</figcaption></figure><figure style="--r:2deg"><img src="{MALDIVES}" alt=""><figcaption>Maldives</figcaption></figure><figure style="--r:-2deg"><img src="{SANTORINI}" alt=""><figcaption>Santorini</figcaption></figure><figure style="--r:3deg"><img src="{SUNSET}" alt=""><figcaption>Sunset beach</figcaption></figure></div>
<div class="entry">
<div class="post l" aria-hidden="true"><figure><img src="{CABIN}" alt=""><figcaption>Business class</figcaption></figure><figure><img src="{MALDIVES}" alt=""><figcaption>Maldives</figcaption></figure></div>
<div class="ecard"><div class="ehead" style="background-image:url('{SUNSET}')"><span><small>The Found Money Drop</small>Found Money Call</span></div>
<div class="ebody"><h3>Claim your free 20-minute call</h3>
<div class="erow"><div><b>Free</b><span>The call</span></div><div><b>20 min</b><span>One call</span></div><div><b>50+</b><span>Programs</span></div></div>
<form id="entryform" novalidate>
<div class="field"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg><input id="em" name="em" type="email" required autocomplete="email" placeholder="Your work email" aria-label="Your work email"></div>
<button class="pillbtn" type="submit" value="call">{CTA} <span class="ar" aria-hidden="true">→</span></button>
<div class="or">or</div>
<button class="gbtn" type="button" id="gbtn">{GOOGLE_G}Continue with Google</button>
<div class="nl"><p><b>Not ready for a call?</b>Get The Daily Redemption instead: one real redemption every weekday, and new Golden Nugget packs as they land.</p><button type="submit" value="news">Just the newsletter</button></div>
<div class="notice" id="notice" role="status"></div>
</form>
<p class="efine">You get The Daily Redemption, every weekday. Leave whenever you like. Ask and we delete your data within 30 days.</p>
</div></div>
<div class="post r" aria-hidden="true"><figure><img src="{SANTORINI}" alt=""><figcaption>Santorini</figcaption></figure><figure><img src="{SUNSET}" alt=""><figcaption>Sunset beach</figcaption></figure></div>
</div>
<div class="after"><a class="pillbtn" href="#entry">{CTA} <span class="ar" aria-hidden="true">→</span></a></div>
</div></section>"""

    faqsec = f"""<section class="sec" id="faq" style="padding-top:clamp(32px,4vw,56px)"><div class="wrap"><div class="sh">{brk('Questions')}<h2>Plain answers. <span class="p">No fine print games.</span></h2></div>
<div class="faq">{faq()}</div></div></section>"""

    foot = """<footer><div class="wrap"><div class="fwrap"><a class="logo" href="#top" style="color:var(--fg)" aria-label="First Officer"><img src="%s" alt="" width="22" height="29"><span><b>First Officer</b><small>by UpNonStop™</small></span></a>
<p class="faddr">UpNonStop | 235 Pavonia Avenue | Jersey City, NJ 07302 | Proudly Made in 🇺🇸</p></div>
<p class="fnote">Mockup preview, not live. Every dollar figure on this page is an estimate. General information, not tax, legal or financial advice.</p></div></footer>""" % CHEV

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(title)}</title><meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="{'#000000' if A else '#FAF6EE'}">
<link rel="icon" href="{CHEV}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://images.unsplash.com">
<style>{CSS}{THEME_A if A else THEME_B}</style></head>
<body class="t{theme}"><a class="skip" href="#entry">Skip to the sign-up</a>
<main>{hero}{calc}{mq}{nug}{entry}{faqsec}</main>{foot}
<script>{JS.replace('__LIVE__', 'true' if SIGNUP_LIVE else 'false')}</script>
</body></html>"""

GALLERY = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Found Money Drop: mockups A and B</title><meta name="robots" content="noindex,nofollow"><link rel="icon" href="%(chev)s">
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,800&family=JetBrains+Mono:wght@600&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box;margin:0}body{font-family:'DM Sans',sans-serif;background:#FAF6EE;color:#141216;padding:40px 20px 60px}
.w{max-width:1200px;margin:0 auto}.k{font:600 11px 'JetBrains Mono',monospace;letter-spacing:.18em;text-transform:uppercase;color:#5e5864}
h1{font-family:'DM Serif Display',serif;font-weight:400;font-size:clamp(40px,6vw,72px);line-height:1;margin-top:10px}h1 span{color:#E60F86;display:block}
.lede{max-width:70ch;margin-top:14px;color:#3d3842;font-size:17px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:32px}
.c{display:block;text-decoration:none;color:inherit;background:#fff;border:2px solid #141216;border-radius:24px;overflow:hidden;box-shadow:8px 8px 0 #141216;transition:transform .15s}.c:hover{transform:translate(-2px,-2px)}
.sh{display:grid;grid-template-columns:3fr 1fr;gap:0;background:#141216}.sh img{width:100%%;height:340px;object-fit:cover;object-position:top;display:block}.sh img+img{border-left:2px solid #141216}
.b{padding:20px 22px 24px}.b h2{font-family:'DM Serif Display',serif;font-weight:400;font-size:32px;line-height:1.05}.b p{color:#5e5864;margin-top:8px}
.go{display:inline-block;margin-top:14px;background:#E60F86;color:#fff;font-weight:800;padding:12px 20px;border-radius:999px}
ul{margin:28px 0 0;padding-left:20px;max-width:80ch;color:#3d3842}li{margin-top:6px}
@media(max-width:760px){.g{grid-template-columns:1fr}.sh img{height:240px}}</style></head><body><div class="w">
<span class="k">[ Mockups · not live · branch mockups/signup-campaign ]</span>
<h1>The Found Money Drop.<span>Two directions.</span></h1>
<p class="lede">One page, one action: claim the free 20-minute Found Money Call, or get The Daily Redemption. Same structure in both: cinematic hero on the landing page's vacation photos, spend slider (example data, est.), 50+ programs marquee, Golden Nugget carousel, one entry card, FAQ.</p>
<div class="g">
<a class="c" href="found-money-drop-a.html"><div class="sh"><img src="shots/fmd-a-1440-hero.jpg" alt="Version A, desktop"><img src="shots/fmd-a-390-hero.jpg" alt="Version A, phone"></div><div class="b"><span class="k">Version A</span><h2>Dark cinematic</h2><p>Pure black, pink #FA1896 as the glow. Chrome 3D wordmark with a pink halo.</p><span class="go">Open A →</span></div></a>
<a class="c" href="found-money-drop-b.html"><div class="sh"><img src="shots/fmd-b-1440-hero.jpg" alt="Version B, desktop"><img src="shots/fmd-b-390-hero.jpg" alt="Version B, phone"></div><div class="b"><span class="k">Version B</span><h2>Light, our brand</h2><p>Cream, ink and block pink with flat gold. Ink and pink 3D wordmark, bold offset shadows.</p><span class="go">Open B →</span></div></a>
</div>
<ul><li>Mockups only: the form never sends anything, it shows a notice.</li><li>No countdown, no timed popup, no seats or availability. Every dollar figure is labelled est.; the slider is example data.</li><li>Hero photos are the landing page's own 31-photo vacation set, slow crossfade, with a pause button. Reduced motion stops all movement.</li></ul>
</div></body></html>"""

if __name__ == '__main__':
    (ROOT / 'found-money-drop-a.html').write_text(page('A'))
    (ROOT / 'found-money-drop-b.html').write_text(page('B'))
    (ROOT / 'index.html').write_text(GALLERY % {'chev': CHEV})
    print('built')
