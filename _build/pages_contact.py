# -*- coding: utf-8 -*-
"""Reviews, gallery, contact and booking."""
from chrome import SITE, TEL, icon, stars, page, cta_band, crumbs

REVIEWS = [
    ("VY", "Verified patient", "If you want high-quality dental care with zero pain, this is the place to go!", "Root canal"),
    ("SK", "Sandip K.", "Had my wisdom tooth extracted here and the entire experience was flawless. The doctors are incredibly skilled, professional, and made sure I felt absolutely no pain during the procedure. The surgery was done much faster than I expected. Highly recommend this clinic for any dental treatments!", "Wisdom tooth"),
    ("JP", "Javnika P.", "I recently visited Smilecraft Multispeciality Dental Clinic in Nikol for a professional teeth whitening procedure, and I am absolutely thrilled with the results! The clinic is exceptionally clean, modern, and maintains top-notch hygiene.", "Whitening"),
    ("VR", "Verified patient", "From the moment I walked in, the staff was warm, welcoming, and incredibly professional.", "General"),
    ("SC", "Verified patient", "Doctor has given perfect explanation and treatment advice.", "Consultation"),
]

GALLERY = [
    ("gen-reception.jpg", "Reception", "a", "Reception and seating"),
    ("gen-operatory.jpg", "Treatment room", "b", "The operatory"),
    ("smile-macro.jpg", "Smile design", "c", "Anterior work"),
    ("gen-doctor.jpg", "Consultation", "d", "Consultation and X-ray review"),
    ("gen-instruments.jpg", "Sterilisation", "e", "Instruments, pouched and dated"),
    ("waiting-room.jpg", "Waiting area", "a", "Waiting area"),
    ("smile-woman.jpg", "Whitening", "c", "After whitening"),
    ("aligner-vs-braces.jpg", "Orthodontics", "b", "Aligner and braces"),
    ("xray-review.jpg", "Diagnosis", "e", "Reading the X-ray"),
]


def reviews():
    cards = "".join(
        f"""<article class="review" data-reveal>
      <div class="flex items-center justify-between">{stars()}<span class="chip">{tag}</span></div>
      <blockquote class="review__quote">“{quote}”</blockquote>
      <div class="review__meta"><span class="review__avatar">{initials}</span>
        <div><div class="review__who">{name}</div><div class="review__src">Google review · Nikol</div></div>
      </div>
    </article>"""
        for initials, name, quote, tag in REVIEWS
    )

    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Reviews", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <div class="split" style="align-items:end">
      <div>
        <span class="eyebrow">Patient reviews</span>
        <h1 class="h1 mt-2">{SITE['rating']} from {SITE['review_count']}<br>people who <span class="serif">came in nervous</span>.</h1>
      </div>
      <div>
        <div class="flex items-center gap-2">{stars()}<b style="font-family:var(--f-display);font-size:2rem;font-weight:400">{SITE['rating']}</b></div>
        <p class="small muted mt-1">Unedited Google reviews. We have not asked anyone to remove a critical one — there are none to remove, which is unusual and worth saying plainly.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="grid g-2" data-reveal-group>{cards}</div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="split" style="align-items:start">
      <div>
        <div class="mark"><b>02</b> Leave a review</div>
        <h2 class="h2">If we did well, say so.<br>If we did not, say that too.</h2>
        <p class="body mt-3">Reviews are how a clinic in Nikol gets found by someone in Naroda who is up at 2 AM with a toothache. It takes about a minute, and it genuinely changes who walks through the door.</p>
        <p class="body mt-2">You will need to be signed in to a Google account. The review is public, attached to your Google profile, and can be edited or deleted later.</p>
        <a class="btn mt-3" href="{SITE['review']}" target="_blank" rel="noopener">{icon("star")}<span>Leave a Google review</span>{icon("arrow-up-right")}</a>
        <p class="tiny muted mt-2">This opens the review form for our Google Business Profile directly.</p>
      </div>
      <div class="stack-1">
        <div class="card"><h3>1 · Open the link</h3><p>The button opens the review box for our listing. Sign in if Google asks you to.</p></div>
        <div class="card"><h3>2 · Pick the stars</h3><p>Five is lovely. Three with a reason is more useful to the next patient.</p></div>
        <div class="card"><h3>3 · Say what happened</h3><p>Which treatment, which tooth, how it felt. One sentence is enough.</p></div>
        <div class="card"><h3>Something went wrong?</h3><p>Tell the clinic first — <a class="textlink" href="{TEL}">{SITE['phone_display']}</a>. Most complaints are a scheduling problem we can fix the same week.</p></div>
      </div>
    </div>
  </div>
