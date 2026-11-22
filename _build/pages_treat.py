# -*- coding: utf-8 -*-
"""Treatments index + individual treatment pages."""
from urllib.parse import quote_plus
from chrome import *

STAR = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="m12 3.6 2.6 5.3 5.8.8-4.2 4.1 1 5.8-5.2-2.8-5.2 2.8 1-5.8-4.2-4.1 5.8-.8Z"/></svg>')


def crumb(items):
    out = []
    for label, href in items:
        if href:
            out.append('<a href="%s">%s</a><span aria-hidden="true">/</span>' % (href, label))
        else:
            out.append('<span aria-current="page">%s</span>' % label)
    return '<nav class="breadcrumb" aria-label="Breadcrumb">%s</nav>' % "".join(out)


def rating_pill():
    return ('<a class="pill" href="%s" target="_blank" rel="noopener">%s 5.0 &middot; 313 reviews</a>'
            % (SITE["maps"], icon("star")))


# ------------------------------------------------------------ index page ----
INDEX_INTRO = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">Treatments</p>
    <h1 style="margin-top:18px">Everything we do, and what it involves.</h1>
    <p class="lead">Four groups, twenty-odd procedures, one address. If the thing bothering you
    is not listed here, message us &mdash; it is probably still something we handle.</p>
    <div class="page-head__meta">
      <a class="btn" href="book.html">Book an appointment</a>
      <a class="btn btn--ghost" href="https://wa.me/919427451885" target="_blank" rel="noopener">__WA__ Ask on WhatsApp</a>
    </div>
  </div>
</section>

<div class="marquee">
  <div class="marquee__track">
    <span class="marquee__item">Dental implants</span>
    <span class="marquee__item">Root canal treatment</span>
    <span class="marquee__item">Clear aligners</span>
    <span class="marquee__item">Zirconia crowns</span>
    <span class="marquee__item">Wisdom tooth removal</span>
    <span class="marquee__item">Smile design</span>
    <span class="marquee__item">Teeth whitening</span>
    <span class="marquee__item">Scaling &amp; polishing</span>
    <span class="marquee__item">Kids&rsquo; dentistry</span>
    <span class="marquee__item">Full-mouth rehabilitation</span>
  </div>
</div>
"""

GROUPS = [
    ("Restorative &amp; surgical", "Fixing what is broken, and replacing what cannot be saved.",
     "restorative", [
         ("01", "Dental implants",
          "A titanium post in the jaw, topped with a crown. Single tooth, several, or a full arch.",
          "treatments/dental-implants.html"),
         ("02", "Root canal treatment",
          "Cleaning out an infected nerve, sealing the canals, then protecting the tooth with a crown.",
          "treatments/root-canal.html"),
         ("03", "Crowns, bridges &amp; caps",
          "Zirconia or metal-ceramic coverage for cracked, heavily filled or root-treated teeth.",
          "book.html?service=" + quote_plus("Crown, bridge or cap")),
         ("04", "Wisdom tooth removal",
          "Impacted third molars, including surgical removal under local anaesthesia.",
          "book.html?service=" + quote_plus("Wisdom tooth removal")),
         ("05", "Simple &amp; surgical extractions",
          "When a tooth genuinely cannot be saved, and what to do in the two weeks after.",
          "book.html?service=" + quote_plus("Something else")),
         ("06", "Full-mouth rehabilitation",
          "Multiple problems rebuilt in a planned sequence, usually over several months.",
          "book.html?service=" + quote_plus("Something else")),
     ]),
    ("Cosmetic dentistry", "For teeth that are healthy but you would rather they looked different.",
     "cosmetic", [
         ("07", "Smile design &amp; veneers",
          "Shape, shade and proportion planned first &mdash; then built in ceramic or composite.",
          "treatments/smile-design.html"),
         ("08", "Teeth whitening",
          "In-clinic bleaching with shade documentation, or a slower take-home kit.",
          "book.html?service=" + quote_plus("Teeth whitening")),
         ("09", "Composite bonding",
          "Resin built up directly on the tooth for chips, small gaps and worn edges.",
          "book.html?service=" + quote_plus("Smile design / veneers")),
         ("10", "Gum contouring",
          "Reshaping the gum line where it sits unevenly or too low over the front teeth.",
          "book.html?service=" + quote_plus("Something else")),
     ]),
    ("Orthodontics", "Straightening teeth, at fifteen or at fifty. Both are common here.",
     "orthodontics", [
         ("11", "Metal braces",
          "The most predictable route for complex crowding and bite correction.",
          "treatments/braces-aligners.html"),
         ("12", "Ceramic braces",
          "Same mechanics as metal, with tooth-coloured brackets and lighter wires.",
          "treatments/braces-aligners.html"),
         ("13", "Clear aligners",
          "Removable trays changed every week or two. Needs discipline: 20&ndash;22 hours a day.",
          "treatments/braces-aligners.html"),
         ("14", "Retainers",
          "Fixed or removable, after treatment. Not optional, however straight things look.",
          "book.html?service=" + quote_plus("Braces or clear aligners")),
     ]),
    ("Preventive &amp; children", "The cheapest dentistry there is: catching things early.",
     "preventive", [
         ("15", "Check-up &amp; X-rays",
          "A proper look, a radiograph where indicated, and a written plan if anything is found.",
          "book.html?service=" + quote_plus("Check-up / not sure yet")),
         ("16", "Scaling &amp; polishing",
          "Calculus and stain removal, gum assessment and honest instruction on what to do at home.",
          "book.html?service=" + quote_plus("Scaling & gum care")),
         ("17", "Fillings",
          "Tooth-coloured composite for decay caught early, before it reaches the nerve.",
          "book.html?service=" + quote_plus("Check-up / not sure yet")),
         ("18", "Children&rsquo;s dentistry",
          "First visits, fluoride, sealants and habit advice &mdash; ideally before anything hurts.",
          "book.html?service=" + quote_plus("Kids' dentistry")),
         ("19", "Night guards",
          "For grinding and jaw clenching that is flattening the back teeth.",
          "book.html?service=" + quote_plus("Something else")),
     ]),
]


def build_index():
    blocks = []
    for title, sub, anchor, rows in GROUPS:
        r = []
        for n, name, desc, href in rows:
            r.append(
                '<a class="svc-row" href="%s">'
                '<span class="svc-row__n">%s</span>'
                '<span class="svc-row__name">%s</span>'
                '<span class="svc-row__desc">%s</span>'
                '<span class="svc-row__go"><span class="arrow-btn">%s</span></span></a>'
                % (href, n, name, desc, icon("arrow")))
        blocks.append(
            '<div class="mt-l" id="%s" data-reveal>'
            '<div class="sec-head" style="margin-bottom:0">'
            '<div class="sec-head__l"><p class="eyebrow">%s</p>'
            '<h2 style="font-size:clamp(1.6rem,2.6vw,2.2rem);margin-top:10px">%s</h2></div>'
            '<div class="sec-head__r"><p>%s</p></div></div>'
            '<div class="svc-index" style="margin-top:26px">%s</div></div>'
            % (anchor, title, title, sub, "".join(r)))

    body = (INDEX_INTRO
            .replace("__CRUMB__", crumb([("Home", "index.html"), ("Treatments", None)]))
            .replace("__WA__", icon("wa"))
            + """
