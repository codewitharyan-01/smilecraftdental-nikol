# -*- coding: utf-8 -*-
"""Verify the site will actually deploy on Vercel.

Windows is case-insensitive; Vercel's builders run on Linux and are not.
A link like `Assets/Img/Hero.jpg` passes locally and 404s in production.
This script checks every local reference for:
  1. exact-case existence on disk
  2. presence in `git ls-files` (untracked files never reach Vercel)
  3. validity of vercel.json
"""
import json
import os
import re
import subprocess
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
ATTR = re.compile(r'(?:href|src|poster)="([^"]+)"')
SKIP = ("http://", "https://", "//", "data:", "mailto:", "tel:", "#", "javascript:")

problems = []
checked = 0


def exact_exists(rel_path):
    """Case-sensitive existence check by walking directory entries."""
    parts = [p for p in rel_path.replace("\\", "/").split("/") if p and p != "."]
    cur = ROOT
    for i, part in enumerate(parts):
        if part == "..":
            cur = os.path.dirname(cur)
            continue
        try:
            entries = os.listdir(cur)
        except OSError:
            return False
        if part not in entries:          # exact string match = case-sensitive
            return False
        cur = os.path.join(cur, part)
    return os.path.exists(cur)


# ---- tracked files -------------------------------------------------------
try:
    tracked = set(
        subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
        .stdout.splitlines()
    )
except Exception as e:
    tracked = set()
    print("WARN: could not read git index ->", e)

# ---- vercel.json ---------------------------------------------------------
vj = os.path.join(ROOT, "vercel.json")
if not os.path.exists(vj):
    problems.append("vercel.json is missing")
else:
    try:
        cfg = json.load(open(vj, encoding="utf-8"))
        print("vercel.json      : valid JSON")
        if not isinstance(cfg, dict):
            problems.append("vercel.json is not a JSON object")
    except Exception as e:
        problems.append("vercel.json invalid -> %s" % e)

# ---- required root files -------------------------------------------------
for f in ("index.html", "404.html", "robots.txt", "sitemap.xml"):
    if not os.path.exists(os.path.join(ROOT, f)):
        problems.append("missing root file: %s" % f)

# ---- walk html -----------------------------------------------------------
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "_qa", "_build", ".zwork", "node_modules")]
    for fn in filenames:
        if not fn.endswith(".html"):
            continue
        page = os.path.join(dirpath, fn)
        rel_page = os.path.relpath(page, ROOT).replace("\\", "/")
        html = open(page, encoding="utf-8").read()
        for ref in ATTR.findall(html):
            ref = ref.strip()
            if not ref or ref.startswith(SKIP):
                continue
            target = ref.split("#")[0].split("?")[0]
            if not target:
                continue
            checked += 1

            if target.startswith("/"):
                resolved = target.lstrip("/")
            else:
                base = os.path.dirname(rel_page)
                resolved = os.path.normpath(os.path.join(base, target)).replace("\\", "/")

            if not exact_exists(resolved):
                problems.append("%s -> WRONG CASE or MISSING: %s" % (rel_page, ref))
                continue
            if tracked and resolved not in tracked:
                problems.append("%s -> NOT COMMITTED: %s" % (rel_page, resolved))

print("references checked: %d" % checked)
print()

if problems:
    print("FAIL - %d problem(s):" % len(problems))
    for p in problems:
        print("  -", p)
else:
    print("PASS - every local reference exists with exact case and is committed.")
