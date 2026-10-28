# Builds the Velocity Shop store from products.json:
#   index.html                    the store (every product rendered as HTML, so search engines and no-JS visitors see it)
#   shipping-returns/index.html   shipping, returns, condition and checkout
#   sitemap.xml                   lastmod set to today
# Run after update.py whenever the catalogue changes:  python3 _build/build.py
import html, json, os, re
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))

SITE = 'https://velocityshop.github.io/'
STORE = 'https://velocity-shop.square.site/'
UTM = 'utm_source=velocityshop.github.io&amp;utm_medium=referral&amp;utm_campaign=store'
data = json.load(open(os.path.join(ROOT, 'products.json'), encoding='utf-8'))
items = data['items']
N = len(items)
e = html.escape

CATS = [  # key, label, one-line description shown on hover
    ('tees', 'Tees', 'Tour, band, team and graphic tees, many from the 90s and Y2K.'),
    ('shirts', 'Shirts & polos', 'Polo Ralph Lauren and Lacoste piqué, oxfords and dress shirts by neck size.'),
    ('hoodies', 'Hoodies & sweaters', 'Champion, Nike and team zips, crewnecks and fine knits.'),
    ('outerwear', 'Jackets & vests', 'Ski jackets, down puffers, fleece vests and cardigans.'),
    ('bottoms', 'Jeans & pants', "Levi's, Silver and Rag & Bone denim and chinos, listed by waist and inseam."),
    ('jerseys', 'Jerseys', 'Raptors, Blue Jays and soccer kit.'),
    ('collectibles', 'Cards & collectibles', 'Pokémon TCG singles, K-pop albums and collector pieces.'),
    ('home', 'Home & tech', 'Tested VCRs, mugs, keyboards and other good finds.'),
    ('shoes', 'Shoes & socks', 'Sneakers and multipacks.'),
]
CAT_LABEL = {k: l for k, l, _ in CATS}
SIZES = [('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL and up'), ('waist', 'Jeans by waist')]


def size_group(s):
    if not s: return ''
    if '×' in s: return 'waist'
    if s in ('XXL', '3XL'): return 'XXL'
    return s if s in ('XS', 'S', 'M', 'L', 'XL') else 'other'


def money(p):
    return '$' + (str(int(p)) if float(p) == int(p) else f'{p:.2f}')


def size_label(it):
    s = it['size']
    if not s: return ''
    if '×' in s: return s + ' waist × inseam'
    return s if s.startswith('US ') else 'Size ' + s


def link(it, slot):
    return f"{e(it['link'])}?{UTM}&amp;utm_content={slot}"


def strip_text(it):
    t = money(it['price'])
    if it['size']: t += ' · ' + it['size']
    return t


def img(path, alt, w=560, h=560, lazy=True, cls=''):
    c = f' class="{cls}"' if cls else ''
    lz = ' loading="lazy"' if lazy else ''
    return f'<img{c} src="/{path}" width="{w}" height="{h}" alt="{e(alt)}"{lz} decoding="async">'


def alt_for(it):
    return it['name'] + (', ' + size_label(it) if it['size'] else '') + ', ' + money(it['price']) + ' CAD.'


NEW_TAB = '<span class="vh"> (opens on our Square store)</span>'

# ---------- hero sheet: six columns of the newest pieces ----------
hero_items = items[:34]
cols = [[] for _ in range(6)]
order = [0, 1, 2, 3, 4, 5]
k = 0
for c in range(6):
    n = 4 if c not in (2, 3, 4) else 3
    cols[c] = hero_items[k:k + n]; k += n
STRIPS = ['st-a', 'st-b', 'st-c', 'st-d']
hero_cols = []
si = 0
for c, col in enumerate(cols):
    frames = []
    for i, it in enumerate(col):
        if c in (2, 3, 4) and i == 1:
            frames.append('<div class="spacer" aria-hidden="true"></div>')
        frames.append(f'<a class="frame" href="{link(it, "hero")}" target="_blank" rel="noopener">'
                      f'{img(it["img"][0], alt_for(it), lazy=(i > 2), cls="frame-img")}'
                      f'<span class="strip {STRIPS[si % 4]}">{e(strip_text(it))}</span>{NEW_TAB}</a>')
        si += 1
    hero_cols.append(f'<div class="col col-{c + 1}">' + ''.join(frames) + '</div>')
HERO = '\n      '.join(hero_cols)

