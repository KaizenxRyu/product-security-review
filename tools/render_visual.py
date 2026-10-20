"""Render the original flow poster with bundled, licensed assets. Requires Pillow 12.3.0."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'assets/source'
OUT = ROOT / 'assets/secure-product-development-flow.png'
W, H = 1600, 2000
BLUE, INK, MUTED = '#1758DF', '#101A2C', '#536277'
canvas = Image.new('RGB', (W, H), '#FAFCFF')
draw = ImageDraw.Draw(canvas)


def font(size, kind='body'):
    names = {'body':'InstrumentSans-Regular.ttf', 'bold':'InstrumentSans-Bold.ttf',
             'title':'BricolageGrotesque-Bold.ttf', 'mono':'DMMono-Regular.ttf'}
    return ImageFont.truetype(str(SRC / names[kind]), size)


def text(x, y, value, size, color=INK, kind='body', anchor=None):
    draw.text((x, y), value, font=font(size, kind), fill=color, anchor=anchor)


def illustration(name, cx, cy, size):
    img = Image.open(SRC / f'{name}.png').convert('RGBA')
    bounds = img.getbbox()
    if bounds:
        img = img.crop(bounds)
    img.thumbnail((size, size), Image.Resampling.LANCZOS)
    canvas.paste(img, (round(cx-img.width/2), round(cy-img.height/2)), img)


def halo(cx, cy, radius):
    mask = Image.new('L', canvas.size)
    ld = ImageDraw.Draw(mask)
    ld.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), fill=125)
    mask = mask.filter(ImageFilter.GaussianBlur(38))
    canvas.paste('#CFE1FF', (0,0,W,H), mask)


def arrow(points):
    draw.line(points, fill=BLUE, width=5, joint='curve')
    end, before = points[-1], points[-2]
    angle = math.atan2(end[1]-before[1], end[0]-before[0])
    head = [end] + [(end[0]-23*math.cos(angle+d), end[1]-23*math.sin(angle+d)) for d in (-.5,.5)]
    draw.polygon(head, fill=BLUE)


def step(x, y, number, label):
    draw.rounded_rectangle((x, y+3, x+57, y+60), radius=17, fill=BLUE)
    text(x+28, y+30, number, 28, '#FFFFFF', 'mono', 'mm')
    text(x+79, y+2, label, 45, kind='bold')


draw.rectangle((90,82,98,114), fill=BLUE)
text(120,78,'SECURE PRODUCT DEVELOPMENT  /  AGENT SKILL',27,BLUE,'mono')
text(88,147,'Give your AI a',95,kind='title')
text(88,254,'secure coding workflow.',88,kind='title')
text(93,381,'Apply security while planning, building and testing.',37,MUTED)

# The path is read clockwise: project, equipped agent, checks, report.
for x,y,r in [(398,720,168),(1193,720,181),(1193,1320,180),(398,1320,168)]:
    halo(x,y,r)
draw = ImageDraw.Draw(canvas)
step(113,492,'01','Your feature')
step(905,492,'02','AI + the skill')
illustration('desktop_computer',398,740,305)
illustration('robot',1193,727,298)
illustration('open_book',1310,824,126)
text(398,934,'Requirements + project context',32,MUTED,anchor='mm')
text(1193,934,'Boundaries • secure defaults',32,MUTED,anchor='mm')
arrow([(662,730),(907,730)])
text(785,688,'APPLY',23,BLUE,'mono','mm')
arrow([(1461,810),(1461,1115),(1390,1170)])

step(901,1066,'03','Build securely')
step(113,1066,'04','Verify + hand off')
illustration('shield',1193,1320,310)
illustration('clipboard',398,1320,306)
arrow([(906,1316),(664,1316)])
text(785,1270,'VERIFY',23,BLUE,'mono','mm')
text(1193,1527,'Access · data · inputs',34,MUTED,anchor='mm')
text(1193,1575,'Controls in the real code path',31,MUTED,anchor='mm')
text(398,1527,'Working code + relevant tests',32,MUTED,anchor='mm')
text(398,1575,'Actual results · honest limits',31,MUTED,anchor='mm')

draw.line((94,1685,1506,1685), fill='#D9E3F2', width=2)
text(93,1722,'Security belongs in the way we build.',53,kind='bold')
text(95,1812,'A development workflow, not a security guarantee.',32,MUTED)
text(95,1856,'No new permissions, tools or model training.',32,MUTED)
text(94,1943,'RAHUL CHAMOLI  /  KAIZEN-RYU',25,BLUE,'mono')
text(1505,1943,'MICROSOFT FLUENT ARTWORK · MIT',18,MUTED,'mono','ra')
OUT.parent.mkdir(exist_ok=True, parents=True)
canvas.save(OUT, optimize=True)
canvas.resize((600,750),Image.Resampling.LANCZOS).save(ROOT / '.work/flow-mobile-preview.png')
print(OUT)
