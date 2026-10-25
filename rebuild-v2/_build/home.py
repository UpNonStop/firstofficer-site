import json, math
from parts import *
CHAT=[
 [["in","Strategist","Your statement closes Thursday. Push the equipment purchase to Friday and it lands in the next bonus window."],["out",None,"Will do."],["in","Strategist","I will confirm when it posts."]],
 [["in","Strategist","Minimum spend on the new card is $15,000 in 90 days. You are at $11,200 with 34 days left. On pace."],["out",None,"Anything I should do?"],["in","Strategist","Nothing. Your normal vendor run covers it."]],
 [["in","Strategist","Fleet fuel is on the 1x card. The fleet card pays 3x on fuel and you already have it."],["out",None,"Switch it."],["in","Strategist","Switched. About $84 a month back."]],
 [["in","Strategist","New vendor detected: $18,400 to a marketing agency last month. That belongs on the 4x card."],["out",None,"Set it up."],["in","Strategist","Routed. Worth about $640 a year at current spend."]],
 [["in","Optioneer","Two ways to book Barcelona: 102,000 points with a transfer bonus, or 138,000 without. Bonus ends Sunday."],["out",None,"Use the bonus."],["in","Desk","Approved. The desk books it with the bonus. 36,000 points saved, about $1,300, est."]],
 [["in","Strategist","Your software subscriptions are on a 1x card. Moving them is worth about $420 a year."],["out",None,"Do it, but not the payroll one."],["in","Strategist","Understood. Payroll stays where it is."]],
 [["in","Strategist","12 month plan is updated. Two applications, one transfer bonus, and the Q1 renewal routed differently."],["out",None,"Send it over."],["in","Strategist","Sent. Every line shows its math."]],
 [["in","Capture Report","Week 33: $3,900 captured. Vendor routing $310, transfer bonus $980, hotel nights $1,450, credits $220, expiring balance rescued $940."],["out",None,"Nice week."],["in","Strategist","Next week we look at the Q4 insurance renewal."]],
]
FEAT=[dict(city=c,img='img/ph/'+i+'.webp',tag=t,pts=p,usual=u,desk=d,x=float(x),us='Statement credit, at 1¢ a point',ks=trip+', est.',tx='est. taxes '+tx) for (c,i,t,p,u,d,x,trip,tx) in [DEST[4],DEST[0],DEST[2],DEST[1],DEST[8]]]

HERO_PH=['bg-0%d'%k for k in range(1,9)]+['d-'+n for n in ['lisbon','santorini','maldives','kyoto','bali','paris','cabo','iceland','costarica','alps','rome','barcelona','dubai','nyc','connemara']]
hero=f'<section class="sec dhero secphoto" id="top" style="--ph:none">{ph(HERO_PH,"noedge",6000)}<div id="fohero"></div></section>'

stat=f'''<div class="sb2"><div class="in gl solid">
<div class="it"><div class="v pk">{miniseal()}<span>$550</span></div><div class="l">Flat monthly · Cancel anytime</div></div>
<div class="it"><div class="v"><span data-cu="20" data-ms="1200">20</span>&nbsp;min</div><div class="l">The Found Money Call, free · We size your capture first</div></div>
<div class="it"><div class="v">Friday</div><div class="l">Dollars saved reported every Friday</div></div>
<div class="it"><div class="v">Yours</div><div class="l">Every decision, always</div></div></div></div>'''

