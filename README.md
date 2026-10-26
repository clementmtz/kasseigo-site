# kasseigo.com

Website of KasseiGo, published by GitHub Pages (domain at OVH). Every push to `main` generates the
pages and publishes them (`.github/workflows/pages.yml`): nothing generated is committed, nothing is
copied by hand.

| File | What it is |
|---|---|
| `src/templates/<page>.html` | One template per page (`index`, `legal`, `terms`, `privacy`, `feedback`): layout, styles, scripts; every text is a `{{key}}` |
| `src/templates/_<part>.html` | Parts shared by several templates, inserted with `{{> part}}` (`_head.html`: head of every page) |
| `src/i18n/<lang>/<page>.json` | Texts of a page in one language (`en`, `fr`, `nl` Belgian Dutch); `site.json`: texts shared by the pages |
| `src/build.py` | Fills each template with each dictionary, writes the pages and `sitemap.xml`; stops on a missing or unused key |
| `src/og.html` | Source of `img/og.jpg`, the 1200×630 sharing image |
| `img/`, `favicon.ico`, `404.html`, `robots.txt`, `CNAME` | Published as they are |

Addresses: English at the root (`/`, `/privacy.html`), the other languages in their folder (`/fr/`,
`/fr/privacy.html`). A page exists in a language when its dictionary does: the legal pages are in
French (the reference text) and English only.

Preview locally:

```sh
python3 src/build.py
python3 -m http.server 8000      # http://localhost:8000
```

To change a text: edit it in `src/i18n/<lang>/<page>.json`, in each language. To add one: a new
`{{key}}` in the template and the same key in each dictionary of that page. Then push.
