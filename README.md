# Smilecraft Dental — website

A complete front-end website for **Smilecraft Multispeciality Dental Clinic & Implant Center**,
Shop 214, Second Floor, Blueberry Complex (National Handloom House), near Virat Nagar Road,
beside Bhojaldham Society, Nikol, Ahmedabad 380049 · +91 94274 51885.

Plain HTML, CSS and JavaScript. No framework, no build step, no database, no backend.
Deploys to Vercel as static files and works on any static host.

---

## 1. Deploy to Vercel

**Drag and drop (about 30 seconds)**

1. Go to <https://vercel.com/new>
2. Drag this whole folder onto the page.
3. Framework preset: **Other**. Build command: *empty*. Output directory: *empty*.
4. Deploy. You get a `*.vercel.app` address immediately.

**From Git (recommended once you start editing)**

1. Push this folder to a GitHub repository.
2. Vercel → **Add New → Project → Import** the repository.
3. Framework preset **Other**, no build command, no output directory.
4. Every push after that redeploys automatically.

**Custom domain** — Vercel → Project → **Settings → Domains → Add**, then point your DNS at Vercel.
After the domain works, update it in one place: `_build/chrome.py` → `SITE["url"]`, then run
`python _build/build.py`. (Or find-and-replace `https://smilecraftdental.in` across the `.html`
files — it appears only in canonical tags, Open Graph tags and the sitemap.)

`vercel.json` is included: long-lived caching for `/assets`, and basic security headers.
`404.html` is picked up automatically.

---

## 2. What is in the folder

```
index.html                        Home
treatments.html                   All eight treatments
treatments/dental-implants.html
treatments/root-canal.html
treatments/braces-aligners.html
treatments/smile-design.html
about.html                        The clinic, sterilisation, Dr Priya Patel
reviews.html                      313 Google reviews + "leave a review"
gallery.html                      Photo gallery with lightbox
book.html                         3-step appointment request → WhatsApp
contact.html                      Address, hours, map, enquiry form
first-visit.html                  What happens at the first appointment
faq.html                          Appointments, cost, treatment, getting here
privacy.html                      What the website collects, in plain language
thank-you.html                    404.html
assets/css/site.css               The entire design system, one file
assets/js/site.js                 Navigation, hours status, gallery, FAQ, sliders
assets/js/lead.js                 Every form: validation, WhatsApp handoff, drafts
assets/img/                       Photography + map + favicon
assets/video/                     Two short clinic loops
_build/                           Optional generators (see §10)
vercel.json  robots.txt  sitemap.xml
```

Every page is a standalone file. You can edit any `.html` in VS Code or Notepad — nothing compiles.

---

## 3. How the booking / enquiry system works

There is no server, so nothing is "stored" anywhere. Instead the form builds a complete
WhatsApp message and hands it to WhatsApp:

1. Visitor fills name, mobile, optional email, treatment, preferred date/time, notes.
2. It validates in the browser (Indian mobile format, email format, consent).
3. Step 3 shows the **exact message** that will be sent.
4. Pressing **Send on WhatsApp** opens `wa.me` with everything pre-written.
5. The visitor presses send inside WhatsApp. It arrives on **+91 94274 51885**.
6. The page then shows a confirmation with a "copy the message" fallback in case WhatsApp
   did not open.

Every message ends with the channel the visitor came from:

```
Source: google / instagram / direct · /book.html
Sent: 22 Nov 2026, 07:42 pm IST
```

That is how you learn whether Google, Instagram or a WhatsApp forward is producing enquiries.

**To change the receiving number**, edit two places:

- `assets/js/lead.js` → `WA_NUMBER: "919427451885"`
- `_build/chrome.py` → `"wa": "919427451885"` and `"phone_tel"`, then rebuild — or find/replace
  `wa.me/919427451885` and `tel:+919427451885` across the `.html` files.

Format: country code + number, digits only, no `+`, no spaces.

**Where visitors can convert**

