import sys; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fosite import *
LINES=[('Dental supply distributors','',34000,2,80000),('Lab fees','',13000,2,40000),('Implants and orthodontic materials','',11000,2,40000),('Practice software and imaging','up to 4x',4500,4,12500),('Utilities and phones','',3500,2,15000),('Everything else','',5000,2,30000)]
SH=['Supply distributors','Lab fees','Implants & ortho','Software & imaging','Utilities & phones','Everything else']
def xp(x): return f'<span class="pill" style="--c:{"var(--earn)" if x>2 else "var(--ink3)"}">{x}x</span>'

prof=''.join(row(SH[k],'',f'${v:,}',"var(--earn)",f'<span style="display:block;margin-top:6px">{xp(x)}</span>'+meter(v/34000*100,"var(--earn)",k*.08)) for k,(n,_,v,x,_m) in enumerate(LINES))
hero=f'''<section class="sec" id="dtop" style="padding-top:28px">{ph(['i-dental2','i-dental3','i-medical','i-dental'],6500)}<div class="wrap"><div class="split">
<div class="head" data-rv style="margin-bottom:0"><span class="hlab"><span class="lab earn">First Officer for Dental</span><span class="stamp" aria-label="Dental, cleared for takeoff"><i>Dental</i>cleared for takeoff</span></span><h1 class="h1">Henry Schein Bills. Lab Fees. <em>All Earning Minimum Points.</em></h1>
<p class="lede">A practice profile at $71,000 a month of card-able spend earns about 151,000 points a month with every bonus rate capped on published terms, and nets about $2,222 a month after our fee at our current valuation. The routing is the work. The receipt is on the calculator.</p>
<div class="btns"><a class="btn" href="book.html">The Found Money Call</a><a class="btn ghost" href="#numbers">Try the Calculator</a></div></div>
<div class="stack">
<div class="card hero worth bp" data-rv><div style="display:flex;justify-content:space-between;align-items:center"><span class="lab earn">Worth it · a dental practice</span><span class="pill" style="--c:var(--earn)">Worth it</span></div>
<div class="bpr" aria-label="From $71,000 a month of card-able spend to 151,000 points a month, caps applied"><div><small>From</small><b class="tn">$71,000</b><span>spend a month</span></div>
<div class="route" aria-hidden="true"><span class="rd o"></span><span class="rl r1"></span><span class="rp"><svg viewBox="0 0 24 24" width="18" height="18"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/></svg></span><span class="rl r2"></span><span class="rd d"></span></div>
<div class="to"><small>To</small><b class="tn">151,000</b><span>points a month</span></div></div>
<div class="tear" aria-hidden="true"></div>
<div class="k" style="margin-top:6px">Net, this year</div><span class="num xl tn" data-dg>$<span data-cu="26668">26,668</span></span>
<div class="wbar" aria-hidden="true"><i class="v" style="--w:80.2%"></i><i class="f" style="--w:19.8%"></i></div>
<div class="wlg"><span><i style="background:var(--earn)"></i>Net to you</span><span><i style="background:var(--ink2)"></i>Our fee, out first</span></div>
<div style="margin-top:10px">{kv('Valued honestly, 60% you would have bought anyway','$33,268')}{kv('Our fee, twelve months','−$6,600','neg')}{kv('Net, this month, after our fee','$2,222<small>/mo</small>','tot')}</div>
<p class="cap" style="margin-top:10px">151,000 points a month, caps applied. Estimated, illustrative.</p></div>
<div class="card" data-rv><div style="display:flex;justify-content:space-between;align-items:center"><span class="lab">The starting profile · per month</span><span class="pill" style="--c:var(--gold2)">Illustrative</span></div>
<div class="rows" style="margin-top:4px">{prof}</div>
{kv('Points a month, caps applied','151,000','tot')}</div>
</div></div></div></section>'''

