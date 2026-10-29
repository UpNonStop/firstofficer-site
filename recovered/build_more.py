# Rebuild of the old (pre -modes) pages on the -modes system. Mockup only.
# Never edits build_modes.py, modes.css, modes.js or fo-modes-data.js. New CSS lives in recovered/modes-pages.css.
# Every owner is fictional and every figure is illustrative, est.
import os,sys,re,json,glob
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.dirname(HERE)
sys.path.insert(0,HERE)
import build as B
import build_pages as BP
WA=BP.WA;ILL=BP.ILL
SITE='https://firstofficer.upnonstop.com/'
DISC='Every owner shown is a fictional example. Illustrative, est. Not tax, legal or financial advice.'
CSSL='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Kalam:wght@300;400&display=swap">\n<link rel="stylesheet" href="recovered/rec.css">\n<link rel="stylesheet" href="recovered/modes.css">\n<link rel="stylesheet" href="recovered/modes-pages.css">'

def chrome(on=''):
    """-modes top bar (pink Get your desk + green Text Your First Officer), ticker, approved footer. No bottom bars."""
    nav=B.nav(on)
    nav=nav.replace('<a class="btn pk" href="'+WA+'">💬 Text Your First Officer</a>\n<button class="burger"','<span class="nbtns"><a class="btn pk" href="book.html">Get your desk</a><a class="btn wa" href="'+WA+'">💬 Text Your First Officer</a></span>\n<button class="burger"',1)
    nav=nav.replace('<a class="btn pk" href="'+WA+'">💬 Text Your First Officer</a>\n</div>','<a class="btn pk" href="book.html">Get your desk</a>\n<a class="btn wa" href="'+WA+'">💬 Text Your First Officer</a>\n</div>',1)
    assert 'class="nbtns"' in nav
    foot=B.footer().replace('Your rewards desk. One conversation, 50+ programs, trained on new data nightly.','Your rewards desk. One conversation, every program.')
    foot=foot.replace('Leo and Linden Row Insurance are fictional. All figures are examples and estimates.',DISC)
    foot=re.sub(r'<div class="mcta">.*?</a></div>\n?','',foot,flags=re.S)
    foot=foot.replace('<a href="industries.html">Industries</a>','<a href="industries.html">Industries</a><a href="field-notes.html">Field Notes</a>',1)
    return nav,B.ticker(),foot

def tail(extra=''):
    return '<script>window.FO_A="'+B.ASSET+'";</script>\n<script src="recovered/rec.js"></script>\n<script src="recovered/pages.js"></script>\n'+extra

def finish(h): return B.absol(BP.relink(h))

def render(fn,title,desc,body,on='',canon=None,head_extra='',tail_extra='',bcls=''):
    h=B.head(title,desc).replace('<link rel="stylesheet" href="recovered/rec.css">',CSSL)
    if canon: h=h.replace('</head>','<link rel="canonical" href="'+SITE+canon+'">\n</head>')
    if head_extra: h=h.replace('</head>',head_extra+'\n</head>')
    nav,tick,foot=chrome(on)
    h+='<body class="modes pgx pgr %s">\n'%bcls+nav+tick+'<main>\n'+body+'</main>\n'+foot+tail(tail_extra)+'</body>\n</html>\n'
    open(os.path.join(ROOT,fn),'w').write(finish(h));print('built',fn)

def redirect(fn,to,title,line,body=''):
    """Lightweight redirect page: meta refresh + canonical + JS replace that keeps any query string."""
    q=to.split('#')
    # htmlpreview-aware: on htmlpreview.github.io the target page is carried in the query, so swap the file name there
    js=("(function(){var t='%s',h='%s',l=location;if(l.hostname=='htmlpreview.github.io'){var s=l.search.slice(1),i=s.indexOf('?'),"
        "u=i<0?s:s.slice(0,i),q=i<0?'':s.slice(i);l.replace(l.origin+l.pathname+'?'+u.replace(/[^\\/]*$/,t)+q+h)}else l.replace(t+l.search+h)})()")%(q[0],('#'+q[1]) if len(q)>1 else '')
    h=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{SITE}{to}">
