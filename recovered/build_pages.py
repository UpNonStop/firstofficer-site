# Builds the deeper "-modes" pages (product, book, about, industries, trust, freebies) on rec.css + modes.css,
# same hero system as home-modes (rotating low-opacity vacation photos), mobile-first patterns:
# swipe rails with rectangle progress, tap-to-expand on phones, phone mockup as the hero star, inline CTAs.
# Mockup only. Every owner is fictional and every figure is illustrative, est.
import os,sys,re,json,subprocess
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.dirname(HERE)
sys.path.insert(0,HERE)
import build as B
WA='https://wa.me/16199404040?text=First%20Officer%20Found%20Money%20Call'
ILL='Illustrative mockup figures, est.'
LINKS=[('product-recovered.html','product-modes.html'),('pricing.html','pricing-modes.html'),('freebies.html','freebies-modes.html'),
       ('calculator.html','calculator-modes.html'),('about.html','about-modes.html'),('trust.html','trust-modes.html'),
       ('industries.html','industries-modes.html'),('book.html','book-modes.html'),('home-recovered.html','home-modes.html')]
def relink(h):
    for a,b in LINKS: h=h.replace('href="'+a,'href="'+b)
    return h
NAMES={1:'Amex',2:'Chase',17:'United',12:'Hyatt',47:'Virgin Atlantic',25:'Aeroplan',9:'Marriott',18:'Delta'}
SL={1:'amex',2:'chase',17:'united',12:'hyatt',47:'virgin-atlantic',25:'aeroplan',9:'marriott',18:'delta'}
LOGOS=[1,12,2,17,47,18,25,9]
def logos(): return '<div class="mlogos">'+''.join('<img src="img/hero/prog/%02d-%s.jpg" alt="%s">'%(n,SL[n],NAMES[n]) for n in LOGOS)+'<span>Every loyalty program. One desk to rule them all.</span></div>'
def personas():
    return json.loads(subprocess.check_output(['node','-e',"global.window={};require(process.argv[1]);process.stdout.write(JSON.stringify(window.FO_MODES))",os.path.join(HERE,'fo-modes-data.js')]))
P=personas()
def esc(s): return s.replace('&','&amp;')
def x(n): return ('%.1f'%n).rstrip('0').rstrip('.')+'x'
def usd(n): return '${:,}'.format(int(round(n)))
def pts(n): return (('%.2f'%(n/1e6)).rstrip('0').rstrip('.')+'M') if n>=1e6 else ('%dk'%round(n/1e3))
def dm(d,m): return '<span class="dk">%s</span><span class="mb">%s</span>'%(d,m)
THREAD='<span class="thr" aria-hidden="true"><i class="te"></i><i class="tb"></i><i class="tr"></i><i class="tl"></i></span>'

def ctas(pk=('Get your desk','book-modes.html'),calc=None):
    h='<div class="mctas"><a class="btn pk" href="%s">%s <span class="ar">→</span></a><a class="btn wa" href="%s">💬 Text Your First Officer</a></div>'%(pk[1],pk[0],WA)
    if calc: h+='<a class="mcalc" href="%s">%s <span class="ar">→</span></a>'%calc
    return h

def hero(pill,h1,sub,checks,visual,pk=('Get your desk','book-modes.html'),calc=('calculator-modes.html','or run the calculator'),cls=''):
    lis=''.join('<li><b>✓</b><span>%s</span></li>'%c for c in checks)
    return f'''<section class="mh ph {cls}" id="mh"><div class="mbg" aria-hidden="true"></div>
<div class="phw">
<div class="pht"><span class="mpill"><i></i>{pill}</span><h1>{h1}</h1></div>
<div class="phv">{visual}</div>
<div class="phb"><ul class="mprob">{lis}</ul><p class="msub">{sub}</p>{ctas(pk,calc and (calc[0],calc[1]))}{logos()}</div>
</div></section>
'''

def sec(kick,h2,lede,body,cls='',id_=''):
    return f'''<section class="sec pgs {cls}"{' id="'+id_+'"' if id_ else ''}><div class="wrap">
<div class="reveal"><span class="kick">{kick}</span><h2 class="h2">{h2}</h2>{'<p class="lede">'+lede+'</p>' if lede else ''}</div>
{body}
</div></section>
'''

def rail(cards,cols=4,label='Cards'):
    return f'<div class="srail" style="--cols:{cols}" role="list" aria-label="{label}">'+''.join(f'<div class="rc" role="listitem">{c}</div>' for c in cards)+'</div><div class="sdots" aria-hidden="true"></div>'

def nxt(n,href,title,hook,btn):
    return f'''<section class="sec tight pnx"><div class="wrap"><a class="nxt reveal" href="{href}">
<span class="nxk">{THREAD}Next chapter · {n}</span><b class="nxh">{title}</b><span class="nxp">{hook}</span><span class="nxb">{btn} <span class="ar">→</span></span></a>
</div></section>
'''

def deskcta(line):
    return f'''<section class="sec tight"><div class="wrap"><div class="pcta"><div class="pctx"><b>Get your desk.</b><span>{line}</span></div><div class="pbtn"><a class="btn pk" href="book-modes.html">Get your desk <span class="ar">→</span></a><a class="btn wa" href="{WA}">💬 Text Your First Officer</a></div></div></div></section>
'''

