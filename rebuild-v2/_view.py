import sys
from PIL import Image
# _view.py png outprefix cols chunkh scale
f,o=sys.argv[1],sys.argv[2]; cols=int(sys.argv[3]); CH=int(sys.argv[4]); sc=float(sys.argv[5])
im=Image.open(f).convert('RGB'); W,H=im.size
ch=[im.crop((0,y,W,min(H,y+CH))) for y in range(0,H,CH)]
n=0
for k in range(0,len(ch),cols):
    g=Image.new('RGB',(cols*(W+10),CH),'white')
    for i,c in enumerate(ch[k:k+cols]): g.paste(c,(i*(W+10),0))
    g=g.resize((int(g.width*sc),int(CH*sc))); g.save(f'{o}{n}.jpg',quality=80); n+=1
print(n)
