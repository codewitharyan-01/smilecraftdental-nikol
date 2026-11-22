# Image-derived facts — permanent record

Everything below was read from the Google Business listing, Maps place data, or rendered screenshots.
**No image is needed to recover any of it.** If photos are replaced, this file remains the source of
truth.

---

## 1. Identifiers (verified, do not change)

| Field | Value |
|---|---|
| Google Place ID | `ChIJBXJ2CL6HXjkRyDeaS15eANI` |
| CID (decimal) | `15132198507053201352` |
| Feature ID | `0x395e87be08767205:0xd2005e5e4b9a37c8` |
| kgmid | `/g/11vjx03s0y` |
| Coordinates | `23.0367285, 72.6722494` |
| Plus code | `2MPC+MV Ahmedabad, Gujarat` |
| Review URL | `https://search.google.com/local/writereview?placeid=ChIJBXJ2CL6HXjkRyDeaS15eANI` |
| Maps place URL | `https://www.google.com/maps/place/?q=place_id:ChIJBXJ2CL6HXjkRyDeaS15eANI` |
| Embed (no API key) | `https://maps.google.com/maps?q=23.0367285,72.6722494&z=16&hl=en&output=embed` |

Verification: the place URL above resolves to this exact business; the review URL redirects to Google
sign-in with that place id in `continue=`, which is the expected behaviour for a signed-out user.

## 2. Contact

- Phone / WhatsApp: **+91 94274 51885** → `tel:+919427451885`, `wa.me/919427451885`
- Verified WhatsApp handoff: `https://api.whatsapp.com/send/?phone=919427451885&text=...` resolved to
  the real profile "Smilecraft Multispeciality Dental Clinic and Implant Center".

## 3. Address (verbatim from the listing)

```
Shop No. 214, Second Floor, Blueberry Complex (National Handloom House),
near Virat Nagar Road, beside Bhojaldham Society,
Nikol, Ahmedabad, Gujarat 380049
```
Located in: **BLUEBERRY** (the complex). Ground floor tenant: National Handloom House.

## 4. Hours — conflicting, flagged

| Source | Stated hours |
|---|---|
| Maps knowledge panel | "Opens 9 AM Mon"; closed Sundays |
| Justdial listing | Mon–Sat 10:00 AM – 8:30 PM; Sunday closed |
| Client brief | Mon–Sat 9:00 AM – 9:00 PM; Sunday closed |

Site currently publishes **Mon–Sat 9:00 AM – 9:00 PM, closed Sunday**. README flags this to confirm.

## 5. Ratings and counts

- **5.0** average · **313** reviews · **64** photos on the listing
- Review topic counts: root canal treatment **30** · painless treatment **25** ·
  wisdom tooth removal **14** · smile designing **4**
- Attributes shown: **women-owned**, **LGBTQ+ friendly**
- Owner replies to reviews exist and are signed by the clinic ("Thank you so much for your wonderful
  review!..."). Reviewer names visible: "Vivo Y50" (1 review), "JAVNIKA PADIYA" (5), "Sandip Kalasva" (2).

## 6. Verbatim review excerpts used

1. "If you want high-quality dental care with zero pain, this is the place to go!"
2. "Doctor has given perfect explanation and treatment advice."
3. "Had my wisdom tooth extracted here and the entire experience was flawless. The doctors are
   incredibly skilled, professional, and made sure I felt absolutely no pain during the procedure.
   The surgery was done much faster than I expected. Highly recommend this clinic for any dental
   treatments!"
4. "I recently visited Smilecraft Multispeciality Dental Clinic in Nikol for a professional teeth
   whitening procedure, and I am absolutely thrilled with the results! The clinic is exceptionally
   clean, modern, and maintains top-notch hygiene…"
5. "From the moment I walked in, the staff was warm, welcoming, and incredibly professional."

A review also names the dentist: "I have consult **Dr Priya Patel** for root canal treatment and cap
on the same. She has explained all the…"

## 7. Services named on the listing

General dentistry · dental implants · cosmetic treatments · root canals · orthodontics ·
teeth whitening · smile makeovers · wisdom tooth removal · crowns/caps · oral care.
Google's own description: "a modern, patient-focused dental clinic … dedicated to delivering
high-quality, painless, and ethical dental care."

## 8. ABSENT — do not invent

- **No prices anywhere.** No consultation fee, no treatment fee, no range.
- **No qualifications** (no BDS/MDS), **no Dental Council registration number**.
- **No founding year**, no "since 20xx", no patient-count claims.
- **No insurance/TPA tie-ups**, no EMI partners named.
- **No awards, seals, certifications or third-party badges.**
- No doctor portrait — only gloved hands and patients are photographed.

## 9. Site copy locked (approved wording)

- Hero: "A calmer kind of dentist visit."
- Manifesto: "We would rather save your tooth than sell you an implant."
- Three promises: Written before we start · Single-use, always · Nothing on commission
- Process: Book in about a minute → We look, properly → You get a plan, in writing →
  Treatment, at your pace → Review, then aftercare
- Booking: "Book a visit — it takes about a minute."
- CTA: "Two minutes on WhatsApp is usually all it takes."

## 10. Asset inventory on disk

Images (11): `smile-portrait`, `smile-macro`, `smile-woman`, `gen-doctor`, `gen-implant`,
`gen-instruments`, `gen-reception`, `gen-operatory`, `aligner-vs-braces`, `waiting-room`,
`xray-review`.

Video (2): `clinic-tour.mp4` (10.4 s, ~1.0 MB), `clinic-walkthrough.mp4` (10.6 s, 818 KB).

All photography is placeholder — see README §5 for the swap table.

## 11. Build state

- v1 editorial ivory/teal — rejected by client
- v2 serif + mono editorial — rejected
- v3 Apple-style minimal — rejected
- **v4 Bright Clinical (white + teal #0E9AA7, Plus Jakarta Sans + Inter)** — current, verified
  structurally (16 pages, zero broken links/assets) but **not yet visually reviewed**.