PILL=[('earn','01','Earn','Which card for which spend.','More points from the spend you already have.'),
      ('burn','02','Burn','Points into trips, vetted.','Better trips for the points you earn. The desk vets every requirement with you and books after you approve.'),
      ('return','03','Return','What the desk found, counted every Friday.','Counted in dollars and checked against your statements.'),
      ('learn','04','Learn','One short lesson a week, from your data.','Know what your points are worth, and what changed in your programs.')]
def pillars(extra=None):
    cards=[]
    for i,(k,n,t,h,p) in enumerate(PILL):
        cards.append(f'<div class="pc4 k-{k}"><div class="pn"><b>{n}</b>{t}</div><h3>{h}</h3><p>{p}</p>{extra[i] if extra else ""}</div>')
    return rail(cards,4,'The four pillars')

def stories(lim=10):
    K=['earn','burn','return','learn']
    out=[]
    for i,p in enumerate(P[:lim]):
        r=sum(v for _,v in p['ret']);c=p['cats'][0]
        out.append(f'''<div class="st"><div class="sth"><span class="sti">{p["ini"]}</span><div><b>{p["first"]}, {esc(p["biz"])}</b><small>{p["ind"]} · {p["city"]}</small></div></div>
<p class="stq">“{esc(p["qE"])}”</p>
<div class="stba"><div><small>Before</small><b>{x(p["from"])}</b><span>per $1</span></div><i>→</i><div class="a"><small>With the desk</small><b>{x(p["to"])}</b><span>per $1</span></div></div>
<p class="stc"><b class="k-earn">The catch</b>{esc(c[0])} was earning {c[2]}. The desk lines it up with a {c[3]} card: {esc(p["move"][0].lower())}, about {usd(p["move"][1])} a year.</p>
<p class="stc"><b class="k-burn">The trip</b>{esc(p["trip"])}, {esc(p["when"].lower() if p["when"][0].isupper() and p["when"].split()[0] in ("Spring","Next","This") else p["when"])}: {p["pct"]}% there.</p>
<p class="stc"><b class="k-return">One Friday</b>{usd(r)} found, from {esc(p["ret"][0][0][0].lower()+p["ret"][0][0][1:])} and more.</p>
<small class="ill">Fictional owner. {ILL}</small></div>''')
    return rail(out,3,'Owner stories')

def page(fn,title,desc,body,on=''):
    h=B.head(title,desc)
    h=h.replace('<link rel="stylesheet" href="recovered/rec.css">','<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kalam:wght@300;400&display=swap">\n<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">')
    h+='<body class="modes pgx">\n'+B.nav(on).replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')+B.ticker()+'<main>\n'+body+'</main>\n'
    h+=B.footer().replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.','Every owner shown is a fictional example. All figures are illustrative estimates.')
    h+='<script>window.FO_A="'+B.ASSET+'";</script>\n<script src="recovered/rec.js"></script>\n<script src="recovered/pages.js"></script>\n</body>\n</html>\n'
    h=h.replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')
    h=re.sub(r'<div class="mcta">.*?</a></div>\n?','',h,flags=re.S)
    h=h.replace('<a class="btn pk" href="'+WA+'">💬 Text Your First Officer</a>\n<button class="burger"','<span class="nbtns"><a class="btn pk" href="book.html">Get your desk</a><a class="btn wa" href="'+WA+'">💬 Text Your First Officer</a></span>\n<button class="burger"',1)
    h=h.replace('<a class="btn pk" href="'+WA+'">💬 Text Your First Officer</a>\n</div>','<a class="btn wa" href="'+WA+'">💬 Text Your First Officer</a>\n</div>',1)
    assert 'class="nbtns"' in h,fn
    h=relink(h)
    open(os.path.join(ROOT,fn),'w').write(B.absol(h));print('built',fn)

