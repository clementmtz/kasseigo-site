# kasseigo-site — kasseigo.com

The public website of KasseiGo, published by GitHub Pages at https://kasseigo.com (domain at OVH,
managed by the owner). Workspace-wide rules are in `../CLAUDE.md`: read it too.

## How it works

The repository holds **sources only**. On every push to `main`, `.github/workflows/pages.yml`
generates the pages and publishes them. Generated files are git-ignored: never commit them, never
copy files here from another repository.

| Source | Becomes |
|---|---|
| `index.html` (English) | `/` |
| `src/build_i18n.py` (French and Belgian Dutch replacements of `index.html`) | `fr/index.html`, `nl/index.html` |
| `src/build_legal.py` (French reference text, English below it) | `legal.html`, `terms.html`, `privacy.html` |
| `src/og.html` | `img/og.jpg`, the 1200×630 sharing image (rendered by hand) |
| `feedback.html`, `404.html`, `img/`, `favicon.ico`, `robots.txt`, `sitemap.xml`, `CNAME` | published as they are |

## Changing the site

- Home page: edit `index.html`, then the matching replacements in `src/build_i18n.py` (it stops with
  `not found` when a translated sentence no longer matches: fix the pair, never skip it). The app
  mock-ups use the app's own words: keep them in sync with `kasseigo/app/lib/l10n/app_*.arb`.
- Legal pages: edit the texts in `src/build_legal.py`. French is the legal reference; update the
  English part with it. They must match the app: no online search (Photon was removed), no account,
  no analytics; the network is used for operator feeds, city packs and map tiles.
- Feedback form (`feedback.html`): posts to the Cloudflare Worker in `kasseigo/backend/feedback`
  (Turnstile site key here, secret on Cloudflare). Only `https://kasseigo.com` is accepted.
- The app links to `/terms.html`, `/privacy.html`, `/legal.html` (with `?lang=fr` or `?lang=en`) and
  `/feedback.html`: never rename them.

## Check before pushing

```sh
python3 src/build_i18n.py && python3 src/build_legal.py
python3 -m http.server 8000      # http://localhost:8000 — check /, /fr/, /nl/ and the legal pages
```

Pushing publishes to the public site: ask the owner first unless they asked for the change. After
the push, check that the `Site` workflow succeeded (`gh run list -R clementmtz/kasseigo-site -L 1`) and
that the pages answer (`curl -sI https://kasseigo.com/fr/`).
