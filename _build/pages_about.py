# -*- coding: utf-8 -*-
"""About, gallery and reviews pages."""
from chrome import *

STAR = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="m12 3.6 2.6 5.3 5.8.8-4.2 4.1 1 5.8-5.2-2.8-5.2 2.8 1-5.8-4.2-4.1 5.8-.8Z"/></svg>')


def star_row():
    return ('<span class="stars" role="img" aria-label="5 out of 5 stars">' + STAR * 5 + "</span>")


def crumb(items):
    out = []
    for label, href in items:
        if href:
            out.append('<a href="%s">%s</a><span aria-hidden="true">/</span>' % (href, label))
        else:
            out.append('<span aria-current="page">%s</span>' % label)
    return '<nav class="breadcrumb" aria-label="Breadcrumb">%s</nav>' % "".join(out)


# ------------------------------------------------------------------ about ----
ABOUT = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">About the clinic</p>
    <h1 style="margin-top:18px">A small clinic that would rather do less, properly.</h1>
    <p class="lead">Smilecraft is a multispeciality dental practice on the second floor of Blueberry
    Complex in Nikol. One dentist, a handful of chairs, and enough time in the day to explain what is
    actually going on in your mouth.</p>
    <div class="page-head__meta">
      <span class="pill">__PINSTAR__ Nikol, Ahmedabad</span>
      <span class="pill">__STAR__ 5.0 on Google &middot; 313 reviews</span>
      <span class="pill">Women-owned</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div data-reveal>
      <p class="eyebrow">Why we work this way</p>
      <h2 style="margin-top:14px">The problem with most dental visits isn&rsquo;t the drill.</h2>
      <div class="prose" style="margin-top:22px;max-width:none">
        <p>It&rsquo;s not knowing. Not knowing whether the pain is urgent. Not knowing what the
        treatment will cost until you are already reclined with your mouth open. Not knowing whether
        the third option you were offered was necessary, or just the most expensive one.</p>
        <p>So we do the boring, unfashionable part first: look properly, take an X-ray when it&rsquo;s
        needed, and put the findings in front of you. Then we talk about what has to happen now,
        what can wait six months, and what is genuinely optional.</p>
        <p>You will hear a number before we pick anything up. If the number changes, we stop and
        tell you why. That is the whole system &mdash; there is nothing clever behind it.</p>
      </div>
    </div>
    <div class="split__media split__media--tall" data-reveal data-delay="60">
      <img src="../assets/img/gen-reception.jpg" alt="Reception and waiting area with a curved terrazzo counter, oak joinery and plants" loading="lazy">
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l" data-reveal>
        <p class="eyebrow">Sterilisation</p>
        <h2>What happens to the instruments between patients.</h2>
      </div>
      <div class="sec-head__r" data-reveal>
        <p>You are allowed to ask to see this. Most people never do, and most clinics are quietly
        grateful for that. Please ask.</p>
      </div>
    </div>
    <div class="split">
      <div class="split__media split__media--wide" data-reveal>
        <img src="../assets/img/gen-instruments.jpg" alt="Dental hand instruments laid out on sterile linen on a stainless steel tray" loading="lazy">
      </div>
      <div data-reveal data-delay="60">
        <ul class="value-list" style="margin-top:0;border-top:1px solid var(--line)">
          <li>__CHK__<span><strong>Single-use, always.</strong> Needles, gloves, suction tips, bibs, cotton rolls and the plastic sleeves on the handles. Opened in front of you, disposed of after.</span></li>
          <li>__CHK__<span><strong>Cleaned before sterilised.</strong> Instruments are scrubbed and ultrasonically cleaned first &mdash; an autoclave cannot sterilise debris.</span></li>
          <li>__CHK__<span><strong>Pouched and dated.</strong> Each load is sealed in an indicator pouch, run through a Class B autoclave and stamped with the cycle date.</span></li>
          <li>__CHK__<span><strong>Surfaces between patients.</strong> Chair, light handle, tray and spittoon are wiped down with a hospital-grade disinfectant, not just a spray and a wipe.</span></li>
          <li>__CHK__<span><strong>Water lines.</strong> Lines are flushed between patients and the suction system is cleaned on a schedule, not when someone remembers.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap doctor">
    <div class="doctor__img" data-reveal>
      <img src="../assets/img/smile-portrait.jpg" alt="A patient smiling after dental treatment" loading="lazy">
    </div>
    <div data-reveal data-delay="60">
      <p class="eyebrow">The dentist</p>
      <h2 style="margin-top:14px">Dr Priya Patel</h2>
      <div class="prose" style="margin-top:20px;max-width:none">
        <p>Dr Priya works across the full scope of general dentistry, with a particular focus on
        implants, root canal treatment and cosmetic work on the front teeth. Her consultations tend to
        run long, because she explains things twice &mdash; once with the X-ray, and once in plain
        Gujarati, Hindi or English, whichever you would rather use.</p>
        <p>The clinic is women-owned, and it is a place where that matters less than it should have to.
        Everyone is welcome here, and nobody is going to be talked into treatment they did not ask about.</p>
      </div>
      <ul class="cred-list">
        <li><span>Special interest</span><span>Implantology, endodontics, smile design</span></li>
        <li><span>Languages</span><span>Gujarati, Hindi, English</span></li>
        <li><span>Consultation</span><span>By appointment &mdash; call or WhatsApp</span></li>
        <li><span>Registration</span><span>Available at reception on request</span></li>
      </ul>
      <p style="margin-top:22px"><a class="tlink" href="../book.html">Book a consultation</a></p>
    </div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l" data-reveal>
        <p class="eyebrow">Practical things</p>
        <h2>Before you come.</h2>
      </div>
    </div>
    <div class="grid-3">
      <div class="card" data-reveal>
        <div class="card__ic">__WALLET__</div>
        <h3>Paying for it</h3>
        <p>Cash, UPI and cards are all accepted. For larger plans &mdash; implants, full-mouth work,
        orthodontics &mdash; we can split the cost across sittings. Ask before treatment starts, not after.</p>
      </div>
      <div class="card" data-reveal data-delay="70">
        <div class="card__ic">__PIN__</div>
        <h3>Getting here</h3>
        <p>Second floor of Blueberry Complex, above National Handloom House, near Virat Nagar Road
        and beside Bhojaldham Society. Two-wheeler parking is on the road; cars park in the complex.</p>
      </div>
      <div class="card" data-reveal data-delay="140">
        <div class="card__ic">__CLOCK__</div>
        <h3>Timing</h3>
        <p>Monday to Saturday, 9:00 AM to 9:00 PM. Sundays are closed. Evening slots fill first, so
        message a day or two ahead if you need after 6 PM.</p>
      </div>
    </div>
    <p class="note mt-l" data-reveal>This page describes how the clinic works, not a medical claim.
    Any treatment decision depends on an examination &mdash; please book a consultation rather than
    relying on what you read here.</p>
  </div>
