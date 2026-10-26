# kasseigo.com

Website of KasseiGo, published by GitHub Pages (domain at OVH). Every push to `main` generates the
pages and publishes them (`.github/workflows/pages.yml`): nothing generated is committed, nothing is
copied by hand.

| File | What it is |
|---|---|
| `index.html` | Home page in English: the source of the French and Dutch ones |
| `src/build_i18n.py` | Builds `fr/` and `nl/` (Belgian Dutch) from `index.html`; stops if a translated sentence is no longer found |
| `src/build_legal.py` | Builds `legal.html`, `terms.html`, `privacy.html` (French is the reference text, English below it) |
| `src/og.html` | Source of `img/og.jpg`, the 1200×630 sharing image |
| `feedback.html` | Feedback form, posting to the Cloudflare Worker of `kasseigo/backend/feedback` |
| `img/`, `favicon.ico`, `404.html`, `robots.txt`, `sitemap.xml`, `CNAME` | Published as they are |

Preview locally:

```sh
python3 src/build_i18n.py && python3 src/build_legal.py
python3 -m http.server 8000      # http://localhost:8000
```

To change a page: edit `index.html` (and its translations in `src/build_i18n.py`) or the legal texts in
`src/build_legal.py`, then push.
