# Visual + behavioural QA record — v5 (current build)

Rendered in headless Chrome at 1440 × 1050 and 390 × 844, page by page, with
`prefers-reduced-motion` forced so scroll reveals do not hide content. Screenshots
were read back and each issue below was fixed and re-rendered.

## What the render confirmed

- Header: pine topbar (address left, live status centre, phone right) · bone header with
  wordmark, five nav items, Call ghost button, Book solid button · active page underlined in clay.
- Hero: eyebrow → H1 (Bricolage, second line in Instrument Serif italic) → lead → two buttons →
  hairline → trust row (5 stars, 5.0 · 313 Google reviews, hours). Right: 5:4 treatment-room
  image with an overlapping review card (5.0, stars, quote, reviewer avatar).
- Stats band: 5.0 / 313 / 8 / 9–9 over four hairline-divided cells.
- Symptom picker: six tabs, one dark-green active pill, panel with heading, paragraph, chips and
  two CTAs. Keyboard arrows switch tabs.
- Treatments: 3 × 2 photo tiles, 4:3 crops, uppercase "Read more" footer.
- Manifesto: pine section, large serif quote with the second clause in clay italic, three ruled
  columns on the right.
- Process: numbered list (clay serif numerals) — colours now inherit correctly on both bone and
  pine backgrounds.
- Doctor: 4:5 photo left with caption chip, name, lead, definition list (focus, languages, clinic,
  Google rating), honesty note about registration.
- Video: 16:9 looping clip with a pill play/pause button, second still and "about 40 minutes" card.
- Reviews: rating panel (5.0, stars, real mention counts: 30 root canal, 25 painless, 14 wisdom
  tooth, 4 smile design), horizontal rail with 5 quotes, arrow controls.
- Visit: local OSM map image (900 × 610) with marker and label, overlay card with directions,
  hours table with today's row marked by an arrow and Sunday in clay.
- FAQ accordion, pine CTA card with clay primary button, four-column footer, hairline bottom bar.
- Mobile: single-column hero, stacked buttons, 2 × 2 stats, full-width treatment cards, horizontally
  scrolling picker tabs, fixed Call / WhatsApp / Book bar, short status text in the topbar.

## Fixed during this QA pass

1. Hero portrait cropped into an extreme face close-up → replaced with the treatment-room photo
   at 5:4, `object-position: 22%` to keep the chair in frame.
2. Stars rendered as outlines → dedicated filled-star SVG.
3. Removed a stray offset hairline box behind the hero image and a redundant floating status chip.
4. Process step headings were white on bone (invisible) → `.step` colours now inherit, with
   explicit overrides inside `.section--ink` / `.section--pine`.
5. CTA card collided with the footer → `cta_band()` uses `.section--cta` with vertical padding.
6. Invented star-distribution chart (97 / 3 / 0 %) → removed, replaced with the real review-topic
   counts from the Google listing.
7. Video play/pause pill was clipped at the frame edge → moved to the top-right, dark translucent.
8. Map iframe rendered blank → replaced with a locally generated OpenStreetMap image (attribution
   baked in) that links to Google Maps.
9. Gallery mosaic had mismatched aspect ratios (items spanned 12 columns with per-item ratios) →
   uniform 3-column 4:3 grid, 9 images.
10. Treatment hub rows: over-wide title column → `44px / 0.78fr / 1.22fr / auto`.
11. Contact cards: full-width link underlines and an unstyled status line → links hug their text,
    status is a small muted line.
12. Booking page: hero split did not collapse on mobile (inline grid override) → `.split--wide-left`
    with a media query; dead left column under the form → "what to bring" / "in pain today" cards.
13. About H1 left an orphan ("off.") → explicit line breaks.
14. FAQ list was centred in a narrow column while its heading was full width → list now spans the
    shell; privacy page heading moved into the same narrow column as its body.
15. Scroll-reveal content stayed invisible without JS → hidden state now gated behind a `.js`
    class set by an inline script in `<head>`.

## Behavioural test (headless, JS executed)

| Check | Result |
|---|---|
| Empty submit | blocked |
| Invalid phone (`12345`) | blocked |
| Valid submit | `https://wa.me/919427451885?text=…` opened |
| Name present in message | yes |
| Confirmation panel shown | yes |
| JS errors during submit | none |
| `node --check` on both scripts | clean |
| `python _build/check.py` | 0 errors across 16 pages |

Opening-hours logic was checked against Asia/Kolkata on a Sunday and correctly produced
"Closed Sunday · opens Monday 9:00 AM".
