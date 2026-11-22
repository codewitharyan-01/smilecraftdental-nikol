# -*- coding: utf-8 -*-
"""Shared page shell for the Smilecraft site.

One source of truth for the head, header, footer and floating widgets so that
15 hand-written pages stay identical. Run `python _build/build.py` to rebuild.
"""

SITE = {
    "name": "Smilecraft",
    "full": "Smilecraft Multispeciality Dental Clinic & Implant Center",
    "short": "Smilecraft Dental",
    "url": "https://smilecraftdental.in",
    "phone_display": "+91 94274 51885",
    "phone_tel": "+919427451885",
    "wa": "919427451885",
    "street": "Shop No. 214, Second Floor, Blueberry Complex (National Handloom House)",
    "street2": "Near Virat Nagar Road, beside Bhojaldham Society",
    "city": "Nikol, Ahmedabad, Gujarat 380049",
    "place_id": "ChIJBXJ2CL6HXjkRyDeaS15eANI",
    "lat": "23.0367285",
    "lng": "72.6722494",
    "rating": "5.0",
    "review_count": "313",
}

SITE["review"] = "https://search.google.com/local/writereview?placeid=" + SITE["place_id"]
SITE["maps"] = "https://www.google.com/maps/place/?q=place_id:" + SITE["place_id"]
SITE["dir"] = "https://www.google.com/maps/dir/?api=1&destination=%s,%s" % (SITE["lat"], SITE["lng"])
SITE["embed"] = "https://maps.google.com/maps?q=%s,%s&z=16&hl=en&output=embed" % (SITE["lat"], SITE["lng"])
SITE["wa_base"] = "https://wa.me/" + SITE["wa"]

TEL = "tel:" + SITE["phone_tel"]