<noscript><meta http-equiv="refresh" content="0; url={to}"></noscript>
<title>{title} | First Officer</title>
<script>{js};</script>
<style>body{{margin:0;font:17px/1.5 'DM Sans',system-ui,sans-serif;background:#FAF6EE;color:#141216;display:grid;place-items:center;min-height:100vh;padding:24px;box-sizing:border-box}}a{{color:#E60F86;font-weight:700}}</style>
</head><body><p>{line} <a href="{to}">Continue →</a></p></body></html>
'''
    open(os.path.join(ROOT,fn),'w').write(h);print('redirect',fn,'->',to)

# ---------------- Step 1: shared chrome transplanted onto old pages that keep their bodies ----------------
CSSDEF=None
def _defs():
    global CSSDEF
    if CSSDEF is None:
        css=open(os.path.join(HERE,'rec.css')).read()+open(os.path.join(HERE,'modes.css')).read()
        CSSDEF=set(re.findall(r'\.([a-zA-Z][\w-]*)',re.sub(r'url\([^)]*\)','',css)))
    return CSSDEF

def _cut(s,start_pat):
    """Remove the balanced element whose open tag matches start_pat (div, section, footer or nav)."""
    m=re.search(start_pat,s)
    if not m: return s,False
    tag=re.match(r'<(\w+)',m.group(0)).group(1)
    i=m.start();depth=0
    for t in re.finditer(r'<(/?)%s\b[^>]*>'%tag,s[i:]):
        depth+=-1 if t.group(1) else 1
        if depth==0: return s[:i]+s[i+t.end():],True
    return s,False

STRAT=[(r'<a[^>]*href="[^"]*strategist(?:\.html)?"[^>]*>.*?</a>\s*(?:·\s*)?',''),(r'The Strategist','The desk'),(r'\bStrategist\b','desk')]
def scrub(s):
    for a,b in STRAT: s=re.sub(a,b,s,flags=re.S)
    s=s.replace('An educational tool, not a licensed financial advisor.','Illustrative, est. Not tax, legal or financial advice.')
    s=s.replace('not a licensed financial advisor','not tax, legal or financial advice')
    return s

def transplant(fn,on=''):
    p=os.path.join(ROOT,fn);s=open(p).read()
    if 'class="modes pgx' in s: print('skip (already on -modes chrome)',fn);return
    hd,bd=s.split('<body',1);battr,bd=bd.split('>',1)
    # old chrome out
    for pat in [r'<div class="fonav[^"]*"',r'<div class="nsheet"',r'<div class="fofoot"',r'<section class="focap"',r'<div class="sitedir"',r'<div class="ftbar"',r'<a[^>]*id="mcta"',r'<div[^>]*id="stickyCta"',r'<div[^>]*class="mcta"',r'<footer\b']:
        while True:
            bd,ok=_cut(bd,pat)
            if not ok: break
    bd=re.sub(r'<script>function foNav\(open\).*?</script>','',bd,flags=re.S)
    bd=re.sub(r'<script id="(?:fo66js|navsolid|focapjs)">.*?</script>','',bd,flags=re.S)
    # rename classes that collide with rec.css / modes.css so the old body keeps its own look
    D=_defs()
    used=set(x for m in re.findall(r'class="([^"]+)"',bd) for x in m.split())
    col=sorted(used&D,key=len,reverse=True)
    def rcls(m): return 'class="'+' '.join(('o-'+x if x in col else x) for x in m.group(1).split())+'"'
    bd=re.sub(r'class="([^"]+)"',rcls,bd)
    def rsel(css):
        for c in col: css=re.sub(r'\.%s(?![\w-])'%re.escape(c),'.o-'+c,css)
        return css
    def rstyle(m): return m.group(1)+rsel(m.group(2))+m.group(3)
    hd=re.sub(r'(?is)(<style[^>]*>)(.*?)(</style>)',rstyle,hd);bd=re.sub(r'(?is)(<style[^>]*>)(.*?)(</style>)',rstyle,bd)
    def rjs(m):
        js=m.group(2)
        def rstr(k):
            t=k.group(0)
            for c in col: t=re.sub(r'\.%s(?![\w-])'%re.escape(c),'.o-'+c,t)
            return t
        js=re.sub(r"'[^'\n]*'|\"[^\"\n]*\"",rstr,js)
        for c in col:
            js=re.sub(r"(classList\.(?:add|remove|toggle|contains)\(\s*['\"])%s(['\"])"%re.escape(c),lambda k:k.group(1)+'o-'+c+k.group(2),js)
            js=re.sub(r"(className\s*=\s*['\"])%s(['\"])"%re.escape(c),lambda k:k.group(1)+'o-'+c+k.group(2),js)
        return m.group(1)+js+m.group(3)
    bd=re.sub(r'(?is)(<script(?![^>]*src)[^>]*>)(.*?)(</script>)',rjs,bd)
    hd=hd.replace('</head>',CSSL+'\n</head>') if '</head>' in hd else hd
    nav,tick,foot=chrome(on)
    bd=bd.replace('</body>','')
    bd=bd.replace('</html>','')
    out=hd+'<body class="modes pgx pgo"'+re.sub(r'\sclass="[^"]*"','',battr)+'>\n'+nav+tick+'<div class="oldbody">\n'+bd+'\n</div>\n'+foot+tail()+'</body>\n</html>\n'
    out=scrub(out)
    open(p,'w').write(finish(out));print('transplanted',fn,'renamed',len(col))

STEP1=['field-notes.html','connect.html','welcome.html','no-charge.html','day-one.html','briefing.html','404.html']+sorted(os.path.basename(f) for f in glob.glob(os.path.join(ROOT,'for-*.html')))

if __name__=='__main__':
    steps=sys.argv[1:] or ['1']
    if '1' in steps:
        for f in STEP1: transplant(f)
