# Visual QA record — v2 build

Facts captured from rendered screenshots before image trimming. Use this if you need to verify the
build still matches what was reviewed.

## Home, desktop (1400 px, viewed scaled)

- Header: ink topbar with `SHOP 214, SECOND FLOOR, BLUEBERRY COMPLEX, NIKOL` · live status
  `CLOSED · OPENS TOMORROW 9:00 AM` · `+91 94274 51885`. Nav in mono uppercase:
  TREATMENTS / REVIEWS / GALLERY / ABOUT / CONTACT, then `CALL` outline + `BOOK A VISIT` solid.
- Hero: meta row `NIKOL · AHMEDABAD` / `MULTISPECIALITY & IMPLANT CENTRE` / ★★★★★ `5.0 / 313`.
  H1 renders as two lines: "A calmer kind" then "of dentist visit." with the second half in teal
  italic (Fraunces). Lead paragraph, two buttons, three pills
  (`MON – SAT · 9 TO 9`, `CLOSED SUNDAYS`, `TWO-WHEELER PARKING`).
- Hero visual: arch-cropped portrait, vertical mono label "Blueberry Complex · 2nd floor",
  floating card `FIND US / Blueberry Complex / Shop 214, 2nd floor / Nikol · Ahmedabad 380049`.
- Stats strip: `5.0` / `313` / `30` / `9–9` with mono captions; counters animate up.
- Manifesto (ink): "We would rather save your tooth than *sell you an implant*." aside paragraph,
  then three columns: **Written before we start** / **Single-use, always** / **Nothing on commission**.
- Treatments: sticky left column `02 What we treat` + "Everything under one roof." + All treatments
  link; right column 8 rows: 01 Dental implants, 02 Root canal treatment, 03 Braces & clear aligners,
  04 Smile design & veneers, 05 Teeth whitening, 06 Crowns, bridges & caps, 07 Wisdom tooth removal,
  08 Scaling & gum care.
- Process (ink): label `03 — A VISIT, START TO FINISH`, big numeral with `/05`, progress bar,
  steps: Book in about a minute / We look, properly / You get a plan, in writing /
  Treatment, at your pace / Review, then aftercare.
- Doctor: `04 The dentist you'll see` — Dr Priya Patel, cred rows Focus (Implants, endodontics,
  smile design), Languages (Gujarati, Hindi, English), Clinic (Blueberry Complex, Nikol),
  On Google (5.0 from 313 reviews).
- Tour: `05 A look inside` — "See the room before you sit in it.", video playing.
- Reviews: `06 Patient reviews` — "People keep using the word “painless”." 5.0 + stars block,
  horizontal slider, prev/next arrows, All reviews link.
- Gallery: `07 — Gallery` dark pinned section, "The clinic, in pictures.", `SCROLL →`.
- Visit: `08 Finding us` — "Second floor, above the handloom showroom.", address block, hours table,
  map iframe.
- CTA (ink): "Two minutes on WhatsApp is usually all it takes." + MESSAGE US / CALL.
- Footer (ink): 4 columns, giant outlined `Smilecraft` wordmark, mono bottom bar with © 2026.

## Home, mobile (≈473 px)

- Hero H1 stacks to two lines, full-bleed arch image below the copy, FIND US card bottom-left,
  floating `CLOSED · OPENS TOMORROW 9:00 AM` pill hidden on mobile (by design).
- Stats collapse to 2×2 grid.
- Fixed bottom bar: `CALL` / `WHATSAPP` / `BOOK A VISIT`.
- WhatsApp float sits above the bar.

## Book page

- Breadcrumb `HOME / BOOK AN APPOINTMENT`, eyebrow `APPOINTMENTS`,
  H1 "Book a visit — it takes about a minute."
- Form: step marker `1 WHO YOU ARE` → Full name, Mobile number, Email (optional),
  chips `FIRST VISIT` / `I'M AN EXISTING PATIENT`; step marker `2 WHY YOU'RE COMING` →
  Reason for the visit, Preferred date, Preferred time, notes, consent checkbox.
- Inputs are transparent with 1 px hairline borders; labels and chips are mono uppercase.

## Known-good behaviours

- Live open/closed status computed for Asia/Kolkata (screenshot taken on a Sunday showed closed).
- WhatsApp handoff produced
  `https://api.whatsapp.com/send/?phone=919427451885&text=...` and resolved to the real profile
  "Smilecraft Multispeciality Dental Clinic and Implant Center".
- `https://search.google.com/local/writereview?placeid=ChIJBXJ2CL6HXjkRyDeaS15eANI` redirects to
  Google sign-in with that place id in `continue=` — valid review link.

## Fixed during QA

1. `.split` class collision (split-text vs two-column layout) → renamed to `.txt-split`.
2. Root-level pages carried `../` asset paths meant for `/treatments/` → corrected.
3. Consent label inherited uppercase field-label styling → scoped rule added.
4. Gallery rows had mismatched aspect ratios → fixed row heights.
5. Ghost button invisible on dark CTA band → light colour override.
6. Section headings crushed into a 42ch column → 560 px.
7. Mobile booking page put the info card above the form → form now first.
8. Parallax unclamped → clamped to ±64 px.
