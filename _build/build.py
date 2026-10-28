# Builds the Velocity Shop store from products.json:
#   index.html                    the store, following a high-converting homepage layout
#   shop/index.html               every piece in stock, with filters
#   img/grid.webp                 a 10 x 10 contact sheet of 100 pieces in stock, for About
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

# Real eBay feedback and best sellers (_build/ebay.json). Never put made-up numbers or words there.
EBAY = json.load(open(os.path.join(HERE, 'ebay.json'), encoding='utf-8'))
CLOTHING = ('tees', 'shirts', 'hoodies', 'outerwear', 'bottoms', 'jerseys')

data = json.load(open(os.path.join(ROOT, 'products.json'), encoding='utf-8'))
items = data['items']
N = len(items)
e = html.escape
HOME_N = 12

CATS = [  # key, label, short description
    ('tees', 'Tees', 'Tour, band, team and graphic tees.'),
    ('shirts', 'Shirts & polos', 'Polo Ralph Lauren, Lacoste and dress shirts by neck size.'),
    ('hoodies', 'Hoodies & sweaters', 'Champion, Nike and team zips, crewnecks and knits.'),
    ('outerwear', 'Jackets & vests', 'Ski jackets, puffers, fleece vests and cardigans.'),
    ('bottoms', 'Jeans & pants', "Levi's, Silver and Rag & Bone, by waist and inseam."),
    ('jerseys', 'Jerseys', 'Raptors, Blue Jays and soccer kit.'),
    ('collectibles', 'Cards & collectibles', 'Pokémon TCG singles, albums and collector pieces.'),
    ('home', 'Home & tech', 'Tested VCRs, mugs, keyboards and other finds.'),
    ('shoes', 'Shoes & socks', 'Sneakers and multipacks.'),
]
CAT_LABEL = {k: l for k, l, _ in CATS}


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
    if '×' in s: return s + ' (waist × inseam)'
    return s if s.startswith('US ') else 'Size ' + s


def link(url, slot):
    return f"{e(url)}?{UTM}&amp;utm_content={slot}"


def alt_for(it):
    return it['name'] + (', ' + size_label(it) if it['size'] else '') + ', ' + money(it['price']) + ' CAD.'


def img(path, alt, w=560, h=560, lazy=True, cls='', priority=False):
    c = f' class="{cls}"' if cls else ''
    lz = ' loading="lazy"' if lazy else ''
    fp = ' fetchpriority="high"' if priority else ''
    return f'<img{c} src="/{path}" width="{w}" height="{h}" alt="{e(alt)}"{lz}{fp} decoding="async">'


NEW_TAB = '<span class="vh"> (opens on our Square store)</span>'


def card(it, slot, i=0, hidden=False, grid=False):
    added = date.fromisoformat(it['added'])
    back = f' data-back="/{it["img"][1]}"' if len(it['img']) > 1 else ''
    meta = e(size_label(it)) if it['size'] else e(CAT_LABEL[it['cat']])
    return (f'<li class="card" data-cat="{it["cat"]}" data-size="{size_group(it["size"])}"{" data-grid" if grid else ""}{" hidden" if hidden else ""}>'
            f'<a href="{link(it["link"], slot)}" target="_blank" rel="noopener"{back}>'
            f'<span class="pic">{img(it["img"][0], alt_for(it), lazy=(i > 3), cls="front")}</span>'
            f'<span class="card-body"><span class="card-name">{e(it["name"])}</span>'
            f'<span class="card-meta">{meta}</span>'
            f'<span class="card-row"><b class="price">{money(it["price"])}</b><span class="card-date">Added {added.strftime("%b")} {added.day}</span></span>'
            f'<span class="card-btn">View on Square <span aria-hidden="true">↗</span></span></span>{NEW_TAB}</a></li>')


def pick(words):
    for w in words:
        for it in items:
            if w.lower() in it['name'].lower(): return it
    return items[0]


# ---------- hero: a deck of standout clothing pieces, dealt one every 2 seconds ----------
hero = pick(['Ski Patch', 'Polo Bear', 'Lacoste', 'Raptors', 'Polo Ralph Lauren'])
deck, seen = [hero], {hero['cat']: 1}
for it in sorted((x for x in items if x['cat'] in CLOTHING and x is not hero), key=lambda x: -x['price']):
    if len(deck) == 8: break
    if seen.get(it['cat'], 0) < 2:
        deck.append(it); seen[it['cat']] = seen.get(it['cat'], 0) + 1