NUG=[('8071','','Lab cases code 8071','Paying a dental lab by card codes as Medical and Dental Laboratories.'),('5047',' / 5122','Supplies vs drugs','Supply distributors are 5047. Drug distributors are 5122.'),('8021','','Your patients see you as 8021',"Dentists and Orthodontists is your own terminal's code.")]
nug=f'''<section class="sec" id="codes">{ph(['i-dental3','e-tablet'])}<div class="wrap">
{head('Golden nuggets','What most dental practices never hear <em>about their codes.</em>',labc='gold')}
<div class="g3">{''.join(f'<div class="card" data-rv><span class="lab gold">🪙 Merchant code</span><span class="num m tn" style="margin-top:6px">{c}<small>{s.strip(" /") and "/ "+s.strip(" /")}</small></span><h3 class="h3" style="margin-top:8px">{h}</h3><p>{p}</p></div>' for c,s,h,p in NUG)}</div>
<p class="cap" style="margin-top:14px">Check your own statements; the desk verifies every one before routing.</p></div></section>'''

cls=''.join(f'''<div class="cl" style="padding:14px 0;border-top:1px solid var(--line)"><div style="display:flex;justify-content:space-between;gap:10px;align-items:baseline"><span><b style="display:block;font:600 15px/1.35 var(--font)">{n}</b><small class="cap" style="margin:0">{"up to 4x" if x>2 else "2x"} · caps applied</small></span><span style="text-align:right"><b class="cv tn" style="font:700 17px/1.2 var(--font)">${v:,}</b> {xp(x)}</span></div>
<input class="rng" type="range" min="0" max="{m}" step="500" value="{v}" data-x="{x}" aria-label="{n}, monthly"><div style="display:flex;align-items:center;gap:10px">{meter(0,"var(--earn)" if x>2 else "var(--gold2)")}<span class="cp cap tn" style="margin:0;white-space:nowrap;min-width:84px;text-align:right"></span></div></div>''' for n,s,v,x,m in LINES)
calc=f'''<section class="sec" id="numbers">{ph(['i-desk','e-laptop','i-dental'])}<div class="wrap">
{head('Your numbers',"See What You're <em>Leaving Behind</em>","This page's profile is the starting point on the calculator. Move the sliders to your own numbers. Every bonus rate is capped on published terms, rent and payroll stay off the card, and our fee comes out before you see a number.",labc='earn')}
<div class="split" id="dcalc">
<div class="card" data-rv><div style="display:flex;justify-content:space-between"><span class="lab">The starting profile</span><span class="lab">Monthly</span></div><div style="margin-top:10px">{cls}</div></div>
<div class="sticky"><div class="card hero top" style="--c:var(--earn)" data-rv><span class="lab earn">Net, this month, after our fee</span><span class="num tn" id="dnet" style="margin-top:8px">$2,222</span>
<div class="div"></div>
{kv('Monthly card-able spend','<span id="dsp">$71,000</span>')}{kv('Points a month, caps applied','<span id="dpts">151,000</span>')}{kv('Blended earn rate','<span id="dbl">2.1x</span>')}{kv('Net, this year','<span id="dyr">$26,668</span>','tot')}
<div class="alt3h"><span class="lab">Same spend, three ways · a year</span></div>
<div class="cmp alt3 live">{bar('No strategy','<span id="a0">$0</span>',0,sub='A debit card, earns nothing',cls='usual a0')}{bar('Cash back','<span id="a1">$17,040</span>',17040/26668*100,sub='At 2% cash back on card-able spend',cls='usual a1',dl=.12)}{bar('Bespoke strategy','<span id="a2">$26,668</span>',100,'var(--earn)',sub='Routed, after our fee',cls='a2',dl=.25)}</div>
<a class="btn" href="calculator.html" style="margin-top:16px">Run your numbers →</a>
<p class="cap" style="margin-top:10px">Estimated, illustrative. Points × 3.0 cents × 85% redeemed × the honest discount, minus our $550 fee. Not a projection of your results. Cash back at 2% cash back on the monthly card-able spend, times 12. Bespoke strategy is illustrative.</p></div></div>
<div class="icta" data-rv><div><b class="lead">See this on your own numbers.</b><p class="cap">The Found Money Call: free, 20 minutes. We verify yours against real transactions.</p></div><a class="btn ghost" href="book.html?from=for-dental-numbers">Book Your "Found Money" Call →</a></div>
</div></section>'''

def bars(rows,mx):
    return '<div class="cmp">'+''.join(bar(lab,txt,max(val/mx*100,0),c,cls=('usual' if not c else ''),dl=k*.2) for k,(lab,val,txt,c) in enumerate(rows))+'</div>'
