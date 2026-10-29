# Steps 4 and 5 (Learn): field-notes.html as the -modes Learn chapter, the 7 topic lessons and education.html. Mockup only.
# No tax content, no application or offer timing, no program names, every figure est.  Run: python3 recovered/build_learn.py
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import build_pages as BP
import build_more as M
from build_pages import ILL,dm,hero,sec,rail,nxt,deskcta
N=[
 dict(s='value',t='What a point is worth',h='A point is not a point. <span class="pk">Not even close.</span>',
  l='The same 50,000 points can be worth a few hundred dollars or a few thousand, est. The balance tells you nothing until you know how it will be spent.',
  st=('0.6¢ to 3¢+','what one point can be worth, est.'),
  p=[('The value ladder is hidden','Programs show the simple options first: statement credit, gift cards. The richer ones, transfers to airline and hotel partners, sit behind menus and partner lists.'),
     ('Cents per point is abstract','“1.6 cents a point” means little. “The ad spend paid for a hotel night” means a lot. It is the same math, est., so the desk always says it in dollars.'),
     ('Prices move by the day','Many programs price awards by demand. The same seat can cost very different points on different days, so a fixed rule of thumb breaks.'),
     ('The best value takes the most knowledge','The richest redemptions depend on three things at once: the transfer ratio, the award space and the timing. Nobody learns that by accident.')],
  d=('Every balance, in dollars','The desk values each balance in dollars, est., against the trips you actually want, and says plainly when the value is not there.'),
  q=['Do you know what one of your points is worth, in cents?','Have you ever moved points to a travel partner?','Is your balance tied to a trip, or just sitting?']),
 dict(s='cashback',t='The floor most people settle for',h='2% cash back feels like winning. <span class="pk">It is the floor.</span>',
  l='Cash back is simple and safe, and often the least valuable use of a point you already earned, est.',
  st=('$1,200','a year at 2% on $60K of spend, est.'),
  p=[('A statement credit is the floor','50,000 points as a statement credit come to about $500. Moved to a travel partner for a trip you wanted anyway, they can be worth more, est.'),
     ('Simple is a design choice','Cash back keeps the transfer partners out of sight. If you never learn that points can move to airline and hotel programs, you keep taking the floor.'),
     ('The gap adds up','A business spending $60,000 a year at 2% gets about $1,200. Routed and redeemed with a plan, the same spend can be worth more in travel, est. Sometimes it is not, and the desk says so.'),
     ('Cash back still has a place','If you will never travel or your spend is small, a flat 2% card is a fine answer. That is why the desk compares against it every month.')],
  d=('Measured against flat 2%, every month','The Friday scorecard puts your month next to a flat 2% card, after the $550 fee, so you can see whether the desk is earning its keep.'),
  q=['What did your last redemption come to, in cents per point?','Do you redeem as statement credit by default?','Would a trip you already plan to take use those points better?']),
 dict(s='complexity',t='Why it is this hard',h='The rules are complex. <span class="pk">That is not an accident.</span>',
  l='Every layer of complexity moves a little value from your account to the program’s.',
  st=('1:1 · 3:1','two common transfer ratios, est.'),
  p=[('Charts gave way to moving prices','Award charts once told you what a seat cost. Many programs now price by demand, with no published chart to plan against.'),
     ('Bonus categories depend on codes','A bonus applies only when the merchant’s category code matches. A grocery pickup or a warehouse club may not code as a grocery store, and few people are told.'),
     ('Transfer ratios are not standard','Many bank points move 1:1 to airline partners. Some move at less, and some hotel points move at about 3:1. Each ratio can change.'),
     ('Terms change with little notice','Programs can change terms, earning rates and partners. What you learned last year may not hold this year.')],
  d=('The desk keeps up, so you don’t have to','Every answer shows the rule it came from, the code it depends on and the date it was checked.'),
  q=['Do you know how your three biggest vendors code?','Do your points transfer 1:1 to the partner you would use?','When did you last check your card’s terms?']),
 dict(s='timing',t='When it has to happen',h='The right answer at the wrong time <span class="pk">is the wrong answer.</span>',
  l='Transfer bonuses, award releases and credit resets all run on clocks nobody publishes in one place.',
  st=('+30%','a transfer bonus in the right week, est.'),
  p=[('Transfer bonuses come and go','Programs sometimes add 20% to 40% bonus points on a transfer to one partner, often for a week or two. 100,000 points in a 30% bonus become 130,000 miles. A day late, they stay 100,000.'),
     ('Award seats open on schedules','Many airlines release award seats about 11 months ahead, and the best cabins go first.'),
     ('Credits reset on different calendars','Calendar year, card year, quarterly, monthly. One card can carry four reset dates.')],
  d=('The desk watches the clocks','It flags a window when it matters, with the math attached, and waits for your yes before anything moves.'),
  q=['Do you know when your card credits reset?','Would you know if a transfer bonus opened this week?','How far ahead do you plan the trip you care about most?']),
 dict(s='expiration',t='What quietly disappears',h='Your rewards have a shelf life <span class="pk">nobody tells you about.</span>',
  l='Points expire, credits reset and certificates lapse. None of it announces itself, and most of it is preventable.',
  st=('18–24 mo','common inactivity windows, est.'),
  p=[('Miles expire on different clocks','Some programs expire miles after 18 months without activity, some after 24 and some never. Each one is a trap if nobody is watching.'),
     ('Credits reset on staggered dates','One premium card can carry an airline credit, a hotel credit, a monthly ride credit and a twice-yearly retail credit, each on its own schedule.'),
     ('Free night certificates lapse','A hotel card’s free night is usually valid for about 12 months. It does not roll over, and you paid for it in the annual fee.'),
     ('A small purchase can save a balance','In many programs one small earning purchase resets the inactivity clock. A balance worth hundreds of dollars, est., can be saved in a minute.')],
  d=('Every clock on one list','The desk tracks each expiry and reset across your programs and flags it while there is still time to act.'),
  q=['Which of your balances has been idle the longest?','Do you have a free night certificate right now?','Which credits on your cards reset this month?']),
 dict(s='loyalty',t='Who the programs serve',h='Loyalty programs are not loyal <span class="pk">to you.</span>',
  l='You are asked to be loyal to a program that can change its terms whenever it likes.',
  st=('1x · 3x · 4x','the same swipe, coded three ways'),
  p=[('You earn blind','Thirty swipes a month, and few owners know whether each one earned 1x, 3x or 4x. The same pump can code as fuel or as a convenience store.'),
     ('You redeem blind','A hotel night for 40,000 points can be a great or a poor use of them, depending on the date. The program does not say which.'),
     ('Prices go up','Programs revalue awards. A trip that costs 60,000 miles this year can cost more next year.')],
  d=('Someone on your side of the table','The desk takes no affiliate commissions, so the only number it works for is yours.'),
  q=['Do you know what your last swipe earned?','Did your favorite program change its prices this year?','Who told you which card to get, and were they paid for it?']),
 dict(s='affiliates',t='Who the advice serves',h='When the advice is paid for, <span class="pk">who is it for?</span>',
  l='The facts in most card content are accurate. The order they appear in is often paid for.',
  st=('$0','affiliate money First Officer takes'),
  p=[('Rankings can follow referral fees','Many card sites earn a fee when you sign up through them. Cards that pay more tend to get more space and a higher spot.'),
     ('Comparison tables can be placements','A card that pays no referral fee may not appear in the table at all.'),
     ('Right facts, bought framing','You get correct information, arranged toward the conclusion that pays the publisher most.')],
  d=('No affiliate money here','First Officer takes no affiliate commissions from any issuer, and the Freebies link to nothing that pays us.'),
  q=['Did the site that ranked your card disclose what it was paid?','Was your card the best fit, or the best-paying link?','Who checks the advice against your own spend?']),
 dict(s='proactive',t='What actually works',h='A dashboard waits for you. <span class="pk">A desk reaches out.</span>',
  l='Information you have to remember to go and look at is information you will not use.',
  st=('30 days','the heads-up before an expiry, example'),
  p=[('Dashboards go unchecked','Most tracking apps get opened a lot in week one and rarely after. An expiring balance does not wait for you to log in.'),
     ('Data without context is noise','“85,000 points.” Is it a lot? Enough for the trip? About to expire? A number alone answers none of it.'),
     ('Reactive is too late','The useful message arrives before the deadline: these miles expire in 30 days, here is the fix, about five minutes.'),
     ('The channel matters','The desk writes where you already read: WhatsApp, email or a call back. One thread, not one more app.')],
  d=('Messages before deadlines','The desk raises a window when it matters, not when you happen to log in, and every move waits for your yes.'),
  q=['When did you last open your points app?','Would you see an expiry notice in time?','Where do you actually read messages: text, email or calls?'])]
