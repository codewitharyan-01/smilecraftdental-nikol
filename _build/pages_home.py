# -*- coding: utf-8 -*-
"""Home page — Bright Clinical dental layout."""
from urllib.parse import quote_plus
from chrome import *

STAR_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
            '<path d="m12 3.6 2.6 5.3 5.8.8-4.2 4.1 1 5.8-5.2-2.8-5.2 2.8 1-5.8-4.2-4.1 5.8-.8Z"/></svg>')


def stars():
    return '<span class="stars" role="img" aria-label="5 out of 5 stars">%s</span>' % (STAR_SVG * 5)


SERVICES = [
    ("treatments/dental-implants.html", "assets/img/gen-implant.jpg", "Dental implants",
     "A missing tooth replaced with something that behaves like the original."),
    ("treatments/root-canal.html", "assets/img/gen-instruments.jpg", "Root canal treatment",
     "Saving the tooth instead of removing it, with proper isolation."),
    ("treatments/braces-aligners.html", "assets/img/aligner-vs-braces.jpg", "Braces &amp; aligners",
     "Metal, ceramic or clear aligners for crowding, gaps and bite problems."),
    ("treatments/smile-design.html", "assets/img/smile-macro.jpg", "Smile design",
     "Shape, shade and proportion planned before anything is made."),
    ("book.html?service=" + quote_plus("Teeth whitening"), "assets/img/smile-woman.jpg", "Teeth whitening",
     "In-clinic bleaching with shade records, or a slower take-home kit."),
    ("treatments.html#restorative", "assets/img/gen-operatory.jpg", "Check-ups &amp; hygiene",
     "Examination, scaling and polishing, and a straight answer about what needs doing."),
]

WHY = [
    ("shield", "Price before treatment", "A written plan with every line costed, agreed before we begin."),
    ("check", "Sterile, without exception", "Instruments pouched and autoclaved; needles and gloves single-use."),
    ("heart", "Comfort first", "Numbing gel, slow injections, and a hand signal to stop at any point."),
    ("users", "One dentist, all the way", "Dr Priya Patel plans and carries out your treatment herself."),
]

REVIEWS = [
    ("If you want high-quality dental care with zero pain, this is the place to go!", "Wisdom tooth"),
    ("Doctor has given perfect explanation and treatment advice.", "Consultation"),
    ("Had my wisdom tooth extracted here and the entire experience was flawless. The doctors are incredibly skilled, professional, and made sure I felt absolutely no pain.", "Wisdom tooth removal"),
]

FAQS = [
    ("Do I need an appointment?",
     "<p>Yes, ideally. Message on WhatsApp or call and we will find a slot &mdash; often the same day "
     "if you are in pain. Sunday is closed.</p>"),
    ("Will treatment hurt?",
     "<p>We use a numbing gel before the injection and give it slowly, so the injection is the least "
     "of it. Most people take a painkiller for a day afterwards and are fine.</p>"),
    ("What does a root canal cost?",
     "<p>It depends on the tooth: a front tooth usually has one canal, a molar three or four. We "
     "examine, take a radiograph, and give you an itemised figure before starting.</p>"),
    ("Do you take cards and UPI?",
     "<p>Yes &mdash; cash, UPI and cards. Larger plans such as implants or braces can be split across "
     "sittings.</p>"),
]

HOURS = """
<table class="hours">
  <tbody>
    <tr data-day="1"><th scope="row">Monday &ndash; Friday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="6"><th scope="row">Saturday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="0" data-closed="true"><th scope="row">Sunday</th><td>Closed</td></tr>
  </tbody>
</table>
"""


def services():
    out = []
    for href, img, title, desc in SERVICES:
        out.append(
            '<a class="service" href="%s">'
            '<span class="service__img"><img src="%s" alt="%s" loading="lazy"></span>'
            '<span class="service__body">'
            '<h3>%s</h3><p>%s</p>'
            '<span class="service__link">Learn more</span>'
            '</span></a>' % (href, img, title.replace("&amp;", "and"), title, desc))
    return "".join(out)


def why():
    out = []
    for ic, title, desc in WHY:
        out.append(
            '<div class="why__item" data-reveal>'
            '<span class="why__ic">%s</span>'
            '<h3>%s</h3><p>%s</p></div>' % (icon(ic), title, desc))
    return "".join(out)