# ---------- category index ----------
count = {k: sum(1 for it in items if it['cat'] == k) for k, _, _ in CATS}
size_count = {g: sum(1 for it in items if size_group(it['size']) == g) for g, _ in SIZES}


def idx_link(kind, key, label, n, desc):
    return (f'<li><a href="#shop" data-{kind}="{key}" data-desc="{e(desc)}">{e(label)} <span class="n">{n}</span></a></li>')


clothing = ''.join(idx_link('cat', k, l, count[k], d) for k, l, d in CATS[:6] if count[k])
finds = ''.join(idx_link('cat', k, l, count[k], d) for k, l, d in CATS[6:] if count[k])
sizes = ''.join(idx_link('size', g, l, size_count[g], f'Every piece in {l if g != "waist" else "a waist and inseam size"}, newest first.') for g, l in SIZES if size_count[g])

# ---------- the shop: every piece, as frames ----------
cards = []
for i, it in enumerate(items):
    # The back photo is created by site.js on first hover, so no image is fetched for pieces nobody points at.
    back = f' data-back="/{it["img"][1]}"' if len(it['img']) > 1 else ''
    big = ' card-big' if i == 0 else ''
    hidden = ' hidden' if i >= 24 else ''
    added = date.fromisoformat(it['added'])
    cards.append(
        f'<li class="card{big}" data-cat="{it["cat"]}" data-size="{size_group(it["size"])}"{hidden}>'
        f'<a href="{link(it, "grid")}" target="_blank" rel="noopener"{back}>'
        f'<span class="pic">{img(it["img"][0], alt_for(it), lazy=(i > 3), cls="front")}</span>'
        f'<span class="strip {STRIPS[i % 4]}">{e(strip_text(it))}</span>'
        f'<span class="card-name">{e(it["name"])}</span>'
        f'<span class="card-date">Added {added.strftime("%b")} {added.day}</span>{NEW_TAB}</a></li>')
CARDS = '\n      '.join(cards)

# ---------- just added: the three most recent listing days ----------
days = []
for it in items:
    if it['added'] not in days: days.append(it['added'])
groups = []
for d in days[:3]:
    dd = date.fromisoformat(d)
    rows = [it for it in items if it['added'] == d][:8]
    li = ''.join(f'<li><a href="{link(it, "just-added")}" target="_blank" rel="noopener">'
                 f'{img(it["img"][0], "", 64, 64, cls="dot")}<span class="ja-name">{e(it["name"])}</span>'
                 f'<span class="ja-price">{money(it["price"])}</span>{NEW_TAB}</a></li>' for it in rows)
    groups.append(f'<h3>{dd.strftime("%B")} {dd.day}</h3><ul role="list">{li}</ul>')
JUST = '\n      '.join(groups)

# ---------- how it works: six moments, real pieces ----------
def pick(name_part):
    for it in items:
        if name_part.lower() in it['name'].lower(): return it
    return items[0]

MOMENTS = [
    ('It comes in', 'Every piece is picked one at a time. If it is not worth wearing again, it does not make the rail.', pick('Ski Patch')),
    ('We check it', 'Seams, zips, cuffs, collars and pits are looked over in good light before anything else.', pick('Lacoste Mens Polo')),
    ('We shoot it', 'Front, back and any wear, photographed on a plain backdrop so you see the real piece.', pick('Kendrick')),
    ('It goes up', 'Listed on our Square store with its size, a plain description and a fair price in CAD.', pick('Showtime')),
    ('You check out', 'Pay securely on Square. The piece is yours the moment the order goes through.', pick('Bichette')),
    ('It ships', 'Folded, packed and out the door within 1–2 business days, to Canada or the US.', pick("Levi")),
]
moments = []
for i, (cap, text, it) in enumerate(MOMENTS):
    moments.append(f'<li class="moment m{i + 1}"><h3>{e(cap)}</h3><p>{e(text)}</p>'
                   f'<a class="moment-pic" href="{link(it, "how-it-works")}" target="_blank" rel="noopener">{img(it["img"][0], alt_for(it), 560, 560)}{NEW_TAB}</a></li>')
MOMENTS_HTML = '\n        '.join(moments)

