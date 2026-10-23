from parts import *
LINES=[('Dental supply distributors','',34000,2,80000),('Lab fees','',13000,2,40000),('Implants and orthodontic materials','',11000,2,40000),('Practice software and imaging','up to 4x',4500,4,12500),('Utilities and phones','',3500,2,15000),('Everything else','',5000,2,30000)]
SH=['Supply distributors','Lab fees','Implants & ortho','Software & imaging','Utilities & phones','Everything else']
# --- hero: routing flow
ys=[34,84,134,184,234,284]
paths='';lbl=''
for k,(n,_,v,x,_m) in enumerate(LINES):
    y=ys[k]; hi=x>2
    paths+=f'<path class="fl{" h" if hi else ""}" d="M232 {y} C300 {y} 300 160 352 160"/>'
    lbl+=f'<g class="vl" style="animation-delay:{k*.12:.2f}s"><rect x="0" y="{y-19}" width="226" height="38" rx="12"/><text class="n" x="14" y="{y+4}">{SH[k]}</text><text class="a" x="212" y="{y+4}" text-anchor="end">${v//1000}K · {x}x</text></g>'
flow=f'''<div class="gl flow" data-rv="2"><div class="fhd"><span>The starting profile · per month</span><span class="estl">Illustrative</span></div>
<svg viewBox="0 0 560 320" role="img" aria-label="Six spending lines routed through the desk to about 151,000 points a month">
{paths}<path class="fl o" d="M398 160 L430 160"/>
{lbl}
<circle cx="375" cy="160" r="30" fill="#fff" stroke="#FA1896" stroke-width="3"/><circle class="pul2" cx="375" cy="160" r="40" fill="none" stroke="rgba(250,24,150,.2)" stroke-width="8"/><image href="img/fo-chevron-alpha.png" x="359" y="144" width="32" height="32"/>
<g class="res"><rect x="436" y="118" width="124" height="84" rx="16"/><text class="k" x="498" y="142" text-anchor="middle">POINTS / MONTH</text><text class="v" x="498" y="178" text-anchor="middle">151,000</text><text class="k" x="498" y="194" text-anchor="middle">CAPS APPLIED</text></g>
</svg>
<div class="flowm">'''+''.join(f'<div class="fr"><span>{SH[k]}</span><b class="tnum">${v:,}</b><em class="{"h" if x>2 else ""}">{x}x</em><div class="fb"><i class="{"h" if x>2 else ""}" style="--w:{v/34000*100:.0f}%"></i></div></div>' for k,(n,_,v,x,_m) in enumerate(LINES))+'''<div class="fr tot"><span>Points a month, caps applied</span><b class="tnum">151,000</b></div></div>
<div class="netbig"><span>Net, this month,<br>after our fee</span><b class="tnum">$<span data-cu="2222" data-ms="2200">2,222</span><small>/mo</small></b></div></div>'''
hero=f'''<section class="sx ps" id="top" style="padding-top:20px">{ph(['i-dental2','i-dental3','i-medical','i-dental'],'',6500)}<div class="w2"><div class="ih">
<div>{kk('First Officer for Dental')}
<h1 data-rv>Henry Schein Bills. Lab Fees. <em>All Earning Minimum Points.</em></h1>
<p class="lede" data-rv="2">A practice profile at $71,000 a month of card-able spend earns about 151,000 points a month with every bonus rate capped on published terms, and nets about $2,222 a month after our fee at our current valuation. The routing is the work. The receipt is on the calculator.</p>
<div class="ctas" data-rv="3"><a class="pill pink" href="book.html">The Found Money Call</a><a class="pill ghost" href="#numbers">Try the Calculator</a></div></div>
{flow}</div></div></section>'''

nug=f'''<section class="sx tight ps" id="codes">{ph(['i-dental3','e-tablet'],'c c2')}{rail('01','Golden nuggets')}<div class="w2">
<div style="text-align:center">{kk('Golden nuggets')}</div>
<h2 class="h2x c" data-rv>What most dental practices never hear <em>about their codes.</em></h2>
<div class="nugs">
<div class="nug3" data-rv><div class="ni">🪙</div><div><div class="code">8071</div><h3>Lab cases code 8071</h3><p>Paying a dental lab by card codes as Medical and Dental Laboratories.</p></div></div>
<div class="nug3" data-rv="2"><div class="ni">🪙</div><div><div class="code">5047 <small>/ 5122</small></div><h3>Supplies vs drugs</h3><p>Supply distributors are 5047. Drug distributors are 5122.</p></div></div>
<div class="nug3" data-rv="3"><div class="ni">🪙</div><div><div class="code">8021</div><h3>Your patients see you as 8021</h3><p>Dentists and Orthodontists is your own terminal's code.</p></div></div>
</div><p class="fine c" style="margin-top:18px">Check your own statements; the desk verifies every one before routing.</p></div></section>'''

