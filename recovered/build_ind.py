# Step 3 of the rebuild: one -modes industry template, regenerated for all 20 for-*.html. Mockup only.
# Every owner is fictional, every figure is illustrative, est. Run: python3 recovered/build_ind.py
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import build as B
import build_pages as BP
import build_more as M
from build_pages import P,TR,ILL,WA,esc,x,usd,pts,dm,hero,sec,rail,nxt,deskcta,stories,fbrows,fbcard,codes_for,nug_for
WACODE={'property-management':'property-mgmt'}  # same per-trade WhatsApp codes as main's for-* pages
CPP=0.016  # est. value of a card point, same 1.6 cents the product page uses
CAP=150000 # yearly cap on a bonus pool, est.
# slug -> calculator ?ind slug and persona index (only the 10 calculator industries have both)
MAP={'hvac':('hvac',1),'dental':('dental-practice',2),'agencies':('marketing-agency',3),'law-firms':('law-firm',4),'restaurants':('restaurant',5),
     'trucking':('trucking',6),'real-estate':('real-estate',7),'ecommerce':('e-commerce',8),'contractors':('contractor',9)}
# Typical lines per trade: (line, $k a month, routed rate). The rate is what the line can earn on a card that rewards it, est.
LINES={
 'agencies':[('Client advertising',145,4),('Software and tools',9.5,4),('Travel and client meetings',6.5,3),('Utilities and insurance',3,2)],
 'auto-repair':[('Parts distributors',44,2),('Paint and consumables',12,2),('Tools and shop equipment',9,2),('Towing and sublet labor',7,2)],
 'cleaning':[('Janitorial and chemical supply',24,2),('Crew fuel and vehicles',11,4),('Equipment and machine leases',9,2),('Insurance and bonding',5.5,1)],
 'consulting':[('Travel booked for clients',22,3),('Software and research',7.5,4),('Conferences and business development',6,2),('Utilities and insurance',2.5,2)],
 'contractors':[('Materials and supply houses',96,2),('Equipment rental and purchase',14,2),('Fleet fuel',12,4),('Insurance and bonding',9,1)],
 'cpa-firms':[('Tax and research software',12,4),('Filing and per-return fees',7,1),('Insurance, dues and licensing',6,1),('Phones and office',5,2)],
 'dental':[('Dental supply distributors',34,2),('Lab fees',13,2),('Implants and ortho materials',11,2),('Practice software and imaging',4.5,4)],
 'ecommerce':[('Inventory and manufacturing',95,2),('Advertising',78,4),('Shipping and fulfillment',34,3),('Software and platform fees',6.5,4)],
 'fitness':[('Equipment leases and service',16,2),('Marketing and promotions',8.5,4),('Cleaning and facility supply',7.5,2),('Software and music licensing',3.2,4)],
 'hvac':[('Equipment and parts distributors',62,2),('Refrigerant and consumables',14,2),('Fleet fuel',13,4),('Vehicle leases and upkeep',11,2)],
 'it-services':[('Cloud and hosting',48,4),('Hardware for client rollouts',42,4),('Software licensing',36,4),('Monitoring and tooling',9.5,4)],
 'landscaping':[('Nursery stock and materials',38,2),('Fuel for trucks and equipment',14,4),('Equipment purchase and repair',12,2),('Dump and disposal fees',5.5,2)],
 'law-firms':[('Legal research subscriptions',9.5,4),('Court, filing and service fees',8,1),('Malpractice, dues and insurance',7.5,1),('Phones and office',6,2)],
 'medical':[('Medical and surgical supply',38,2),('Lab and diagnostics',12,2),('Malpractice and insurance',9,1),('Practice software',4.5,4)],
 'property-management':[('Repairs and turnovers',72,2),('Utilities on the portfolio',44,2),('Insurance',20,1),('Management software',4.5,4)],
 'real-estate':[('Listing marketing and photos',18,4),('Staging and prep',12,2),('Client travel',7,3),('CRM and software',3.5,4)],
 'restaurants':[('Food distributors',46,2),('Produce, meat and specialty',14,2),('Delivery app advertising',2,4),('Software and subscriptions',1.5,4)],
 'salons':[('Professional product',18,2),('Retail stock for resale',9,2),('Marketing and social',4.5,4),('Booking software',1.8,4)],
 'trucking':[('Diesel across fuel networks',185,4),('Maintenance, tires and parts',42,2),('Insurance and permits',26,1),('Tolls and scale fees',14,4)],
 'veterinary':[('Veterinary distributors',32,2),('Pharmacy and vaccine stock',14,2),('Lab and diagnostics',11,2),('Imaging and software',5.5,4)]}
