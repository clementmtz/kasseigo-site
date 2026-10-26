"""Builds every page of kasseigo.com from the templates of src/templates and their dictionaries.

Usage: python3 src/build.py   (writes the pages and sitemap.xml at the root of the site)

- Each src/templates/<page>.html is published in every language that has
  src/i18n/<lang>/<page>.json: /<page>.html in English, /<lang>/<page>.html otherwise (index.html:
  / and /<lang>/). English is required; a link to a page missing in a language goes to the English one.
- {{key}} is a dotted path into the page's dictionary, {{site.key}} into src/i18n/<lang>/site.json
  (texts shared by several pages). Values are HTML; keys starting with _ are comments.
- {{> name}} inserts src/templates/_name.html, a part shared by several templates.
- Filled in by this script: {{lang}}, {{url}}, {{href.<page>}}, {{here.<page>}} (aria-current on
  the page itself), {{lang_links}} (language menu), {{lang_paths}}, {{alternates}} (hreflang links).
- Every template starts with a guard that keeps search engines away (noindex), removed here.
The build stops on a key missing in a language, a dictionary key no template uses, or a template
without its guard, so every language always has the same content.
"""
import json, pathlib, re

SITE = pathlib.Path(__file__).parent.parent
SRC = SITE / 'src'
ORIGIN = 'https://kasseigo.com'
LANGS = ('en', 'fr', 'nl')  # English first: the root of the site and the fallback
GUARD_START, GUARD_END = '<!-- Template', '<!-- /template -->\n'
KEY = re.compile(r'\{\{([a-z0-9_.]+)\}\}')
PART = re.compile(r'\{\{> ([a-z0-9_]+)\}\}')
CURRENT = ' aria-current="page"'
errors = []


def template(name):
    path = SRC / 'templates' / f'{name}.html'
    s = path.read_text()
    if not s.startswith(GUARD_START) or GUARD_END not in s:
        errors.append(f'templates/{name}.html: the guard is missing at the top')
        return s
    s = s.split(GUARD_END, 1)[1]
    return PART.sub(lambda m: template('_' + m[1]).rstrip('\n'), s)


def flatten(d, prefix=''):
    """{'a': {'b': 'x'}} -> {'a.b': 'x'}, without the comments."""
    out = {}
    for k, v in d.items():
        if k.startswith('_'):
            continue
        if isinstance(v, dict):
            out.update(flatten(v, f'{prefix}{k}.'))
        else:
            out[prefix + k] = v
    return out


def dictionary(lang, name):
    path = SRC / 'i18n' / lang / f'{name}.json'
    return flatten(json.loads(path.read_text())) if path.exists() else None


def path(page, lang):
    folder = '/' if lang == 'en' else f'/{lang}/'
    return folder if page == 'index' else f'{folder}{page}.html'


pages = sorted(p.stem for p in (SRC / 'templates').glob('*.html') if not p.stem.startswith('_'))
langs_of = {page: [l for l in LANGS if (SRC / 'i18n' / l / f'{page}.json').exists()] for page in pages}
errors += [f'i18n/en/{page}.json is missing (English is required)' for page in pages if 'en' not in langs_of[page]]
sites = {lang: dictionary(lang, 'site') for lang in LANGS}
hreflang = {lang: sites[lang]['html_lang'] for lang in LANGS}
site_used = {lang: set() for lang in LANGS}
out = {}

for page in pages:
    tpl = template(page)
    used = set(KEY.findall(tpl))
    langs = langs_of[page]
    for lang in langs:
        texts = dictionary(lang, page)
        values = {f'site.{k}': v for k, v in sites[lang].items()}
        values.update(texts)
        values.update({
            'lang': lang,
            'url': ORIGIN + path(page, lang),
            'lang_links': ''.join(
                f'<a href="{path(page, l)}" hreflang="{hreflang[l]}" lang="{l}"{CURRENT if l == lang else ""}>{l.upper()}</a>'
                for l in langs),
            'lang_paths': json.dumps({l: path(page, l) for l in langs}),
            'alternates': '\n'.join(
                [f'<link rel="alternate" hreflang="{hreflang[l]}" href="{ORIGIN}{path(page, l)}">' for l in langs]
                + [f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}{path(page, "en")}">']),
        })
        for p in pages:
            values[f'href.{p}'] = path(p, lang if lang in langs_of[p] else 'en')
            values[f'here.{p}'] = CURRENT if p == page else ''
        site_used[lang] |= {k[len('site.'):] for k in used if k.startswith('site.')}
        errors += [f'i18n/{lang}/{page}.json: missing {k}' for k in sorted(used - values.keys())]
        errors += [f'i18n/{lang}/{page}.json: unused {k}' for k in sorted(texts.keys() - used)]
        out[path(page, lang)] = KEY.sub(lambda m: values.get(m[1], ''), tpl)
errors += [f'i18n/{lang}/site.json: unused {k}' for lang in LANGS for k in sorted(sites[lang].keys() - site_used[lang])]
if errors:
    raise SystemExit('\n'.join(dict.fromkeys(errors)))

for url, html in out.items():
    file = SITE / (url.lstrip('/') + ('index.html' if url.endswith('/') else ''))
    file.parent.mkdir(exist_ok=True)
    file.write_text(html)
(SITE / 'sitemap.xml').write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{ORIGIN}{url}</loc></url>\n' for url in out)
    + '</urlset>\n')
print('ok', ' '.join(out), 'sitemap.xml')