cls=''
for k,(n,s,v,x,m) in enumerate(LINES):
    cls+=f'<div class="cl"><label>{n}<small>{"up to 4x" if x>2 else "2x"} · caps applied</small></label><span class="v tnum">${v:,}</span><span class="x{" hi" if x>2 else ""}">{x}x</span><input class="rng" type="range" min="0" max="{m}" step="500" value="{v}" data-x="{x}" aria-label="{n}, monthly"><div class="pb"><i></i></div></div>'
calc=f'''<section class="sx ps" id="numbers">{ph(['i-desk','e-laptop','i-dental'],'r')}{rail('02','Your numbers')}<div class="w2">
{kk('Your numbers')}
<h2 class="h2x" data-rv>See What You're <em>Leaving Behind</em></h2>
<p class="lede" data-rv="2">This page's profile is the starting point on the calculator. Move the sliders to your own numbers. Every bonus rate is capped on published terms, rent and payroll stay off the card, and our fee comes out before you see a number.</p>
<div class="gl solid calc" id="dcalc" data-rv>
<div class="l"><div class="chd"><span>The starting profile</span><span>Monthly</span></div>{cls}</div>
<div class="r"><div class="k">Net, this month, after our fee</div><div class="nn pk tnum" id="dnet">$2,222</div>
<div class="row"><span>Monthly card-able spend</span><b id="dsp">$71,000</b></div>
<div class="row"><span>Points a month, caps applied</span><b id="dpts">151,000</b></div>
<div class="row"><span>Blended earn rate</span><b id="dbl">2.1x</b></div>
<div class="row"><span>Net, this year</span><b id="dyr">$26,668</b></div>
<a class="pill pink" href="calculator.html">Run your numbers →</a>
<p class="fine">Estimated, illustrative. Points × 3.0 cents × 85% redeemed × the honest discount, minus our $550 fee. Not a projection of your results.</p></div>
</div></div></section>'''

def bars(rows,mx):
    o=''
    for lab,val,txt,c in rows:
        o+=f'<div class="r"><span>{lab}</span><div class="t" style="--w:{max(val/mx*100,0):.1f}%"><i class="{c}"></i><b>{txt}</b></div></div>'
    return '<div class="bars">'+o+'</div>'
M=[('01','Putting dental supply distributors on a debit card, or on a card that earns one point on it',
 'Your biggest line, $34,000 a month, codes outside every bonus category on the cards that matter. A debit card earns nothing on it. The no-fee 2x card earns two points on the first $50,000 a year and one point after that. The flat-2x card with an annual fee earns two points on all of it. Neither is a bonus. Both beat the debit card by six figures of points a year.',
 bars([('Flat-2x card with a fee',816000,'816,000 pts',''),('No-fee 2x card',458000,'458,000 pts','g'),('Debit card',0,'0','g')],816000),
 '$408,000 a year. No-fee 2x card: 458,000 points. Flat-2x card with a fee: 816,000 points. Debit card: 0.'),
('02','Leaving the lines that earn 3x and 4x on the same card as the invoice',
 'The small lines are the ones that pay: practice software and imaging, $4,500 a month on this profile. On published terms, 4x applies on the first $150,000 a year of advertising, software, fuel and tolls combined, and 3x on the first $150,000 of shipping, travel, internet and phone combined, then 1x. This profile sits under both pools, so every dollar on these lines earns its full rate.',
 bars([('Routed',216000,'216,000 pts / yr',''),('Invoice card at 2x',108000,'108,000','g'),('Debit card',0,'0','g')],216000),
 '$4,500 a month on the bonus lines, routed: 216,000 points a year. On the invoice card at 2x: 108,000. On a debit card: 0.'),
('03','Forcing rent, payroll and non-card vendors onto the card to chase points',
 'Left off this profile: rent, staff costs. Rent and vendor bills can ride a bill-pay service at 2.9%; at this page\'s own defaults 2x is worth about 3.7 cents a dollar after the honest discount, so it clears by well under a cent. The desk decides those line by line.',
 bars([('2x, valued honestly',3.7,'3.7¢ a dollar',''),('Bill-pay fee',2.9,'−2.9¢','g'),('What is left',0.8,'well under a cent','ink')],3.7),
 '2 points × 3.0 cents × 85% redeemed × the honest discount = about 3.7 cents a dollar. Minus a 2.9% bill-pay fee = well under a cent. That is not a strategy; it is a rounding error with a fee attached.')]
