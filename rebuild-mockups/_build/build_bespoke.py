import sys,json,re,html as H; sys.path.insert(0,'/workspace/fo-rebuild-mockups/_build')
from common import *
E=H.escape
IJ=json.load(open('/workspace/fo-home-v2/tools/industries.json'))
PH=json.load(open(ROOT+'/_work/data/indphoto.json'))
NM={s:(n,e) for s,n,e in INDS}
def head(k,h,pk,sub='',center=False):
    return f'<div class="head{" center" if center else ""}"><div class="fok">{k}</div><h2 class="foh2">{h} <span class="pk">{pk}</span></h2>{f"<p class=fosub>{sub}</p>" if sub else ""}</div>'
def phero(k,h1a,h1b,sub,ctas='',side='',cls=''):
    sp=' split' if side else ''
    return f'''<section class="phero{sp} {cls}"><img class="chev" src="img/fo-chevron-alpha.png" alt=""><div class="wrap"><div><div class="fok">{k}</div><h1>{h1a} <span class="pk">{h1b}</span></h1><p class="fosub">{sub}</p>{f'<div class="ctas">{ctas}</div>' if ctas else ''}</div>{side}</div></section>'''
BOOK='<a class="pill pink" href="book.html">Book Your “Found Money” Call</a>'
def out(name,title,body,act='',src=None,**kw):
    write(name,page(f'{title} · First Officer',fix(body,name),active=act,src=src or name.replace('.html',''),**kw)); print('wrote',name)

# ---------------- BOOK ----------------
tiles=[('💬','WhatsApp me','Message us, we reply in the thread.','wa',''),('✉️','Email me','Send a note, get a reply by email.','em',''),('📞','Call me back','Leave a number and a good time.','cb',''),('📱','Text me','A plain text from your phone.','tx','soon')]
tl=''.join(f'<button type="button" class="opt{" on" if c=="wa" else ""}{" dis" if s else ""}" data-t="{c}"{" disabled" if s else ""}><span class="oi">{i}</span><b>{t}</b><span>{d}</span>{"<span class=\"tag\">Coming soon</span>" if s else ""}</button>' for i,t,d,c,s in tiles)
IO=''.join(f'<option>{n}</option>' for s,n,e in INDS)
body=phero('The Found Money Call · Free, 20 minutes','Twenty minutes, your way.','See what your spend missed.',"We look at where your business card spend goes and what it already earns. If the math won't clear the fee, you get an honest no, in writing.",
 '<span class="tag greent">No cost</span><span class="tag">No card login needed</span><span class="tag">No affiliate links</span><span class="tag pinkt">$550/month only if you say yes</span>')
