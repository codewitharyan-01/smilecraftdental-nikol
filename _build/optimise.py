# -*- coding: utf-8 -*-
"""Resize and compress images for the web."""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")

# filename -> max width
LIMITS = {
    "smile-portrait.jpg": 1200,
    "smile-macro.jpg": 1000,
    "smile-woman.jpg": 1100,
    "gen-doctor.jpg": 1400,
    "gen-implant.jpg": 1300,
    "gen-instruments.jpg": 1300,
    "gen-reception.jpg": 1400,
    "gen-operatory.jpg": 1300,
    "aligner-vs-braces.jpg": 1100,
}
QUALITY = 82

total_before = total_after = 0
for fn, maxw in LIMITS.items():
    p = os.path.join(IMG, fn)
    if not os.path.exists(p):
        print("missing:", fn)
        continue
    before = os.path.getsize(p)
    total_before += before
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if w > maxw:
        im = im.resize((maxw, round(h * maxw / w)), Image.LANCZOS)
    im.save(p, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    after = os.path.getsize(p)
    total_after += after
    print("%-24s %4dx%-4d  %5.0f KB -> %5.0f KB" % (fn, im.size[0], im.size[1], before / 1024, after / 1024))

print("\ntotal %.0f KB -> %.0f KB" % (total_before / 1024, total_after / 1024))
