import asyncio, sys, shutil
from playwright.async_api import async_playwright
BASE='http://localhost:8824/rebuild-v3/'
NS=[int(x) for x in sys.argv[1:]] or [1,2,3]
PROBE="""new Promise(r=>{var a=[],l=performance.now(),s=l;function f(t){a.push(t-l);l=t;if(t-s<2000)requestAnimationFrame(f);else{a.sort((x,y)=>x-y);r({n:a.length,avg:+(a.reduce((x,y)=>x+y,0)/a.length).toFixed(1),p95:+a[Math.floor(a.length*.95)].toFixed(1),max:+a[a.length-1].toFixed(1)})}}requestAnimationFrame(f)})"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for n in NS:
            for w,h in [(1440,900),(390,844),(360,780)]:
                vid={'record_video_dir':'/tmp/vid','record_video_size':{'width':w,'height':h}} if w in (390,1440) else {}
                ctx=await b.new_context(viewport={'width':w,'height':h},device_scale_factor=2 if w<500 else 1,**vid)
                pg=await ctx.new_page();errs=[]
                pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None);pg.on('pageerror',lambda e: errs.append(str(e)))
                await pg.goto(BASE+f'desk-sphere-{n}.html',wait_until='networkidle')
                await pg.add_style_tag(content='header.nav{position:static!important}')
                await pg.evaluate("var s=document.querySelector('.sx');s.scrollIntoView({block:'center'})")
                await pg.wait_for_timeout(4300)
                ov=await pg.evaluate("[document.documentElement.scrollWidth,innerWidth]")
                fr=await pg.evaluate(PROBE)
                await pg.set_viewport_size({'width':w,'height':1300 if w<500 else 1100});await pg.evaluate("document.querySelector('.dv').scrollIntoView()");await pg.wait_for_timeout(1800)
                el=await pg.query_selector('.dv')
                out=f'/workspace/mockme/sphere-{n}-{w}.png' if w!=360 else f'/tmp/sphere-{n}-360.png'
                bb=await el.bounding_box();await pg.screenshot(path=out,clip=bb,animations='allow')
                v=await pg.query_selector('.sx');await v.screenshot(path=f'/tmp/svis-{n}-{w}.png')
                await pg.wait_for_timeout(3000)
                print(n,w,'overflow' if ov[0]>ov[1] else 'ok',ov,'raf',fr,'errors:',errs,flush=True)
                vp=pg.video
                await ctx.close()
                if vp: shutil.move(await vp.path(),f'/workspace/mockme/sphere-{n}-{w}.webm')
        await b.close()
asyncio.run(main())