body+=f'''<section class="sec white"><div class="wrap"><div class="bookgrid"><div>
<div class="step"><span class="sn">1</span><div><h3>How do you want to reach us?</h3><p class="small">Pick the one that fits your day. Same call, same honest answer.</p></div></div>
<div class="opts" data-tabs>{tl.replace('data-t="wa"','data-t="wa"')}
<div class="optpanel" data-p="wa"><p><b>Message us on WhatsApp.</b> Opens WhatsApp with a short note already written, including anything you brought from the calculator. Edit it before you send.</p><span class="pill green">💬 Open WhatsApp</span><p class="small">WhatsApp is run by Meta, as listed in our Privacy Policy. Texting is coming soon.</p></div>
<div class="optpanel" data-p="em" hidden><p><b>Email me about the call.</b> Four fields. We reply by email to set up the call.</p></div>
<div class="optpanel" data-p="cb" hidden><p><b>Call me back.</b> Leave a number and a good time. We call the number you give, nothing else.</p></div></div>
<div class="step"><span class="sn">2</span><div><h3>How should we talk on the call?</h3><p class="small">Your choice. Both are the same 20 minutes.</p></div></div>
<div class="mode" data-tabs><button type="button" class="opt on" data-t="ph"><span class="oi">📞</span><b>Phone call</b><span>We call you at the time you pick.</span></button><button type="button" class="opt" data-t="gm"><span class="oi">🎥</span><b>Google Meet</b><span>A video link arrives with your calendar invite.</span></button>
<div data-p="ph" class="modenote">Phone it is. Add your number below.</div><div data-p="gm" class="modenote" hidden>Google Meet it is. The link comes in your calendar invite.</div></div>
<div class="step"><span class="sn">3</span><div><h3>Tell us where to send the invite</h3><p class="small">Choose a time and you'll get a calendar invite and email reminders.</p></div></div>
<form class="card bkform" onsubmit="return false"><div class="grid g2"><label class="fld">First name<input placeholder="Maya"></label><label class="fld">Business email<input placeholder="maya@yourbusiness.com"></label>
<label class="fld">Industry<select><option>Choose one</option>{IO}<option>Other</option></select></label><label class="fld">Phone (for a phone call)<input placeholder="(201) 555 0142"></label>
<label class="fld">Preferred day<select><option>Any weekday</option><option>Monday</option><option>Tuesday</option><option>Wednesday</option><option>Thursday</option><option>Friday</option></select></label><label class="fld">Preferred time<select><option>Morning</option><option>Midday</option><option>Afternoon</option></select></label></div>
<label class="fld" style="margin-top:16px">Anything we should look at? (optional)<textarea rows="3" placeholder="Rough monthly card spend, the cards you use today, anything else."></textarea></label>
<div class="ctas"><span class="pill pink">Send my request</span></div>
<p class="small">This opens your own email app with the request written out, so nothing is stored on this page. By sending it you agree to our <a href="terms-of-service.html">Terms &amp; Conditions</a> and <a href="privacy-policy.html">Privacy Policy</a>.</p></form></div>
<aside class="bkside"><div class="card"><span class="kk">Here's what happens next</span>
<ol class="nsteps"><li><b>Within one business day</b> we reply on the channel you picked to set the time.</li><li><b>On the call</b> we walk through where your card spend goes. Bring a rough monthly number, nothing else.</li><li><b>After the call</b> you get a written answer: a yes at $550 a month, month to month, or an honest no.</li></ol>
<p class="small">While you wait: <a href="field-notes.html">read the field notes</a>.</p></div>
<div class="human"><div class="hi">👤</div><div><b>Strategy within 24 hours</b><p>{APPROVED}</p></div></div>
<div class="nug"><div class="coin">🪙</div><div><h3>Not sure it's worth 20 minutes?</h3><p>Run your number on the <a href="calculator.html">calculator</a> first and bring it with you.</p></div></div></aside></div></div></section>
<section class="sec cream"><div class="wrap"><div class="center"><div class="fok">Four ways in. One desk.</div></div><div class="grid g3 steps3">
<div class="card"><span class="kk">01 / The call</span><p>20 minutes on where your card spend goes and what it earns today.</p></div>
<div class="card"><span class="kk">02 / The written answer</span><p>A yes with the math behind it, or an honest no if it won't clear the fee.</p></div>
<div class="card"><span class="kk">03 / Your decision</span><p>Month to month, cancel anytime. Not ready? Get the weekday note instead.</p></div></div>
<p class="bk-note">First Officer is an educational tool, not a licensed financial advisor. {APPROVED} Calculator figures you bring here are estimates, not a projection of your results. See our <a href="terms-of-service.html">Terms &amp; Conditions</a>.</p></div></section>'''
out('book.html','Book Your “Found Money” Call',body,'book.html',band=False)

