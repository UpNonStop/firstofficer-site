import json, sys
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from fosite import *
CHAT=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'chat.json')))
DEST=[('Lisbon','d-lisbon','Flights',120000,1200,7400,'6.2','Business class for 2','+$118'),
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
 ('Los Cabos','d-cabo','Combined',118000,1180,5700,'4.8','Flights and 5 nights','+$92')]
FEAT=[dict(city=d[0],img='img/ph/'+d[1]+'.webp',tag=d[2],pts=d[3],usual=d[4],cash=round(d[3]/2.1*0.02),desk=d[5],x=float(d[6]),us='Statement credit, at 1¢ a point',ks=d[7]+', est.',tx='est. taxes '+d[8]) for d in [DEST[4],DEST[0],DEST[2],DEST[1],DEST[8]]]

def story(city,img,tag,pts,us,dk,x,trip,tx, more=False, ids=False):
    I=(lambda n: f' id="{n}"') if ids else (lambda n:'')
    return f'''<article class="ptile{' more' if more else ''}{' sig' if ids else ''}" aria-label="{city}: {pts:,} points, about ${round(pts/2.1*0.02):,} at 2% cash back, about ${us:,} as points with no strategy, or about ${dk:,} with the Bespoke strategy, estimated">
<div class="im{' ba' if ids else ''}">{(f'<img id="fimg0" class="ba0" src="img/ph/{img}.webp" alt="" aria-hidden="true" decoding="async">') if ids else ''}<img{I('fimg')} src="img/ph/{img}.webp" alt="{city}" loading="lazy" decoding="async">{(f'<span class="bal l">What most people book<b>≈ $<span id="fbu">{us:,}</span> statement credit</b></span><span class="bal r">What the desk books<b id="fbk">{trip}, est.</b></span><span class="bapt"><b id="fbp">{pts:,}</b> pts · fixed</span><i class="bah" aria-hidden="true"></i><input class="bar-r" type="range" min="4" max="96" value="50" aria-label="Drag to compare what most people book with what the desk books, same points">') if ids else ''}</div>
<div class="cp"><b{I('fcity')}>{city}</b><span{I('ftrip')}>{tag} · {trip}</span></div>
<div class="bd"><span class="lab burn">Same points{', every way' if ids else ''}</span><span class="num m tn" style="margin:4px 0 14px"><span{I('fpts')} data-cu="{pts}">{pts:,}</span><small>pts</small></span>
<div class="cmp alt3">{bar('Cash back',f'≈ $<span{I("fc")} data-cu="{round(pts/2.1*0.02)}">{round(pts/2.1*0.02):,}</span>',round(pts/2.1*0.02)/dk*100,sub='At 2% cash back on the same spend',cls='usual cbk',dl=0)}{bar('Points, no strategy',f'≈ $<span{I("fu")} data-cu="{us}">{us:,}</span>',us/dk*100,sub='Statement credit, at 1¢ a point',cls='usual nos',dl=.12)}{bar('Bespoke strategy',f'≈ $<span{I("fk")} data-cu="{dk}">{dk:,}</span>',100,'var(--burn)',sub=f'<span{I("fks")}>{trip}, est.</span>',dl=.25)}</div>
<div class="mult"><b><span{I('fm')} data-cu="{x}" data-d="1">{x}</span>x</b><span>{'more trip<br>for the same points' if ids else 'more trip'}</span></div>
<div class="cap" style="margin-top:10px">Estimated, illustrative · <span{I('ftx')}>est. taxes {tx}</span></div></div></article>'''

HERO_PH=['bg-0%d'%k for k in range(1,9)]+['d-'+n for n in ['lisbon','santorini','maldives','kyoto','bali','paris','cabo','iceland','costarica','alps','rome','barcelona','dubai','nyc','connemara']]
hero=f'<section id="top"><div class="phx" data-iv="6000" data-ph="{",".join("img/ph/"+n+".webp" for n in HERO_PH)}" aria-hidden="true"></div><div id="fohero"></div></section>'

