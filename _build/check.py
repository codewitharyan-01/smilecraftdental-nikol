# -*- coding: utf-8 -*-
"""Static QA for the built site: links, assets, anchors, ids, head metadata.

    python _build/check.py
"""
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_build", ".git", "__pycache__"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []      # (attr, value)
        self.ids = []
        self.imgs = []
        self.h1 = 0
        self.title = ""
        self.meta = {}
        self.canonical = ""
        self.in_title = False
        self._ld = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(("a", a["href"]))
        if tag in ("link", "script", "img", "source", "video") and (a.get("href") or a.get("src")):
            self.links.append((tag, a.get("href") or a.get("src")))
        if tag == "img":
            self.imgs.append(a)
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self.in_title = True
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href", "")
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k:
                self.meta[k] = a.get("content", "")
        if a.get("id"):
            self.ids.append(a["id"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip()


def html_files():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".html") and not f.startswith("__"):
                out.append(os.path.join(base, f))
    return sorted(out)


def main():
    errors = []
    warnings = []
    pages = {}

    for path in html_files():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        p = Page()
        with open(path, encoding="utf-8") as fh:
            p.feed(fh.read())
        pages[rel] = p

        if not p.title:
            errors.append("%s: missing <title>" % rel)
        if not p.meta.get("description"):
            errors.append("%s: missing meta description" % rel)
        if p.h1 != 1:
            errors.append("%s: %d <h1> elements (expected 1)" % (rel, p.h1))
        if not p.canonical and rel not in ("404.html",):
            errors.append("%s: missing canonical" % rel)
        dupes = set([i for i in p.ids if p.ids.count(i) > 1])
        if dupes:
            errors.append("%s: duplicate ids %s" % (rel, sorted(dupes)))
        for img in p.imgs:
            if "alt" not in img:
                errors.append("%s: <img> without alt (%s)" % (rel, img.get("src")))

    # link targets
    for rel, p in pages.items():
        base = os.path.dirname(os.path.join(ROOT, rel))
        for tag, href in p.links:
            if not href or href.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            u = urlparse(href)
            if u.scheme in ("http", "https"):
                if tag == "a" and "wa.me" in href:
                    if "?text=" not in href and "https://wa.me/919427451885" == href.split("?")[0]:
                        warnings.append("%s: WhatsApp link without context" % rel)
                continue
            target_path = os.path.normpath(os.path.join(base, unquote(u.path))) if u.path else os.path.join(ROOT, rel)
            if not os.path.exists(target_path):
                errors.append("%s: broken link -> %s" % (rel, href))
                continue
            if u.fragment:
                t_rel = os.path.relpath(target_path, ROOT).replace("\\", "/")
                tp = pages.get(t_rel)
                if tp and u.fragment not in tp.ids:
                    errors.append("%s: missing anchor #%s in %s" % (rel, u.fragment, t_rel))

    # assets referenced by css
    css = os.path.join(ROOT, "assets", "css", "site.css")
    with open(css, encoding="utf-8") as fh:
        text = fh.read()
    # data URIs contain their own url(...)/%23n references; drop the whole token
    text = re.sub(r'url\(\s*"data:[^"]*"\s*\)', 'url(DATAURI)', text)
    text = re.sub(r"url\(\s*'data:[^']*'\s*\)", "url(DATAURI)", text)
    for m in re.finditer(r"url\((['\"]?)([^'\")]+)\1\)", text):
        val = m.group(2)
        if val.startswith("data:") or val == "DATAURI":
            continue
        f = os.path.normpath(os.path.join(os.path.dirname(css), val))
        if not os.path.exists(f):
            errors.append("site.css: missing asset %s" % val)

    print("Pages checked: %d" % len(pages))
    for e in errors:
        print("  ERROR  %s" % e)
    for w in warnings[:20]:
        print("  warn   %s" % w)
    print("\n%d errors, %d warnings" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
