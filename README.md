# Velocity Shop

The Velocity Shop website, served with GitHub Pages at https://velocityshop.github.io/.
Plain HTML, CSS and JavaScript: no build step, nothing server-side.

| Path | What it is |
| --- | --- |
| `index.html` | Landing page (hero, Find your size, On the rail, How it works, About) |
| `rack/index.html` | The interactive round clothing rack |
| `rack/rack.json` | Every piece on the rack: `{store, synced, items[]}` |
| `rack/images.json` | Photo index: `{photo: {w, h, front, back}}`, paths relative to `rack/` |
| `rack/img/*.webp` | Garment photos, front and back |
| `assets/` | Stylesheet, script, logo, icons and share images |
| `sitemap.xml`, `robots.txt`, `404.html` | Search engine files and the not-found page |

Both pages read `rack/rack.json` and `rack/images.json`, which the Square sync rewrites.
Edit listings in Square, not here. Every link to Square carries `utm_source=velocityshop.github.io`.
Old piece links (`/#piece-name-abc123`) forward to `/rack/#piece-name-abc123`.