stat=f'''<section class="sec" id="terms" style="padding-top:28px;padding-bottom:28px"><div class="wrap"><div class="card hero" data-rv><div class="pair">
<div><div class="k">Flat monthly · Cancel anytime</div><div class="v">$550</div></div>
<div><div class="k">The Found Money Call, free · We size your capture first</div><div class="v"><span data-cu="20">20</span> min</div></div>
<div><div class="k">Dollars saved reported every Friday</div><div class="v">Friday</div></div>
<div><div class="k">Every decision, always</div><div class="v">Yours</div></div></div></div></div></section>'''

PORD=[('Earn','earn'),('Burn','burn'),('Return','return'),('Learn','learn')]
def prail(cls=''): return f'<span class="prail {cls}" role="list" aria-label="The 4 pillars, in order: Earn, Burn, Return, Learn">'+'<i aria-hidden="true"></i>'.join(f'<span role="listitem" style="--c:var(--{c});--ci:var(--{c}-i)">{n}</span>' for n,c in PORD)+'</span>'
yn=f'''<section class="sec" id="number">{ph(['bg-04','d-costarica','bg-08','d-bali'])}<div class="wrap">
{head(prail('mini'),'Your monthly spend on cards and vendors. <em>What that should be buying you every year.</em>')}
<div class="split wide"><div>
<div class="card hero top" style="--c:var(--earn)" id="dial" data-rv>
<span class="lab earn">Your monthly spend on cards and vendors</span>
<span class="num tn" id="spv" style="margin-top:8px">$35,000</span>
<input class="rng" type="range" min="10000" max="150000" step="500" value="35000" aria-label="Monthly spend on cards and vendors" style="margin-top:10px">
<div class="mcap"><span>$10K</span><span>$75K</span><span>$150K</span></div>
<div class="div"></div>
<span class="lab">Every year · sticker value, est.</span>
<span class="num tn" id="yv" style="margin-top:6px">$19,492</span>
<div class="rows" style="margin-top:14px">
{row('In flights','',f'<span id="fv">$11,695</span>','var(--burn)',meter(60,'var(--burn)'),cls='')}
{row('In hotel stays','',f'<span id="hv">$5,848</span>','var(--s-hotel)',meter(30,'var(--s-hotel)'))}
{row('In everything else','',f'<span id="ov">$1,949</span>','var(--earn)',meter(10,'var(--earn)'))}
</div>
<div class="btns"><a class="btn" href="book.html?from=home-dial">Book Your "Found Money" Call</a><a class="btn ghost" href="calculator.html">See the full breakdown</a></div>
<p class="cap" style="margin-top:14px">The Found Money Call: 20 minutes, free, no card required. Modelled at a blended 2.1x earn, 85% of points actually used, and 2.6 cents of value per point. Sticker value of the travel, before our fee. Your category mix and your redemptions will differ. The full calculator shows the number net of our fee.</p>
</div>
<div class="note" style="margin-top:12px" data-rv><span class="ic">🪙</span><span><b>Our promise:</b> if the call shows our work won't clear the fee, we tell you in writing and you never pay.</span></div>
<div class="card" style="margin-top:12px" data-rv><div style="display:flex;gap:12px;align-items:center"><span class="row ini" style="padding:0;border:0;box-shadow:none;background:none"><span class="av" style="width:44px;height:44px" aria-label="OS portrait coming">OS</span></span><div><b style="display:block;font-size:15px">Ohad Sternberg</b><span class="cap">Founder · draft line</span></div></div>
<p style="margin-top:12px;font-size:16px;line-height:1.5;color:var(--ink)">“I built this so the money your business already spends finally works for you. If it won't, I'll tell you.”</p>
<p style="margin-top:8px">Before First Officer, Ohad built fraud and authentication products for financial institutions (<a href="about.html" style="color:var(--pink2)">public profile</a>). The same rule applies here: read-only access, no passwords, nothing moves without your written yes.</p></div>
</div>
<div class="sticky" data-rv><span class="lab zone" style="margin-top:0">This is the entire product</span>
<div class="chat"><div class="ch"><span class="mk"><img src="img/fo-chevron-transparent-v2.png" alt=""></span><div><b>First Officer</b><small>Online</small></div><span class="badge">2 at work</span></div>
<div class="th wac" aria-live="polite"></div><div class="cf"><div class="in">Ask your First Officer<i>↑</i></div></div></div>
<p class="cap" style="margin-top:10px">One thread, no app to install. Simulated conversation. Actual results vary by portfolio.</p></div>
</div></div></section>'''

