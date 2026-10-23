"""Approximate AA audit: text colour vs rendered background pixels in each text's tight box (glyph pixels excluded by distance from the text colour)."""
import asyncio,sys,json,io
from playwright.async_api import async_playwright
from PIL import Image
import numpy as np
def lum(c):
    c=np.asarray(c,dtype=float)/255;c=np.where(c<=.03928,c/12.92,((c+.055)/1.055)**2.4);return c@[.2126,.7152,.0722]
JS='''()=>{const out=[];const W=innerWidth;
document.querySelectorAll('body *').forEach(e=>{if(e.closest('.mcta,header,#fohero,svg,.fsp,.focap .phx'))return;
 let t='';for(const n of e.childNodes)if(n.nodeType===3)t+=n.textContent;t=t.trim();if(!t)return;
 const s=getComputedStyle(e);if(s.visibility==='hidden')return;let op=1;for(let a=e;a;a=a.parentElement)op*=+getComputedStyle(a).opacity;if(op<.6)return;if(e.closest('.tick,.ticker,[aria-hidden=true]'))return;let r=null;for(const n of e.childNodes)if(n.nodeType===3&&n.textContent.trim()){const g=document.createRange();g.selectNodeContents(n);for(const q of g.getClientRects()){if(q.width<2)continue;if(!r)r={left:q.left,top:q.top,right:q.right,bottom:q.bottom};else{r.left=Math.min(r.left,q.left);r.top=Math.min(r.top,q.top);r.right=Math.max(r.right,q.right);r.bottom=Math.max(r.bottom,q.bottom)}}}if(!r)return;r.width=r.right-r.left;r.height=r.bottom-r.top;if(r.width<2||r.height<2)return;
 const m=s.color.match(/[\\d.]+/g).map(Number);if(m.length>3&&m[3]<.5)return;
 out.push({t:t.slice(0,50),c:m.slice(0,3),x:r.left+scrollX,y:r.top+scrollY,w:r.width,h:r.height,fs:parseFloat(s.fontSize),fw:+s.fontWeight,ps:!!e.closest('.ps')})});return out}'''
async def main(url,tag,w):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        c=await b.new_context(viewport={'width':w,'height':900});pg=await c.new_page()
        await pg.goto(url,wait_until='load');H=await pg.evaluate('document.body.scrollHeight')
        for y in range(0,H,700):await pg.evaluate(f'scrollTo(0,{y})');await pg.wait_for_timeout(120)
        await pg.evaluate('scrollTo(0,0)');await pg.wait_for_timeout(1500)
        await pg.add_style_tag(content='.mcta,header.fonav{display:none!important}html.ctx *{color:transparent!important;text-shadow:none!important;-webkit-text-fill-color:transparent!important}')
        H=await pg.evaluate('document.documentElement.scrollHeight');VH=900 if w>800 else 844;y=0;fails=[];n=0;seen=set()
        while y<H:
            await pg.evaluate(f'scrollTo(0,{y})');await pg.wait_for_timeout(500)
            els=await pg.evaluate(JS);sy=await pg.evaluate('scrollY')
            im=np.asarray(Image.open(io.BytesIO(await pg.screenshot())).convert('RGB'))
            for e in els:
                x0=int(e['x']);y0=int(e['y']-sy);x1=int(e['x']+e['w']);y1=int(e['y']-sy+e['h'])
                if y0<0 or y1>VH or x0<0 or x1>im.shape[1]:continue
                k=(e['t'],int(e['y']))
                if k in seen:continue
                seen.add(k);n+=1
                dx=int((x1-x0)*.12);dy=int((y1-y0)*.22);x0+=dx;x1-=dx;y0+=dy;y1-=dy
                if x1<=x0+1 or y1<=y0+1:continue
                px=im[y0:y1,x0:x1].reshape(-1,3);L=lum(px);lt=lum(e['c'])
                # text is visible: background = pixels away from the text colour; take the 15th worst of those
                cr_px=(np.maximum(L,lt)+.05)/(np.minimum(L,lt)+.05);bg=L[cr_px>=1.6]
                if bg.size<20:continue
                worst=np.percentile(bg,15) if lt<.2 else np.percentile(bg,85)
                cr=(max(worst,lt)+.05)/(min(worst,lt)+.05)
                big=e['fs']>=24 or (e['fs']>=18.6 and e['fw']>=700);need=3 if big else 4.5
                if cr<need:fails.append((round(float(cr),2),need,e['t'],e['fs'],e['ps'],int(e['y'])))
            y+=VH-200
        await b.close()
    els=range(n)
    print(tag,'elements',len(els),'fails',len(fails))
    for f in sorted(fails)[:40]:print('  ',f)
asyncio.run(main(sys.argv[1],sys.argv[2],int(sys.argv[3])))
