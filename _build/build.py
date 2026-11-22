# -*- coding: utf-8 -*-
"""Build the whole Smilecraft static site. Run:  python _build/build.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import pages_home
import pages_about
import pages_treat
import pages_util
from chrome import SITE

PAGES = [
    ("index.html", "1.0", "weekly"),
    ("treatments.html", "0.9", "monthly"),
    ("treatments/dental-implants.html", "0.9", "monthly"),
    ("treatments/root-canal.html", "0.9", "monthly"),
    ("treatments/braces-aligners.html", "0.9", "monthly"),
    ("treatments/smile-design.html", "0.9", "monthly"),
    ("about.html", "0.7", "monthly"),
    ("reviews.html", "0.8", "weekly"),
    ("gallery.html", "0.6", "monthly"),
    ("book.html", "0.9", "monthly"),
    ("contact.html", "0.8", "monthly"),
    ("first-visit.html", "0.6", "monthly"),
    ("faq.html", "0.7", "monthly"),
    ("privacy.html", "0.2", "yearly"),
]


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<rect width="32" height="32" rx="7" fill="#0E463C"/>
<path d="M16 6.2c-1.8 0-2.9.9-3.9.9-.8 0-1.4-.6-2.5-.4-2.4.3-4 2.5-4 5.3 0 2.5 1 4 1.6 6.3.4 1.6.6 3.6 1.2 5.2.3.9.8 1.5 1.5 1.5 1.3 0 1.4-3.8 2-5.4.3-1 .7-1.6 1.5-1.6s1.2.6 1.5 1.6c.6 1.6.7 5.4 2 5.4.7 0 1.2-.6 1.5-1.5.6-1.6.8-3.6 1.2-5.2.6-2.3 1.6-3.8 1.6-6.3 0-2.8-1.6-5-4-5.3-1.1-.2-1.7.4-2.5.4-1 0-2.1-.9-3.9-.9Z" fill="#FBF8F2"/>
</svg>
"""

ROBOTS = """User-agent: *
Allow: /

Sitemap: {url}/sitemap.xml
""".format(url=SITE["url"])

VERCEL = """{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "trailingSlash": false,
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    },
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "X-Frame-Options", "value": "SAMEORIGIN" },
        { "key": "Permissions-Policy", "value": "geolocation=(), microphone=(), camera=()" }
      ]
    },
    {
      "source": "/(.*)\\.html",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=0, must-revalidate" }
      ]
    }
  ]
}
"""


def build_sitemap():
    from datetime import date
    today = date.today().isoformat()
    urls = []
    for path, prio, freq in PAGES:
        urls.append(
            "  <url>\n"
            "    <loc>%s/%s</loc>\n"
            "    <lastmod>%s</lastmod>\n"
            "    <changefreq>%s</changefreq>\n"
            "    <priority>%s</priority>\n"
            "  </url>" % (SITE["url"], path, today, freq, prio))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(urls) + "\n</urlset>\n")


def main():
    pages_home.build()
    pages_about.build_about()
    pages_about.build_gallery()
    pages_about.build_reviews()
    pages_treat.build_all()
    pages_util.build_all()

    write("assets/img/favicon.svg", FAVICON)
    write("robots.txt", ROBOTS)
    write("sitemap.xml", build_sitemap())
    write("vercel.json", VERCEL)

    built = []
    for dirpath, _, files in os.walk(ROOT):
        if "_build" in dirpath:
            continue
        for fn in files:
            if fn.endswith(".html"):
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT).replace("\\", "/")
                built.append(rel)
    print("Built %d HTML pages:" % len(built))
    for b in sorted(built):
        print("  ", b)


if __name__ == "__main__":
    main()