C2=2*math.pi*92
yn=f'''<section class="sx ps" id="number">{ph(['bg-04','d-costarica','bg-08','d-bali'],'')}{rail('01','Your number')}<div class="w2">
{kk('Earn · Burn · Return · Learn')}
<h2 class="h2x" data-rv>Your monthly spend on cards and vendors. <em>What that should be buying you every year.</em></h2>
<div class="yn">
<div><div class="gl dial" id="dial" data-rv>
<div class="lab">Your monthly spend on cards and vendors</div>
<div class="spend tnum" id="spv">$35,000</div>
<input class="rng" type="range" min="10000" max="150000" step="500" value="35000" aria-label="Monthly spend on cards and vendors">
<div class="rngt"><span>$10K</span><span>$75K</span><span>$150K</span></div>
<div class="gauge"><svg viewBox="0 0 230 230" role="img" aria-label="Annual value split into flights, hotel stays and everything else">
<circle cx="115" cy="115" r="92" fill="none" stroke="#f0ebe2" stroke-width="22"/>
<g transform="rotate(-90 115 115)"><circle id="a1" class="arc" cx="115" cy="115" r="92" fill="none" stroke="#FA1896" stroke-width="22" stroke-dasharray="0 {C2:.1f}"/><circle id="a2" class="arc" cx="115" cy="115" r="92" fill="none" stroke="#E8C547" stroke-width="22" stroke-dasharray="0 {C2:.1f}"/><circle id="a3" class="arc" cx="115" cy="115" r="92" fill="none" stroke="#16A06A" stroke-width="22" stroke-dasharray="0 {C2:.1f}"/></g>
<text class="ctl" x="115" y="92" text-anchor="middle">EVERY YEAR</text><text class="ctr tnum" id="yv" x="115" y="128" text-anchor="middle">$19,492</text><text class="ctl" x="115" y="150" text-anchor="middle">STICKER VALUE, EST.</text></svg>
<div class="split">
<div class="r"><span class="sw" style="background:#FA1896"></span><span class="n">In flights</span><span class="a tnum" id="fv">$11,695</span><div class="bar"><i id="b1" style="background:#FA1896;width:60%"></i></div></div>
<div class="r"><span class="sw" style="background:#E8C547"></span><span class="n">In hotel stays</span><span class="a tnum" id="hv">$5,848</span><div class="bar"><i id="b2" style="background:#E8C547;width:30%"></i></div></div>
<div class="r"><span class="sw" style="background:#16A06A"></span><span class="n">In everything else</span><span class="a tnum" id="ov">$1,949</span><div class="bar"><i id="b3" style="background:#16A06A;width:10%"></i></div></div>
</div></div>
<div class="ctas"><a class="pill pink" href="book.html?from=home-dial">Book Your "Found Money" Call</a><a class="pill outline" href="calculator.html">See the full breakdown</a></div>
<p class="meth">The Found Money Call: 20 minutes, free, no card required. Modelled at a blended 2.1x earn, 85% of points actually used, and 2.6 cents of value per point. Sticker value of the travel, before our fee. Your category mix and your redemptions will differ. The full calculator shows the number net of our fee.</p>
<div class="promise"><span class="coin">🪙</span><span><b>Our promise:</b> if the call shows our work won't clear the fee, we tell you in writing and you never pay.</span></div>
</div>
<div class="gl founder" data-rv="2"><div class="pt" aria-label="OS portrait coming">OS</div><div><q>I built this so the money your business already spends finally works for you. If it won't, I'll tell you.</q><div class="by">Ohad Sternberg · Founder · draft line</div><p>Before First Officer, Ohad built fraud and authentication products for financial institutions (<a href="about.html">public profile</a>). The same rule applies here: read-only access, no passwords, nothing moves without your written yes.</p></div></div>
</div>
<div class="phwrap" data-rv="2"><div style="position:relative">{seal_svg()}<div class="iph"><div class="isl"></div><div class="scr">
<div class="wah"><div class="av"><img src="img/fo-chevron-alpha.png" alt=""></div><div><b>First Officer</b><small>Online</small></div></div>
<div class="wac" aria-live="polite"></div><div class="wacap">Simulated conversation. Actual results vary by portfolio.</div></div></div></div>
<div class="phcap">This is the entire product. One thread, no app to install.</div></div>
</div></div></section>'''

