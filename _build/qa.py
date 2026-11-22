# -*- coding: utf-8 -*-
"""Emit scaled desktop-preview slices for visual QA (not part of the deploy)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "_qa")
os.makedirs(OUT, exist_ok=True)

TPL = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>QA %(page)s %(off)s</title>
<style>
  html,body{margin:0;background:#c9c9c9;overflow:hidden}
  #vp{width:472px;height:704px;overflow:hidden;position:relative}
  iframe{width:1400px;height:12000px;border:0;transform:scale(.337);transform-origin:0 0;
         display:block;position:absolute;left:0;top:-%(off)spx}
</style></head>
<body><div id="vp"><iframe src="../%(page)s" title="preview"></iframe></div></body></html>
"""

pages = {
    "home": ("index.html", [0, 620, 1240, 1860, 2480, 3100]),
    "book": ("book.html", [0, 620, 1240]),
    "treat": ("treatments/root-canal.html", [0, 620, 1240]),
    "gal": ("gallery.html", [0, 620]),
    "rev": ("reviews.html", [0, 620]),
}

for key, (page, offsets) in pages.items():
    for off in offsets:
        name = "q_%s_%d.html" % (key, off)
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(TPL % {"page": page, "off": off})
        print("wrote", name)