<section class="section">
  <div class="wrap">__BLOCKS__</div>
</section>

<section class="section section--paper2">
  <div class="wrap grid-3">
    <div class="card"><div class="card__ic">__CHK__</div><h3>A written plan</h3>
      <p>Every treatment you need, in the order it should happen, with the cost against each line.
      Nothing gets added without you being told.</p></div>
    <div class="card"><div class="card__ic">__CLOCK__</div><h3>Realistic timelines</h3>
      <p>We will tell you if a crown takes two visits and an implant takes four months. We would
      rather you knew before than halfway through.</p></div>
    <div class="card"><div class="card__ic">__SHIELD__</div><h3>Second opinions welcome</h3>
      <p>Bring the plan another clinic gave you. We will go through it honestly, including the
      parts we agree with.</p></div>
  </div>
</section>

<section class="cta-band">
  <span class="cta-band__mark" aria-hidden="true">S</span>
  <div class="wrap cta-band__in">
    <div><h2>Not sure which of these you need?</h2>
      <p>That is what the first appointment is for. Describe the problem on WhatsApp and we will
      tell you whether it needs a visit at all.</p></div>
    <div class="cta-band__actions">
      <a class="btn btn--light btn--lg" href="https://wa.me/919427451885" target="_blank" rel="noopener">__WA__ Message on WhatsApp</a>
      <a class="btn btn--ghost btn--lg" href="book.html">Book a visit</a>
    </div>
  </div>
</section>
""" .replace("__BLOCKS__", "".join(blocks))
      .replace("__CHK__", icon("check"))
      .replace("__CLOCK__", icon("clock"))
      .replace("__SHIELD__", icon("shield"))
      .replace("__WA__", icon("wa")))

    page("treatments.html", "Dental Treatments in Nikol, Ahmedabad | Smilecraft",
         "Dental implants, root canal treatment, braces, clear aligners, smile design, whitening, "
         "crowns and children's dentistry at Smilecraft, Blueberry Complex, Nikol.",
         body, "", "treatments", "treatments.html",
         schema=[breadcrumb_schema([("Home", ""), ("Treatments", "treatments.html")]),
                 {"@context": "https://schema.org", "@type": "ItemList",
                  "itemListElement": [
                      {"@type": "ListItem", "position": i + 1, "name": n}
                      for i, (n, _) in enumerate([
                          ("Dental implants", ""), ("Root canal treatment", ""),
                          ("Crowns, bridges and caps", ""), ("Wisdom tooth removal", ""),
                          ("Smile design and veneers", ""), ("Teeth whitening", ""),
                          ("Braces", ""), ("Clear aligners", ""),
                          ("Scaling and polishing", ""), ("Children's dentistry", "")])]}])


# ---------------------------------------------------------- detail pages ----
def detail(cfg):
    root = "../"
    svc = quote_plus(cfg["service"])
    anchors = "".join('<a href="#%s">%s</a>' % (a, t) for a, t in cfg["jump"])

    rows = "".join(
        '<div><dt>%s</dt><dd>%s</dd></div>' % (k, v) for k, v in cfg["facts"])

    faqs = "".join(
        '<details class="faq__item"><summary>%s</summary><div class="faq__a">%s</div></details>'
        % (q, a) for q, a in cfg["faqs"])

    related = "".join(
        '<a class="card" href="%s" style="display:block"><h3>%s</h3><p>%s</p>'
        '<p style="margin-top:14px"><span class="tlink">Read more</span></p></a>' % (h, t, d)
        for t, d, h in cfg["related"])

    body = """