portal=f'''<section class="sec" id="portal">{ph(['d-lisbon','bg-02','d-rome','bg-06'])}<div class="wrap">
{head('How the game is built','The house wins twice. <em>Nobody tells you when.</em>','This is not a conspiracy. It is a business model, published in the annual reports, and it runs on you being busy.')}
<div class="split"><div class="sticky"><div class="card hero top" style="--c:var(--burn)" data-rv>
<span class="lab burn">The spread, in cents per mile</span>
<div class="cmp" style="margin-top:16px">{bar('Banks pay the program','1.25–2¢',80,'var(--ink2)')}{bar('Typical redemption','1.1–1.5¢',60,cls='usual',dl=.2)}{bar('Chapter 04: above the spread','2¢ +',100,'var(--earn)',dl=.4)}</div>
<p class="cap" style="margin-top:14px">Banks buy miles at 1.25 to 2 cents; typical redemption value runs 1.1 to 1.5. The gap is the business model. Chapter 04 is the way out.</p></div></div>
<div class="stack">
<article class="card" data-rv><span class="lab">Chapter 01</span><h3 class="h3" style="margin-top:6px">Miles are a product. You are not the customer.</h3>
<div class="note" style="margin:14px 0;display:block"><span class="num m tn">$<span data-cu="7.4" data-d="1">7.4</span>B</span><span class="sub" style="display:block;margin-top:4px">collected by one airline from its card partner in 2024, larger than its entire operating profit that year.</span></div>
<p>Airlines do not give miles away, they sell them in bulk to banks. Delta collected roughly $7.4 billion from its card partner in 2024, larger than the airline's entire operating profit that year. American and United run the same play. When the planes were grounded they mortgaged the loyalty programs alongside everything else: $9 billion raised against SkyMiles and $6.8 billion against MileagePlus in 2020, then $10 billion against AAdvantage in March 2021.</p>
<div class="src">Delta figure from its 2024 Form 10-K. Loyalty financings from the 2020 and 2021 offering documents.</div></article>
<article class="card" data-rv><span class="lab">Chapter 02</span><h3 class="h3" style="margin-top:6px">They win on the spread.</h3>
<div class="rows" style="margin:14px 0">{row('Loyalty program A, 2019','EBITDA margin','49%','var(--burn)',meter(49,'var(--burn)'))}{row('Loyalty program B, 2019','EBITDA margin','34%','var(--burn)',meter(34,'var(--burn)',.15))}{row('The airlines, 2024','Operating margin','4.8–9.7%','var(--ink3)',meter(9.7,'var(--ink3)',.3))}</div>
<p>Programs sell miles to the banks for somewhere between 1.25 and 2 cents each, and independent valuations put typical redemption value at 1.1 to 1.5. Neither number appears in any filing, because co-brand pricing is confidential, but the direction of the gap is the business model and it repeats across every mile issued. In the 2019 figures the airlines showed bond investors, AAdvantage ran a 49 percent EBITDA margin and MileagePlus 34. The airlines themselves earned operating margins of 4.8 to 9.7 percent in 2024.</p>
<div class="src">Margins from the 2019 AAdvantage and MileagePlus investor presentations.</div></article>
<article class="card" data-rv><span class="lab">Chapter 03</span><h3 class="h3" style="margin-top:6px">They win again when you forget.</h3>
<div class="note" style="margin:14px 0;display:block"><span class="num m tn"><span data-cu="30">30</span> trillion</span><span class="sub" style="display:block;margin-top:4px">miles estimated sitting unredeemed in 2018. Breakage runs a quarter to a third of everything issued.</span>
<div style="margin-top:12px">{meter(25,'var(--burn)')}<div class="mcap"><span>About a quarter of points issued are never used</span><span>¼</span></div></div></div>
<p>Points earned and never used have a name on the balance sheet: breakage. An industry study estimated in 2018 that more than 30 trillion frequent flyer miles were sitting unredeemed, and it is still the most-cited figure in the industry. Breakage typically runs a quarter to a third of everything issued, around 25 percent in retail programs and 15 to 30 in airline ones, and every one of those forgotten points is margin nobody has to deliver. Your balance is in that number.</p>
<div class="src">Breakage and unredeemed miles from a 2018 industry study. See the Ghost Economy on The Daily Redemption for the full working.</div></article>
<article class="card top" style="--c:var(--earn)" data-rv><span class="lab earn">Chapter 04</span><h3 class="h3" style="margin-top:6px">One move beats the house.</h3>
<p style="margin-top:6px">Redeem above the spread. Move the points into the airline or hotel program itself, at the right moment, against the right chart, on the right dates, and the value lands on your side of the table instead of theirs. That takes somebody watching all day, every day. That is the entire job you are hiring.</p></article>
</div></div>
<h2 class="h2 center" style="margin-top:34px;max-width:760px;text-align:center" data-rv>2 departments are working on your points. <em>Until now, neither one worked for you.</em></h2>
</div></section>'''