def reviews():
    out = []
    for q, topic in REVIEWS:
        out.append(
            '<figure class="rev">'
            '%s'
            '<blockquote class="rev__q">&ldquo;%s&rdquo;</blockquote>'
            '<figcaption class="rev__foot">'
            '<span class="avatar" aria-hidden="true">G</span>'
            '<span class="rev__who"><strong>Google review</strong><span>%s</span></span>'
            '</figcaption></figure>' % (stars(), q, topic))
    return "".join(out)


def faqs():
    out = []
    for q, a in FAQS:
        out.append('<details class="faq__item"><summary>%s</summary><div class="faq__a">%s</div></details>' % (q, a))
    return "".join(out)


HOME = """
<section class="hero">
  <div class="wrap hero__grid">
    <div class="hero__copy">
      <p class="eyebrow">Nikol &middot; Ahmedabad</p>
      <h1 data-words>A calmer kind of <em>dentist visit</em>.</h1>
      <p class="hero__sub">Implants, root canals, braces and everyday dentistry on the second floor
      of Blueberry Complex &mdash; with a written plan and a price before anything begins.</p>

      <div class="hero__actions">
        <a class="btn btn--lg" href="book.html">Book an appointment</a>
        <a class="btn btn--ghost btn--lg" href="https://wa.me/919427451885" target="_blank" rel="noopener">__WA__ WhatsApp us</a>
      </div>

      <div class="hero__trust">
        <span class="hero__trust-item">__STAR__ <strong>5.0</strong> &middot; 313 Google reviews</span>
        <span class="hero__trust-item">__CLOCK__ Mon&ndash;Sat, 9 AM &ndash; 9 PM</span>
        <span class="hero__trust-item">__PIN__ Blueberry Complex, 2nd floor</span>
      </div>
    </div>

    <div class="hero__media">
      <img src="assets/img/smile-portrait.jpg" width="1200" height="800"
           alt="A patient smiling after dental treatment at Smilecraft in Nikol, Ahmedabad">
      <span class="hero__open">
        <span class="status" data-open-status data-open="true">
          <span class="status__dot" aria-hidden="true"></span>
          <span data-status-text>Checking hours&hellip;</span>
        </span>
      </span>
      <div class="hero__card">
        <span class="hero__card-badge">__SHIELD__</span>
        <span>
          <strong>Same-day care</strong>
          <span>Space kept free each day for urgent pain</span>
        </span>
      </div>
    </div>
  </div>
</section>

<div class="ticker">
  <div class="ticker__track">
    <span class="ticker__item">Dental implants</span>
    <span class="ticker__item">Root canal treatment</span>
    <span class="ticker__item">Clear aligners</span>
    <span class="ticker__item">Zirconia crowns</span>
    <span class="ticker__item">Wisdom tooth removal</span>
    <span class="ticker__item">Smile design</span>
    <span class="ticker__item">Teeth whitening</span>
    <span class="ticker__item">Kids&rsquo; dentistry</span>
  </div>
</div>

<section class="trust">
  <div class="wrap">
    <div class="trust__grid">
      <div class="trust__item">
        <span class="trust__ic">__STAR__</span>
        <span><span class="trust__n">5.0 rating</span><span class="trust__l">313 Google reviews</span></span>
      </div>
      <div class="trust__item">
        <span class="trust__ic">__CLOCK__</span>
        <span><span class="trust__n">Open 6 days</span><span class="trust__l">9 AM &ndash; 9 PM, closed Sunday</span></span>
      </div>
      <div class="trust__item">
        <span class="trust__ic">__TOOTH__</span>
        <span><span class="trust__n">Implant centre</span><span class="trust__l">Guided placement on imaging</span></span>
      </div>
      <div class="trust__item">
        <span class="trust__ic">__PH__</span>
        <span><span class="trust__n">Direct line</span><span class="trust__l">WhatsApp the clinic, no call centre</span></span>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Our treatments</p>
        <h2>Everything under one roof.</h2>
      </div>
      <div class="sec-head__r">
        <p>General dentistry through to implants and orthodontics, so you are not sent to three
        different addresses for one problem.</p>
      </div>
    </div>
    <div class="services" data-stagger>__SERVICES__</div>
    <div style="margin-top:28px"><a class="btn btn--ghost" href="treatments.html">See all treatments</a></div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Not sure what you need?</p>
        <h2>Tell us where it hurts.</h2>
      </div>
      <div class="sec-head__r">
        <p>Pick the closest match and we will point you at the right treatment &mdash; no guessing,
        and no upselling you something you don&rsquo;t need.</p>
      </div>
    </div>

    <div class="finder" data-finder>
      <p class="finder__q">What is bothering you most right now?</p>
      <div class="finder__chips">
        <button class="fchip" type="button" data-symptom="Toothache" aria-pressed="false">Toothache</button>
        <button class="fchip" type="button" data-symptom="Sensitivity" aria-pressed="false">Sensitivity</button>
        <button class="fchip" type="button" data-symptom="Bleeding gums" aria-pressed="false">Bleeding gums</button>
        <button class="fchip" type="button" data-symptom="A missing tooth" aria-pressed="false">A missing tooth</button>
        <button class="fchip" type="button" data-symptom="Crooked teeth" aria-pressed="false">Crooked teeth</button>
        <button class="fchip" type="button" data-symptom="Stained teeth" aria-pressed="false">Stained teeth</button>
      </div>
      <div class="finder__result" data-finder-result data-show="false">
        <span class="finder__label">Most likely</span>
        <span class="finder__title" data-finder-title></span>
        <p class="finder__text" data-finder-text></p>
        <div class="finder__actions">
          <a class="btn" data-finder-link href="treatments.html">Read more</a>
          <a class="btn btn--ghost" href="https://wa.me/919427451885" target="_blank" rel="noopener">__WA__ Ask on WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Why patients stay</p>
        <h2>Four things we do differently.</h2>
      </div>
      <div class="sec-head__r" style="color:rgba(255,255,255,.72)">
        <p>Every clinic says it is different. Here is what that means in practice.</p>
      </div>
    </div>
    <div class="why">__WHY__</div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap feature">
    <div class="feature__media">
      <img src="assets/img/gen-implant.jpg" alt="A dental implant fixture with a ceramic crown beside a radiograph" loading="lazy">
    </div>
    <div class="feature__copy">
      <p class="eyebrow">Implant centre</p>
      <h2>Planned before anything is drilled.</h2>
      <p class="lead">A titanium post takes the place of the root; a crown takes the place of the
      tooth. What matters is the bone you have, and whether the plan is honest about it.</p>
      <ul class="feature__list">
        <li>__CHK__<span>Imaging and bone assessment before placement</span></li>
        <li>__CHK__<span>Written breakdown: fixture, graft, abutment, crown</span></li>
        <li>__CHK__<span>Healing checked, not assumed</span></li>
      </ul>
      <a class="tlink" href="treatments/dental-implants.html">How implants work</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap doctor">
    <div class="doctor__img" data-reveal="scale">
      <img src="assets/img/gen-doctor.jpg" alt="Dr Priya Patel treating a patient in the Smilecraft operatory" loading="lazy">
    </div>
    <div data-reveal>
      <p class="eyebrow">Your dentist</p>
      <h2 style="margin-top:10px">Dr Priya Patel</h2>
      <p class="lead" style="margin-top:14px">Most people who book here have been putting it off for
      a while. So the first visit is mostly listening &mdash; what hurts, what has been tried, and what
      you can actually spend.</p>
      <p style="margin-top:12px;color:var(--ink-2);font-size:0.9375rem;line-height:1.65">
      You leave with a plan on paper. If the honest answer is &ldquo;nothing urgent, come back in six
      months&rdquo;, that is what it will say.</p>
      <ul class="cred-list">
        <li><span>Focus</span><span>Implants, endodontics, smile design</span></li>
        <li><span>Languages</span><span>Gujarati, Hindi, English</span></li>
        <li><span>Clinic</span><span>Blueberry Complex, Nikol</span></li>
        <li><span>On Google</span><span>5.0 from 313 reviews</span></li>
      </ul>
      <p style="margin-top:22px"><a class="btn btn--ghost" href="about.html">More about the clinic</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">A look inside</p>
        <h2>See the room before you sit in it.</h2>
      </div>
      <div class="sec-head__r">
        <p>Two short clips &mdash; the space and the pace. Nothing staged, no music, no voiceover.</p>
      </div>
    </div>
    <div class="videos" data-stagger>
      <div class="video-card video-card--wide" data-reveal>
        <video data-autoplay muted loop playsinline preload="metadata"
               poster="assets/img/gen-reception.jpg" aria-label="Clinic tour: reception, operatory and sterilisation">
          <source src="assets/video/clinic-tour.mp4" type="video/mp4">
        </video>
        <div class="video-card__cap">
          <span><strong>The clinic, in 10 seconds</strong><span>Reception, operatory, sterilisation</span></span>
        </div>
      </div>
      <div class="video-card video-card--tall" data-reveal>
        <video data-autoplay muted loop playsinline preload="metadata"
               poster="assets/img/waiting-room.jpg" aria-label="Waiting area walkthrough">
          <source src="assets/video/clinic-walkthrough.mp4" type="video/mp4">
        </video>
        <div class="video-card__cap">
          <span><strong>Where you wait</strong><span>Mon&ndash;Sat, 9 to 9</span></span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint section--tight">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">The clinic</p>
        <h2 style="font-size:clamp(1.4rem,2.2vw,1.9rem)">A look inside.</h2>
      </div>
      <div class="sec-head__r"><a class="tlink" href="gallery.html">See the gallery</a></div>
    </div>
    <div class="strip">
      <a href="gallery.html"><img src="assets/img/gen-reception.jpg" alt="Reception and waiting area" loading="lazy"></a>
      <a href="gallery.html"><img src="assets/img/gen-operatory.jpg" alt="Dental treatment room" loading="lazy"></a>
      <a href="gallery.html"><img src="assets/img/gen-instruments.jpg" alt="Sterilised instruments on a tray" loading="lazy"></a>
      <a href="gallery.html"><img src="assets/img/smile-macro.jpg" alt="A finished anterior result" loading="lazy"></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Patient reviews</p>
        <h2>What people say afterwards.</h2>
      </div>
      <div class="sec-head__r">
        <div class="rev__score">5.0</div>
        __STARS__
        <p class="rev__meta">313 reviews on Google</p>
      </div>
    </div>
    <div class="rev-grid">__REVIEWS__</div>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:26px">
      <a class="btn btn--ghost" href="reviews.html">Read all reviews</a>
      <a class="btn" href="__REVIEW__" target="_blank" rel="noopener">Leave a Google review</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Whitening</p>
        <h2>Drag to see what whitening changes.</h2>
      </div>
      <div class="sec-head__r">
        <p>Shade only. Whitening does not move teeth or change their shape &mdash; if that is the
        problem, it is a smile design conversation, not a bleaching one.</p>
      </div>
    </div>

    <div class="ba" data-ba aria-label="Before and after whitening comparison">
      <img src="assets/img/smile-macro.jpg" alt="A smile after whitening treatment">
      <div class="ba__before">
        <img src="assets/img/smile-macro.jpg" alt="The same smile before whitening">
      </div>
      <div class="ba__handle">
        <span class="ba__knob">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6 4 12l5 6M15 6l5 6-5 6"/></svg>
        </span>
      </div>
      <span class="ba__tag ba__tag--l">Before</span>
      <span class="ba__tag ba__tag--r">After</span>
    </div>

    <p class="tiny" style="margin-top:12px;max-width:70ch">Illustration of a shade change only &mdash; not a
    patient of this clinic, and not a promise of outcome. Real before-and-after photographs are shown
    in the clinic, with the patient&rsquo;s written consent.</p>

    <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:20px">
      <a class="btn" href="book.html?service=Teeth+whitening">Ask about whitening</a>
      <a class="btn btn--ghost" href="treatments/smile-design.html">Smile design instead</a>
    </div>
  </div>
</section>

<section class="section section--sky">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Questions</p>
        <h2>Before you book.</h2>
      </div>
      <div class="sec-head__r"><a class="tlink" href="faq.html">All questions</a></div>
    </div>
    <div class="faq">__FAQS__</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Before you book</p>
        <h2>Three things worth knowing.</h2>
      </div>
    </div>

    <div class="info-cards">
      <div class="info-card">
        <span class="info-card__ic">__SHIELD__</span>
        <h3>What a visit costs</h3>
        <p>We don&rsquo;t publish a price list, because the same tooth can need two different plans.
        You get an itemised figure after the examination, before anything begins.</p>
        <ul>
          <li>__CHK__<span>Consultation fee, adjusted against treatment</span></li>
          <li>__CHK__<span>Written estimate you can take away</span></li>
          <li>__CHK__<span>Cash, UPI and cards; larger plans split</span></li>
        </ul>
      </div>
      <div class="info-card">
        <span class="info-card__ic">__CAL__</span>
        <h3>Your first visit</h3>
        <p>Thirty to forty-five minutes, mostly talking and looking. Nothing is drilled unless you
        are in pain and ask us to treat it that day.</p>
        <ul>
          <li>__CHK__<span>Bring old X-rays or a previous plan</span></li>
          <li>__CHK__<span>Bring your medicine list</span></li>
          <li>__CHK__<span>Bring a parent for anyone under 18</span></li>
        </ul>
      </div>
      <div class="info-card">
        <span class="info-card__ic">__HEART__</span>
        <h3>If you are nervous</h3>
        <p>Tell us at the start &mdash; on WhatsApp if saying it out loud is harder. It changes how the
        appointment runs: shorter, with breaks, and the chair kept upright.</p>
        <ul>
          <li>__CHK__<span>Numbing gel before any injection</span></li>
          <li>__CHK__<span>Raise your left hand to stop, any time</span></li>
          <li>__CHK__<span>Come and look around before booking</span></li>
        </ul>
      </div>
    </div>

    <div class="urgent mt-l">
      <span class="urgent__ic">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8.5v5M12 17h.01"/><path d="M10.3 3.9 2.6 17.2A2 2 0 0 0 4.3 20h15.4a2 2 0 0 0 1.7-2.8L13.7 3.9a2 2 0 0 0-3.4 0Z"/></svg>
      </span>
      <div>
        <h3>In pain right now?</h3>
        <p>Call rather than message &mdash; we keep a slot free each day for urgent cases.
        Sundays are closed, so if it can wait until Monday we will tell you honestly.</p>
      </div>
      <a class="btn btn--light" href="__TEL__">__PH__ Call +91 94274 51885</a>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l">
        <p class="eyebrow">Find us</p>
        <h2>Second floor, Blueberry Complex.</h2>
      </div>
      <div class="sec-head__r">
        <p>Above National Handloom House, near Virat Nagar Road. Take the lift to the second floor
        and turn right.</p>
      </div>
    </div>
    <div class="visit">
      <div class="visit__card">
        <address class="visit__addr">
          Shop 214, Second Floor, Blueberry Complex.
          <span>National Handloom House, near Virat Nagar Road, beside Bhojaldham Society,
          Nikol, Ahmedabad, Gujarat 380049</span>
        </address>
        <div>__HOURS__</div>
        <div style="display:flex;flex-wrap:wrap;gap:10px">
          <a class="btn" href="book.html">Book a visit</a>
          <a class="btn btn--ghost" href="__DIR__" target="_blank" rel="noopener">Directions</a>
        </div>
      </div>
      <div class="visit__map">
        <iframe title="Map showing Smilecraft Dental Clinic, Nikol, Ahmedabad" loading="lazy"
          src="https://maps.google.com/maps?q=23.0367285,72.6722494&z=16&hl=en&output=embed"
          referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap cta-band__in">
    <div>
      <h2>Book in about a minute, on WhatsApp.</h2>
      <p>Send the problem, a photo if you have one, and a time that suits you. We reply during clinic
      hours &mdash; usually within the hour.</p>
    </div>
    <div class="cta-band__actions">
      <a class="btn btn--light btn--lg" href="https://wa.me/919427451885" target="_blank" rel="noopener">__WA__ Message us</a>
      <a class="btn btn--ghost btn--lg" href="__TEL__">__PH__ Call the clinic</a>
    </div>
  </div>
</section>
"""


