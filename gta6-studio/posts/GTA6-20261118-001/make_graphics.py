"""Original 1080x1920 background graphics for GTA6-20261118-001 (news-explainer).
Content zone: x 80..950, y 160..1060 (captions sit ~y1100-1300, platform UI bottom/right)."""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
PID = "GTA6-20261118-001"
W, H = 1080, 1920
BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
SEMI = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
if not os.path.exists(SEMI):
    SEMI = BOLD
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

BG_TOP = (10, 14, 28)
BG_BOT = (34, 14, 48)
PINK = (255, 64, 129)
TEAL = (34, 211, 238)
WHITE = (240, 244, 250)
GREY = (110, 118, 140)
DIM = (52, 58, 80)
GREEN = (52, 211, 120)
RED = (244, 63, 94)
CX = 515  # centre of the safe content zone (80..950)


def font(path, size):
    return ImageFont.truetype(path, size)


def base():
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    # subtle grid lines for texture
    img = img.convert("RGBA")
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for x in range(0, W, 90):
        od.line([(x, 0), (x, H)], fill=(255, 255, 255, 10), width=1)
    for y in range(0, H, 90):
        od.line([(0, y), (W, y)], fill=(255, 255, 255, 10), width=1)
    # soft glow behind content area
    for r in range(420, 0, -6):
        a = int(26 * (1 - r / 420))
        od.ellipse([CX - r, 610 - r, CX + r, 610 + r], fill=(PINK[0], PINK[1], PINK[2], a))
    img = Image.alpha_composite(img, ov)
    return img


def text_c(d, xy, s, f, fill, anchor="mm"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)


