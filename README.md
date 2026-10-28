# Velocity Shop

The Velocity Shop store site, served with GitHub Pages at https://velocityshop.github.io/.
Plain HTML, CSS and a little JavaScript. No server code and no payments: every product links to its listing on https://velocity-shop.square.site/, where checkout happens.

| Path | What it is |
| --- | --- |
| `index.html` | The store: every product in stock, categories, how it works, trust, about |
| `shipping-returns/index.html` | Shipping, returns, condition and checkout |
| `products.json` | The product snapshot the pages are built from |
| `img/p/` | Product photos (WebP, 560 px) |
| `css/`, `js/`, `fonts/`, `img/` | Styles, script, the Switzer font, logo and icons |
| `sitemap.xml`, `robots.txt`, `404.html` | Search engine files and the not-found page |

Products refresh from the Square store with `python3 _build/update.py` then `python3 _build/build.py` (the daily sync does this). `rack/` only forwards old rack links to the store.