# ---------------- CALCULATOR ----------------
src=open(f'{SRC}/calculator.html').read()
js=[m.group(1) for m in re.finditer(r'<script(?![^>]*src)[^>]*>(.*?)</script>',src,re.S) if 'var IND' in m.group(1)][0]
CALCID={}
for m in re.finditer(r'id:"([a-z]+)",nm:"[^"]*",pg:"for-([a-z-]+)\.html"',js): CALCID[m.group(2)]=m.group(1)
bands=[(10,14,'1.0¢ to 1.4¢','Cashed out, or booked in the travel store on your card'),(15,22,'1.5¢ to 2.2¢','Straight transfers, economy fares, standard hotel nights'),(23,35,'2.3¢ to 3.5¢','Hotel sweet spots and mixed cabins, booked with care'),(36,50,'3.6¢ to 5.0¢','Premium cabins on partner charts, booked when award space appears')]
bd=''.join(f'<div class="band" data-lo="{a}" data-hi="{b}"><b>{c}</b><span>{d}</span></div>' for a,b,c,d in bands)
body=phero('The calculator · Estimates','What is your return','on spend?','Everyone quotes an earn rate. Almost nobody tells you what the points are worth once they are spent, and that second number decides everything. Here is the whole formula, in the open.','<span class="tag est">Estimate only · not a projection of your results</span>')
body+=f'''<div class="calcread" id="machine"><div class="wrap"><span class="kk">Live estimate · changes with your answers below</span><div class="crr"><div><small>Net this month, est.</small><b id="roNet">$0</b></div><div><small>Return on spend, est.</small><b id="roRos">0%</b></div><div><small>Flat 2% cash back</small><b id="roCash">$0</b></div></div></div></div>
<section class="sec white"><div class="wrap calcsec"><div>{head('The earn','What your spending','earns you','Pick your trade and set your monthly spend. The multipliers reflect how those vendors commonly code, which is why a restaurant and an agency get very different answers.')}
<label class="fld">Your industry<select id="indSel"></select></label></div>
<div class="card"><div id="cats" class="cats"></div><div class="tot3"><div><small>Monthly spend</small><b id="mSpend"></b></div><div><small>Blended earn rate</small><b id="mEarn"></b></div><div><small>Points a month</small><b id="mPts"></b></div></div>
<p class="small" id="capNote"></p><p class="small" id="offNote"></p></div></div></section>
<section class="sec cream"><div class="wrap calcsec"><div>{head('The burn','What those points are','worth when spent','A point has no fixed value. It is worth whatever the booking you make is worth, and the spread between the worst and best answer is the entire business.')}</div>
<div class="card"><div class="ctl"><span class="name">Cents per point</span><span class="hint">On the points you actually redeem.</span><div class="val" id="cppVal">3.0¢</div><input type="range" id="cpp" min="10" max="50" step="1" value="30"></div><div class="bands">{bd}</div>
<div class="ctl"><span class="name">Share you redeem</span><span class="hint">The lever nobody measures. Points you never redeem are worth nothing, and balances lose ground while they wait.</span><div class="val" id="mUtil">85%</div><input type="range" id="util" min="0" max="100" step="5" value="85"></div>
<div class="tot3"><div><small>Points redeemed</small><b id="mUsed"></b></div><div><small>Travel value, at sticker, est.</small><b id="mValue"></b></div></div></div></div></section>
<section class="sec white"><div class="wrap calcsec"><div>{head('The honest discount','How much of it would you','have paid cash for?','This is where most calculators cheat. A $9,000 business class ticket is only worth $9,000 to you if you would have bought it. Set the share you would genuinely have paid for and we will value the rest at what a sensible cash alternative costs instead.')}</div>
<div class="card"><div class="ctl"><span class="name">Share you would have bought anyway</span><div class="val" id="realVal">60%</div><input type="range" id="real" min="0" max="100" step="5" value="60"></div></div></div></section>
<section class="sec cream"><div class="wrap calcsec"><div>{head('The return','The formula,','with our fee inside it','One month at a time, because that is how a fee is felt. Our $550 comes out before you see the number.')}</div>
<div><div class="rows"><div class="r"><span>Monthly spend</span><span id="fSpend"></span></div><div class="r"><span>× Gross return, est.</span><span id="fRate"></span></div><div class="r minus"><span>− Our fee</span><span>$550</span></div><div class="r tot"><span>= Net, this month, est.</span><span id="fNet"></span></div></div>
<div class="card rosbox"><span class="kk">Estimated return on spend</span><b id="rosBig"></b><p id="rosSub"></p></div>
<div class="grid g2"><div class="card"><span class="kk">A flat 2% cash back card</span><b class="vsn" id="vsCash"></b><p class="small">Simple, certain, and it needs no desk. Worth remembering that a rebate also reduces the business expense you deduct, so ask your accountant what it nets.</p></div>
<div class="card vsus"><span class="kk">Routed, booked, after our fee, est.</span><b class="vsn" id="vsUs"></b><p class="small">Discounted to what you would have paid cash for, so this is a like for like comparison rather than a sticker price.</p></div></div>
<div class="ctas">{BOOK}<a class="pill ghost" href="pricing.html">See what the desk costs →</a></div></div></div>
<div class="wrap"><p class="l4note">Point valuations are estimates based on common redemption benchmarks. Actual value depends on how and when you redeem. Estimate only, built from category averages and common transfer partner valuations, before card annual fees. Bonus rates are capped on published product terms: 4x and 3x hold on the first $150,000 a year at each rate, then 1x; flat 2x assumes a card with an annual fee. Starting spend figures are illustrative profiles, not client data. Award pricing and availability change constantly and we control neither. Not a guarantee of any outcome and not financial or tax advice.</p></div></section>'''
calc_html=page('Calculator · First Officer',fix(body,'calculator.html'),active='calculator.html',src='calculator')
calc_html=calc_html.replace('</body>','<script>'+js+'</script></body>')
write('calculator.html',calc_html); print('wrote calculator')

