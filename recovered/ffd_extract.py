"""One-off: pull the keepers out of PR #14's free-from-the-desk.html (branch feature/freebies-3h) into freebies-data.json.
Run: git show origin/feature/freebies-3h:free-from-the-desk.html > /tmp/ffd.html && python3 recovered/ffd_extract.py /tmp/ffd.html
Leaves out: tax, legal, lending, credit-file and HR content, playbooks, myths, deadlines, founder byline, copy-link buttons."""
import sys,os,re,json
from bs4 import BeautifulSoup
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=sys.argv[1] if len(sys.argv)>1 else '/tmp/ffd.html'
KEEP_TY={'nuggets','sheet','decoder','checklist','script','travel','gutcheck'}
KEEP_ID={'decode-cards','decode-travel','decode-pay','statement-check','empcard-check','annual-check','separator-check','refrigerant-check',
         'supplier','processor','fee-line','net-terms','counter-line','ap-line','travel-codes','travel-rules','gut-cards'}
DROP_ID={'nug-tax','nug-tipped','nug-cpa-firms','nug-law-firms','nug-property-management','nug-trucking','codes-cpa-firms'}
OVR={'nug-property':{'love':'Rent, deposits, dues and utilities. Where property money lands on a card.'}}
ALLOW=('Carrier-imposed surcharge',)
# item-level: anything touching tax, IRS forms, deductions, consumer-protection law, retirement or credit files goes
BAD=re.compile(r"\b(tax|taxes|taxable|tax-paid|taxed|IRS|1099s?|W-9s?|W-2s?|deduct\w*|Regulation E|accountable plan|IFTA|retirement|credit reports?|credit files?|your score|cents a gallon|preparer|CPA's|lawyer|attorney|Federal card rules|Federal law|Marketing services agreements)\b",re.I)
REPL=[('The stuff I see on contractor statements that nobody mentions','What shows up on contractor statements that nobody mentions'),('Specialists have their own codes','Specialty practices have their own codes'),('specialists','specialty practices'),('Specialists','Specialty practices'),
      ('the desk asks every new client','worth asking yourself'),('how many points or miles a seat costs','how many points or miles an award costs'),('The cheapest award seats on a flight','The cheapest awards on a flight'),("It's how the desk starts every new client.",'A simple monthly habit.')]
def clean(h):
    h=re.sub(r'\s*<span class="chip ex">[^<]*</span>','',h)
    for a,b in REPL: h=h.replace(a,b)
    return h.strip()
s=BeautifulSoup(open(SRC).read(),'html.parser')
out=[];dropped=[]
for a in s.find_all('article',class_='dk'):
    i,ty=a['id'],a['data-ty']
    if i in DROP_ID or not (ty in('nuggets','sheet') or i in KEEP_ID): dropped.append(i);continue
    ins=a.find('div',class_='inside')
    d=dict(id=i,ty=ty,ind=a.get('data-ind','all'),kind=a.find(class_='kind').get_text(strip=True),
           time=(a.find(class_='time').get_text(strip=True) if a.find(class_='time') else ''),
           title=clean(a.find('h3').decode_contents()),love=clean(a.find('p',class_='love').decode_contents()))
    lst=ins.find(['ol','ul']); tab=ins.find('table'); bq=ins.find('blockquote')
    if tab:
        rows=[]
        for tr in tab.find_all('tr')[1:]:
            td=tr.find_all('td'); vn=td[1].find('span',class_='vn')
            name=vn.get_text(strip=True) if vn else td[1].get_text(strip=True)
            if vn: vn.extract()
            where=td[1].get_text(' ',strip=True) if vn else ''
            row=[td[0].get_text(strip=True),where,name]
            if BAD.search(' '.join(row)): dropped.append(i+':'+row[0]);continue
            rows.append(row)
        d['rows']=rows
    elif bq:
        d['lead']=clean(ins.find('p').decode_contents()); d['quote']=clean(bq.decode_contents())
        if BAD.search(d['lead']+d['quote']): dropped.append(i);continue
    else:
        items=[]
        for li in lst.find_all('li',recursive=False):
            t=li.get_text(' ',strip=True)
            if BAD.search(t) and not t.startswith(ALLOW): dropped.append(i+': '+t[:60]);continue
            items.append(clean(li.decode_contents()))
        if not items: dropped.append(i+' (empty)');continue
        d['items']=items; d['list']=' '.join(lst.get('class',[])) or lst.name
        d['title']=re.sub(r'\b\d+ (?=(Golden |card |marketing |software )?(N|n)uggets|marketing codes)',str(len(items))+' ',d['title'])
    d.update(OVR.get(i,{}))
    if BAD.search(d['title']+d['love']): dropped.append(i+' (head)');continue
    out.append(d)
json.dump(out,open(os.path.join(HERE,'freebies-data.json'),'w'),indent=1,ensure_ascii=False)
print(len(out),'cards kept');print('\n'.join(dropped))
