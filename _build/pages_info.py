# -*- coding: utf-8 -*-
"""About, first visit, FAQ, privacy, 404, thank you."""
from chrome import SITE, TEL, icon, stars, page, cta_band, crumbs

PX = ""  # depth 0 pages


def about():
    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("About", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <div class="split" style="align-items:end">
      <div>
        <span class="eyebrow">About · Nikol, Ahmedabad</span>
        <h1 class="h1 mt-2">A clinic for people<br>who have been<br><span class="serif">putting it off</span>.</h1>
      </div>
      <p class="lead">Most of our patients arrive late — after a year of a tooth that “only hurts sometimes”. The first job is not treatment. It is making the room calm enough that you come back for the second visit.</p>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="film-stage" data-video>
      <video src="assets/video/clinic-film.mp4" poster="assets/img/gen-reception.jpg" autoplay muted loop playsinline preload="metadata" data-managed aria-label="A short film of the clinic"></video>
      <div class="film-stage__scrim" aria-hidden="true"></div>
      <div class="film-stage__copy">
        <div>
          <h3>The room, before you book.</h3>
          <p>Shot on a normal working day. No styling, no stock models.</p>
        </div>
      </div>
      <button class="video-block__btn" data-video-btn aria-label="Pause the clinic film">{icon("pause")}<span data-video-label>Pause</span></button>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="treat-body">
      <div class="prose">
        <h2 class="h3">The setting</h2>
        <p class="mt-2">Blueberry Complex is on Virat Nagar Road, next to Bhojaldham Society. The ground floor is the National Handloom House showroom; the clinic is on the second floor, at 214. It is a short drive from Nikol Cross Roads and easy to reach from Vastral, Odhav and Naroda.</p>
        <p>Being on the second floor has one practical consequence: we are not a shopfront you wander into. Every appointment is scheduled, which is why the waiting room is usually quiet and why the chair is ready when you arrive.</p>

        <h2 class="h3">What we are trying to do differently</h2>
        <p class="mt-2">Dentistry has a reputation problem, and most of it is earned. It comes from being told you need eight fillings without seeing the X-ray, from prices that appear at the end, and from treatment that starts before anyone has explained what is happening.</p>
        <p>So the practice is built around three habits: show the image, write the plan, and never sell the most expensive option first. If a tooth can be watched for six months, we say that. If it cannot, we say that too — and show you why.</p>

        <h2 class="h3">Sterilisation</h2>
        <p class="mt-2">Instruments are cleaned, pouched, dated and autoclaved between every patient. Packs are opened in front of you. Needles, gloves, suction tips and bibs are single-use. The chairs and surfaces are wiped down between appointments, not at the end of the day.</p>
        <p>If you want to see how a pack is opened or where the autoclave is, ask. It is a reasonable question and nobody here will be offended by it.</p>

        <h2 class="h3">What we deliberately do not do</h2>
        <ul class="mt-2">
          <li>No treatment packages sold at the front desk, and no commission on anything.</li>
          <li>No “full mouth rehabilitation” quote on a first visit before the gums have even been assessed.</li>
          <li>No before-and-after photographs of other people's patients used as our own.</li>
          <li>No prices invented for a website. The estimate is written after the X-ray, because that is the first moment it can be honest.</li>
        </ul>
      </div>

      <aside class="treat-rail">
        <div class="rail-card">
          <span class="eyebrow eyebrow--plain">The clinic</span>
          <dl class="defs" style="margin-top:.75rem">
            <div class="defs__row"><dt>Name</dt><dd>Smilecraft Multispeciality Dental Clinic &amp; Implant Center</dd></div>
            <div class="defs__row"><dt>Floor</dt><dd>Second floor, Shop 214</dd></div>
            <div class="defs__row"><dt>Building</dt><dd>Blueberry Complex (National Handloom House)</dd></div>
            <div class="defs__row"><dt>Area</dt><dd>Nikol, Ahmedabad 380049</dd></div>
            <div class="defs__row"><dt>Hours</dt><dd>Mon–Sat, 9 AM – 9 PM</dd></div>
            <div class="defs__row"><dt>Sunday</dt><dd>Closed</dd></div>
          </dl>
          <a class="btn btn--wide mt-2" href="book.html"><span>Book a visit</span>{icon("arrow")}</a>
        </div>
        <div class="rail-card rail-card--plain">
          <span class="eyebrow eyebrow--plain">Directions</span>
          <p class="small muted mt-2">{SITE['street']}<br>{SITE['street2']}<br>{SITE['city']}</p>
          <a class="link-arrow mt-2" href="{SITE['dir']}" target="_blank" rel="noopener">Open in Maps {icon("arrow-up-right")}</a>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="shell">
    <div class="section-head">
      <div>
        <div class="mark"><b>02</b> The dentist</div>
        <h2 class="h2">Dr Priya Patel</h2>
      </div>
      <div class="section-head__aside"><p class="small muted">Named repeatedly in the clinic's Google reviews — usually alongside the word “painless”.</p></div>
    </div>
    <div class="split">
      <div>
        <p class="lead">Her consultations tend to run long, because she explains the X-ray before recommending anything.</p>
        <p class="body mt-2">The special interests are root canal treatment, implants and smile design — the three areas where the difference between an acceptable result and a good one is planning, not equipment. Patients frequently mention that the explanation came first and the treatment second, which is the part we care most about.</p>
        <p class="body mt-2">Qualifications and Dental Council registration are kept at reception and are available on request. You are entitled to know who is treating you and what they are registered to do.</p>
      </div>
      <div class="stack-1">
        <div class="card">
          <h3>Root canal treatment</h3>
          <p>Isolation with a rubber dam, rotary cleaning, and a crown afterwards so the tooth does not fracture.</p>
        </div>
        <div class="card">
          <h3>Implants</h3>
          <p>Planned and placed in-house, with the restoration done by the same dentist who planned the position.</p>
        </div>
        <div class="card">
          <h3>Smile design</h3>
          <p>Trial smile before anything permanent. Whitening first wherever it is enough on its own.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{cta_band("Come and look at the room first.", "If you are anxious, book a short visit with no treatment at all. Sit in the chair, ask your questions, and decide afterwards.")}
"""
    return page(
        title="About the Clinic | Smilecraft Dental, Nikol Ahmedabad",
        desc="Smilecraft Multispeciality Dental Clinic & Implant Center on the second floor of Blueberry Complex, Nikol. Written plans, single-use instruments, and Dr Priya Patel.",
        path="about.html", body=body, active="about.html", depth=0,
        og_image="assets/img/gen-reception.jpg",
    )


def first_visit():
    steps = [
        ("Arrive, sit down, no clipboard marathon", "There is a short medical history form — about a page. If you would rather give it verbally, that is fine too. Tell the front desk if you are nervous; it changes how the appointment is paced."),
        ("Talk before the chair", "What hurts, for how long, what makes it worse, what you have already tried. Bring a list of medicines if you take several."),
        ("Examination and X-ray", "A look at every tooth, the gums, and the bite. An X-ray of the area in question — usually a single small one, not a full set."),
        ("The plan, explained on the screen", "You will see the image, the problem circled, and the options. Ask what happens if you do nothing; it is a legitimate option and often has an honest answer."),
        ("Written estimate", "What is being done, over how many visits, and what each stage costs. Take it home. Nothing is booked under pressure."),
    ]
    timeline = "".join(
        '<div class="step" style="border-color:var(--line)"><div class="step__no">%02d</div><h3 style="color:var(--ink)">%s</h3><p style="color:var(--ink-soft)">%s</p></div>'
        % (i + 1, t, d) for i, (t, d) in enumerate(steps)
    )

    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Your first visit", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <div class="split" style="align-items:end">
      <div>
        <span class="eyebrow">Patient information</span>
        <h1 class="h1 mt-2">What actually happens<br>at the <span class="serif">first visit</span>.</h1>
      </div>
      <p class="lead">About forty minutes, no drilling, and a written plan you can take home. That is the whole promise.</p>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="process" style="border-top-color:var(--line)">{timeline}</div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="split">
      <div class="prose">
        <h2 class="h3">What to bring</h2>
        <ul class="mt-2">
          <li>A list of medicines you take, including blood thinners and anything for diabetes.</li>
          <li>Any X-rays or reports from another clinic in the last year — it may save you a repeat.</li>
          <li>Your insurance card or TPA details, if you plan to claim. Ask at reception what paperwork they can provide.</li>
          <li>The name of any dentist you saw previously, if the treatment was recent.</li>
        </ul>
        <h2 class="h3">If you are in pain</h2>
        <p class="mt-2">Do not wait for a routine slot. Call <a class="textlink" href="{TEL}">{SITE['phone_display']}</a> and say that you are in pain. Same-day slots are kept for emergencies, and a swollen face is treated as urgent.</p>
        <p>If the clinic is closed and the swelling is spreading towards your eye or throat, or you cannot swallow, go to a hospital emergency department. That is not a dental appointment any more.</p>
        <h2 class="h3">Children</h2>
        <p class="mt-2">The first appointment for a child is deliberately short and deliberately boring: sit in the chair, count the teeth in the mirror, leave. No instruments unless the child is comfortable. Bringing a favourite toy helps more than any explanation.</p>
        <h2 class="h3">Payment and insurance</h2>
        <p class="mt-2">Ask at reception about accepted payment methods and about the documents needed for reimbursement. We do not publish a fee list, because it would be wrong for most cases — the estimate you get after the X-ray is the number that matters.</p>
      </div>
      <aside class="treat-rail">
        <div class="rail-card">
          <span class="eyebrow eyebrow--plain">Before you come</span>
          <div class="stack-1 mt-2">
            <div class="flex items-center gap-1">{icon("check-circle")}<span class="small">Eat something — do not arrive on an empty stomach</span></div>
            <div class="flex items-center gap-1">{icon("check-circle")}<span class="small">Bring your medicine list</span></div>
            <div class="flex items-center gap-1">{icon("check-circle")}<span class="small">Arrive five minutes early</span></div>
            <div class="flex items-center gap-1">{icon("check-circle")}<span class="small">Tell us if you are nervous</span></div>
          </div>
          <div class="divider mt-3"></div>
          <p class="tiny muted mt-2">Second floor, Shop 214. Blueberry Complex is on Virat Nagar Road, beside Bhojaldham Society.</p>
          <a class="btn btn--wide mt-2" href="book.html"><span>Book a visit</span>{icon("arrow")}</a>
        </div>
      </aside>
    </div>
  </div>
</section>

{cta_band("Anxious about the first appointment?", "Say so when you book. We will keep it short, explain everything before it happens, and stop whenever you raise a hand.")}
"""
    return page(
        title="Your First Visit | Smilecraft Dental, Nikol",
        desc="What happens at your first appointment at Smilecraft Dental in Nikol: examination, X-ray, a written plan and a written estimate. About forty minutes.",
        path="first-visit.html", body=body, active="first-visit", depth=0,
        og_image="assets/img/gen-operatory.jpg",
    )


def faq():
    groups = [
        ("Appointments", [
            ("Do I need an appointment?", "Yes for anything planned. Walk-ins are seen when there is a gap, but booked patients and emergencies come first, so you may wait. A WhatsApp message a day ahead usually gets you a better time."),
            ("How long is the first appointment?", "Around forty minutes, including the examination, an X-ray and the plan. Complex cases with several problems take longer."),
            ("Can I book for the same day?", "For pain or swelling, call the clinic. Same-day slots are kept for emergencies. For a routine check-up, the next available slot is usually within a few days."),
            ("What if I need to cancel?", "Message the clinic on WhatsApp as early as you can. A late cancellation is only a problem because someone else could have had that slot."),
        ]),
        ("Cost and payment", [
            ("Why are there no prices on this website?", "Because a published price would be wrong for most cases. A crown costs differently on a front tooth and a molar; a root canal depends on how many canals and how infected the tooth is. The estimate after the X-ray is the honest number."),
            ("Will I be told the cost before treatment?", "Yes. Written, itemised, before anything starts. If the plan changes mid-treatment — a canal that turns out to be more complex — we stop and tell you before continuing."),
            ("Do you accept insurance?", "Ask at reception about your specific policy. We can provide the itemised bills and reports needed to claim reimbursement, but approval is between you and your insurer."),
        ]),
        ("Treatment", [
            ("Is treatment painful?", "Local anaesthetic, topical numbing gel before the injection, and a stop signal you control. Patients mention “painless” more than any other word in the reviews."),
            ("How many visits will I need?", "The plan states it. A single filling is one visit; a root canal plus crown is three; an implant is three to five over several months."),
            ("Can I drive home afterwards?", "After local anaesthetic and routine treatment, yes. After sedation — which we do not offer — you could not. After a surgical extraction, arrange someone to drive if you feel faint."),
            ("Do you treat children?", "Yes. First visits for children are kept short and non-invasive so the second one is easy."),
        ]),
        ("Getting here", [
            ("Where exactly is the clinic?", "Shop 214, second floor, Blueberry Complex (the National Handloom House building), near Virat Nagar Road, beside Bhojaldham Society, Nikol, Ahmedabad 380049."),
            ("Is there parking?", "Blueberry Complex is on a commercial road with street-level parking. Two-wheelers usually find space directly outside; for a car, allow a couple of minutes to find a spot."),
            ("What are the timings?", "Monday to Saturday, 9:00 AM to 9:00 PM. Closed on Sundays. Some directories list 10:00 AM to 8:30 PM — if you are travelling from far, call and confirm before setting out."),
        ]),
    ]

    sections_html = ""
    faq_schema = []
    for title, items in groups:
        rows = ""
        for q, a in items:
            rows += ('<div class="faq__item" data-open="false"><button class="faq__q" aria-expanded="false">%s'
                     '<i aria-hidden="true"></i></button><div class="faq__a"><div>%s</div></div></div>' % (q, a))
            faq_schema.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
        sections_html += ('<div class="mt-4"><h2 class="h4" style="letter-spacing:.1em;text-transform:uppercase;'
                          'font-family:var(--f-text);font-size:.75rem;color:var(--ink-mute)">%s</h2>'
                          '<div class="faq mt-2" data-faq>%s</div></div>' % (title, rows))

    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Questions", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <div class="split" style="align-items:end">
      <div>
        <span class="eyebrow">Questions</span>
        <h1 class="h1 mt-2">The things people ask<br>on the <span class="serif">phone</span>.</h1>
      </div>
      <p class="lead">Answered the same way here as we would answer them at the desk — including the ones with no comfortable answer.</p>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">{sections_html}</div>
</section>

<section class="section">
  <div class="shell">
    <div class="note-box">
      <strong>Still not answered?</strong> Message the clinic on WhatsApp — a photograph of the tooth is often enough for a first opinion, and it costs nothing to ask. <a class="textlink" href="{SITE['wa_base']}?text=Hello%20Smilecraft%2C%20I%20have%20a%20question." target="_blank" rel="noopener">Open WhatsApp</a>
    </div>
  </div>
</section>

{cta_band("Ask first, book later.", "There is no obligation attached to a question. Send a message and the clinic will reply during opening hours.")}
"""
    jsonld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_schema}
    return page(
        title="Questions & Answers | Smilecraft Dental, Nikol",
        desc="Appointments, costs, pain, parking and timings — the questions patients ask most about Smilecraft Dental in Nikol, Ahmedabad.",
        path="faq.html", body=body, active="faq", depth=0, jsonld=jsonld,
    )


def privacy():
    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Privacy & consent", None)])}</div>

<section class="section section--tight">
  <div class="shell narrow">
    <span class="eyebrow">Privacy</span>
    <h1 class="h1 mt-2" style="max-width:20ch">What happens to the details you type here.</h1>
    <p class="lead mt-3">Plain language, because a privacy notice you cannot read is not really consent.</p>
  </div>
</section>

<section class="section section--flush">
  <div class="shell narrow prose">
    <h2 class="h3">What this website collects</h2>
    <p class="mt-2">Only what you type into a form: your name, mobile number, and — if you choose to give it — your email address, the treatment you are interested in, a preferred date and time, and any notes you add.</p>
    <p>Nothing is collected automatically. There are no advertising cookies, no tracking pixels and no third-party analytics installed on this site. The map on the contact page is an embedded Google Map, which is subject to Google's own policies once it loads.</p>

    <h2 class="h3">Where it goes</h2>
    <p class="mt-2">When you press send, your browser opens WhatsApp with the message written out. You press send there. The message arrives on the clinic's WhatsApp number and is read by the clinic's staff — the same as if you had messaged them directly.</p>
    <p>This site has no database and no server of its own. The enquiry is not stored on the website. If the clinic has enabled the optional email delivery, a copy is also sent to the clinic's email address.</p>

    <h2 class="h3">What stays on your device</h2>
    <p class="mt-2">Your browser keeps a draft of your name and number so that the next form is pre-filled, and remembers which page you first arrived from so the clinic knows whether you found them on Google, Instagram or a referral. Both live in your browser's local storage. Clearing your browser data removes them. They are never transmitted until you press send.</p>

    <h2 class="h3">How long it is kept</h2>
    <p class="mt-2">Enquiries on WhatsApp follow WhatsApp's retention. Clinical records, once you become a patient, are kept as required for dental records in India and are separate from this website.</p>

    <h2 class="h3">Your choices</h2>
    <ul class="mt-2">
      <li>You can ask what information the clinic holds about you, and ask for a copy.</li>
      <li>You can ask for a correction, or for the enquiry to be deleted if you did not become a patient.</li>
      <li>You can withdraw consent to being contacted about an enquiry at any time — reply “stop” on WhatsApp.</li>
      <li>You never have to give an email address. It is optional everywhere on this site.</li>
    </ul>

    <h2 class="h3">Who to contact</h2>
    <p class="mt-2">The clinic, on <a class="textlink" href="{TEL}">{SITE['phone_display']}</a> or on WhatsApp, at {SITE['street']}, {SITE['street2']}, {SITE['city']}.</p>
    <p class="tiny muted mt-3">Last updated: November 2026. This notice describes current practice and will be updated if the website starts using analytics or a booking database.</p>
  </div>
</section>

{cta_band("Questions about your data?", "Ask at reception, or message the clinic. You do not need to explain why you are asking.")}
"""
    return page(
        title="Privacy & Consent | Smilecraft Dental",
        desc="What the Smilecraft Dental website collects, where it goes, what stays in your browser, and how to ask for it to be deleted.",
        path="privacy.html", body=body, active="privacy", depth=0,
    )


def not_found():
    body = f"""
<section class="section" style="min-height:58vh;display:grid;place-items:center">
  <div class="shell center">
    <span class="eyebrow eyebrow--plain">404</span>
    <h1 class="h1 mt-2">This page has been<br><span class="serif">extracted</span>.</h1>
    <p class="lead mx-auto mt-3" style="text-align:center">The link is old, or the page moved. The clinic is still on the second floor of Blueberry Complex.</p>
    <div class="flex gap-1 mt-3" style="justify-content:center;flex-wrap:wrap">
      <a class="btn" href="index.html"><span>Back to home</span>{icon("arrow")}</a>
      <a class="btn btn--ghost" href="book.html"><span>Book a visit</span></a>
    </div>
    <div class="grid g-3 mt-4" style="max-width:760px;margin-inline:auto;text-align:left">
      <a class="card" href="treatments.html"><h3>Treatments</h3><p>All eight, in one place.</p></a>
      <a class="card" href="contact.html"><h3>Find us</h3><p>Address, hours and map.</p></a>
      <a class="card" href="faq.html"><h3>Questions</h3><p>Costs, timings, parking.</p></a>
    </div>
  </div>
</section>
"""
    return page(
        title="Page not found | Smilecraft Dental",
        desc="That page does not exist. Find treatments, opening hours or book a visit at Smilecraft Dental in Nikol, Ahmedabad.",
        path="404.html", body=body, active="404", depth=0,
    )


def thank_you():
    body = f"""
<section class="section" style="min-height:62vh;display:grid;place-items:center">
  <div class="shell narrow center">
    <span class="eyebrow eyebrow--plain">Enquiry</span>
    <h1 class="h1 mt-2">That is with the clinic.</h1>
    <p class="lead mx-auto mt-3" style="text-align:center">If WhatsApp did not open, use the button below — or simply call. The clinic replies during opening hours, Monday to Saturday.</p>
    <div class="flex gap-1 mt-3" style="justify-content:center;flex-wrap:wrap">
      <a class="btn" href="{SITE['wa_base']}?text=Hello%20Smilecraft%2C%20I%20have%20just%20sent%20an%20enquiry%20through%20the%20website." target="_blank" rel="noopener">{icon("wa")}<span>Open WhatsApp</span></a>
      <a class="btn btn--ghost" href="{TEL}">{icon("phone")}<span>{SITE['phone_display']}</span></a>
    </div>
    <p class="small muted mt-4">Shop 214, second floor, Blueberry Complex · Nikol · Mon–Sat, 9 AM – 9 PM</p>
  </div>
</section>
"""
    return page(
        title="Thank you | Smilecraft Dental",
        desc="Your enquiry has been prepared for WhatsApp. The clinic replies during opening hours.",
        path="thank-you.html", body=body, active="thank-you", depth=0,
    )