for i,n in enumerate(N): n['n']='%02d'%(i+1)
LESSON={n['s'] for n in N if n['s']!='affiliates'}  # affiliates.html stays a do-not-touch redirect to field-notes.html#affiliates
def href(n): return n['s']+'.html' if n['s'] in LESSON else 'field-notes.html#'+n['s']
def lcard(n,big=False):
    return f'<div class="lsn{" big" if big else ""}"><span class="chk">Field note {n["n"]} · {n["t"]}</span><b>{n["st"][0]}</b><small>{n["st"][1]}</small><div class="lsf"><span>2 min read</span><span>Learn</span></div></div>'
def card(i,a,b): return f'<div class="pc4 k-learn"><div class="pn"><b>{i:02d}</b>Learn</div><h3>{a}</h3><p>{b}</p></div>'
def desk(n): return f'<div class="lsd"><div class="pc4 k-learn dsk"><div class="pn"><b>✓</b>What the desk does</div><h3>{n["d"][0]}</h3><p>{n["d"][1]}</p></div><div class="lsq"><span class="chk">Ask your own statements</span><ol>'+''.join(f'<li>{q}</li>' for q in n['q'])+'</ol></div></div>'

def field_notes():
    idx='<div class="fnx">'+''.join(f'<a class="fni" href="#{n["s"]}"><b>{n["n"]}</b><span>{n["t"]}</span></a>' for n in N)+'</div>'
    h=hero('Learn · Field Notes','How the rewards game <span class="pk">actually works.</span>',
      dm('Eight short notes from the desk: what a point is worth, why the easy option is often the weakest, and who the advice you have been reading is written for. No affiliate links, because we take no affiliate money.','Eight short notes on how points really work. No affiliate links.'),
      ['Eight notes, two minutes each.','Plain words, no program jargon.','Every figure an estimate.'],lcard(N[0],True),pk=('Get your desk','book-modes.html'),calc=('education.html','or see how Learn works on your desk'))
    body=h+sec('The index','Eight notes. <span class="brush">Start anywhere.</span>','',idx,id_='index')
    for n in N:
        more=f'<p class="fnm"><a href="{href(n)}">Read the two-minute lesson <span class="ar">→</span></a> · <a href="#index">Back to the index</a></p>' if n['s'] in LESSON else '<p class="fnm"><a href="#index">Back to the index</a></p>'
        body+=sec(f'Field note {n["n"]} · {n["t"]}',n['h'],n['l'],rail([card(i+1,a,b) for i,(a,b) in enumerate(n['p'][:3])],3,n['t'])+more,id_=n['s'],cls='fn')
    body+='<section class="sec tight"><div class="wrap"><p class="ill">'+ILL+' Point values depend on how and when you redeem. Not tax, legal or financial advice.</p></div></section>\n'
    body+=nxt('03','calculator-modes.html','Notes are general. <span class="pk">Your numbers aren\'t.</span>','Move one slider and see what your own spend is worth against $550 a month.','Run your numbers')
    M.render('field-notes.html','Field Notes | How the rewards game actually works | First Officer','Eight short notes on what a point is worth, cash back, timing, expiry and who card advice serves. Illustrative estimates.',body,on='',canon='field-notes.html',bcls='pgl')