ICONS = {
    "arrow": '<path d="M4 12h15M13 6l6 6-6 6"/>',
    "arrow-up-right": '<path d="M7 17 17 7M8 7h9v9"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "chevron-l": '<path d="m14 6-6 6 6 6"/>',
    "chevron-r": '<path d="m10 6 6 6-6 6"/>',
    "phone": '<path d="M6.6 3h2.2l1.6 4.1-2 1.4a12 12 0 0 0 5.1 5.1l1.4-2 4.1 1.6v2.2A2.4 2.4 0 0 1 16.5 21C9.8 20.4 3.6 14.2 3 7.5A2.4 2.4 0 0 1 6.6 3Z"/>',
    "pin": '<path d="M12 21s7-5.8 7-11a7 7 0 1 0-14 0c0 5.2 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3.2 1.9"/>',
    "check": '<path d="m4.5 12.5 5 5 10-11"/>',
    "check-circle": '<circle cx="12" cy="12" r="9"/><path d="m8 12.2 2.8 2.8L16.4 9"/>',
    "star": '<path d="m12 3.4 2.6 5.4 5.9.8-4.3 4.1 1 5.9-5.2-2.9-5.2 2.9 1-5.9L3.5 9.6l5.9-.8Z"/>',
    "wa": '<path d="M12 3a9 9 0 0 0-7.7 13.6L3 21.5l5-1.3A9 9 0 1 0 12 3Z"/><path d="M8.8 8.4c.3-.7.6-.7.9-.7h.7c.2 0 .5 0 .7.6l.8 1.9c.1.2.1.4 0 .6l-.5.7c-.2.2-.3.4-.1.7a6.6 6.6 0 0 0 2.9 2.4c.3.1.5.1.7-.1l.6-.8c.2-.2.4-.2.6-.1l1.9.9c.2.1.4.3.4.6a2.2 2.2 0 0 1-1.6 2c-.6.2-1.3.3-3.3-.6a11 11 0 0 1-4.5-4.4c-.8-1.6-.8-2.6-.6-3.2Z"/>',
    "shield": '<path d="M12 3 5.5 6v6c0 4.3 2.8 7.6 6.5 8.9 3.7-1.3 6.5-4.6 6.5-8.9V6Z"/><path d="m9.2 12 2 2 3.6-4"/>',
    "tooth": '<path d="M12 3.2c3.5 0 5.9 2.2 5.9 5.5 0 2.6-.8 3.9-1.3 6.2-.3 1.6-.4 4.3-1.9 4.3-1.2 0-1.3-2.4-2.7-2.4s-1.5 2.4-2.7 2.4c-1.5 0-1.6-2.7-1.9-4.3C6.9 12.6 6.1 11.3 6.1 8.7 6.1 5.4 8.5 3.2 12 3.2Z"/>',
    "spark": '<path d="M12 3v4.5M12 16.5V21M4.5 12H9M15 12h4.5"/><path d="m6.7 6.7 2.4 2.4M14.9 14.9l2.4 2.4M17.3 6.7l-2.4 2.4M9.1 14.9l-2.4 2.4"/>',
    "heart": '<path d="M12 20s-7-4.3-7-9.2A4.3 4.3 0 0 1 12 7.4a4.3 4.3 0 0 1 7 3.4C19 15.7 12 20 12 20Z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="16" rx="2.5"/><path d="M8 3v4M16 3v4M3.5 10h17"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><path d="M16 5.4a3.2 3.2 0 0 1 0 5.9M17.7 14.9c2 .6 3.3 2.3 3.3 5.1"/>',
    "eye": '<path d="M2.5 12S6 5.8 12 5.8 21.5 12 21.5 12 18 18.2 12 18.2 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>',
    "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8Z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    "close": '<path d="m6 6 12 12M18 6 6 18"/>',
    "play": '<path d="M8 5.5v13l11-6.5Z"/>',
    "pause": '<path d="M9 5v14M15 5v14"/>',
    "zoom": '<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5M11 8.5v5M8.5 11h5"/>',
    "car": '<path d="M5 16.5h14M6.5 16.5v2M17.5 16.5v2"/><path d="M4 16.5v-4l2-5h12l2 5v4Z"/><circle cx="8" cy="16.5" r="0"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
    "shield-heart": '<path d="M12 3 5.5 6v6c0 4.3 2.8 7.6 6.5 8.9 3.7-1.3 6.5-4.6 6.5-8.9V6Z"/><path d="M12 15s-2.6-1.6-2.6-3.4a1.6 1.6 0 0 1 2.6-1.2 1.6 1.6 0 0 1 2.6 1.2C14.6 13.4 12 15 12 15Z"/>',
    "phone-call": '<path d="M6.6 3h2.2l1.6 4.1-2 1.4a12 12 0 0 0 5.1 5.1l1.4-2 4.1 1.6v2.2A2.4 2.4 0 0 1 16.5 21C9.8 20.4 3.6 14.2 3 7.5A2.4 2.4 0 0 1 6.6 3Z"/><path d="M15 5.5a5 5 0 0 1 3.5 3.5"/>',
    "message": '<path d="M21 12a8.5 8.5 0 0 1-12.6 7.5L3.5 21l1.6-4.6A8.5 8.5 0 1 1 21 12Z"/>',
    "route": '<circle cx="6" cy="19" r="2.2"/><circle cx="18" cy="5" r="2.2"/><path d="M8.2 19h6.3a3.5 3.5 0 0 0 0-7H9.5a3.5 3.5 0 0 1 0-7h6.3"/>',
    "wallet": '<path d="M4 7.5A2.5 2.5 0 0 1 6.5 5H18a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H6.5A2.5 2.5 0 0 1 4 17.5Z"/><path d="M4 8.5h16"/><circle cx="16" cy="13.5" r="1.2"/>',
    "baby": '<circle cx="12" cy="8" r="4"/><path d="M5 21c0-3.6 3.1-6 7-6s7 2.4 7 6"/><path d="M10.5 7.5h.01M13.5 7.5h.01"/>',
    "crown": '<path d="M3.5 8.5 7 11l5-6 5 6 3.5-2.5V18H3.5Z"/><path d="M3.5 18h17"/>',
    "aligner": '<path d="M4 9.5c2.5-2 13.5-2 16 0 1.6 1.3 1.2 4.6-1 6.4-2.8 2.3-11.2 2.3-14 0-2.2-1.8-2.6-5.1-1-6.4Z"/><path d="M7.5 12.2c3-1 6-1 9 0"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "minus": '<path d="M5 12h14"/>',
    "arrow-down": '<path d="M12 4v15M6 13l6 6 6-6"/>',
    "arrow-left": '<path d="M20 12H5M11 6l-6 6 6 6"/>',
    "quote": '<path d="M9 7c-3 1.4-4.5 3.9-4.5 7.2 0 2.2 1.2 3.8 3.1 3.8 1.7 0 2.9-1.2 2.9-2.9 0-1.6-1.1-2.7-2.6-2.7-.3 0-.6 0-.8.1.3-1.4 1.2-2.5 2.6-3.4Zm8.4 0c-3 1.4-4.5 3.9-4.5 7.2 0 2.2 1.2 3.8 3.1 3.8 1.7 0 2.9-1.2 2.9-2.9 0-1.6-1.1-2.7-2.6-2.7-.3 0-.6 0-.8.1.3-1.4 1.2-2.5 2.6-3.4Z"/>',
    "calendar-check": '<rect x="3.5" y="5" width="17" height="16" rx="3"/><path d="M8 3v4M16 3v4M3.5 10h17M9 15.5l2 2 4-4"/>',
    "tooth-check": '<path d="M12 3.2c3.5 0 5.9 2.2 5.9 5.5 0 2.6-.8 3.9-1.3 6.2-.3 1.6-.4 4.3-1.9 4.3-1.2 0-1.3-2.4-2.7-2.4s-1.5 2.4-2.7 2.4c-1.5 0-1.6-2.7-1.9-4.3C6.9 12.6 6.1 11.3 6.1 8.7 6.1 5.4 8.5 3.2 12 3.2Z"/><path d="m9.4 9.6 1.8 1.8 3.4-3.6"/>',
}

