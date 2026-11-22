# -*- coding: utf-8 -*-
"""Treatments hub + four treatment detail pages."""
from chrome import SITE, TEL, icon, stars, page, cta_band, crumbs

# --------------------------------------------------------------------------
# Shared detail layout
# --------------------------------------------------------------------------
def detail(key, no, h1, lead, img, alt, glance, sections, faqs, related, jsonld_extra=None):
    glance_rows = "".join(
        '<div class="defs__row"><dt>%s</dt><dd>%s</dd></div>' % (k, v) for k, v in glance
    )

    body_blocks = ""
    for title, paras, bullets in sections:
        body_blocks += '<div class="mt-4"><h2 class="h3">%s</h2>' % title
        for p in paras:
            body_blocks += '<p class="mt-2 body">%s</p>' % p
        if bullets:
            body_blocks += '<ul class="bullets mt-2">%s</ul>' % "".join("<li>%s</li>" % b for b in bullets)
        body_blocks += "</div>"

    faq_html = "".join(
        '<div class="faq__item" data-open="false"><button class="faq__q" aria-expanded="false">%s<i aria-hidden="true"></i></button>'
        '<div class="faq__a"><div>%s</div></div></div>' % (q, a) for q, a in faqs
    )

    related_html = "".join(
        '<a class="rel-link" href="%s"><span>%s</span>%s</a>' % (href, label, icon("arrow"))
        for href, label in related
    )

    body = f"""
<div class="shell">
  {crumbs([("Home", "index.html"), ("Treatments", "treatments.html"), (h1, None)], depth=1)}
</div>

<section class="section section--tight">
  <div class="shell">
    <div class="treat-head">
      <div>
        <span class="eyebrow">Treatment {no} · Nikol, Ahmedabad</span>
        <h1 class="h1 mt-2">{h1}</h1>
        <p class="lead mt-3">{lead}</p>
        <div class="hero__actions">
          <a class="btn" href="../book.html?treatment={key}"><span>Book a consultation</span>{icon("arrow")}</a>
          <a class="btn btn--ghost" href="{SITE['wa_base']}?text=Hello%20Smilecraft%2C%20I%20would%20like%20to%20ask%20about%20{key}." target="_blank" rel="noopener">{icon("wa")}<span>Ask on WhatsApp</span></a>
        </div>
      </div>
      <dl class="defs" style="margin-top:0">{glance_rows}</dl>
    </div>

    <figure class="frame frame--21x9 mt-4">
      <img src="../{img}" width="1400" height="600" alt="{alt}" fetchpriority="high">
    </figure>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="treat-body">
      <div class="prose">
        {body_blocks}

        <div class="note-box mt-4">
          <strong>What it costs.</strong> We do not publish a fee table, because the honest number depends on the tooth, the material and how much work is needed. What you will get: a fixed examination fee quoted before you book, a written estimate after the X-ray, and no additions without your approval.
        </div>
      </div>

      <aside class="treat-rail">
        <div class="rail-card">
          <span class="eyebrow eyebrow--plain">At a glance</span>
          <dl class="defs" style="margin-top:.75rem">
            {glance_rows}
          </dl>
          <a class="btn btn--wide mt-2" href="../book.html?treatment={key}"><span>Book a visit</span>{icon("arrow")}</a>
          <a class="btn btn--ghost btn--wide mt-1" href="{TEL}">{icon("phone")}<span>Call the clinic</span></a>
        </div>
        <div class="rail-card rail-card--plain">
          <span class="eyebrow eyebrow--plain">Related</span>
          <div class="rel-links">{related_html}</div>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="shell">
    <div class="section-head section-head--stack">
      <div>
        <div class="mark"><b>Q</b> Questions</div>
        <h2 class="h2">{h1}: the questions people actually ask.</h2>
      </div>
    </div>
    <div class="faq" data-faq>{faq_html}</div>
  </div>
</section>

{cta_band("Book the consultation, not the treatment.", "The first visit is an examination and a written plan. Nothing is drilled unless you are in pain and ask for it.", depth=1)}
"""
    return body