# ---------------- INDUSTRIES ----------------
cards=''.join(f'<a class="indcard" href="for-{s}.html"><div class="iph" style="background-image:url(img/ind/{s}.jpg)"></div><div class="ib"><span class="ie">{e}</span><h3>{n}</h3><p>{E(IJ[s]["h1b"][0].upper()+IJ[s]["h1b"][1:])}</p><span class="go">See the codes →</span></div></a>' for s,n,e in INDS)
sel='<select data-go aria-label="Pick your industry"><option value="">Pick your industry…</option>'+''.join(f'<option value="for-{s}.html">{e} {n}</option>' for s,n,e in INDS)+'</select>'
body=phero('Industries · 20 trades','Your trade decides','what your cards earn.','Every card payment carries a merchant code set by the seller’s processor. The same dollar earns 1x or 4x depending on how your vendors code. Pick your industry and see the codes that matter.',f'<div class="indsel">{sel}</div>')
body+=f'<section class="sec white"><div class="wrap">{head("All 20","Find yours,","then run the number.","Each page shows the codes your vendors commonly run under, the golden nuggets worth knowing, and a calculator preset for your trade.")}<div class="indgrid">{cards}</div></div></section>'
out('industries.html','Industries',body,'industries.html')

def indpage(s,d,tmpl=False):
    n,e=NM.get(s,('{Industry}','🏷️'))
    ph=PH.get(s,{})
    img=f'img/ind/{s}.jpg' if not tmpl else 'img/ind/desk.jpg'
    pola=f'<figure class="pola"><img src="{img}" alt="{E(ph.get("alt",""))}"><figcaption>{E(ph.get("cap","Your industry, in the real world"))}{f" · Photo: <a href={chr(34)}{ph["url"]}{chr(34)}>{E(ph["credit"])}</a> / Unsplash" if ph else ""}</figcaption></figure>'
    others='<select data-go aria-label="Another industry"><option value="">Another industry…</option>'+''.join(f'<option value="for-{x}.html">{ee} {nn}</option>' for x,nn,ee in INDS)+'</select>'
    b=phero(f'{e} For {d["name"].lower()}',d['h1a'],d['h1b'],d['intro'],f'{BOOK}<a class="pill ghost" href="calculator.html?ind={CALCID.get(s,"")}">Run the {n} preset →</a>',pola)
    ng=''.join(f'<div class="nug"><div class="coin">🪙</div><div><h3>{E(t)}</h3><p>{E(p)}</p></div></div>' for t,p,src_ in d['nuggets'])
    thin=f'<div class="l4note thinn"><b>What we could not source yet:</b> {E(d["thin"])}</div>' if d.get('thin') else ''
    rows=''.join(f'<tr><td class="mono">{c}</td><td>{E(t)}</td><td>{E(w)}</td></tr>' for c,t,w in d['codes'])
    b+=f'''<section class="sec white"><div class="wrap">{head("Golden nuggets","What most "+d["name"].lower()+" never hear","about their codes.")}<div class="grid g3 nuggrid">{ng}</div>{thin}</div></section>
<section class="sec cream"><div class="wrap">{head("The codes","Where your money","actually lands.","The merchant codes your vendors commonly run under. Check your own statements; the desk verifies every one before routing.")}
<div class="card tblcard"><table class="mcc"><thead><tr><th>Code</th><th>Category</th><th>Who usually runs it</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="grid g2" style="margin-top:28px"><div class="human"><div class="hi">👤</div><div><b>Strategy within 24 hours</b><p>{APPROVED}</p></div></div><div class="card"><span class="kk">Not your trade?</span>{others}<p class="small" style="margin-top:12px"><a href="industries.html">All 20 industries →</a></p></div></div></div></section>'''
    return b
for s,n,e in INDS:
    out(f'for-{s}.html',n,indpage(s,IJ[s]),'industries.html')
T={'name':'{Industry}','h1a':'{Industry}:','h1b':'{one line on what decides the earn}.','intro':'{Intro: one or two sentences on how merchant codes work in this trade.}','codes':[['{MCC}','{Category name}','{who usually runs it}']]*4,'nuggets':[['{Nugget headline}','{One or two verifiable sentences.}','']]*3,'thin':'{Optional: what we could not verify, shown when fewer than 3 nuggets.}'}
out('industry-template.html','Industry template',indpage('template',T,True),'industries.html')

