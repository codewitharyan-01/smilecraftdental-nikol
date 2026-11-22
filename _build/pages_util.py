# -*- coding: utf-8 -*-
"""Contact, booking, first visit, FAQ, privacy, thank you, 404."""
from urllib.parse import quote_plus
from chrome import *


def crumb(items):
    out = []
    for label, href in items:
        if href:
            out.append('<a href="%s">%s</a><span aria-hidden="true">/</span>' % (href, label))
        else:
            out.append('<span aria-current="page">%s</span>' % label)
    return '<nav class="breadcrumb" aria-label="Breadcrumb">%s</nav>' % "".join(out)


def crumb_root(root, active_label):
    return crumb([("Home", root + "index.html"), (active_label, None)])


HOURS_TABLE = """
<table class="hours">
  <caption class="sr-only">Opening hours</caption>
  <tbody>
    <tr data-day="1"><th scope="row">Monday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="2"><th scope="row">Tuesday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="3"><th scope="row">Wednesday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="4"><th scope="row">Thursday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="5"><th scope="row">Friday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="6"><th scope="row">Saturday</th><td>9:00 AM &ndash; 9:00 PM</td></tr>
    <tr data-day="0" data-closed="true"><th scope="row">Sunday</th><td>Closed</td></tr>
  </tbody>
</table>
"""

MAP = """
<div class="map-frame">
  <iframe title="Map showing Smilecraft Dental Clinic on Blueberry Complex, Nikol, Ahmedabad" loading="lazy"
    src="https://maps.google.com/maps?q=23.0367285,72.6722494&z=16&hl=en&output=embed"
    referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
  <div class="map-note"><strong>Smilecraft</strong><br>Blueberry Complex, shop 214, 2nd floor<br>
    <a href="__DIR__" target="_blank" rel="noopener" style="border-bottom:1px solid var(--line-2)">Get directions &rarr;</a></div>
</div>
""".replace("__DIR__", SITE["dir"])


INFO_BLOCK = """
<div class="info-block">
  <div class="info-row">
    <span class="info-row__ic">__PIN__</span>
    <div><h4>Address</h4>
      <address>__A1__<br>__A2__<br>__A3__</address>
      <p style="margin-top:8px"><a href="__MAPS__" target="_blank" rel="noopener">Open in Google Maps &rarr;</a></p>
    </div>
  </div>
  <div class="info-row">
    <span class="info-row__ic">__PH__</span>
    <div><h4>Phone &amp; WhatsApp</h4>
      <p><a href="__TEL__">+91 94274 51885</a></p>
      <p style="margin-top:6px"><a href="https://wa.me/__WA__" target="_blank" rel="noopener">Message us on WhatsApp &rarr;</a></p>
    </div>
  </div>
  <div class="info-row">
    <span class="info-row__ic">__CLOCK__</span>
    <div><h4>Opening hours</h4>__HOURS__</div>
  </div>
  <div class="info-row">
    <span class="info-row__ic">__COMPASS__</span>
    <div><h4>Finding the door</h4>
      <p>Blueberry Complex is the building with National Handloom House on the ground floor, on the
      Virat Nagar Road side. Take the lift or stairs to the second floor; shop 214 is along the
      corridor. There is two-wheeler parking on the road and car parking inside the complex.</p>
    </div>
  </div>
</div>
"""


def info_block():
    return (INFO_BLOCK
            .replace("__PIN__", icon("pin"))
            .replace("__PH__", icon("phone"))
            .replace("__CLOCK__", icon("clock"))
            .replace("__COMPASS__", icon("compass"))
            .replace("__A1__", SITE["addr1"])
            .replace("__A2__", SITE["addr2"])
            .replace("__A3__", SITE["addr3"])
            .replace("__MAPS__", SITE["maps"])
            .replace("__TEL__", TEL)
            .replace("__WA__", SITE["wa"])
            .replace("__HOURS__", HOURS_TABLE))


