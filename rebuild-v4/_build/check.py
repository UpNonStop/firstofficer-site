import asyncio, sys, json
from playwright.async_api import async_playwright
BASE='file:///workspace/fo-v4-wt/rebuild-v4/'
PAGES=sys.argv[1].split(',') if len(sys.argv)>1 else ['free-from-the-desk','home','for-dental','book','index-gallery']
WS=[360,390,1440]
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
        await page.wait_for_timeout(600)
        ov=await page.evaluate('''()=>{const W=document.documentElement.clientWidth;let bad=[];document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.right>W+1&&getComputedStyle(e).position!=='fixed'){let p=e,cl=false;while(p&&p!==document.body){const o=getComputedStyle(p).overflowX;if(o==='hidden'||o==='auto'||o==='scroll'||o==='clip'){if(p!==e){cl=true;break;}}p=p.parentElement;}if(!cl)bad.push(e.tagName+'.'+e.className+' '+Math.round(r.right))}});return {sw:document.documentElement.scrollWidth,W,bad:bad.slice(0,6)}}''')
        # full page shot with all reveals forced
        await page.evaluate("document.querySelectorAll('[data-rv],.dk').forEach(e=>e.classList.add('in','vis'))")
        await page.evaluate("window.scrollTo(0,document.body.scrollHeight)"); await page.wait_for_timeout(500); await page.evaluate("window.scrollTo(0,0)"); await page.wait_for_timeout(300)
        await page.screenshot(path=f'/workspace/mockme/v4-{pg}-{w}.png',full_page=True)
        res={'page':pg,'w':w,'overflow':ov,'errors':errs}
        if pg=='free-from-the-desk':
          r={}
          r['cards_shown']=await page.evaluate("[...document.querySelectorAll('#desk-grid .dk')].filter(c=>!c.hidden).length")
          await page.select_option('#typesel','decoder'); await page.wait_for_timeout(500)
          r['decoder']=await page.evaluate("[...document.querySelectorAll('#desk-grid .dk')].filter(c=>!c.hidden).length")
          await page.select_option('#typesel','all'); await page.select_option('#tradesel','dental'); await page.wait_for_timeout(500)
          r['dental']=await page.evaluate("[...document.querySelectorAll('#desk-grid .dk')].filter(c=>!c.hidden).length")
          r['dental_count']=await page.text_content('#deskcount')
          await page.select_option('#tradesel','all')
          await page.fill('#deskq','5812'); await page.wait_for_timeout(700)
          r['search']=await page.text_content('#deskcount')
          r['hl']=await page.evaluate("CSS.highlights&&CSS.highlights.get('deskq')?CSS.highlights.get('deskq').size:0")
          await page.screenshot(path=f'/workspace/mockme/v4-ffd-search-{w}.png')
          await page.fill('#deskq',''); await page.wait_for_timeout(500)
          g=page.locator('#desk-grid .dk:not([hidden]) summary.grab').nth(1)
          await g.scroll_into_view_if_needed(); await g.click(); await page.wait_for_timeout(600)
          r['reader_open']=await page.evaluate("!document.querySelector('.rdr').hidden && document.querySelector('.rdr').classList.contains('on')")
          r['reader_title']=await page.text_content('#rdr-h'); r['hash']=await page.evaluate('location.hash')
          r['reader_items']=await page.evaluate("document.querySelectorAll('.rdr .inside li,.rdr .inside tr').length")
          ov2=await page.evaluate("document.documentElement.scrollWidth")
          await page.screenshot(path=f'/workspace/mockme/v4-ffd-reader-{w}.png')
          await page.click('.rdr [data-go=\"1\"]'); await page.wait_for_timeout(300)
          r['next_title']=await page.text_content('#rdr-h')
          await page.keyboard.press('Escape'); await page.wait_for_timeout(500)
          r['reader_closed']=await page.evaluate("document.querySelector('.rdr').hidden")
          if w<700:
            await page.evaluate("document.getElementById('desk-grid').scrollIntoView()"); await page.evaluate("window.scrollBy(0,600)"); await page.wait_for_timeout(700)
            r['mpick']=await page.evaluate("document.querySelector('.mpick').classList.contains('on')")
            mo=await page.evaluate("(()=>{const r=document.querySelector('.mpick').getBoundingClientRect();return [Math.round(r.top),Math.round(r.height)]})()")
            r['mpick_box']=mo
            await page.screenshot(path=f'/workspace/mockme/v4-ffd-sticky-{w}.png')
          # deep link
          await page.goto(BASE+pg+'.html#nug-tax',wait_until='networkidle'); await page.wait_for_timeout(800)
          r['deeplink']=await page.evaluate("document.querySelector('.rdr').classList.contains('on')?document.getElementById('rdr-h').textContent:'no'")
          res['ffd']=r
        print(json.dumps(res))
        await ctx.close()
    await b.close()
asyncio.run(main())