# ---------------- product: what the desk can do ----------------
def product():
    L=P[0]
    vis='<div class="celcol phstar">'+B.celphone(B.cs_found(' on')+B.cs_ahead()+B.cs_goal())+'<div class="celnav"><button>Found money</button><button>Ahead</button><button>Milestone</button></div><small class="ill">Example app screens. '+ILL+'</small></div>'
    h=hero('Product · what the desk can do','Outnumbered? <span class="pk">Now you have a desk.</span>',
      dm('Every program has a team rewriting the rules. You get one conversation with a desk that keeps up: it matches your spend to the right cards, plans trips with your points, counts what it finds every Friday, and teaches you along the way.','One conversation. A desk that keeps up with the rules, so you don\'t have to.'),
      ['One conversation, every program.','Every move waits for your yes.','One number in dollars, every Friday.'],vis)
    ch=[('earn','Chapter 1 · Earn','The ads were on the wrong card.','Leo puts about $35K a month on cards. Lead-gen ads, $14K of it, earned 1x. The desk matches them to a 4x card and shows the move in dollars before anything changes.',
         '<div class="bfa"><div><small>Before</small><b>1.2x</b><span>per $1</span></div><i>→</i><div class="a"><small>With the desk</small><b>3.4x</b><span>per $1</span></div></div>','Ads to the 4x card: about +$7,200 a year. Waiting for Leo\'s OK.'),
        ('burn','Chapter 2 · Burn','Tokyo stopped being a someday.','102,400 points were sitting still. The desk maps the transfer partners, checks taxes and fees, and gives the trip a pace and a plan.',
         '<div class="bgo"><div class="im" style="background-image:url(img/tokyo.jpg)"></div><div><b>Tokyo in business for 2</b><small>Spring 2027 · 32% there</small><div class="tr"><i style="width:32%"></i></div></div></div>','Every requirement vetted with Leo. Nothing moves until he approves.'),
        ('return','Chapter 3 · Return','Friday counted it, in dollars.','A travel credit was about to reset unclaimed. Software was on a 1x card. The Friday scorecard counts each catch in dollars and checks it against the statement.',
         '<ul class="bls"><li><span>Software on the 4x card</span><b>$640</b></li><li><span>Carrier visits through the travel portal</span><b>$690</b></li><li><span>Unused travel credit, claimed</span><b>$530</b></li><li class="t"><span>Week 43</span><b>$1,860</b></li></ul>','One number, in dollars, never in points.'),
        ('learn','Chapter 4 · Learn','Now he knows what a point is worth.','Two minutes a week, built from Leo\'s own data. What changed in his programs, and what it means for Tokyo.',
         '<div class="bfa"><div><small>A card point</small><b>1.6¢</b><span>est.</span></div><i>·</i><div class="a"><small>This week</small><b>2 min</b><span>lesson</span></div></div>','Points in some programs expire without activity. The lesson says which, and when.')]
    chap=''.join(f'''<article class="chp k-{k} reveal"><div class="chx"><span class="chk">{kk}</span><h3>{t}</h3><p>{d}</p><p class="chm"><b>✓</b>{m}</p></div><div class="chv">{v}<small class="ill">Leo is fictional. {ILL}</small></div></article>''' for k,kk,t,d,v,m in ch)
    body=h
    body+=sec('One owner, four chapters',"Meet Leo. <span class=\"brush\">Watch the desk catch what he missed.</span>",
        dm('Leo runs Linden Row Insurance in Columbus, Ohio. He is not bad at points. He is outnumbered. Here is a year at his desk, one pillar at a time.','Leo runs an insurance agency. He is not bad at points. He is outnumbered.'),
        '<div class="chps">'+chap+'</div>',id_='leo')
    body+=sec('The win','When money lands, <span class="brush">your app cheers.</span>','Found money, a month ahead of flat cash back, a points milestone. Each one gets its moment.',
        '<div class="win3"><div class="wcards">'+B.scorecard()+'</div><div class="wcards">'+B.versus()+B.share().replace(' style="background:rgba(255,255,255,.2);color:#fff"','')+'</div></div><p class="p4f">Example: Leo, Linden Row Insurance. Fictional. '+ILL+'</p>',cls='pwin')
    body+=sec('Ten owners, ten catches','Every trade hides money <span class="brush">in a different place.</span>',dm('Swipe through ten owners like you. Each one asked a simple question, and each desk caught something different.','Swipe: ten owners, ten different catches.'),stories(),id_='stories')
    steps=[('Today','Your desk opens','Tell First Officer about your spend and goals. About 10 minutes.'),('Day 1','Time-boxed fixes first','A credit about to reset, points about to lapse.'),('Within 24 hours','Your Bespoke Strategy','Which card for which spend, line by line.'),('Week 1','Your first moves','Three moves, with the exact taps shown. Each waits for your yes.'),('Every Friday','Your scorecard','One number, in dollars.'),('Month 1','Us vs flat cash back','Your month next to a flat 2% card, after the $550 fee.'),('Month 3','Your first trip goal','The desk vets the requirements with you and books after you approve.')]
    tl='<ol class="tl90">'+''.join(f'<li class="reveal"><span>{a}</span><b>{b}</b><p>{c}</p></li>' for a,b,c in steps)+'</ol>'
    body+=sec('After you are in','Your first 90 days, <span class="brush">step by step.</span>','Some things are fast. Some take time. Here is what happens, and what the desk asks of you.',tl)
    LK=[('earn','Leak 01 · Earn','Your spend codes wrong.','Wholesale vendors, insurance, fuel and freight often earn 1x. Ads, software and fuel can earn more on the right card.','Move the vendor to the right card. What you buy stays the same.'),
        ('burn','Leak 02 · Burn','Your points get spent cheaply.','A plain cash-out prices a point at about a cent. A well-planned transfer can be worth more, est.','The desk plans where points go, and books only after you approve.'),
        ('return','Leak 03 · Return','Value quietly runs out.','Credits reset, certificates lapse and balances can expire. None of it announces itself.','The desk watches the clocks and flags each one in time.')]
    body+=sec('Where the money hides','Three leaks. <span class="brush">Three fixes.</span>',dm('Most businesses lose value in the same three places, and none of the fixes ask you to spend differently.','Three places value leaks. None of the fixes change what you buy.'),
        rail([f'<div class="pc4 k-{k}"><div class="pn"><b>{a}</b></div><h3>{t}</h3><p>{d}</p><p class="chm"><b>✓</b> The fix: {f[0].lower()+f[1:]}</p></div>' for k,a,t,d,f in LK],3,'Three leaks'),id_='leaks')
    body+=nxt('03','calculator-modes.html','Leo\'s numbers are fiction. <span class="pk">Yours aren\'t.</span>','Move one slider and see what your spend is really worth, against $550 a month: fits, close call or not a fit.','Run your numbers')
    page('product-modes.html','Product | One desk, four pillars | First Officer','What the desk can do: Earn, Burn, Return, Learn. Fictional examples, illustrative estimates.',body,'Product')

