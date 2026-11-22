# -*- coding: utf-8 -*-
"""Home page — recomposed: fewer sections, no repeated imagery, denser blocks."""
from chrome import SITE, TEL, icon, stars, page, cta_band

PICKER = [
    ("Toothache", "toothache",
     "A tooth that wakes you up at night usually means the nerve is involved.",
     "Most toothaches here are a deep cavity or an inflamed nerve. We take an X-ray on the first visit, tell you what it shows, and give you two options: settle it, or remove it.",
     ["Root canal", "Deep filling", "X-ray on day one"], "treatments/root-canal.html", "Root canal treatment"),
    ("Sensitive teeth", "sensitivity",
     "Cold water, hot tea, a sharp second of pain.",
     "Sensitivity is usually worn enamel, a receded gum line, or a tiny crack. It is rarely an emergency and almost always treatable without drilling half the tooth away.",
     ["Gum check", "Desensitising", "Sealant"], "treatments.html#hygiene", "Scaling &amp; gum care"),
    ("A missing tooth", "missing",
     "One gap changes how the rest of the bite wears.",
     "A bridge is faster, an implant keeps the neighbouring teeth untouched. We show you both, with the honest difference in cost, time and how long each lasts.",
     ["Implant", "Bridge", "Bone check"], "treatments/dental-implants.html", "Dental implants"),
    ("Crooked or crowded", "crooked",
     "At fourteen or at forty, the mechanics are the same.",
     "Metal, ceramic or clear aligners — the right one depends on how much movement is needed and how visible you are willing to be. Records first, then a written timeline.",
     ["Braces", "Aligners", "Retainers"], "treatments/braces-aligners.html", "Braces &amp; aligners"),
    ("Stained or chipped", "stained",
     "Colour is the last decision, not the first.",
     "Whitening lifts the shade of your own teeth. Veneers change shape as well. Doing the second when the first would have been enough is the expensive mistake.",
     ["Whitening", "Veneers", "Smile design"], "treatments/smile-design.html", "Smile design"),
    ("Child's first visit", "child",
     "The first visit should be boring, on purpose.",
     "No drill, no surprise. The child sits in the chair, counts their own teeth in the mirror, and leaves. A short first appointment makes the second one easy.",
     ["Fluoride", "Sealants", "Habit advice"], "book.html?treatment=Child%27s%20first%20visit", "Book a first visit"),
]