# ---------------- FREE FROM THE DESK (content from fo-home-v2 tools/build_desk.py) ----------------
V=open('/workspace/fo-home-v2/tools/build_desk.py').read().split('\n')
ns={'re':re}; exec('\n'.join(V[8:49]),ns)
ffd=re.sub(r'(<article class="dk gold"[^>]*>\s*<div class="dk-top"><div class="ic">)<svg.*?</svg>',r'\1<span class="coin">🪙</span>',''.join(ns['cards']),flags=re.S); pick=ns['picker']; calcic=ns['IC']['calc']
for x,y in [("Visa's name for it","Category"),("Visa\\'s name for it","Category"),('<span class="chip a">Visa MDSM</span>',''),('Source: Visa Merchant Data Standards Manual. ','Codes from the card networks\' published merchant code lists. '),
  ('Merchant codes are defined in the Visa Merchant Data Standards Manual.','Merchant codes come from the card networks\' published lists.'),('Source: Visa MDSM','Source: network code lists'),('Coding: Visa MDSM','Coding: network code lists'),('Visa, IRS, EPA','IRS, EPA, code lists'),('Visa, IRS','IRS, code lists'),
  ('for-contractors-v2.html','for-contractors.html'),('stroke="#141216"','stroke="#3a3540"'),('fill="#141216"','fill="#3a3540"')]:
    ffd=ffd.replace(x,y); calcic=calcic.replace(x,y)
body=f"""<section class="phero split ffdhero"><img class="chev" src="img/fo-chevron-alpha.png" alt=""><div class="wrap"><div><div class="fok">Free From the Desk</div><h1>Everything I'd tell you <span class="pk">over coffee.</span></h1>
<p class="fosub">Most owners put serious money on cards every month, and nobody ever sits them down and explains how it actually works. So here it is: the codes, the questions, the notes we keep for each trade. Free. <b>No email. No catch.</b></p>
<div class="sig"><div class="av">O</div><div><span class="sign">Ohad</span><span class="role">Founder, UpNonStop</span></div></div></div>
<a class="feat card" href="calculator.html"><span class="kk">Start here</span><div class="fic">{calcic}</div><h2>The Found Money Calculator</h2><p>Put in what you spend in a normal month. See what it could be worth, with every assumption shown so you can argue with it.</p><div><span class="tag est">Estimate</span> <span class="small">takes 60 seconds</span></div><span class="pill pink">Run my numbers →</span></a></div></section>
<section class="sec white"><div class="wrap"><figure class="deskphoto"><img src="img/ind/desk.jpg" alt="A notebook, pen and cup of coffee on a white desk"><figcaption><span>Pull up a chair. Coffee's on me.</span><span>Photo: <a href="https://unsplash.com/photos/56J8143b7PU">Elena Leya</a> / Unsplash</span></figcaption></figure>
<div class="filters">{pick}</div><div class="dkgrid">{ffd}</div>
<div class="endnote card"><p>That's the desk. Take whatever helps. If you'd rather we just do it for you, that's what <a href="book.html">The Found Money Call</a> is: 20 minutes, and if the math says no, I'll tell you no.</p><span class="sign">Ohad</span></div>
<p class="l4note"><b>Plainly:</b> First Officer is an educational tool, not a licensed financial advisor. Nothing here is financial, tax or legal advice. Every number is sourced or labeled Example, and your results will be different. Rules change, so check with your issuer or program before you act. No affiliate links, and no money from any bank or program. Nobody pays us to send you anywhere. <a href="terms-of-service.html">Terms &amp; Conditions</a></p></div></section>
<script>(function(){{var f={{ind:'all',ty:'all'}};document.querySelectorAll('.picker button').forEach(function(b){{b.addEventListener('click',function(){{f[b.dataset.k]=b.dataset.v;document.querySelectorAll('.picker button[data-k="'+b.dataset.k+'"]').forEach(function(x){{x.classList.toggle('on',x===b)}});document.querySelectorAll('.dk').forEach(function(c){{var i=c.dataset.ind.split(' ');var ok=(f.ind=='all'||i.indexOf(f.ind)>-1||i.indexOf('all')>-1)&&(f.ty=='all'||c.dataset.ty==f.ty);c.hidden=!ok}})}})}})}})();</script>"""
out('free-from-the-desk.html','Free From the Desk',body,'free-from-the-desk.html')