| Place | What it captures |
|---|---|
| `book.html` | 3-step wizard: name, mobile, email, patient type, treatment, date, time, notes, consent |
| `contact.html` | Question form: name, mobile, email, message, consent |
| Every page (floating card) | Callback request — name + mobile. Appears once per 12 hours, after 58% scroll or on exit intent, dismissible, never on the booking page |
| Every page | Call / WhatsApp / Book bar on mobile; WhatsApp button on desktop |

---

## 4. Optional: also receive enquiries by email (free, 2 minutes)

By default the enquiry only goes to WhatsApp. If you also want it in an inbox:

1. Go to <https://web3forms.com>, enter your email, and copy the access key.
2. Open `assets/js/lead.js` and paste it here:
   ```js
   WEB3FORMS_KEY: "your-key-here",
   ```
3. Redeploy. From then on every form submission is posted to Web3Forms *and* handed to
   WhatsApp. Leave the key empty and nothing is posted anywhere.

That is the only "backend" option built in. It is off by default on purpose: no key, no
third-party data processor, nothing to explain to a patient.

---

## 5. Google reviews

The "Leave a review" buttons open:

```
https://search.google.com/local/writereview?placeid=ChIJBXJ2CL6HXjkRyDeaS15eANI
```

The place ID was recorded during the research for this build. **Click it once before you go
live** and confirm it lands on your own listing — if the Google Business Profile is ever
recreated, the ID changes and this link must be updated in `_build/chrome.py` (`SITE["review"]`)
and rebuilt.

To find the link again: Google Maps → your business → Share → review link, or Google's
"Place ID Finder".

---

## 6. Replace the photographs ⚠️

**This is the most important thing to do before launch.** The images are a licensed placeholder
set. They are not photographs of Blueberry Complex, and the gallery page says so in a note.
Real photographs of your own rooms and your own patients will do more for trust than any redesign.

Keep the same file names and roughly the same dimensions:

| File | Where it appears | What to shoot |
|---|---|---|
| `smile-portrait.jpg` | Review card, reviews page | A patient smiling, with written permission |
| `gen-reception.jpg` | Home tour, gallery, about | Your reception desk and seating |
| `gen-operatory.jpg` | Home hero, gallery | Your chair, light and unit — landscape |
| `gen-doctor.jpg` | Home, about, gallery | Dr Priya at work (mask on is fine) |
| `gen-instruments.jpg` | Treatments, gallery | Sterilised instruments on a tray |
| `gen-implant.jpg` | Implants page, home | An implant model or your planning screen |
| `aligner-vs-braces.jpg` | Braces page, home, gallery | Aligner tray and braces model |
| `smile-macro.jpg` | Smile design, home | Close-up of anterior work |
| `smile-woman.jpg` | Whitening, home | A whitening result, with permission |
| `waiting-room.jpg` | Home, gallery | The waiting area |
| `xray-review.jpg` | Root canal, home | Reviewing an X-ray |

Shoot on a phone in daylight, landscape, no flash. Keep them under ~1500 px wide and save as JPEG
around quality 80, then overwrite the files with the **same names**. Nothing else needs changing.

**Do not** put a stock photo of a different person in the "Dr Priya Patel" section, and do not
use another clinic's before-and-after photographs. Both mislead patients.

---

## 7. Video

`assets/video/clinic-tour.mp4` plays muted and looping in the "See the room before you sit in it"
section, with a pause button. To use real footage, export MP4 (H.264, 1280×720 or 1920×1080, no
audio needed), keep the filename, keep it under ~5 MB. If it fails to load, the poster image
stays visible and nothing breaks.

---

## 8. Lessons from the previous build (why this one is different)

Earlier versions of this site stacked several competing theme stylesheets, and the rendered home
page lost its `<h1>` and broke the rating row. This build has **one** stylesheet, one JS file for
the shell and one for forms, and every page was rendered and inspected at 1440 px and 390 px
before delivery.

Design decisions worth knowing:

- **Type** — the iOS system stack (`-apple-system`, `SF Pro Display/Text`) so it renders natively on
  iPhone, iPad and Mac, with Inter loaded from Google Fonts as the fallback on Windows and Android.
  Weights 400/500/600 only.