<section class="page-head">
  <div class="wrap">
    __CRUMB__
    <p class="eyebrow">{kicker}</p>
    <h1 style="margin-top:18px">{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="page-head__meta">
      <a class="btn" href="{root}book.html?service={svc}">Book this treatment</a>
      <a class="btn btn--ghost" href="https://wa.me/{wa}" target="_blank" rel="noopener">{wa_ic} Ask a question</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap article">
    <div class="prose">{prose}</div>
    <aside class="aside-card">
      <h4>At a glance</h4>
      <p>{aside_intro}</p>
      <a class="btn btn--block" href="{root}book.html?service={svc}">Book a consultation</a>
      <dl class="aside-card__rows">{rows}</dl>
      <nav class="jump" aria-label="On this page">{anchors}</nav>
    </aside>
  </div>
</section>

<section class="section section--paper2">
  <div class="wrap wrap--narrow">
    <p class="eyebrow">Questions</p>
    <h2 style="margin-top:14px;margin-bottom:32px">Things people ask before booking.</h2>
    <div class="faq">{faqs}</div>
    <p class="small muted mt-l">Still unsure? Message the clinic on WhatsApp with your question &mdash;
    you will get a straight answer, not a sales pitch.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-head__l"><p class="eyebrow">Also worth reading</p><h2>Related treatments</h2></div>
    </div>
    <div class="grid-3">{related}</div>
  </div>
</section>
""".format(root=root, kicker=cfg["kicker"], h1=cfg["h1"], lead=cfg["lead"], svc=svc,
           wa=SITE["wa"], wa_ic=icon("wa"), prose=cfg["prose"],
           aside_intro=cfg["aside_intro"], rows=rows, anchors=anchors,
           faqs=faqs, related=related)

    body = body.replace("__CRUMB__", crumb([
        ("Home", root + "index.html"),
        ("Treatments", root + "treatments.html"),
        (cfg["crumb"], None),
    ]))

    page(cfg["path"], cfg["title"], cfg["desc"], body, root, "treatments",
         cfg["path"], og=cfg["og"],
         schema=[breadcrumb_schema([("Home", ""), ("Treatments", "treatments.html"),
                                    (cfg["crumb"], cfg["path"])]),
                 faq_schema([(q, a) for q, a in cfg["faqs"]])])


IMPLANTS = {
    "path": "treatments/dental-implants.html",
    "crumb": "Dental implants",
    "service": "Dental implants",
    "title": "Dental Implants in Nikol, Ahmedabad | Smilecraft Implant Center",
    "desc": "Single tooth and full-arch dental implants at Smilecraft, Nikol. Planned on imaging, "
            "placed under local anaesthesia. What the procedure involves, how long it takes, what it costs.",
    "og": "assets/img/gen-implant.jpg",
    "kicker": "Implant centre",
    "h1": "Dental implants, planned before anything is drilled.",
    "lead": "A titanium post takes the place of the root; a crown takes the place of the tooth. "
            "It is the closest thing dentistry has to putting a tooth back &mdash; and it only works "
            "if the planning is honest about the bone you have.",
    "aside_intro": "Implant placement is a minor surgical procedure done under local anaesthesia, "
                   "usually in a single sitting of 45&ndash;90 minutes.",
    "facts": [("Sitting 1", "Consultation, X-ray, plan"),
              ("Placement", "45&ndash;90 minutes"),
              ("Healing", "3&ndash;6 months"),
              ("Final crown", "2 visits"),
              ("Anaesthesia", "Local")],
    "jump": [("what", "What an implant is"), ("who", "Who it suits"),
             ("process", "The process"), ("after", "Afterwards"),
             ("cost", "What drives cost")],
    "prose": """
<p class="lead">Most people arrive at this page because they are missing a tooth and have been
told, or have read, that a bridge means grinding down the two healthy teeth either side. That is
the single best argument for an implant, and it is a fair one.</p>

<h2 id="what">What an implant actually is</h2>
<p>Three parts. A <strong>titanium fixture</strong> that is placed into the jawbone and, over a few
months, fuses with it. An <strong>abutment</strong> that screws into the fixture and connects to
the visible tooth. And a <strong>crown</strong> &mdash; ceramic or zirconia &mdash; that is shaped and
shaded to match its neighbours.</p>
<p>Because nothing is joined to the adjacent teeth, they stay untouched. Because the fixture sits
in bone, it also keeps that bone from shrinking away the way it does after an extraction.</p>

<h2 id="who">Who it suits &mdash; and who it doesn&rsquo;t</h2>
<p>Implants work well for a single missing tooth, for several missing teeth (sometimes on two
implants rather than one each), and for a full arch, where four to six implants can carry a fixed
bridge.</p>
<p>What matters is the bone. If there has been a tooth missing for years, or there has been gum
disease, there may not be enough volume in the right place. That is not a dead end &mdash; a graft
can usually rebuild it &mdash; but it adds a step and a few months, and you should be told that
before you commit rather than after.</p>
<p>It is generally not the right answer where the bone is still growing, where uncontrolled
diabetes or heavy smoking makes healing unpredictable, or where the underlying gum disease has not
been treated. We will say so plainly if that is your situation.</p>

<div class="fig"><img src="../assets/img/gen-implant.jpg" alt="A titanium implant fixture with a ceramic crown, beside a dental radiograph" loading="lazy">
<figcaption>The fixture and the crown, photographed next to the radiograph used to plan its position.</figcaption></div>

<h2 id="process">The process, step by step</h2>
<ol>
<li><strong>Consultation and imaging.</strong> A clinical examination and a radiograph; for more
complex cases, a CBCT scan to measure the bone in three dimensions.</li>
<li><strong>A written plan.</strong> How many implants, what length and diameter, whether a graft
is needed, how long it will take, and what it costs. You take this away with you.</li>
<li><strong>Placement.</strong> Under local anaesthesia. The site is opened, the bone is prepared
with sequential drills, and the fixture is placed. Most people describe pressure rather than pain.
Sutures come out after seven to ten days.</li>
<li><strong>Healing.</strong> Three to six months, during which the bone integrates with the
fixture. You will have a temporary tooth or a small healing cap in the meantime.</li>
<li><strong>The crown.</strong> An impression or scan, a shade match, and the final crown fitted
&mdash; usually two short visits.</li>
</ol>
<p>In selected cases &mdash; good bone, a single tooth, no infection &mdash; the implant and a
temporary crown can be done in one stage. It is not suitable for everyone, and any clinic that
offers it to everyone is not planning properly.</p>

<h2 id="after">Afterwards</h2>
<p>The first two or three days involve some swelling, and possibly a little bruising. Cold packs,
the prescribed medication and soft food for a few days covers most of it. Avoid smoking for at
least a fortnight &mdash; it is the single biggest avoidable cause of an implant failing.</p>
<p>Long term, an implant needs cleaning like a tooth, and rather more attention at the gum line,
because it has no ligament to warn you when something is wrong. We will put you on a review
schedule rather than simply waving you off.</p>

<h2 id="cost">What drives the cost</h2>
<p>There is no single price for an implant, at this clinic or any other, because the price is
really the sum of several decisions: how many implants, which system, whether a bone graft or
sinus lift is needed, what the crown is made of, and whether a temporary restoration is required
during healing. Two patients with &ldquo;one missing tooth&rdquo; can have very different plans.</p>
<p>We quote in writing after the examination, item by item, and we do not revise it upwards
mid-treatment without telling you why. Ask us for the figure before you book, and ask the same
question of any clinic you are comparing us with.</p>
""",
    "faqs": [
        ("Does getting an implant hurt?",
         "<p>The placement itself is done under local anaesthesia, so you should not feel sharp pain "
         "&mdash; pressure and vibration, yes. Most people take a painkiller for a day or two "
         "afterwards and are back at work the next day.</p>"),
        ("How long does the whole thing take?",
         "<p>Typically four to six months from placement to final crown, because the bone needs time "
         "to integrate. If a graft is required, add three to four months before placement even "
         "begins. Single-stage cases can be faster.</p>"),
        ("Can I have an implant if I have diabetes?",
         "<p>Often yes, if it is well controlled and your physician is comfortable. Poorly controlled "
         "diabetes affects healing and we would want that addressed first. Bring your recent reports "
         "to the consultation.</p>"),
        ("What if there isn&rsquo;t enough bone?",
         "<p>A bone graft &mdash; either at the time of extraction or later &mdash; can usually "
         "rebuild the site. It adds a procedure and a few months, and it is planned for, not "
         "discovered halfway through.</p>"),
        ("Is a bridge cheaper?",
         "<p>Usually, yes, in the short term. A bridge also means preparing the two adjacent teeth, "
         "which may be perfectly healthy. Over fifteen or twenty years the arithmetic often reverses. "
         "We will lay out both, honestly, and let you choose.</p>"),
    ],
    "related": [
        ("Root canal treatment", "Saving a tooth is almost always better than replacing it. Start here if the tooth can still be kept.", "root-canal.html"),
        ("Crowns &amp; bridges", "The restorative half of the same decision, and what a crown is made of.", "../treatments.html#restorative"),
        ("Smile design", "Where implants sit alongside cosmetic work on the front teeth.", "smile-design.html"),
    ],
}

ROOTCANAL = {
    "path": "treatments/root-canal.html",
    "crumb": "Root canal treatment",
    "service": "Root canal treatment",
    "title": "Root Canal Treatment in Nikol, Ahmedabad | Smilecraft Dental",
    "desc": "Root canal treatment at Smilecraft, Nikol Ahmedabad. What happens during RCT, how many "
            "sittings it takes, aftercare, and what drives the cost. 30 Google reviews mention RCT.",
    "og": "assets/img/gen-doctor.jpg",
    "kicker": "Endodontics",
    "h1": "Root canal treatment, without the dread.",
    "lead": "Thirty of our Google reviews are about root canals. The word that keeps appearing in "
            "them is not &ldquo;painful&rdquo; &mdash; it is the opposite. Here is exactly what the "
            "appointment involves.",
    "aside_intro": "Most first-time root canals here are completed in one or two sittings, under "
                   "local anaesthesia, with the tooth isolated by a rubber dam.",
    "facts": [("Sittings", "1&ndash;2 typically"),
              ("Time per visit", "45&ndash;75 minutes"),
              ("Anaesthesia", "Local"),
              ("Then", "A crown, usually"),
              ("Retreatment", "Sometimes needed")],
    "jump": [("what", "What it is"), ("signs", "Signs you need one"),
             ("process", "During the visit"), ("after", "Afterwards"),
             ("cost", "Cost")],
    "prose": """
<p class="lead">The reputation is worse than the reality. A root canal is uncomfortable because of
the infection that made it necessary &mdash; not because of the treatment. Removing the infected
tissue is what stops the pain.</p>

<h2 id="what">What a root canal actually does</h2>
<p>Inside every tooth is a chamber of soft tissue &mdash; the pulp &mdash; containing nerves and blood
vessels. When decay or a crack lets bacteria in, that tissue becomes inflamed and then infected.
Because the tooth is sealed, the pressure has nowhere to go. That is the throbbing pain, and the
abscess at the root tip.</p>
<p>A root canal removes the infected pulp, cleans and shapes the canals, disinfects them, and seals
them. The tooth stays in your mouth, keeps its root, and keeps the bone around it. It stops being
a living tooth; it does not stop being a useful one.</p>

<h2 id="signs">Signs you might need one</h2>
<ul>
<li>Pain that lingers for more than a few seconds after something hot or cold.</li>
<li>A dull ache when you bite down, or tenderness to tapping.</li>
<li>Swelling of the gum near a tooth, or a small pimple-like bump that comes and goes.</li>
<li>Discolouration of a single tooth.</li>
<li>Sometimes, no symptoms at all &mdash; found on an X-ray during a routine check-up.</li>
</ul>
<p>Pain on its own is not a diagnosis. A tooth that is sensitive for a second and settles is often
just recession or a lost filling. The examination and radiograph are what decide it.</p>

<h2 id="process">During the visit</h2>
<ol>
<li><strong>Isolation.</strong> The tooth is numbed, then isolated with a rubber dam &mdash; a sheet
that keeps saliva and bacteria out of the canals while we work. It is not optional; a root canal
done without one is a gamble.</li>
<li><strong>Access.</strong> A small opening is made through the top of the tooth.</li>
<li><strong>Cleaning and shaping.</strong> The canals are measured, then cleaned with rotary
nickel-titanium files and irrigated with disinfecting solutions. This is the part that takes
the time.</li>
<li><strong>Sealing.</strong> The canals are dried and filled with a rubber-like material, and the
access is closed.</li>
<li><strong>The crown.</strong> A root-treated tooth becomes brittle. Almost always it needs a
crown to survive biting forces &mdash; and that is a separate, later appointment.</li>
</ol>
<div class="fig"><img src="../assets/img/gen-doctor.jpg" alt="Dentist wearing gloves examining a patient in the dental chair" loading="lazy">
<figcaption>Most of the appointment is diagnosis and isolation, not drilling.</figcaption></div>

<h2 id="after">Afterwards</h2>
<p>For two or three days the tooth may feel tender when you bite, because the ligament around the
root has been irritated. That settles. A painkiller is usually enough.</p>
<p>Until the crown is on, avoid chewing hard food on that side &mdash; an unrestored root-treated
tooth can split, and a split tooth cannot be saved. This is the single most common way a good root
canal ends badly.</p>
<p>If swelling returns, or the tooth becomes painful again weeks later, tell us. Retreatment is
sometimes necessary and is far easier than leaving it.</p>

<h2 id="cost">What drives the cost</h2>
<p>The number of canals is the main factor &mdash; a front tooth typically has one, a molar has
three or four &mdash; along with whether it is a first treatment or a retreatment of a tooth
someone else started, and what kind of crown goes on afterwards.</p>
<p>We quote after the examination, with the crown priced separately so you can see what you are
paying for. If a tooth is not restorable, we will say that too, rather than charging for a root
canal that will fail.</p>
""",
    "faqs": [
        ("Is a root canal painful?",
         "<p>The treatment is done under local anaesthesia, so it should not be. Most of the pain "
         "people associate with root canals comes from the infection beforehand &mdash; which is "
         "exactly what the treatment resolves.</p>"),
        ("How many visits will it take?",
         "<p>One or two for most teeth. Molars with curved or calcified canals, retreatment, or a "
         "tooth with a large abscess may need an extra visit with medication in between.</p>"),
        ("Can I just have the tooth removed instead?",
         "<p>You can, and sometimes that is the right call &mdash; if the tooth is split or there is "
         "too little left to restore. But extraction is cheaper today and usually costs more later, "
         "once the gap needs an implant or bridge. We will explain both.</p>"),
        ("Do I really need a crown afterwards?",
         "<p>For back teeth, essentially yes. The tooth is more brittle after treatment and the "
         "chewing loads are high. Front teeth sometimes manage with a filling, depending on how much "
         "tooth is left.</p>"),
        ("How long does a root canal last?",
         "<p>With a good seal, a proper crown and reasonable hygiene, many last decades. The usual "
         "reasons for failure are a leaked restoration, a cracked tooth, or untreated canals &mdash; "
         "all of which is why the crown matters as much as the root canal itself.</p>"),
    ],
    "related": [
        ("Dental implants", "If a tooth has already been lost and cannot be saved.", "dental-implants.html"),
        ("Crowns &amp; bridges", "The restoration that protects a root-treated tooth.", "../treatments.html#restorative"),
        ("Smile design", "When the concern is appearance rather than pain.", "smile-design.html"),
    ],
}

ORTHO = {
    "path": "treatments/braces-aligners.html",
    "crumb": "Braces &amp; aligners",
    "service": "Braces or clear aligners",
    "title": "Braces and Clear Aligners in Nikol, Ahmedabad | Smilecraft",
    "desc": "Metal braces, ceramic braces and clear aligners for adults and teenagers at Smilecraft, "
            "Nikol. Records, treatment length, retention and what it involves.",
    "og": "assets/img/aligner-vs-braces.jpg",
    "kicker": "Orthodontics",
    "h1": "Straightening teeth, at fifteen or at fifty.",
    "lead": "Both are common here. The mechanics do not change with age &mdash; what changes is how "
            "much time you have for appointments, and how visible you are willing for the hardware "
            "to be.",
    "aside_intro": "Orthodontic treatment starts with records &mdash; photographs, a radiograph and a "
                   "scan or impressions &mdash; before any bracket is bonded.",
    "facts": [("Records", "1 visit"),
              ("Typical duration", "12&ndash;24 months"),
              ("Reviews", "Every 4&ndash;8 weeks"),
              ("Aligners", "20&ndash;22 hrs/day"),
              ("Retainers", "Long term")],
    "jump": [("options", "The options"), ("who", "What it fixes"),
             ("process", "How it runs"), ("after", "Retention"),
             ("cost", "Cost")],
    "prose": """
<p class="lead">Crowded teeth are harder to clean, which is why they decay more. That is the
clinical argument. The other argument &mdash; that you would rather not hide your teeth in
photographs &mdash; is just as valid, and we will not pretend otherwise.</p>

<h2 id="options">The options, honestly compared</h2>
<h3>Metal braces</h3>
<p>Stainless steel brackets and wires. The most predictable option for complex cases, and usually
the least expensive. Visible, and the wires can irritate for the first week or two. Modern
self-ligating brackets need fewer visits and hold less plaque than the older tied design.</p>

<h3>Ceramic braces</h3>
<p>Tooth-coloured brackets. Less obvious from a distance, slightly more fragile, and a little more
expensive. The wire is still metal, so &ldquo;invisible&rdquo; is not the right word.</p>

<h3>Clear aligners</h3>
<p>A series of removable trays, changed every week or two, that move teeth in small planned steps.
Excellent for crowding, spacing and mild bite correction. Not magic: they only work while they are
in your mouth, and they need to be in for 20&ndash;22 hours a day. Patients who take them out for
meetings, meals and photographs do not finish on schedule.</p>

<div class="fig"><img src="../assets/img/aligner-vs-braces.jpg" alt="A clear aligner held in a hand beside a model of teeth with fixed braces" loading="lazy">
<figcaption>The same problem, two routes: a removable aligner, or fixed brackets and wire.</figcaption></div>

<h2 id="who">What it fixes</h2>
<ul>
<li>Crowding and overlapping teeth.</li>
<li>Gaps and spacing.</li>
<li>Deep bites, open bites and crossbites.</li>
<li>Teeth that have drifted after an earlier extraction or a lost tooth.</li>
<li>Relapse after orthodontics as a teenager &mdash; very common in the thirties and forties.</li>
</ul>
<p>Jaw discrepancies in a growing child are a different problem, sometimes needing functional
appliances or a referral. If that is what we see, we will say so at the first visit.</p>

<h2 id="process">How the treatment runs</h2>
<ol>
<li><strong>Records.</strong> Photographs, a radiograph, and a scan or impressions. This is what the
plan is built on.</li>
<li><strong>The plan.</strong> Which option, how long, whether any teeth need extracting to make
room, and the cost &mdash; in writing.</li>
<li><strong>Fitting.</strong> Brackets bonded and wire placed, or the first aligners delivered with
instructions and a schedule.</li>
<li><strong>Reviews.</strong> Every four to eight weeks for braces; longer intervals for aligners,
with remote photo check-ins in between.</li>
<li><strong>Debonding.</strong> Braces removed, teeth cleaned and polished, retainers fitted.</li>
</ol>

<h2 id="after">Retention is not optional</h2>
<p>Teeth move back. They do it for years after treatment ends, and no appliance prevents it
entirely. A fixed wire behind the front teeth, a removable retainer at night, or both &mdash;
usually for the long term.</p>
<p>Patients who stop wearing retainers after six months are the reason we see the same case twice.
It is the least glamorous part of orthodontics and the part that decides whether the money was
well spent.</p>

<h2 id="cost">What drives the cost</h2>
<p>The type of appliance, the complexity of the case, how long it runs, whether extractions or
additional appliances are needed, and the retainers at the end. Aligners are priced by the number
of stages required.</p>
<p>Payments are usually split across the treatment rather than paid up front, with a portion at
each review. Ask at the consultation and we will set out the schedule.</p>
""",
    "faqs": [
        ("Am I too old for braces?",
         "<p>No. Provided the gums and bone are healthy, adults are treated routinely here. The main "
         "difference is that adult treatment takes a little longer and retention matters more.</p>"),
        ("Metal or clear &mdash; which should I choose?",
         "<p>It depends on the case and on you. Complex bite correction is more predictable with "
         "fixed braces; mild to moderate crowding is well suited to aligners. We will show you both "
         "plans with timelines rather than pushing one.</p>"),
        ("How often are the appointments?",
         "<p>Every four to eight weeks for braces. Aligners need fewer in-person visits &mdash; often "
         "six to eight weeks &mdash; with photo check-ins in between.</p>"),
        ("Do braces hurt?",
         "<p>They are uncomfortable rather than painful. The first week and the day after each "
         "adjustment are the worst of it: tenderness, and a wire that rubs. Soft food and the wax we "
         "give you get most people through.</p>"),
        ("Will I need teeth removed?",
         "<p>Sometimes, where there is significant crowding and not enough space. It is decided at "
         "the planning stage, not halfway through, and you will know before treatment starts.</p>"),
    ],
    "related": [
        ("Smile design", "When alignment is fine but shape and shade are the concern.", "smile-design.html"),
        ("Teeth whitening", "Often done after orthodontics, once the brackets are off.", "../treatments.html#cosmetic"),
        ("Dental implants", "Where a missing tooth is part of the alignment problem.", "dental-implants.html"),
    ],
}

SMILE = {
    "path": "treatments/smile-design.html",
    "crumb": "Smile design",
    "service": "Smile design / veneers",
    "title": "Smile Design and Veneers in Nikol, Ahmedabad | Smilecraft",
    "desc": "Smile design, ceramic veneers and composite bonding at Smilecraft, Nikol. How the shape "
            "and shade are planned before anything is made, and what it realistically involves.",
    "og": "assets/img/smile-macro.jpg",
    "kicker": "Cosmetic dentistry",
    "h1": "A smile that still looks like yours.",
    "lead": "The worst cosmetic dentistry is the kind people notice. Smile design here starts from "
            "your face, your age and your other teeth &mdash; not from a photograph of someone else.",
    "aside_intro": "Cosmetic work is planned on photographs and a trial smile before any tooth is "
                   "prepared, so you can see the proposal first.",
    "facts": [("Planning", "Photos &amp; mock-up"),
              ("Trial smile", "Before preparation"),
              ("Veneers", "2&ndash;3 visits"),
              ("Bonding", "1 visit"),
              ("Longevity", "With care, years")],
    "jump": [("what", "What it covers"), ("who", "Who it suits"),
             ("process", "The process"), ("honest", "The honest part"),
             ("cost", "Cost")],
    "prose": """
<p class="lead">Smile design is not a single procedure. It is a plan that may involve whitening,
composite bonding, ceramic veneers, crowns, or simply cleaning and leaving things alone. The value
is in deciding which, and in what order.</p>

<h2 id="what">What it can change</h2>
<ul>
<li><strong>Colour</strong> &mdash; staining that cleaning will not shift, or a single dark tooth.</li>
<li><strong>Shape</strong> &mdash; chipped edges, worn biting surfaces, teeth that are short or
overly rounded.</li>
<li><strong>Proportion</strong> &mdash; a tooth that is noticeably wider or narrower than its
neighbours.</li>
<li><strong>Spacing</strong> &mdash; small gaps closed with bonding or veneers, larger ones with
orthodontics first.</li>
<li><strong>Gum line</strong> &mdash; where the gums sit unevenly across the front teeth.</li>
</ul>
<p>What it cannot do is fix a bite. If the problem is alignment, orthodontics comes first and
cosmetics second &mdash; otherwise you put expensive ceramic on teeth that are in the wrong place.</p>

<div class="fig"><img src="../assets/img/smile-macro.jpg" alt="Close-up of a natural-looking smile after cosmetic treatment" loading="lazy">
<figcaption>The aim is a result that reads as healthy, not as dentistry.</figcaption></div>

<h2 id="who">Who it suits</h2>
<p>Adults with healthy teeth and gums, who want a specific change and can describe it. Also people
whose front teeth have been chipped or worn for years and who have stopped smiling in photographs
because of it.</p>
<p>It is not the right starting point where there is active decay, untreated gum disease, or heavy
grinding that has not been addressed. Ceramic is unforgiving of a clenching habit; a night guard is
part of the plan, not an upsell.</p>

<h2 id="process">The process</h2>
<ol>
<li><strong>Consultation and photographs.</strong> Close-up and full-face photographs, a shade
record, and a conversation about what you actually want to change.</li>
<li><strong>A proposal.</strong> Which teeth, which material, how many visits, and the cost.</li>
<li><strong>Trial smile or mock-up.</strong> Composite or a digital mock-up placed on the teeth
without drilling, so you can see the proposal in your own mouth &mdash; and change your mind
before anything is permanent.</li>
<li><strong>Preparation.</strong> Minimal for veneers &mdash; often a fraction of a millimetre of
enamel &mdash; and none at all for bonding.</li>
<li><strong>Fitting.</strong> Impressions or a scan go to the lab; temporaries in the meantime; the
final restorations are tried, adjusted and bonded.</li>
</ol>

<h2 id="honest">The honest part</h2>
<p>Veneers are permanent. Enamel does not grow back, and the teeth will always need some form of
restoration afterwards. That is why we push the trial smile stage and why we will happily talk you
out of treatment if whitening and cleaning would achieve most of what you want for a fraction of
the cost.</p>
<p>We also will not promise a result that looks untouched by dentistry. Some clinics do. Teeth that
have been rebuilt in ceramic look like teeth that have been rebuilt in ceramic &mdash; the aim is
that they look well, in proportion, and like they belong to your face.</p>

<h2 id="cost">What drives the cost</h2>
<p>The number of teeth involved, whether the material is composite or laboratory ceramic, the
complexity of the shade matching, and whether gum contouring or orthodontics is needed first.</p>
<p>Composite bonding is done directly in the chair and costs less per tooth; ceramic veneers are
made by a technician, take longer, and last differently. We will give you both numbers.</p>
""",
    "faqs": [
        ("Will veneers look fake?",
         "<p>They can, and that is usually a shade or proportion problem rather than a materials "
         "problem. We match to the adjacent teeth and to your age, and we use the trial smile so you "
         "can see the proposal before committing.</p>"),
        ("How much tooth is removed?",
         "<p>For ceramic veneers, typically 0.3&ndash;0.7 mm of enamel &mdash; sometimes none, where "
         "the teeth are already worn. Composite bonding requires no drilling at all in most cases.</p>"),
        ("How long do veneers last?",
         "<p>Many years with good hygiene and a night guard if you grind. Chipping is the usual "
         "failure, and it is usually repairable. Bonding wears faster and is easier to refresh.</p>"),
        ("Can I just get my teeth whitened instead?",
         "<p>Very often, yes. If the teeth are the right shape and the only issue is colour, "
         "whitening is cheaper, reversible and does not remove tooth structure. We will say so if "
         "that is the case.</p>"),
        ("Does it hurt?",
         "<p>Preparation is done under local anaesthesia. Some sensitivity for a few days afterwards "
         "is normal, particularly with whitening, and settles.</p>"),
    ],
    "related": [
        ("Teeth whitening", "The least invasive way to change colour, and often the first step.", "../treatments.html#cosmetic"),
        ("Braces &amp; aligners", "When the teeth need moving before they need re-shaping.", "braces-aligners.html"),
        ("Dental implants", "For a missing front tooth in the middle of a smile plan.", "dental-implants.html"),
    ],
}


def build_all():
    build_index()
    for cfg in (IMPLANTS, ROOTCANAL, ORTHO, SMILE):
        detail(cfg)


if __name__ == "__main__":
    build_all()