f0=FEAT[0]
fomo=f'''<section class="sec" id="fomo">{ph(['d-santorini','d-kyoto','d-maldives'])}<div class="wrap">
{head('The difference is the search','Same points. <em>Three very different outcomes.</em>','We do not set the prices and we do not control award space. We know where to look, and that is the whole gap.')}
<div style="max-width:560px" id="feat" data-rv>
<div class="chiprow ftabs" style="margin-bottom:12px">{''.join(f'<button type="button" class="chip{" on" if k==0 else ""}">{d["city"]}</button>' for k,d in enumerate(FEAT))}</div>
{story(*DEST[4], ids=True)}</div>
<div class="icta" style="max-width:560px" data-rv><div><b class="lead">See this on your own numbers.</b><p class="cap">The Found Money Call: 20 minutes, free.</p></div><a class="btn ghost" href="book.html?from=home-sig">Book Your "Found Money" Call →</a></div>
<p class="method"><b>Method.</b> Three ways, lowest to highest. Cash back: the spend that earns these points at the 2.1x blended rate used on this page, at 2% cash back. Points, no strategy: the points cashed as a statement credit at 1.0¢ each. Bespoke strategy (illustrative): the estimated cash price of the trip the same points buy through a partner program, divided by the points (3.4 to 6.2¢ a point in these examples). Estimated, illustrative; taxes and fees extra. Award pricing and award space change constantly. We control neither.</p>
</div></section>'''