# --------------------------------------------------------------------------
# 1. Implants
# --------------------------------------------------------------------------
def implants():
    sections = [
        ("What an implant actually is", [
            "An implant is a titanium post that sits in the jaw where a tooth root used to be. Once the bone has accepted it — usually three to four months — a crown is fixed on top. The two teeth on either side are not touched, which is the whole point: a bridge supports itself on its neighbours, an implant supports itself.",
            "We place and restore implants in the same clinic, so the surgeon who plans the position is the dentist who fits the crown. That sounds obvious. In practice, it is often two different practices and two sets of records.",
        ], None),
        ("When it is the right answer", [
            "One missing tooth, with healthy teeth either side. Several missing teeth in a row. A denture that moves when you talk. A tooth that has fractured below the gum line and cannot be saved.",
            "It is not the right answer for everyone. If the bone volume is too low, a graft may be needed first — or a bridge may genuinely be the better, cheaper, faster option. You will be told which case you are before anything is booked.",
        ], [
            "Bone volume is checked on an X-ray, and sometimes a CT scan",
            "Gum health has to be stable first — implants fail in untreated gum disease",
            "Smoking and uncontrolled diabetes both lower the success rate, and we will say so plainly",
        ]),
        ("The appointments, in order", [
            "Assessment and planning. X-ray or scan, measurements, and a written plan with the number of visits and the cost of each stage.",
            "Placement. The post goes in under local anaesthetic. Most single implants take forty minutes to an hour in the chair. You go home the same day.",
            "Healing. Three to four months while the bone integrates. You will have a temporary tooth or a gap, depending on the site.",
            "The crown. An impression or scan, then the final crown is fitted and the bite is checked.",
            "Review. Short checks at one week and around three months, then the usual six-monthly visits.",
        ], None),
        ("Afterwards", [
            "Expect some swelling and tenderness for two to three days. Ice for the first day, soft food, and the painkillers you are given. Do not chew on the implant side until you are told it is safe.",
            "Long term, an implant needs cleaning like a tooth — and slightly more attention at the gum line, because there is no ligament to warn you when something is wrong. That is what the review appointments are for.",
        ], None),
    ]
    faqs = [
        ("Does having an implant hurt?", "The placement itself is done under local anaesthetic, so you should not feel pain during it. Afterwards it feels like a deep extraction: sore for a few days, manageable with ordinary painkillers. Most people take one day off, not a week."),
        ("How long does the whole thing take?", "Typically three to five months from placement to the final crown, because the bone needs time to integrate. If you need a graft first, add a few months. The exact timeline is written into your plan."),
        ("Will it look different from my other teeth?", "The crown is matched to the shade and shape of your neighbours. For a front tooth we spend more time on this, and may use a temporary crown first so you can see the shape before it is final."),
        ("Can I just have a bridge instead?", "Often, yes — and sometimes it is the better choice. A bridge is faster and involves no surgery, but it requires cutting down the two healthy teeth beside the gap. We will show you both on the X-ray and let you choose."),
    ]
    related = [("root-canal.html", "Root canal treatment"), ("../treatments.html#crowns", "Crowns &amp; bridges"), ("../book.html", "Book a visit")]
    body = detail(
        "Dental%20implants", "01",
        "Dental implants",
        "A missing tooth replaced with something that behaves like the original — and without cutting down the two healthy teeth beside it.",
        "assets/img/gen-implant.jpg",
        "Implant model and planning X-ray at Smilecraft Dental",
        [("Visits", "3–5, over 3–5 months"), ("Chair time", "40–60 min per stage"), ("Anaesthetic", "Local"), ("Best for", "Single or several missing teeth")],
        sections, faqs, related,
    )
    jsonld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }
    return page(
        title="Dental Implants in Nikol, Ahmedabad | Smilecraft Dental",
        desc="Single and multiple dental implants in Nikol, Ahmedabad. Planned, placed and restored in one clinic, with a written plan and cost before treatment begins.",
        path="treatments/dental-implants.html", body=body, active="treatments", depth=1, jsonld=jsonld,
        og_image="assets/img/gen-implant.jpg",
    )