def build():
    ICONS_FOR = {"toothache": "tooth", "sensitivity": "spark", "missing": "crown", "crooked": "aligner", "stained": "spark", "child": "baby"}
    SUBS = {"toothache": "Wakes you at night", "sensitivity": "Cold and heat", "missing": "A gap in the bite",
            "crooked": "Crowded or spaced", "stained": "Colour and chips", "child": "First appointment"}

    picker_tabs = "".join(
        '<button class="triage__row" role="tab" id="tab-%s" aria-controls="panel-%s" aria-selected="%s" tabindex="%s">'
        '<span class="triage__ico">%s</span>'
        '<span class="triage__txt"><b>%s</b><i>%s</i></span>'
        '<span class="triage__chev">%s</span></button>'
        % (key, key, "true" if i == 0 else "false", "0" if i == 0 else "-1",
           icon(ICONS_FOR.get(key, "tooth")), label, SUBS.get(key, ""), icon("chevron-r"))
        for i, (label, key, _, _, _, _, _) in enumerate(PICKER)
    )
    picker_panels = "".join(
        '<div class="triage__panel" role="tabpanel" id="panel-%s" aria-labelledby="tab-%s" data-active="%s">'
        '<span class="triage__no">%02d</span>'
        '<h3>%s</h3><p>%s</p>'
        '<div class="triage__tags">%s</div>'
        '<div class="triage__actions"><a class="btn" href="%s"><span>%s</span>%s</a>'
        '<a class="btn btn--ghost" href="book.html?treatment=%s">Book for this</a></div></div>'
        % (key, key, "true" if i == 0 else "false", i + 1, headline, text,
           "".join('<span class="chip">%s</span>' % t for t in tags),
           link, link_label, icon("arrow"), key)
        for i, (label, key, headline, text, tags, link, link_label) in enumerate(PICKER)
    )

    body = f"""
<section class="hero hero--collage">
  <div class="shell hero__inner">
    <div class="hero__copy">
      <span class="eyebrow">Nikol, Ahmedabad · Implant centre</span>
      <h1 class="h1" data-split>A calmer kind<br>of <span class="serif">dentist visit</span>.</h1>
      <p class="lead hero__lead">Implants, root canals, braces and everyday dentistry on the second floor of Blueberry Complex — with a written plan before anything begins.</p>
      <div class="hero__actions">
        <a class="btn" href="book.html" data-magnetic><span>Book a visit</span>{icon("arrow")}</a>
        <a class="btn btn--ghost" href="{SITE['wa_base']}?text=Hello%20Smilecraft%2C%20I%20would%20like%20to%20ask%20about%20a%20visit." target="_blank" rel="noopener">{icon("wa")}<span>WhatsApp</span></a>
      </div>
      <div class="hero__trust">
        <span class="flex items-center gap-1">{stars()} <b>{SITE['rating']}</b> <span class="muted">{SITE['review_count']} reviews</span></span>
        <span><b>Mon–Sat</b> 9–9</span>
        <span>Shop 214 · 2nd floor</span>
      </div>
    </div>

    <div class="hero__collage">
      <figure class="hero__film" data-video data-parallax="0.03">
        <video src="assets/video/hero-loop.mp4" poster="assets/img/hero-poster.jpg" autoplay muted loop playsinline preload="metadata" data-managed aria-label="A slow look around the treatment room"></video>
        <button class="video-pill" type="button" data-video-btn aria-label="Pause the background film">{icon("pause")}<span data-video-label>Pause</span></button>
      </figure>
      <div class="hero__chip hero__chip--rating">
        <b>{SITE['rating']}</b>{stars()}<span>{SITE['review_count']} Google reviews</span>
      </div>
      <div class="hero__chip hero__chip--live">
        <span class="status" data-status data-open="false"><i class="status__dot"></i><span data-status-text>Mon–Sat, 9 AM – 9 PM</span></span>
      </div>
      <figure class="hero__thumb">
        <img src="assets/img/smile-portrait.jpg" width="320" height="320" alt="A patient at the clinic" loading="lazy">
      </figure>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee__track">
    <div class="marquee__set"><span>Dental implants</span><span>Root canals</span><span>Clear aligners</span><span>Smile design</span><span>Whitening</span><span>Crowns</span><span>Wisdom teeth</span><span>Gum care</span></div>
    <div class="marquee__set"><span>Dental implants</span><span>Root canals</span><span>Clear aligners</span><span>Smile design</span><span>Whitening</span><span>Crowns</span><span>Wisdom teeth</span><span>Gum care</span></div>
  </div>
</div>

<section class="section section--tight" id="glance">
  <div class="shell">
    <div class="bento bento--five" data-reveal-group>
      <div class="bento__tile bento__tile--wide" data-reveal>
        {icon("star")}
        <div class="bento__num">{SITE['rating']}</div>
        {stars()}
        <div class="bento__label">From {SITE['review_count']} Google reviews</div>
        <a class="link-arrow mt-1" href="reviews.html">Read them {icon("arrow")}</a>
      </div>
      <div class="bento__tile" data-reveal>
        {icon("tooth-check")}
        <div class="bento__num">8</div>
        <div class="bento__label">Treatments, one roof</div>
      </div>
      <div class="bento__tile" data-reveal>
        {icon("clock")}
        <div class="bento__num">9–9</div>
        <div class="bento__label">Mon–Sat · closed Sunday</div>
      </div>
      <div class="bento__tile" data-reveal>
        {icon("file")}
        <div class="bento__label"><b>Written plan</b><br>before we start</div>
      </div>
      <div class="bento__tile" data-reveal>
        {icon("shield")}
        <div class="bento__label"><b>Single-use</b><br>opened in front of you</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" aria-labelledby="picker-h">
  <div class="shell">
    <div class="section-head">
      <div>
        <div class="mark"><b>01</b> Start here</div>
        <h2 class="h2" id="picker-h">What is bothering you most right now?</h2>
      </div>
      <div class="section-head__aside">
        <p class="small muted">Pick the closest one. A plain answer about what it usually means, with no sign-up and no phone number required.</p>
      </div>
    </div>
    <div class="triage" data-picker data-reveal>
      <div class="triage__list" role="tablist" aria-label="Common dental problems">{picker_tabs}</div>
      <div class="triage__panels">{picker_panels}</div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="svc-h">
  <div class="shell">
    <div class="section-head">
      <div>
        <div class="mark"><b>02</b> Treatments</div>
        <h2 class="h2" id="svc-h">Everything under one roof.</h2>
      </div>
      <div class="section-head__aside">
        <p class="small muted">One clinic, one set of records, one dentist who knows the whole picture.</p>
        <a class="link-arrow mt-2" href="treatments.html">All eight {icon("arrow")}</a>
      </div>
    </div>

    <div class="grid g-3" data-reveal-group>
      <a class="svc" href="treatments/dental-implants.html" data-reveal>
        <div class="svc__media"><img src="assets/img/gen-implant.jpg" width="640" height="480" alt="Implant model and planning X-ray" loading="lazy"></div>
        <div class="svc__body"><h3>Dental implants</h3><p>A missing tooth, replaced without touching the neighbours.</p><span class="svc__foot">Read more {icon("arrow")}</span></div>
      </a>
      <a class="svc" href="treatments/root-canal.html" data-reveal>
        <div class="svc__media"><img src="assets/img/xray-review.jpg" width="640" height="480" alt="Dentist reviewing a dental X-ray" loading="lazy"></div>
        <div class="svc__body"><h3>Root canal</h3><p>Saving the tooth you have, properly isolated.</p><span class="svc__foot">Read more {icon("arrow")}</span></div>
      </a>
      <a class="svc" href="treatments/braces-aligners.html" data-reveal>
        <div class="svc__media"><img src="assets/img/aligner-vs-braces.jpg" width="640" height="480" alt="Clear aligner and braces" loading="lazy"></div>
        <div class="svc__body"><h3>Braces &amp; aligners</h3><p>Metal, ceramic or clear, at fourteen or forty.</p><span class="svc__foot">Read more {icon("arrow")}</span></div>
      </a>
      <a class="svc" href="treatments/smile-design.html" data-reveal>
        <div class="svc__media"><img src="assets/img/smile-macro.jpg" width="640" height="480" alt="Close-up of finished front teeth" loading="lazy"></div>
        <div class="svc__body"><h3>Smile design</h3><p>Shape planned before anything is made.</p><span class="svc__foot">Read more {icon("arrow")}</span></div>
      </a>
      <a class="svc" href="treatments.html#whitening" data-reveal>
        <div class="svc__media"><img src="assets/img/smile-woman.jpg" width="640" height="480" alt="A bright smile after whitening" loading="lazy"></div>
        <div class="svc__body"><h3>Whitening</h3><p>In-clinic with shade records, or a slower kit.</p><span class="svc__foot">Read more {icon("arrow")}</span></div>
      </a>
      <a class="svc" href="treatments.html#hygiene" data-reveal>
        <div class="svc__media"><img src="assets/img/gen-operatory.jpg" width="640" height="480" alt="The treatment room" loading="lazy"></div>
        <div class="svc__body"><h3>Check-ups &amp; hygiene</h3><p>The six-month visit that keeps this list short.</p><span class="svc__foot">Read more {icon("arrow")}</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section section--pine" id="work-h" aria-labelledby="why-h">
  <div class="shell">
    <div class="work">
      <div class="work__lead">
        <div class="mark"><b>03</b> How we work</div>
        <p class="quote-large" id="why-h">We would rather save your tooth than <em>sell you an implant</em>.</p>
        <a class="link-arrow mt-2" href="about.html" style="color:#fff">About the clinic {icon("arrow")}</a>
      </div>
      <div class="work__pillars">
        <div><span class="work__ico">{icon("file")}</span><b>Written before we start</b><p>What is done, how many visits, what it costs. On paper, before the first instrument opens.</p></div>
        <div><span class="work__ico">{icon("shield")}</span><b>Single-use, always</b><p>Needles, gloves, suction tips, bibs. Wrapped, dated, opened in front of you.</p></div>
        <div><span class="work__ico">{icon("wallet")}</span><b>Nothing on commission</b><p>No targets, no packages. If the honest answer is watch it, that is the answer.</p></div>
      </div>
      <div class="work__steps">
        <div><span>01</span><b>We look, properly</b><p>History, exam, and an X-ray of the area in question.</p></div>
        <div><span>02</span><b>You get a plan</b><p>Options in plain language, with the trade-offs and the cost of each.</p></div>
        <div><span>03</span><b>Treatment, at your pace</b><p>Then a review, and a number to message if something feels wrong.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="dr-h">
  <div class="shell">
    <div class="doctor">
      <figure class="doctor__media" data-tilt>
        <img src="assets/img/gen-doctor.jpg" width="900" height="1100" alt="Dentist treating a patient in the consultation room" loading="eager" style="object-position:50% 32%">
        <figcaption>{icon("shield")} Single-use, opened in front of you</figcaption>
        <span class="doctor__badge">{icon("tooth-check")} Consultation room</span>
      </figure>
      <div class="doctor__body">
        <div class="mark"><b>04</b> The dentist you will see</div>
        <h2 class="h2" id="dr-h">Dr Priya Patel</h2>
        <div class="doctor__quote">
          <span class="doctor__qmark">{icon("quote")}</span>
          <p>“She explained the X-ray before recommending anything.” That sentence, in different words, is in most of the reviews.</p>
        </div>
        <div class="doctor__meta">
          <div><span>Focus</span><b>Root canals, implants, smile design</b></div>
          <div><span>Languages</span><b>Gujarati, Hindi, English</b></div>
          <div><span>Registration</span><b>Ask at reception</b></div>
        </div>
        <div class="doctor__actions">
          <a class="btn" href="book.html"><span>Book a visit</span>{icon("arrow")}</a>
          <a class="btn btn--ghost" href="about.html">About the clinic</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" aria-labelledby="rev-h">
  <div class="shell">
    <div class="revband">
      <div class="revband__score">
        <b>{SITE['rating']}</b>
        {stars()}
        <span class="tiny muted">{SITE['review_count']} Google reviews</span>
      </div>
      <div class="revband__quotes">
        <p>“If you want high-quality dental care with zero pain, this is the place to go.”</p>
        <p>“Doctor has given perfect explanation and treatment advice.”</p>
        <p>“From the moment I walked in, the staff was warm, welcoming, and incredibly professional.”</p>
      </div>
      <div class="revband__side">
        <a class="btn btn--ghost btn--sm" href="reviews.html">All reviews</a>
        <a class="link-arrow" href="{SITE['review']}" target="_blank" rel="noopener">Leave one {icon("arrow-up-right")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" aria-labelledby="visit-h">
  <div class="shell">
    <div class="section-head">
      <div>
        <div class="mark"><b>05</b> Finding us</div>
        <h2 class="h2" id="visit-h">Second floor, above the handloom showroom.</h2>
      </div>
      <div class="section-head__aside">
        <p class="small muted">Blueberry Complex on Virat Nagar Road, Nikol. Shop 214, one level up from the showroom.</p>
      </div>
    </div>

    <div class="visit">
      <div class="mapx">
        <img class="mapx__img" src="assets/img/map-nikol.jpg" width="900" height="610" alt="Map showing the clinic on Virat Nagar Road" loading="lazy">
        <span class="mapx__sonar" aria-hidden="true"></span>
        <span class="mapx__pulse" aria-hidden="true"></span>
        <span class="mapx__pin">{icon("pin")}<b>Shop 214</b></span>
        <div class="mapx__chips">
          <span class="mapx__chip">{icon("route")} Virat Nagar Road</span>
          <span class="mapx__chip">{icon("pin")} Beside Bhojaldham Society</span>
        </div>
        <a class="mapx__cta btn btn--sm" href="{SITE['dir']}" target="_blank" rel="noopener">{icon("route")}<span>Directions</span></a>
      </div>
      <div class="visit__info">
        <div class="visit__row">{icon("pin")}<div><b>Address</b><span>{SITE['street']}<br>{SITE['street2']}<br>{SITE['city']}</span></div></div>
        <div class="visit__row">{icon("clock")}<div><b>Hours</b><span>Mon–Sat 9:00 AM – 9:00 PM<br>Sunday closed</span></div></div>
        <div class="visit__row">{icon("phone")}<div><b>Phone</b><a href="{TEL}">{SITE['phone_display']}</a></div></div>
        <div class="visit__row">{icon("route")}<div><b>Directions</b><a href="{SITE['dir']}" target="_blank" rel="noopener">Open in Google Maps</a></div></div>
        <div class="visit__actions">
          <a class="btn btn--sm" href="book.html"><span>Book</span>{icon("arrow")}</a>
          <a class="btn btn--ghost btn--sm" href="{TEL}">{icon("phone")}<span>Call</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="faq-h">
  <div class="shell">
    <div class="section-head">
      <div>
        <div class="mark"><b>06</b> Before you come</div>
        <h2 class="h2" id="faq-h">The questions people ask on the phone.</h2>
      </div>
      <div class="section-head__aside"><a class="link-arrow" href="faq.html">All questions {icon("arrow")}</a></div>
    </div>

    <div class="faq faq--2" data-faq data-reveal>
      <div class="faq__item" data-open="false">
        <button class="faq__q" aria-expanded="false">Does it hurt?<i aria-hidden="true"></i></button>
        <div class="faq__a"><div>Most procedures are under local anaesthetic, with a numbing gel first. “Painless” is the word patients use most, and it is not an accident.</div></div>
      </div>
      <div class="faq__item" data-open="false">
        <button class="faq__q" aria-expanded="false">What does treatment cost?<i aria-hidden="true"></i></button>
        <div class="faq__a"><div>A written estimate after the X-ray, and no additions without asking. We do not publish a fee list that would be wrong half the time.</div></div>
      </div>
      <div class="faq__item" data-open="false">
        <button class="faq__q" aria-expanded="false">Do I need an appointment?<i aria-hidden="true"></i></button>
        <div class="faq__a"><div>For anything planned, yes. Walk-ins are seen when there is a gap, but booked patients and emergencies come first.</div></div>
      </div>
      <div class="faq__item" data-open="false">
        <button class="faq__q" aria-expanded="false">Where exactly is the clinic?<i aria-hidden="true"></i></button>
        <div class="faq__a"><div>Shop 214, second floor of Blueberry Complex on Virat Nagar Road, beside Bhojaldham Society, Nikol.</div></div>
      </div>
    </div>
  </div>
</section>

{cta_band("Two minutes on WhatsApp is usually all it takes.", "Send a photo, describe the pain, or ask what a treatment involves. The clinic replies during opening hours.")}
"""

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Dentist",
        "@id": SITE["url"] + "/#clinic",
        "name": SITE["full"],
        "url": SITE["url"] + "/",
        "image": SITE["url"] + "/assets/img/gen-operatory.jpg",
        "telephone": SITE["phone_tel"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Shop No. 214, Second Floor, Blueberry Complex, near Virat Nagar Road",
            "addressLocality": "Nikol, Ahmedabad",
            "addressRegion": "Gujarat",
            "postalCode": "380049",
            "addressCountry": "IN",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00", "closes": "21:00",
        }],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": SITE["rating"], "reviewCount": SITE["review_count"]},
        "sameAs": [SITE["maps"]],
        "areaServed": ["Nikol", "Naroda", "Vastral", "Odhav", "Ahmedabad"],
    }

    return page(
        title="Dental Clinic in Nikol, Ahmedabad | Smilecraft Dental & Implant Center",
        desc="Multispeciality dental clinic in Nikol, Ahmedabad — implants, root canals, braces, smile design and everyday dentistry. 5.0 from 313 Google reviews. Mon–Sat, 9 AM – 9 PM.",
        path="",
        body=body,
        active="home",
        depth=0,
        jsonld=jsonld,
        preload="hero-poster.jpg",
    )