</section>

<section class="cta-band">
  <span class="cta-band__mark" aria-hidden="true">S</span>
  <div class="wrap cta-band__in">
    <div data-reveal>
      <h2>Come and see the room before you commit.</h2>
      <p>You are welcome to visit, look around and ask questions without booking a treatment.
      Message us and we will find a quiet half hour.</p>
    </div>
    <div class="cta-band__actions" data-reveal data-delay="60">
      <a class="btn btn--light btn--lg" href="https://wa.me/919427451885" target="_blank" rel="noopener">__WA__ Message on WhatsApp</a>
      <a class="btn btn--ghost btn--lg" href="../book.html">Book a visit</a>
    </div>
  </div>
</section>
"""


def build_about():
    body = (ABOUT
            .replace("__CRUMB__", crumb([("Home", "index.html"), ("About", None)]))
            .replace("__PINSTAR__", icon("pin"))
            .replace("__STAR__", icon("star"))
            .replace("__CHK__", icon("check"))
            .replace("__WA__", icon("wa"))
            .replace("__WALLET__", icon("shield"))
            .replace("__PIN__", icon("pin"))
            .replace("__CLOCK__", icon("clock")))
    page("about.html", "About Smilecraft Dental Clinic, Nikol | Dr Priya Patel",
         "A patient-first multispeciality dental clinic in Nikol, Ahmedabad. How we plan treatment, "
         "how we sterilise, and what to expect before you book.",
         body.replace('"../', '"'), "", "about", "about.html",
         og="assets/img/gen-reception.jpg",
         schema=breadcrumb_schema([("Home", ""), ("About", "about.html")]))


# ---------------------------------------------------------------- gallery ----
GAL = [
    ("gal__a", "../assets/img/gen-reception.jpg",
     "The waiting area &mdash; terrazzo, oak and a lot of daylight"),
    ("gal__b", "../assets/img/gen-operatory.jpg",
     "A treatment room, set up before the first patient"),
    ("gal__c", "../assets/img/gen-instruments.jpg",
     "Hand instruments, sterilised and pouched between patients"),
    ("gal__d", "../assets/img/gen-doctor.jpg",
     "Examination in progress"),
    ("gal__e", "../assets/img/gen-implant.jpg",
     "Implant planning &mdash; the model and the radiograph side by side"),
    ("gal__f", "../assets/img/aligner-vs-braces.jpg",
     "Clear aligner versus fixed braces"),
    ("gal__g", "../assets/img/smile-macro.jpg",
     "A finished anterior result"),
]


def build_gallery():
    items = "".join(
        '<figure class="gal__item %s" data-full="%s" data-cap="%s" data-reveal>'
        '<img src="%s" alt="%s" loading="lazy">'
        '<figcaption class="gal__cap">%s</figcaption></figure>' % (
            cls, src, cap, src, cap.replace("&mdash;", "-"), cap)
        for cls, src, cap in GAL)

    body = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">Gallery</p>
    <h1 style="margin-top:18px">The clinic, in pictures.</h1>
    <p class="lead">The room, the instruments, the work. If you would rather see it in person before
    booking anything, message us and we will show you around.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="gal">__ITEMS__</div>
    <p class="small muted mt-l" style="max-width:70ch">Photographs on this page are illustrative of the
    clinic, its equipment and the treatments described. For photographs of your own treatment, ask at
    reception &mdash; we can document your case before and after, with your permission.</p>
    <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:26px">
      <a class="btn" href="../book.html">Book a visit</a>
      <a class="btn btn--ghost" href="__MAPS__" target="_blank" rel="noopener">See the 64 photos on Google</a>
    </div>
  </div>
</section>

<div class="lb" data-lightbox data-open="false" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="lb__close" type="button" data-lb-close aria-label="Close">&times;</button>
  <img src="" alt="">
  <p class="lb__cap" data-lb-cap></p>
</div>
""".replace("__CRUMB__", crumb([("Home", "index.html"), ("Gallery", None)])) \
   .replace("__ITEMS__", items) \
   .replace("__MAPS__", SITE["maps"])

    page("gallery.html", "Clinic Gallery | Smilecraft Dental, Nikol Ahmedabad",
         "Photographs of the Smilecraft dental clinic in Nikol, Ahmedabad - the treatment room, "
         "sterilised instruments and the treatments we carry out.",
         body.replace('"../', '"'), "", "gallery", "gallery.html",
         og="assets/img/gen-reception.jpg",
         schema=breadcrumb_schema([("Home", ""), ("Gallery", "gallery.html")]))