# ---------------------------------------------------------------- contact ----
def build_contact():
    body = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">Find us</p>
    <h1 style="margin-top:18px">Second floor, Blueberry Complex.</h1>
    <p class="lead">Near Virat Nagar Road, beside Bhojaldham Society, in Nikol. Open six days a
    week from 9 in the morning until 9 at night &mdash; which means an evening appointment is
    usually possible.</p>
    <div class="page-head__meta">
      <a class="btn" href="book.html">Book an appointment</a>
      <a class="btn btn--ghost" href="__TEL__">__PH__ Call the clinic</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div data-reveal>__INFO__</div>
    <div data-reveal data-delay="60">__MAP__</div>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap grid-3">
    <div class="card" data-reveal>
      <div class="card__ic">__WA__</div>
      <h3>WhatsApp is fastest</h3>
      <p>Send a message with what is bothering you, and attach a photo if you have one. During clinic
      hours you will usually hear back within the hour.</p>
      <p style="margin-top:14px"><a class="tlink" href="https://wa.me/__WA__" target="_blank" rel="noopener">Open WhatsApp</a></p>
    </div>
    <div class="card" data-reveal data-delay="70">
      <div class="card__ic">__PH__</div>
      <h3>Call if it is urgent</h3>
      <p>For severe pain, swelling or a knocked-out tooth, call rather than message. If we are with a
      patient, leave a voice note and we will call back the same day.</p>
      <p style="margin-top:14px"><a class="tlink" href="__TEL__">+91 94274 51885</a></p>
    </div>
    <div class="card" data-reveal data-delay="140">
      <div class="card__ic">__CLOCK__</div>
      <h3>Outside hours</h3>
      <p>Sundays are closed. For a dental emergency on a Sunday, message on WhatsApp anyway &mdash;
      we will tell you honestly whether it can wait until Monday.</p>
      <p style="margin-top:14px"><a class="tlink" href="first-visit.html">What to expect</a></p>
    </div>
  </div>