# ---------------- book: the Found Money Call ----------------
def book():
    thread='''<div class="wat"><div class="wath"><b>First Officer</b><small>Found Money Call</small></div>
<p class="bu me">Hi, I'd like a Found Money Call. Insurance agency, about $35K a month on cards.</p>
<p class="bu">Happy to. Twenty minutes. Send a recent statement or two when you're ready, a screenshot works.</p>
<p class="bu me">Sent. What do you look at?</p>
<p class="bu">Where the spend goes, what it earns today, and what the desk could find. Then the number, in dollars, against $550 a month.</p>
<small class="ill">Example conversation. {ILL}</small></div>'''.replace('{ILL}',ILL)
    h=hero('The Found Money Call · free, 20 minutes','Twenty minutes, your way. <span class="pk">See what your spend missed.</span>',
      dm('We look at where your business card spend goes and what it already earns, from your real statements. Then the number: fits, close call or not a fit. $550 a month only if you say yes.','Your real statements, twenty minutes, one number. $550 a month only if you say yes.'),
      ['No cost, no card login needed.','No affiliate links.','Your number, against $550 a month.'],thread,pk=('Book the call','#doors'),calc=('calculator-modes.html','or run the calculator first'))
    doors=[('wa','Door one','WhatsApp','Message us and we reply in the thread. The fastest door.','<a class="btn wa" href="'+WA+'">💬 Open WhatsApp</a>'),
           ('em','Door two','Email','Send a short note with your industry and monthly card spend. We reply by email to set the time.','<a class="btn ghost" href="mailto:desk@upnonstop.com?subject=Found%20Money%20Call%20request&amp;body=Industry%3A%20%0AMonthly%20card%20spend%3A%20about%20%24">Email the desk</a>'),
           ('cb','Door three','Call me back','Leave a number and a good time in a message. We call the number you give.','<a class="btn ghost" href="'+WA.replace('Found%20Money%20Call','Callback%20request%20for%20a%20Found%20Money%20Call')+'">Ask for a callback</a>')]
    dc=[f'<div class="door d-{k}"><span class="chk">{a}</span><h3>{b}</h3><p>{c}</p>{btn}</div>' for k,a,b,c,btn in doors]
    body=h+sec('Pick your door','Three ways in. <span class="brush">One desk.</span>','Every door leads to the same desk and the same twenty minutes.',rail(dc,3,'Ways to book'),id_='doors')
    steps=[('earn','Day 1','We reply','Within one business day, on the channel you picked, to set the time.'),('burn','The call','Twenty minutes','Where your card spend goes and what it already earns.'),('return','After','Your number','What the desk could find, est., and whether it clears the fee.'),('learn','Your call','Yes or no','Say yes and the desk opens. Say no and you keep the number.')]
    body+=sec('After you reach out','What happens next, <span class="brush">in four beats.</span>','',pillars_like(steps))
    body+=sec('Fits, close call, not a fit','Three owners. <span class="brush">Three honest answers.</span>',dm('The call works out where you land. These are illustrative edge cases, so you know what each answer looks like.','Three illustrative answers, so you know what each looks like.'),edge(),id_='edge')
    body+=numbers()
    body+=nxt('∞','product-modes.html','Not ready to talk? <span class="pk">Watch the desk work first.</span>','Follow Leo through Earn, Burn, Return and Learn, then come back with your statements.','See what the desk does')
    page('book-modes.html','Book the Found Money Call | First Officer','Twenty minutes, free. See what your business card spend missed, against $550 a month.',body)

def pillars_like(steps):
    return rail([f'<div class="pc4 k-{k}"><div class="pn"><b>{a}</b></div><h3>{b}</h3><p>{c}</p></div>' for k,a,b,c in steps],4,'Steps')

def edge():
    E=[('fit','✓','Fits','$35K a month on cards','Insurance agency','~$850','a month found, est.','The floor of the range beats $550. The desk opens if you say yes.'),
       ('meh','≈','Close call','$26K a month on cards','Restaurant','$420–$640','a month found, est.','Only the top of the range clears $550. The call settles it on your statements.'),
       ('no','×','Not a fit yet','$15K a month on cards','E-commerce','~$300','a month found, est.','Under $550. Keep the card you have, use the Freebies, come back as you grow.')]
    return rail([f'<div class="edg e-{c}"><div class="edh"><b aria-hidden="true">{s}</b><span>{t}</span></div><p class="eds">{sp} · {ind}</p><div class="edv"><b>{v}</b><small>{u}</small></div><div class="edf"><span>vs the fee</span><b>$550</b></div><p>{d}</p><small class="ill">{ILL}</small></div>' for c,s,t,sp,ind,v,u,d in E],3,'Edge cases')

def numbers():
    N=[('The desk','$550','a month, flat','Whatever the spend, the same fee.'),('The Found Money Call','20 min','free, and first','Your number from your real statements.'),('The report','Friday','every week','What the desk found, counted in dollars.'),('The decisions','Yours','every move','The desk advises, reminds, calculates and flags. You approve. The desk books after vetting.')]
    return f'''<section class="sec tight"><div class="wrap"><div class="reveal"><span class="kick">The numbers</span><h2 class="h2">Four numbers <span class="brush">to hold us to.</span></h2></div>
<div class="why">'''+''.join(f'<div class="reveal d{i}"><b>{v}</b><span><strong>{a}</strong> · {u}. {d}</span></div>' for i,(a,v,u,d) in enumerate(N))+'</div></div></section>\n'