M=[('01','Putting dental supply distributors on a debit card, or on a card that earns one point on it',
 'Your biggest line, $34,000 a month, codes outside every bonus category on the cards that matter. A debit card earns nothing on it. The no-fee 2x card earns two points on the first $50,000 a year and one point after that. The flat-2x card with an annual fee earns two points on all of it. Neither is a bonus. Both beat the debit card by six figures of points a year.',
 bars([('Flat-2x card with a fee',816000,'816,000 pts','var(--burn)'),('No-fee 2x card',458000,'458,000 pts',''),('Debit card',0,'0','')],816000),
 '$408,000 a year. No-fee 2x card: 458,000 points. Flat-2x card with a fee: 816,000 points. Debit card: 0.'),
('02','Leaving the lines that earn 3x and 4x on the same card as the invoice',
 'The small lines are the ones that pay: practice software and imaging, $4,500 a month on this profile. On published terms, 4x applies on the first $150,000 a year of advertising, software, fuel and tolls combined, and 3x on the first $150,000 of shipping, travel, internet and phone combined, then 1x. This profile sits under both pools, so every dollar on these lines earns its full rate.',
 bars([('Routed',216000,'216,000 pts / yr','var(--burn)'),('Invoice card at 2x',108000,'108,000',''),('Debit card',0,'0','')],216000),
 '$4,500 a month on the bonus lines, routed: 216,000 points a year. On the invoice card at 2x: 108,000. On a debit card: 0.'),
('03','Forcing rent, payroll and non-card vendors onto the card to chase points',
 "Left off this profile: rent, staff costs. Rent and vendor bills can ride a bill-pay service at 2.9%; at this page's own defaults 2x is worth about 3.7 cents a dollar after the honest discount, so it clears by well under a cent. The desk decides those line by line.",
 bars([('2x, valued honestly',3.7,'3.7¢ a dollar','var(--burn)'),('Bill-pay fee',2.9,'−2.9¢','var(--ink2)'),('What is left',0.8,'well under a cent','var(--ink3)')],3.7),
 '2 points × 3.0 cents × 85% redeemed × the honest discount = about 3.7 cents a dollar. Minus a 2.9% bill-pay fee = well under a cent. That is not a strategy; it is a rounding error with a fee attached.')]
ms=''.join(f'<article class="card" data-rv><span class="lab burn">Mistake {n}</span><h3 class="h3" style="margin-top:6px">{h}</h3><p>{p}</p><div class="note" style="display:block;margin-top:14px;background:var(--paper)"><span class="lab">The math</span><div style="margin-top:10px">{b}</div><p class="cap" style="margin-top:10px">{t}</p></div></article>' for n,h,p,b,t in M)
mist=f'''<section class="sec" id="mistakes">{ph(['i-dental','e-tablet','i-dental2'])}<div class="wrap">
{head('The mistakes','What Dental Practices <em>Get Wrong</em>','None of this is obvious from a statement. It is what the desk sees on a practice profile, line by line.',labc='burn')}
<div class="g3">{ms}</div></div></section>'''