# --------------------------------------------------------------------------
# 2. Root canal
# --------------------------------------------------------------------------
def root_canal():
    sections = [
        ("What a root canal is — and is not", [
            "Inside every tooth is a nerve and a blood supply, in a space called the pulp. When that pulp gets infected — through a deep cavity, a crack, or a knock — it cannot heal itself. The pressure builds, and that is the pain that wakes people up at night.",
            "A root canal removes the infected tissue, cleans and shapes the canals, and seals them. The tooth stays in your mouth. It is not a “dead tooth” that will crumble: with a proper crown on top it usually lasts decades.",
            "What it is not: a quick fix done through a tiny hole with no isolation. Doing it properly takes time, magnification, and a rubber dam to keep saliva out.",
        ], None),
        ("Signs you probably need one", [
            "Not every case hurts. Some are found on an X-ray with no symptoms at all. The usual signals:",
        ], [
            "Pain that lingers after hot or cold, rather than fading in a second",
            "Pain that wakes you up, or throbs when you lie down",
            "Tenderness when you bite down on that tooth",
            "A small pimple on the gum that tastes bad, or comes and goes",
            "Swelling in the face, which is an urgent same-day call",
        ]),
        ("How the appointment goes", [
            "We take an X-ray, test the tooth, and confirm the diagnosis before anaesthetising. Then the tooth is isolated with a rubber dam, the canals are cleaned with rotary files and an irrigant, and the space is sealed. Some teeth are finished in one visit; infected or curved canals are safer in two.",
            "You should not feel the work. If you do, raise a hand — the anaesthetic gets topped up, not talked over.",
        ], None),
        ("Afterwards, and the crown", [
            "The tooth is often tender for two or three days, especially when biting. That is the ligament around it settling, not the treatment failing. Ordinary painkillers cover it.",
            "A root-treated tooth becomes brittle, so a back tooth needs a crown fairly soon — usually within a few weeks. Skipping that step is the most common reason a saved tooth fractures later and has to come out.",
        ], None),
    ]
    faqs = [
        ("Is a root canal painful?", "The procedure is done under local anaesthetic, so it should not hurt. Most patients say the relief afterwards is immediate — the pain they came in with is gone. The phrase “painless root canal” in our reviews is about that difference."),
        ("How many visits does it take?", "One or two. Straightforward front teeth are often finished in a single sitting. Molars with curved or infected canals are safer over two visits, with a temporary seal in between."),
        ("Can I take a painkiller before coming?", "Yes — if you are in pain, take what you normally take. Tell us what and when. Do not take aspirin on an empty stomach before a procedure without asking."),
        ("What if the tooth cannot be saved?", "Then we say so, and show you why on the X-ray. The options are removal with an implant or bridge later, or removal and leaving the gap. Either way you get the plan in writing before deciding."),
    ]
    related = [("dental-implants.html", "Dental implants"), ("../treatments.html#crowns", "Crowns &amp; caps"), ("../book.html", "Book a visit")]
    body = detail(
        "Root%20canal%20treatment", "02",
        "Root canal treatment",
        "Saving the tooth you already have — properly isolated, properly cleaned, and finished with a crown that protects it.",
        "assets/img/xray-review.jpg",
        "Dentist reading an X-ray before root canal treatment",
        [("Visits", "1–2"), ("Chair time", "45–90 min"), ("Anaesthetic", "Local"), ("Best for", "Infected or inflamed pulp")],
        sections, faqs, related,
    )
    jsonld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }
    return page(
        title="Root Canal Treatment in Nikol, Ahmedabad | Smilecraft Dental",
        desc="Painless root canal treatment in Nikol, Ahmedabad, with rubber dam isolation and rotary cleaning. One or two visits, written plan, and a crown to protect the tooth.",
        path="treatments/root-canal.html", body=body, active="treatments", depth=1, jsonld=jsonld,
        og_image="assets/img/xray-review.jpg",
    )