def build():
    body = (HOME
            .replace("__SERVICES__", services())
            .replace("__WHY__", why())
            .replace("__REVIEWS__", reviews())
            .replace("__FAQS__", faqs())
            .replace("__HOURS__", HOURS)
            .replace("__STARS__", stars())
            .replace("__STAR__", icon("star"))
            .replace("__CLOCK__", icon("clock"))
            .replace("__PIN__", icon("pin"))
            .replace("__PH__", icon("phone"))
            .replace("__WA__", icon("wa"))
            .replace("__SHIELD__", icon("shield"))
            .replace("__CAL__", icon("calendar"))
            .replace("__HEART__", icon("heart"))
            .replace("__CHK__", icon("check"))
            .replace("__TOOTH__", icon("heart"))
            .replace("__REVIEW__", REVIEW)
            .replace("__DIR__", SITE["dir"])
            .replace("__TEL__", TEL))

    page(
        "index.html",
        "Dental Clinic in Nikol, Ahmedabad | Smilecraft Dental &amp; Implant Center",
        "Smilecraft Multispeciality Dental Clinic &amp; Implant Center in Nikol, Ahmedabad. "
        "Implants, root canals, braces, smile design and general dentistry. 5.0 from 313 Google "
        "reviews. Open Monday to Saturday, 9 AM to 9 PM.",
        body, "", "home", "index.html",
        schema=[dentist_schema(), {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Smilecraft Dental Clinic",
            "url": SITE["url"] + "/",
        }],
    )


if __name__ == "__main__":
    build()