TRI=[('MCC','Vendor Code Analysis',"We've mapped how your vendors code with card networks. Verified, not guessed.",'var(--learn)'),('CAP','Spending Cap Tracking','Every bonus category has annual caps. We flag the pool before it fills, so the next dollar goes to the next rate down instead of to 1x.','var(--learn)'),('CPP','Transfer Partner Math','Earning is half. We show you which redemptions clear our current valuation and which do not, and we print the call before the booking.','var(--learn)')]
route=f'''<section class="sec" id="routing">{ph(['i-medical','e-phone'])}<div class="wrap">
{head('How it works','Your vendors. <em>Our routing.</em>','Every vendor sends a merchant category code (MCC) when you swipe. That code determines your multiplier. The same $5,000 payment earns 5,000 points on the wrong card or up to 20,000 on the right one, inside the pool. We match every vendor to its highest-earning card.',labc='learn')}
<div class="split"><div class="rows" data-rv>{''.join(f'<div class="row"><span class="av" style="width:44px;height:44px;border-radius:12px;background:color-mix(in srgb,{c} 12%,transparent);color:{c};display:grid;place-items:center;font:700 11.5px/1 var(--font);letter-spacing:.04em;flex:none">{a}</span><span class="bd"><span class="t">{t}</span><span class="s">{p}</span></span></div>' for a,t,p,c in TRI)}</div>
<div class="card hero" data-rv><span class="lab">One payment · MCC → multiplier</span><span class="num tn" style="margin-top:8px">$5,000</span>
<div class="pair" style="margin-top:16px"><div><div class="k">The wrong card · 1x</div><div class="v"><span data-cu="5000">5,000</span></div><div class="d">points</div></div><div><div class="k">The right card · up to 4x</div><div class="v"><span data-cu="20000">20,000</span></div><div class="d">points, inside the pool</div></div></div>
<div class="cmp" style="margin-top:16px">{bar('The wrong card · 1x','5,000 pts',25,cls='usual')}{bar('The right card · up to 4x','20,000 pts',100,'var(--learn)',dl=.25)}</div>
<p class="cap" style="margin-top:12px">Your card stack, routing rules, and redemption strategy are built specifically for your vendors and spend. <a href="book.html">See what yours looks like.</a></p></div>
</div>
<div class="dchips" data-rv><span class="pill" style="--c:var(--learn)">Vendor codes verified, not guessed</span><span class="pill" style="--c:var(--learn)">Caps flagged before the pool fills</span><span class="pill" style="--c:var(--learn)">The call printed before the booking</span></div>
<div class="card lanes" data-rv><div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="lab learn">Two lines, routed · a year</span><span class="pill" style="--c:var(--gold2)">Illustrative</span></div>
<div class="lane" style="--i:0"><div class="lsrc"><b>Dental supply distributors</b><small>$34,000 a month · codes 5047</small></div><i class="ar" aria-hidden="true"></i>
<div class="best"><span class="tg">Best lane</span><b>Flat-2x card</b><small>2x on every dollar of the line</small><span class="pt tn"><span data-cu="816000">816,000</span> pts</span></div>
<div class="alt"><span class="tg">Alternative</span><span>No-fee 2x card, 2x to $50,000 a year then 1x</span><span class="pt tn">458,000</span></div></div>
<div class="lane" style="--i:1"><div class="lsrc"><b>Practice software and imaging</b><small>$4,500 a month · the bonus lines</small></div><i class="ar" aria-hidden="true"></i>
<div class="best"><span class="tg">Best lane</span><b>4x and 3x categories</b><small>Inside the $150,000 annual caps</small><span class="pt tn"><span data-cu="216000">216,000</span> pts</span></div>
<div class="alt"><span class="tg">Alternative</span><span>Left on the invoice card at 2x</span><span class="pt tn">108,000</span></div></div>
<div class="stk"><div class="ln"><span>Points stacking up</span><b class="tn"><span data-cu="1032000">1,032,000</span> pts</b></div><div class="sb" aria-hidden="true"><i style="--w:79.1%"></i><i style="--w:20.9%"></i></div></div>
<p class="cap" style="margin-top:10px">Card types, not card names, on the published terms used in the mistakes above. Lab fees and implants are routed once the desk checks how your lab codes against real transactions. Estimated, illustrative.</p></div>
</div></section>'''