portal=f'''<section class="sx ps" id="portal">{ph(['d-lisbon','bg-02','d-rome','bg-06'],'r')}{rail('02','How the game is built')}<div class="w2">
<div class="hw"><div class="stick">
{kk('How the game is built')}
<h2 class="h2x" data-rv>The house wins twice. <em>Nobody tells you when.</em></h2>
<p class="lede" data-rv>This is not a conspiracy. It is a business model, published in the annual reports, and it runs on you being busy.</p>
<div class="gl spread" data-io data-rv="2"><div class="same">The spread, in cents per mile</div>
<div class="spr"><div class="r"><span>Banks pay the program</span><div class="t"><i style="left:37.5%;width:37.5%;background:#141216;transition-delay:0s">1.25–2¢</i></div></div><div class="r"><span>Typical redemption</span><div class="t"><i style="left:30.0%;width:20.0%;background:#a39cab;transition-delay:0.3s">1.1–1.5¢</i></div></div><div class="r"><span>Chapter 04: above the spread</span><div class="t"><i style="left:75.0%;width:25.0%;background:linear-gradient(90deg,#FA1896,#ff8fcb);transition-delay:0.6s">2¢ +</i></div></div><div class="ax"><span></span><div><span>0.5¢</span><span>1.0¢</span><span>1.5¢</span><span>2.0¢</span><span>2.5¢</span></div></div></div>
<p class="fine" style="margin:10px 0 0">Banks buy miles at 1.25 to 2 cents; typical redemption value runs 1.1 to 1.5. The gap is the business model. Chapter 04 is the way out.</p></div>
</div>
<div>
<article class="gl chap" data-rv><span class="no">01</span><h3>Miles are a product. You are not the customer.</h3>
<div class="big tnum">$<span data-cu="7.4" data-d="1">7.4</span>B<small>collected by one airline from its card partner in 2024, larger than its entire operating profit that year.</small></div>
<p>Airlines do not give miles away, they sell them in bulk to banks. Delta collected roughly $7.4 billion from its card partner in 2024, larger than the airline's entire operating profit that year. American and United run the same play. When the planes were grounded they mortgaged the loyalty programs alongside everything else: $9 billion raised against SkyMiles and $6.8 billion against MileagePlus in 2020, then $10 billion against AAdvantage in March 2021.</p>
<div class="src">Delta figure from its 2024 Form 10-K. Loyalty financings from the 2020 and 2021 offering documents.</div></article>
<article class="gl chap" data-rv><span class="no">02</span><h3>They win on the spread.</h3>
<div class="mg" data-io><div class="r"><span>Loyalty program A, 2019</span><div class="t"><i style="--w:49%"></i></div><b>49%</b></div><div class="r"><span>Loyalty program B, 2019</span><div class="t"><i style="--w:34%"></i></div><b>34%</b></div><div class="r"><span>The airlines, 2024</span><div class="t"><i class="g" style="--w:9.7%"></i></div><b style="font-size:16px">4.8–9.7%</b></div></div>
<p>Programs sell miles to the banks for somewhere between 1.25 and 2 cents each, and independent valuations put typical redemption value at 1.1 to 1.5. Neither number appears in any filing, because co-brand pricing is confidential, but the direction of the gap is the business model and it repeats across every mile issued. In the 2019 figures the airlines showed bond investors, AAdvantage ran a 49 percent EBITDA margin and MileagePlus 34. The airlines themselves earned operating margins of 4.8 to 9.7 percent in 2024.</p>
<div class="src">Margins from the 2019 AAdvantage and MileagePlus investor presentations.</div></article>
<article class="gl chap" data-rv><span class="no">03</span><h3>They win again when you forget.</h3>
<div class="brk" data-io><svg viewBox="0 0 120 120" aria-label="About a quarter of points issued are never used"><circle cx="60" cy="60" r="46" fill="none" stroke="#efe8dc" stroke-width="18"/><circle cx="60" cy="60" r="46" fill="none" stroke="#FA1896" stroke-width="18" stroke-dasharray="72.3 216.8" transform="rotate(-90 60 60)"/><text x="60" y="66" text-anchor="middle" style="font:400 26px 'DM Serif Display',serif" fill="#141216">¼</text></svg>
<div><div class="big" style="font-size:64px"><span data-cu="30">30</span> trillion</div><div class="fine" style="font-size:13px">miles estimated sitting unredeemed in 2018. Breakage runs a quarter to a third of everything issued.</div></div></div>
<p>Points earned and never used have a name on the balance sheet: breakage. An industry study estimated in 2018 that more than 30 trillion frequent flyer miles were sitting unredeemed, and it is still the most-cited figure in the industry. Breakage typically runs a quarter to a third of everything issued, around 25 percent in retail programs and 15 to 30 in airline ones, and every one of those forgotten points is margin nobody has to deliver. Your balance is in that number.</p>
<div class="src">Breakage and unredeemed miles from a 2018 industry study. See the Ghost Economy on The Daily Redemption for the full working.</div></article>
<article class="gl chap win" data-rv><span class="no">04</span><h3>One move beats the house.</h3>
<p>Redeem above the spread. Move the points into the airline or hotel program itself, at the right moment, against the right chart, on the right dates, and the value lands on your side of the table instead of theirs. That takes somebody watching all day, every day. That is the entire job you are hiring.</p></article>
</div></div>
<div class="closer" data-rv><h2 class="h2x c">2 departments are working on your points. <em>Until now, neither one worked for you.</em></h2></div>
</div></section>'''

