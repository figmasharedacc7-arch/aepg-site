# AEPG Website

Static site for Aiman El-Ramly Promotional Group (AEPG), strategic growth advisory.

Two parallel builds live here:

- **Main build** (root of this repo, port 8765): hand-built HTML with inline/shared CSS, editorial typography, and the upgraded content flow (proof bar, case studies, Notes from Aiman, Discovery-first CTA).
- **`aepg-site-exact/`** (separate folder, port 8766): a byte-level clone of the live Framer build with trackers stripped and images self-hosted.

## Pages

- `index.html` — homepage with hero, proof bar, portfolio, services, testimonial, notes preview, Discovery CTA
- `how-we-create-value.html` — four practice pillars
- `growth-programs.html` — five AEPG programs
- `case-studies.html` — three featured cases (ZEMA Global Data, ZE Power Engineering, OmniGTM.ai)
- `founder.html` — Aiman bio, credentials, historical contributions, reels
- `resources.html` — Notes from Aiman (signed essays + subscribe)
- `contact.html` — Book a Discovery Intensive

## Local preview

```bash
python3 serve.py
# open http://localhost:8765
```

`serve.py` serves the current directory on port 8765 with pretty URLs (`/contact` → `/contact.html`).

## Assets

- `assets/css/site.css` — shared stylesheet
- `assets/img/` — all images self-hosted (69 files, originally sourced from Framer CDN)

Fonts are loaded from Google Fonts (Fraunces for display, Inter for body).

## Deployment

Any static host works (GitHub Pages, Vercel, Netlify, Cloudflare Pages). No build step.

For GitHub Pages: enable Pages in repo settings, point at `main` branch, root folder.
