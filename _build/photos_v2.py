# Builds gallery images (v2): SRC + VRBO merged, deduped (see manifest)
from PIL import Image, ImageOps
import json, glob, os
I='/workspace/real_estate/ellijay_str/img'; S='/workspace/real_estate/ellijay_str/site'
def f(k):
    if k.startswith('r'): return sorted(glob.glob(f'{I}/ryan/{k}_*.jpg'))[0]
    return glob.glob(f'{I}/src_full/{k}_*.jpg')[0] if k[0]!='v' else glob.glob(f'{I}/vrbo_full/{k}_*.jpg')[0]
RYAN=[('r1','Rosé on the deck above the river'),('r2','Evening on the deck by the river'),('r3','Candlelit dinner on the covered porch'),('r4','Stone fire pit at the river’s edge')]
RYAN=[x for x in RYAN if glob.glob(f'{I}/ryan/{x[0]}_*.jpg') and not glob.glob(f'{I}/ryan/{x[0]}_*original*')[:0]]
L=[('12','Hot tub deck over the Ellijay River'),('v24','Deck-side seat right above the river'),('06','Deck seating over the river'),
('v21','Hot tub with a river view'),('v17','Deck, porch and hot tub on the riverbank'),('v14','Riverfront setting'),('v19','Stone river wall and riverside yard'),
('v10','Fire pit between the cabin and the river'),('v01','Covered porch along the river'),('08','Rocking chairs on the covered porch'),
('09','Riverside fire pit'),('v08','The Ellijay River'),('25','The river beside the cabin'),('v20','Private hot tub on the deck'),
('v22','Porch dining'),('07','Covered porch with picnic table'),('05','Gas grill on the deck'),
('10','Living room with gas log fireplace'),('v15','Fireplace and big windows'),('11','Living room and stairs to the loft'),
('v06','Fully equipped kitchen'),('14','Coffee station'),('15','Dining nook'),('17','Media / reading room'),
('19','Main-level king bedroom'),('v16','Bedroom with dresser and TV'),('18','Upstairs loft king bedroom'),('v03','Loft king bed'),
('16','Main-level bathroom'),('20','Loft bathroom'),
('v04','Cabin and gravel drive'),('22','Cabin exterior'),('21','Cabin tucked in the trees'),('v18','Front entry'),('23','The River Solace sign'),('24','Riverside swing')]
L=RYAN+L
for d in ('img/full','img/thumb'):
    for x in glob.glob(f'{S}/{d}/rs-*'): os.remove(x)
out=[]
for i,(k,c) in enumerate(L,1):
    im=ImageOps.exif_transpose(Image.open(f(k))).convert('RGB'); n=f'rs-{i:02d}'
    a=im.copy(); a.thumbnail((1600,1600),Image.LANCZOS)
    a.save(f'{S}/img/full/{n}.jpg',quality=78,optimize=True,progressive=True); a.save(f'{S}/img/full/{n}.webp',quality=76,method=6)
    t=im.copy(); t.thumbnail((640,640),Image.LANCZOS)
    t.save(f'{S}/img/thumb/{n}.jpg',quality=72,optimize=True,progressive=True); t.save(f'{S}/img/thumb/{n}.webp',quality=70,method=6)
    out.append(dict(n=n,cap=c,w=a.width,h=a.height,tw=t.width,th=t.height,src=os.path.basename(f(k)),origin={'v':'vrbo','r':'ryan'}.get(k[0],'src')))
json.dump(out,open(f'{S}/_build/photos.json','w'),indent=1)
# hero (v17)
h=Image.open(f('v17')).convert('RGB')
h.save(f'{S}/img/hero-desktop.webp',quality=80,method=6); h.save(f'{S}/img/hero-desktop.jpg',quality=80,optimize=True,progressive=True)
m=h.crop((760,0,1440,1028)); m.save(f'{S}/img/hero-mobile.webp',quality=80,method=6); m.save(f'{S}/img/hero-mobile.jpg',quality=80,optimize=True,progressive=True)
og=ImageOps.fit(h,(1200,630),Image.LANCZOS,centering=(0.5,0.55)); og.save(f'{S}/img/og-image.jpg',quality=82,optimize=True)
print(len(out), sum(o['origin']=='vrbo' for o in out))