BEHIND = ' tabindex="-1" aria-hidden="true"'
HERO_IMG = '<div class="deck" id="deck" aria-roledescription="carousel" aria-label="Pieces in stock">\n      ' + '\n      '.join(
    f'<a class="deck-card" style="--p:{i}" href="{link(it["link"], "hero-deck")}" target="_blank" rel="noopener"'
    f'{BEHIND if i else ""}>'
    f'{img(it["img"][0], alt_for(it), lazy=(i > 2), priority=(i == 0))}'
    f'<span class="hero-tag">{money(it["price"])}{" · " + e(it["size"]) if it["size"] else ""}</span>{NEW_TAB}</a>'
    for i, it in enumerate(deck)) + (
    '\n      <button type="button" class="deck-pause" id="deck-pause" aria-pressed="false" hidden>Pause</button>\n    </div>')

# ---------- best sellers: most-viewed clothing on eBay (only with real view counts) ----------
by_id = {it['id']: it for it in items}
best = [(by_id[b['square_id']], b['views']) for b in sorted(EBAY.get('bestsellers', []), key=lambda b: -b['views'])
        if b.get('square_id') in by_id and by_id[b['square_id']]['cat'] in CLOTHING][:8]

# ---------- under $40 ----------
deals = sorted([it for it in items if it['price'] < 40], key=lambda x: (x['price'], x['added']))
deals_pick = sorted(deals, key=lambda x: x['added'], reverse=True)[:8]
DEALS = '\n      '.join(card(it, 'under-40', i) for i, it in enumerate(deals_pick))
if len(best) >= 4:
    ROW_HTML = f'''<section class="row" id="best-sellers" aria-labelledby="h-best">
    <div class="sec-head">
      <h2 id="h-best">Best sellers</h2>
      <p>The clothing buyers look at most on our eBay store, ranked by views.</p>
    </div>
    <ul class="cards cards-row" role="list">
      {chr(10).join(card(it, 'best-sellers', i) for i, (it, v) in enumerate(best))}
    </ul>
  </section>'''
    ROW_ID, ROW_LABEL = 'best-sellers', 'Best sellers'
else:
    ROW_HTML = f'''<section class="row" id="under-40" aria-labelledby="h-deals">
    <div class="sec-head">
      <h2 id="h-deals">Under $40</h2>
      <p>{len(deals)} pieces for less than forty dollars. The newest eight are here.</p>
    </div>
    <ul class="cards cards-row" role="list">
      {DEALS}
    </ul>
  </section>'''
    ROW_ID, ROW_LABEL = 'under-40', 'Under $40'

# ---------- categories ----------
cat_tiles = []
for k, l, d in CATS:
    mine = [it for it in items if it['cat'] == k]
    if not mine: continue
    cover = mine[0]
    cat_tiles.append(f'<li><a class="cat" href="/shop/?cat={k}">{img(cover["img"][0], "")}'
                     f'<span class="cat-name">{e(l)}</span><span class="cat-n">{len(mine)} {"piece" if len(mine) == 1 else "pieces"}</span></a></li>')
CATS_HTML = '\n        '.join(cat_tiles[:8])

# ---------- just in (home) and the whole shop (/shop/) ----------
JUST_IN = '\n      '.join(card(it, 'just-in', i) for i, it in enumerate(items[:HOME_N]))
CARDS = '\n      '.join(card(it, 'shop', i, grid=True) for i, it in enumerate(items))
CAT_OPTIONS = ''.join(f'<option value="{k}">{e(l)}</option>' for k, l, _ in CATS if any(it['cat'] == k for it in items))