NAV = [
    ("treatments.html", "Treatments"),
    ("reviews.html", "Reviews"),
    ("gallery.html", "Gallery"),
    ("about.html", "About"),
    ("contact.html", "Visit us"),
]

TREATMENTS = [
    ("treatments/dental-implants.html", "Dental implants", "A missing tooth, replaced"),
    ("treatments/root-canal.html", "Root canal treatment", "Save the tooth, not the bill"),
    ("treatments/braces-aligners.html", "Braces &amp; clear aligners", "Straighten, at any age"),
    ("treatments/smile-design.html", "Smile design &amp; veneers", "Shape before shade"),
    ("treatments.html#whitening", "Teeth whitening", "In-clinic or take-home"),
    ("treatments.html#crowns", "Crowns, bridges &amp; caps", "Rebuild what is worn"),
    ("treatments.html#wisdom", "Wisdom tooth removal", "The one people postpone"),
    ("treatments.html#hygiene", "Scaling &amp; gum care", "The six-month visit"),
]


def sprite():
    """One inline symbol sheet per page. Keeps icons consistent and the markup small."""
    syms = []
    for key, paths in ICONS.items():
        syms.append(
            '<symbol id="i-%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</symbol>' % (key, paths)
        )
    return ('<svg class="sprite" aria-hidden="true" width="0" height="0" '
            'style="position:absolute;width:0;height:0;overflow:hidden">%s</svg>' % "".join(syms))


def icon(name, cls=""):
    classes = ("i " + cls).strip()
    return '<svg class="%s" aria-hidden="true" focusable="false"><use href="#i-%s"></use></svg>' % (classes, name)


def stars(n=5):
    star = ('<svg viewBox="0 0 24 24" fill="currentColor" stroke="none" aria-hidden="true">'
            '<path d="m12 3.4 2.6 5.4 5.9.8-4.3 4.1 1 5.9-5.2-2.9-5.2 2.9 1-5.9L3.5 9.6l5.9-.8Z"/></svg>')
    return '<span class="stars" aria-label="5 out of 5 stars">%s</span>' % (star * n)


