import sys
from PIL import Image
# usage: view.py in.png out.png [cols] [maxw]
im=Image.open(sys.argv[1]).convert('RGB'); cols=int(sys.argv[3]) if len(sys.argv)>3 else 3; maxw=int(sys.argv[4]) if len(sys.argv)>4 else 1800
W,Hh=im.size; seg=-(-Hh//cols)
sheet=Image.new('RGB',(W*cols+20*(cols-1),seg),'#888')
for i in range(cols):
    sheet.paste(im.crop((0,i*seg,W,min(Hh,(i+1)*seg))),(i*(W+20),0))
s=maxw/sheet.width
if s<1: sheet=sheet.resize((maxw,int(sheet.height*s)),Image.LANCZOS)
sheet.save(sys.argv[2]); print(sheet.size)