ms=''.join(f'<div class="gl ms" data-io data-rv><div class="n">{n}</div><div><h3>{h}</h3><p>{p}</p></div><div class="math"><div class="k">The math</div>{b}<p>{t}</p></div></div>' for n,h,p,b,t in M)
mist=f'''<section class="sx ps" id="mistakes">{ph(['i-dental','e-tablet','i-dental2'],'c c2')}{rail('03','The mistakes')}<div class="w2">
<div style="text-align:center">{kk('The mistakes')}</div>
<h2 class="h2x c" data-rv>What Dental Practices <em>Get Wrong</em></h2>
<p class="lede c" data-rv="2">None of this is obvious from a statement. It is what the desk sees on a practice profile, line by line.</p>
<div class="mist">{ms}</div></div></section>'''

route=f'''<section class="sx ps" id="routing">{ph(['i-medical','e-phone'],'r')}{rail('04','How it works')}<div class="w2"><div class="route">
<div>{kk('How it works')}<h2 class="h2x" data-rv>Your vendors. <em>Our routing.</em></h2>
<p class="lede" data-rv="2">Every vendor sends a merchant category code (MCC) when you swipe. That code determines your multiplier. The same $5,000 payment earns 5,000 points on the wrong card or up to 20,000 on the right one, inside the pool. We match every vendor to its highest-earning card.</p>
<div class="trio" style="margin-top:26px">
<div class="gl tri" data-rv><div class="ab">MCC</div><div><b>Vendor Code Analysis</b><p>We've mapped how your vendors code with card networks. Verified, not guessed.</p></div></div>
<div class="gl tri" data-rv="2"><div class="ab">CAP</div><div><b>Spending Cap Tracking</b><p>Every bonus category has annual caps. We flag the pool before it fills, so the next dollar goes to the next rate down instead of to 1x.</p></div></div>
<div class="gl tri" data-rv="3"><div class="ab">CPP</div><div><b>Transfer Partner Math</b><p>Earning is half. We show you which redemptions clear our current valuation and which do not, and we print the call before the booking.</p></div></div></div></div>
<div><div class="gl solid swipe" data-io data-rv="2">
<div class="pay"><div><span>One payment</span><br><b>$5,000</b></div><span class="mcc">MCC → multiplier</span></div>
<div class="cards2"><div class="cd wr"><span class="emv"></span><div><div class="k">The wrong card · 1x</div><b class="tnum"><span data-cu="5000" data-ms="1400">5,000</span></b><div class="k">points</div></div></div>
<div class="cd rt"><span class="emv"></span><div><div class="k">The right card · up to 4x</div><b class="tnum"><span data-cu="20000" data-ms="2200">20,000</span></b><div class="k">points, inside the pool</div></div></div></div>
<div class="sbar"><i style="--w:25%"></i><i class="pk" style="--w:100%"></i></div>
<p class="fine" style="margin:12px 0 0">Your card stack, routing rules, and redemption strategy are built specifically for your vendors and spend. <a href="book.html">See what yours looks like.</a></p></div></div>
</div></div></section>'''

