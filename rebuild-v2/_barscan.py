"""390 check: scroll every page, and wherever the sticky CTA is showing, list any text/figure it overlaps."""
import asyncio,sys
from playwright.async_api import async_playwright
JS='''()=>{const m=document.querySelector('.mcta');if(!m)return {vis:false};const s=getComputedStyle(m);
 const vis=s.display!=='none'&&+s.opacity>0.1&&!m.classList.contains('mhide');if(!vis)return {vis:false};
 const r=m.getBoundingClientRect();const hits=[];
 document.querySelectorAll('body *').forEach(e=>{if(m.contains(e)||e.closest('.phx,header'))return;
  let t='';for(const n of e.childNodes)if(n.nodeType===3)t+=n.textContent;t=t.trim();
  const media=/^(IMG|svg|CANVAS|VIDEO|INPUT|BUTTON)$/.test(e.tagName);if(!t&&!media)return;
  const es=getComputedStyle(e);if(es.visibility==='hidden'||+es.opacity===0)return;
  const b=e.getBoundingClientRect();if(b.width<2||b.height<2)return;
  if(b.bottom>r.top&&b.top<r.bottom&&b.right>r.left&&b.left<r.right)hits.push((t||e.tagName).slice(0,40))});
 return {vis:true,hits}}'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for pgn in sys.argv[1:]:
            c=await b.new_context(viewport={'width':390,'height':844});pg=await c.new_page()
            await pg.goto(f'http://localhost:8811/fo-rebuild-v2/{pgn}.html?snap=1',wait_until='load')
            await pg.wait_for_timeout(1500);H=await pg.evaluate('document.documentElement.scrollHeight')
            shown=0;bad=[];y=0
            while y<H:
                await pg.evaluate(f'scrollTo(0,{y})');await pg.wait_for_timeout(420)
                r=await pg.evaluate(JS)
                if r['vis']:
                    shown+=1
                    if r['hits']:bad.append((y,r['hits'][:4]))
                y+=150;H=await pg.evaluate('document.documentElement.scrollHeight')
            print(pgn,'H',H,'steps',H//150,'bar shown',shown,'overlaps',len(bad))
            for x in bad[:15]:print('   ',x)
            await c.close()
        await b.close()
asyncio.run(main())