</section>
""".replace("__CRUMB__", crumb_root("", "Contact")) \
   .replace("__INFO__", info_block()) \
   .replace("__MAP__", MAP) \
   .replace("__PH__", icon("phone")) \
   .replace("__WA__", icon("wa")) \
   .replace("__CLOCK__", icon("clock")) \
   .replace("__TEL__", TEL) \
   .replace("__WA2__", SITE["wa"])

    body = body.replace('href="https://wa.me/__WA__"', 'href="https://wa.me/%s"' % SITE["wa"])

    page("contact.html", "Contact &amp; Directions | Smilecraft Dental, Nikol Ahmedabad",
         "Smilecraft Multispeciality Dental Clinic, Shop 214, Blueberry Complex, Nikol, Ahmedabad "
         "380049. Phone +91 94274 51885. Open Monday to Saturday, 9 AM to 9 PM.",
         body, "", "contact", "contact.html",
         schema=breadcrumb_schema([("Home", ""), ("Contact", "contact.html")]))


# ------------------------------------------------------------------ book ----
SERVICES = [
    "Dental implants",
    "Root canal treatment",
    "Braces or clear aligners",
    "Smile design / veneers",
    "Teeth whitening",
    "Crown, bridge or cap",
    "Wisdom tooth removal",
    "Scaling & gum care",
    "Kids' dentistry",
    "Check-up / not sure yet",
    "Something else",
]


def build_book():
    opts = "".join('<option value="%s">%s</option>' % (s, s) for s in SERVICES)
    presel = ""
    body = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">Appointments</p>
    <h1 style="margin-top:18px">Book a visit &mdash; it takes about a minute.</h1>
    <p class="lead">Fill this in and it opens WhatsApp with your details already written out. You
    press send, we reply. Nothing is stored on a server, because there isn&rsquo;t one.</p>
  </div>
</section>

<section class="section">
  <div class="wrap book-layout">
    <div class="form-card" data-reveal>
      <form id="enquiry-form" novalidate>
        <div class="form-step"><span class="form-step__n">1</span> Who you are</div>
        <div class="form-grid">
          <div class="field field--full">
            <label for="name">Full name <span class="field__req">*</span></label>
            <input class="input" type="text" id="name" name="name" autocomplete="name"
                   placeholder="e.g. Rakesh Mehta" required>
            <span class="field__error">Please tell us your name.</span>
          </div>
          <div class="field">
            <label for="phone">Mobile number <span class="field__req">*</span></label>
            <input class="input" type="tel" id="phone" name="phone" inputmode="numeric"
                   autocomplete="tel" placeholder="10-digit number" required>
            <span class="field__error">Enter a valid 10-digit Indian mobile number.</span>
          </div>
          <div class="field">
            <label for="email">Email <span class="field__hint">(optional)</span></label>
            <input class="input" type="email" id="email" name="email" autocomplete="email"
                   placeholder="you@example.com">
            <span class="field__error">That email address doesn&rsquo;t look right.</span>
          </div>
          <div class="field field--full">
            <span class="field__label">Have you been here before?</span>
            <div class="choices">
              <span class="choice"><input type="radio" id="p-new" name="patient" value="New patient" checked>
                <label for="p-new">First visit</label></span>
              <span class="choice"><input type="radio" id="p-old" name="patient" value="Existing patient">
                <label for="p-old">I&rsquo;m an existing patient</label></span>
            </div>
          </div>
        </div>

        <div class="form-step" style="margin-top:32px"><span class="form-step__n">2</span> Why you&rsquo;re coming</div>
        <div class="form-grid">
          <div class="field field--full">
            <label for="treatment">Reason for the visit <span class="field__req">*</span></label>
            <select class="select" id="treatment" name="treatment" required>
              <option value="">Choose one&hellip;</option>
              __OPTS__
            </select>
            <span class="field__error">Choose the reason for your visit.</span>
          </div>
          <div class="field">
            <label for="date">Preferred date</label>
            <input class="input" type="date" id="date" name="date">
          </div>
          <div class="field">
            <label for="slot">Preferred time</label>
            <input class="input" type="text" id="slot" name="slot" readonly
                   placeholder="Pick a date first">
            <div class="slot-grid" data-slot-grid hidden></div>
            <p class="slot-note" data-slot-note data-show="false"></p>
          </div>
          <div class="field field--full">
            <label for="notes">Anything we should know? <span class="field__hint">(optional)</span></label>
            <textarea class="textarea" id="notes" name="notes"
              placeholder="Pain, previous treatment, medication, or anything that would help us plan."></textarea>
          </div>
        </div>

        <div class="field" style="margin-top:20px">
          <label class="check" for="consent">
            <input type="checkbox" id="consent" name="consent" required>
            <span>I&rsquo;m happy for the clinic to contact me on the number above about this enquiry,
            and I&rsquo;ve read the <a href="privacy.html">privacy note</a>.
            <span class="field__req">*</span></span>
          </label>
          <span class="field__error">Please tick this so we know we may reply.</span>
        </div>

        <div class="sr-only" aria-hidden="true">
          <label for="company_website">Company website</label>
          <input type="text" id="company_website" name="company_website" tabindex="-1" autocomplete="off">
        </div>

        <div class="form-actions">
          <button class="btn btn--lg btn--block" type="submit">__WA__ Send enquiry on WhatsApp</button>
          <p class="form-alt">Prefer to talk? <a href="__TEL__">Call +91 94274 51885</a></p>
        </div>

        <div class="preview" data-preview data-show="false">
          <div class="preview__head">__WA__ This is what will be sent</div>
          <div class="preview__body" data-preview-body></div>
        </div>

        <p class="form-note">__SHIELD__ Your details go straight into a WhatsApp message written by
        this page &mdash; we do not run a database, a CRM, or an email list. That also means we can
        only reply once you press send in WhatsApp.</p>
      </form>

      <div class="sent" data-sent data-show="false">
        <div class="sent__ic">__CHK__</div>
        <h3>WhatsApp should have opened.</h3>
        <p>Press <strong>send</strong> in WhatsApp and it comes straight to the clinic. If the app
        didn&rsquo;t open, use the button below &mdash; or copy your details and send them yourself.</p>
        <div class="sent__actions">
          <a class="btn" data-wa-link href="https://wa.me/__WA__" target="_blank" rel="noopener">Open WhatsApp again</a>
          <button class="btn btn--ghost" type="button" data-copy>Copy my details</button>
        </div>
        <p class="small muted" style="margin-top:18px">Clinic hours: Mon&ndash;Sat, 9 AM &ndash; 9 PM.
        Messages outside these hours are answered the next morning.</p>
      </div>
    </div>

    <aside class="book-aside">
      <div class="book-aside__card">
        <h4>Where to find us</h4>
        <p>Shop 214, Second Floor, Blueberry Complex, National Handloom House, near Virat Nagar Road,
        Nikol, Ahmedabad 380049.</p>
        <p style="margin-top:12px"><a class="tlink" href="contact.html">Directions &amp; parking</a></p>
      </div>
      <div class="book-aside__card">
        <h4>Opening hours</h4>
        __HOURS__
      </div>
      <div class="book-aside__card">
        <h4>What happens next</h4>
        <p>We reply on WhatsApp to confirm a slot or suggest the nearest one. If you have sent a
        photo, we may be able to tell you what to expect before you arrive &mdash; and what it will
        roughly cost.</p>
      </div>
      <div class="book-aside__card" style="background:var(--teal);color:var(--paper)">
        <h4 style="color:var(--paper)">In pain right now?</h4>
        <p style="color:rgba(251,248,242,.78)">Call instead of messaging. We keep space in the day for
        urgent cases.</p>
        <p style="margin-top:16px"><a class="btn btn--light btn--block" href="__TEL__">__PH__ Call the clinic</a></p>
      </div>
    </aside>
  </div>
</section>
""".replace("__CRUMB__", crumb_root("", "Book an appointment")) \
   .replace("__OPTS__", opts) \
   .replace("__WA__", icon("wa")) \
   .replace("__CHK__", icon("check")) \
   .replace("__SHIELD__", icon("shield")) \
   .replace("__PH__", icon("phone")) \
   .replace("__HOURS__", HOURS_TABLE) \
   .replace("__TEL__", TEL)

    body = body.replace('href="https://wa.me/__WA__"', 'href="https://wa.me/%s"' % SITE["wa"])

    page("book.html", "Book an Appointment | Smilecraft Dental, Nikol Ahmedabad",
         "Book a dental appointment at Smilecraft, Nikol. Send your details straight to the clinic on "
         "WhatsApp - no forms, no waiting on hold. Open Monday to Saturday, 9 AM to 9 PM.",
         body, "", "book", "book.html",
         extra_scripts='<script src="assets/js/booking.js" defer></script>\n',
         schema=breadcrumb_schema([("Home", ""), ("Book an appointment", "book.html")]))