def wa_link(context, label, cls="btn btn--clay", extra=""):
    import urllib.parse
    text = context + "\n\n(Source: website · " + label + ")"
    href = SITE["wa_base"] + "?text=" + urllib.parse.quote(text)
    return '<a class="%s" href="%s" target="_blank" rel="noopener"%s>%s</a>' % (cls, href, extra, label)


# --------------------------------------------------------------------------
# Head
# --------------------------------------------------------------------------
def head(title, desc, path, depth=0, jsonld=None, og_image="assets/img/smile-portrait.jpg", preload=None):
    p = "../" * depth
    url = SITE["url"] + "/" + path if path else SITE["url"] + "/"
    abs_img = SITE["url"] + "/" + og_image
    ld = ""
    if jsonld:
        import json
        blocks = jsonld if isinstance(jsonld, list) else [jsonld]
        for b in blocks:
            ld += '<script type="application/ld+json">%s</script>\n' % json.dumps(b, ensure_ascii=False)
    pre = ""
    if preload:
        pre = '<link rel="preload" as="image" href="%sassets/img/%s" fetchpriority="high">\n' % (p, preload)
    return """<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#ffffff">
<meta name="color-scheme" content="light">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="format-detection" content="telephone=no">
<meta name="geo.region" content="IN-GJ">
<meta name="geo.placename" content="Nikol, Ahmedabad">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{full}">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">

<link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
{pre}<link rel="stylesheet" href="{p}assets/css/site.css">
<script>document.documentElement.className+=" js";</script>
{ld}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" data-progress aria-hidden="true"></div>
""".format(title=title, desc=desc, url=url, img=abs_img, p=p, pre=pre, ld=ld,
           full=SITE["full"])


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------
def topbar():
    return """<div class="topbar">
  <div class="shell topbar__in">
    <div class="topbar__group topbar__group--addr">
      <span class="topbar__item">{pin}<span>Shop 214, Blueberry Complex · Nikol</span></span>
    </div>
    <div class="topbar__group">
      <span class="status" data-status data-open="false"><i class="status__dot"></i><span class="status__long" data-status-text>Mon–Sat, 9 AM – 9 PM</span><span class="status__short" data-status-short>9 AM – 9 PM</span></span>
      <a class="topbar__item" href="{tel}">{phone_icon}<span>{phone}</span></a>
    </div>
  </div>
</div>
""".format(pin=icon("pin"), tel=TEL, phone_icon=icon("phone"), phone=SITE["phone_display"])


def brand(p=""):
    return """<a class="brand" href="{p}index.html" aria-label="{full} — home">
  <svg class="brand__mark" viewBox="0 0 24 28" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="M12 1.8c4 0 6.8 2.5 6.8 6.3 0 3-1 4.5-1.5 7.2-.4 1.9-.5 5-2.2 5-1.4 0-1.5-2.8-3.1-2.8s-1.7 2.8-3.1 2.8c-1.7 0-1.8-3.1-2.2-5C6.2 12.6 5.2 11.1 5.2 8.1 5.2 4.3 8 1.8 12 1.8Z"/>
    <path d="M9.1 7.4c.7-.7 1.8-1 2.9-1"/>
  </svg>
  <span class="brand__text">
    <span class="brand__name">Smilecraft</span>
    <span class="brand__sub">Dental · Nikol</span>
  </span>
</a>""".format(p=p, full=SITE["full"])


