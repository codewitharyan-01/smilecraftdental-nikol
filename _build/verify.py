# -*- coding: utf-8 -*-
"""Stricter post-build verification for the upgrade pass.

    python _build/verify.py
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import chrome  # noqa: E402

errors = []

# 1. every icon("name") used in the templates must exist in the sprite
used = set()
for f in glob.glob(os.path.join(HERE, "*.py")):
    src = open(f, encoding="utf-8").read()
    used.update(re.findall(r"""icon\(\s*["']([a-z0-9\-]+)["']""", src))
missing = sorted(n for n in used if n not in chrome.ICONS and n != "name")
if missing:
    errors.append("icon names referenced but not defined: %s" % missing)

# 2. per page checks
pages = []
for base, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ("_build", ".git", "__pycache__")]
    for f in files:
        if f.endswith(".html") and not f.startswith("__"):
            pages.append(os.path.join(base, f))

sprite_sizes = []
for path in sorted(pages):
    rel = os.path.relpath(path, ROOT).replace("\\", "/")
    html = open(path, encoding="utf-8").read()

    syms = set(re.findall(r'<symbol id="i-([a-z0-9\-]+)"', html))
    if not syms:
        errors.append("%s: icon sprite missing" % rel)
    sprite_sizes.append(len(syms))

    undefined = sorted(set(re.findall(r'<use href="#i-([a-z0-9\-]+)"', html)) - syms)
    if undefined:
        errors.append("%s: <use> points at undefined icons %s" % (rel, undefined))

    if html.count("<h1") != 1:
        errors.append("%s: %d <h1> elements" % (rel, html.count("<h1")))

    for token in ("footer__panel", "data-book-pill", "side-label", 'class="grain"'):
        if token not in html:
            errors.append("%s: missing %s" % (rel, token))

    for token in ("{icon(", "{SITE", "{p}", "{brand}", "{street}"):
        if token in html:
            errors.append("%s: unreplaced template token %s" % (rel, token))

    if "<title></title>" in html or '<meta name="description" content="">' in html:
        errors.append("%s: empty title or description" % rel)

print("pages: %d | icons per page: %s | icon names used: %d"
      % (len(pages), sorted(set(sprite_sizes)), len(used)))
for e in errors:
    print("  ERROR  %s" % e)
print("\n%d errors" % len(errors))
sys.exit(1 if errors else 0)

