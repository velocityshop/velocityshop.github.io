# Refreshes products.json and the product photos from the Square store's public product feed.
# Run from anywhere:  python3 _build/update.py   then   python3 _build/build.py
# Needs Pillow (pip install pillow). Prints what changed; exits 2 if the feed could not be read.
import html, io, json, os, re, sys, urllib.request
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEED = ('https://cdn5.editmysite.com/app/store/api/v28/editor/users/156368681/sites/261932279624443156/'
        'products?per_page=100&include=images&page={}')
STORE = 'https://velocity-shop.square.site/'

RULES = [
    ('jerseys', r'\bjersey\b|swingman|sleeveless t'),
    ('outerwear', r'jacket|vest\b|cardigan|puffer|windbreaker|fleece lined|parka|coat\b'),
    ('hoodies', r'hoodie|sweatshirt|crewneck|full zip|full-zip|sweater'),
    ('bottoms', r'jeans|pants?\b|chino|shorts|trousers|overalls'),
    ('shirts', r'polo shirt|\bpolo\b|dress shirt|button[- ]?(up|down)|oxford|flannel|shirt men.s \d|chemise'),
    ('tees', r't-shirt|t shirt|\btee\b|tank'),
    ('shirts', r'\bshirt\b|\bdress\b'),
    ('shoes', r'shoe|sneaker|ultraboost|running|boots?\b|jordan|nike air max|socks'),
    ('collectibles', r'pokemon|tcg|album|card\b|holo|vinyl|funko|figure|inclusions pictured|boyds bears'),
]


def cat(name):
    n = name.lower()
    for c, rx in RULES:
        if re.search(rx, n): return c
    return 'home'


def size(name):
    n = ' ' + name + ' '
    m = re.search(r'\b(\d{2})\s?[xX×]\s?(\d{2})\b', n)
    if m: return f'{m.group(1)}×{m.group(2)}'
    m = re.search(r'\b(XXS|XS|S|M|L|XL|XXL|2XL|3XL)\b', n)
    if m: return {'2XL': 'XXL'}.get(m.group(1), m.group(1))
    m = re.search(r'\b(Small|Medium|Large|X-Large)\b', n, re.I)
    if m: return {'small': 'S', 'medium': 'M', 'large': 'L', 'x-large': 'XL'}[m.group(1).lower()]
    m = re.search(r"Women.?s (\d{1,2}(\.5)?)\b|\b(\d{1,2}(\.5)?) (?:Mens|Women)", n)
    if m: return 'US ' + (m.group(1) or m.group(3))
    return ''


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'velocityshop.github.io sync'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def read_feed():
    out, page = [], 1
    while True:
        data = json.loads(fetch(FEED.format(page)))['data']
        out += data
        if len(data) < 100: return out
        page += 1


def save_photo(url, path):
    im = ImageOps.exif_transpose(Image.open(io.BytesIO(fetch(url)))).convert('RGB')
    w, h = im.size; s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s)).resize((560, 560), Image.LANCZOS)
    im.save(path, 'WEBP', quality=74, method=6)


def main():
    try:
        feed = read_feed()
    except Exception as e:
        print('FEED UNREACHABLE:', type(e).__name__, str(e)[:200]); sys.exit(2)
    old_path = os.path.join(ROOT, 'products.json')
    old = {p['id']: p for p in json.load(open(old_path, encoding='utf-8'))['items']} if os.path.exists(old_path) else {}
    items, failed = [], []
    os.makedirs(os.path.join(ROOT, 'img', 'p'), exist_ok=True)
    for p in feed:
        if p.get('visibility') != 'visible' or (p.get('badges') or {}).get('out_of_stock'): continue
        pics = (p.get('images') or {}).get('data') or []
        if not pics: continue  # nothing to show yet; it appears once it has a photo
        sid = p['square_id']
        imgs = []
        for i, im in enumerate(pics[:2]):
            rel = f'img/p/{sid.lower()}-{i}.webp'
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                try: save_photo(im['absolute_url'], path)
                except Exception as e:
                    failed.append(f'{sid} photo {i}: {type(e).__name__}'); continue
            imgs.append(rel)
        if not imgs: continue
        desc = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(p.get('short_description') or ''))).strip()
        c = cat(p['name'])
        items.append({'id': sid, 'name': p['name'].strip(), 'price': p['price']['low'],
                      'link': STORE + p['site_link'], 'cat': c,
                      'size': size(p['name']) if c not in ('collectibles', 'home') else '',
                      'added': p['created_date'][:10], 'img': imgs, 'desc': desc[:300]})
    if not items:
        print('FEED EMPTY: refusing to write an empty store'); sys.exit(2)
    items.sort(key=lambda x: (x['added'], x['id']), reverse=True)
    new = {p['id']: p for p in items}
    added = [new[k]['name'] for k in new if k not in old]
    removed = [old[k]['name'] for k in old if k not in new]
    changed = [new[k]['name'] for k in new if k in old and any(new[k][f] != old[k][f] for f in ('name', 'price', 'link', 'img'))]
    # Photos of pieces that are gone are deleted with them.
    keep = {i for p in items for i in p['img']}
    for f in os.listdir(os.path.join(ROOT, 'img', 'p')):
        if f'img/p/{f}' not in keep: os.remove(os.path.join(ROOT, 'img', 'p', f))
    json.dump({'synced': max(x['added'] for x in items), 'store': STORE, 'items': items},
              open(old_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(items)} pieces in stock. Added {len(added)}, removed {len(removed)}, updated {len(changed)}.')
    for n in added: print('  + ' + n)
    for n in removed: print('  - ' + n)
    for n in changed: print('  ~ ' + n)
    for f in failed: print('  photo failed: ' + f)


if __name__ == '__main__':
    main()