# --------------------------------------------------------------------------
# 3. Braces & aligners
# --------------------------------------------------------------------------
def braces():
    sections = [
        ("Straightening is not only cosmetic", [
            "Crowded teeth trap plaque where a brush cannot reach. A deep bite wears the front teeth flat. A crossbite can strain the jaw joint. Wanting a better smile is a perfectly good reason on its own — but there are usually functional reasons too, and they are worth knowing about.",
            "Adults are more than half of the orthodontic cases we see. If you had braces as a teenager and stopped wearing the retainer, this is a very common place to end up.",
        ], None),
        ("The three realistic options", [
            "Metal braces. The most predictable for complex movement, the least expensive, and the most visible. Modern brackets are smaller than the ones you remember.",
            "Ceramic braces. Same mechanics, tooth-coloured brackets. Less obvious from a distance, slightly more fragile, and food staining around the ligatures is a real thing.",
            "Clear aligners. Removable trays, changed roughly every one to two weeks. Excellent for mild to moderate crowding and spacing. They only work if you wear them 20–22 hours a day — which is a discipline problem, not a technology problem.",
        ], None),
        ("Records first, quote second", [
            "No responsible clinic quotes orthodontics from a photograph. We take photographs, an X-ray, and either an impression or a scan, then work out how much movement is needed and how long it will take. Only then is there a plan with a timeline and a fee.",
        ], None),
        ("Living with them", [
            "The first three to five days after fitting, and a day or two after each adjustment, are the uncomfortable part. Soft food, wax for the edges that rub, and it settles.",
            "Cleaning takes longer than usual — a brush plus interdental brushes, and for aligners, cleaning the trays themselves. Decalcification marks from poor hygiene during braces are permanent, which is why we are fussy about this.",
            "Retainers afterwards are not optional. Teeth move back; that is what they do. A night-time retainer is the difference between a result that lasts and one that quietly undoes itself.",
        ], None),
    ]
    faqs = [
        ("Am I too old for braces?", "No. Age affects the gum response and the speed slightly, but not whether teeth can be moved. The oldest patient we would treat is the one whose gums are healthy — not one below a particular birthday."),
        ("How long will it take?", "Typically 12 to 24 months for braces, and 6 to 18 months for aligners, depending on the case. Complex bite corrections take longer. A realistic estimate is given after the records, in writing."),
        ("Do aligners hurt?", "They feel tight for a day or two after each new tray — that is the tooth moving. It is pressure rather than sharp pain. Most people stop noticing it by the third tray."),
        ("Will people notice?", "With clear aligners, usually not unless they are looking closely. With ceramic braces, less than you fear. With metal braces, yes — but you would be surprised how quickly colleagues stop commenting."),
    ]
    related = [("smile-design.html", "Smile design"), ("../treatments.html#hygiene", "Gum care"), ("../book.html", "Book a visit")]
    body = detail(
        "Braces%20and%20clear%20aligners", "03",
        "Braces &amp; clear aligners",
        "Metal, ceramic or clear aligners — chosen on the basis of records, not on what looks best in an advertisement.",
        "assets/img/aligner-vs-braces.jpg",
        "Clear aligner and braces on a model",
        [("Records", "Photos, X-ray, scan"), ("Timeline", "6–24 months"), ("Visits", "Every 4–8 weeks"), ("Retainers", "Night-time, long term")],
        sections, faqs, related,
    )
    jsonld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }
    return page(
        title="Braces & Clear Aligners in Nikol, Ahmedabad | Smilecraft Dental",
        desc="Metal braces, ceramic braces and clear aligners in Nikol, Ahmedabad. Records first, a written timeline, and retainers that keep the result.",
        path="treatments/braces-aligners.html", body=body, active="treatments", depth=1, jsonld=jsonld,
        og_image="assets/img/aligner-vs-braces.jpg",
    )


