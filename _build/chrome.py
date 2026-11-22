# -*- coding: utf-8 -*-
"""Shared chrome for the Smilecraft site — Bright Clinical theme."""
import os
import json

SITE = {
    "name": "Smilecraft",
    "full": "Smilecraft Multispeciality Dental Clinic & Implant Center",
    "url": "https://smilecraftdental.in",          # change after you pick a domain
    "phone_display": "+91 94274 51885",
    "phone_tel": "+919427451885",
    "wa": "919427451885",
    "addr1": "Shop 214, Second Floor, Blueberry Complex",
    "addr2": "National Handloom House, near Virat Nagar Road",
    "addr3": "Beside Bhojaldham Society, Nikol, Ahmedabad, Gujarat 380049",
    "place_id": "ChIJBXJ2CL6HXjkRyDeaS15eANI",
    "lat": "23.0367285",
    "lng": "72.6722494",
    "review": "https://search.google.com/local/writereview?placeid=ChIJBXJ2CL6HXjkRyDeaS15eANI",
    "maps": "https://www.google.com/maps/place/?q=place_id:ChIJBXJ2CL6HXjkRyDeaS15eANI",
    "dir": "https://www.google.com/maps/dir/?api=1&destination=23.0367285,72.6722494",
    "rating": "5.0",
    "reviews": "313",
}

TEL = "tel:" + SITE["phone_tel"]
WA = "https://wa.me/" + SITE["wa"]
REVIEW = SITE["review"]

IC = {
    "pin": '<path d="M12 21s7-6.1 7-11a7 7 0 1 0-14 0c0 4.9 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/>',
    "phone": '<path d="M6.6 3h2.2l1.6 4-2 1.4a12 12 0 0 0 5.2 5.2l1.4-2 4 1.6v2.2A2.6 2.6 0 0 1 16.4 21C9.5 20.4 3.6 14.5 3 7.6A2.6 2.6 0 0 1 6.6 3Z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.2l3.2 2"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "check": '<path d="M4 12.5 9.5 18 20 6.5"/>',
    "star": '<path d="m12 3.6 2.6 5.3 5.8.8-4.2 4.1 1 5.8-5.2-2.8-5.2 2.8 1-5.8-4.2-4.1 5.8-.8Z"/>',
    "wa": '<path d="M12.04 3a9 9 0 0 0-7.7 13.6L3 21.5l5-1.3A9 9 0 1 0 12.04 3Z"/><path d="M8.7 8.3c.3-.7.6-.7.9-.7h.7c.2 0 .5 0 .7.6l.9 2c.1.2.1.4 0 .6l-.5.7c-.2.2-.3.4-.1.7a6.6 6.6 0 0 0 2.9 2.5c.3.1.5.1.7-.1l.7-.8c.2-.2.4-.2.6-.1l2 .9c.2.1.4.3.4.6a2.2 2.2 0 0 1-1.6 2.1c-.6.2-1.3.3-3.4-.6a11 11 0 0 1-4.6-4.5c-.8-1.6-.8-2.6-.6-3.3Z"/>',
    "shield": '<path d="M12 3 5 6v6c0 4.4 3 7.7 7 9 4-1.3 7-4.6 7-9V6Z"/><path d="m9 12 2.2 2.2L15.5 10"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5Z"/>',
    "tooth": '',
    "calendar": '<rect x="3.5" y="5" width="17" height="16" rx="3"/><path d="M8 3v4M16 3v4M3.5 10h17"/>',
    "heart": '<path d="M12 20s-7-4.4-7-9.3A4.2 4.2 0 0 1 12 7a4.2 4.2 0 0 1 7 3.7C19 15.6 12 20 12 20Z"/>',
    "sparkle": '<path d="M12 3v5M12 16v5M4.5 12h5M14.5 12h5"/><path d="m7 7 2.5 2.5M14.5 14.5 17 17M17 7l-2.5 2.5M9.5 14.5 7 17"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.4 6-5.4s6 2.1 6 5.4"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6.2M17.5 14.8c2.1.5 3.5 2.2 3.5 4.6"/>',
}

TOOTH_PATH = ('M16 3.6c-2.3 0-3.7 1.1-4.9 1.1-1 0-1.7-.7-3.1-.5C4.9 4.6 2.8 7.4 2.8 11'
              'c0 3.2 1.3 5.1 2 8 .5 2.1.7 4.6 1.5 6.7.4 1.1 1 1.9 2 1.9 1.7 0 1.8-4.8 2.5-6.9'
              '.4-1.3 1-2 1.9-2s1.5.7 1.9 2c.7 2.1.8 6.9 2.5 6.9 1 0 1.6-.8 2-1.9'
              '.8-2.1 1-4.6 1.5-6.7.7-2.9 2-4.8 2-8 0-3.6-2.1-6.4-5.2-6.8-1.4-.2-2.1.5-3.1.5'
              '-1.2 0-2.6-1.1-4.9-1.1Z')