f0=FEAT[0]
fomo=f'''<section class="sx ps" id="fomo">{ph(['d-santorini','d-kyoto','d-maldives'],'c')}{rail('03','The difference is the search')}<div class="w2">
<div style="text-align:center">{kk('The difference is the search')}</div>
<h2 class="h2x c" data-rv>Same points. <em>Two very different bookings.</em></h2>
<p class="lede c" data-rv>We do not set the prices and we do not control award space. We know where to look, and that is the whole gap.</p>
<div class="fst gl solid" id="feat" data-rv>
<div class="fsp"><img src="{f0['img']}" alt="{f0['city']}"><div class="glow"></div>
<div class="ftabs">{''.join(f'<button type="button"{" class=on" if k==0 else ""}>{d["city"]}</button>' for k,d in enumerate(FEAT))}</div>
<div class="fcity"><b>{f0['city']}</b><span>{f0['tag']}</span></div></div>
<div class="fb"><div class="same">Same points, either way</div>
<div class="ptsbig tnum"><span id="fpts" data-cu="{f0['pts']}">{f0['pts']:,}</span><i>pts</i></div>
<div class="fork">
<div class="way"><div class="wl"><span class="wn">The usual way</span><span class="wv tnum">≈ $<span id="fu" data-cu="{f0['usual']}">{f0['usual']:,}</span></span></div><div class="ws" id="fus">{f0['us']}</div><div class="mt"><i id="fub" style="--w:{f0['usual']/f0['desk']*100:.1f}%"></i></div></div>
<div class="way d"><div class="wl"><span class="wn">With your desk</span><span class="wv tnum">≈ $<span id="fk" data-cu="{f0['desk']}" data-ms="2200">{f0['desk']:,}</span></span></div><div class="ws" id="fks">{f0['ks']}</div><div class="mt"><i style="--w:100%"></i></div></div>
</div>
<div class="mult"><b class="tnum"><span id="fm" data-cu="{f0['x']}" data-d="1" data-ms="2400">{f0['x']}</span>x</b><span class="ml">more trip<br>for the same points</span></div>
<div class="ft fn" style="display:flex;justify-content:space-between;align-items:center"><span class="estl">Estimated, illustrative</span><small class="fine" id="ftx">{f0['tx']}</small></div>
</div></div>
<p class="method"><b>Method.</b> The usual way: the points cashed as a statement credit at 1.0¢ each. With your desk: the estimated cash price of the trip the same points buy through a partner program, divided by the points (3.4 to 6.2¢ a point in these examples). Estimated, illustrative; taxes and fees extra. Award pricing and award space change constantly. We control neither.</p>
</div></section>'''

deck_cards=''.join(story_card(d, more=k>=5) for k,d in enumerate(DEST))
deck=f'''<section class="sx ps" id="deck">{ph(['bg-01','d-maldives','bg-07','d-cabo'],'lite')}{rail('04','What it turns into')}<div class="w2">
<div class="deckhd"><div>{kk('What it turns into')}<h2 class="h2x" data-rv>Same points. <em>A very different trip.</em></h2>
<p class="lede" data-rv>15 trips in the style the desk finds. Each card starts from the same balance: what it buys the usual way, and what it buys with your desk.</p></div>
<div class="dnav"><button type="button" data-dir="-1" aria-label="Previous trips">←</button><span class="cnt" id="dcnt">01 / 15</span><button type="button" data-dir="1" aria-label="Next trips">→</button></div></div>
<div class="track" id="track">{deck_cards}</div>
<div class="prog"><i id="dprog"></i></div>
<button class="pill outline more" id="dmore" type="button">Show all 15 trips</button>
<p class="method"><b>Estimated, illustrative.</b> Usual way at 1.0¢ a point as a statement credit. Desk value is the estimated cash price of the trip ÷ the points, 3.4 to 6.2¢ in these examples. Taxes extra, shown per card. Award space and pricing change.</p>
</div></section>'''