rows=[('Monthly card-able spend','$71,000'),('Annual spend','$852,000'),('Points on one card at 1x','852,000'),('Points routed, caps applied','1,812,000'),('Blended earn rate','2.1x'),('Travel value at sticker, 85% redeemed, 3.0 cents','$46,206'),('Valued honestly, 60% you would have bought anyway','$33,268'),('Our fee, twelve months','$6,600')]
yrt=''.join(f'<div class="row"><span>{a}</span><b>{b}</b></div>' for a,b in rows)+'<div class="row tot"><span>Net, this year</span><b class="tnum">$<span data-cu="26668" data-ms="2400">26,668</span></b></div>'
cols=[('$46,206','',46206,'Sticker value'),('$33,268','m',33268,'Valued honestly'),('−$6,600','f',6600,'Our fee'),('$26,668','',26668,'Net, this year')]
cc=''.join(f'<div class="col"><div class="vl">{v}</div><div class="bar {c}" style="--h:{h/46206*100:.1f}%;transition-delay:{k*.25:.2f}s"></div></div>' for k,(v,c,h,_) in enumerate(cols))
ll=''.join(f'<span>{l}</span>' for *_,l in cols)
yr=f'''<section class="sx ps" id="math">{ph(['d-santorini','d-maldives','d-kyoto','d-lisbon'],'c c2')}{rail('05','Real math')}<div class="w2">
<div style="text-align:center">{kk('Real math')}</div>
<h2 class="h2x c" data-rv>What This Looks Like for a <em>$71,000 a Month Dental Profile</em></h2>
<p class="lede c" data-rv="2">Same spend. Different strategy. Different outcome.</p>
<div class="yr"><div class="gl solid yrt" data-rv><div class="chd"><span>One year, on the calculator's defaults</span></div>{yrt}</div>
<div class="gl wfv" data-io data-rv="2"><div class="chd"><span>From sticker to net</span><span class="estl">Estimated, illustrative</span></div>
<div class="ptsvs"><div class="pv"><span>One card at 1x</span><div class="t"><i class="g" style="--w:47%"></i><b>852,000 pts</b></div></div><div class="pv"><span>Routed, caps applied</span><div class="t"><i style="--w:100%"></i><b>1,812,000 pts</b></div></div></div>
<div class="cols">{cc}</div><div class="lbls">{ll}</div></div></div>
<p class="fine c" style="margin-top:22px;max-width:860px;margin-left:auto;margin-right:auto">Illustrative profile, not client data. Point valuations are estimates based on common redemption benchmarks; actual value depends on how and when you redeem. Bonus rates capped on published product terms, before card annual fees. Not a guarantee of any outcome and not financial or tax advice.</p>
</div></section>'''

L4=[('Dental supply distributors','Commonly flagged as wholesale, which is the single most common capped category in the practice.',34000),('Lab fees','Steady per-case spend that adds up to a meaningful annual category.',13000),('Implants and orthodontic materials','High ticket, low frequency, and worth timing against a bonus.',11000),('Practice management software and imaging','Recurring, rarely routed, easy to move.',4500)]
l4=''.join(f'<div class="gl l4" data-rv="{k+1}"><div class="n">0{k+1}</div><h4>{h}</h4><p>{p}</p><div class="amt tnum">${a:,}<small>/mo on this profile</small></div><div class="l4b"><i style="--w:{a/34000*100:.0f}%"></i></div></div>' for k,(h,p,a) in enumerate(L4))
MON=['J','F','M','A','M','J','J','A','S','O','N','D']; HOT={0:'78%',1:'40%',9:'45%',10:'70%',11:'92%'}
cal=''.join(f'<i class="{"hot" if k in HOT else ""}" style="--h:{HOT.get(k,"0%")}">{m}</i>' for k,m in enumerate(MON))
lines=f'''<section class="sx ps" id="lines">{ph(['i-dental2','i-dental3'],'')}{rail('06','Where the money goes')}<div class="w2">
{kk('Where the money actually goes')}
<h2 class="h2x" data-rv>The 4 lines that decide <em>a dental practice year</em></h2>
<p class="lede" data-rv="2">Generic card advice sorts spending into dining, travel and office supplies. That is not what your P&amp;L looks like. This is.</p>
<div class="lines4" data-io>{l4}</div>
<div class="ctx">
<div class="gl" data-rv><b>The cash cycle</b><p>Insurance reimbursement lags treatment by weeks, so supplies are bought ahead of payment.</p><div class="lag"><span>Treatment</span><i></i><span>Reimbursed</span></div></div>
<div class="gl" data-rv="2"><b>The calendar</b><p>Insurance benefit resets pull volume into Q4 and the start of the year.</p><div class="cal">{cal}</div></div>
<div class="gl" data-rv="3"><b>A profile at $71,000 a month</b><p>Roughly $852,000 a year of card-able spend, and the routing decision on the lines above is worth more than every other optimization combined.</p></div></div>
<p class="fine" style="margin-top:18px">Coding varies by processor, location and how each vendor is registered, so we verify yours against real transactions during The Found Money Call rather than assuming. Point valuations are estimates based on common redemption benchmarks. Actual value depends on how and when you redeem. The calendar strip is illustrative.</p>
</div></section>'''