def icon(name, cls="ic"):
    body = IC.get(name, "")
    return ('<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>' % (cls, body))


TOOTH_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="%s" fill="currentColor"/></svg>' % TOOTH_PATH

NAV = [
    ("treatments", "Treatments", [
        ("treatments/dental-implants.html", "Dental implants"),
        ("treatments/root-canal.html", "Root canal treatment"),
        ("treatments/braces-aligners.html", "Braces &amp; aligners"),
        ("treatments/smile-design.html", "Smile design"),
        ("__sep__", ""),
        ("treatments.html", "All treatments"),
    ]),
    ("reviews", "Reviews", None),
    ("gallery", "Gallery", None),
    ("about", "About", None),
    ("contact", "Contact", None),
]

PAGE_FILES = {
    "home": "index.html",
    "reviews": "reviews.html",
    "gallery": "gallery.html",
    "about": "about.html",
    "contact": "contact.html",
    "treatments": "treatments.html",
    "book": "book.html",
    "first-visit": "first-visit.html",
    "faq": "faq.html",
    "privacy": "privacy.html",
    "thanks": "thank-you.html",
}


def link(key, root=""):
    return root + PAGE_FILES[key]


# ------------------------------------------------------------------ head ----
def head(title, desc, root="", canonical="", og="assets/img/smile-portrait.jpg",
         schema=None, extra_head=""):
    ld = ""
    if schema:
        blocks = schema if isinstance(schema, list) else [schema]
        for b in blocks:
            ld += '<script type="application/ld+json">%s</script>\n' % json.dumps(
                b, ensure_ascii=False, separators=(",", ":"))
    if not canonical or canonical == "index.html":
        can = SITE["url"] + "/"
    else:
        can = SITE["url"] + "/" + canonical

    return """<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{can}">
<meta name="theme-color" content="#0E9AA7">
<meta name="robots" content="index,follow">
<meta name="geo.region" content="IN-GJ">
<meta name="geo.placename" content="Nikol, Ahmedabad">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Smilecraft Dental Clinic, Nikol">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{can}">
<meta property="og:image" content="{site}/{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/{og}">

<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/img/favicon.svg">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="format-detection" content="telephone=no">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<link rel="stylesheet" href="{root}assets/css/main.css">
<link rel="stylesheet" href="{root}assets/css/pages.css">
<link rel="stylesheet" href="{root}assets/css/components.css">
<link rel="stylesheet" href="{root}assets/css/animations.css">
<link rel="stylesheet" href="{root}assets/css/responsive.css">
<link rel="stylesheet" href="{root}assets/css/site.css">
<link rel="stylesheet" href="{root}assets/css/theme.css">
<link rel="stylesheet" href="{root}assets/css/theme-swiss.css">
<link rel="stylesheet" href="{root}assets/css/theme-dark.css">
<link rel="stylesheet" href="{root}assets/css/theme-minimal.css">
<link rel="stylesheet" href="{root}assets/css/theme-soft.css">
<link rel="stylesheet" href="{root}assets/css/theme-soft-v2.css">
<link rel="stylesheet" href="{root}assets/css/theme-rich.css">
<noscript><style>[data-reveal]{{opacity:1!important;transform:none!important}}</style></noscript>
{ld}{extra}
</head>
<body data-menu="closed">
<a class="skip" href="#main">Skip to content</a>
<div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
""".format(title=title, desc=desc, can=can, site=SITE["url"], og=og,
           root=root, ld=ld, extra=extra_head)