LED=[('EC','E-commerce owner','$62K/MO SPEND','','Example +30% transfer bonus: September buying trip vetted and sent to the desk to book.',6940),
('HV','HVAC contractor','$41K/MO SPEND','','Routed the Q3 insurance premium to clear the 200K business card bonus with 11 days to spare.',4000),
('RE','Real estate broker','$38K/MO SPEND','','Mapped 12 nights of corporate hotel stays to points, at an est. 2.1 cents per point.',2300),
('TR','Trucking operator','$84K/MO SPEND','','Fleet fuel rerouted after fuel-card coding verification: diesel now earns at 2.1x blended.',1760),
('AG','Agency founder','$55K/MO SPEND','','Meta and Google spend moved to 3x. First full month at the new blended rate.',1240),
('IT','IT / MSP owner','$52K/MO SPEND','','AWS and the SaaS stack routed to the 3x card, category cap tracked to the dollar.',1130),
('LW','Law firm partner','$47K/MO SPEND','','Westlaw and expert fees restacked, plus a retention offer landed in month 13, not 12.',980),
('RG','Restaurant group','$58K/MO SPEND · AMBER','am','Sysco stays capped at 1x, everything around it rerouted. The amber gate, working as designed.',890),
('DN','Dental practice','$36K/MO SPEND · AMBER','am','Henry Schein flagged as wholesale; the non-wholesale mix carried the math anyway.',610),
('LS','Landscaper','$18K/MO SPEND','','Honest no. Under the bar, told so on The Found Money Call, for free. Reads The Daily Redemption now.',0)]
cols=['#FA1896','#ff4fb0','#ff7cc2','#f99fd0','#7348F0','#2E9BE8','#16A06A','#e2a33a','#f0c26a']
rows=''
for k,(ini,nm,sp,am,ds,v) in enumerate(LED):
    vv=f'<div class="vv"><div class="vb"><i class="{am}" style="--w:{v/6940*100:.1f}%;transition-delay:{.3+k*.08:.2f}s"></i></div><span class="vn tnum">${v:,}</span></div>' if v else '<div class="vv"><div class="vb"></div><span class="vn">HONEST NO · $0</span></div>'
    rows+=f'<div class="lr{" no" if not v else ""}" style="transition-delay:{k*.07:.2f}s"><div class="ini">{ini}</div><div class="nm"><b>{nm}</b><small class="{am}">{sp}</small></div><div class="ds">{ds}</div>{vv}</div>'
stack=''.join(f'<i style="--w:{v/19850*100:.2f}%;background:{cols[k]};transition-delay:{.4+k*.1:.1f}s" title="{nm}"></i>' for k,(ini,nm,sp,am,ds,v) in enumerate(LED) if v)
receipts=f'''<section class="sx ps" id="receipts">{ph(['d-connemara','bg-03','d-iceland'],'')}{rail('05','A month at the desk')}<div class="w2">
{kk('What a month at the desk looks like')}
<h2 class="h2x" data-rv>A modelled month, <em>built from the routing we actually run.</em></h2>
<p class="lede" data-rv>Every engagement, every capture, and the ones we would turn away. This is how the ledger reads, not a highlight reel.</p>
<div class="gl solid ledger" data-io><div class="lg-h"><span class="d">July 2026 ledger</span><span>Illustrative month · resets on the 1st</span></div>
{rows}
<div style="padding:20px 0 0"><div class="stack">{stack}</div></div>
<div class="lg-f"><span class="c">10 engagements · July 2026</span><span class="t tnum">$<span data-cu="19850" data-ms="2400">19,850</span><small>captured</small></span></div></div>
<p class="method">Illustrative ledger showing how a month reads. Not client results. Actual results vary by portfolio.</p>
</div></section>'''

