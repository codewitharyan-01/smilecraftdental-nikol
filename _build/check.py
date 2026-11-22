# -*- coding: utf-8 -*-
"""Static integrity check: leftovers, broken links, missing assets, tag balance."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = []
for dp, _, fs in os.walk(ROOT):
    if "_build" in dp:
        continue
    for f in fs:
        if f.endswith(".html"):
            pages.append(os.path.join(dp, f))

problems = []
PH = re.compile(r"__[A-Z0-9_]{2,}__")
BRACE = re.compile(r"\{[a-z_]+\}")

for p in pages:
    rel = os.path.relpath(p, ROOT).replace("\\", "/")
    html = open(p, encoding="utf-8").read()
    d = os.path.dirname(p)

    for m in PH.finditer(html):
        problems.append("%s: unfilled placeholder %s" % (rel, m.group()))
    for m in BRACE.finditer(html):
        problems.append("%s: unfilled brace %s" % (rel, m.group()))

    for attr, val in re.findall(r'(href|src)="([^"]*)"', html):
        v = val.strip()
        if not v or v.startswith(("#", "http", "mailto:", "tel:", "data:", "//")):
            continue
        target = v.split("#")[0].split("?")[0]
        if not target:
            continue
        full = os.path.normpath(os.path.join(d, target.lstrip("/") if not target.startswith("/") else target.lstrip("/")))
        if target.startswith("/"):
            full = os.path.normpath(os.path.join(ROOT, target.lstrip("/")))
        if not os.path.exists(full):
            problems.append("%s: missing target %s" % (rel, v))

    # rough tag balance for key containers
    for tag in ("div", "section", "main", "aside", "figure", "nav", "header", "footer", "a", "span"):
        o = len(re.findall(r"<%s[\s>]" % tag, html))
        c = len(re.findall(r"</%s>" % tag, html))
        if o != c:
            problems.append("%s: <%s> open=%d close=%d" % (rel, tag, o, c))

# assets referenced anywhere
print("Pages checked:", len(pages))
if problems:
    print("\n%d problem(s):" % len(problems))
    for x in problems:
        print("  -", x)
else:
    print("No structural problems found.")
