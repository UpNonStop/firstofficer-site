import sys, asyncio, os
from playwright.async_api import async_playwright
BASE='http://localhost:8940/'
OUT='/workspace/fo-rebuild-mockups/shots/'
async def main(pages,widths):
    os.makedirs(OUT,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w in widths:
            ctx=await b.new_context(viewport={'width':w,'height':900 if w>500 else 844},device_scale_factor=1,is_mobile=w<500,has_touch=w<500)
            pg=await ctx.new_page()
            for f in pages:
                await pg.goto(BASE+f,wait_until='load'); await pg.wait_for_timeout(1800 if 'home' not in f else 6000); await pg.add_style_tag(content='.mcta{display:none!important}')
                # overflow check
                ov=await pg.evaluate("()=>{const W=document.documentElement.clientWidth;let bad=[];document.querySelectorAll('main *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width>0&&r.right>W+2&&getComputedStyle(e).position!='fixed'&&!e.closest('.ticker')&&!e.closest('.scrollx')&&!e.classList.contains('chev')&&!e.classList.contains('mk')&&!e.closest('[data-scroll]'))bad.push(e.tagName+'.'+e.className+':'+Math.round(r.right))});return [document.documentElement.scrollWidth,W,bad.slice(0,6)]}")
                name=f.replace('/','_').replace('.html','')
                await pg.screenshot(path=f'{OUT}{name}-{w}.png',full_page=True)
                print(f,w,'scrollW',ov[0],'vw',ov[1],ov[2] if ov[2] else '')
            await ctx.close()
        await b.close()
ws=[1440,390]
args=sys.argv[1:]
if args and args[0].startswith('w='): ws=[int(x) for x in args[0][2:].split(',')]; args=args[1:]
asyncio.run(main(args,ws))
