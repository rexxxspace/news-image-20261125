#!/usr/bin/env python3
"""News Image entry - 'The World in One Page', Wednesday 25 November 2026.

Written for the make.fun news-image-20261125 competition. The design keeps
the newspaper system that scored best in the previous day's teardown:
a giant serif date masthead, a big-numbers strip, a region bar, three
illustrated lead cards, nine story cards, a pinned world map, an
18-story 'also' index and a DATE CHECK box naming the older stories
that were deliberately left out.

Date discipline is the point of this edition: every story below happened
or was first reported on Wednesday 25 November 2026, checked the same
morning against Reuters, AP, AFP, NOS, Antara, Bernama and PANA items
carrying a 25 November 2026 dateline or publication stamp.

Revision note (submission pass): the markets lead card originally drew
its "TAIEX -6% · KOSPI -5.6%" caption straight over the falling chart
line, where the two reds collided and the text turned unreadable at
thumbnail size. The caption now sits clear of the line as a short
"SELL-OFF" tag in the card's top-right corner, and the exact index
numbers live in the headline and body copy underneath the chart,
where nothing crosses them.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 242, 227)
INK = (22, 34, 54)
NAVY = (20, 38, 76)
RED = (176, 48, 38)
TEAL = (24, 105, 88)
GOLD = (176, 116, 20)
GREY = (105, 100, 88)
CARD = (255, 253, 246)
LINE = (196, 188, 164)
PURPLE = (110, 70, 130)
BROWN = (140, 100, 40)

F_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
F_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
F_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def tw(text, font):
    return d.textlength(text, font=font)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(t, font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def block(x, y, text, font, maxw, leading, color=INK, max_lines=None):
    lines = wrap(text, font, maxw)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=font, fill=color)
        y += leading
    return y


def badge(x, y, n, color=NAVY, r=11):
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=color)
    f = F(F_BLACK, 12)
    s = str(n)
    d.text((x + r - tw(s, f) / 2, y + r - 8), s, font=f, fill=(255, 255, 255))


# ---------------------------------------------------------------- top strip
f = F(F_BOLD, 13)
d.text((16, 10), "THE WORLD IN ONE PAGE", font=f, fill=INK)
r = "30 STORIES · 7 REGIONS · EVERY ONE FROM WEDNESDAY 25 NOV 2026"
d.text((W - 16 - tw(r, f), 10), r, font=f, fill=INK)
d.line([16, 32, W - 16, 32], fill=INK, width=2)

# ---------------------------------------------------------------- masthead
f = F(F_SERIF, 54)
t = "Wednesday 25 November 2026"
d.text(((W - tw(t, f)) / 2, 40), t, font=f, fill=INK)
d.line([16, 106, W - 16, 106], fill=RED, width=3)
f = F(F_BOLD, 14.5)
t = "Coalition bombs Hodeidah after Riyadh strike   •   Dozens trapped in a Java mine   •   Asia's chip rally reverses"
d.text(((W - tw(t, f)) / 2, 112), t, font=f, fill=(120, 32, 24))

# ---------------------------------------------------------------- numbers strip
nums = [
    ("11", "INJURED IN HOOTHI\nSTRIKE ON RIYADH"),
    ("~30", "MINERS TRAPPED 100M\nDOWN IN WEST JAVA"),
    ("$7.4BN", "XIAMEN AIRLINES ORDERS\n50 BOEING 737-8 JETS"),
    ("15,164", "INDONESIANS IN OVERSEAS\nSCAM CASES THIS YEAR"),
    ("-20%", "GLOBAL HIV FUNDING\nIN A SINGLE YEAR"),
    ("18,290", "RUPIAH'S RECORD LOW\nPER US DOLLAR"),
]
x = 16
cw = (W - 32) / 6
for i, (big, lab) in enumerate(nums):
    cx = x + i * cw
    fb = F(F_BLACK, 27)
    d.text((cx + (cw - tw(big, fb)) / 2, 136), big, font=fb, fill=NAVY)
    fl = F(F_BOLD, 9.5)
    yy = 170
    for ln in lab.split("\n"):
        d.text((cx + (cw - tw(ln, fl)) / 2, yy), ln, font=fl, fill=GREY)
        yy += 12
    if i:
        d.line([cx, 140, cx, 190], fill=LINE, width=1)
d.line([16, 196, W - 16, 196], fill=INK, width=2)

# ---------------------------------------------------------------- region bar
regions = [("EUROPE 5", (58, 92, 140)), ("ASIA 6", TEAL),
           ("SE ASIA 5", GOLD), ("M. EAST 3", RED),
           ("AMERICAS 4", (150, 60, 90)), ("AFRICA 4", BROWN),
           ("OCEANIA 3", PURPLE)]
total = 30
x = 16
counts = [5, 6, 5, 3, 4, 4, 3]
for (lab, col), c in zip(regions, counts):
    wseg = (W - 32) * c / total
    d.rectangle([x, 202, x + wseg - 2, 224], fill=col)
    fl = F(F_BOLD, 11)
    if wseg > 62:
        d.text((x + (wseg - tw(lab, fl)) / 2, 207), lab, font=fl, fill=(255, 255, 255))
    x += wseg

# ---------------------------------------------------------------- lead cards
leads = [
    dict(n=1, tag="MIDDLE EAST · WAR", color=RED, ill="port",
         head="Coalition strikes Hodeidah port",
         body="Saudi-led jets bomb Yemen's Hodeidah port early Wednesday, hours after a Houthi strike on a Riyadh tower injured 11 people.",
         src="REPORTED — Arab News · Reuters"),
    dict(n=2, tag="SE ASIA · RESCUE", color=GOLD, ill="mine",
         head="Dozens trapped in Java gold mine",
         body="Rescuers search Wednesday for about 30 workers stuck 100m down a flooded, unauthorised mine at Pongkor, Bogor, since Monday's rains.",
         src="CONFIRMED — Reuters · Basarnas"),
    dict(n=3, tag="ASIA · MARKETS", color=TEAL, ill="chart",
         head="Chip rally reverses: Taiex -6%",
         body="Wednesday's Asian sell-off undoes Tuesday's record surge: Taiex down over 6%, Kospi -5.6%, Nikkei -3.6% as AI confidence cracks.",
         src="CONFIRMED — AP · Reuters"),
]
LX, LY, LW, LH, GAP = 16, 232, 325, 238, 9
for i, L in enumerate(leads):
    x = LX + i * (LW + GAP)
    d.rectangle([x, LY, x + LW, LY + LH], fill=CARD, outline=LINE, width=1)
    d.rectangle([x, LY, x + LW, LY + 26], fill=L["color"])
    ft = F(F_BOLD, 12.5)
    d.text((x + 10, LY + 6), L["tag"], font=ft, fill=(255, 255, 255))
    d.ellipse([x + LW - 28, LY + 2, x + LW - 6, LY + 24], fill=(255, 255, 255))
    fb = F(F_BLACK, 12)
    s = str(L["n"])
    d.text((x + LW - 17 - tw(s, fb) / 2, LY + 6), s, font=fb, fill=L["color"])
    iy = LY + 34
    if L["ill"] == "port":
        d.rectangle([x + 8, iy, x + LW - 8, iy + 82], fill=(238, 220, 200))
        d.polygon([(x + 50, iy + 60), (x + 210, iy + 60), (x + 192, iy + 74), (x + 68, iy + 74)], fill=INK)
        d.rectangle([x + 86, iy + 46, x + 174, iy + 60], fill=INK)
        for k in range(3):
            d.line([x + 236 + k * 22, iy + 58, x + 244 + k * 22, iy + 22], fill=RED, width=3)
            d.ellipse([x + 238 + k * 22, iy + 12, x + 250 + k * 22, iy + 24], fill=RED)
        fl = F(F_BLACK, 13)
        d.text((x + 16, iy + 6), "RIYADH HIT · 11 HURT", font=fl, fill=RED)
    elif L["ill"] == "mine":
        d.rectangle([x + 8, iy, x + LW - 8, iy + 82], fill=(226, 216, 196))
        d.polygon([(x + 30, iy + 82), (x + 130, iy + 18), (x + 230, iy + 82)], fill=(120, 100, 70))
        d.polygon([(x + 118, iy + 82), (x + 130, iy + 52), (x + 142, iy + 82)], fill=(30, 26, 20))
        for k in range(4):
            d.line([x + 236 + k * 16, iy + 30, x + 236 + k * 16, iy + 52], fill=(90, 130, 170), width=3)
        fl = F(F_BLACK, 13)
        d.text((x + 16, iy + 6), "100M DOWN · FLOODED", font=fl, fill=NAVY)
    else:
        d.rectangle([x + 8, iy, x + LW - 8, iy + 82], fill=(240, 222, 218))
        pts = [(x + 24, iy + 14), (x + 90, iy + 22), (x + 150, iy + 20),
               (x + 210, iy + 44), (x + 268, iy + 58), (x + 296, iy + 70)]
        d.line(pts, fill=RED, width=4)
        for px, py in pts:
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED)
        fl = F(F_BLACK, 13)
        d.text((x + 200, iy + 6), "SELL-OFF", font=fl, fill=RED)
    fh = F(F_BLACK, 19)
    yy = block(x + 10, iy + 90, L["head"], fh, LW - 20, 23, max_lines=2)
    fbd = F(F_REG, 12)
    yy = block(x + 10, yy + 2, L["body"], fbd, LW - 20, 15.5, max_lines=3)
    fs = F(F_BOLD, 10)
    d.text((x + 10, LY + LH - 17), L["src"], font=fs, fill=GREY)

# ---------------------------------------------------------------- mid cards
cards = [
    dict(n=4, tag="EUROPE · CLIMATE LAW", color=NAVY,
         head="Dutch climate targets stay binding",
         body="The Hague appeal court refuses to suspend the targets: they must be law by 28 July 2027."),
    dict(n=5, tag="EUROPE · WAR", color=RED,
         head="Putin vows retaliation over refineries",
         body="Kyiv's strikes have cut Russian refinery processing about 45% since late October, Putin tells the Kremlin."),
    dict(n=6, tag="EUROPE · TALKS", color=NAVY,
         head="Kremlin: no seat for Europe at talks",
         body="Aide Ushakov says the next Russia-US-Ukraine round will not invite European representatives."),
    dict(n=7, tag="AMERICAS · NATO", color=RED,
         head="Trump meets NATO chief Rutte",
         body="The NATO secretary general visits Mar-a-Lago on Wednesday amid fights over Ukraine security guarantees."),
    dict(n=8, tag="AMERICAS · TRADE", color=NAVY,
         head="US weighs tariffs on 16 partners",
         body="The USTR probe into 'excess capacity' in China, the EU, India and 13 others nears release; new duties loom."),
    dict(n=9, tag="AMERICAS · CRIME", color=RED,
         head="25 held hostage in Cartagena shop",
         body="Armed men seize 25 hostages in a supermarket after a failed armoured-van robbery in Colombia."),
    dict(n=10, tag="ASIA · AVIATION", color=TEAL,
         head="Xiamen Air orders 50 Boeing jets",
         body="The China Southern unit agrees to buy 50 737-8s for about $7.4bn - Boeing's first big China order in a decade."),
    dict(n=11, tag="SE ASIA · POLITICS", color=GOLD,
         head="Indonesia's vice-president resigns",
         body="Gibran Rakabuming Raka steps down, opening an 11 December vote to fill the vacant vice-presidency."),
    dict(n=12, tag="OCEANIA · APOLOGY", color=PURPLE,
         head="Australia apologises to LGBTQ veterans",
         body="Canberra formally apologises Wednesday for decades of discriminatory military policies, Marles tells parliament."),
]
MX, MY, MW, MH = 16, 480, 325, 88
for idx, C in enumerate(cards):
    cx = MX + (idx % 3) * (MW + GAP)
    cy = MY + (idx // 3) * (MH + 8)
    d.rectangle([cx, cy, cx + MW, cy + MH], fill=CARD, outline=LINE, width=1)
    d.rectangle([cx, cy, cx + MW, cy + 4], fill=C["color"])
    badge(cx + 8, cy + 10, C["n"], color=C["color"], r=10)
    ft = F(F_BOLD, 10.5)
    d.text((cx + 34, cy + 11), C["tag"], font=ft, fill=C["color"])
    fh = F(F_BLACK, 14.5)
    yy = block(cx + 10, cy + 28, C["head"], fh, MW - 20, 17, max_lines=1)
    fb = F(F_REG, 11)
    block(cx + 10, cy + 50, C["body"], fb, MW - 20, 13.5, max_lines=2)

# ---------------------------------------------------------------- bottom: map + also list
BY = 772
d.rectangle([16, BY, 492, 946], fill=CARD, outline=LINE, width=1)
fh = F(F_BLACK, 13)
d.text((26, BY + 8), "WHERE IT HAPPENED", font=fh, fill=INK)
fs = F(F_REG, 10)
d.text((196, BY + 11), "pins carry the story numbers", font=fs, fill=GREY)

MAP = [
    "                                                                        ",
    "        #####                                                           ",
    "      #########        #     ####################################       ",
    "     ###########     #####  ######################################      ",
    "      ##########      ##    ################  ##################        ",
    "       ########              ##############    ################         ",
    "        ######    ##          ############      ##############          ",
    "         ####   ######         #########         ############           ",
    "          ##  ########          #######           ##########            ",
    "               ########          #####             ########             ",
    "                ######            ###     ##        ######   #          ",
    "                #####            ####    ####        ####   ###         ",
    "                 ###              ##      ##          ##     #          ",
    "                 ##                                                     ",
    "                 #                         ##                           ",
    "                                            ##      ########            ",
    "                                             #     ##########           ",
    "                                                    ########            ",
]
MX0, MY0, CELL = 26, BY + 34, 6.4
for ri, row in enumerate(MAP):
    for ci, ch in enumerate(row):
        if ch == "#":
            cx = MX0 + ci * CELL
            cyy = MY0 + ri * CELL
            d.ellipse([cx, cyy, cx + 3.4, cyy + 3.4], fill=(178, 168, 138))
PINS = {1: (44, 9), 2: (56, 12), 3: (58, 9), 4: (35, 4), 5: (40, 5),
        6: (41, 4), 7: (14, 8), 8: (15, 7), 9: (17, 12),
        10: (57, 8), 11: (55, 13), 12: (66, 16)}
for n, (ci, ri) in PINS.items():
    cx = MX0 + ci * CELL
    cyy = MY0 + ri * CELL
    d.ellipse([cx - 6, cyy - 6, cx + 8, cyy + 8], fill=RED)
    fb = F(F_BLACK, 8)
    s = str(n)
    d.text((cx + 1 - tw(s, fb) / 2, cyy - 3.5), s, font=fb, fill=(255, 255, 255))

AX = 508
d.rectangle([AX, BY, W - 16, 946], fill=CARD, outline=LINE, width=1)
fh = F(F_BLACK, 13)
d.text((AX + 10, BY + 8), "ALSO ON WEDNESDAY - 18 MORE STORIES", font=fh, fill=INK)
also = [
    "Drone strikes near Samara refineries",
    "Iran's rial hits a record low",
    "US embassy Doha issues alert",
    "Shanghai party chief faces graft probe",
    "N. Korea expels Swiss diplomat",
    "India pledges $1.6bn to Nepal",
    "Suryavanshi, 15, hits 204 off 53",
    "BI sees 2027 rate at 6%",
    "72 orangutans saved from fires",
    "UNAIDS: HIV rebound risk in 2027",
    "Nollywood's Pete Edochie dies, 79",
    "Togo vaccination reaches 90%",
    "Nigeria court freezes N135.6bn",
    "Solomons-Australia pact signed",
    "Australia CPI: trimmed mean 3.8%",
    "Oil slips: Brent $90.97, WTI $81.58",
    "Bitcoin falls 1% to $59,258",
    "Citi weighs a return to Venezuela",
]
colw = (W - 16 - AX - 30) / 2
fb = F(F_REG, 10)
fn = F(F_BLACK, 10)
for i, s in enumerate(also):
    cx = AX + 10 + (i // 9) * (colw + 10)
    cy = BY + 32 + (i % 9) * 15.5
    num = f"{13 + i}"
    d.text((cx, cy), num, font=fn, fill=RED)
    block(cx + 20, cy, s, fb, colw - 22, 12, max_lines=1)

# ---------------------------------------------------------------- date check + footer
d.rectangle([16, 954, W - 16, 988], outline=RED, width=2)
fd = F(F_BOLD, 10.5)
d.text((24, 960), "DATE CHECK", font=fd, fill=RED)
txt = ("Left out as other days' news: Nvidia reinstates Huang and Asia's record chip surge (Mon 23-Tue 24 Nov) - only Wednesday's reversal and board scrutiny count - "
       "Ukraine's Libya ship strike (22-24 Nov), Senegal restored as AFCON champions (Tue 24 Nov), the Hanoi restaurant blast (Tue 24 Nov).")
block(104, 960, txt, F(F_REG, 10.5), W - 130, 13, max_lines=2)
ff = F(F_REG, 9.5)
t = "Every story here happened, or was first reported, on Wednesday 25 November 2026, as the named outlets reported it. Maps and drawings are original vector art."
d.text(((W - tw(t, ff)) / 2, 996), t, font=ff, fill=GREY)

img.save("/home/hatch/workspace/makefun/news-image-20261125/entry.png")
img.resize((300, 300), Image.LANCZOS).save("/home/hatch/workspace/makefun/news-image-20261125/entry-300px.png")
print("saved entry for 25 Nov")
