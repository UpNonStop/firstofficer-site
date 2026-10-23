from PIL import Image, ImageDraw, ImageFont
import sys
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',34)
def sheet(out, cols, W=620, maxh=7000):
    ims=[]
    for lab,p in cols:
        im=Image.open(p).convert('RGB'); s=W/im.width; im=im.resize((W,int(im.height*s)))
        ims.append((lab,im.crop((0,0,W,min(im.height,maxh)))))
    H=max(i.height for _,i in ims)+80; S=Image.new('RGB',(len(ims)*(W+30)+30,H+30),'#eeeae3'); d=ImageDraw.Draw(S)
    for k,(lab,i) in enumerate(ims):
        x=30+k*(W+30); d.text((x,22),lab,font=F,fill='#141216'); S.paste(i,(x,80))
    S.save(out,quality=82); print(out,S.size)
R='_shots/ref/'; V1='/workspace/fo-rebuild-mockups/shots/'; V2='_shots/v2/'
for name,live,v1,v2 in [('home','live-index','home','home'),('book','live-book','book','book'),('for-dental','live-for-dental','for-dental','dental')]:
    v1d=(R+'v1-home-1440-full.png' if name=='home' else V1+v1+'-1440.png')
    v1m=(R+'v1-home-390-full.png' if name=='home' else V1+v1+'-390.png')
    sheet(f'_shots/compare-{name}-1440.jpg',[('LIVE',R+live+'-1440-full.png'),('V1',v1d),('V2',V2+v2+'-1440-full.png')],620,9000)
    sheet(f'_shots/compare-{name}-390.jpg',[('LIVE',R+live+'-390-full.png'),('V1',v1m),('V2',V2+v2+'-390-full.png')],390,16000)