# ---------- structured data ----------
store_ld = {
    '@type': 'OnlineStore', '@id': SITE + '#store', 'name': 'Velocity Shop', 'alternateName': 'Velocity Shop International',
    'url': SITE, 'logo': SITE + 'img/logo.png', 'image': SITE + 'img/og.jpg',
    'description': 'Online resale shop for one-of-a-kind pre-loved clothing and finds. Every piece is checked by hand, photographed and priced in Canadian dollars. Checkout on Square.',
    'currenciesAccepted': 'CAD', 'sameAs': [STORE],
    'hasMerchantReturnPolicy': {
        '@type': 'MerchantReturnPolicy', '@id': SITE + '#returns', 'applicableCountry': ['CA', 'US'],
        'returnPolicyCategory': 'https://schema.org/MerchantReturnFiniteReturnWindow', 'merchantReturnDays': 30,
        'returnMethod': 'https://schema.org/ReturnByMail', 'url': SITE + 'shipping-returns/'},
}
products = []
for i, it in enumerate(items):
    p = {'@type': 'Product', 'name': it['name'], 'url': it['link'], 'image': [SITE + x for x in it['img']],
         'itemCondition': 'https://schema.org/UsedCondition', 'category': CAT_LABEL[it['cat']],
         'offers': {'@type': 'Offer', 'url': it['link'], 'priceCurrency': 'CAD', 'price': f"{it['price']:.2f}",
                    'availability': 'https://schema.org/InStock', 'itemCondition': 'https://schema.org/UsedCondition',
                    'hasMerchantReturnPolicy': {'@id': SITE + '#returns'}, 'seller': {'@id': SITE + '#store'}}}
    if it['size']: p['size'] = it['size']
    if it['desc']: p['description'] = it['desc']
    products.append({'@type': 'ListItem', 'position': i + 1, 'item': p})
LD_HOME = json.dumps({'@context': 'https://schema.org', '@graph': [
    store_ld,
    {'@type': 'WebSite', '@id': SITE + '#website', 'url': SITE, 'name': 'Velocity Shop', 'inLanguage': 'en-CA', 'publisher': {'@id': SITE + '#store'}},
    {'@type': 'ItemList', '@id': SITE + '#shop', 'name': 'Everything in stock at Velocity Shop', 'numberOfItems': N, 'itemListElement': products},
]}, ensure_ascii=False, indent=1).replace('</', '<\\/')
LD_POLICY = json.dumps({'@context': 'https://schema.org', '@graph': [
    store_ld,
    {'@type': 'WebPage', 'url': SITE + 'shipping-returns/', 'name': 'Shipping, returns and condition | Velocity Shop',
     'isPartOf': {'@id': SITE + '#website'},
     'breadcrumb': {'@type': 'BreadcrumbList', 'itemListElement': [
         {'@type': 'ListItem', 'position': 1, 'name': 'Velocity Shop', 'item': SITE},
         {'@type': 'ListItem', 'position': 2, 'name': 'Shipping and returns', 'item': SITE + 'shipping-returns/'}]}},
]}, ensure_ascii=False, indent=1)

lowest = min(it['price'] for it in items)
newest = date.fromisoformat(items[0]['added'])
values = {
    '{{HERO}}': HERO, '{{CLOTHING}}': clothing, '{{FINDS}}': finds, '{{SIZES}}': sizes, '{{CARDS}}': CARDS,
    '{{JUST}}': JUST, '{{MOMENTS}}': MOMENTS_HTML, '{{LD}}': LD_HOME, '{{N}}': str(N), '{{FROM}}': money(lowest),
    '{{UTM}}': UTM, '{{NEWEST}}': f'{newest.strftime("%B")} {newest.day}', '{{YEAR}}': str(date.today().year),
    '{{MORE}}': str(min(24, N - 24)),
}
for src, dst in (('index.template.html', 'index.html'), ('policy.template.html', 'shipping-returns/index.html')):
    src, dst = os.path.join(HERE, src), os.path.join(ROOT, dst)
    page = open(src, encoding='utf-8').read()
    page = page.replace('{{LD_POLICY}}', LD_POLICY)
    for key, v in values.items():
        page = page.replace(key, v)
    assert '{{' not in page, (src, page[page.index('{{'):page.index('{{') + 30])
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    open(dst, 'w', encoding='utf-8').write(page)
print('built', N, 'products; lowest', money(lowest), '; newest', newest)
sm = os.path.join(ROOT, 'sitemap.xml')
xml = open(sm, encoding='utf-8').read()
open(sm, 'w', encoding='utf-8').write(re.sub(r'<lastmod>[^<]*</lastmod>', f'<lastmod>{date.today().isoformat()}</lastmod>', xml))
