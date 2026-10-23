import sys; sys.path.insert(0,'/workspace/fo-rebuild-mockups/_build')
from common import *
from convert import convert
# name: (title, nav-active, photo, caption)
PAGES={
 'how':('How it works','how.html','img/fo-kyoto.jpg','Kyoto, on points'),
 'pricing':('Pricing','pricing.html','img/fo-maldives.jpg','The Maldives, on points'),
 'about':('About','about.html','img/fo-lisbon.jpg','Lisbon, on points'),
 'trust':('Trust & Security','trust.html',None,''),
 'product':('The Product','product.html','img/fo-santorini.jpg','Santorini, on points'),
 'hello':('The long version','',None,''),
 'strategist':('The Strategist','',None,''),
 'connect':('Connect','',None,''),
 'day-one':('Day one','',None,''),
 'welcome':('Welcome aboard','',None,''),
 'field-notes':('Field Notes','',None,''),
 'briefing':('The Briefing','',None,''),
 'no-charge':('No charge','',None,''),
 '404':('Page not found','',None,''),
 'privacy-policy':('Privacy Policy','',None,''),
 'terms-of-service':('Terms of Service','',None,''),
}
for k in (sys.argv[1:] or PAGES):
    t,act,ph,cap=PAGES[k]
    body=convert(f'{SRC}/{k}.html',fix,k+'.html',ph,cap)
    write(k+'.html',page(f'{t} · First Officer',body,active=act,src=k,tick=('hello' if k=='hello' else False)))
    print('wrote',k)
save_log()
