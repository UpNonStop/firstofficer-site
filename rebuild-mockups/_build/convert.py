import re
from bs4 import BeautifulSoup, NavigableString, Tag
KEEP={'phone','bub','in','out','wa-cap','wa-head','fok','foh2','pk','fosub','statband','v','l','tl','tlrow','ty','eq','eqcard','eqk','eqop','mid','soon','callout','updated','human','hi','nug','coin','src','ctas'}
DROP_SEL='.tickerbar,.hbgs,.typing,.swipehint,.js-date,script,style,noscript,svg,canvas,iframe,template,link,meta,.fonav,.nsheet,.mcta,.fofoot,.sitedir,.ftbar,.focap,.pinkband,.fo-datanote,.hellobar,.nburger,[hidden],[aria-hidden=true]'
BLOCK={'div','section','article','header','footer','aside','figure','ul','ol','li','p','h1','h2','h3','h4','h5','h6','table','blockquote','form','details','main','nav','dl','dt','dd'}
INLINE_OK={'a','span','strong','b','em','i','br','small','sup','sub','code','img','u','mark','abbr','time'}
def txt(t): return re.sub(r'\s+',' ',t.get_text(' ',strip=True)) if isinstance(t,Tag) else str(t).strip()
def echildren(t): return [c for c in t.children if isinstance(c,Tag)]
def is_hidden(t):
    st=(t.get('style') or '').replace(' ','').lower()
    return 'display:none' in st or 'visibility:hidden' in st
def sig(t): return t.name+'.'+'.'.join(sorted(t.get('class',[])))
def mark(t):
    """heuristics on original tree; sets data-x"""
    for d in t.find_all(['div','section','ul','article']):
        ch=echildren(d)
        if len(ch)<2 or d.get('data-x'): continue
        cls=set(d.get('class',[]))
        if cls & {'statband','tl','eq','tlrow','eqcard'}: continue
        sigs=[sig(c) for c in ch]
        common=max(set(sigs),key=sigs.count)
        same=sigs.count(common)
        if same<2 or same<len(ch)*0.6: continue
        reps=[c for c in ch if sig(c)==common]
        lens=[len(txt(c)) for c in reps]
        if min(lens)==0: continue
        # row-like: each rep has 2-4 element children with short texts and no deeper blocks
        def rowlike(c):
            k=echildren(c)
            if not (2<=len(k)<=4): return False
            if sum(len(txt(x)) for x in k)>170: return False
            return all(not any(isinstance(g,Tag) and g.name in BLOCK and len(txt(g))>60 for g in x.find_all(True)) for x in k)
        if d.name=='ul' and all(c.name=='li' for c in ch) and max(lens)<220 and not all(rowlike(c) for c in reps):
            continue
        if all(rowlike(c) for c in reps) and len(reps)>=2 and max(lens)<170:
            d['data-x']='rows'; [c.__setitem__('data-x','row') for c in reps]
        elif max(lens)>25 or any(echildren(c) for c in reps):
            d['data-x']='grid'+('2' if len(reps)==2 or len(reps)==4 else '')
            for c in reps: c['data-x']='card'
