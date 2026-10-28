# Velocity Shop

The Velocity Shop store site, served with GitHub Pages at https://velocityshop.github.io/.
Plain HTML, CSS and a little JavaScript. No server code and no payments: every product links to its listing on https://velocity-shop.square.site/, where checkout happens.

| Path | What it is |
| --- | --- |
| `index.html` | The store: hero, Under $40, categories, every product in stock, why us, how it works, about, FAQ |
| `shipping-returns/index.html` | Shipping, returns, condition and checkout |
| `products.json` | The product snapshot the pages are built from |
| `img/p/` | Product photos (WebP, 560 px) |
| `css/`, `js/`, `fonts/`, `img/` | Styles, script, the Satoshi font, logo and icons |
| `sitemap.xml`, `robots.txt`, `404.html` | Search engine files and the not-found page |

To refresh products, run `make_products.py` and `build.py` from the build kit.
