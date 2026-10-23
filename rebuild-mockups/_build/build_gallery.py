import sys,os,re; sys.path.insert(0,'/workspace/fo-rebuild-mockups/_build')
from common import *
from PIL import Image
G=[('Core',[('home','Home'),('book','Book Your “Found Money” Call'),('how','How it works'),('product','The Product'),('pricing','Pricing'),('calculator','Calculator'),('about','About'),('trust','Trust & Security'),('strategist','The Strategist')]),
('Onboarding & flows',[('hello','Hello (the long version)'),('connect','Connect'),('day-one','Day one'),('welcome','Welcome aboard'),('briefing','The Briefing'),('no-charge','Checkout closed'),('app','App (coming soon)')]),
('Free & reading',[('free-from-the-desk','Free From the Desk'),('field-notes','Field Notes'),('upns','Intelligence Report archive'),('upns-064','UPNS-064'),('upns-063','UPNS-063'),('upns-062','UPNS-062')]),
('Industries',[('industries','Industries index'),('industry-template','Industry template')]+[(f'for-{s}',f'{e} {n}') for s,n,e in INDS]),
('Legal & system',[('privacy-policy','Privacy Policy'),('terms-of-service','Terms of Service'),('disclaimer','Disclaimer'),('404','404')])]
os.makedirs(ROOT+'/shots/thumbs',exist_ok=True)
for _,ps in G:
    for n,_t in ps:
        f=f'{ROOT}/shots/{n}-1440.png'
        if os.path.exists(f):
            im=Image.open(f).convert('RGB'); im=im.crop((0,0,1440,min(im.height,1100))); im.thumbnail((560,560)); im.save(f'{ROOT}/shots/thumbs/{n}.jpg',quality=82)
tot=sum(len(p) for _,p in G)
sec=''
for g,ps in G:
    cards=''.join(f'<a class="gcard" href="{n}.html"><div class="gth"><img src="shots/thumbs/{n}.jpg" alt="" loading="lazy"></div><div class="gb"><b>{t}</b><span class="mono">{n}.html</span><span class="glinks"><span>1440</span> · <object><a href="shots/{n}-390.png">390 shot</a></object></span></div></a>' for n,t in ps)
    sec+=f'<section class="sec {"white" if len(sec)%2==0 else "cream"}"><div class="wrap"><div class="fok">{g} · {len(ps)}</div><div class="ggrid">{cards}</div></div></section>'
body=f'''<section class="phero"><img class="chev" src="img/fo-chevron-alpha.png" alt=""><div class="wrap"><div class="fok">Rebuild v1 · mockups</div><h1>Every page, <span class="pk">one look.</span></h1>
<p class="fosub">{tot} static mockups of the First Officer site rebuild, in the look of the new hero. HTML only, not production. Nothing here touches the live site.</p>
<div class="ctas"><a class="pill pink" href="home.html">Open the home page</a><a class="pill ghost" href="CHANGES.md">CHANGES.md</a><a class="pill ghost" href="PROPOSALS.md">PROPOSALS.md</a><a class="pill ghost" href="shots/contact-1440.png">Contact sheet 1440</a><a class="pill ghost" href="shots/contact-390.png">Contact sheet 390</a></div></div></section>{sec}'''
css='<style>.ggrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:10px}.gcard{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--sh);text-decoration:none;color:inherit;display:flex;flex-direction:column}.gcard:hover{transform:translateY(-2px)}.gth{aspect-ratio:1440/1100;overflow:hidden;border-bottom:1px solid var(--line);background:var(--cream)}.gth img{width:100%;display:block}.gb{padding:12px 14px;display:flex;flex-direction:column;gap:3px}.gb b{font-size:15px}.gb .mono{font-size:11.5px;color:var(--mute2)}.glinks{font-size:12px;color:var(--mute)}.glinks a{color:var(--pinkdeep)}@media(max-width:1060px){.ggrid{grid-template-columns:repeat(2,1fr)}}@media(max-width:560px){.ggrid{grid-template-columns:1fr}}</style>'
write('index.html',page('Rebuild v1 · All mockups · First Officer',body,extra_head=css,src='gallery'))
print('gallery',tot)