MAX=21924
def wf(rows_, start, tot, label):
    out=''; rem=start
    out+=f'<div class="r"><span>{rows_[0][0]}</span><b>{rows_[0][1]}</b><div class="bx"><i style="--l:0%;--w:{start/MAX*100:.1f}%"></i></div></div>'
    for k,(t,v,n) in enumerate(rows_[1:]):
        if n:
            rem2=rem-n
            out+=f'<div class="r"><span>{t}</span><b class="neg">{v}</b><div class="bx"><i class="rem" style="--l:0%;--w:{rem2/MAX*100:.1f}%;transition-delay:{.3+k*.25:.2f}s"></i><i class="neg" style="--l:{rem2/MAX*100:.1f}%;--w:{n/MAX*100:.1f}%;transition-delay:{.5+k*.25:.2f}s"></i></div></div>'
            rem=rem2
        else:
            out+=f'<div class="r"><span>{t}</span><b>{v}</b></div>'
    return out+f'<div class="tot"><span>{label}</span><b class="tnum">$<span data-cu="{tot}" data-ms="2200">{tot:,}</span></b></div>'
bill=wf([('2% on $420,000 of spend','$8,400',0),('Everything, except the capped categories','−$1,900',1900),('Everything, except foreign transaction fees','−$310',310),('Everything, except the annual fee, taken first','−$95',95),('Everything, except the vendors that code wrong','−$640',640),('Redeemed as a statement credit, at face value','Included',0)],8400,5455,'What actually lands')
ours=wf([('1,218,000 points on $420,000, blended 2.9x after routing','$21,924',0),('Everything, except the capped categories','−$1,180',1180),('Everything, except foreign transaction fees','−$310',310),('Everything, except the annual fees, taken first','−$1,290',1290),('Everything, except the vendors that code wrong','−$460',460),('Redeemed as real flights and hotel nights, not cashed at the bottom','Included',0)],21924,18684,'Return on the same spend')
cashback=f'''<section class="sx ps" id="cashback">{ph(['bg-06','d-santorini','e-relax','bg-03'],'c c2')}{rail('06','The 2 percent promise')}<div class="w2">
<div style="text-align:center">{kk('The 2 percent promise')}</div>
<h2 class="h2x c" data-rv>2% back sounds like a win. <em>Then you read the tax code.</em></h2>
<p class="lede c" data-rv>Cash back is the easiest thing to advertise and the hardest thing to verify. Here is the same $420,000 of business spending, run both ways, with the same frictions subtracted from both columns and the tax question left to the panel below.</p>
<div class="cbw"><div class="cb" data-io>
<div class="gl solid cbc"><div class="hd">What the billboard says</div><h3>“2% back on everything”</h3><div class="wf">{bill}</div></div>
<div class="gl solid cbc us"><div class="hd">The same $420,000</div><h3>Routed on the Earn, booked on the Burn</h3><div class="wf">{ours}</div></div>
</div><div class="vs">VS</div></div>
<div style="text-align:center;margin-top:72px" data-rv><h3 class="h2x c" style="font-size:clamp(32px,3.4vw,46px)">Cash back is not income. <em>That is not a compliment.</em></h3></div>
<div class="tax">
<div class="gl taxc" data-rv><div class="hd"><span class="ic">💵</span><h4><small>Cash back</small>Treated as a rebate</h4></div><ul><li>Not income, which sounds generous</li><li>A rebate is a discount on money you already spent</li><li>So the business expense you deduct shrinks by the same amount</li></ul></div>
<div class="gl taxc pt" data-rv="2"><div class="hd"><span class="ic">✈️</span><h4><small>Points</small>Treated differently</h4></div><ul><li>In Announcement 2002-18 the IRS said it will not assert that a taxpayer understated tax by reason of receiving or personally using miles attributable to business travel</li><li>The same announcement excludes miles converted to cash and miles paid as compensation, and it has not been revisited since</li><li>Spend points on business travel and you give up that deduction, so it is not free either</li></ul></div>
</div>
<div class="closer" data-rv><h2 class="h2x c" style="font-size:clamp(30px,3.2vw,44px)">One arrives with a tax drag. <em>The other arrives as a trip.</em></h2>
<p class="lede c">We are not your accountant and we will not pretend to be one. Ask yours which of the two they would rather see on your return. It is a 2 minute question with a 4 figure answer.</p></div>
<p class="method">Modelled on a $35,000 a month profile. Points column assumes a blended 2.9x earn redeemed at 1.8 cents. Both columns subtract the same four frictions. Neither column prices tax treatment. Caps, fees, coding and tax treatment vary by business. General information, not tax advice.</p>
</div></section>'''