def header(active="", depth=0):
    p = "../" * depth
    links = []
    for href, label in NAV:
        if href == "treatments.html":
            items = "".join(
                '<a href="%s%s"><span><b>%s</b><span>%s</span></span></a>' % (p, h, t, s)
                for h, t, s in TREATMENTS
            )
            cur = ' aria-current="page"' if active == "treatments" else ""
            links.append(
                '<div class="nav__item" data-dropdown>'
                '<button class="nav__trigger" aria-expanded="false" aria-haspopup="true">Treatments %s</button>'
                '<div class="dropdown">%s</div></div>' % (icon("chevron"), items)
            )
            continue
        cur = ' aria-current="page"' if active == href else ""
        links.append('<a class="nav__link" href="%s%s"%s>%s</a>' % (p, href, cur, label))

    return """<header class="header" data-header>
  <div class="shell header__in">
    {brand}
    <nav class="nav" aria-label="Primary">{links}</nav>
    <div class="header__cta">
      <span class="hdr-status status" data-status data-open="false"><i class="status__dot"></i><span data-status-text>Mon–Sat, 9 AM – 9 PM</span></span>
      <a class="btn btn--ghost btn--sm" href="{tel}">{phone}<span>Call</span></a>
      <a class="btn btn--sm" href="{p}book.html">Book a visit</a>
    </div>
    <button class="burger" data-menu-open aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><span></span></button>
  </div>
</header>

<div class="drawer" id="drawer" data-drawer>
  <div class="drawer__top">
    {brand_d}
    <button class="drawer__close" data-menu-close aria-label="Close menu">{close}</button>
  </div>
  <nav class="drawer__nav" aria-label="Mobile">
    <a href="{p}index.html">Home <small>01</small></a>
    <a href="{p}treatments.html">Treatments <small>02</small></a>
    <a href="{p}reviews.html">Reviews <small>03</small></a>
    <a href="{p}gallery.html">Gallery <small>04</small></a>
    <a href="{p}about.html">About <small>05</small></a>
    <a href="{p}first-visit.html">First visit <small>06</small></a>
    <a href="{p}contact.html">Visit us <small>07</small></a>
    <a href="{p}faq.html">FAQ <small>08</small></a>
  </nav>
  <div class="drawer__foot">
    <a class="btn btn--light btn--wide" href="{p}book.html">Book a visit</a>
    <a class="btn btn--outline-light btn--wide" href="{tel}">Call {phone_display}</a>
    <div class="drawer__meta">
      <span>{street}</span>
      <span>{street2}</span>
      <span>{city}</span>
      <span>Mon–Sat, 9 AM – 9 PM · closed Sunday</span>
    </div>
  </div>
</div>
""".format(brand=brand(p), brand_d=brand(p), links="".join(links), tel=TEL,
           phone=icon("phone"), close=icon("close"), p=p,
           phone_display=SITE["phone_display"], street=SITE["street"],
           street2=SITE["street2"], city=SITE["city"])


def footer(depth=0):
    p = "../" * depth
    return """<footer class="footer">
  <div class="shell">
    <div class="footer__grid">
      <div>
        {brand}
        <p class="footer__blurb">A multispeciality dental clinic and implant centre on the second floor of Blueberry Complex, Nikol. Quiet rooms, written plans, and appointments that start on time.</p>
        <div class="pill-row mt-3">
          <span class="chip chip--live">{star} {rating} · {count} Google reviews</span>
        </div>
      </div>
      <div class="footer__col">
        <h4><svg class="i" aria-hidden="true"><use href="#i-tooth"></use></svg> Treatments</h4>
        <ul>
          <li><a href="{p}treatments/dental-implants.html">Dental implants</a></li>
          <li><a href="{p}treatments/root-canal.html">Root canal treatment</a></li>
          <li><a href="{p}treatments/braces-aligners.html">Braces &amp; aligners</a></li>
          <li><a href="{p}treatments/smile-design.html">Smile design</a></li>
          <li><a href="{p}treatments.html">All treatments</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4><svg class="i" aria-hidden="true"><use href="#i-info"></use></svg> Clinic</h4>
        <ul>
          <li><a href="{p}about.html">About the clinic</a></li>
          <li><a href="{p}first-visit.html">Your first visit</a></li>
          <li><a href="{p}reviews.html">Patient reviews</a></li>
          <li><a href="{p}gallery.html">Gallery</a></li>
          <li><a href="{p}faq.html">Questions</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Visit</h4>
        <ul>
          <li>{street}</li>
          <li>{street2}</li>
          <li>{city}</li>
          <li class="mt-1"><a href="{tel}">{phone}</a></li>
          <li><a href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp the clinic</a></li>
          <li class="mt-1">Mon–Sat · 9:00 AM – 9:00 PM<br>Sunday closed</li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> {full}. All rights reserved.</span>
      <div class="footer__legal">
        <a href="{p}privacy.html">Privacy &amp; consent</a>
        <a href="{p}contact.html">Directions</a>
        <a href="{p}book.html">Book</a>
      </div>
    </div>
  </div>
</footer>
""".format(brand=brand(p), p=p, star=icon("star"), rating=SITE["rating"],
           count=SITE["review_count"], street=SITE["street"], street2=SITE["street2"],
           city=SITE["city"], tel=TEL, phone=SITE["phone_display"], wa=SITE["wa"],
           full=SITE["full"])