- **Colour** — `#0071E3` accent, `#1D1D1F` label, `#6E6E73` secondary, `#F5F5F7` grouped surface,
  `#1D1D1F` graphite panels, hairline separators at `rgba(60,60,67,.10)`.
- **Layout** — 1180 px shell, 68 px centred hero headline at desktop, 18/22/28 px radii, pill buttons
  (980 px), grouped inset cards, segmented controls, iOS tab bar under 900 px.
- **Motion** — reveal on scroll, counters, FAQ accordion, carousel, lightbox, sticky header that
  hides on scroll down. Everything is disabled under `prefers-reduced-motion`, and a `.js` class
  guard keeps all content visible if the script never runs.
- **Accessibility** — semantic landmarks, one `<h1>` per page, alt text on every image, visible
  focus rings, 44 px tap targets, keyboard-operable tabs, accordion, slider and lightbox.

---

## 9. Facts used, and the things you must confirm

Every claim on the site comes from your brief or from the Google listing. **Nothing was invented.**

- Address, phone, hours: from your brief. Hours vary between sources (9–9 vs 10:00–8:30) — the
  site publishes **Mon–Sat 9:00 AM – 9:00 PM, closed Sunday** and adds "call before travelling
  from far". Fix it here if that is wrong: `_build/chrome.py` → `SITE`, plus the hours tables in
  `index.html`, `contact.html`, `book.html` and the JSON-LD.
- 5.0 rating and 313 reviews: from the Google listing at the time of the research.
- Review quotes: verbatim from Google, attributed as "Google review · Nikol". Names are shortened
  to first name + initial, or shown as "Verified patient".
- Dr Priya Patel is named in a Google review. **No qualifications or registration numbers are
  invented** — the page says they are available at reception. Add them when you are ready.
- No prices anywhere, deliberately. The FAQ explains what drives cost instead. Inventing a price
  list would be worse than omitting one.
- No founding year, no patient-count claims, no awards, no insurance partners.

Before launch, confirm: the domain in the canonical tags, the review link, the exact hours, and
Dr Priya's qualifications wording on `about.html`.

---

## 10. Rebuilding the HTML (optional)

The pages were generated from `_build/` so that the header, footer and floating widgets stay
identical across 16 pages. **You do not need this to edit text** — edit the `.html` files directly.

If you would rather change something site-wide:

```powershell
python _build\build.py     # rebuilds all pages + sitemap from _build/*.py
python _build\check.py     # link / asset / SEO check, prints errors
python _build\make_map.py  # re-renders assets/img/map-nikol.jpg from OpenStreetMap tiles
```

Python 3 only. `make_map.py` needs Pillow and an internet connection; the other two need nothing.
The map image uses OpenStreetMap data (© OpenStreetMap contributors, ODbL) and the attribution is
baked into the image.

---

## 11. What is not included

- **No backend, CRM or database.** Enquiries arrive on WhatsApp (and optionally email). If you want
  a real booking calendar with automatic reminders, the natural next step is a Vercel serverless
  function plus a scheduling service — the forms are already structured for it.
- **No analytics.** Nothing is tracked out of the box, and the privacy page says so. If you add
  Vercel Analytics or GA4, update `privacy.html` first — the current wording would become untrue.
- **No cookie banner**, because there are no cookies to consent to.
- **No online payments.**

---

## 12. What was checked before delivery

- 16 pages built; `python _build/check.py` reports **0 broken links, 0 missing assets, 0 duplicate
  ids, 0 missing alt text**, one `<h1>` and one canonical per page.
- Every page rendered in headless Chrome at 1440 px and spot-checked at 390 px.
- The form logic was executed in a browser: empty submit blocked, bad phone blocked, valid submit
  produced `https://wa.me/919427451885?text=…` with the name included and showed the confirmation
  panel, with no JS errors.