# ---------------- about ----------------
def about():
    import build_modes as M
    vis='<div class="abv"><div class="abq"><span class="chk">The mission</span><b>You are not bad at Points &amp; Miles.</b><b class="pk">You are just outnumbered.</b><p>Every program has a team rewriting the rules. We built a desk to stand on your side of the table.</p></div>'+'<div class="abph" style="background-image:url(img/hero/dest/01.jpg)" role="img" aria-label="A trip worth planning"></div></div>'
    h=hero('About · why First Officer','Every program has a team. <span class="pk">Now you do too.</span>',
      dm('UpNonStop started with one question from owners: am I doing this right? Usually the honest answer was no, and not because they were careless. The rules change faster than anyone with a business to run can follow.','Owners kept asking: am I doing this right? The rules move faster than anyone running a business can follow.'),
      ['A desk for US business owners.','No affiliate money from any program.','Every move waits for your yes.'],vis,pk=('Meet the desk','product-modes.html'))
    rules=[('earn','Rule one','Your yes, first.','Nothing moves without your approval. A recommendation is a recommendation until you say yes.'),
           ('burn','Rule two','No affiliate money.','Nobody pays us to recommend a card. The only person who pays us is you.'),
           ('return','Rule three','Dollars, not points.','Every Friday, one number in dollars, checked against your statements.')]
    rc=[f'<div class="pc4 k-{k}"><div class="pn"><b>{a}</b></div><h3>{b}</h3><p>{c}</p></div>' for k,a,b,c in rules]
    body=h+M.note()
    body+=sec('01 · The mission','You run the business. <span class="brush">The desk runs the points.</span>',dm('Business owners put real money on cards every month and most of it earns less than it could. The desk exists to close that gap, one move at a time, with you deciding every move.','Most business card spend earns less than it could. The desk closes the gap, with you deciding.'),'')
    body+=sec('02 · The rules','Three rules <span class="brush">we work by.</span>','',rail(rc,3,'Our rules'))
    body+=sec('03 · The system','Four pillars, <span class="brush">in this order.</span>','Earn feeds Burn. Burn shows up in Return. Learn keeps you a step ahead.',pillars())
    nots=[('Not a bank','We are not a bank, lender or broker.'),('Not an advisor','We are not a licensed financial, tax or legal advisor. Rewards guidance only.'),('Not a booking site','The desk books ad hoc, only after vetting with you and your approval.'),('Not a guarantee','Award space, transfer ratios and program rules change. Figures are estimates.')]
    body+=sec('04 · What we are not','Clear lines, <span class="brush">so you know where we stand.</span>','',rail([f'<div class="pc4 nt"><h3>{a}</h3><p>{b}</p></div>' for a,b in nots],4,'What we are not'))
    body+=numbers()
    body+=nxt('02','product-modes.html','Enough about us. <span class="pk">Watch the desk work.</span>','One fictional owner, Leo, four chapters: the catch on his ads, the Tokyo plan, the Friday count, the lesson.','Follow Leo\'s year')
    page('about-modes.html','About | You are just outnumbered | First Officer','Why First Officer exists, the rules we work by and the four pillars: Earn, Burn, Return, Learn.',body,'About')

# ---------------- industries ----------------
TR=[('agencies','Agencies','Client ad spend, software, contractors'),('auto-repair','Auto repair','Parts, tools, towing'),('cleaning','Cleaning','Supplies, laundry, vehicles'),('consulting','Consulting','Client travel, software, research'),
    ('contractors','Contractors','Materials, rentals, job-site hotels'),('cpa-firms','CPA firms','Software, research, filing fees'),('dental','Dental','Supplies, labs, patient ads'),('ecommerce','E-commerce','Ads, shipping, packaging'),
    ('fitness','Fitness','Equipment, software, ads'),('hvac','HVAC','Equipment, refrigerant, fuel'),('it-services','IT services','Hardware, licenses, cloud'),('landscaping','Landscaping','Plants, fuel, equipment'),
    ('law-firms','Law firms','Research, filing fees, travel'),('medical','Medical','Supplies, labs, software'),('property-management','Property management','Repairs, utilities, software'),('real-estate','Real estate','Listing ads, signage, travel'),
    ('restaurants','Restaurants','Food suppliers, delivery apps, utilities'),('salons','Salons','Product, booking software, ads'),('trucking','Trucking','Fuel, tires, tolls'),('veterinary','Veterinary','Pharmacy, labs, supplies')]
def industries():
    p=P[1]
    mix=''.join(f'<li><span>{esc(c[0])}</span><em>${c[1]:g}k/mo</em><b>{c[2]} → {c[3]}</b></li>' for c in p['cats'])
    vis=f'<div class="tmx"><div class="tmh"><span class="chk">Example mix · HVAC</span><b>{p["first"]}, {esc(p["biz"])}</b><small>{p["city"]} · about ${sum(c[1] for c in p["cats"]):.1f}k a month on cards</small></div><ul>{mix}</ul><div class="tmf"><span>Per $1, est.</span><b>{x(p["from"])} → {x(p["to"])}</b></div><small class="ill">Fictional owner. {ILL}</small></div>'
    h=hero('Industries · 20 trades','Same four pillars. <span class="pk">Your trade\'s own codes.</span>',
      dm('A roofer\'s money hides in job-site hotels. A dentist\'s in lab fees. A trucker\'s in fuel. The desk knows how each line codes, so it knows which card earns most on it.','Every trade hides money in a different line. The desk knows which.'),
      ['20 trades, each with its own page.','How each line of spend codes.','Example mixes, not your numbers.'],vis)
    cards=[f'<div class="trd"><span class="trn">{i+1:02d}</span><h3>{n}</h3><p>{d}</p><div class="trl"><a href="for-{s}.html">Read about the trade <span class="ar">→</span></a><a href="calculator-modes.html?m=adv">Run your numbers <span class="ar">→</span></a></div></div>' for i,(s,n,d) in enumerate(TR)]
    body=h+sec('01 · Pick your trade','Twenty trades. <span class="brush">Twenty kinds of found money.</span>',dm('Each trade has its own page, with the codes, the catches and an example owner.','Swipe to find yours.'),'<div class="trg">'+''.join(cards)+'</div>',id_='trades')
    body+=sec('02 · Same four pillars','Every trade, <span class="brush">one desk.</span>','',pillars())
    body+=sec('03 · Owners like you','Ten trades, <span class="brush">ten catches.</span>','',stories())
    body+=nxt('03','calculator-modes.html','You know your trade. <span class="pk">Now see your number.</span>','Pick your industry in the calculator for a typical mix, then type your own lines.','Run the calculator')
    page('industries-modes.html','Industries | Your trade, your codes | First Officer','Twenty trades, each with how its spend codes and an example owner. Illustrative estimates.',body)