deck=f'''<section class="sec" id="deck">{ph(['bg-01','d-maldives','bg-07','d-cabo'])}<div class="wrap">
{head('What it turns into','Same points. <em>A very different trip.</em>','15 trips in the style the desk finds. Each card starts from the same balance: what it buys three ways.')}
<div class="track" id="track">{''.join(story(*d, more=k>=5) for k,d in enumerate(DEST))}</div>
<div class="trackbar"><button class="arrow" type="button" data-dir="-1" aria-label="Previous trips">←</button><div class="meter in"><i id="dprog" style="--w:7%;transform:none"></i></div><span class="cnt" id="dcnt">01 / 15</span><button class="arrow" type="button" data-dir="1" aria-label="Next trips">→</button></div>
<button class="btn ghost" id="dmore" type="button" style="margin-top:14px">Show all 15 trips</button>
<p class="method"><b>Estimated, illustrative.</b> Lowest to highest: Cash back at 2% cash back on the spend that earns the points at a 2.1x blended rate. Points, no strategy at 1.0¢ a point as a statement credit. Bespoke strategy is illustrative: its value is the estimated cash price of the trip ÷ the points, 3.4 to 6.2¢ in these examples. Taxes extra, shown per card. Award space and pricing change.</p>
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
def lrow(ini,nm,sp,am,ds,v):
    pill='<span style="display:block;margin-top:8px"><span class="pill" style="--c:var(--ink3)">HONEST NO · $0</span></span>' if not v else ''
    return f'<div class="row ini"><span class="av">{ini}</span><span class="bd"><span class="t">{nm}</span><span class="lab{' burn' if am else ''}" style="display:block;margin:2px 0 4px;font-size:10px">{sp}</span><span class="s">{ds}</span>{pill}</span><span class="v">{"$"+format(v,",") if v else "$0"}</span></div>'
receipts=f'''<section class="sec" id="receipts">{ph(['d-connemara','bg-03','d-iceland'])}<div class="wrap">
{head('What a month at the desk looks like','A modelled month, <em>built from the routing we actually run.</em>','Every engagement, every capture, and the ones we would turn away. This is how the ledger reads, not a highlight reel.')}
<div class="split"><div class="sticky"><div class="card hero top" style="--c:var(--earn)" data-rv><span class="lab earn">July 2026 ledger</span>
<span class="num tn" style="margin-top:8px">$<span data-cu="19850">19,850</span><small>captured</small></span><p class="sub">10 engagements · July 2026. Illustrative month · resets on the 1st.</p>
<div style="margin-top:16px">{meter(90,'var(--green)')}<div class="mcap"><span>9 captured</span><span>1 honest no</span></div></div></div></div>
<div class="rows" data-rv>{''.join(lrow(*l) for l in LED)}</div></div>
<p class="method">Illustrative ledger showing how a month reads. Not client results. Actual results vary by portfolio.</p>
</div></section>'''

BILL=[('2% on $420,000 of spend','$8,400',''),('Everything, except the capped categories','−$1,900','neg'),('Everything, except foreign transaction fees','−$310','neg'),('Everything, except the annual fee, taken first','−$95','neg'),('Everything, except the vendors that code wrong','−$640','neg'),('Redeemed as a statement credit, at face value','Included','')]
OURS=[('1,218,000 points on $420,000, blended 2.9x after routing','$21,924',''),('Everything, except the capped categories','−$1,180','neg'),('Everything, except foreign transaction fees','−$310','neg'),('Everything, except the annual fees, taken first','−$1,290','neg'),('Everything, except the vendors that code wrong','−$460','neg'),('Redeemed as real flights and hotel nights, not cashed at the bottom','Included','')]
cashback=f'''<section class="sec" id="cashback">{ph(['bg-06','d-santorini','e-relax','bg-03'])}<div class="wrap">
{head('The 2 percent promise','2% back sounds like a win. <em>Then you read the tax code.</em>','Cash back is the easiest thing to advertise and the hardest thing to verify. Here is the same $420,000 of business spending, run both ways, with the same frictions subtracted from both columns and the tax question left to the panel below.')}
<div class="card hero" style="margin-bottom:12px" data-rv><span class="lab">The same $420,000, three ways</span>
<div class="cmp alt3" style="margin-top:14px">{bar('No strategy','$0',0,sub='A debit card, earns nothing',cls='usual')}{bar('Cash back','$5,455',5455/18684*100,sub='“2% back on everything”: what actually lands',cls='usual',dl=.12)}{bar('Bespoke strategy','$18,684',100,'var(--earn)',sub='Routed on the earn, booked on the burn',dl=.25)}</div>
<p class="cap" style="margin-top:12px">Bespoke strategy is illustrative, not a projection of your results.</p></div>
<div class="g2">
<div class="card" data-rv><span class="lab">What the billboard says</span><h3 class="h3" style="margin:6px 0 10px">“2% back on everything”</h3>{''.join(kv(a,b,c) for a,b,c in BILL)}{kv('What actually lands','$<span data-cu="5455">5,455</span>','tot')}</div>
<div class="card top" style="--c:var(--earn)" data-rv><span class="lab earn">The same $420,000</span><h3 class="h3" style="margin:6px 0 10px">Routed on the earn, booked on the burn</h3>{''.join(kv(a,b,c) for a,b,c in OURS)}{kv('Return on the same spend','$<span data-cu="18684">18,684</span>','tot')}</div>
</div>
<h3 class="h2" style="margin:34px 0 16px;font-size:24px" data-rv>Cash back is not income. <em>That is not a compliment.</em></h3>
<div class="g2">
<div class="card" data-rv><span class="lab">💵 Cash back</span><h3 class="h3" style="margin:6px 0 10px">Treated as a rebate</h3><div class="rows">{row('Not income, which sounds generous',c='var(--ink3)')}{row('A rebate is a discount on money you already spent',c='var(--ink3)')}{row('So the business expense you deduct shrinks by the same amount',c='var(--ink3)')}</div></div>
<div class="card" data-rv><span class="lab learn">✈️ Points</span><h3 class="h3" style="margin:6px 0 10px">Treated differently</h3><div class="rows">{row('In Announcement 2002-18 the IRS said it will not assert that a taxpayer understated tax by reason of receiving or personally using miles attributable to business travel',c='var(--learn)')}{row('The same announcement excludes miles converted to cash and miles paid as compensation, and it has not been revisited since',c='var(--learn)')}{row('Spend points on business travel and you give up that deduction, so it is not free either',c='var(--learn)')}</div></div>
</div>
<div class="head" style="margin:34px 0 0" data-rv><h2 class="h2" style="font-size:24px">One arrives with a tax drag. <em>The other arrives as a trip.</em></h2><p class="lede">We are not your accountant and we will not pretend to be one. Ask yours which of the two they would rather see on your return. It is a 2 minute question with a 4 figure answer.</p></div>
<p class="method">Modelled on a $35,000 a month profile. Points column assumes a blended 2.9x earn redeemed at 1.8 cents. Both columns subtract the same four frictions. Neither column prices tax treatment. Caps, fees, coding and tax treatment vary by business. General information, not tax advice.</p>
</div></section>'''

PIL=[('Earn','earn','Pillar 01','You already do this','Every dollar your business spends on cards and vendors quietly earns points. The only question is whether it lands on the card that pays 4 times instead of one.','Your fuel and insurance move to the right card. Nothing about your week changes.'),
('Burn','burn','Pillar 02','Spending points is the skill','Burn is the industry word for spending points, and it is where all the value lives or dies. The same 120,000 points are a $600 gift card or business class for 2 to Lisbon, est.','Same points, 2 outcomes: $600 or $7,400. That gap is the entire job.'),
('Return','ret','Pillar 03','In dollars, every Friday','Not points, not vibes. A written report every Friday with the dollar value of what we captured that week. If it stops beating the fee, you cancel.','$550 a month, flat. Cancel anytime.'),
('Learn','learn','Pillar 04','You get sharper, for free','Every recommendation arrives with its math in plain language. No course to buy, no jargon to memorize. Keep the desk or leave it, what you learn stays yours.','Every message answers why, not just what.')]
CV={'earn':'var(--earn)','burn':'var(--burn)','learn':'var(--learn)','ret':'var(--return)'}
CI={'earn':'var(--earn-i)','burn':'var(--burn-i)','learn':'var(--learn-i)','ret':'var(--return-i)'}
pillars=f'''<section class="sec" id="pillars">{ph(['d-iceland','bg-02','d-alps'])}<div class="wrap">
{head('The 4 pillars','Earn, burn, return, learn. <em>That is the whole system.</em>',cls='duo',lede='4 words, in this order, until the money comes back to you. We will teach you the one piece of jargon that matters and skip the rest.')}
{prail()}<div class="g4 pilg">{''.join(f'<article class="card hero top pil" style="--c:{CV[c]};--ci:{CI[c]}" data-rv><span class="lab {c}">{pn} · {n}</span><h3 class="h3" style="margin-top:6px;font-size:22px">{n}.</h3><p style="font-weight:600;color:var(--ink);margin-top:2px">{sub}</p><p style="margin-top:8px">{p}</p><div class="tip" style="--c:{CV[c]}"><p style="margin:0;color:var(--ink)">{pull}</p></div></article>' for n,c,pn,sub,p,pull in PIL)}</div>
</div></section>'''

friday=f'''<section class="sec" id="friday">{ph(['e-relax','bg-04','e-coffee'])}<div class="wrap">
<div class="split"><div>{head('The return, in writing','Every Friday, <em>a number you can bank.</em>','This is what lands in your thread at the end of the week. No dashboard to check, no report to download.')}
<div class="tip" style="--c:var(--gold2)" data-rv><div class="tt">👤 Reviewed by a person</div><p>{APPROVED}</p></div></div>
<div class="card hero top" style="--c:var(--gold2)" data-rv><div style="display:flex;justify-content:space-between;align-items:center"><span class="lab ret">Friday · Week 33</span><span class="cap">First Officer</span></div>
<h3 class="h3" style="margin-top:6px">Capture Report</h3>
<span class="num tn" style="margin-top:6px">$<span data-cu="3900">3,900</span></span><p class="sub" style="margin-top:2px">Captured this week</p>
<div class="div"></div>
{kv('Vendor routing corrected (3 vendors)','$310')}{kv('Transfer bonus caught, 30 percent','$980')}{kv('Hotel nights booked on points','$1,450')}{kv('Statement credits claimed','$220')}{kv('Expiring balance rescued','$940')}
<p class="cap" style="margin-top:12px">Illustrative week. Your report shows your own captures.</p></div>
</div></div></section>'''

def xrow(k,t,d,g,c,h): return f'<a class="row" href="{h}" data-rv><span class="dot" style="--c:{c}"></span><span class="bd"><span class="lab" style="color:{c};font-size:10px">{k}</span><span class="t" style="display:block;margin-top:2px">{t}</span><span class="s">{d}</span><span class="s" style="color:var(--pink2);font-weight:600;margin-top:6px">{g}</span></span></a>'
explore=f'''<section class="sec" id="explore">{ph(['d-santorini','bg-05','d-paris'])}<div class="wrap">
{head('If you want to check us','Everything else is <em>optional reading.</em>')}
<div class="g2 rows" style="gap:10px">
{xrow('Calculator','What is my number?','Your industry, your categories, your range, with the math shown.','Run it →','var(--earn)','calculator.html')}
{xrow('Product','Inside the machine','Coverage across 96 programs, what is shipped, and what we have not built yet.','Look inside →','var(--s-analyst)','product.html')}
{xrow('Trust','What do you see?','Read-only, revocable, nothing sold, and how you switch it off.','Read the terms →','var(--learn)','trust.html')}
{xrow('Field Notes','Why does this exist?','8 notes on how the rewards game actually works.','Start reading →','var(--burn)','field-notes.html')}

</div>
<div class="note" style="margin-top:16px" data-rv><span class="ic">📖</span><span>Prefer the whole argument in one sitting? <a href="hello.html" style="color:var(--pink2)">Read the long version</a>, every section, in order.</span></div>
<p class="method">Your points stay in your accounts, in your name, and nothing moves without you. Award trips are a separate $500 flat: we vet the requirements, then the desk books once you approve.</p>
<p class="method" style="margin-top:6px">Point valuations are estimates based on common redemption benchmarks. Actual value depends on how and when you redeem.</p>
</div></section>'''

body=hero+stat+yn+portal+fomo+deck+receipts+cashback+pillars+friday+explore
tail='<script>window.FO_CHAT='+json.dumps(CHAT)+';window.FO_FEAT='+json.dumps(FEAT)+';</script>'
page('home.html','First Officer · You are not bad at Points & Miles', body, desc='A desk of specialists across 96 programs, working for your business spend.', hero=True, src='home', tail=tail)
