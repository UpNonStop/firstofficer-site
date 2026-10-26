import asyncio, sys, json
from playwright.async_api import async_playwright
BASE='file:///workspace/fo-signup-wt/signup-campaign/'
PAGES=sys.argv[1].split(',') if len(sys.argv)>1 else ['found-money-drop-a','found-money-drop-b','index']
WS=[360,390,1440]
OUT='/workspace/mockme/'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    for pg in PAGES:
      for w in WS:
        ctx=await b.new_context(viewport={'width':w,'height':900 if w>1000 else 844},device_scale_factor=1)
        page=await ctx.new_page(); errs=[]
        page.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        page.on('pageerror',lambda e: errs.append(str(e)))
        await page.goto(BASE+pg+'.html',wait_until='networkidle')
        await page.wait_for_timeout(1800)
        ov=await page.evaluate('''()=>{const W=document.documentElement.clientWidth;let bad=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.right>W+1&&getComputedStyle(e).position!=='fixed'){let p=e,cl=false;while(p&&p!==document.body){const o=getComputedStyle(p).overflowX;if(o==='hidden'||o==='auto'||o==='scroll'||o==='clip'){if(p!==e){cl=true;break;}}p=p.parentElement;}if(!cl)bad.push(e.tagName+'.'+e.className+' '+Math.round(r.right))}});return {sw:document.documentElement.scrollWidth,W,bad:bad.slice(0,6)}}''')
        res={'page':pg,'w':w,'overflow':ov,'errors':errs}
        if pg!='index':
          tag='a' if pg.endswith('-a') else 'b'
          if w in (390,1440):
            await page.screenshot(path=f'{OUT}fmd-{tag}-{w}-hero.png')
          # trigger count-up
          await page.evaluate("document.getElementById('calc').scrollIntoView()"); await page.wait_for_timeout(1200)
          res['calc']=await page.evaluate("[document.getElementById('bignum').textContent,document.getElementById('lNet').textContent,document.getElementById('delta').textContent]")
          await page.evaluate("window.scrollTo(0,document.body.scrollHeight)"); await page.wait_for_timeout(600)
          await page.evaluate("window.scrollTo(0,0)"); await page.wait_for_timeout(400)
          if w in (390,1440):
            await page.screenshot(path=f'{OUT}fmd-{tag}-{w}.png',full_page=True)
          # mock submit
          await page.fill('#em','leo@lindenrow.example'); await page.click('#entryform button[value=call]'); await page.wait_for_timeout(200)
          res['notice']=await page.text_content('#notice')
        else:
          if w==1440: await page.screenshot(path=f'{OUT}gallery-1440.png',full_page=True)
          if w==390: await page.screenshot(path=f'{OUT}gallery-390.png',full_page=True)
        print(json.dumps(res))
        await ctx.close()
    await b.close()
asyncio.run(main())