# ---------------- UPNS archive ----------------
U=[('064','July 25, 2026','The year’s biggest door closes Thursday, July 30.','Most of you should walk past it.'),('063','July 18, 2026','Example: a 100% transfer bonus.','The richest windows close fast.'),('062','July 11, 2026','5 bonus windows are open this week.','2 of them close Tuesday night.')]
uc=''.join(f'<a class="card ucard" href="upns-{n}.html"><img src="img/upns/UPNS-{n}-TEASER.png" alt="UPNS-{n} teaser"><div><span class="kk">UPNS-{n} · {d}</span><h3>{E(a)} <span class="pk">{E(b)}</span></h3><span class="go">Read the dispatch →</span></div></a>' for n,d,a,b in U)
body=phero('The Intelligence Report · Saturday Dispatch','Every Saturday,','the week, read for you.','Transfer bonuses worth acting on, quiet repricings that shrink your points, and one save from a wallet like yours. It starts plain and gets deeper as you scroll.')
body+=f'<section class="sec white"><div class="wrap"><div class="ugrid">{uc}</div><div class="l4note">Issues use lettered placeholders (Bank A, Airline A) and illustrative figures. Aggregates describe an illustrative client base.</div></div></section>'
out('upns.html','The Intelligence Report',body,'free-from-the-desk.html')

# ---------------- DISCLAIMER ----------------
body=phero('Disclaimer','Plain words,','no fine print games.','What First Officer is, what it is not, and how to read the numbers on this site.')
D=[('An educational tool','First Officer is an educational tool, not a licensed financial advisor. Nothing on this site is financial, tax or legal advice. Ask your accountant before acting on anything with a tax angle.'),
('How the desk works',APPROVED),('Estimates are estimates','Point valuations are estimates based on common redemption benchmarks. Actual value depends on how and when you redeem. Calculator figures are estimates, not a projection of your results.'),
('Award pricing','Award pricing and award space change constantly and we control neither. Not a guarantee of any outcome.'),
('Illustrative stories','Client stories are shared with permission. Names, figures and examples on this site may be illustrative or altered to protect privacy. Personas on this site are fictional.'),
('Independence','UpNonStop has no affiliate relationships with any issuer. We are not paid by any card, bank or program for what we recommend.'),
('Who it is for','US businesses only. The monthly fee is $550, month to month, cancel anytime. Award search is a separate $500 per trip, always.')]
body+='<section class="sec white"><div class="wrap legalw">'+''.join(f'<h2>{t}</h2><p>{p}</p>' for t,p in D)+'<p class="small">Mockup text assembled from disclaimer lines already on the site. Needs review before publishing.</p></div></section>'
out('disclaimer.html','Disclaimer',body)

# ---------------- APP (coming soon) ----------------
side='<div class="herochat"><div class="phone"><div class="wa-head"><p><b>First Officer</b></p><p>app preview</p></div><div class="bub in"><p>Friday · Week 33 Capture Report is ready. $3,900 captured, est.</p></div><div class="bub out"><p>Nice. What is next week?</p></div><div class="bub in"><p>One transfer bonus worth acting on. I will send the math before anything moves.</p></div><p class="wa-cap">Illustrative preview</p></div></div>'
body=phero('The app · Coming soon','Your desk,','in your pocket.','The First Officer app is coming soon. Today the desk lives in one WhatsApp thread, and texting is coming soon too. Nothing changes about how it works: '+APPROVED,'<a class="pill green" href="book.html">💬 Text Your First Officer</a><span class="tag">App coming soon</span>',side)
body+=f'<section class="sec white"><div class="wrap"><div class="grid g3"><div class="card"><span class="kk">Today</span><h3>WhatsApp</h3><p>One thread, every answer, every Friday report.</p></div><div class="card"><span class="kk">Coming soon</span><h3>Texting</h3><p>The same thread over plain text messages.</p></div><div class="card"><span class="kk">Coming soon</span><h3>The app</h3><p>Your reports, your balances and your thread in one place.</p></div></div><div class="l4note">This page appears when a private link is opened outside your thread: “This link needs to come from your thread.” The production page keeps that message.</div></div></section>'
out('app.html','The app',body)
save_log()