# ---------- eBay reviews (written by real buyers, copied word for word) ----------
reviews = EBAY.get('reviews', [])
if len(reviews) >= 3:
    quotes = '\n      '.join(
        f'<li class="review"><p class="review-badge">Positive feedback</p><blockquote><p>{e(r["text"])}</p></blockquote>'
        f'<p class="review-by"><b>{e(r["buyer"])}</b>, verified eBay buyer<span class="review-item">Bought: {e(r["item"])}</span></p></li>'
        for r in reviews)
    EBAY_HTML = f'''<section class="reviews" id="reviews" aria-labelledby="h-reviews">
    <div class="sec-head">
      <h2 id="h-reviews">What eBay buyers say</h2>
      <p><b>{e(EBAY["positive"])} positive feedback</b> in the last 12 months, with a feedback score of {EBAY["score"]}. These are buyers' own words, unedited.</p>
    </div>
    <ul class="review-grid" role="list">
      {quotes}
    </ul>
    <p class="reviews-more"><a class="btn btn-green" href="{e(EBAY["feedback"])}" target="_blank" rel="noopener">Read all our eBay feedback<span class="vh"> (opens eBay)</span> <span aria-hidden="true">↗</span></a></p>
  </section>'''
    WHY_HTML = ''
else:
    EBAY_HTML = ''
    WHY_HTML = None  # keep the Why shop with us section

# ---------- why choose us, how it works, about ----------
why = pick(['Lacoste Classic', 'Lacoste', 'Polo'])
WHY_IMG = img(why['img'][0], alt_for(why))
steps = [
    ('Picked', 'One piece at a time, only if it is worth wearing again.', pick(['Ski Patch', 'Jacket'])),
    ('Checked', 'Seams, zips, cuffs and collars looked over in good light.', pick(['Lacoste Mens Polo', 'Polo'])),
    ('Photographed', 'Front, back and any wear, so you see the real piece.', pick(['Kendrick', 'T-Shirt'])),
    ('Listed', 'On our Square store with its size and a fair price in CAD.', pick(['Showtime', 'Hoodie'])),
    ('Shipped', 'Packed and out the door in 1-2 business days.', pick(["Levi", 'Jeans'])),
]
STEPS = '\n      '.join(
    f'<li class="step"><a href="{link(it["link"], "how-it-works")}" target="_blank" rel="noopener">{img(it["img"][0], alt_for(it))}{NEW_TAB}</a>'
    f'<h3><span class="step-n" aria-hidden="true">{i + 1}</span> {e(t)}</h3><p>{e(d)}</p></li>'
    for i, (t, d, it) in enumerate(steps))