st=[('Message us','6 questions. About 20 minutes.'),('We map everything','Cards, balances, credits, programs.'),('Get your game plan','Card stack, routing rules, bonus calendar.'),('We watch. You save time.','Proactive alerts, weekly digests, strategy.')]
steps=f'''<section class="sx tight ps" id="steps">{ph(['e-coffee','e-relax','e-window'],'c c2')}{rail('07','Four steps')}<div class="w2">
<div style="text-align:center">{kk('How it works')}</div>
<h2 class="h2x c" data-rv>Four Steps to <em>Full Optimization</em></h2>
<p class="lede c" data-rv="2">No apps to download. No spreadsheets. Just a conversation.</p>
<div class="st4" data-io>{"".join(f'<div class="gl" data-rv="{k+1}"><div class="n">0{k+1}</div><h4>{a}</h4><p>{b}</p></div>' for k,(a,b) in enumerate(st))}</div></div></section>'''

V=[('2.0x','Trucking','$9,530','$275,000'),('2.2x','E-Commerce','$8,382','$224,500'),('2.2x','Agencies','$6,381','$170,000'),('2.2x','IT Services','$5,215','$144,500'),('2.1x','Contractors','$4,793','$138,000'),('1.9x','Property Management','$4,664','$147,500'),('2.2x','HVAC','$3,921','$112,500'),('2.2x','Landscaping','$2,755','$80,000'),('2.0x','Auto Repair','$2,424','$81,000'),('2.1x','Restaurants','$2,314','$74,500'),('2.2x','Veterinary','$2,259','$71,000'),('2.1x','Dental','$2,222','$71,000'),('2.0x','Medical','$2,149','$73,500'),('2.3x','Cleaning','$1,919','$59,000'),('2.7x','Real Estate','$1,855','$48,000'),('2.5x','Fitness','$1,558','$45,700'),('2.6x','Consulting','$1,534','$43,000'),('2.3x','Salons','$1,198','$41,300'),('2.3x','CPA Firms','$956','$35,500'),('2.1x','Law Firms','$891','$37,500')]
vc=''.join(f'<div class="vc{" me" if n=="Dental" else ""}"><div class="x">{x}</div><b>{n}</b><small>{a} a month net of our fee on a {p} profile.</small></div>' for x,n,a,p in V)
mar=f'''<section class="sx tight ps" id="verticals">{ph(['bg-03','bg-06'],'c c2')}{rail('08','20 verticals')}<div class="w2">
<div style="text-align:center">{kk('Trusted across industries')}</div>
<h2 class="h2x c" data-rv>Trusted across industries</h2>
<p class="lede c" data-rv="2">The same routing, applied to 20 verticals. Different vendors, different coding, one set of published terms, our fee already out.</p></div>
<div class="vmar"><div class="in2">{vc}{vc}</div></div>
<div class="w2"><p class="vtag" data-rv>Restaurants. HVAC. Dental. Salons. Fitness. Landscaping. Veterinary. IT. Consulting. Cleaning. Property Management. Auto Repair. <em>And yours.</em></p></div></section>'''

cta=f'''<section class="sx tight ps" id="call">{ph(['d-bali','d-costarica','bg-05'],'c c2')}<div class="w2"><div class="gl ctaw" data-rv><div><h3>The Found Money Call. Free, 20 minutes.</h3><p>Pick how we talk. We'll show you what your dental practice is leaving on the table.</p></div><a class="pill pink" href="book.html">Book Your "Found Money" Call</a></div></div></section>'''

html=page('First Officer for Dental', hero+nug+calc+mist+route+yr+lines+steps+mar+cta, desc='What dental practices leave behind on supplies, lab fees and implants, and how the routing works.', src='for-dental')
open('/workspace/fo-rebuild-v2/for-dental.html','w').write(html); print(len(html))