</section>

{cta_band("Reviews are nice. Coming in is better.", "If you have been putting off a tooth, book the examination. You can decide about treatment afterwards, with the X-ray in front of you.")}
"""
    jsonld = [
        {
            "@context": "https://schema.org",
            "@type": "Dentist",
            "name": SITE["full"],
            "url": SITE["url"] + "/reviews.html",
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": SITE["rating"], "reviewCount": SITE["review_count"]},
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE["url"] + "/"},
                {"@type": "ListItem", "position": 2, "name": "Reviews", "item": SITE["url"] + "/reviews.html"},
            ],
        },
    ]
    return page(
        title="Patient Reviews | Smilecraft Dental, Nikol Ahmedabad",
        desc="5.0 from 313 Google reviews. Read what patients say about root canals, wisdom tooth removal and whitening at Smilecraft Dental in Nikol.",
        path="reviews.html", body=body, active="reviews.html", depth=0, jsonld=jsonld,
    )


def gallery():
    items = "".join(
        f"""<button class="gal__item gal__item--{size}" data-lightbox data-label="{label}" data-full="assets/img/{img}" type="button">
      <img src="assets/img/{img}" width="800" height="600" alt="{alt}" loading="lazy">
    </button>"""
        for img, label, size, alt in GALLERY
    )

    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Gallery", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <div class="split" style="align-items:end">
      <div>
        <span class="eyebrow">Gallery</span>
        <h1 class="h1 mt-2">The room, the work,<br>the <span class="serif">unremarkable</span> details.</h1>
      </div>
      <p class="lead">No dark wood, no leather chairs, no waterfall in the corner. A clean dental clinic with good light and a door that closes.</p>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="film-stage" data-video>
      <video src="assets/video/clinic-tour.mp4" poster="assets/img/gen-operatory.jpg" autoplay muted loop playsinline preload="metadata" data-managed aria-label="Clinic tour film"></video>
      <div class="film-stage__scrim" aria-hidden="true"></div>
      <div class="film-stage__copy">
        <div>
          <h3>Ten seconds in the chair, before you sit in it.</h3>
          <p>The light, the unit, the tray — exactly where they are on the day.</p>
        </div>
      </div>
      <button class="video-block__btn" data-video-btn aria-label="Pause the clinic tour">{icon("pause")}<span data-video-label>Pause</span></button>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="gal">{items}</div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="note-box">
      <strong>A note on the photographs.</strong> Some images here are representative rather than photographs of our own rooms, and the smiles are models. Ask at reception if you would like to walk through the treatment room before you book — nobody will mind, and it is a better use of five minutes than a picture.
    </div>
  </div>
</section>

{cta_band("Come and see it in person.", "The clinic is on the second floor of Blueberry Complex. Walk in during opening hours for a look, or book a proper appointment.")}
"""
    lb = """<div class="lightbox" data-lightbox-box data-open="false" role="dialog" aria-modal="true" aria-label="Photograph">
  <button class="lightbox__close" data-lightbox-close aria-label="Close">%s</button>
  <button class="lightbox__close" data-lightbox-prev aria-label="Previous" style="right:5.2rem">%s</button>
  <button class="lightbox__close" data-lightbox-next aria-label="Next" style="right:8.9rem">%s</button>
  <img alt="">
  <div class="lightbox__cap" data-lightbox-cap></div>
</div>""" % (icon("close"), icon("chevron-l"), icon("chevron-r"))
    body += lb

    return page(
        title="Gallery | Smilecraft Dental, Nikol Ahmedabad",
        desc="Inside Smilecraft Dental in Nikol — the treatment room, sterilisation, the waiting area, and the treatments we do.",
        path="gallery.html", body=body, active="gallery.html", depth=0,
        og_image="assets/img/gen-reception.jpg",
    )