YR=[('Monthly card-able spend','$71,000'),('Annual spend','$852,000'),('Points on one card at 1x','852,000'),('Points routed, caps applied','1,812,000'),('Blended earn rate','2.1x'),('Travel value at sticker, 85% redeemed, 3.0 cents','$46,206'),('Valued honestly, 60% you would have bought anyway','$33,268'),('Our fee, twelve months','$6,600')]
yr=f'''<section class="sec" id="math">{ph(['d-santorini','d-maldives','d-kyoto','d-lisbon'])}<div class="wrap">
{head('Real math','What This Looks Like for a <em>$71,000 a Month Dental Profile</em>','Same spend. Different strategy. Different outcome.',labc='earn')}
<div class="split">
<div class="card hero" style="background:var(--cream2)" data-rv><span class="lab earn">One year, on the calculator's defaults</span><div style="margin-top:8px">{''.join(kv(a,b,'neg' if 'fee' in a else '') for a,b in YR)}{kv('Net, this year','$<span data-cu="26668">26,668</span>','tot')}</div></div>
<div class="card hero" data-rv><div style="display:flex;justify-content:space-between;align-items:center"><span class="lab">From sticker to net</span><span class="pill" style="--c:var(--gold2)">Estimated, illustrative</span></div>
<div class="cmp" style="margin-top:14px">{bar('One card at 1x','852,000 pts',47,cls='usual')}{bar('Routed, caps applied','1,812,000 pts',100,'var(--earn)',dl=.2)}</div>
<div class="div"></div>
<div class="cmp">{bar('Sticker value','$46,206',100,'#BDB7C3')}{bar('Valued honestly','$33,268',33268/46206*100,'var(--ink3)',dl=.15)}{bar('Our fee','−$6,600',6600/46206*100,'var(--ink2)',dl=.3)}{bar('Net, this year','$26,668',26668/46206*100,'var(--earn)',dl=.45)}</div>
<div class="div"></div><span class="lab">The same $852,000, three ways</span>
<div class="cmp alt3" style="margin-top:12px">{bar('No strategy','$0',0,sub='A debit card, earns nothing',cls='usual')}{bar('Cash back','$17,040',17040/26668*100,sub='At 2% cash back on $852,000',cls='usual',dl=.12)}{bar('Bespoke strategy','$26,668',100,'var(--earn)',sub='Routed, caps applied, after our fee',dl=.25)}</div>
<p class="cap" style="margin-top:10px">Bespoke strategy is illustrative, not client data.</p></div>
</div>
<p class="method" style="margin-top:18px">Illustrative profile, not client data. Point valuations are estimates based on common redemption benchmarks; actual value depends on how and when you redeem. Bonus rates capped on published product terms, before card annual fees. Not a guarantee of any outcome and not financial or tax advice.</p>
</div></section>'''

L4=[('Dental supply distributors','Commonly flagged as wholesale, which is the single most common capped category in the practice.',34000),('Lab fees','Steady per-case spend that adds up to a meaningful annual category.',13000),('Implants and orthodontic materials','High ticket, low frequency, and worth timing against a bonus.',11000),('Practice management software and imaging','Recurring, rarely routed, easy to move.',4500)]
l4=''.join(row(h,p,f'${a:,}','var(--gold2)',meter(a/34000*100,'var(--gold2)',k*.1),vsub='/mo on this profile') for k,(h,p,a) in enumerate(L4))
MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']; HOT={0:78,1:40,9:45,10:70,11:92}
cal=''.join(f'<div style="text-align:center"><div style="height:56px;background:var(--track);border-radius:6px;display:flex;align-items:flex-end;overflow:hidden"><i style="display:block;width:100%;height:{max(HOT.get(k,8),8)}%;background:{"var(--burn)" if k in HOT else "#BDB7C3"};border-radius:6px"></i></div><span class="cap" style="display:block;margin-top:4px;font-size:11px">{m}</span></div>' for k,m in enumerate(MON))
lines=f'''<section class="sec" id="lines">{ph(['i-dental2','i-dental3'])}<div class="wrap">
{head('Where the money actually goes','The 4 lines that decide <em>a dental practice year</em>','Generic card advice sorts spending into dining, travel and office supplies. That is not what your P&amp;L looks like. This is.',labc='gold')}
<div class="rows" data-rv>{l4}</div>
<div class="g3" style="margin-top:14px">
<div class="card" data-rv><span class="lab">The cash cycle</span><p style="margin-top:6px">Insurance reimbursement lags treatment by weeks, so supplies are bought ahead of payment.</p><div style="margin-top:14px">{tl([('done','Treatment','','Supplies bought'),('now','Reimbursed','','Weeks later')])}</div></div>
<div class="card" data-rv><span class="lab">The calendar</span><p style="margin-top:6px">Insurance benefit resets pull volume into Q4 and the start of the year.</p><div style="display:grid;grid-template-columns:repeat(6,1fr);gap:8px 6px;margin-top:14px">{cal}</div></div>
<div class="card" data-rv><span class="lab">A profile at $71,000 a month</span><p style="margin-top:6px">Roughly $852,000 a year of card-able spend, and the routing decision on the lines above is worth more than every other optimization combined.</p></div></div>
<p class="method" style="margin-top:18px">Coding varies by processor, location and how each vendor is registered, so we verify yours against real transactions during The Found Money Call rather than assuming. Point valuations are estimates based on common redemption benchmarks. Actual value depends on how and when you redeem. The calendar strip is illustrative.</p>
</div></section>'''