def lesson(i):
    n=N[i];nx=N[i+1] if i+1<len(N) else None
    h=hero(f'Learn · Field note {n["n"]}',n['h'],n['l'],['A two-minute read.','Plain words, no program jargon.','What the desk does about it.'],lcard(n,True),calc=('field-notes.html','or browse all eight field notes'))
    body=h+sec(f'Field note {n["n"]} · {n["t"]}','The note, <span class="brush">in '+('four' if len(n['p'])==4 else 'three')+' points.</span>','',rail([card(j+1,a,b) for j,(a,b) in enumerate(n['p'])],len(n['p']),n['t']))
    body+=sec('What the desk does','Know it. <span class="brush">Then hand it off.</span>','',desk(n))
    body+=deskcta('Learn is the fourth pillar of every desk: one short lesson a week, built from your own data. $550 a month, flat.')
    if nx: body+=nxt('Field note '+nx['n'],href(nx),nx['h'],nx['l'],'Read the next note')
    else: body+=nxt('03','calculator-modes.html','You know the game. <span class="pk">Now see your number.</span>','Move one slider and see what your spend is worth against $550 a month.','Run your numbers')
    M.render(n['s']+'.html',f'{n["t"]} | Field note {n["n"]} | First Officer',n['l'].replace('<span class="pk">','').replace('</span>',''),body,canon=n['s']+'.html',bcls='pgl')