# ---------------- connect, folded into trust (old connect.html redirects here with its ?t= token) ----------------
CNX_CSS='<style>.cnx .cw{display:grid;gap:8px;margin:14px 0 0;padding:0;list-style:none}.cnx .cw li{display:grid;grid-template-columns:92px 1fr;gap:10px;font-size:13px;padding:8px 10px;border-radius:10px;background:var(--cream)}.cnx .cw li span{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);padding-top:2px}.cnx .pc4 .btn{margin-top:14px;width:100%;justify-content:center}'\
 '#sees .ledger2{margin:22px 0 0;background:#fff;border-radius:22px;overflow:hidden;box-shadow:0 0 0 1px rgba(20,18,22,.08),0 18px 36px -24px rgba(20,18,22,.35)}#sees .lhead{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;padding:12px 18px;background:var(--cream);font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}#sees .lhead b{color:var(--ink)}'\
 '#sees .lrow2{display:grid;gap:10px;padding:16px 18px;border-top:1px solid rgba(20,18,22,.08)}#sees .lrow2 .card{font-weight:700;font-size:15px}#sees .lrow2 .card small{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-top:3px;font-weight:500}'\
 '#sees .lamps{display:flex;gap:6px;flex-wrap:wrap}#sees .lamp{display:inline-flex;align-items:center;gap:6px;font-family:var(--mono);font-size:11px;padding:5px 9px;border-radius:8px;background:var(--cream);color:var(--mute)}#sees .lamp::before{content:"";width:8px;height:8px;border-radius:2px;background:#C9C4D0}#sees .lamp.on{color:var(--ink);background:#fff;box-shadow:inset 0 0 0 1.5px #12834E}#sees .lamp.on::before{background:#12834E}'\
 '#sees .status{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;padding:4px 9px;border-radius:7px;justify-self:start;color:#fff;background:#12834E}#sees .status.a{background:#E8590C}#sees .status.g{background:#857E8C}#sees .act{font-size:13px;font-weight:700;color:var(--pinkd);text-decoration:none}#sees .act small{display:block;font-weight:500;color:var(--mute);font-size:12px}'\
 '#sees .lfoot{padding:14px 18px;font-size:13px;line-height:1.6;color:var(--body);background:var(--cream)}@media(min-width:900px){#sees .lrow2{grid-template-columns:1.1fr 2.6fr .8fr 1fr;align-items:center}#sees .act{justify-self:end;text-align:right}}</style>'
