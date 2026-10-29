# Step 5 (flow pages): welcome, no-charge, day-one and 404 as -modes siblings, access as a redirect. Mockup only.
# Run: python3 recovered/build_flow.py
import os,sys,re
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
import build_more as M
from build_pages import ILL,WA,dm,hero,sec,rail,nxt,deskcta
THR='https://wa.me/16199404040?text=I%27m%20in'
def fcard(chk,big,small,rows,foot=''):
    li=''.join(f'<li><span>{a}</span><b>{b}</b></li>' for a,b in rows)
    return f'<div class="fcd"><span class="chk">{chk}</span><b class="fbg">{big}</b><small>{small}</small><ul>{li}</ul>{"<p class=fft>"+foot+"</p>" if foot else ""}</div>'
def step(k,a,t,d,x=''): return f'<div class="pc4 k-{k}"><div class="pn"><b>{a}</b></div><h3>{t}</h3><p>{d}</p>{x}</div>'

def welcome():
    v=fcard('Payment received · Welcome','You’re in.','Your welcome message is waiting in WhatsApp.',[('Today','Show the desk your spend'),('This week','A short note each weekday'),('On a Friday','Your first scorecard')])
    b=hero('Payment received','You’re in. <span class="pk">Your welcome is in WhatsApp.</span>','Head back to your thread and say hello. Your welcome arrives with the first step and the date of your first Friday scorecard.',
        ['Your desk is open today.','One thread, one desk.','Nothing moves without your yes.'],v,pk=('💬 Back to my thread',THR),calc=('trust-modes.html#connect','or see the three ways to share your spend'))
    b+=sec('What happens next','From today to <span class="brush">your first scorecard.</span>',dm('Three steps, all in your thread. Give as much or as little as you like; the desk works from whatever is there.','Three steps, all in your thread.'),
        rail([step('earn','Today','Show the desk your spend','Three read-only ways, and you can mix them: tell it in your own words, send a statement, or connect an account once. None of them can move a dollar.'),
              step('burn','This week','The desk learns your business','A short note each weekday with one small question back, so the routing fits how you actually spend. Your routing map follows as soon as there is spend to build it from.'),
              step('return','On a Friday','Your first scorecard','What the desk sees, card by card, in dollars, est., wherever a statement or a connection lets it measure. Your welcome message has the date.')],3,'What happens next'))
    b+=sec('Worth knowing','Reply once a day <span class="brush">and nothing gets lost.</span>','',
        '<div class="fnt"><div class="fnc"><span class="chk">WhatsApp</span><p>WhatsApp only lets the desk write within 24 hours of your last message. A short reply to each note keeps everything arriving.</p></div>'
        '<div class="fnc"><span class="chk">Billing</span><p>$550 a month, billed monthly. Manage it in your <a href="https://billing.stripe.com/p/login/fZe02g10J1In7mMcMM">billing portal</a>, or ask in your thread. A month you have paid for runs to its end. There is no pause: if you stop, the work stops.</p></div></div>')
    b+=nxt('02','day-one.html','Day one: your draft strategy.','The desk drafts your strategy from what you told it, then asks for the two things that would sharpen it.','See day one')
    M.render('welcome.html','You’re in | First Officer','Payment received. Your welcome is waiting in WhatsApp.',b,canon='welcome.html',bcls='pgf',robots='noindex',ga=True,meta=M.seo('You’re in | First Officer','Payment received. Your welcome is waiting in WhatsApp.','welcome.html'))

def no_charge():
    v=fcard('Checkout closed','$0','Nothing was charged and nothing has started.',[('Your link','Live for 24 hours from when it was sent'),('Expired?','Reply READY for a fresh one'),('Questions first?','Ask in your thread')])
    b=hero('Checkout closed','Nothing was charged. <span class="pk">Your link is in your thread.</span>','You left the checkout before paying, so no card was charged. The link stays live for 24 hours from when it was sent. Pick it up any time before then, or ask anything first.',
        ['No card was charged.','Nothing has started.','Your link is still in the thread.'],v,pk=('💬 Back to my thread','https://wa.me/16199404040?text=READY'),calc=('pricing-modes.html','or read what the $550 a month covers'))
    b+=nxt('01','book-modes.html','Not sure yet? Start with the free call.','The Found Money Call is free and takes 20 minutes. Bring your statements; leave with what your spend is leaving on the table, est.','Book the Found Money Call')
    M.render('no-charge.html','Nothing was charged | First Officer','You left the checkout before paying. Nothing was charged.',b,canon='no-charge.html',bcls='pgf',robots='noindex',ga=True,meta=M.seo('Nothing was charged | First Officer','You left the checkout before paying. Nothing was charged.','no-charge.html'))