# ---------------------------------------------------------------- header ----
def header(root="", active=""):
    items = []
    for key, label, kids in NAV:
        cur = ' aria-current="page"' if key == active else ""
        if kids:
            sub = []
            for href, txt in kids:
                if href == "__sep__":
                    sub.append('<div class="dropdown__sep"></div>')
                else:
                    sub.append('<a href="%s%s">%s</a>' % (root, href, txt))
            items.append(
                '<div class="nav__item"><a class="nav__link" href="%streatments.html"%s>%s'
                '<svg viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="1.8" '
                'stroke-linecap="round" aria-hidden="true"><path d="M1 1.5 6 6.5 11 1.5"/></svg></a>'
                '<div class="dropdown">%s</div></div>' % (root, cur, label, "".join(sub)))
        else:
            items.append('<div class="nav__item"><a class="nav__link" href="%s%s"%s>%s</a></div>'
                         % (root, PAGE_FILES[key], cur, label))

    drawer_links = [
        (root + "treatments.html", "Treatments", "01"),
        (root + "reviews.html", "Reviews", "02"),
        (root + "gallery.html", "Gallery", "03"),
        (root + "about.html", "About the clinic", "04"),
        (root + "first-visit.html", "Your first visit", "05"),
        (root + "faq.html", "Questions", "06"),
        (root + "contact.html", "Find us", "07"),
    ]
    draw = "".join('<a href="%s">%s<span>%s</span></a>' % (h, t, n) for h, t, n in drawer_links)

    return """<div class="topbar">
  <div class="wrap topbar__in">
    <p class="topbar__item topbar__item--addr">{pin}<span>{a1}, Nikol</span></p>
    <p class="topbar__item topbar__item--hours">
      <span class="status" data-open-status data-open="true">
        <span class="status__dot" aria-hidden="true"></span>
        <span data-status-text>Mon&ndash;Sat &middot; 9:00 AM &ndash; 9:00 PM</span>
      </span>
    </p>
    <p class="topbar__item"><a class="topbar__tel" href="{tel}">{phone}</a></p>
  </div>
</div>

<header class="site-head" data-stuck="false">
  <div class="wrap site-head__in">
    <a class="brand" href="{root}index.html" aria-label="Smilecraft Dental Clinic, Nikol">
      <span class="brand__mark">{tooth}</span>
      <span class="brand__text">
        <span class="brand__name">Smilecraft</span>
        <span class="brand__sub">Dental Clinic &middot; Nikol</span>
      </span>
    </a>
    <nav class="nav" aria-label="Primary">{items}</nav>
    <div class="head-actions">
      <a class="btn btn--ghost" href="{tel}">{ph}<span>Call</span></a>
      <a class="btn" href="{root}book.html">Book appointment</a>
      <button class="burger" type="button" data-burger aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><span></span></button>
    </div>
  </div>
</header>

<div class="drawer" id="drawer" data-drawer aria-hidden="true" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="drawer__head">
    <span class="brand">
      <span class="brand__mark">{tooth}</span>
      <span class="brand__text"><span class="brand__name">Smilecraft</span><span class="brand__sub">Nikol, Ahmedabad</span></span>
    </span>
    <button class="drawer__close" type="button" data-drawer-close aria-label="Close menu">&times;</button>
  </div>
  <nav class="drawer__nav" aria-label="Mobile">{draw}</nav>
  <div class="drawer__foot">
    <a class="btn btn--block" href="{root}book.html">Book an appointment</a>
    <a class="btn btn--ghost btn--block" href="https://wa.me/{wa}" target="_blank" rel="noopener">{waic} Message on WhatsApp</a>
    <p class="drawer__meta">{a1}<br>{a3}<br><a href="{tel}">{phone}</a></p>
  </div>
</div>
""".format(pin=icon("pin"), a1=SITE["addr1"], a3=SITE["addr3"], tel=TEL,
           phone=SITE["phone_display"], root=root, tooth=TOOTH_SVG,
           items="".join(items), draw=draw, wa=SITE["wa"],
           ph=icon("phone"), waic=icon("wa"))


# ---------------------------------------------------------------- footer ----
def footer(root=""):
    return """<footer class="site-foot">
  <div class="wrap">
    <div class="foot__grid">
      <div class="foot__brand">
        <a class="brand" href="{root}index.html">
          <span class="brand__mark">{tooth}</span>
          <span class="brand__text">
            <span class="brand__name">Smilecraft</span>
            <span class="brand__sub">Multispeciality &amp; Implant Center</span>
          </span>
        </a>
        <p class="foot__blurb">A patient-first dental practice in Nikol, Ahmedabad &mdash; implants,
        root canals, braces and everyday dentistry, without the rush.</p>
        <div class="foot__social">
          <a href="https://wa.me/{wa}" target="_blank" rel="noopener" aria-label="WhatsApp">{waic}</a>
          <a href="{tel}" aria-label="Call the clinic">{ph}</a>
          <a href="{maps}" target="_blank" rel="noopener" aria-label="Google Maps">{pin}</a>
        </div>
      </div>

      <div>
        <h4>Treatments</h4>
        <ul class="foot__list">
          <li><a href="{root}treatments/dental-implants.html">Dental implants</a></li>
          <li><a href="{root}treatments/root-canal.html">Root canal treatment</a></li>
          <li><a href="{root}treatments/braces-aligners.html">Braces &amp; aligners</a></li>
          <li><a href="{root}treatments/smile-design.html">Smile design</a></li>
          <li><a href="{root}treatments.html">All treatments</a></li>
        </ul>
      </div>

      <div>
        <h4>The clinic</h4>
        <ul class="foot__list">
          <li><a href="{root}about.html">About us</a></li>
          <li><a href="{root}first-visit.html">Your first visit</a></li>
          <li><a href="{root}reviews.html">Patient reviews</a></li>
          <li><a href="{root}gallery.html">Gallery</a></li>
          <li><a href="{root}faq.html">Questions</a></li>
          <li><a href="{root}privacy.html">Privacy note</a></li>
        </ul>
      </div>

      <div>
        <h4>Visit us</h4>
        <a class="foot__tel" href="{tel}">{phone}</a>
        <address class="foot__addr">
          {a1}<br>{a2}<br>{a3}
        </address>
        <p class="foot__addr" style="margin-top:8px">Mon&ndash;Sat, 9:00 AM &ndash; 9:00 PM<br>Closed Sunday</p>
        <p style="margin-top:8px"><a href="{dir}" target="_blank" rel="noopener" style="color:#6FD9E2;font-weight:600">Get directions &rarr;</a></p>
      </div>
    </div>

    <p class="foot__legal">
      Information on this site is general in nature and is not a substitute for an in-person
      consultation. Treatment suitability, duration and cost can only be confirmed after examination.
    </p>

    <div class="foot__bottom">
      <span>&copy; <span data-year>2026</span> Smilecraft Multispeciality Dental Clinic &amp; Implant Center.</span>
      <nav aria-label="Legal">
        <a href="{root}privacy.html">Privacy</a>
        <a href="{root}contact.html">Directions</a>
        <a href="{review}" target="_blank" rel="noopener">Leave a review</a>
      </nav>
    </div>
  </div>
</footer>
""".format(root=root, tooth=TOOTH_SVG, wa=SITE["wa"], waic=icon("wa"),
           ph=icon("phone"), pin=icon("pin"), tel=TEL, phone=SITE["phone_display"],
           maps=SITE["maps"], dir=SITE["dir"], review=REVIEW,
           a1=SITE["addr1"], a2=SITE["addr2"], a3=SITE["addr3"])