OFF={'agencies':'contractors, freelancers and studio rent','auto-repair':'bay rent and payroll','cleaning':'crew payroll','consulting':'subcontractors and office rent',
 'contractors':'subcontractors and payroll','cpa-firms':'seasonal staff and rent','dental':'rent and staff costs','ecommerce':'warehouse rent and payroll','fitness':'rent and payroll',
 'hvac':'payroll','it-services':'rent and payroll','landscaping':'crew payroll','law-firms':'expert fees and rent','medical':'rent and staff costs',
 'property-management':'big bills and vendors that do not take cards','real-estate':'desk fees and payroll','restaurants':'rent, payroll and delivery commissions',
 'salons':'booth rent and payroll','trucking':'factoring and driver payroll','veterinary':'rent and staff costs'}
# Fictional owners for the 11 trades the calculator has no example for: first, biz, city, trip, when, dest image, % there
OWN={'auto-repair':('Marco','Ridgeline Auto Service','Boise, ID','Yellowstone in a cabin for 4','Next summer',5,38),
 'cleaning':('Rosa','BrightPath Cleaning','Tampa, FL','Cancún for two','This winter',9,44),
 'consulting':('Priya','Northgate Advisory','Denver, CO','Lisbon for two','Next spring',14,52),
 'cpa-firms':('Martin','Fairlane CPA Group','Omaha, NE','Hawaii after tax season','Next May',2,35),
 'fitness':('Jordan','Ironline Fitness','Austin, TX','Costa Rica for two','Next fall',11,29),
 'it-services':('Samir','Bluepeak IT','Raleigh, NC','Iceland for a family of 4','Next summer',17,46),
 'landscaping':('Gus','Greenway Landscapes','Charlotte, NC','Orlando for a family of 5','This winter',7,40),
 'medical':('Elena','Lakeside Family Clinic','Madison, WI','Paris for two','Next spring',3,33),
 'property-management':('Nadia','Harborview Property Co.','San Diego, CA','Rome for two','Next fall',13,48),
 'salons':('Camille','Studio Camille','Nashville, TN','Mexico City for two','This spring',19,37),
 'veterinary':('Owen','Cedar Hill Animal Clinic','Lexington, KY','Banff for a family of 4','Next summer',15,31)}
H1={'agencies':'Client ad spend. Software. Travel. <span class="pk">Almost all of it can earn more.</span>',
 'auto-repair':'Parts runs. Shop supplies. <span class="pk">On the right card?</span>',
 'cleaning':'Supply runs and crew fuel. <span class="pk">Earning what they should?</span>',
 'consulting':'Client travel and software. <span class="pk">Worth more on the right card.</span>',
 'contractors':'Material runs and fleet fuel. <span class="pk">Earning half what they could?</span>',
 'cpa-firms':'Tax software. Filing fees. <span class="pk">Most of it underearning.</span>',
 'dental':'Supply bills. Lab fees. <span class="pk">Earning the minimum?</span>',
 'ecommerce':'Every ad, every package. <span class="pk">On the right card?</span>',
 'fitness':'Equipment. Software. Marketing. <span class="pk">Your gym can earn more.</span>',
 'hvac':'Parts orders. Fleet fuel. Equipment. <span class="pk">Earning 1x?</span>',
 'it-services':'Cloud, licenses, hardware. <span class="pk">Some of your best-earning spend.</span>',
 'landscaping':'Nursery stock. Diesel. Equipment. <span class="pk">Earning the minimum?</span>',
 'law-firms':'Research. Filing fees. Travel. <span class="pk">None of it routed?</span>',
 'medical':'Supply invoices. Lab fees. <span class="pk">Your biggest spend, earning least.</span>',
 'property-management':'Every repair, every turnover. <span class="pk">On the right card?</span>',
 'real-estate':'Listing ads, staging, travel. <span class="pk">Worth more on the right card.</span>',
 'restaurants':'Food distributor orders. <span class="pk">Earning zero bonus?</span>',
 'salons':'Product orders. Booking software. <span class="pk">Earning the minimum?</span>',
 'trucking':'Diesel is your biggest line. <span class="pk">Is it earning the most?</span>',
 'veterinary':'Distributor orders. Labs. Imaging. <span class="pk">Earning the minimum?</span>'}