PIL=[('Earn','--earn','#12834E','Pillar 01','You already do this','Every dollar your business spends on cards and vendors quietly earns points. The only question is whether it lands on the card that pays 4 times instead of one.','Your fuel and insurance move to the right card. Nothing about your week changes.'),
('Burn','--burn','#E8590C','Pillar 02','Spending points is the skill','Burn is the industry word for spending points, and it is where all the value lives or dies. The same 120,000 points are a $600 gift card or business class for 2 to Lisbon, est.','Same points, 2 outcomes: $600 or $7,400. That gap is the entire job.'),
('Return','--ret','#7149C9','Pillar 03','In dollars, every Friday','Not points, not vibes. A written report every Friday with the dollar value of what we captured that week. If it stops beating the fee, you cancel.','$550 a month, flat. Cancel anytime.'),
('Learn','--learn','#1E78B8','Pillar 04','You get sharper, for free','Every recommendation arrives with its math in plain language. No course to buy, no jargon to memorize. Keep the desk or leave it, what you learn stays yours.','Every message answers why, not just what.')]
pos=[(240,70),(410,240),(240,410),(70,240)]
nodes=''.join(f'<g class="node" data-c="{c}" role="button" aria-label="{n}"><circle cx="{x}" cy="{y}" r="44" fill="#fff" stroke="{c}" stroke-width="3"/><text x="{x}" y="{y+7}" text-anchor="middle" fill="{c}">{n}.</text></g>' for (n,v,c,*_),(x,y) in zip(PIL,pos))
cards=''.join(f'<article class="gl solid pc2{" on" if k==0 else ""}" style="--c:{c}"><div class="pn">{pn}</div><h3>{n}.</h3><div class="sub">{sub}</div><p>{p}</p><div class="pull">{pull}</div></article>' for k,(n,v,c,pn,sub,p,pull) in enumerate(PIL))
tabs=''.join(f'<button type="button" style="--c:{c}">{n}</button>' for (n,v,c,*_) in PIL)
pillars=f'''<section class="sx ps" id="pillars">{ph(['d-iceland','bg-02','d-alps'],'')}{rail('07','The 4 pillars')}<div class="w2">
{kk('The 4 pillars')}
<h2 class="h2x" data-rv>Earn, Burn, Return, Learn. <em>That is the whole system.</em></h2>
<p class="lede" data-rv>4 words, in this order, until the money comes back to you. We will teach you the one piece of jargon that matters and skip the rest.</p>
<div class="orb" id="orb"><svg viewBox="0 0 480 480" role="img" aria-label="Earn, Burn, Return, Learn: a loop around your desk">
<circle cx="240" cy="240" r="170" fill="none" stroke="#e6dfd2" stroke-width="2" stroke-dasharray="3 7"/>
<circle id="oarc" cx="240" cy="240" r="170" fill="none" stroke="#12834E" stroke-width="5" stroke-linecap="round" stroke-dasharray="0 1068" transform="rotate(-90 240 240)" style="transition:stroke-dasharray .9s cubic-bezier(.2,.8,.2,1),stroke .6s"/>
<circle cx="240" cy="240" r="96" fill="#fff" stroke="#fde7f3" stroke-width="10"/>
<image href="img/fo-chevron-alpha.png" x="206" y="190" width="68" height="68"/>
<text x="240" y="284" text-anchor="middle" style="font:700 10px 'JetBrains Mono',monospace;letter-spacing:2px" fill="#141216">YOUR DESK</text>
{nodes}</svg>
<div><div class="pcards">{cards}</div><div class="ptabs">{tabs}</div></div></div>
</div></section>'''