st=[('Message us','6 questions. About 20 minutes.'),('We map everything','Cards, balances, credits, programs.'),('Get your game plan','Card stack, routing rules, bonus calendar.'),('We watch. You save time.','Proactive alerts, weekly digests, strategy.')]
steps=f'''<section class="sec" id="steps">{ph(['e-coffee','e-relax','e-window'])}<div class="wrap">
{head('How it works','Four Steps to <em>Full Optimization</em>','No apps to download. No spreadsheets. Just a conversation.',labc='learn')}
<div class="card hero" style="max-width:640px" data-rv><span class="lab">How we get you there</span><div style="margin-top:14px">{tl([('now' if k==0 else '',a,b,f'Step 0{k+1}') for k,(a,b) in enumerate(st)])}</div></div></div></section>'''

V=[('2.0x','Trucking','$9,530','$275,000'),('2.2x','E-Commerce','$8,382','$224,500'),('2.2x','Agencies','$6,381','$170,000'),('2.2x','IT Services','$5,215','$144,500'),('2.1x','Contractors','$4,793','$138,000'),('1.9x','Property Management','$4,664','$147,500'),('2.2x','HVAC','$3,921','$112,500'),('2.2x','Landscaping','$2,755','$80,000'),('2.0x','Auto Repair','$2,424','$81,000'),('2.1x','Restaurants','$2,314','$74,500'),('2.2x','Veterinary','$2,259','$71,000'),('2.1x','Dental','$2,222','$71,000'),('2.0x','Medical','$2,149','$73,500'),('2.3x','Cleaning','$1,919','$59,000'),('2.7x','Real Estate','$1,855','$48,000'),('2.5x','Fitness','$1,558','$45,700'),('2.6x','Consulting','$1,534','$43,000'),('2.3x','Salons','$1,198','$41,300'),('2.3x','CPA Firms','$956','$35,500'),('2.1x','Law Firms','$891','$37,500')]
vr=''.join(f'<div class="row{" me" if n=="Dental" else ""}{" xtra" if k>=8 and n!="Dental" else ""}"><span class="tn" style="font:700 13px/1.6 var(--font);color:var(--ink3);min-width:20px">{k+1:02d}</span><span class="bd"><span class="t">{n}{" · this page" if n=="Dental" else ""}</span><span class="s">{a} a month net of our fee on a {p} profile.</span><span style="display:block;margin-top:6px"><span class="pill" style="--c:var(--earn)">{x}</span></span></span><span class="v">{a}<small>/mo</small></span></div>' for k,(x,n,a,p) in enumerate(V))
mar=f'''<section class="sec" id="verticals">{ph(['bg-03','bg-06'])}<div class="wrap">
{head('Trusted across industries','Trusted across industries','The same routing, applied to 20 verticals. Different vendors, different coding, one set of published terms, our fee already out.',labc='earn')}
<div class="card hero" data-rv><div style="display:flex;justify-content:space-between;align-items:center"><span class="lab">Ranked by net a month</span><span class="pill" style="--c:var(--gold2)">Estimated</span></div><div class="rows vlist" id="vlist" style="margin-top:4px">{vr}</div>
<button class="btn ghost" type="button" data-showall="#vlist" style="margin-top:12px">Show all 20 verticals</button></div>
<p class="lede" style="margin-top:16px" data-rv>Restaurants. HVAC. Dental. Salons. Fitness. Landscaping. Veterinary. IT. Consulting. Cleaning. Property Management. Auto Repair. <em style="font-style:normal;color:var(--ink);font-weight:600">And yours.</em></p>
</div></section>'''

cta=f'''<section class="sec" id="call">{ph(['d-bali','d-costarica','bg-05'])}<div class="wrap"><div class="card hero cta-card" data-rv>{MK}<h3 class="h2" style="font-size:24px">The Found Money Call. Free, 20 minutes.</h3><p class="lede">Pick how we talk. We'll show you what your dental practice is leaving on the table.</p><div class="btns"><a class="btn" href="book.html">Book Your "Found Money" Call</a></div></div></div></section>'''

page('for-dental.html','First Officer for Dental', hero+nug+calc+mist+route+yr+lines+steps+mar+cta, desc='What dental practices leave behind on supplies, lab fees and implants, and how the routing works.', src='for-dental')