def foot_scripts(root="", extra=""):
    return """<nav class="mbar" aria-label="Quick actions">
  <a href="{tel}">{ph}<span>Call</span></a>
  <a href="https://wa.me/{wa}" target="_blank" rel="noopener">{waic}<span>WhatsApp</span></a>
  <a class="mbar__primary" href="{root}book.html">{cal}<span>Book</span></a>
</nav>
<a class="wa-float" href="https://wa.me/{wa}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  {waic}
</a>

<button class="to-top" type="button" data-to-top aria-label="Back to top" data-show="false">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M6 11l6-6 6 6"/></svg>
</button>

<div class="sticky-book" data-sticky-book data-show="false">
  <span class="sticky-book__text">
    <strong>Ready when you are</strong>
    <span>Mon&ndash;Sat, 9 AM &ndash; 9 PM</span>
  </span>
  <a class="btn" href="{root}book.html">Book a visit</a>
</div>

<script src="{root}assets/js/site.js" defer></script>
<script src="{root}assets/js/app.js" defer></script>
<script src="{root}assets/js/motion.js" defer></script>
{extra}</body>
</html>
""".format(tel=TEL, ph=icon("phone"), wa=SITE["wa"], waic=icon("wa"),
           cal=icon("calendar"), root=root, extra=extra)


def page(path, title, desc, body, root="", active="", canonical="",
         og="assets/img/smile-portrait.jpg", schema=None, extra_head="",
         extra_scripts=""):
    html = (head(title, desc, root, canonical or path, og, schema, extra_head)
            + header(root, active) + '<main id="main">' + body + "</main>"
            + footer(root) + foot_scripts(root, extra_scripts))
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return path


# ------------------------------------------------------- schema helpers ----
def dentist_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Dentist",
        "@id": SITE["url"] + "/#clinic",
        "name": SITE["full"],
        "url": SITE["url"] + "/",
        "image": SITE["url"] + "/assets/img/smile-portrait.jpg",
        "telephone": SITE["phone_tel"],
        "priceRange": "₹₹",
        "currenciesAccepted": "INR",
        "paymentAccepted": "Cash, UPI, Credit Card, Debit Card",
        "medicalSpecialty": "Dentistry",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Shop No. 214, Second Floor, Blueberry Complex, National Handloom House, near Virat Nagar Road, beside Bhojaldham Society",
            "addressLocality": "Nikol, Ahmedabad",
            "addressRegion": "Gujarat",
            "postalCode": "380049",
            "addressCountry": "IN",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "hasMap": SITE["maps"],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "21:00",
        }],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": SITE["rating"],
            "reviewCount": SITE["reviews"],
            "bestRating": "5",
        },
        "sameAs": [SITE["maps"]],
    }


def breadcrumb_schema(crumbs):
    items = []
    for i, (name, p) in enumerate(crumbs, start=1):
        it = {"@type": "ListItem", "position": i, "name": name}
        if p:
            it["item"] = SITE["url"] + "/" + p
        items.append(it)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def faq_schema(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        } for q, a in pairs],
    }
