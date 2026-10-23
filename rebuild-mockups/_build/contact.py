import glob,os
from PIL import Image,ImageDraw,ImageFont
R='/workspace/fo-rebuild-mockups/shots'
names=sorted(os.path.basename(f)[:-9] for f in glob.glob(R+'/*-1440.png') if not os.path.basename(f).startswith('contact'))
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16) if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf') else ImageFont.load_default()
def sheet(w,crop,tw,cols,out):
    th=int(tw*crop/w); rows=-(-len(names)//cols)
    S=Image.new('RGB',(cols*(tw+16)+16,rows*(th+40)+16),'#F6F1EA'); d=ImageDraw.Draw(S)
    for i,n in enumerate(names):
        im=Image.open(f'{R}/{n}-{w}.png').convert('RGB'); im=im.crop((0,0,w,min(crop,im.height))).resize((tw,int(tw*min(crop,im.height)/w)))
        x=16+(i%cols)*(tw+16); y=16+(i//cols)*(th+40); S.paste(im,(x,y)); d.text((x,y+th+6),n,fill='#3a3540',font=F)
    S.save(out,optimize=True); print(out,S.size)
sheet(1440,1100,320,8,R+'/contact-1440.png')
sheet(390,1400,180,12,R+'/contact-390.png')