# ---------------------------------------------------------------- reviews ----
REVS = [
    ("If you want high-quality dental care with zero pain, this is the place to go!", ""),
    ("Doctor has given perfect explanation and treatment advice.", ""),
    ("Had my wisdom tooth extracted here and the entire experience was flawless. The doctors are "
     "incredibly skilled, professional, and made sure I felt absolutely no pain during the procedure. "
     "The surgery was done much faster than I expected. Highly recommend this clinic for any dental "
     "treatments!", ""),
    ("I recently visited Smilecraft Multispeciality Dental Clinic in Nikol for a professional teeth "
     "whitening procedure, and I am absolutely thrilled with the results! The clinic is exceptionally "
     "clean, modern, and maintains top-notch hygiene&hellip;", ""),
    ("From the moment I walked in, the staff was warm, welcoming, and incredibly professional.", ""),
]

TOPICS = [("Root canal treatment", "30"), ("Painless treatment", "25"),
          ("Wisdom tooth removal", "14"), ("Smile designing", "4")]


def build_reviews():
    cards = "".join(
        '<figure class="rev" data-reveal>%s<blockquote class="rev__q">&ldquo;%s&rdquo;</blockquote>'
        '<figcaption class="rev__foot"><span class="avatar" aria-hidden="true">G</span>'
        '<span class="rev__who"><strong>Google review</strong><span>Smilecraft, Nikol</span></span>'
        '</figcaption></figure>' % (star_row(), q) for q, _ in REVS)

    topics = "".join(
        '<li class="pill">%s <strong style="color:var(--ink)">%s</strong></li>' % (t, n) for t, n in TOPICS)

    body = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">Patient reviews</p>
    <h1 style="margin-top:18px">313 reviews. An average of five stars.</h1>
    <p class="lead">We do not curate this page. These are excerpts from the clinic&rsquo;s Google
    profile, including the answers the owner posted underneath each one.</p>
    <div class="page-head__meta">
      <a class="pill" href="__MAPS__" target="_blank" rel="noopener">__STAR__ 5.0 &middot; 313 reviews on Google</a>
      <span class="pill">__CHK__ Verified reviews</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="rev-band" style="margin-bottom:48px">
      <div class="rev-score" data-reveal>
        <span class="rev-score__n">5.0</span>
        __STARS__
        <span class="rev-score__meta">313 reviews &middot; Google</span>
      </div>
      <div data-reveal data-delay="60">
        <h2 style="max-width:20ch">What people actually write about.</h2>
        <p class="lead" style="margin-top:16px">Google groups the reviews by topic. These are the
        words that come up most often on our profile.</p>
        <ul style="display:flex;flex-wrap:wrap;gap:8px;margin-top:22px">__TOPICS__</ul>
      </div>
    </div>
    <div class="rev-grid">__CARDS__</div>
    <p class="small muted mt-l">Excerpts are reproduced as written by patients on Google, with long
    passages shortened using an ellipsis. Names are withheld here; the full, attributed reviews are
    public on the clinic&rsquo;s Google profile.</p>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap" style="display:grid;grid-template-columns:1.2fr .8fr;gap:clamp(24px,4vw,60px);align-items:center">
    <div data-reveal>
      <p class="eyebrow">Been treated here?</p>
      <h2 style="margin-top:14px">Tell the next nervous patient what to expect.</h2>
      <p class="lead" style="margin-top:16px">Most people find this clinic after reading a review from
      someone who was equally unsure. If we did right by you, a few lines on Google helps more than
      you would think &mdash; and if we did not, we would rather hear it directly first.</p>
      <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:26px">
        <a class="btn btn--clay btn--lg" href="__REVIEW__" target="_blank" rel="noopener">__STAR__ Leave a Google review</a>
        <a class="btn btn--ghost btn--lg" href="https://wa.me/919427451885" target="_blank" rel="noopener">Tell us directly</a>
      </div>
    </div>
    <div class="card" data-reveal data-delay="60">
      <h3>How to leave a review</h3>
      <ol style="display:grid;gap:12px;margin-top:14px;counter-reset:n">
        <li style="display:grid;grid-template-columns:22px 1fr;gap:10px;font-size:var(--t-sm);color:var(--ink-2)">
          <span style="font-family:var(--f-display);color:var(--clay)">1</span>
          <span>Tap the button. It opens the clinic&rsquo;s Google listing.</span></li>
        <li style="display:grid;grid-template-columns:22px 1fr;gap:10px;font-size:var(--t-sm);color:var(--ink-2)">
          <span style="font-family:var(--f-display);color:var(--clay)">2</span>
          <span>Sign in with the Google account you already have on your phone.</span></li>
        <li style="display:grid;grid-template-columns:22px 1fr;gap:10px;font-size:var(--t-sm);color:var(--ink-2)">
          <span style="font-family:var(--f-display);color:var(--clay)">3</span>
          <span>Pick the stars, add a line or two, done. It takes under a minute.</span></li>
      </ol>
    </div>
  </div>
</section>
""".replace("__CRUMB__", crumb([("Home", "index.html"), ("Reviews", None)])) \
   .replace("__MAPS__", SITE["maps"]) \
   .replace("__REVIEW__", REVIEW) \
   .replace("__STAR__", icon("star")) \
   .replace("__STARS__", star_row()) \
   .replace("__CHK__", icon("check")) \
   .replace("__TOPICS__", topics) \
   .replace("__CARDS__", cards)

    page("reviews.html", "Patient Reviews | Smilecraft Dental, Nikol Ahmedabad",
         "Smilecraft Dental Clinic in Nikol has a 5.0 rating from 313 Google reviews. Read what "
         "patients say about root canals, wisdom tooth removal and painless treatment.",
         body.replace('"../', '"'), "", "reviews", "reviews.html",
         schema=[breadcrumb_schema([("Home", ""), ("Reviews", "reviews.html")]),
                 {"@context": "https://schema.org", "@type": "Dentist",
                  "name": SITE["full"], "aggregateRating":
                  {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "313"}}])


if __name__ == "__main__":
    build_about()
    build_gallery()
    build_reviews()