def day_one():
    v=('<div class="fcd dft"><span class="chk">The draft · built today · example</span><small>Draft strategy for $35,000 a month of spend, est.</small>'
       '<ul><li><span>Where your spend lands today</span><b><i data-count="1.1" data-dec="1" data-suf="x">0x</i></b></li><li><span>Where it could land, routed</span><b class="g"><i data-count="2.6" data-dec="1" data-suf="x">0x</i></b></li>'
       '<li><span>The gap, in points a year</span><b><i data-count="630000">0</i></b></li><li><span>What that could be worth</span><b class="g"><i data-count="13230" data-pre="$">$0</i></b></li></ul>'
       '<p class="fft">Modelled at 2.1¢ a point on stated spend. Your mix and redemptions will differ. '+ILL+'</p></div>')
    b=hero('Day one · The desk is open','Welcome to day one. <span class="pk">Here is your draft.</span>','The desk drafted your strategy from what you told it. Two things would sharpen it, and both take a minute.',
        ['Your file: 2 of 4 done.','Drafted from your own words.','The draft is yours to change.'],v,pk=('💬 Talk about my draft','https://wa.me/16199404040?text=About%20my%20draft'),calc=('trust-modes.html#connect','or see the ways to share your spend'))
    b+=sec('What it turns into','Not points. <span class="brush">Trips and nights.</span>',dm('The same spending, routed and then spent well. This is what a year of it could look like at this volume, est.','A year of it at this volume, est.'),
        '<div class="fnt two"><div class="fnc big"><b><i data-count="2">0</i></b><span>Business-class trips a year, est.</span></div><div class="fnc big"><b><i data-count="11">0</i></b><span>Hotel nights a year, est.</span></div></div><p class="fill">'+ILL+'</p>')
    b+=sec('What is missing · 3 items','Three things <span class="brush">would sharpen it.</span>','',
        rail([step('earn','01','Offers in your inbox','Targeted offers and statement credits arrive by email and expire quietly. Forward them and the desk reads only those.','<a class="btn pk fbt" href="https://wa.me/16199404040?text=STATEMENT">Send statements</a>'),
              step('burn','02','How your vendors code','Two of your suppliers probably code as wholesale, which pays 1x whichever card you use. A read-only connection shows which.','<a class="btn pk fbt" href="trust-modes.html#connect">See the ways to connect</a>'),
              step('return','03','Anything look wrong?','The draft is the desk’s until you say otherwise. Say what it missed and it rebuilds.','<a class="btn wa fbt" href="https://wa.me/16199404040?text=About%20my%20draft">💬 Tell the desk</a>')],3,'What is missing'))
    b+=sec('Two ways to reach the desk','One thread, one inbox. <span class="brush">The same desk.</span>','',
        '<div class="fnt"><a class="fnc" href="https://wa.me/16199404040?text=My%20cards"><span class="chk">WhatsApp</span><p>Text the desk in your thread. <b>Open WhatsApp →</b></p></a><a class="fnc" href="mailto:desk@upnonstop.com?subject=My%20cards"><span class="chk">Email</span><p>Reply by email and it lands in the same file. <b>Write an email →</b></p></a></div>')
    b+=nxt('03','trust-modes.html#connect','Share your spend, your way.','Tell it, send a statement or connect once. All read-only, and you can mix them per card.','See the three ways')
    M.render('day-one.html','Day one | First Officer','Day one: your draft strategy, and the two things that would sharpen it. Illustrative estimates.',b,canon='day-one.html',bcls='pgf',robots='noindex,follow')