CNX_JS=r"""<script>(function(){var t=new URLSearchParams(location.search).get('t');var box=document.querySelector('#sees .ledger2');if(!box||!t)return;var head=box.querySelector('.lhead span:last-child');head.textContent='Loading';
if(location.hash!=='#connect'){var c=document.getElementById('connect');if(c)c.scrollIntoView();}
fetch('https://cuzuzzbezswvejnoskum.supabase.co/functions/v1/fo-connect-ledger?t='+encodeURIComponent(t)).then(function(r){return r.json()}).then(function(j){var rows=box.querySelectorAll('.lrow2'),i,foot=box.querySelector('.lfoot');
if(!j||j.error||!Array.isArray(j.cards)){head.textContent='Link expired';for(i=0;i<rows.length;i++)rows[i].remove();if(foot)foot.innerHTML='This link has expired. Reply CONNECT in your thread and a fresh one comes back in a minute.';return}
for(i=0;i<rows.length;i++)rows[i].remove();head.textContent=j.first_name?('Your account, '+j.first_name):'Your account';
var fmt=function(d){if(!d)return null;var x=new Date(d+'T00:00:00Z');return x.toLocaleDateString('en-US',{month:'short',day:'numeric',timeZone:'UTC'})};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
if(j.cards.length===0){var e=document.createElement('div');e.className='lrow2';e.innerHTML='<div class="card">No cards on file yet<small>Reply TELL in your thread to name them</small></div>';box.insertBefore(e,foot);return}
j.cards.forEach(function(c){var told=c.told_at?fmt(String(c.told_at).slice(0,10)):null,st=c.statements_through?fmt(c.statements_through):null,co=c.connected_through?fmt(c.connected_through):null;
var cls=c.freshness==='current'?'w':(c.freshness==='from your words'?'g':'a');var act=co?'Disconnect<small>from here or at your bank</small>':(st?"Send this month's statement<small>or connect this card</small>":'Send a statement<small>or connect this card</small>');
var el=document.createElement('div');el.className='lrow2';el.innerHTML='<div class="card">'+esc(c.card_name)+'</div><div class="lamps"><span class="lamp'+(told?' on':'')+'">Told'+(told?' &middot; '+esc(told):'')+'</span><span class="lamp'+(st?' on':'')+'">Statements'+(st?' &middot; to '+esc(st):'')+'</span><span class="lamp'+(co?' on':'')+'">Connected'+(co?' &middot; to '+esc(co):'')+'</span></div><span class="status '+cls+'">'+esc(c.freshness)+'</span><a class="act" href="https://wa.me/16199404040?text=STATEMENT">'+act+'</a>';box.insertBefore(el,foot)})}).catch(function(){head.textContent='Could not load'})})();</script>"""
def connect_sec():
    W=[('earn','In the thread','Tell us','Say it in WhatsApp: which cards the business uses, roughly what runs through each, and what is coming up. The desk works from your words and asks when something is missing.',[('Desk gets','Your cards and numbers, as you give them'),('Your part','About five minutes, then a question now and then'),('Current to','The day you told us')],('💬 Tell us in WhatsApp',WA,'wa')),
       ('burn','Once a month','Send statements','Export a statement file from each card\'s own site and drop it in the thread. The desk reads every line. Your login stays with you.',[('Desk gets','Every transaction on the statement'),('Your part','One export per card a month, about two minutes'),('Current to','The last statement date')],('Send a statement','https://wa.me/16199404040?text=STATEMENT','pk')),
       ('return','Once, then never again','Connect once','A read-only link to the card accounts you choose, made through your provider\'s own sign-in, so your login never touches us. Settled transactions arrive on their own.',[('Desk gets','Transactions and balances as they settle'),('Your part','About two minutes, once'),('Current to','A few days after a charge settles')],('Connect a card','https://wa.me/16199404040?text=CONNECT','pk'))]
    cards=[f'<div class="pc4 k-{k}"><div class="pn"><b>{a}</b></div><h3>{t}</h3><p>{d}</p><ul class="cw">'+''.join(f'<li><span>{x}</span>{y}</li>' for x,y in L)+f'</ul><a class="btn {c}" href="{u}">{b}</a></div>' for k,a,t,d,L,(b,u,c) in W]
    led=('<div id="sees"><div class="ledger2"><div class="lhead"><b>What the desk sees</b><span>Example account</span></div>'
         '<div class="lrow2"><div class="card">Card A<small>Office, internet, fuel</small></div><div class="lamps"><span class="lamp on">Told</span><span class="lamp on">Statements · last month</span><span class="lamp">Connected</span></div><span class="status a">A month behind</span><a class="act" href="https://wa.me/16199404040?text=STATEMENT">Send last month\'s statement<small>or connect this card</small></a></div>'
         '<div class="lrow2"><div class="card">Card B<small>Flights, hotels, software</small></div><div class="lamps"><span class="lamp on">Told</span><span class="lamp">Statements</span><span class="lamp on">Connected · current</span></div><span class="status">Current</span><a class="act" href="https://wa.me/16199404040?text=DISCONNECT">Disconnect<small>from here or at your bank</small></a></div>'
         '<div class="lrow2"><div class="card">Card C<small>Vendors, everything else</small></div><div class="lamps"><span class="lamp on">Told</span><span class="lamp">Statements</span><span class="lamp">Connected</span></div><span class="status g">From your words</span><a class="act" href="https://wa.me/16199404040?text=STATEMENT">Send a statement<small>or connect this card</small></a></div>'
         '<div class="lfoot">Open this from your thread and it shows your own cards. Reply DELETE STATEMENTS in your thread to remove statement rows. Revoke a connection at your bank and the feed stops. Example cards shown here are fictional.</div></div></div>')
    return CNX_CSS+sec('Connect · three ways in','Tell us, send us or connect us. <span class="brush">Mix as you like.</span>',
        dm('Three ways to give the desk your spend, all read-only, all leading to the same Friday report. Pick per card and switch whenever you want; the report says where each line came from.','Three read-only ways in. Pick per card, switch any time.'),
        '<div class="cnx">'+rail(cards,3,'Three ways in')+'</div>'+led,id_='connect')+CNX_JS