def education():
    vis='<div class="bfa lsv"><div><small>A card point</small><b>1.6¢</b><span>est.</span></div><i>·</i><div class="a"><small>This week</small><b>2 min</b><span>lesson</span></div></div><small class="ill">Example lesson card. '+ILL+'</small>'
    h=hero('Learn · the fourth pillar','Two minutes a week. <span class="pk">From your own data.</span>',
      dm('Earn, Burn and Return are what the desk does for you. Learn is what you keep: one short lesson a week on what your points are worth and what changed in your programs.','What your points are worth, and what changed, two minutes a week.'),
      ['One lesson a week, two minutes.','Built from your own programs.','Plain words, every figure est.'],vis,calc=('field-notes.html','or read the field notes'))
    L=[('This week','What a point is worth','Your points, valued in dollars against the trip you want, est.'),('When it changes','What moved in your programs','A partner added, a price raised, a credit about to reset.'),('Every month','Your month in one lesson','What the desk caught, and the one habit that made it possible.')]
    body=h+sec('What a lesson looks like','Short, plain, <span class="brush">and yours.</span>','',rail([f'<div class="pc4 k-learn"><div class="pn"><b>{a}</b></div><h3>{b}</h3><p>{c}</p></div>' for a,b,c in L],3,'Lessons'))
    body+=sec('The library','Eight field notes, <span class="brush">two minutes each.</span>','','<div class="fnx">'+''.join(f'<a class="fni" href="{href(n)}"><b>{n["n"]}</b><span>{n["t"]}</span></a>' for n in N)+'</div>')
    body+=sec('The four pillars','Learn is one of four, <span class="brush">in every desk.</span>','',BP.pillars())
    body+=nxt('Learn','field-notes.html','Start with field note 01. <span class="pk">A point is not a point.</span>','Eight short notes on how the rewards game actually works.','Read the field notes')
    M.render('education.html','Learn | Two minutes a week | First Officer','Learn, the fourth pillar: one short lesson a week on what your points are worth. Illustrative estimates.',body,canon='education.html',bcls='pgl')

if __name__=='__main__':
    field_notes()
    for i,n in enumerate(N):
        if n['s'] in LESSON: lesson(i)
    education()