def clean(t, imgok=True):
    for n in t.select(DROP_SEL): n.decompose()
    for n in list(t.find_all(True)):
        if n.decomposed if hasattr(n,'decomposed') else False: continue
        if is_hidden(n): n.decompose()
    for n in list(t.find_all(string=re.compile(r'^\s*TODO'))):
        par=n.parent
        if par and par.name!='[document]': par.decompose()
    for n in t.find_all(['input','select','textarea','button','label','form']):
        if n.name=='button':
            n.name='span'; n['class']=['chipb']
        elif n.name=='form': n.name='div'
        elif n.name=='label': n.name='span'
        else: n.decompose()
    for n in t.find_all('img'):
        s=n.get('src','')
        if s.startswith('data:') and len(s)>60000: n.decompose()
    for n in t.find_all(True):
        x=n.get('data-x'); cls=[c for c in n.get('class',[]) if c in KEEP]
        if x=='grid': cls+=['agrid']
        if x=='grid2': cls+=['agrid','g2c']
        if x=='rows': cls+=['arows']
        if x=='row': cls+=['arow']
        if x=='card': cls+=['acard']
        keep={}
        if cls: keep['class']=cls
        for a in ('href','id','src','alt','colspan','rowspan','target','rel','open'):
            if n.get(a) is not None: keep[a]=n[a]
        if 'href' in keep:
            h=keep['href']
            if h in ('index.html','./','/','https://firstofficer.upnonstop.com/'): keep['href']='home.html'
            elif h.startswith('index.html#'): keep['href']='home.html'+h[10:]
        n.attrs=keep
    # unwrap meaningless nested divs
    for n in t.find_all('div'):
        ch=echildren(n)
        if not n.attrs and len(ch)==1 and ch[0].name=='div' and not txt_direct(n): n.unwrap()
    # leaf divs with only inline content -> p ; first short child in card -> kicker
    for n in t.find_all('div'):
        if n.get('class') and set(n['class'])&{'v','l','ty','eqk','eqop','fok','fosub'}: continue
        if not any(isinstance(c,Tag) and c.name in BLOCK for c in n.children):
            if n.parent and n.parent.get('class') and 'arow' in n.parent.get('class'): n.name='span'; continue
            n.name='p'
    for g in t.select('.agrid'):
        if len(g.select(':scope > .acard'))>12: g['class']=g['class']+['scrollx']
    for c in t.select('.acard'):
        ch=echildren(c)
        if len(ch)>=2 and ch[0].name in ('p','span','div') and len(txt(ch[0]))<=46:
            s=txt(ch[0])
            if re.match(r'^(\$|\d|[A-Z0-9 ·/&%,.+:\-–]+$)',s) and len(s)<=14 and re.search(r'\d',s): ch[0]['class']=['bn']
            elif s.upper()==s or re.match(r'^\d\d',s): ch[0]['class']=['k1']
            elif ch[1].name in ('p','span','div','ul'): ch[0]['class']=['lead']
    for sp in t.select('.pk'):
        pv=sp.previous_sibling
        if isinstance(pv,NavigableString) and pv and not pv[-1].isspace(): pv.replace_with(pv+' ')
        elif isinstance(pv,Tag): sp.insert_before(' ')
    return t
def txt_direct(n): return ''.join(str(c) for c in n.children if isinstance(c,NavigableString)).strip()

def convert(path, fixer, page, photo=None, cap=''):
    s=BeautifulSoup(open(path).read(),'lxml')
    root=s.select_one('.gallery .screen') or s.select_one('.gallery') or s.select_one('main') or s.body
    l4=[txt(x) for x in root.select('.l4note')]
    for x in root.select('.l4note'): x.decompose()
    mark(root)
    clean(root)
    def flat(nodes):
        r=[]
        for c in nodes:
            ch=echildren(c)
            if c.name in ('div','main') and not (set(c.get('class',[]))&{'sec','statband','hero'}) and any(set(x.get('class',[]))&{'sec','statband'} for x in ch):
                r+=flat(ch)
            elif 'hero' in c.get('class',[]) and c.find('h1'):
                c.attrs.pop('class',None); r.append(c)
            else: r.append(c)
        return r
    blocks=flat(echildren(root))
    if len(blocks)==1 and blocks[0].name in ('main','div') and len(echildren(blocks[0]))>2 and not (set(blocks[0].get('class',[]))&{'statband'}):
        blocks=echildren(blocks[0])
    out=[];hero_done=False;alt=0
    for b in blocks:
        cls=set(b.get('class',[]))
        if not txt(b) and not b.find('img'): continue
        if 'statband' in cls:
            out.append(f'<div class="statwrap">{b}</div>'); continue
        if not hero_done and b.find('h1'):
            hero_done=True
            h1=b.find('h1').extract(); h1.attrs={k:v for k,v in h1.attrs.items() if k=='id'}
            ph=b.select_one('.phone')
            if ph and not photo:
                ph=ph.extract(); photo_html=f'<div class="herochat">{ph}</div>'
            else: photo_html=''
            rest=''.join(str(c) for c in b.children if c is not h1)
            fig=photo_html or f'<figure class="pola"><img src="{photo}" alt=""><figcaption><span>{cap}</span><span>Illustrative</span></figcaption></figure>' if photo else ''
            out.append(f'<section class="phero{" split" if (photo or photo_html) else ""}"{" id="+repr(b.get("id")) if b.get("id") else ""}><img class="chev" src="img/fo-chevron-alpha.png" alt=""><div class="wrap"><div class="gx">{h1}{rest}</div>{fig}</div></section>'); continue
        alt+=1
        bid=b.get('id')
        inner=''.join(str(c) for c in b.children) if b.name in ('section','div') else str(b)
        out.append(f'<section class="sec {"cream" if alt%2==0 else "white"}"{(" id=%s" % repr(bid)) if bid else ""}><div class="wrap gx">{inner}</div></section>')
    if not hero_done and out:
        pass
    html='\n'.join(out)
    html=html.replace('<p></p>','')
    if l4: html+=''.join(f'<div class="l4note">{x}</div>' for x in dict.fromkeys(l4))
    return fixer(html,page)
