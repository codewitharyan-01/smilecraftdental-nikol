# Deploying Smilecraft

Repo: **https://github.com/codewitharyan-01/smilecraftdental**

Plain static site. No framework, no build step, no dependencies. `index.html` is at the repo root.

---

## Deploy on Vercel

1. Go to **https://vercel.com/new**
2. **Import Git Repository** → pick `smilecraftdental`
   (if you see `smilecraftdental-nikol`, that's the same repo — GitHub renamed it)
3. Settings:
   - **Framework Preset:** `Other`
   - **Root Directory:** leave as `./`
   - **Build Command:** leave **empty**
   - **Output Directory:** leave **empty**
   - **Install Command:** leave **empty**
4. **Deploy**

Every later push to `main` redeploys automatically.

Do **not** drag-and-drop a ZIP — use the Git import so future pushes flow through.

---

## A bug that used to block every deploy

`vercel.json` previously contained:

```json
"source": "/(.*)\.html"
```

JSON only allows `\" \\ \/ \b \f \n \r \t \uXXXX`. `\.` is **not** a legal escape, so Vercel
rejected the whole config with "invalid JSON" before reading a single page. Fixed in commit
`fe71e1c` by deleting that redundant cache rule. `_build/build.py` was patched too, so rebuilding
cannot reintroduce it.

Validate at any time:

```powershell
python -c "import json; json.load(open('vercel.json', encoding='utf-8')); print('valid')"
```

---

## CSS architecture

Six stylesheets, loaded in this order. The last one wins.

| File | Role |
|---|---|
| `main.css` | design tokens, reset, type scale, buttons, header, footer, forms |
| `pages.css` | page components — hero, services, feature splits, prose, article, gallery, booking |
| `components.css` | upgrade layer — video band, treatment finder, info cards, urgent strip, slot grid, FAQ search |
| `animations.css` | motion — scroll progress, word reveal, parallax, comparison slider, tilt |
| `responsive.css` | first responsive pass (kept as a safety net) |
| **`site.css`** | **authoritative layout layer — mobile-first, `min-width` breakpoints only** |

`site.css` controls layout at every size. It is mobile-first: every grid starts as one column and
**adds** columns at 480 / 700 / 900 / 1180 / 1440 px. Because breakpoints only ever go upward, the
cascade cannot fight itself when you shrink the window — which is what the older desktop-first
files were doing.

Two rules in it matter more than the rest:

- `html, body { overflow-x: clip }` — `clip` stops horizontal scrolling **without** creating a
  scroll container. `hidden` would break `position: sticky` on iOS Safari.
- `min-width: 0` on every grid/flex child — without it, items refuse to shrink below their content
  and push the page wider than the screen.

---

## Editing content

Text lives directly in the `.html` files — edit and push, Vercel rebuilds.

If you prefer regenerating from templates, the generator is in `_build/`:

```powershell
python _build\build.py     # rebuild all 16 pages
python _build\check.py     # verify links, assets, placeholder leftovers
```

`_build/` also holds `FACTS.md`, the verified record of every business detail and Google identifier.
Keep it — it is the source of truth if anything gets lost.

---

## Before going live

- [ ] **Confirm the hours.** The site says Mon–Sat 9:00 AM – 9:00 PM, closed Sunday. Justdial says
      10:00 AM – 8:30 PM and Maps says it opens at 9 AM. Fix whichever is wrong.
- [ ] **Replace the photographs.** 11 images in `assets/img/` are placeholders. Keep the filenames;
      the README swap table lists where each one appears.
- [ ] **Add the domain.** The site currently claims `https://smilecraftdental.in` in canonical tags,
      Open Graph and JSON-LD. If you use a different domain, find-and-replace it.
- [ ] **Add Dr Priya Patel's qualifications** and Dental Council registration number to `about.html`.
- [ ] **Link the site from the Google Business Profile** — the listing has no website URL yet, which
      costs visibility.

---

## Known limitations

- No prices are published anywhere. This is deliberate: inventing figures would be worse than
  omitting them.
- The before/after slider uses one photograph with a CSS filter on the "before" half. It is labelled
  on the page as an illustration, not a patient result.
- The layout layer was authored by reasoning about the cascade. It has been structurally verified
  (16 pages, zero broken links) but not visually reviewed across devices.