# --------------------------------------------------------------------------
# 4. Smile design
# --------------------------------------------------------------------------
def smile_design():
    sections = [
        ("The order matters more than the material", [
            "Most people arrive asking for veneers. Often what they actually want is a lighter, more even smile — and whitening plus a little bonding gets there without touching a single healthy tooth surface.",
            "So we work in steps: clean and check the gums, whiten if the shade is the issue, bond the small chips and gaps, and only then talk about veneers. If a veneer is the right answer, you will hear it as a considered recommendation, not the first thing on the menu.",
        ], None),
        ("What a smile design appointment involves", [
            "Photographs, a shade record, and a conversation about proportion — how much tooth shows at rest, where the midline sits, whether the smile line follows the lower lip. Then a trial smile: composite or a digital mock-up placed on your teeth so you can see the shape in your own face before anything is permanent.",
            "Only after you have seen and approved the trial do we make the final restorations.",
        ], None),
        ("Veneers, honestly", [
            "A conventional veneer removes a thin layer of enamel from the front of the tooth. That is irreversible. A minimal-prep or no-prep veneer removes less or none, but it only suits certain teeth and certain bites.",
            "Composite bonding is cheaper, done in one sitting, and can be repaired. It also stains and chips sooner than ceramic. Ceramic looks better for longer and costs more. Both are legitimate; the choice depends on your teeth, your budget and how much you want to commit.",
        ], None),
        ("Who should not start with cosmetics", [
            "If there is active gum disease, cavities, or a bite that is grinding the front teeth flat, cosmetics on top of that will fail early. Fix the foundation first — then design. Anyone who offers to skip that step is selling, not treating.",
        ], None),
    ]
    faqs = [
        ("Will veneers look fake?", "Only if they are made badly. The failures you notice are usually too white, too opaque, too uniform in length. We match the shade to your age and face, and vary the edges slightly — that is what makes a smile read as natural."),
        ("How long do veneers last?", "With good hygiene and a night guard if you grind, ten to fifteen years is a reasonable expectation. Composite bonding lasts less — typically four to seven years before it needs refreshing."),
        ("Can I see the result before it is permanent?", "Yes. That is the point of the trial smile. You will see the proposed shape on your own teeth, and you can change it before anything is made."),
        ("Do you do whitening on its own?", "Yes — in-clinic bleaching with a before-and-after shade record, or a take-home kit with custom trays. Whitening does not change the colour of crowns, veneers or fillings, which is why the shade conversation comes before the material conversation."),
    ]
    related = [("braces-aligners.html", "Braces &amp; aligners"), ("../treatments.html#whitening", "Teeth whitening"), ("../book.html", "Book a visit")]
    body = detail(
        "Smile%20design", "04",
        "Smile design &amp; veneers",
        "Shape and proportion planned before anything is made — and a trial smile you can see and change before it becomes permanent.",
        "assets/img/smile-macro.jpg",
        "Close-up of a finished smile",
        [("Visits", "2–3"), ("Timeline", "2–3 weeks"), ("Trial smile", "Yes, always"), ("Materials", "Ceramic or composite")],
        sections, faqs, related,
    )
    jsonld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }
    return page(
        title="Smile Design & Veneers in Nikol, Ahmedabad | Smilecraft Dental",
        desc="Smile design, ceramic veneers and composite bonding in Nikol, Ahmedabad. Whitening first where it is enough, a trial smile where it is not.",
        path="treatments/smile-design.html", body=body, active="treatments", depth=1, jsonld=jsonld,
        og_image="assets/img/smile-macro.jpg",
    )


