# -*- coding: utf-8 -*-
"""Builds every page from the modules in this folder.

    python _build/build.py
"""
import os
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from chrome import SITE  # noqa: E402
import pages_home  # noqa: E402
import pages_treat  # noqa: E402
import pages_info  # noqa: E402
import pages_contact  # noqa: E402

PAGES = [
    ("index.html", pages_home.build),
    ("treatments.html", pages_treat.hub),
    ("treatments/dental-implants.html", pages_treat.implants),
    ("treatments/root-canal.html", pages_treat.root_canal),
    ("treatments/braces-aligners.html", pages_treat.braces),
    ("treatments/smile-design.html", pages_treat.smile_design),
    ("about.html", pages_info.about),
    ("reviews.html", pages_contact.reviews),
    ("gallery.html", pages_contact.gallery),
    ("contact.html", pages_contact.contact),
    ("book.html", pages_contact.book),
    ("first-visit.html", pages_info.first_visit),
    ("faq.html", pages_info.faq),
    ("privacy.html", pages_info.privacy),
    ("thank-you.html", pages_info.thank_you),
    ("404.html", pages_info.not_found),
]

SITEMAP_SKIP = {"404.html", "thank-you.html"}


def write(rel, content):
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("  %-38s %6.1f KB" % (rel, len(content.encode("utf-8")) / 1024))


def main():
    print("Building %d pages into %s" % (len(PAGES), ROOT))
    urls = []
    for rel, fn in PAGES:
        html = fn()
        write(rel, html)
        if rel not in SITEMAP_SKIP:
            urls.append((rel, "1.0" if rel == "index.html" else "0.7" if rel.startswith("treatments") else "0.6"))

    today = datetime.date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for rel, prio in urls:
        loc = SITE["url"] + "/" + ("" if rel == "index.html" else rel)
        sm.append("  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>" % (loc, today, prio))
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")

    robots = """User-agent: *
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE["url"]
    write("robots.txt", robots)
    print("Done.")


if __name__ == "__main__":
    main()