# ------------------------------------------------------------ first visit ----
def build_first_visit():
    body = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">Your first visit</p>
    <h1 style="margin-top:18px">What actually happens in the first forty minutes.</h1>
    <p class="lead">No surprises, no treatment on the first visit unless you are in pain and ask for
    it. This is what the appointment looks like.</p>
  </div>
</section>

<section class="section">
  <div class="wrap article">
    <div class="prose">
      <h2>The conversation</h2>
      <p>We start with questions, not instruments. What brought you in, how long it has been going on,
      what makes it better or worse, what you have already tried. If you have had treatment elsewhere,
      bring whatever was given to you &mdash; a plan, an X-ray, a prescription. It saves repeating work.</p>

      <h2>The examination</h2>
      <p>A visual check of every tooth and the gums, with a small mirror and a probe. We check the
      bite, the jaw joint and the soft tissue. Nothing is drilled at this stage.</p>
      <p>If a radiograph is needed &mdash; and for most new patients one is &mdash; we take it and go
      through it with you on the screen, pointing at the actual thing we are talking about rather
      than describing it in the air.</p>

      <h2>The plan</h2>
      <p>You leave with it written down: what needs doing now, what can wait, what is optional, and
      what each part costs. If the honest answer is &ldquo;come back in six months&rdquo;, that is what
      the plan will say.</p>
      <p class="note">If you are in pain, we will treat the cause of the pain that day where it is
      possible. Everything else can be planned calmly afterwards.</p>

      <h2>What to bring</h2>
      <ul>
        <li>Any previous dental records, X-rays or treatment plans.</li>
        <li>A list of medicines you take regularly, or the strip itself.</li>
        <li>Recent blood sugar or blood pressure reports, if you have them.</li>
        <li>For a child, their immunisation record is not needed &mdash; but knowing their age and
        whether they have been to a dentist before helps.</li>
      </ul>

      <h2>If you are nervous</h2>
      <p>Say so at the start, on WhatsApp if it is easier. It changes how the appointment is run:
      shorter, with breaks, and the chair kept upright the first time. You can stop the appointment
      at any point by raising your left hand &mdash; that is the signal, and we will stop.</p>

      <h2>If you are bringing a child</h2>
      <p>The first visit is a look and a chat, not a treatment. Ideally before anything hurts, so the
      chair and the light are not associated with pain. Bring them along to your own appointment if
      that helps &mdash; watching a parent be examined is the best preparation there is.</p>

      <h2>Paying</h2>
      <p>Cash, UPI and cards are accepted. Larger plans can be split across sittings. Ask for the
      written estimate before treatment begins; you are entitled to it and we would rather give it
      than have you guess.</p>
    </div>

    <aside class="aside-card">
      <h4>At a glance</h4>
      <p>A consultation, an examination and a written plan. Roughly 30&ndash;45 minutes.</p>
      <a class="btn btn--block" href="book.html">Book a first visit</a>
      <dl class="aside-card__rows">
        <div><dt>Duration</dt><dd>30&ndash;45 minutes</dd></div>
        <div><dt>Treatment same day</dt><dd>Only if urgent</dd></div>
        <div><dt>Bring</dt><dd>Old records, medicines</dd></div>
        <div><dt>Payment</dt><dd>Cash, UPI, card</dd></div>
        <div><dt>Parking</dt><dd>In the complex</dd></div>
      </dl>
      <nav class="jump" aria-label="Other pages">
        <a href="faq.html">Common questions</a>
        <a href="contact.html">Directions</a>
        <a href="treatments.html">All treatments</a>
      </nav>
    </aside>
  </div>
