# -*- coding: utf-8 -*-
"""Builds assets/img/map-nikol.jpg from OpenStreetMap tiles.

Run once:  python _build/make_map.py
Requires Pillow and an internet connection. 16 tiles, well inside OSM's
tile usage policy; attribution is baked into the image.
"""
import math
import os
import urllib.request
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

LAT, LON = 23.0367285, 72.6722494
ZOOM = 16
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "assets", "img", "map-nikol.jpg")
UA = "SmilecraftDentalSiteBuilder/1.0 (one-off static map render)"


def deg2num(lat, lon, z):
    n = 2 ** z
    x = (lon + 180.0) / 360.0 * n
    lat_r = math.radians(lat)
    y = (1.0 - math.asinh(math.tan(lat_r)) / math.pi) / 2.0 * n
    return x, y


def fetch(x, y, z):
    url = "https://tile.openstreetmap.org/%d/%d/%d.png" % (z, x, y)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return Image.open(BytesIO(r.read())).convert("RGB")


def main():
    n = 2 ** ZOOM
    fx, fy = deg2num(LAT, LON, ZOOM)
    cx, cy = int(fx), int(fy)
    px, py = (fx - cx) * 256, (fy - cy) * 256          # position inside centre tile

    W, H = 5, 4                                        # tiles across / down (must cover the crop)
    canvas = Image.new("RGB", (W * 256, H * 256), "#e9e5dc")
    for ty in range(H):
        for tx in range(W):
            x = (cx - 1 + tx) % n
            y = cy - 1 + ty
            try:
                canvas.paste(fetch(x, y, ZOOM), (tx * 256, ty * 256))
            except Exception as e:                     # keep going; blank tile is fine
                print("  tile %s/%s failed: %s" % (x, y, e))

    # crop so the clinic sits centre-left, giving space for the label
    out_w, out_h = 1120, 760
    left = 256 + px - int(out_w * 0.42)
    top = 256 + py - int(out_h * 0.52)
    left = max(0, min(left, canvas.width - out_w))
    top = max(0, min(top, canvas.height - out_h))
    assert left + out_w <= canvas.width and top + out_h <= canvas.height, "crop exceeds stitched tiles"
    img = canvas.crop((left, top, left + out_w, top + out_h))

    # gentle warm grade so it belongs with the rest of the palette
    warm = Image.new("RGB", img.size, "#f3ecdd")
    img = Image.blend(img, warm, 0.10)

    d = ImageDraw.Draw(img, "RGBA")
    mx = int(out_w * 0.42)
    my = int(out_h * 0.52)

    # marker: soft halo, ring, dot
    for r, a in ((34, 26), (22, 38)):
        d.ellipse([mx - r, my - r, mx + r, my + r], fill=(18, 59, 50, a))
    d.ellipse([mx - 13, my - 13, mx + 13, my + 13], fill=(18, 59, 50, 255),
              outline=(255, 253, 248, 255), width=3)
    d.ellipse([mx - 3, my - 3, mx + 3, my + 3], fill=(255, 253, 248, 255))

    # label
    try:
        bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 19)
        small = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
    except Exception:
        bold = ImageFont.load_default()
        small = ImageFont.load_default()

    label = "Smilecraft Dental"
    sub = "Blueberry Complex · 2nd floor"
    tw = max(d.textlength(label, font=bold), d.textlength(sub, font=small))
    bx, by = mx + 26, my - 34
    d.rounded_rectangle([bx, by, bx + tw + 26, by + 62], radius=6,
                        fill=(255, 253, 248, 246), outline=(221, 212, 196, 255), width=1)
    d.rectangle([bx, by + 8, bx + 3, by + 54], fill=(191, 90, 51, 255))
    d.text((bx + 13, by + 10), label, font=bold, fill=(20, 29, 25, 255))
    d.text((bx + 13, by + 35), sub, font=small, fill=(108, 122, 115, 255))

    # attribution
    attr = "© OpenStreetMap contributors"
    aw = d.textlength(attr, font=small)
    d.rectangle([out_w - aw - 14, out_h - 22, out_w, out_h], fill=(255, 253, 248, 230))
    d.text((out_w - aw - 7, out_h - 19), attr, font=small, fill=(60, 74, 68, 255))

    img = img.resize((900, int(900 * out_h / out_w)), Image.LANCZOS)
    img.save(OUT, "JPEG", quality=82, optimize=True, progressive=True)
    print("wrote %s  %dx%d  %.0f KB" % (OUT, img.width, img.height, os.path.getsize(OUT) / 1024))


if __name__ == "__main__":
    main()