def contact():
    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Visit us", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <div class="split" style="align-items:end">
      <div>
        <span class="eyebrow">Visit · Nikol, Ahmedabad</span>
        <h1 class="h1 mt-2">Second floor, above the<br><span class="serif">handloom showroom</span>.</h1>
      </div>
      <div>
        <div class="flex items-center gap-1 mb-1">{stars()}<span class="small muted">{SITE['rating']} · {SITE['review_count']} Google reviews</span></div>
        <p class="small muted">Open Monday to Saturday, 9:00 AM to 9:00 PM. Closed Sunday. If you are travelling from far, call before setting out.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="grid g-3">
      <div class="card">
        <span class="card__icon">{icon("pin")}</span>
        <h3>Address</h3>
        <p>{SITE['street']}<br>{SITE['street2']}<br>{SITE['city']}</p>
        <a class="link-arrow mt-2" href="{SITE['dir']}" target="_blank" rel="noopener">Directions {icon("arrow-up-right")}</a>
      </div>
      <div class="card">
        <span class="card__icon">{icon("phone")}</span>
        <h3>Phone &amp; WhatsApp</h3>
        <p><a class="textlink" href="{TEL}">{SITE['phone_display']}</a><br>WhatsApp is usually faster during clinic hours.</p>
        <a class="link-arrow mt-2" href="{SITE['wa_base']}?text=Hello%20Smilecraft%2C%20I%20would%20like%20to%20ask%20about%20an%20appointment." target="_blank" rel="noopener">Message the clinic {icon("arrow")}</a>
      </div>
      <div class="card">
        <span class="card__icon">{icon("clock")}</span>
        <h3>Hours</h3>
        <p>Monday – Saturday<br>9:00 AM – 9:00 PM<br>Sunday closed</p>
        <span class="status mt-1" data-status data-open="false"><i class="status__dot"></i><span data-status-text>Mon–Sat, 9 AM – 9 PM</span></span>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="shell">
    <div class="split" style="align-items:start">
      <div class="map-wrap">
        <a class="map-canvas" href="{SITE['dir']}" target="_blank" rel="noopener" aria-label="Open directions to Smilecraft Dental in Google Maps">
          <img src="assets/img/map-nikol.jpg" width="900" height="610" alt="Map of Nikol showing Blueberry Complex on Virat Nagar Road" loading="lazy">
        </a>
        <div class="map-card">
          <b>Blueberry Complex · Shop 214</b>
          <span>Ground floor: National Handloom House. The clinic is one level up.</span>
          <a class="link-arrow mt-1" href="{SITE['dir']}" target="_blank" rel="noopener">Directions {icon("arrow-up-right")}</a>
        </div>
      </div>
      <div>
        <span class="eyebrow">Getting here</span>
        <h2 class="h3 mt-2">Two minutes off Virat Nagar Road.</h2>
        <div class="prose mt-2">
          <p>Blueberry Complex sits on Virat Nagar Road, beside Bhojaldham Society in Nikol. The ground floor is the National Handloom House showroom; take the stairs or lift to the second floor and look for 214.</p>
          <ul>
            <li><strong>By two-wheeler:</strong> street-level parking outside the complex.</li>
            <li><strong>By car:</strong> allow a couple of minutes to find a spot on the service road.</li>
            <li><strong>From Nikol Cross Roads:</strong> about five minutes by auto.</li>
            <li><strong>From Vastral or Odhav:</strong> 15–20 minutes depending on traffic.</li>
          </ul>
        </div>
        <div class="pill-row mt-3">
          <a class="btn btn--sm" href="{SITE['dir']}" target="_blank" rel="noopener">{icon("pin")}<span>Open in Maps</span></a>
          <a class="btn btn--ghost btn--sm" href="{SITE['maps']}" target="_blank" rel="noopener"><span>View the listing</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">Send a message</span>
        <h2 class="h2 mt-2">Ask before you book.</h2>
        <p class="body mt-3">A question about a tooth, a quote, or whether something is urgent — send it here. The form opens WhatsApp with your message ready to send, so nothing gets lost in an inbox.</p>
        <dl class="defs mt-3">
          <div class="defs__row"><dt>Phone</dt><dd><a class="textlink" href="{TEL}">{SITE['phone_display']}</a></dd></div>
          <div class="defs__row"><dt>WhatsApp</dt><dd>Same number</dd></div>
          <div class="defs__row"><dt>Reply time</dt><dd>Usually within a couple of hours during clinic hours</dd></div>
        </dl>
        <p class="tiny muted mt-3">We use your number only to reply to this enquiry. <a class="textlink" href="privacy.html">Privacy note</a>.</p>
      </div>

      <div data-form-shell>
        <form class="form" data-lead-form="enquiry" novalidate>
          <div class="form-grid">
            <div class="field">
              <label class="field__label" for="c-name">Name</label>
              <input class="input" id="c-name" name="name" autocomplete="name" data-required>
              <span class="field__error" data-error></span>
            </div>
            <div class="field">
              <label class="field__label" for="c-phone">Mobile</label>
              <input class="input" id="c-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" data-required data-validate="phone">
              <span class="field__error" data-error></span>
            </div>
            <div class="field field--full">
              <label class="field__label" for="c-email">Email <span class="opt">optional</span></label>
              <input class="input" id="c-email" name="email" type="email" inputmode="email" autocomplete="email" data-validate="email">
              <span class="field__error" data-error></span>
            </div>
            <div class="field field--full">
              <label class="field__label" for="c-msg">Your question</label>
              <textarea class="textarea" id="c-msg" name="notes" data-required placeholder="e.g. a molar hurts when I drink something cold — is that urgent?"></textarea>
              <span class="field__error" data-error></span>
            </div>
            <div class="field field--full">
              <label class="consent">
                <input type="checkbox" name="consent" data-required>
                <span>I agree to be contacted on this number about this enquiry. No marketing lists.</span>
              </label>
              <span class="field__error" data-error></span>
            </div>
          </div>
          <button class="btn btn--wide" type="submit">{icon("wa")}<span>Send on WhatsApp</span></button>
          <p class="form-note">{icon("shield")}<span>This opens WhatsApp with your message written out. You press send — the website never sends anything on its own.</span></p>
        </form>

        <div class="sent" data-sent style="border:1px solid var(--line);border-radius:var(--r-md);background:var(--paper)">
          <span class="sent__icon">{icon("check-circle")}</span>
          <h3>Message ready.</h3>
          <p>WhatsApp should have opened with your enquiry. If it did not, copy the message below and send it to {SITE['phone_display']}.</p>
          <div class="sent__actions">
            <button class="btn btn--ghost btn--sm" type="button" data-copy=" " data-sent-copy><span>Copy message</span></button>
            <a class="btn btn--sm" href="{SITE['wa_base']}" target="_blank" rel="noopener">{icon("wa")}<span>Open WhatsApp</span></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{cta_band("Prefer to just turn up?", "You can, during opening hours. Booked patients come first, so a message ahead usually saves you a wait.")}