def widgets(depth=0):
    p = "../" * depth
    return """<div class="grain" aria-hidden="true"></div>
<div class="veil" data-veil-box aria-hidden="true"></div>
<span class="side-label side-label--l" aria-hidden="true">Nikol · Ahmedabad 380049</span>
<span class="side-label side-label--r" aria-hidden="true">Blueberry Complex · 2nd floor</span>

<a class="book-pill" href="{p}book.html" data-book-pill aria-label="Book an appointment">
  <span>Book a visit</span>{cal}
</a>

<a class="wa-float" href="{wa}?text={msg}" target="_blank" rel="noopener" aria-label="Message the clinic on WhatsApp">
  {wa_icon}<span class="wa-float__label">Message the clinic</span>
</a>

<nav class="mobile-bar" aria-label="Quick actions">
  <a href="{tel}">{phone}<span>Call</span></a>
  <a href="{wa}?text={msg}" target="_blank" rel="noopener">{wa_icon}<span>WhatsApp</span></a>
  <a href="{p}book.html" data-primary="true">{cal}<span>Book</span></a>
</nav>

<aside class="leadcard" data-leadcard aria-label="Request a callback">
  <button class="leadcard__close" data-leadcard-close aria-label="Close">{close}</button>
  <h3>Would a call back be easier?</h3>
  <p>Leave a number and the clinic will ring you during opening hours. No forms to chase, no email needed.</p>
  <form data-lead-form="callback" novalidate>
    <div class="field">
      <label class="field__label" for="lc-name">Your name</label>
      <input class="input" id="lc-name" name="name" autocomplete="name" data-required>
      <span class="field__error" data-error></span>
    </div>
    <div class="field">
      <label class="field__label" for="lc-phone">Mobile number</label>
      <input class="input" id="lc-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" data-required data-validate="phone">
      <span class="field__error" data-error></span>
    </div>
    <button class="btn btn--wide" type="submit"><span>Send on WhatsApp</span>{arrow}</button>
    <p class="leadcard__foot">This opens WhatsApp with your message ready to send. We only use the number to reply to this enquiry.</p>
  </form>
</aside>
""".format(wa=SITE["wa_base"], msg="Hello%20Smilecraft%2C%20I%20would%20like%20to%20ask%20about%20an%20appointment.",
           tel=TEL, phone=icon("phone"), wa_icon=icon("wa"), cal=icon("calendar"),
           arrow=icon("arrow"), close=icon("close"), p=p)


def cta_band(title_html, text, depth=0, eyebrow="Appointments"):
    p = "../" * depth
    return """<section class="section section--cta" aria-labelledby="cta-h">
  <div class="shell">
    <div class="cta">
      <div class="cta__body">
        <span class="eyebrow eyebrow--plain" style="color:rgba(255,253,248,.6)">{eyebrow}</span>
        <h2 class="h2 mt-2" id="cta-h">{title}</h2>
        <p>{text}</p>
      </div>
      <div class="cta__actions">
        <a class="btn btn--clay" href="{p}book.html"><span>Book a visit</span>{arrow}</a>
        <a class="btn btn--outline-light" href="{wa}" target="_blank" rel="noopener">{wa_icon}<span>WhatsApp</span></a>
      </div>
    </div>
  </div>
</section>
""".format(eyebrow=eyebrow, title=title_html, text=text, p=p, arrow=icon("arrow"),
           wa=SITE["wa_base"] + "?text=Hello%20Smilecraft%2C%20I%20would%20like%20to%20book%20an%20appointment.",
           wa_icon=icon("wa"))