</section>

<section class="cta-band">
  <span class="cta-band__mark" aria-hidden="true">S</span>
  <div class="wrap cta-band__in">
    <div><h2>Bring the list of things you have been ignoring.</h2>
      <p>Most first visits end with a plan, not a drill. Message us and we will find you a slot.</p></div>
    <div class="cta-band__actions">
      <a class="btn btn--light btn--lg" href="book.html">Book an appointment</a>
      <a class="btn btn--ghost btn--lg" href="https://wa.me/__WA__" target="_blank" rel="noopener">Message on WhatsApp</a>
    </div>
  </div>
</section>
""".replace("__CRUMB__", crumb_root("", "Your first visit")) \
   .replace("__WA__", SITE["wa"])

    page("first-visit.html", "Your First Visit | Smilecraft Dental, Nikol Ahmedabad",
         "What happens at your first appointment at Smilecraft, Nikol - the consultation, the "
         "examination, the written plan, what to bring and how we handle nervous patients.",
         body, "", "", "first-visit.html",
         schema=breadcrumb_schema([("Home", ""), ("Your first visit", "first-visit.html")]))


# ------------------------------------------------------------------- faq ----
FAQS = [
    ("General", [
        ("Do I need an appointment, or can I walk in?",
         "<p>Appointments are better &mdash; you will not sit waiting while someone else&rsquo;s root "
         "canal overruns. That said, if you are in pain, call or message and we will fit you in the "
         "same day wherever possible.</p>"),
        ("What are your timings?",
         "<p>Monday to Saturday, 9:00 AM to 9:00 PM. Closed on Sundays. Evening slots after 6 PM go "
         "first, so message a day or two ahead if that is the only time you can come.</p>"),
        ("Where exactly are you?",
         "<p>Shop 214, Second Floor, Blueberry Complex, above National Handloom House, near Virat "
         "Nagar Road, beside Bhojaldham Society, Nikol, Ahmedabad 380049. Take the lift to the second "
         "floor.</p>"),
        ("How do I pay?",
         "<p>Cash, UPI and cards. For larger plans &mdash; implants, orthodontics, full-mouth work "
         "&mdash; payment can be split across the treatment. Ask for the written estimate first.</p>"),
    ]),
    ("Cost", [
        ("How much does root canal treatment cost in Ahmedabad?",
         "<p>It depends on the tooth. A front tooth usually has one canal and costs less; a molar has "
         "three or four and takes longer. Retreatment of a previously root-filled tooth costs more "
         "again, and a crown is additional.</p><p>We do not publish a single number, because it would "
         "be wrong for most people. Come in, get the tooth examined and radiographed, and you will "
         "have an itemised figure before anything begins.</p>"),
        ("How much do dental implants cost in Gujarat?",
         "<p>Implants are priced as several components: the fixture itself, any bone grafting, the "
         "abutment, and the crown on top. Different implant systems and crown materials account for "
         "most of the variation between clinics, and quoted prices are rarely comparing the same thing.</p>"
         "<p>Ask any clinic for a written breakdown listing each component and the brand of the "
         "implant. That is the only way to compare fairly.</p>"),
        ("How much does it cost to remove a wisdom tooth?",
         "<p>An erupted wisdom tooth is a straightforward extraction. An impacted one &mdash; still "
         "under the gum, or lying sideways against the molar in front &mdash; is a surgical procedure "
         "and costs more. A radiograph decides which you are looking at.</p>"),
        ("Is there a consultation fee?",
         "<p>Consultations are charged, and the fee is adjusted against treatment if you go ahead. Ask "
         "when you book &mdash; the reception will tell you the exact figure for your case.</p>"),
    ]),
    ("Treatment", [
        ("Will it hurt?",
         "<p>Treatment is done under local anaesthesia, so it should not be painful. The injection "
         "itself is the part most people dread; we use a topical numbing gel first and give it slowly. "
         "Afterwards, tenderness for a day or two is normal and a painkiller covers it.</p>"),
        ("How many sittings will I need?",
         "<p>A filling or a scaling is one visit. A root canal is one or two, plus a crown. An implant "
         "is a consultation, a placement, then a crown months later. Orthodontics runs for a year or "
         "two with reviews every month or two. You will be told at the planning stage.</p>"),
        ("Can I get treatment during pregnancy?",
         "<p>Routine cleaning and urgent treatment are generally fine, particularly in the second "
         "trimester. Elective cosmetic work and non-urgent X-rays are better delayed. Tell us, and we "
         "will plan around it &mdash; and coordinate with your obstetrician where needed.</p>"),
        ("Do you treat children?",
         "<p>Yes. First visits, fluoride, sealants, fillings and habit advice. The first appointment is "
         "a look and a chat, ideally before anything hurts.</p>"),
        ("What if I need a specialist you don&rsquo;t have?",
         "<p>Most treatment is done in-house. For a small number of cases &mdash; complex jaw surgery, "
         "certain orthodontic discrepancies &mdash; we refer to people we know and trust, and we will "
         "tell you who and why.</p>"),
    ]),
    ("This website", [
        ("Does the booking form send my details somewhere?",
         "<p>No. It writes your details into a WhatsApp message and hands them to WhatsApp, where you "
         "press send. There is no server, no database and no email list behind this site.</p>"),
        ("How do I leave a Google review?",
         "<p>Use the button on the <a href='reviews.html'>reviews page</a>. It opens the clinic&rsquo;s "
         "Google listing with the review form ready. It takes under a minute.</p>"),
    ]),
]


def build_faq():
    blocks = []
    flat = []
    for group, items in FAQS:
        ds = []
        for q, a in items:
            import re
            flat.append((q, re.sub(r"<[^>]+>", " ", a).replace("  ", " ").strip()))
            ds.append('<details class="faq__item"><summary>%s</summary>'
                      '<div class="faq__a">%s</div></details>' % (q, a))
        blocks.append('<h2 style="font-size:clamp(1.5rem,2.4vw,2rem);margin-top:%s">%s</h2>'
                      '<div class="faq" style="margin-bottom:16px">%s</div>'
                      % ("0" if not blocks else "56px", group, "".join(ds)))

    body = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">Questions</p>
    <h1 style="margin-top:18px">The things people actually ask.</h1>
    <p class="lead">Written the way we would answer on the phone &mdash; including the ones about
    money, which most clinic websites avoid.</p>
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow">
    <div class="faq-search">
      <input type="search" data-faq-search placeholder="Search questions&hellip;" aria-label="Search questions">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
    </div>
    __BLOCKS__
    <p class="faq-empty" data-faq-empty data-show="false">No question matches that. Message the clinic on WhatsApp and we will answer it directly.</p>
    <p class="note mt-l">If your question is not here, message the clinic on WhatsApp. You will get a
    real answer from a person, usually within the hour during clinic hours.</p>
    <p style="margin-top:24px"><a class="btn" href="book.html">Book an appointment</a></p>
  </div>
</section>
""".replace("__CRUMB__", crumb_root("", "Questions")) \
   .replace("__BLOCKS__", "".join(blocks))

    page("faq.html", "Frequently Asked Questions | Smilecraft Dental, Nikol",
         "Answers about appointments, costs of root canals, implants and wisdom tooth removal, "
         "treatment times, payment and children at Smilecraft, Nikol Ahmedabad.",
         body, "", "", "faq.html",
         schema=[breadcrumb_schema([("Home", ""), ("Questions", "faq.html")]),
                 faq_schema(flat)])


