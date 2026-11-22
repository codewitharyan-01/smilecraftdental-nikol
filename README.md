# Smilecraft Dental — website

A complete, front-end-only website for **Smilecraft Multispeciality Dental Clinic & Implant Center**,
Shop 214, Second Floor, Blueberry Complex, Nikol, Ahmedabad 380049.

Plain HTML, CSS and JavaScript. No build step, no framework, no backend, no database.
It deploys to Vercel as static files and works from any static host (Netlify, Cloudflare Pages,
Hostinger, GitHub Pages).

---

## 1. Deploy it (Vercel)

### Option A — drag and drop (fastest)
1. Go to <https://vercel.com/new>.
2. Drag this whole folder onto the page.
3. Framework preset: **Other**. Build command: leave empty. Output directory: leave empty.
4. Deploy. You get a `*.vercel.app` URL in about 20 seconds.

### Option B — from Git
1. Push this folder to a GitHub repository.
2. In Vercel: **Add New → Project → Import** the repo.
3. Framework preset **Other**, no build command, no output directory.
4. Deploy. Every push redeploys.

### Custom domain
Vercel → Project → **Settings → Domains → Add**. Point the domain's DNS at Vercel as instructed.
Then update the domain inside the site (see §7).

`vercel.json` is already included: it sets long-lived caching for `/assets` and basic security
headers. `404.html` is picked up automatically.

---

## 2. What is in here

```
index.html                     Home
treatments.html                All treatments, grouped
treatments/dental-implants.html
treatments/root-canal.html
treatments/braces-aligners.html
treatments/smile-design.html
about.html                     The clinic, sterilisation, Dr Priya Patel
reviews.html                   Google reviews + "leave a review" flow
gallery.html                   Photo gallery with lightbox
book.html                      Appointment enquiry → WhatsApp
contact.html                   Address, hours, map, directions
first-visit.html               What happens at the first appointment
faq.html                       Questions, including costs
privacy.html                   Privacy note
thank-you.html                 404.html
assets/css/                    main.css, pages.css
assets/js/                     site.js, booking.js
assets/img/                    Photography
assets/video/clinic-tour.mp4   Clinic tour video
robots.txt  sitemap.xml  vercel.json  favicon
```

Every page is a standalone HTML file. You can edit it in VS Code or even Notepad — there is nothing
to compile.

---

## 3. How the booking system works

There is no server, so nothing can be "stored". Instead the form builds a WhatsApp message and hands
it to WhatsApp:

1. Visitor fills in name, phone, treatment, preferred date/time and notes on `book.html`.
2. The page validates it and shows a live preview of the exact message.
3. On **Send enquiry on WhatsApp**, the browser opens `wa.me` with the whole message pre-written.
4. The visitor presses **send** in WhatsApp. It arrives on the clinic's phone: **+91 94274 51885**.
5. The page then shows a confirmation with a "Copy my details" fallback in case WhatsApp did not open.

Every enquiry message also ends with the channel the visitor first arrived from, for example:

> — Sent from the Smilecraft website (google)

That is populated from `localStorage` on first visit (UTM parameters, referrer, landing page). It is
how you find out whether Instagram, Google or a WhatsApp forward is producing the enquiries.

**To change the destination number**, edit two files:

- `assets/js/booking.js` → `var WHATSAPP = "919427451885";`
- `index.html`, `book.html` etc. → search for `wa.me/919427451885` and replace.

The number must be in international format with no `+`, no spaces: `91` + the 10-digit number.

---

## 4. Google reviews

The **Leave a Google review** buttons open this URL, which goes straight to the review form for the
clinic's actual Google listing:

```
https://search.google.com/local/writereview?placeid=ChIJBXJ2CL6HXjkRyDeaS15eANI
```

The place ID `ChIJBXJ2CL6HXjkRyDeaS15eANI` was verified against the live listing. Do not change it
unless the Google Business Profile is recreated.