# ---------------- trust ----------------
def trust():
    vis='<div class="lvl">'+''.join(f'<div class="lv k-{k}"><span class="chk">Level {n}</span><b>{t}</b><p>{d}</p></div>' for k,n,t,d in [('earn',1,'Screenshots only','Only the numbers in an image you choose to send. Nothing is connected.'),('return',2,'Email connection','Travel, rewards and expense messages. Granted through your provider\'s own sign-in.'),('learn',3,'Card and spend connection','Transactions and balances, read-only, revocable from your bank at any time.')])+'</div>'
    h=hero('Trust · plain answers','What we see. <span class="pk">What we never touch.</span>',
      dm('First Officer reads your spending so it can find value you already earned. Connections are read-only: it cannot move money, open or close accounts, redeem points or buy anything.','Read-only connections. Nothing moves without your yes.'),
      ['Read-only, every connection.','Nothing moves without your yes.','We do not sell your data.'],vis,pk=('Book the call','book-modes.html'))
    C=[('Read-only','Every connection you grant is read-only. The desk can see transactions and balances. It cannot move money or make a purchase.'),
       ('Your own sign-in','You connect through your provider\'s own sign-in. We never ask you for a password in the thread. If anyone claiming to be First Officer does, it is not us.'),
       ('Your yes, first','Applications, transfers and bookings happen only after you say yes, in your own thread.'),
       ('Not for sale','Your information is not sold or rented to advertisers, data brokers or card issuers. We take no affiliate commissions.'),
       ('Yours to revoke','Revoke any connection from the provider\'s own settings, whenever you want, and ask us to delete your data.')]
    body=h+sec('The short version','Five commitments, <span class="brush">in one place.</span>','If you read nothing else on this page, read these.',rail([f'<div class="pc4"><div class="pn"><b>0{i+1}</b></div><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(C)],5,'Commitments'))
    G=[('Black box','An answer appears. No source, no reasoning, no caveats.'),('Glass box','An answer with the card rule it came from, the merchant code it depends on and the date it was checked.'),('You can audit us','Every claim is checkable, so you never have to take our word for a number.')]
    body+=sec('Every answer shows its work','A black box, <span class="brush">or a glass box.</span>','',rail([f'<div class="pc4 {"gb" if i==1 else ""}"><h3>{a}</h3><p>{b}</p></div>' for i,(a,b) in enumerate(G)],3,'Glass box'))
    body+=connect_sec()
    Q=[('Are you certified?','First Officer holds no security certification today. If that is a requirement for your business, tell us before you sign up.'),('Are you a financial advisor?','No. We are an advisory service for rewards and business spend, not a bank, lender, broker, or licensed financial, tax or legal advisor.'),('Can the desk move my money?','No. The desk cannot move money, open accounts or buy anything. It recommends; you approve; only then does it act.'),('Can the desk find award seats that do not exist?','No. Award space is set by each program. The desk looks for it and tells you plainly when it is not there.'),('Do you guarantee results?','No. Award space, transfer ratios and program rules change without notice. Every figure on this site is an estimate.')]
    body+=sec('What we do not claim','Straight answers <span class="brush">to the hard questions.</span>','<a href="privacy.html">Privacy Policy</a> · <a href="terms-of-service.html">Terms of Service</a>','<div class="txs">'+''.join(f'<details class="tx"><summary>{a}</summary><p>{b}</p></details>' for a,b in Q)+'</div>')
    body+=nxt('05','book-modes.html','Read-only, your yes first. <span class="pk">Ready to see your number?</span>','Twenty minutes, free, on WhatsApp, email or a call back.','Book the Found Money Call')
    page('trust-modes.html','Trust | What we see, what we never touch | First Officer','Read-only connections, your approval first, no affiliate money and what we do not claim.',body)

# ---------------- freebies ----------------
NUG=[('earn','Shipping and mail','4 nuggets','Labels, freight and storage. Three ways a box gets coded.',['Couriers code as 4215. Motor freight is 4214.','Storage you pay for codes as 4225, public warehousing.','Ask your card which of the three it treats as a bonus line.']),
     ('burn','Auto repair','3 nuggets','Towing, parts and the shop itself code apart.',['Towing you pay for is 7549, its own code, separate from repair.','Parts houses and repair shops code differently.','A card that rewards one may not reward the other.']),
     ('return','Cleaning','3 nuggets','Same jug of chemical, different codes.',['Your carpet sub is 7217, apart from janitorial.','Mops and rags out for laundry: 7211, commercial laundries.','Supply houses and big-box stores code differently.']),
     ('learn','Clinics','2 nuggets','Supplies and uniforms through every exam room.',['Scrubs are 5137, uniforms and commercial clothing.','Medical supply houses and pharmacies code apart.'])]
def freebies():
    vis='<div class="fst">'+''.join(f'<div class="fpk k-{k}"><span class="chk">Golden Nugget pack · {n}</span><b>{t}</b><p>{d}</p></div>' for k,t,n,d,_ in NUG[:3])+'</div>'
    h=hero('Freebies · free from the desk','Everything I\'d tell you <span class="pk">on a call. Free.</span>',
      dm('Read it, use it, keep it. Golden Nugget packs on how your spend codes, and a page for every trade. General education, not tax, legal or financial advice.','Read it, use it, keep it. General education, not advice.'),
      ['Golden Nugget packs, a minute each.','Twenty trade pages.','No sign-up to read.'],vis,calc=('calculator-modes.html','or start with the calculator'))
    packs=''.join(f'<details class="tx np k-{k}"><summary><span class="chk">Golden Nugget pack · {n}</span><b>{t}</b><small>{d}</small></summary><ul>'+''.join(f'<li><b>✓</b>{x_}</li>' for x_ in L)+'</ul></details>' for k,t,n,d,L in NUG)
    body=h+sec('Start here','Four packs, <span class="brush">a minute each.</span>',dm('Merchant codes decide what a purchase earns. These are the ones owners miss most. Codes can vary by merchant and card.','Tap a pack to open it. Codes can vary by merchant and card.'),'<div class="txs n2">'+packs+'</div>')
    body+=sec('By trade','Your trade\'s <span class="brush">own page.</span>','','<div class="trg sm">'+''.join(f'<a class="trd" href="for-{s}.html"><h3>{n}</h3><p>{d}</p><span class="mcalc">Read it <span class="ar">→</span></span></a>' for s,n,d in TR)+'</div>')
    body+=nxt('01','home-modes.html','Rather have it done for you? <span class="pk">That\'s what the desk is for.</span>','Start where every owner starts: you are not bad at Points &amp; Miles, you are just outnumbered.','Start the story')
    page('freebies-modes.html','Freebies | Free from the desk | First Officer','Golden Nugget packs on how spend codes, and a page for every trade. General education, not advice.',body,'Freebies')

if __name__=='__main__':
    product();book();about();industries();trust();freebies()