def crumbs(items, depth=0):
    """items: [(label, href or None)]"""
    p = "../" * depth
    out = []
    for i, (label, href) in enumerate(items):
        if href:
            out.append('<a href="%s%s">%s</a>' % (p, href, label))
        else:
            out.append('<span aria-current="page">%s</span>' % label)
        if i < len(items) - 1:
            out.append('<i aria-hidden="true">/</i>')
    return '<nav class="crumbs" aria-label="Breadcrumb">%s</nav>' % "".join(out)


def page(title, desc, path, body, active="", depth=0, jsonld=None, og_image="assets/img/smile-portrait.jpg", preload=None):
    return (head(title, desc, path, depth, jsonld, og_image, preload)
            + sprite() + header_v2(active, depth)
            + '<main id="main">' + body + "</main>"
            + footer_v2(depth) + widgets(depth)
            + '<script src="%sassets/js/site.js" defer></script>\n' % ("../" * depth)
            + '<script src="%sassets/js/lead.js" defer></script>\n' % ("../" * depth)
            + '<script src="%sassets/js/motion.js" defer></script>\n' % ("../" * depth)
                        + '<script src="%sassets/js/scrollfx.js" defer></script>\n' % ("../" * depth)
            + "</body>\n</html>\n")


def footer_v2(depth=0):
    """Compact graphite footer: CTA row, four columns with icons, wordmark, legal row."""
    p = "../" * depth
    return """<footer class="footer">
  <div class="shell">
    <div class="footer__panel">
      <div class="footer__cta">
        <div>
          <span class="eyebrow eyebrow--plain footer__eyebrow">Appointments</span>
          <h2 class="footer__h">Book the visit you have been putting off.</h2>
        </div>
        <div class="footer__cta-actions">
          <a class="btn btn--light" href="{p}book.html"><span>Book a visit</span>{arrow}</a>
          <a class="btn btn--outline-light" href="{wa}" target="_blank" rel="noopener">{wa_icon}<span>WhatsApp</span></a>
        </div>
      </div>

      <div class="footer__grid">
        <div class="footer__brand">
          {brand}
          <p class="footer__blurb">A multispeciality dental clinic and implant centre on the second floor of Blueberry Complex, Nikol. Quiet rooms, written plans, and appointments that start on time.</p>
          <div class="pill-row mt-2">
            <span class="chip chip--live">{star} {rating} · {count} Google reviews</span>
          </div>
        </div>
        <div class="footer__col">
          <h4><svg class="i" aria-hidden="true"><use href="#i-tooth"></use></svg> Treatments</h4>
          <ul>
            <li><a href="{p}treatments/dental-implants.html">Dental implants</a></li>
            <li><a href="{p}treatments/root-canal.html">Root canal treatment</a></li>
            <li><a href="{p}treatments/braces-aligners.html">Braces &amp; aligners</a></li>
            <li><a href="{p}treatments/smile-design.html">Smile design</a></li>
            <li><a href="{p}treatments.html">All treatments</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h4><svg class="i" aria-hidden="true"><use href="#i-info"></use></svg> Clinic</h4>
          <ul>
            <li><a href="{p}about.html">About the clinic</a></li>
            <li><a href="{p}first-visit.html">Your first visit</a></li>
            <li><a href="{p}reviews.html">Patient reviews</a></li>
            <li><a href="{p}gallery.html">Gallery</a></li>
            <li><a href="{p}faq.html">Questions</a></li>
          </ul>
        </div>
        <div class="footer__col footer__col--contact">
          <h4><svg class="i" aria-hidden="true"><use href="#i-pin"></use></svg> Find us</h4>
          <ul class="contact-list">
            <li>{pin}<span>{street}<br>{street2}<br>{city}</span></li>
            <li>{phone_icon}<a href="{tel}">{phone}</a></li>
            <li>{clock}<span>Mon–Sat · 9:00 AM – 9:00 PM<br>Sunday closed</span></li>
          </ul>
        </div>
      </div>

      <div class="footer__word" aria-hidden="true">Smilecraft</div>

      <div class="footer__bottom">
        <span>&copy; <span data-year>2026</span> {full}</span>
        <div class="footer__legal">
          <a href="{p}privacy.html">Privacy</a>
          <a href="{p}contact.html">Directions</a>
          <a href="{p}faq.html">FAQ</a>
          <a href="#" data-top>Back to top &uarr;</a>
        </div>
      </div>
    </div>
  </div>
</footer>
""".format(
        brand=brand(p), p=p, arrow=icon("arrow"), wa_icon=icon("wa"),
        wa=SITE["wa_base"] + "?text=Hello%20Smilecraft%2C%20I%20would%20like%20to%20book%20an%20appointment.",
        star=icon("star"), rating=SITE["rating"], count=SITE["review_count"],
        pin=icon("pin"), phone_icon=icon("phone"), clock=icon("clock"),
        tel=TEL, phone=SITE["phone_display"], street=SITE["street"],
        street2=SITE["street2"], city=SITE["city"], full=SITE["full"],
    )