To find this link again: Google Maps → your business → Share → the review link, or use the free
"Place ID Finder" tool. The linked review page is also on `reviews.html`.

---

## 5. Replace the photographs with real ones ⚠️

**This is the single most important thing to do.** Real photos of your own clinic will do more for
trust than any redesign, and they are what makes the site unmistakably yours.

The images in `assets/img/` are a placeholder set: one genuine portrait and a set of studio
photographs that illustrate the treatments. They are not photographs of Blueberry Complex, and the
gallery page says so in small print.

Swap them by keeping the same **file names and rough dimensions**:

| File | Where it appears | Suggested real photo |
|---|---|---|
| `smile-portrait.jpg` | Hero, `about.html` | A patient of yours, smiling, with permission |
| `gen-reception.jpg` | Tour video, gallery | Your reception desk and seating |
| `gen-operatory.jpg` | Tour video, gallery | Your chair, light and unit |
| `gen-doctor.jpg` | Home, RCT page, gallery | Dr Priya at work (mask on is fine) |
| `gen-instruments.jpg` | About, gallery | Sterilised instruments on a tray |
| `gen-implant.jpg` | Implants page, gallery | An implant model or your planning screen |
| `aligner-vs-braces.jpg` | Braces page, gallery | Aligner tray and braces model |
| `smile-macro.jpg` | Smile design, gallery | Close-up of anterior work |

Take them on a phone in daylight, landscape, no flash. Rename to the same filenames and overwrite.
Keep them under ~1500 px wide and save as JPEG at quality ~80, otherwise the site gets slow.

**Do not** put a stock photo of a different person in the "Dr Priya Patel" section, and do not use
another clinic's before/after photos. Both mislead patients and, for dental advertising, are a
regulatory problem.

---

## 6. Video

`assets/video/clinic-tour.mp4` is a 10-second, 1 MB silent loop built from the photography. It
plays automatically in the "See the room before you sit in it" section.

To replace it with real footage: export an MP4 (H.264, 1280×720 or 1920×1080, no audio needed),
keep the filename `clinic-tour.mp4`, and keep it under ~5 MB. If the file is missing or fails to
load, the section automatically falls back to a slow cross-fade of three stills — nothing breaks.

---

## 7. Before you go live — checklist

- [ ] **Domain.** The site currently claims `https://smilecraftdental.in` in canonical tags, Open
      Graph tags, `sitemap.xml` and the JSON-LD schema. If you use a different domain, replace it:
      in PowerShell, from this folder:
      ```powershell
      Get-ChildItem -Recurse -Include *.html,*.xml,*.txt |
        ForEach-Object { (Get-Content $_.FullName -Raw) -replace 'https://smilecraftdental\.in','https://YOURDOMAIN.com' | Set-Content $_.FullName -NoNewline }
      ```
- [ ] **Photos.** See §5.
- [ ] **Timings.** The site says Monday–Saturday, 9:00 AM – 9:00 PM, closed Sunday. Your brief said
      this, but some directories list 10:00 AM – 8:30 PM. Fix whichever is wrong — it appears on
      every page (`hours` tables) and in the schema.
- [ ] **Dr Priya Patel's credentials.** The `about.html` page lists special interests, languages and
      "registration available at reception". Add her BDS/MDS qualifications and Dental Council
      registration number when you are ready.
- [ ] **Prices.** No prices are published anywhere, deliberately — inventing them would be worse than
      omitting them. The FAQ explains what drives cost. If you want a fee table, add it to
      `treatments.html`.
- [ ] **Google Business Profile.** Add this website's URL to the profile — at the time of writing the
      listing has no website link, which is costing you visibility.
- [ ] **Analytics (optional).** Nothing is tracked out of the box. Add Vercel Analytics in the
      dashboard, or paste a GA4 snippet before `</head>` in `_build/chrome.py` and rebuild — or just
      in each HTML file. The site already pushes events (`enquiry_submitted`, `whatsapp_click`,
      `call_click`, `google_review_click`) to `window.dataLayer`.

---

## 8. About capturing visitor details