def clock(d, cx, cy, r, hh, mm, ring=TEAL, face=(18, 22, 40), hand=WHITE, width=None, ticks=True):
    width = width or max(4, r // 14)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=face, outline=ring, width=width)
    if ticks:
        for i in range(12):
            a = math.radians(i * 30)
            r1 = r * (0.78 if i % 3 == 0 else 0.85)
            r2 = r * 0.92
            d.line([(cx + r1 * math.sin(a), cy - r1 * math.cos(a)),
                    (cx + r2 * math.sin(a), cy - r2 * math.cos(a))],
                   fill=ring if i % 3 == 0 else GREY, width=max(2, width // 2))
    ha = math.radians((hh % 12) * 30 + mm * 0.5)
    ma = math.radians(mm * 6)
    d.line([(cx, cy), (cx + r * 0.5 * math.sin(ha), cy - r * 0.5 * math.cos(ha))], fill=hand, width=max(4, r // 10))
    d.line([(cx, cy), (cx + r * 0.75 * math.sin(ma), cy - r * 0.75 * math.cos(ma))], fill=hand, width=max(3, r // 16))
    d.ellipse([cx - r // 12, cy - r // 12, cx + r // 12, cy + r // 12], fill=PINK)


def pill(d, box, fill, outline=None, width=4, radius=None):
    x0, y0, x1, y1 = box
    radius = radius if radius is not None else (y1 - y0) // 2
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def badge(d, cx, cy, label, size=90, fg=WHITE, border=WHITE, fill=None):
    f = font(BOLD, size)
    bb = d.textbbox((0, 0), label, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    pad_x, pad_y = int(size * 0.45), int(size * 0.3)
    box = [cx - w // 2 - pad_x, cy - h // 2 - pad_y, cx + w // 2 + pad_x, cy + h // 2 + pad_y]
    d.rounded_rectangle(box, radius=int(size * 0.3), fill=fill, outline=border, width=6)
    text_c(d, (cx, cy), label, f, fg)
    return box


def save(img, name):
    p = os.path.join(OUT, f"{PID}_{name}.png")
    img.convert("RGB").save(p)
    print(p)


# 00 reusable plain background
save(base(), "00_bg_dark")

# 01 hook: big clock with question mark + plain-text PS5 badge
img = base(); d = ImageDraw.Draw(img)
clock(d, CX, 560, 330, 10, 50, ring=PINK, width=18)
d.ellipse([CX - 330, 230, CX + 330, 890], outline=None)
# question mark bubble
pill(d, [CX + 150, 230, CX + 330, 410], fill=TEAL, radius=90)
text_c(d, (CX + 240, 318), "?", font(BOLD, 140), BG_TOP)
badge(d, CX, 990, "PS5", size=96, border=TEAL, fill=(18, 22, 40))
save(img, "01_hook_clock_ps5")

# 02 world clock strip: same instant, different local times (unlabelled, illustrative)
def strip(img, highlighted, nz_label=True, times=None, arrow=True, title_y=None):
    d = ImageDraw.Draw(img)
    n = 5
    xs = [CX - 2 * 170 + i * 170 for i in range(n)]
    cy = 560
    # band
    pill(d, [xs[0] - 95, cy - 115, xs[-1] + 95, cy + 115], fill=(16, 20, 38), outline=DIM, width=3, radius=40)
    for i, x in enumerate(xs):
        on = i in highlighted
        if times:
            hh, mm = times[i]
        else:
            hh, mm = (0, 0) if on else (8, 0)
        if on:
            for r in range(92, 72, -4):
                d.ellipse([x - r, cy - r, x + r, cy + r], outline=(PINK[0], PINK[1], PINK[2]), width=1)
        clock(d, x, cy, 68, hh, mm, ring=PINK if on else (TEAL if times else GREY),
              hand=WHITE if (on or times) else GREY, width=7)
        if on:
            text_c(d, (x, cy + 150), "00:00", font(MONO, 36), PINK)
    if nz_label:
        pill(d, [xs[0] - 55, cy - 225, xs[0] + 55, cy - 165], fill=PINK if 0 in highlighted else DIM, radius=20)
        text_c(d, (xs[0], cy - 195), "NZ", font(BOLD, 40), WHITE)
    if arrow:
        y = cy + 260
        d.line([(xs[0], y), (xs[-1] - 30, y)], fill=TEAL, width=8)
        d.polygon([(xs[-1] + 10, y), (xs[-1] - 40, y - 28), (xs[-1] - 40, y + 28)], fill=TEAL)
        text_c(d, (CX, y + 55), "WESTWARD", font(SEMI, 36), TEAL)
    return d

# same instant, different local times: 00:00, 20:00, 11:00, 06:00, 03:00 (illustrative offsets)
img = base(); d = strip(img, highlighted=[], nz_label=False, times=[(0, 0), (8, 0), (11, 0), (6, 0), (3, 0)], arrow=False)
# horizontal "time" waves to suggest rolling
for k in range(3):
    y = 860 + k * 50
    pts = [(x, y + 18 * math.sin((x + k * 60) / 70)) for x in range(110, 930, 6)]
    d.line(pts, fill=(TEAL[0], TEAL[1], TEAL[2]), width=4 - k)
save(img, "02_world_clocks")

# 03 calendar page 19 NOV 2026
img = base(); d = ImageDraw.Draw(img)
x0, y0, x1, y1 = CX - 280, 230, CX + 280, 920
d.rounded_rectangle([x0 + 14, y0 + 18, x1 + 14, y1 + 18], radius=40, fill=(5, 6, 14))
d.rounded_rectangle([x0, y0, x1, y1], radius=40, fill=WHITE)
d.rounded_rectangle([x0, y0, x1, y0 + 170], radius=40, fill=PINK)
d.rectangle([x0, y0 + 120, x1, y0 + 170], fill=PINK)
text_c(d, (CX, y0 + 88), "NOV", font(BOLD, 100), WHITE)
for rx in (x0 + 120, x1 - 120):
    d.rounded_rectangle([rx - 16, y0 - 40, rx + 16, y0 + 40], radius=14, fill=GREY)
text_c(d, (CX, y0 + 400), "19", font(BOLD, 330), BG_TOP)
text_c(d, (CX, y1 - 85), "2026", font(SEMI, 80), (90, 96, 120))
save(img, "03_calendar_19nov")

# 04 midnight clock + PS5 badge
img = base(); d = ImageDraw.Draw(img)
clock(d, CX, 520, 300, 0, 0, ring=PINK, width=18)
pill(d, [CX - 220, 870, CX + 220, 990], fill=(18, 22, 40), outline=TEAL, width=5, radius=28)
text_c(d, (CX, 930), "00:00", font(MONO, 96), TEAL)
badge(d, CX, 190, "PS5", size=64, border=WHITE, fill=None)
save(img, "04_clock_midnight")

# 05 / 07 sweep frames
for name, hl in [("05a_sweep_nz", [0]), ("05b_sweep_2", [0, 1]), ("07a_sweep_3", [0, 1, 2]),
                 ("07b_sweep_4", [0, 1, 2, 3]), ("07c_sweep_all", [0, 1, 2, 3, 4])]:
    img = base(); strip(img, highlighted=hl)
    save(img, name)

# 06 NZ vs UK conversion with permanent OUR CONVERSION tag
img = base(); d = ImageDraw.Draw(img)
for cx, lab, hh, tm, date, col in [(CX - 210, "NZ", 0, "00:00", "19 NOV", PINK), (CX + 210, "UK", 11, "11:00", "18 NOV", TEAL)]:
    pill(d, [cx - 50, 330, cx + 50, 390], fill=col, radius=20)
    text_c(d, (cx, 360), lab, font(BOLD, 40), WHITE)
    clock(d, cx, 560, 150, hh, 0, ring=col, width=10)
    text_c(d, (cx, 775), tm, font(MONO, 80), WHITE)
    text_c(d, (cx, 850), date, font(SEMI, 48), col)
text_c(d, (CX, 560), "=", font(BOLD, 110), WHITE)
pill(d, [CX - 330, 190, CX + 330, 270], fill=(250, 204, 21), radius=20)
text_c(d, (CX, 230), "OUR CONVERSION", font(BOLD, 48), BG_TOP)
text_c(d, (CX, 960), "not an official time", font(SEMI, 40), (250, 204, 21))
save(img, "06_nz_uk_conversion")

# 08 several time zones -> check support: three small clocks + info icon
img = base(); d = ImageDraw.Draw(img)
for i, (hh, x) in enumerate([(0, CX - 220), (1, CX), (2, CX + 220)]):
    clock(d, x, 470, 95, 11 + i, 0, ring=TEAL if i else PINK, width=8)
d.ellipse([CX - 120, 650, CX + 120, 890], fill=(18, 22, 40), outline=WHITE, width=10)
text_c(d, (CX, 770), "i", font(BOLD, 170), WHITE)
save(img, "08_timezones_info")

# 09 PS4 struck through, PS5 ticked
img = base(); d = ImageDraw.Draw(img)
b = badge(d, CX, 400, "PS4", size=130, fg=GREY, border=GREY, fill=(18, 22, 40))
d.line([(b[0] - 20, b[3] + 20), (b[2] + 20, b[1] - 20)], fill=RED, width=22)
b2 = badge(d, CX - 50, 790, "PS5", size=110, fg=WHITE, border=GREEN, fill=(18, 22, 40))
# check mark
cx, cy = b2[2] + 80, 790
d.ellipse([cx - 55, cy - 55, cx + 55, cy + 55], fill=GREEN)
d.line([(cx - 28, cy + 2), (cx - 6, cy + 26), (cx + 30, cy - 22)], fill=WHITE, width=14, joint="curve")
save(img, "09_not_ps4")

# 10 download bar (generic, not console UI)
img = base(); d = ImageDraw.Draw(img)
d.ellipse([CX - 170, 230, CX + 170, 570], fill=(18, 22, 40), outline=TEAL, width=10)
d.rectangle([CX - 30, 300, CX + 30, 430], fill=TEAL)
d.polygon([(CX - 85, 420), (CX + 85, 420), (CX, 505)], fill=TEAL)
d.rounded_rectangle([CX - 100, 515, CX + 100, 530], radius=6, fill=TEAL)
pill(d, [120, 680, 910, 750], fill=(18, 22, 40), outline=DIM, width=4)
pill(d, [128, 688, 902, 742], fill=TEAL)
text_c(d, (CX, 820), "100%", font(MONO, 64), TEAL)
pill(d, [CX - 150, 900, CX + 150, 980], fill=PINK, radius=24)
text_c(d, (CX, 940), "10 NOV", font(BOLD, 52), WHITE)
save(img, "10_download_bar")

# 11 storage bar 212GB minimum
img = base(); d = ImageDraw.Draw(img)
# simple drive icon
d.rounded_rectangle([CX - 200, 240, CX + 200, 420], radius=30, fill=(18, 22, 40), outline=WHITE, width=8)
for k in range(3):
    d.ellipse([CX + 110 - k * 50, 315, CX + 140 - k * 50, 345], fill=GREEN if k == 0 else GREY)
d.line([(CX - 160, 330), (CX - 20, 330)], fill=GREY, width=10)
text_c(d, (CX, 570), "212GB", font(BOLD, 190), WHITE)
pill(d, [120, 720, 910, 800], fill=(18, 22, 40), outline=WHITE, width=4)
pill(d, [128, 728, 640, 792], fill=PINK)
d.line([(640, 700), (640, 820)], fill=WHITE, width=6)
text_c(d, (640, 870), "MIN", font(BOLD, 44), PINK)
save(img, "11_storage_212gb")

# 12 end card: neutral info card (no platform logos)
img = base(); d = ImageDraw.Draw(img)
d.ellipse([CX - 200, 320, CX + 200, 720], fill=(18, 22, 40), outline=TEAL, width=12)
text_c(d, (CX, 520), "?", font(BOLD, 260), TEAL)
for k in range(3):
    d.rounded_rectangle([CX - 260 + k * 190, 830, CX - 150 + k * 190, 870], radius=20, fill=DIM)
save(img, "12_end_info")