friday=f'''<section class="sx ps" id="friday">{ph(['e-relax','bg-04','e-coffee'],'r')}{rail('08','The return, in writing')}<div class="w2">
<div class="fri"><div>
{kk('The return, in writing')}
<h2 class="h2x" data-rv>Every Friday, <em>a number you can bank.</em></h2>
<p class="lede" data-rv>This is what lands in your thread at the end of the week. No dashboard to check, no report to download.</p>
<div class="gl person nug2" data-rv="2"><div class="ni">👤</div><div><b>Reviewed by a person</b><p>{APPROVED}</p></div></div>
</div>
<div class="slot" data-io><div class="rcpt"><div class="rh"><span>Friday · Week 33</span><span>First Officer</span></div>
<h4>Capture Report</h4>
<div class="li"><span>Vendor routing corrected (3 vendors)</span><b>$310</b></div>
<div class="li"><span>Transfer bonus caught, 30 percent</span><b>$980</b></div>
<div class="li"><span>Hotel nights booked on points</span><b>$1,450</b></div>
<div class="li"><span>Statement credits claimed</span><b>$220</b></div>
<div class="li"><span>Expiring balance rescued</span><b>$940</b></div>
<div class="tt"><span>Captured this week</span><b class="tnum">$<span data-cu="3900" data-ms="2600">3,900</span></b></div>
<div class="bc"></div><div class="ill">Illustrative week. Your report shows your own captures.</div></div></div>
</div></div></section>'''

dots=''.join('<i style="animation-delay:%.2fs"></i>'%((k*37%96)/24) for k in range(96))
explore=f'''<section class="sx ps" id="explore">{ph(['d-santorini','bg-05','d-paris'],'c')}{rail('09','If you want to check us')}<div class="w2">
<div style="text-align:center">{kk('If you want to check us')}</div>
<h2 class="h2x c" data-rv>Everything else is <em>optional reading.</em></h2>
<div class="ex">
<a class="gl exc" href="calculator.html" data-rv><div class="viz"><svg width="110" height="70" viewBox="0 0 110 70"><path d="M10 62a45 45 0 0 1 90 0" fill="none" stroke="#efe8dc" stroke-width="12" stroke-linecap="round"/><path d="M10 62a45 45 0 0 1 72-36" fill="none" stroke="#FA1896" stroke-width="12" stroke-linecap="round"/><text x="55" y="60" text-anchor="middle" style="font:400 18px 'DM Serif Display'" fill="#141216">$19,492</text></svg></div><div class="k">Calculator</div><h3>What is my number?</h3><p>Your industry, your categories, your range, with the math shown.</p><span class="go2">Run it →</span></a>
<a class="gl exc" href="product.html" data-rv="2"><div class="viz"><div class="dots96">{dots}</div></div><div class="k">Product</div><h3>Inside the machine</h3><p>Coverage across 96 programs, what is shipped, and what we have not built yet.</p><span class="go2">Look inside →</span></a>
<a class="gl exc" href="trust.html" data-rv="3"><div class="viz"><div class="lk">READ-ONLY</div></div><div class="k">Trust</div><h3>What do you see?</h3><p>Read-only, revocable, nothing sold, and how you switch it off.</p><span class="go2">Read the terms →</span></a>
<a class="gl exc" href="field-notes.html" data-rv="4"><div class="viz"><div class="notes8"><i style="left:0;top:18px;transform:rotate(-8deg)"></i><i style="left:22px;top:10px;transform:rotate(-2deg)"></i><i style="left:44px;top:4px;transform:rotate(6deg);display:grid;place-items:center;font:400 30px 'DM Serif Display';color:#FA1896">8</i></div></div><div class="k">Field Notes</div><h3>Why does this exist?</h3><p>8 notes on how the rewards game actually works.</p><span class="go2">Start reading →</span></a>
</div>
<div class="longr" data-rv><p>Prefer the whole argument in one sitting? <a href="hello.html">Read the long version</a>, every section, in order.</p>
<p class="fine c">Your points stay in your accounts, in your name, and nothing moves without you. Award trips are a separate $500 flat: we vet the requirements, then the desk books once you approve.</p>
<p class="fine c">Point valuations are estimates based on common redemption benchmarks. Actual value depends on how and when you redeem.</p></div>
</div></section>'''

body=hero+stat+yn+portal+fomo+deck+receipts+cashback+pillars+friday+explore
tail='<script>window.FO_CHAT='+json.dumps(CHAT)+';window.FO_FEAT='+json.dumps(FEAT)+';</script>'
html=page('First Officer · You are not bad at Points & Miles', body, desc='A desk of specialists across 96 programs, working for your business spend.', hero=True, src='home', tail=tail)
open('/workspace/fo-rebuild-v2/home.html','w').write(html)
print(len(html))