# --------------------------------------------------------------- privacy ----
def build_privacy():
    body = """
<section class="page-head">
  <div class="wrap wrap--narrow">
    __CRUMB__
    <p class="eyebrow">Privacy</p>
    <h1 style="margin-top:18px">What we do with your information.</h1>
    <p class="lead">Short version: this website has no database. Your enquiry goes from your browser
    into WhatsApp. Nothing is stored on a server we control.</p>
  </div>
</section>

<section class="section">
  <div class="wrap wrap--narrow prose">
    <h2>What the website collects</h2>
    <p>Nothing, until you type it into the enquiry form. When you submit the form, the page builds a
    WhatsApp message containing the name, phone number, email address, treatment, preferred date and
    any notes you entered, and opens WhatsApp with that message ready to send.</p>
    <p>That message is only transmitted when you press send inside WhatsApp. Until then it sits in
    your own browser.</p>

    <h2>What stays in your browser</h2>
    <p>Two things, stored locally on your device using <code>localStorage</code>:</p>
    <ul>
      <li>Your name, phone and email, so the form is pre-filled if you come back.</li>
      <li>The page and referring link you first arrived from, so the clinic knows which channel
      brought you in. Only the channel name is added to the WhatsApp message.</li>
    </ul>
    <p>Both are stored on your device only. Clearing your browser data removes them. The site sets no
    advertising cookies and does not run third-party trackers by default.</p>

    <h2>What happens after you send the message</h2>
    <p>The conversation lives in the clinic&rsquo;s WhatsApp account, on the clinic&rsquo;s phone.
    It is used to reply to you, to arrange an appointment, and for clinical records if you become a
    patient. It is not sold, shared or used for marketing broadcasts.</p>
    <p>WhatsApp&rsquo;s own privacy terms apply to the message itself. If you would rather not use
    WhatsApp, call +91 94274 51885 instead.</p>

    <h2>Clinical records</h2>
    <p>If you become a patient, your clinical records are kept by the clinic as required by the Dental
    Council of India and applicable Indian law. Those records are not on this website.</p>

    <h2>Your requests</h2>
    <p>You can ask us to correct or delete the details we hold about you, or to stop contacting you,
    at any time. Call the clinic or message on WhatsApp and say so; there is no form to fill in.</p>

    <h2>Children</h2>
    <p>Enquiries for a child should be made by a parent or guardian. We do not knowingly collect
    information from children through this site.</p>

    <h2>Changes</h2>
    <p>If this note changes, the date at the bottom of the page changes with it. This version is
    current as of November 2026.</p>

    <p class="note">This page is written to be readable, not to be a legal document. If you need the
    clinic&rsquo;s formal data-handling policy, ask at reception.</p>
  </div>
</section>
""".replace("__CRUMB__", crumb_root("", "Privacy"))

    page("privacy.html", "Privacy Note | Smilecraft Dental, Nikol",
         "How Smilecraft handles enquiry details submitted through this website: no server, no "
         "database, WhatsApp delivery, and what is stored in your browser.",
         body, "", "", "privacy.html")


