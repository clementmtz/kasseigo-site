# kasseigo-site — kasseigo.com

The public website of KasseiGo, published by GitHub Pages at https://kasseigo.com (domain at OVH,
managed by the owner). Workspace-wide rules are in `../CLAUDE.md`: read it too.

## How it works

The repository holds **sources only**. On every push to `main`, `.github/workflows/pages.yml`
generates the pages and publishes them. Generated files are git-ignored: never commit them, never
copy files here from another repository.

| Source | Becomes |
|---|---|
| `src/templates/<page>.html` + `src/i18n/<lang>/<page>.json`, filled by `src/build.py` | `/<page>.html` in English, `/<lang>/<page>.html` in the other languages (`index`: `/`, `/fr/`, `/nl/`), and `sitemap.xml` |
| `src/og.html` | `img/og.jpg`, the 1200×630 sharing image (rendered by hand) |
| `404.html`, `img/`, `favicon.ico`, `robots.txt`, `CNAME` | published as they are |

How `src/build.py` works (details at the top of the script):

- A page exists in a language when `src/i18n/<lang>/<page>.json` exists; English is required. The
  legal pages exist in French and English only (no Dutch version on purpose); a link to a page
  missing in a language goes to the English one.
- `{{key}}`: dotted path into the page's dictionary; `{{site.key}}`: into `src/i18n/<lang>/site.json`
  (texts shared by several pages). Values are HTML; keys starting with `_` are comments.
- `{{> part}}` inserts `src/templates/_part.html` (`_head.html`: head of every page, with the
  canonical and hreflang links and the `?lang=` redirect; `_legal_*.html`: shared by the legal pages).
- Filled in by the script: `{{lang}}`, `{{url}}`, `{{href.<page>}}` (link to a page in the current
  language), `{{here.<page>}}`, `{{lang_links}}` (language menu), `{{lang_paths}}`, `{{alternates}}`.
- Every template, parts included, starts with a guard block (`noindex`) that the build removes.
- The build stops on a key missing in a language, a dictionary key nothing uses, or a template
  without its guard: never skip the error, fix the dictionary or the template.

## Changing the site

- Texts: `src/i18n/<lang>/<page>.json`, in every language of the page. A new text is a new `{{key}}`
  in the template and the same key in each dictionary of that page. Layout, styles and scripts: the
  template.
- "Join the iPhone beta" buttons (`data-beta`) open the TestFlight steps (`<dialog id="join">` in
  `src/templates/index.html`, texts `beta.*`); the invitation link is in the template, and the buttons
  lead to it straight without JavaScript.
- Home page: the `mock` and `demo` keys are the app's own words: keep them in sync with
  `kasseigo/app/lib/l10n/app_*.arb`. The `demo` keys are patterns (`{n}`, `{km}`, `{m}`…) filled by
  the page's script: the surface and no-ride zone selectors recompute a trip (drawn at random, with
  the app's loading shimmer) and the guidance card plays "Nearest parking". The selector, loader and
  guidance styles copy the app (`seg_control.dart`, `Skeleton`, `nav.dart`).
- Legal pages (`legal`, `terms`, `privacy`): French is the legal reference; change
  `src/i18n/fr/<page>.json` first, then the English one, and the `updated` date of both. Keys follow
  the sections (`s3.p1`: section 3, first paragraph); a sentence identical in both languages is
  written in the template. They must match the app: no online search (Photon was removed), no
  account, no analytics; the network is used for operator feeds, city packs and map tiles.
- Feedback form (`src/templates/feedback.html`): posts to the Cloudflare Worker in
  `kasseigo/backend/feedback` (Turnstile site key there, secret on Cloudflare). Only
  `https://kasseigo.com` is accepted. Messages shown by its script come from `data-` attributes of
  the form. `?type=bug|idea|data|other` picks the type (links of the home page's feedback section).
- The app links to `/terms.html`, `/privacy.html`, `/legal.html` with `?lang=fr` or `?lang=en`, and
  to `/feedback.html?lang=…&app=…&os=…`: never rename them. The script in `_head.html` sends these
  links to the page in that language (`/fr/privacy.html`), keeping the other parameters.

## Check before pushing

```sh
python3 src/build.py
python3 -m http.server 8000      # http://localhost:8000 — check /, /fr/, /nl/, the legal pages and the form
```

Pushing publishes to the public site: ask the owner first unless they asked for the change. After
the push, check that the `Site` workflow succeeded (`gh run list -R clementmtz/kasseigo-site -L 1`) and
that the pages answer (`curl -sI https://kasseigo.com/fr/`).