def k1(v): return ('$%gk'%v)
def rnd(n,s=10): return int(round(n/s)*s)

def owner(slug):
    """One fictional example owner per trade: a calculator persona where one exists, else a page-only owner built from the trade's lines."""
    if slug in MAP:
        p=P[MAP[slug][1]];c=max(p['cats'],key=lambda c:(float(c[3][:-1])-float(c[2][:-1]))*c[1])
        return dict(first=p['first'],biz=p['biz'],city=p['city'],trip=p['trip'],when=p['when'],img=p['img'],pct=p['pct'],
            mix=[(a,b,f,t) for a,b,f,t in p['cats']],catch=c[0],cfrom=c[2],cto=c[3],gain=p['move'][1],
            frm=p['from'],to=p['to'],spend=sum(c[1] for c in p['cats']),ex=p['first'].lower(),ind=MAP[slug][0])
    f,b,ci,tr,wh,im,pc=OWN[slug];L=LINES[slug]
    mix=[(a,k,'1x','%dx'%r) for a,k,r in L[:3]]
    bon=max(L,key=lambda l:(l[2]-1)*min(l[1]*12000,CAP))
    gain=rnd((bon[2]-1)*min(bon[1]*12000,CAP)*CPP)
    tot=sum(k for _,k,_ in L);frm=1.0;to=sum(k*r for _,k,r in L)/tot
    return dict(first=f,biz=b,city=ci,trip=tr,when=wh,img='img/hero/dest/%02d.jpg'%im,pct=pc,mix=mix,catch=bon[0],cfrom='1x',cto='%dx'%bon[2],
            gain=gain,frm=frm,to=round(to,1),spend=tot,ex=None,ind=None)

def phone(o,name):
    hd=B.hd()
    found=f'''<div class="cs on" data-confetti="1">{hd}
<div class="bd">✓ Found · {esc(name)}</div><div class="lb">{esc(o["catch"])}, {o["cfrom"]} → {o["cto"]}</div>
<div class="bg" data-to="{o["gain"]}" data-pre="+$">+{usd(o["gain"])}</div><div class="sub">a year, if {esc(o["first"])} says yes <em>est.</em></div>
<p class="p">{esc(o["catch"])} was on a card that earns {o["cfrom"]}. The desk lines it up with a {o["cto"]} card and shows the move in dollars first.</p>
<div class="mini"><div><small>On cards</small><b>{k1(o["spend"])}/mo</b></div><div><small>Per $1 today</small><b>{x(o["frm"])}</b></div><div><small>Per $1, routed</small><b>{x(o["to"])}</b></div></div>
<div class="by"><i>✓</i>Checked by the desk against the statement</div>
{B.nm("a",esc(o["catch"])+" to the "+o["cto"]+" card","Waiting for "+esc(o["first"])+"'s OK","+"+usd(o["gain"])+" <em>est.</em>","Approve")}
<div class="cta">See it on my ledger</div><div class="home"></div></div>'''
    goal=f'''<div class="cs" data-confetti="1">{hd}
<div class="bd pkb">Goal · {esc(o["trip"].split(" for ")[0].split(" in ")[0].split(" after ")[0])}</div><div class="lb">Points toward the trip</div>
<div class="bg pk" data-to="{o["pct"]}" data-suf="%">{o["pct"]}%</div><div class="sub">of the way there <em>est.</em></div>
<div class="goal"><div class="im" style="background-image:url({o["img"]})"></div><div class="gb"><b>{esc(o["trip"])}</b><small>{esc(o["when"])}, est.</small><div class="tr"><i style="width:{o["pct"]}%"></i></div><div class="ax"><span>Today</span><span>{o["pct"]}% there</span><span>{esc(o["when"])}</span></div></div></div>
<p class="p">The desk vets every requirement with {esc(o["first"])} and books only after {esc(o["first"])} approves.</p>
{B.nm("g","Pick the dates",esc(o["when"])+" window","%d%% to go"%(100-o["pct"]),"Pick dates")}
<div class="cta gd">See my plan</div><div class="home"></div></div>'''
    return '<div class="celcol phstar">'+B.celphone(found+goal)+'<div class="celnav"><button>Found money</button><button>Trip goal</button></div><small class="ill">Example app screens. '+esc(o["first"])+' is fictional. '+ILL+'</small></div>'