# --------------------------------------------------------------------------
# Hub
# --------------------------------------------------------------------------
def hub():
    rows = [
        ("treatments/dental-implants.html", "01", "Dental implants", "A missing tooth replaced with a titanium post and a crown — without cutting down the teeth either side."),
        ("treatments/root-canal.html", "02", "Root canal treatment", "Removing the infected nerve, sealing the canals, and keeping the tooth you already have."),
        ("treatments/braces-aligners.html", "03", "Braces &amp; clear aligners", "Metal, ceramic or clear aligners for crowding, gaps and bite problems, at any age."),
        ("treatments/smile-design.html", "04", "Smile design &amp; veneers", "Whitening first where it is enough; ceramic or composite only where it is not."),
        ("#whitening", "05", "Teeth whitening", "In-clinic bleaching with a recorded shade, or a slower take-home kit with custom trays."),
        ("#crowns", "06", "Crowns, bridges &amp; caps", "Rebuilding a tooth that has cracked, worn or just had a root canal."),
        ("#wisdom", "07", "Wisdom tooth removal", "The appointment people postpone the longest. Usually simpler than expected."),
        ("#hygiene", "08", "Scaling &amp; gum care", "The six-month visit that keeps the rest of the list short."),
    ]
    row_html = "".join(
        '<a class="svc-row" href="%s"><span class="svc-row__no">%s</span><h3>%s</h3><p>%s</p>'
        '<span class="svc-row__go">%s</span></a>' % (h, n, t, d, icon("arrow"))
        for h, n, t, d in rows
    )

    body = f"""
<div class="shell">{crumbs([("Home", "index.html"), ("Treatments", None)])}</div>

<section class="section section--tight">
  <div class="shell">
    <span class="eyebrow">Treatments · Nikol, Ahmedabad</span>
    <h1 class="h1 mt-2" style="max-width:18ch">Eight treatments, one set of records.</h1>
    <div class="split mt-4" style="align-items:end">
      <p class="lead">Most clinics refer the complicated cases out. Here, the implant, the root canal and the crown are planned by the same person — which is why the plan holds together.</p>
      <p class="small muted">If you are not sure which of these you need, start with an examination. The first visit is diagnostic, not treatment, and you leave with the plan in writing.</p>
    </div>
  </div>
</section>

<section class="section section--flush">
  <div class="shell">
    <div class="svc-list">{row_html}</div>
  </div>
</section>

<section class="section section--paper" id="whitening">
  <div class="shell">
    <div class="split">
      <div class="split__body">
        <div class="mark"><b>05</b> Teeth whitening</div>
        <h2 class="h2">Lighter, without pretending it is permanent.</h2>
        <p class="lead mt-2">Two routes, and we will tell you which one your teeth are suited to.</p>
        <p class="body mt-2">In-clinic bleaching is faster: a stronger gel, a protective barrier on the gums, and a shade record taken before and after so you can see the actual change rather than judge it from memory. It takes one appointment of about an hour.</p>
        <p class="body mt-2">Take-home whitening is slower and gentler: custom trays made from an impression, a lower-strength gel used over one to two weeks. Less sensitivity for most people, and you keep the trays for top-ups.</p>
        <p class="body mt-2">Neither changes the colour of crowns, veneers or old fillings. If those are visible when you smile, whitening the teeth around them can make the mismatch more obvious — which is a conversation to have before starting, not after.</p>
        <ul class="bullets mt-3">
          <li>Not advised during pregnancy, or with untreated cavities and gum disease</li>
          <li>Tea, coffee, turmeric and tobacco will re-stain the result over time</li>
          <li>Sensitivity during treatment is common and settles within a day or two</li>
        </ul>
        <a class="btn mt-3" href="book.html?treatment=Teeth%20whitening"><span>Book a whitening consultation</span>{icon("arrow")}</a>
      </div>
      <div class="split__media">
        <figure class="frame frame--4x5"><img src="assets/img/smile-woman.jpg" width="900" height="1100" alt="Patient smiling after teeth whitening" loading="lazy"></figure>
      </div>
    </div>
  </div>
</section>

<section class="section" id="crowns">
  <div class="shell">
    <div class="split split--media-left">
      <div class="split__media">
        <figure class="frame frame--3x4"><img src="assets/img/gen-instruments.jpg" width="900" height="1200" alt="Sterile dental instruments laid out for a crown preparation" loading="lazy"></figure>
      </div>
      <div class="split__body">
        <div class="mark"><b>06</b> Crowns, bridges &amp; caps</div>
        <h2 class="h2">A cover for a tooth that has run out of tooth.</h2>
        <p class="body mt-3">A crown is a full cover, cemented over a tooth that has cracked, worn down, or just had a root canal. A bridge is a crown on either side of a gap, joined by a false tooth in the middle. Both are made from a scan or impression, and both need the bite checked carefully — a high crown is the most common cause of “it still hurts when I bite”.</p>
        <p class="body mt-2">Materials: full ceramic for front teeth where appearance matters; ceramic on a metal base or zirconia for back teeth where strength matters more. The choice is explained per tooth, not per price list.</p>
        <dl class="defs mt-3">
          <div class="defs__row"><dt>Visits</dt><dd>Two — preparation, then fitting</dd></div>
          <div class="defs__row"><dt>Between visits</dt><dd>A temporary crown, 5–10 days</dd></div>
          <div class="defs__row"><dt>Lifespan</dt><dd>Typically 10–15 years with care</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="section section--pill" id="wisdom">
  <div class="shell">
    <div class="split">
      <div class="split__body">
        <div class="mark"><b>07</b> Wisdom tooth removal</div>
        <h2 class="h2">The one everybody postpones.</h2>
        <p class="body mt-3">A wisdom tooth only needs removing if it is impacted, infected, damaging the tooth in front of it, or cannot be cleaned. Being “crooked” on its own is not always a reason — we will show you the X-ray and say which category yours falls into.</p>
        <p class="body mt-2">Simple extractions are done under local anaesthetic in a single appointment. Surgical removal of an impacted tooth takes longer, needs a small incision, and is followed by a week of soft food and careful rinsing. Both are done here; neither is referred out.</p>
        <p class="body mt-2">If you have swelling, a fever, or cannot open your mouth fully, call the clinic the same day rather than waiting for an appointment.</p>
        <div class="pill-row mt-3">
          <span class="chip">{icon("clock")} 30–60 min</span>
          <span class="chip">{icon("shield")} Local anaesthetic</span>
          <span class="chip">{icon("users")} Same-day emergency slots</span>
        </div>
      </div>
      <div class="split__media">
        <figure class="frame frame--4x5"><img src="assets/img/xray-review.jpg" width="900" height="1100" alt="X-ray review for wisdom tooth assessment" loading="lazy"></figure>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" id="hygiene">
  <div class="shell">
    <div class="split split--media-left">
      <div class="split__media">
        <figure class="frame frame--4x5"><img src="assets/img/gen-operatory.jpg" width="900" height="1100" alt="Dental operatory set up for a hygiene appointment" loading="lazy"></figure>
      </div>
      <div class="split__body">
        <div class="mark"><b>08</b> Scaling &amp; gum care</div>
        <h2 class="h2">The visit that keeps the rest of this page short.</h2>
        <p class="body mt-3">Bleeding when you brush is not normal, and it is not “just what happens”. It is gum inflammation, and it is reversible at this stage. Scaling removes the hardened deposit that a brush cannot reach; polishing removes the surface stain.</p>
        <p class="body mt-2">If the pockets around the teeth are already deep, scaling is done in quadrants with a review a few weeks later. If the gums have receded, that does not grow back — which is the argument for the six-month visit rather than the emergency one.</p>
        <ul class="bullets mt-3">
          <li>Usually one appointment of 30–45 minutes</li>
          <li>Some sensitivity and slight bleeding for a day or two afterwards</li>
          <li>Twice a year for most adults; more often if you smoke or have diabetes</li>
        </ul>
        <a class="btn mt-3" href="book.html?treatment=Check-up%20and%20scaling"><span>Book a check-up</span>{icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

{cta_band("Not sure which one you need?", "That is what the first appointment is for. Examination, X-ray if needed, and a written plan — no treatment on the day unless you ask for it.")}
"""

    jsonld = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Dental treatments at Smilecraft, Nikol",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": t.replace("&amp;", "&"),
             "url": (SITE["url"] + "/treatments.html" + h) if h.startswith("#") else (SITE["url"] + "/" + h)}
            for i, (h, n, t, d) in enumerate(rows)
        ],
    }
    return page(
        title="Dental Treatments in Nikol, Ahmedabad | Smilecraft Dental",
        desc="Implants, root canals, braces, aligners, smile design, whitening, crowns, wisdom tooth removal and gum care — all under one roof in Nikol, Ahmedabad.",
        path="treatments.html", body=body, active="treatments", depth=0, jsonld=jsonld,
        og_image="assets/img/gen-operatory.jpg",
    )