# ---------- about: a 10 x 10 contact sheet of the pieces in stock right now ----------
from PIL import Image
k = 10 if N >= 100 else int(N ** 0.5)
TILE = 120
sheet = Image.new('RGB', (k * TILE, k * TILE), (242, 246, 255))
for n, it in enumerate(items[:k * k]):
    with Image.open(os.path.join(ROOT, it['img'][0])) as im:
        sheet.paste(im.convert('RGB').resize((TILE, TILE), Image.LANCZOS), ((n % k) * TILE, (n // k) * TILE))
sheet.save(os.path.join(ROOT, 'img', 'grid.webp'), 'WEBP', quality=78, method=6)
ABOUT_IMG = (f'<a class="about-grid" href="/shop/">{img("img/grid.webp", f"A {k} by {k} grid of photos of {k * k} pieces in stock right now at Velocity Shop: polos, tees, hoodies, jeans, jerseys and finds.", w=k * TILE, h=k * TILE)}'
             f'<span class="vh"> Shop all {N} pieces</span></a>')
GRID_N = k * k

# ---------- FAQ (answers are the shop's real policies) ----------
FAQ = [
    ('Where do you ship, and how fast?', 'We ship to Canada and the United States. Orders are packed and handed to the carrier within 1-2 business days of checkout. Shipping options and costs are shown on our Square store before you pay.'),
    ('Can I return something?', 'Yes. You can return a piece within 30 days of delivery, as long as it is unworn and in the condition it arrived in. Start a return through our Square store with your order details.'),
    ('What condition are the pieces in?', 'Everything is pre-owned. Each piece is checked by hand before it is listed, and any wear, mark or flaw is shown in the photos and named in the listing.'),
    ('How do sizes work?', 'Each listing gives the tag size. Jeans and pants are listed by waist and inseam, like 32×30, and dress shirts by neck size, like 15.5. Use the size filter to see what fits.'),
    ('Is checkout secure?', 'Yes. You check out on our Square store, which handles payment. Your card details go to Square and never to us. Prices are in Canadian dollars.'),
    ('Will you restock something that sold?', 'Almost never. Nearly everything is one of a kind, so once a piece sells it is gone. New pieces go up most weeks.'),
]
FAQ_HTML = '\n      '.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in FAQ)

# ---------- structured data ----------
store_ld = {
    '@type': 'OnlineStore', '@id': SITE + '#store', 'name': 'Velocity Shop', 'alternateName': 'Velocity Shop International',
    'url': SITE, 'logo': SITE + 'img/logo.png', 'image': SITE + 'img/og.jpg',
    'description': 'Online resale shop for one-of-a-kind pre-loved clothing and finds. Every piece is checked by hand, photographed front and back and priced in Canadian dollars. Checkout on Square.',
    'currenciesAccepted': 'CAD', 'sameAs': [STORE] + ([EBAY['profile']] if EBAY.get('profile') else []),
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
    {'@type': 'FAQPage', '@id': SITE + '#faq', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]},
]}, ensure_ascii=False, indent=1).replace('</', '<\\/')
LD_SHOP = json.dumps({'@context': 'https://schema.org', '@graph': [
    store_ld,
    {'@type': 'CollectionPage', 'url': SITE + 'shop/', 'name': 'Shop all | Velocity Shop', 'isPartOf': {'@id': SITE + '#website'},
     'breadcrumb': {'@type': 'BreadcrumbList', 'itemListElement': [
         {'@type': 'ListItem', 'position': 1, 'name': 'Velocity Shop', 'item': SITE},
         {'@type': 'ListItem', 'position': 2, 'name': 'Shop all', 'item': SITE + 'shop/'}]},
     'mainEntity': {'@type': 'ItemList', '@id': SITE + 'shop/#items', 'name': 'Everything in stock at Velocity Shop', 'numberOfItems': N, 'itemListElement': products}},
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
    '{{HERO_IMG}}': HERO_IMG, '{{ROW}}': ROW_HTML, '{{ROW_ID}}': ROW_ID, '{{ROW_LABEL}}': ROW_LABEL, '{{CATS}}': CATS_HTML,
    '{{JUST_IN}}': JUST_IN, '{{CARDS}}': CARDS, '{{CAT_OPTIONS}}': CAT_OPTIONS, '{{EBAY}}': EBAY_HTML, '{{WHY_IMG}}': WHY_IMG,
    '{{LD_SHOP}}': LD_SHOP, '{{GRID_N}}': str(GRID_N), '{{HOME_N}}': str(HOME_N),
    '{{STEPS}}': STEPS, '{{ABOUT_IMG}}': ABOUT_IMG, '{{FAQ}}': FAQ_HTML, '{{LD}}': LD_HOME,
    '{{N}}': str(N), '{{FROM}}': money(lowest), '{{UTM}}': UTM, '{{YEAR}}': str(date.today().year),
    '{{NEWEST}}': f'{newest.strftime("%B")} {newest.day}',
}
for src, dst in (('index.template.html', 'index.html'), ('shop.template.html', 'shop/index.html'), ('policy.template.html', 'shipping-returns/index.html')):
    page = open(os.path.join(HERE, src), encoding='utf-8').read().replace('{{LD_POLICY}}', LD_POLICY)
    if WHY_HTML is not None:  # real reviews take the place of the Why section
        page = re.sub(r'<!-- why -->.*?<!-- /why -->', WHY_HTML, page, flags=re.S)
    page = page.replace('<!-- why -->', '').replace('<!-- /why -->', '')
    for key, v in values.items():
        page = page.replace(key, v)
    assert '{{' not in page, (src, page[page.index('{{'):page.index('{{') + 30])
    out = os.path.join(ROOT, dst)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(page)
sm = os.path.join(ROOT, 'sitemap.xml')
xml = open(sm, encoding='utf-8').read()
open(sm, 'w', encoding='utf-8').write(re.sub(r'<lastmod>[^<]*</lastmod>', f'<lastmod>{date.today().isoformat()}</lastmod>', xml))
print('built', N, 'products;', len(best), 'best sellers;', len(reviews), 'reviews;', len(deals), 'under $40; lowest', money(lowest), '; newest', newest)