def page(slug,name,desc):
    o=owner(slug);L=LINES[slug];lname=name.lower() if name not in('HVAC','IT services') else name
    calc='calculator-modes.html'+('?ind='+o['ind'] if o['ind'] else '')
    big=max(L,key=lambda l:l[1]);bon=max(L,key=lambda l:(l[2]-1)*min(l[1]*12000,CAP))
    h=hero('First Officer for '+name,H1[slug],
        dm(f'{esc(o["first"])} runs {esc(o["biz"])} in {o["city"]}, a fictional {lname} business. Here is where {lname} spend hides money, and what the desk does about it, one pillar at a time.',
           f'Where {lname} spend hides money, and what the desk does about it.'),
        [f'How {lname} spend codes, line by line.','Every move waits for your yes.','One number in dollars, every Friday.'],phone(o,name),
        calc=(calc,'or run '+('the '+name+' example' if o['ind'] else 'your numbers')+' in the calculator'))
    mix=''.join(f'<li><span>{esc(a)}</span><em>{k1(b)}/mo</em><b>{f} → {t}</b></li>' for a,b,f,t in o['mix'])
    tmx=f'<div class="tmx"><div class="tmh"><span class="chk">Example mix · {esc(name)}</span><b>{esc(o["first"])}, {esc(o["biz"])}</b><small>{o["city"]} · about {k1(o["spend"])} a month on cards</small></div><ul>{mix}</ul><div class="tmf"><span>Per $1, est.</span><b>{x(o["frm"])} → {x(o["to"])}</b></div><small class="ill">Fictional owner. {ILL}</small></div>'
    codes=''.join(f'<li><span>{esc(a)}</span><b class="r{r}">up to {r}x</b></li>' if r>1 else f'<li><span>{esc(a)}</span><b class="r1">often 1x</b></li>' for a,k,r in L)
    side=f'<div class="ixc"><span class="chk">How {esc(lname)} lines code</span><ul class="ixl">{codes}</ul><p class="ixn">Rates a line can earn on a card that rewards it, inside yearly caps. Est. Your own codes decide.</p><div class="ixb"><a class="btn pk" href="{calc}">Run {"the "+esc(o["first"])+" example" if o["ind"] else "your numbers"} <span class="ar">→</span></a><a class="btn gh" href="industries-modes.html#trades">All 20 trades</a></div></div>'
    body=h+sec('01 · The example',f'Meet {esc(o["first"])}. <span class="brush">One catch, in dollars.</span>',
        dm(f'{esc(o["catch"])} was earning {o["cfrom"]}. On a {o["cto"]} card it is worth about {usd(o["gain"])} a year, est. The desk shows the move first and waits for a yes.',f'{esc(o["catch"])}: {o["cfrom"]} → {o["cto"]}, about {usd(o["gain"])} a year, est.'),
        '<div class="ix2">'+tmx+side+'</div>',id_='example')
    W=[('earn','Earn',f'{esc(bon[0])} belongs on a bonus card.',f'It can earn up to {bon[2]}x on a card that rewards it, inside a yearly cap. The desk tracks the cap and moves the next dollar before it fills.'),
       ('burn','Burn',f'Points into {esc(o["trip"].lower() if o["trip"].split()[0] not in ("Yellowstone","Cancún","Cancun","Lisbon","Hawaii","Costa","Iceland","Orlando","Paris","Rome","Mexico","Banff","Maui","Tokyo") else o["trip"])}.','The desk maps the programs, checks taxes and fees, and gives the trip a pace. It books only after you approve.'),
       ('return','Return',f'{esc(OFF[slug][0].upper()+OFF[slug][1:])} stay off the card.','A bill-pay fee often costs more than the points are worth. The desk decides line by line, and Friday counts what was found, in dollars.'),
       ('learn','Learn',f'How {esc(big[0].lower())} codes.','One short lesson a week from your own data: why the same purchase can code differently at two vendors, and what it means for you.')]
    body+=sec('02 · Where the money hides',f'Four places {esc(lname)} <span class="brush">money leaks.</span>',dm('Same four pillars as every desk, read through your trade\'s own codes.','Swipe: four places, one desk.'),
        rail([f'<div class="pc4 k-{k}"><div class="pn"><b>0{i+1}</b>{t}</div><h3>{a}</h3><p>{b}</p></div>' for i,(k,t,a,b) in enumerate(W)],4,'Where the money hides'),id_='leaks')
    S=[('earn','Today','The Found Money Call','Free, about 20 minutes, six plain questions. Your number from your real statements.'),
       ('burn','Within 24 hours','Your strategy','Which card for which line, written for your vendors.'),
       ('return','Week 1','Your first moves','Three moves, with the exact taps. Each waits for your yes.'),
       ('learn','Every Friday','Your scorecard','One number in dollars, next to a flat 2% card, after the $550 fee.')]
    cs,rows=codes_for(slug);ng=nug_for(slug);own=cs['id']=='codes-'+slug
    sheet=(f'<div class="ixc csh"><span class="chk">{"Code sheet · "+esc(name) if own else "Code sheet · every business"}</span><b class="csb">{cs["title"]}</b>{fbrows(rows)}'
           f'<p class="ixn">Codes are set by each merchant\'s processor and can vary. General information, not tax, legal or financial advice.</p></div>')
    right=(fbcard(ng,cid=False) if ng else '')+f'<p class="csm"><a href="freebies-modes.html?t={slug}#library">Every code sheet and nugget pack <span class="ar">→</span></a></p>'
    body+=sec('03 · The code sheet',f'The codes {esc(lname)} spend <span class="brush">runs under.</span>',
        dm('Your card pays its bonus on the code a store runs under, not on what you bought. These are the ones a '+esc(lname)+' statement shows most.','The code decides the bonus, not the item.'),
        '<div class="ix2 csx">'+sheet+'<div class="csr">'+right+'</div></div>',id_='codes')
    body+=sec('04 · How it starts','Four steps. <span class="brush">No spreadsheets.</span>','',BP.pillars_like(S))
    body+=sec('05 · Owners like you','Ten trades, <span class="brush">ten catches.</span>',dm('Every trade hides money in a different place. Swipe through ten fictional owners.','Swipe: ten owners, ten catches.'),stories(),id_='stories')
    body+=deskcta(f'$550 a month, flat. The Found Money Call is free and tells you first if {lname} spend like yours clears the fee.')
    body+=nxt('03',calc,f'{esc(o["first"])}\'s numbers are fiction. <span class="pk">Yours aren\'t.</span>',f'Open the calculator{" on the "+esc(name)+" example" if o["ind"] else ""}, then type your own lines. Fits, close call or not a fit, against $550 a month.','Run your numbers')
    fn='for-%s.html'%slug;title=f'First Officer for {name} | Where {lname} spend hides money'
    svc={"@context":"https://schema.org","@type":"Service","name":title.split(' | ')[0],"serviceType":"Business rewards desk for "+lname,
         "description":desc,"url":M.SITE+fn,"areaServed":{"@type":"Country","name":"United States"},"provider":M.ORG}
    M.render(fn,title,desc,body,canon=fn,bcls='pgi',robots=None,ga=True,wa_tag='site-%s-1'%WACODE.get(slug,slug),
        meta=M.seo(title,desc,fn,'og-for-%s.png'%slug,[svc,M.crumbs(name,fn)]))

if __name__=='__main__':
    for s,n,d in TR: page(s,n,f'Where {n.lower() if n not in ("HVAC","IT services") else n} spend hides money: {d.lower()}. A fictional example owner, illustrative estimates.')
