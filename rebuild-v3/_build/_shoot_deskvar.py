import asyncio, sys, os, shutil, glob
from playwright.async_api import async_playwright
BASE='http://localhost:8824/rebuild-v3/'
NS=[int(x) for x in sys.argv[1:]] or [1,2,3,4,5]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for n in NS:
            for w,h in [(1440,900),(390,844),(360,780)]:
                ctx=await b.new_context(viewport={'width':w,'height':h},device_scale_factor=2 if w<500 else 1,
                    **({'record_video_dir':'/tmp/vid','record_video_size':{'width':390,'height':844}} if w==390 else {}))
                pg=await ctx.new_page();errs=[]
                pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None);pg.on('pageerror',lambda e: errs.append(str(e)))
                await pg.goto(BASE+f'desk-var-{n}.html',wait_until='networkidle')
                el=await pg.query_selector('.dv')
                await pg.evaluate("document.querySelector('.dvk').scrollIntoView({block:'start'});window.scrollBy(0,-70)")
                await pg.add_style_tag(content='header.nav{position:static!important}')
                await pg.wait_for_timeout(4700)
                ov=await pg.evaluate("[document.documentElement.scrollWidth,innerWidth]")
                v=await pg.query_selector('.dv .lede2 + *')
                await v.screenshot(path=f'/tmp/vis-{n}-{w}.png')
                if w!=360:
                    await el.screenshot(path=f'/workspace/mockme/deskvar-{n}-{w}.png')
                else:
                    await el.screenshot(path=f'/tmp/deskvar-{n}-360.png')
                if w==390:
                    await pg.wait_for_timeout(4000)
                print(n,w,'overflow' if ov[0]>ov[1] else 'ok',ov,'errors:',errs)
                vp=pg.video
                await ctx.close()
                if vp:
                    src=await vp.path();shutil.move(src,f'/workspace/mockme/deskvar-{n}-390.webm')
        await b.close()
asyncio.run(main())