def header_v2(active="", depth=0):
    """Floating dock header: one rounded glass bar instead of two stacked strips."""
    p = "../" * depth
    links = []
    for href, label in NAV:
        if href == "treatments.html":
            items = "".join(
                '<a href="%s%s"><span><b>%s</b><span>%s</span></span></a>' % (p, h, t, s)
                for h, t, s in TREATMENTS
            )
            cur = ' aria-current="page"' if active == "treatments" else ""
            links.append(
                '<div class="nav__item" data-dropdown>'
                '<button class="nav__trigger" aria-expanded="false" aria-haspopup="true">Treatments %s</button>'
                '<div class="dropdown">%s</div></div>' % (icon("chevron"), items)
            )
            continue
        cur = ' aria-current="page"' if active == href else ""
        links.append('<a class="nav__link" href="%s%s"%s>%s</a>' % (p, href, cur, label))

    return """<header class="dock" data-header>
  <div class="shell dock__shell">
    <div class="dock__bar">
      {brand}
      <nav class="nav dock__nav" aria-label="Primary">{links}</nav>
      <div class="dock__cta">
        <span class="hdr-status status" data-status data-open="false"><i class="status__dot"></i><span data-status-text>Mon-Sat, 9 AM - 9 PM</span></span>
        <a class="dock__icon" href="{tel}" aria-label="Call the clinic">{phone}</a>
        <a class="btn btn--sm dock__book" href="{p}book.html">Book</a>
        <button class="burger" data-menu-open aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><span></span></button>
      </div>
    </div>
  </div>
</header>

<div class="drawer" id="drawer" data-drawer>
  <div class="drawer__top">
    {brand_d}
    <button class="drawer__close" data-menu-close aria-label="Close menu">{close}</button>
  </div>
  <nav class="drawer__nav" aria-label="Mobile">
    <a href="{p}index.html">Home <small>01</small></a>
    <a href="{p}treatments.html">Treatments <small>02</small></a>
    <a href="{p}reviews.html">Reviews <small>03</small></a>
    <a href="{p}gallery.html">Gallery <small>04</small></a>
    <a href="{p}about.html">About <small>05</small></a>
    <a href="{p}first-visit.html">First visit <small>06</small></a>
    <a href="{p}contact.html">Visit us <small>07</small></a>
    <a href="{p}faq.html">FAQ <small>08</small></a>
  </nav>
  <div class="drawer__foot">
    <a class="btn btn--light btn--wide" href="{p}book.html">Book a visit</a>
    <a class="btn btn--outline-light btn--wide" href="{tel}">Call {phone_display}</a>
    <div class="drawer__meta">
      <span>{street}</span>
      <span>{street2}</span>
      <span>{city}</span>
      <span>Mon-Sat, 9 AM - 9 PM · closed Sunday</span>
    </div>
  </div>
</div>
""".format(brand=brand(p), brand_d=brand(p), links="".join(links), tel=TEL,
           phone=icon("phone"), close=icon("close"), p=p,
           phone_display=SITE["phone_display"], street=SITE["street"],
           street2=SITE["street2"], city=SITE["city"])