def p404():
    v=fcard('404 · Missed connection','404','This page is not on the route. The desk has rebooked you.',
        [('Requested','<i>Not found</i>'),('Rebooked to','<a href="home-modes.html">The story, from the top</a>'),('Fastest route','<a href="calculator-modes.html">Your number, est.</a>'),('Or ask','<a href="'+WA+'">Text the desk</a>')])
    b=hero('404 · Page not found','Missed connection. <span class="pk">We rebooked you.</span>',
        dm('The page you asked for is not here. Missing a connection happens to the best itineraries; the answer is always the next good route. Here are four, in story order.','Not here. Here are four good routes, in story order.'),
        ['Four routes, one story.','The Found Money Call is free, 20 min.','Nothing moves without your yes.'],v,pk=('Start the story','home-modes.html'),calc=('calculator-modes.html','or run your numbers'))
    R=[('01','Home','home-modes.html','You are not bad at Points & Miles. You are just outnumbered.','Every program has a team rewriting the rules. Start here to see what a desk on your side changes.','Start the story'),
       ('02','Calculator','calculator-modes.html','What could your spend earn?','Pick your trade, set your monthly card spend and see the gap in dollars, est.','Run your numbers'),
       ('03','Pricing','pricing-modes.html','$550 a month, flat.','The desk fits best from about $25k a month on cards. See first if your spend clears it.','See pricing'),
       ('04','Book','book-modes.html','The Found Money Call.','Free, 20 minutes. The desk walks you through what it found in your spend.','Book the call')]
    cards=''.join(f'<a class="fnc rt" href="{h}"><span class="chk">Chapter {n} · {k}</span><b class="rth">{t}</b><p>{d}</p><span class="rtb">{bt} <span class="ar">→</span></span></a>' for n,k,h,t,d,bt in R)
    b+=sec('Four routes back','Pick up the story <span class="brush">where it suits you.</span>',dm('Home tells the story, the calculator puts your numbers in it, pricing shows what the desk costs, and the call shows what it found.','Story, numbers, price, call.'),'<div class="fnt rts">'+cards+'</div>')
    Q=[('product-modes.html','What the desk does'),('trust-modes.html','What it sees, and never touches'),('industries-modes.html','Your trade'),('field-notes.html','Field notes'),('about-modes.html','About'),(WA,'💬 Text the desk')]
    b+=sec('Looking for something else','Or jump <span class="brush">straight there.</span>','','<div class="fql">'+''.join(f'<a href="{h}">{t} <span class="ar">→</span></a>' for h,t in Q)+'</div>',cls='tight')
    b+=nxt('01','home-modes.html','Start at the beginning.','You are not bad at Points & Miles. You are just outnumbered. Meet the desk that evens it out.','Start the story')
    M.render('404.html','Page not found | First Officer','This page is not on the route. Four good routes back into the First Officer story.',b,canon='404.html',bcls='pgf',robots='noindex',ga=True,meta=M.seo('Page not found | First Officer','This page is not on the route. Four good routes back into the First Officer story.','404.html'))

if __name__=='__main__':
    welcome();no_charge();day_one();p404()
    M.redirect('access.html','pricing-modes.html','Pricing','Access and pricing live on the pricing page.')

def briefing_patch():
    # briefing keeps its transplanted intake (and its FO.url ?t= wire); only copy fixes and a Next chapter card are added here
    p=os.path.join(M.ROOT,'briefing.html');s=open(p).read()
    s=s.replace('<p>Gmail will tell me a lot. Your accounts will tell me more.','<p>Your inbox will tell me a lot. Your statements will tell me more.')
    s=s.replace('The link was made for\n    you, it is not listed anywhere, and nobody else can open it or see what you write here.','The link was made for\n    you and is not listed anywhere.')
    if 'class="sec tight pnx"' not in s:
        s=s.replace('</main>',nxt('02','day-one.html','Day one: your draft strategy.','What you answer here becomes the first draft. Day one shows it, with the two things that would sharpen it.','See day one')+'</main>',1)
    # the shared footer (now with The Daily Redemption signup) replaces the frozen copy
    nf=re.search(r'<footer class="foot">.*?</footer>',M.finish(M.chrome('')[2]),re.S).group(0)
    s=re.sub(r'<footer class="foot">.*?</footer>',lambda m:nf,s,count=1,flags=re.S)
    open(p,'w').write(s);print('patched briefing.html')
if __name__=='__main__': briefing_patch()
