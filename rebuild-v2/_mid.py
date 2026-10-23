import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w,h,tag,sel in [(1440,900,'1440','#feat'),(390,844,'390','#feat')]:
            c=await b.new_context(viewport={'width':w,'height':h});pg=await c.new_page()
            await pg.goto('http://localhost:8811/fo-rebuild-v2/home.html',wait_until='load');await pg.wait_for_timeout(1500)
            await pg.evaluate(f"document.documentElement.style.scrollBehavior='auto';var t=document.querySelector('{sel}').getBoundingClientRect().top+scrollY-100;window.scrollTo({{top:t,behavior:'instant'}})")
            await pg.wait_for_timeout(650)
            await pg.screenshot(path=f'_shots/v2/home-story-mid-{tag}.png')
            await pg.wait_for_timeout(2600)
            await pg.screenshot(path=f'_shots/v2/home-story-end-{tag}.png');await c.close()
        await b.close()
asyncio.run(main())