"""
    return page(
        title="Contact & Directions | Smilecraft Dental, Nikol Ahmedabad",
        desc="Smilecraft Dental, Shop 214, Blueberry Complex, Virat Nagar Road, Nikol, Ahmedabad 380049. Phone +91 94274 51885. Mon–Sat 9 AM – 9 PM.",
        path="contact.html", body=body, active="contact.html", depth=0,
        og_image="assets/img/gen-reception.jpg",
    )


def book():
    treatments = [
        "Not sure — please advise",
        "Check-up and scaling",
        "Toothache / emergency",
        "Root canal treatment",
        "Dental implants",
        "Braces or clear aligners",
        "Smile design or veneers",
        "Teeth whitening",
        "Crown, bridge or cap",
        "Wisdom tooth removal",
        "Child's first visit",
    ]
    opts = "".join('<option value="%s">%s</option>' % (t, t) for t in treatments)

    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Book an appointment", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <div class="split split--wide-left" style="align-items:end">
      <div>
        <span class="eyebrow">Appointments</span>
        <h1 class="h1 mt-2">Book a visit —<br>it takes about <span class="serif">a minute</span>.</h1>
      </div>
      <p class="lead">Three short steps. The form opens WhatsApp with everything written out; you press send and the clinic replies during opening hours.</p>
    </div>
  </div>
</section>

<section class="section section--flush" style="padding-bottom:var(--pad-y)">
  <div class="shell">
    <div class="book-grid">
      <div data-form-shell>
        <div class="book-card">
          <div class="wizard__steps">
            <span class="wizard__step" data-wizard-step="1" data-state="active"><b>1</b> You</span>
            <span class="wizard__bar"></span>
            <span class="wizard__step" data-wizard-step="2" data-state="todo"><b>2</b> The visit</span>
            <span class="wizard__bar"></span>
            <span class="wizard__step" data-wizard-step="3" data-state="todo"><b>3</b> Send</span>
          </div>

          <form data-lead-form="booking" novalidate>
            <fieldset data-step class="step-panel">
              <legend class="sr-only">Who you are</legend>
              <h2 class="h4">First, who are we expecting?</h2>
              <div class="form-grid mt-2">
                <div class="field">
                  <label class="field__label" for="b-name">Full name</label>
                  <input class="input" id="b-name" name="name" autocomplete="name" data-required>
                  <span class="field__error" data-error></span>
                </div>
                <div class="field">
                  <label class="field__label" for="b-phone">Mobile number</label>
                  <input class="input" id="b-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" data-required data-validate="phone" placeholder="10-digit number">
                  <span class="field__error" data-error></span>
                </div>
                <div class="field field--full">
                  <label class="field__label" for="b-email">Email <span class="opt">optional — for a written copy of the plan</span></label>
                  <input class="input" id="b-email" name="email" type="email" inputmode="email" autocomplete="email" data-validate="email">
                  <span class="field__error" data-error></span>
                </div>
                <div class="field field--full">
                  <span class="field__label">Have you been here before?</span>
                  <div class="chips">
                    <input type="radio" id="pt-new" name="patient" value="First visit" checked>
                    <label for="pt-new">First visit</label>
                    <input type="radio" id="pt-old" name="patient" value="Existing patient">
                    <label for="pt-old">I am an existing patient</label>
                  </div>
                </div>
              </div>
              <div class="flex justify-between items-center mt-3">
                <span class="tiny muted">Step 1 of 3</span>
                <button class="btn" type="button" data-next><span>Next</span>{icon("arrow")}</button>
              </div>
            </fieldset>

            <fieldset data-step class="step-panel" hidden>
              <legend class="sr-only">What you need</legend>
              <h2 class="h4">What is the visit for?</h2>
              <div class="form-grid mt-2">
                <div class="field field--full">
                  <label class="field__label" for="b-treatment">Treatment</label>
                  <select class="select" id="b-treatment" name="treatment">{opts}</select>
                </div>
                <div class="field">
                  <label class="field__label" for="b-date">Preferred date</label>
                  <input class="input" id="b-date" name="date" type="date">
                </div>
                <div class="field">
                  <label class="field__label" for="b-time">Preferred time</label>
                  <select class="select" id="b-time" name="time">
                    <option value="">Any time</option>
                    <option>Morning (9 AM – 12 PM)</option>
                    <option>Afternoon (12 PM – 4 PM)</option>
                    <option>Evening (4 PM – 9 PM)</option>
                  </select>
                </div>
                <div class="field field--full">
                  <label class="field__label" for="b-notes">Anything we should know? <span class="opt">optional</span></label>
                  <textarea class="textarea" id="b-notes" name="notes" placeholder="Pain, since when, medicines you take, or if you are nervous about dentists."></textarea>
                </div>
              </div>
              <div class="flex justify-between items-center mt-3">
                <button class="btn btn--ghost" type="button" data-back>{icon("chevron-l")}<span>Back</span></button>
                <button class="btn" type="button" data-next><span>Next</span>{icon("arrow")}</button>
              </div>
            </fieldset>

            <fieldset data-step class="step-panel" hidden>
              <legend class="sr-only">Check and send</legend>
              <h2 class="h4">Check it, then send.</h2>
              <p class="small muted mt-1">This is exactly what will arrive on the clinic's WhatsApp.</p>
              <pre class="preview mt-2" data-preview></pre>
              <div class="field mt-2">
                <label class="consent">
                  <input type="checkbox" name="consent" data-required>
                  <span>I agree to be contacted on this number about this appointment. My details are used for this enquiry only.</span>
                </label>
                <span class="field__error" data-error></span>
              </div>
              <div class="flex justify-between items-center mt-3" style="gap:.5rem;flex-wrap:wrap">
                <button class="btn btn--ghost" type="button" data-back>{icon("chevron-l")}<span>Back</span></button>
                <button class="btn" type="submit">{icon("wa")}<span>Send on WhatsApp</span></button>
              </div>
              <p class="form-note mt-2">{icon("shield")}<span>No account, no OTP, no card. WhatsApp opens with the message ready; you send it yourself.</span></p>
            </fieldset>
          </form>
        </div>

        <div class="sent book-card" data-sent>
          <span class="sent__icon">{icon("check-circle")}</span>
          <h3>Thanks, <span data-sent-name>there</span> — that is ready to send.</h3>
          <p>WhatsApp should have opened with your request. Press send there and the clinic will confirm a time, usually the same day.</p>
          <pre class="preview mt-3" style="text-align:left" data-sent-message></pre>
          <div class="sent__actions">
            <button class="btn btn--ghost btn--sm" type="button" data-copy=" " data-sent-copy><span>Copy the message</span></button>
            <a class="btn btn--sm" href="{SITE['wa_base']}" target="_blank" rel="noopener">{icon("wa")}<span>Open WhatsApp</span></a>
            <a class="btn btn--ghost btn--sm" href="{TEL}">{icon("phone")}<span>Call instead</span></a>
          </div>
        </div>

        <div class="grid g-2 mt-3">
          <div class="book-card book-card--plain">
            <span class="eyebrow eyebrow--plain">What to bring</span>
            <ul class="bullets mt-2">
              <li>Your medicine list, if you take several</li>
              <li>Any X-ray or report from the last year</li>
              <li>Insurance or TPA details, if you plan to claim</li>
            </ul>
          </div>
          <div class="book-card book-card--plain">
            <span class="eyebrow eyebrow--plain">In pain today?</span>
            <p class="small mt-2">Do not wait for a routine slot — call the clinic and say that you are in pain. Same-day slots are kept for emergencies, and a swollen face is treated as urgent.</p>
            <a class="link-arrow mt-2" href="{TEL}">Call {SITE['phone_display']} {icon("arrow")}</a>
          </div>
        </div>
      </div>

      <aside class="book-aside">
        <div class="book-card book-card--dark">
          <span class="eyebrow eyebrow--plain" style="color:rgba(255,253,248,.6)">What happens next</span>
          <ol class="mini-steps mt-2">
            <li><b>1</b><span>The clinic reads your message and checks the diary.</span></li>
            <li><b>2</b><span>You get a reply confirming a slot — or a couple of alternatives.</span></li>
            <li><b>3</b><span>You arrive five minutes early. The examination takes about forty minutes.</span></li>
          </ol>
          <div class="divider" style="background:rgba(255,253,248,.16)"></div>
          <p class="small mt-2" style="color:rgba(255,253,248,.7)">In pain today? Call rather than book — same-day slots are kept for emergencies.</p>
          <a class="btn btn--light btn--wide mt-2" href="{TEL}">{icon("phone")}<span>{SITE['phone_display']}</span></a>
        </div>

        <div class="book-card">
          <span class="eyebrow eyebrow--plain">Opening hours</span>
          <table class="hours mt-2" data-hours>
            <tbody>
              <tr data-day="1"><th scope="row">Mon – Fri</th><td>9:00 AM – 9:00 PM</td></tr>
              <tr data-day="6"><th scope="row">Saturday</th><td>9:00 AM – 9:00 PM</td></tr>
              <tr data-day="0" data-closed="true"><th scope="row">Sunday</th><td>Closed</td></tr>
            </tbody>
          </table>
          <div class="divider mt-2"></div>
          <p class="small mt-2">{SITE['street']}<br>{SITE['street2']}<br>{SITE['city']}</p>
          <a class="link-arrow mt-2" href="{SITE['dir']}" target="_blank" rel="noopener">Directions {icon("arrow-up-right")}</a>
          <p class="tiny muted mt-2">Some directories list 10:00 AM – 8:30 PM. If you are coming from far, message first.</p>
        </div>
      </aside>
    </div>
  </div>
</section>
"""
    return page(
        title="Book an Appointment | Smilecraft Dental, Nikol",
        desc="Book a dental appointment in Nikol, Ahmedabad. Send your name, preferred time and treatment on WhatsApp — the clinic confirms the same day.",
        path="book.html", body=body, active="book", depth=0,
        og_image="assets/img/smile-portrait.jpg",
    )