- Opening-hours status was checked against Asia/Kolkata time (it correctly read "Closed Sunday ·
  opens Monday 9:00 AM" on a Sunday).

## 13. Motion, video and ambience (upgrade pass)

**Video is generated locally, not embedded.** All clips are made with ffmpeg from the clinic
photography, so they load from your own domain, work offline and add no third-party player:

| File | Size | Use |
|---|---|---|
| `assets/video/hero-loop.mp4` | 1600×900, 13.6 s, 1.6 MB | Home hero backdrop, muted loop |
| `assets/video/clinic-film.mp4` | 1280×720, 13.9 s, 0.91 MB | Home film stage, About |
| `assets/video/clinic-tour.mp4` | 1280×720, 10.4 s | Gallery stage, home tile |
| `assets/video/clinic-walkthrough.mp4` | 1280×720, 10.6 s | Home tile |
| `assets/img/hero-poster.jpg` | 1600×900, 94 KB | Poster frame, first paint |

Rebuild them with the filter scripts (ffmpeg 9 renamed the flag to `-/filter_complex`):

```powershell
ffmpeg -y -i assets\img\gen-reception.jpg -i assets\img\gen-operatory.jpg `
  -i assets\img\waiting-room.jpg -i assets\img\gen-instruments.jpg `
  -/filter_complex _build\hero.filter -map "[out]" -c:v libx264 -crf 26 `
  -pix_fmt yuv420p -movflags +faststart -an assets\video\hero-loop.mp4
```

**Motion layer — `assets/js/motion.js`.** Masked word reveal on the hero headline, clip-path
image reveals, parallax on the hero film, a magnetic primary button, a 3° card tilt, video that
only plays while on screen, a white veil between pages, and a section-index observer. Everything
returns early under `prefers-reduced-motion`; if the file fails to load, the site is complete.

**Ambience beside the column.** A fixed four-stop radial mesh (blue/white, very low opacity) plus
a 3.5 % SVG grain across the viewport, and two vertical margin labels — “Nikol · Ahmedabad 380049”
and “Blueberry Complex · 2nd floor” — that appear only above 1420 px so they never crowd the text.

**Performance notes.** Embeds are muted, looped, `playsinline`, and paused off-screen. The two
film tiles use `preload="none"`, so nothing heavy downloads until pressed. The hero film is 1.6 MB
and has a poster, so the first paint is a still.

## 14. Upgrade pass: density, icons, boxes, effects

**Icon sprite.** One inline `<symbol>` sheet per page (42 icons, 1.6 px stroke), referenced with
`<use href="#i-name">`. `icon("name")` in `_build/chrome.py` emits the reference, and
`_build/verify.py` fails if any page points at an icon that is not in the sprite.

**Density.** Section padding, card padding, grid gaps and header height were reduced theme-wide
(`--pad-y` is now `clamp(2.6rem, 2rem + 3vw, 4.5rem)`), so pages read tighter without shrinking type.

**Bento.** The home stat strip became an eight-tile bento: rating, 8 treatments, 9–9 hours, map
(2×2), written plan, single-use, same-day, call.

**Header.** Live status pill on desktop, 2 px sliding underline on nav links, 44 px condensed state
after 24 px of scroll.

**Footer.** New graphite panel: CTA row, four columns (last one with pin/phone/clock icons), a
stroked "Smilecraft" wordmark, and a back-to-top link.

**Effects.** Pointer-follow spotlight on cards, magnetic primary button, 3° tilt, masked word reveal,
clip-path image reveals, parallax, marquee, desktop section-dot index, sticky book pill after 620 px,
page veil. All of it exits early under `prefers-reduced-motion`.

**Checks.** `python _build/check.py` → 0 errors; `python _build/verify.py` → 0 errors across 16 pages.

## 15. Responsive pass (measured, not guessed)

Audited at **320, 360, 390, 480, 620, 768, 900, 1024, 1280, 1440 and 1920 px**, across eight page
types (home, book, treatments, contact, gallery, reviews, faq, first visit).
`documentElement.scrollWidth` equals the viewport at every one — **no horizontal scroll anywhere**.
The only "overflow" the probe reports is the marquee track and the photo rail, both intentionally
inside `overflow: hidden` / `overflow-x: auto`.

**Breakpoints** — 1600 (wider shell) · 1420 (margin labels, section dots) · 1100 (nav becomes a
drawer) · 900 (tab bar appears, splits go single column) · 700–1024 (three columns become two) ·
620 (type scale drops) · 560 (treatment rows stack their description) · 420 (one-column bento and
footer) · 380 (header CTA steps aside for the tab bar).

**Touch** — `pointer: coarse` raises buttons to 46 px, header controls to 40 px, footer links to
40 px, chips to 44 px, and `hover: none` removes sticky hover lifts and the pointer spotlight.

**Safe areas** — shell padding uses `env(safe-area-inset-left/right)`; the tab bar and lead sheet
use the bottom inset, so nothing sits under the home indicator.

**Short landscape** — under 540 px tall the hero loses its lead paragraph and tightens padding, so
the film is still visible above the fold.

**Anchors** — `scroll-margin-top: 78px` keeps section headings clear of the sticky header.

## 16. Home recomposition (v6)

The home page was rebuilt rather than patched, because the old version repeated itself: the map appeared
twice, six photos appeared in both the treatment grid and a photo rail, and reviews occupied a full band
plus a carousel.

Now: asymmetric hero with a 4:5 film and two floating glass chips (rating, live status) · five-tile bento
(no map) · symptom picker · six treatment tiles (each image used once) · one dark section carrying the
manifesto, three promises and the three-step process · dentist split with the clinic film inline ·
compressed review band (3 quotes, one row) · a single map in the visit block · two-column FAQ · CTA · footer.

Header is now a floating glass dock (`header_v2`): one rounded bar with the brand, nav, live status,
call icon and Book pill, condensing on scroll. The old two-tier topbar is gone.

Nine sections instead of twelve; no image repeats on the page; the map appears once.

## 17. Section rebuilds (v7)

**01 Start here → triage sheet.** The tab strip plus wide panel became a two-column selector: six
iOS-style rows on the left (icon, label, one-line symptom, chevron) and a single answer panel on the
right with a large ghost numeral, a headline, three chips and two actions. Rows tint blue when active;
below 900 px the list collapses to two columns, below 620 px to one.

**04 The dentist → profile card.** Instead of an image + definition list + inline video, the section is
now a 5:6 portrait with a "single-use" caption chip, the name, a pull quote set at 21 px with a quote
mark, three credential cells in one row (Focus / Languages / Registration) and two actions. The clinic
film was removed here — it already runs in the hero — so the page no longer plays two videos.

**05 Finding us → animated map.** The static map link now carries motion: a 30 s drift, a sonar ring
that expands from the clinic pin, a pulsing halo, a bobbing "Shop 214" label, two glass chips
("Virat Nagar Road", "Beside Bhojaldham Society") and a Directions button. All animation stops under
`prefers-reduced-motion`.

## 18. Portrait fix, smaller hero film, micro-interactions (v8)

**Empty left column, diagnosed.** The dentist portrait carried `.reveal-img`, whose hidden state is
`clip-path: inset(0 0 100% 0)` — when the observer did not fire, the figure was clipped to nothing while
the right column stayed visible. The class was removed from that figure, the image is now `loading="eager"`
with `object-position: 50% 32%`, the panel keeps a soft gradient behind it, and a "Consultation room"
badge sits top-left. As a belt-and-braces measure, `motion.js` now force-adds `is-in` to any remaining
`.reveal-img` after 1.4 s, so no photograph can ever stay clipped.

**Hero film, smaller.** The collage is capped at 430 px and the film is 1:1 instead of 4:5 (4:3 below
900 px), and the headline steps down a little to keep the fold balanced.

**Micro-interactions added.** Sheen sweep on every button · growing rule after each section mark ·
icons rotate on card hover · gradient scrim + arrow slide on treatment tiles · triage chevron slides
and tints · chips stagger in when a triage answer appears · quote mark floats · FAQ rows tint and
their plus turns blue · hours and visit rows tint, visit rows indent · map chips lift on hover ·
chips lift · footer links get a sliding underline · dock call icon rotates · the sticky book pill
breathes · treatment tiles and bento boxes take a 2–3° pointer tilt (replacing the earlier 3° tilt).

All of it is disabled under `prefers-reduced-motion`.
