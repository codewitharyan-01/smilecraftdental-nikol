# V3 visual record — Apple-inspired build (current state)

Captured from a rendered screenshot of `index.html` at ~473 px (mobile). This is the current
design; the earlier editorial/serif build is superseded.

## What is on screen (mobile)

- **Header:** white, no border until scrolled. Tooth mark + "Smilecraft" wordmark (bold, SF-style,
  ~19 px, tight tracking). Right side: hamburger only — nav links and the "Book a visit" pill are
  hidden below 1060 px by design.
- **Eyebrow:** small blue (#0071E3) line with a leading dot —
  "Multispeciality dental clinic & implant centre".
- **H1:** "A calmer kind / of dentist visit." — two centred lines, ~44 px, weight 600,
  letter-spacing ≈ −0.021em. First line black (#1D1D1F); "dentist visit" in blue.
- **Sub:** two centred lines, grey #6E6E73, ~18 px.
- **CTAs:** solid blue pill "Book an appointment" (radius fully rounded) beside blue text link
  "Message on WhatsApp ›".
- **Badges:** three #F5F5F7 pills — "★★★★★ 5.0 · 313 reviews", "📍 Nikol, Ahmedabad",
  "🕐 Mon–Sat, 9 to 9". They wrap to two rows on mobile (2 + 1).
- **Hero media:** large-radius (~36 px) rounded image of a smiling woman, 16:10, bleeding to the
  container edges, cropped by the fold.
- **iOS tab bar (fixed):** frosted white with a hairline top border — Call (handset icon) ·
  WhatsApp (speech icon) · Book (calendar icon, blue = primary). Labels ~10 px grey, Book in blue.
- **WhatsApp float:** green circular button, right side, sitting above the tab bar and overlapping
  the hero image edge.

## Palette in use
White #FFFFFF · alt grey #F5F5F7 · text #1D1D1F · secondary #6E6E73 · blue #0071E3 ·
line #D2D2D7 / #E8E8ED · tab-bar grey #8E8E93 · iOS green #25D366

## Type in use
`-apple-system, BlinkMacSystemFont, "SF Pro Text", Inter, "Segoe UI", Roboto, sans-serif`
Inter is loaded from Google Fonts so non-Apple devices still get a near-SF look. No serif, no mono.

## Radii in use
8 / 12 / 18 / 28 / 36 px and a 980 px pill. Everything is rounded; nothing is square.

## Content confirmed present on the page
Hero · stat bar (5.0 / 313 / 30 / 9–9) · showcase tiles (implants, smile design) · three pillars
(written before we start, single-use always, we save the tooth first) · 8-row treatments list ·
two feature splits (implants, root canal) · 5-step process · Dr Priya Patel with cred rows ·
clinic tour video · reviews carousel (5 quotes) · visit card + map · dark CTA band.

## Known cosmetic notes
- Hero badges wrap 2 + 1 on narrow screens — intentional, but could be tightened to 3 + 0 by
  shortening the labels.
- WhatsApp float overlaps the hero image's right edge on mobile; does not obscure text.
- Desktop header shows the six nav links plus the blue "Book a visit" pill; mobile relies on the
  drawer and the tab bar.
