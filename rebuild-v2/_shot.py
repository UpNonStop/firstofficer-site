import sys, asyncio, io
from playwright.async_api import async_playwright
from PIL import Image
# usage: _shot.py out_prefix url [wait_ms]   -> stitched full pages (DPR1) to avoid >16k tiling artifacts
async def main(prefix, url, wait=2500):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for w,h,tag in [(1440,900,'1440'),(390,844,'390')]:
            ctx = await b.new_context(viewport={'width':w,'height':h}, device_scale_factor=1)
            pg = await ctx.new_page()
            await pg.goto(url, wait_until='load', timeout=90000)
            await pg.wait_for_timeout(wait)
            await pg.screenshot(path=f'{prefix}-{tag}-fold.png')
            H = await pg.evaluate('document.documentElement.scrollHeight')
            y=0
            while y < H:
                await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(110); y+=h//2
                H = await pg.evaluate('document.documentElement.scrollHeight')
            await pg.evaluate("document.querySelectorAll('header.fonav,.mcta').forEach(e=>e.style.visibility='hidden')")
            H = await pg.evaluate('document.documentElement.scrollHeight')
            out=Image.new('RGB',(w,H),'white'); y=0
            while y < H:
                yy=min(y,H-h)
                await pg.evaluate(f'window.scrollTo(0,{yy})'); await pg.wait_for_timeout(350)
                if y==0: await pg.evaluate("document.querySelectorAll('header.fonav').forEach(e=>e.style.visibility='visible')")
                im=Image.open(io.BytesIO(await pg.screenshot()))
                if y==0: await pg.evaluate("document.querySelectorAll('header.fonav').forEach(e=>e.style.visibility='hidden')")
                out.paste(im,(0,yy)); y+=h
            out.save(f'{prefix}-{tag}-full.png')
            await ctx.close()
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 2500))