# ----------------------------------------------------------------- thanks ----
def build_thanks():
    body = """
<section class="section" style="padding-top:clamp(64px,9vw,120px)">
  <div class="wrap wrap--narrow center">
    <div class="sent__ic center-x">__CHK__</div>
    <p class="eyebrow" style="justify-content:center">Enquiry sent</p>
    <h1 style="margin-top:16px">Thank you &mdash; WhatsApp should be open.</h1>
    <p class="lead center-x" style="margin-top:20px">Press send in WhatsApp and your details come
    straight to the clinic. During clinic hours we usually reply within the hour; outside them, first
    thing next morning.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:32px">
      <a class="btn btn--lg" href="https://wa.me/__WA__" target="_blank" rel="noopener">Open WhatsApp</a>
      <a class="btn btn--ghost btn--lg" href="index.html">Back to the site</a>
    </div>
  </div>
</section>
""".replace("__CHK__", icon("check")).replace("__WA__", SITE["wa"])

    page("thank-you.html", "Thank you | Smilecraft Dental, Nikol",
         "Your appointment enquiry is ready to send on WhatsApp.",
         body, "", "", "thank-you.html")


# ------------------------------------------------------------------- 404 ----
def build_404():
    body = """
<section class="section" style="padding-top:clamp(72px,10vw,140px)">
  <div class="wrap wrap--narrow">
    <p class="eyebrow">404</p>
    <h1 style="margin-top:18px">This page has been extracted.</h1>
    <p class="lead" style="margin-top:20px">The link is broken or the page has moved. The clinic is
    still where it was &mdash; second floor, Blueberry Complex, Nikol.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:32px">
      <a class="btn" href="/index.html">Go to the homepage</a>
      <a class="btn btn--ghost" href="/treatments.html">All treatments</a>
      <a class="btn btn--ghost" href="/book.html">Book a visit</a>
    </div>
    <p class="small muted mt-l">Or call the clinic: <a href="tel:+919427451885">+91 94274 51885</a></p>
  </div>
</section>
"""
    page("404.html", "Page not found | Smilecraft Dental, Nikol",
         "That page could not be found.", body, "/", "", "404.html")


def build_all():
    build_contact()
    build_book()
    build_first_visit()
    build_faq()
    build_privacy()
    build_thanks()
    build_404()


if __name__ == "__main__":
    build_all()