Your brief asked to capture "contact, email and other details as much as possible" from visitors.
Worth being straight about what is possible:

- **A website cannot see an email address or phone number just because someone visited.** Browsers
  and servers do not expose them. Anyone who tells you otherwise is selling lead-scraping software.
- **Collecting them covertly** — fingerprinting devices, harvesting from other apps — would breach
  India's Digital Personal Data Protection Act, 2023, and would be a serious reputational risk for a
  clinic that trades on trust.

So this site captures details the legitimate way, in four places:

1. **The enquiry form** (`book.html`) — name, phone, optional email, treatment, preferred date/time,
   free-text notes, consent. Sent to WhatsApp with the lead source attached.
2. **Every WhatsApp button** — pre-filled with a message so you know which page they tapped from.
3. **Click events** — call clicks, WhatsApp clicks, direction clicks and review clicks fire into
   `window.dataLayer` so you can see intent, not identity.
4. **Return-visit memory** — a visitor's own name and number are saved in *their* browser, so the form
   is pre-filled next time. That data never leaves their device until they send it.

If you later want a proper CRM with email follow-ups, the natural upgrade is a serverless function
(Vercel function + Resend/Postmark) that also posts to WhatsApp. The form is already structured for it.

---

## 9. Design & motion system

**Type** — Fraunces (display, optical sizing on), Instrument Sans (body), JetBrains Mono
(micro-labels, buttons, tables). The mono is what gives the site its editorial signature: every
label, eyebrow, button and table row is set in it at 10–11 px with wide tracking.

**Colour** — near-black ink `#0F1512`, warm paper `#F6F3EC`, deep teal `#0B3F35`, clay `#A9552F`.
The page alternates light and ink sections; colour is used sparingly so the type carries the layout.

**Motion** — all in `assets/js/site.js`, no libraries:

| Effect | Where | How |
|---|---|---|
| Word-by-word headline reveal | Hero H1, manifesto | `data-split` — words rise from a mask, 46 ms apart |
| Scroll reveals with stagger | Sections across the site | `data-reveal` inside `data-stagger` |
| Parallax image | Hero portrait | `data-parallax` (clamped to ±64 px) |
| Animated counters | Home stats | `data-count` |
| Sticky step sequence | Home “A visit, start to finish” | `data-process` — step highlights as you scroll |
| Horizontal scroll gallery | Home gallery | `data-hgal` — pinned section, vertical scroll drives horizontal travel |
| Cursor-follow image | Treatments list (desktop) | `data-cursor-src` per row |
| Draggable review slider | Home reviews | `data-slider`, scroll-snap + pointer drag |
| Page transition veil | Every internal link | `[data-veil]` — ink panel wipes in, then navigates |
| Header condense + hide | Site-wide | Hides on scroll down, returns on scroll up |
| Scroll progress bar | Site-wide | 2 px clay line at the top |
| Fill-sweep buttons | All buttons | Pseudo-element slides up on hover |
| Giant outlined wordmark | Footer | `-webkit-text-stroke` |

Every one of these is disabled under `prefers-reduced-motion`, there is a `<noscript>` fallback that
forces all revealed content visible, and the split-text routine is wrapped in try/catch so a failure
can never leave the headline hidden.

**Accessibility** — keyboard-operable menus, lightbox and slider; visible focus rings; alt text on
every image; 44 px minimum tap targets; semantic landmarks; reduced-motion support.

**SEO** — per-page titles and descriptions, canonical URLs, Open Graph, `Dentist` + `FAQPage` +
`BreadcrumbList` JSON-LD, sitemap and robots.

---

## 10. Rebuilding the HTML (optional)

The pages were generated from templates in `_build/` so that the header and footer stay identical
across 16 pages. You do **not** need this to edit text — edit the `.html` files directly.

If you would rather change something site-wide (the phone number, the nav, an address), edit
`_build/chrome.py` and run:

```powershell
python _build\build.py
```

Requires Python 3. Nothing else.
