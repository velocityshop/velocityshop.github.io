# Evidence-Based Ecommerce Conversion and Usability: Homepage, Product Lists, Product Cards (Apparel)

Method note: Research done 2026-10-28. Direct fetches of baymard.com and web.dev failed: their hostnames are not on this session's allowed network list (DNS failure). Baymard and web.dev findings below therefore come from search-result snippets of their own pages, not full-page reads. Most of Baymard's detailed guideline text is behind Baymard Premium in any case. Each item is labelled **[Tested]** (usability testing, A/B test or measured field data with stated method), **[Benchmark]** (audit of how many sites do X), **[Correlational]** (observational data), **[Standard]** (a published standard or platform guideline) or **[Opinion]** (practitioner advice without stated testing).

## Homepage and above the fold (hero, value proposition, carousels, showing products early, CTAs)

### Takeaway
The evidence argues against auto-rotating carousels, especially on mobile. A static hero followed by stacked rows of content tests as well and is simpler to build. The homepage should show a broad sample of the catalog early: Baymard found users underestimate a store's range when the homepage features too few product types. I found no rigorous public study that fixes an ideal number of primary CTAs or tests value-proposition copy for apparel.

### Cited Findings
- **[Benchmark]** 33% of top US/European desktop ecommerce sites have a homepage carousel. About 46% of desktop and mobile sites that use one have an implementation with usability issues. Another Baymard page gives 28%, so the figure varies by date and sample. — [Baymard, homepage carousel](https://baymard.com/blog/homepage-carousel)
- **[Tested]** In Baymard's mobile testing, auto-rotating carousels sent participants on unintended detours. 52% of mobile sites and apps auto-rotate their homepage carousel. Baymard's guidance: turn off auto-rotation, don't put vital features only in slides, support swipe gestures, and make controls visible and legible. — [Baymard, homepage carousel](https://baymard.com/blog/homepage-carousel)
- **[Tested, per Baymard]** An alternative pattern performs as well with users and is technically much simpler to get right: the slide content shown as static sections on a taller homepage. — [Baymard, homepage carousel](https://baymard.com/blog/homepage-carousel)
- **[Tested, older classic, 2013]** In Nielsen Norman Group testing, a user failed to find a target shown at the top of the page in 98-point type because the carousel panel auto-forwarded. NN/g recommends not auto-forwarding on mobile and says several rows of content usually work better than a rotating slider. *Note: I could not reach the NN/g page itself; this comes from secondary summaries.* — [VWO summary of NN/g](https://vwo.com/blog/image-slider-alternatives); [Yale Usability, hero images/carousels](https://usability.yale.edu/usability-best-practices/hero-imagescarousels)
- **[Tested, older classic]** NN/g's banner-blindness finding: users "never look at anything that looks like an advertisement, whether or not it's actually an ad". This is a risk for promo-styled heroes. — [Yale Usability](https://usability.yale.edu/usability-best-practices/hero-imagescarousels)
- **[Tested]** Baymard guideline #237: when the homepage showed only a narrow range of product types, many participants misunderstood what kind of site it was or underestimated its range. Recommendation: feature a broad range of product types, aiming for at least 40% of your product types. — [Baymard, 35 data-driven ecommerce best practices](https://baymard.com/blog/ecommerce-ux-best-practices)
- **[Benchmark]** Baymard's 2023 Homepage & Category benchmark update reassessed 68 sites against 45 research-based homepage and category guidelines. — [Baymard, 2023 benchmark update](https://baymard.com/blog/2023-benchmark-update-homepage-and-category)
- **[Opinion]** Econsultancy offers carousel alternatives that it says convert better. These are practitioner case examples, not a controlled study. — [Econsultancy](https://econsultancy.com/three-ideas-that-convert-better-than-a-standard-carousel/)

### Inferences
- For a small resale clothing store: use one static hero with a clear value line (what is sold, condition, price range) and a single primary CTA (e.g. "Shop new arrivals"). Then show real product cards and category tiles high on the page instead of more slides.
- Show items from most product types (tops, outerwear, denim, shoes, etc.) on the homepage. This follows Baymard's 40% guideline and keeps visitors from underestimating the range.
- If a carousel is used anyway, it should never auto-rotate and should support swipe gestures.

### Gaps
- No credible public study gave an optimal number of hero CTAs. "One primary CTA" is practitioner convention.
- No 2022–2026 controlled A/B data on hero image vs. product-grid-first for apparel was found.
- I could not read NN/g's carousel or homepage articles directly (not in search results) or Baymard's full carousel guidance (fetch blocked).

## Navigation and category tiles (count, labels, "shop by" entry points, mobile nav patterns, sticky headers)

### Takeaway
Visible or partially visible navigation beats navigation hidden entirely behind a hamburger, on both desktop and mobile (NN/g, 2016). On mobile, the product categories themselves should be the top-level menu items, not tucked under a "Shop" link. For apparel, size is the dominant "shop by" dimension. I found no research-backed ideal category count.

### Cited Findings
- **[Tested, older classic, 2016]** NN/g ran a quantitative study (179 participants, six live sites, desktop and mobile). Hidden navigation reduced discoverability by about 20% compared with visible or combo navigation (one secondary source says about 21%). Tasks took 39% longer on desktop and 15% longer on mobile, and self-rated difficulty was higher. NN/g concluded that hidden navigation is worse than visible or partially visible navigation on both phones and desktop. *Note: comes from secondary summaries; original NN/g page not retrieved.* — [Smart Insights summary](https://www.smartinsights.com/digital-marketing-strategy/are-hamburger-menus-hidden-navigation-good-for-ux/); [Adrian Roselli](https://adrianroselli.com/2016/01/avoid-the-hamburger-menu-for-desktop-layouts.html)
- **[Tested + Benchmark]** 33% of mobile sites fail to make product categories the top-level items in the mobile main navigation. In testing, nesting categories under a "Shop" link led users to abandon the navigation and switch to search. — [Baymard, mobile main nav / product categories](https://baymard.com/research-articles/main-navigation-product-categories)
- **[Benchmark]** Only 24% of mobile sites fully handle the tap ambiguity, i.e. whether tapping a parent category opens its page or expands its subcategories. Baymard also recommends a "View all" option within mobile nav levels. — [Baymard, mobile main nav "view all"](https://baymard.com/research-articles/mobile-main-nav-view-all)
- **[Benchmark]** Across 244 benchmarked desktop sites, the average top-grossing US/EU site rates "poor" for homepage and category navigation. Up to 67% of leading sites are "mediocre" to "poor" on mobile. Hover menus should use a 300–500 ms hover delay, which 60% of sites don't. — [Baymard, homepage and category usability](https://baymard.com/homepage-and-category-usability)
- **[Tested, apparel]** When the Size filter sits at or near the top of the filter sidebar and is expanded by default, 90% of test participants filtered by size first. 39% of participants found on the product page that their chosen item was not available in their size. — [Baymard, apparel size filter near top](https://baymard.com/blog/apparel-put-size-filter-near-top-and-expand-for-sidebar-filtering)
- **[Opinion/heuristic, NN/g]** Sticky headers help when they keep navigation, search and utility links reachable, but they can annoy users and cover content when done poorly. Partially persistent headers, which reappear when the user scrolls up, are common on mobile and save space. — [NN/g, sticky headers](https://www.nngroup.com/articles/sticky-headers/)
- **[Tested, academic, 2024]** A SciTePress paper reports that persistent headers improved performance and satisfaction, particularly on slightly larger screens. *I only saw the search snippet; method details are unverified.* — [SciTePress 2024](https://scitepress.org/Papers/2024/125549/125549.pdf)
- **[Benchmark]** On mobile, sites often hide the search field behind an icon or inside the hamburger menu, while desktop usually shows it in the header. These are annotated examples from 93 sites; the conclusions are behind Premium. — [Baymard, mobile search field benchmark](https://baymard.com/mcommerce-usability/benchmark/mobile-page-types/search-field)

### Inferences
- On mobile, show the main categories as visible tabs, chips or tiles on the homepage or under the header. A small resale catalog likely has few enough categories to fit (e.g. New in / Tops / Bottoms / Outerwear / Shoes). Keep the hamburger only for secondary links.
- Offer "Shop by size" as a first-class entry point (size chips on the homepage, and size first in filters). Resale stock is one-of-a-kind, so a size mismatch dead-ends the shopper (Baymard's 39% finding).
- A slim, partially persistent header (logo, categories or search, external "Shop on Square" link) fits the NN/g guidance.

### Gaps
- I found no research-backed optimal number of top-level categories or homepage category tiles.
- I found no study testing "Shop by" homepage modules (size, category, new in) against alternatives. Recommending them combines Baymard's size-filter findings with inference.
- The NN/g hamburger study is from 2016. I found no 2022–2026 replication.

## Product list/grid and card design (images, hover images, card info, grid density, load more vs pagination vs infinite scroll, filtering and sorting)

### Takeaway
Cards should show a consistent, "just enough" set of attributes (for apparel: image, title, price, size, condition, availability) so shoppers can judge relevance without opening each item. Baymard's testing favours "Load more" with lazy-loading over pagination and infinite scroll. Size is the key apparel filter. Colour variants belong in one list item as swatches. Baymard also flags a need for multiple images in the list.

### Cited Findings
- **[Benchmark]** 64% of sites fail to present information adequately in product listings, and 50% don't show the right balance of important content in list items. — [Baymard, product listing information](https://baymard.com/research-articles/product-listing-information); [Baymard, list item design](https://baymard.com/research-articles/list-item-design-ecommerce)
- **[Tested]** When list items lacked key attributes, participants missed relevant products or bounced between the list and product pages, which often led to abandonment. Baymard's principles: show the same attributes across all list items, make separate elements visually distinct, and show "just enough" to judge relevance and compare. — [Baymard, product listing information](https://baymard.com/research-articles/product-listing-information)
- **[Tested, scale]** Baymard's product list study tested 19 leading ecommerce sites across 8 verticals and produced 83 product list usability guidelines. — [Baymard, product lists research](https://baymard.com/research/ecommerce-product-lists)
- **[Benchmark, guideline heading]** "Always Provide 3 or More Product Thumbnails in Product Lists and Search Results (80% Don't)". *I only saw the heading in a snippet; the full rationale was not retrieved.* — [Baymard, product list collection](https://baymard.com/research-articles/collections/product-list)
- **[Tested]** Colour variants should be one list item shown as swatches, not text or separate items. On 57% of sites, not all colour variations are available in the product list. On mobile, a horizontally scrollable swatch list performed well for most users. When only a few swatches were shown, participants still had to open product pages to assess suitability. — [Baymard, mobile interactive colour swatches](https://baymard.com/research-articles/mobile-interactive-color-swatches)
- **[Tested, older classic, 2016]** Baymard tested pagination, "Load more" and infinite scroll across more than 50 sites on desktop and mobile. "Load more" combined with lazy-loading was the better implementation. Infinite scroll can be "downright harmful" to usability, especially for search results and on mobile. Pagination remains common mainly because platforms ship it by default. — [Smashing Magazine (Baymard's Christian Holst)](https://www.smashingmagazine.com/2016/03/pagination-infinite-scrolling-load-more-buttons/); [Baymard original](https://baymard.com/blog/external-load-more-vs-pagination-vs-infinite-scrolling)
- **[Tested, apparel]** For apparel, put the Size filter at the top and expand it by default (90% then filter by size first). Size options should be grouped by size type with clear headers, e.g. jeans in Petite / Regular / Plus plus Waist and Length. — [Baymard, size filter placement](https://baymard.com/blog/apparel-put-size-filter-near-top-and-expand-for-sidebar-filtering); [Baymard, formatting size options](https://baymard.com/research-articles/apparel-how-to-format-size-options-in-the-size-filter)
- **[Secondary summary of Baymard checklist]** The core filter types are Price, Ratings, Color, Size and Brand. Applied filters should appear both inline and in a summary at the top of the filter area. Alphabetical sorting should not be the default. — [YesPlz summary of Baymard 2023 criteria](https://yesplz.ai/resource/dont-make-these-product-filtering-mistakes-baymard-checklist-2023.html)
- **[Standard]** Google Merchant Center allows titles up to 150 characters, but only about 70 display on Shopping ads and listings. Google advises putting distinctive attributes first. — [Google Merchant Center help](https://support.google.com/merchants/answer/14989281)
- **[Opinion, vendor]** Titles longer than about 30–40 characters typically truncate in mobile collection grids, hiding details such as size or shade. — [GrowthSuite](https://www.growthsuite.net/questions/are-my-product-titles-truncating-in-collection-grids-and-confusing-visitors)
- **[Vendor feature, not research]** Hover-swap ("second image on hover") tools show the second image on first tap on touch devices. — [X-Cart addon](https://market.x-cart.com/addons/dual-image-hover-on-product-listings.html); [Shopify app](https://apps.shopify.com/gs-change-image-on-hover?locale=cs)

### Inferences
- Card spec for a one-of-a-kind resale apparel store: image at a consistent aspect ratio, short title with brand and item type first, price, size, condition, and a sold/available state. Keep these fields in the same position on every card. Baymard's consistency and "just enough" findings are the basis.
- Size on the card matters even more in resale, where every item comes in one size. Baymard's 39% "wrong size discovered on PDP" problem would otherwise recur on every card.
- A second image (back view, label or detail) adds information. Baymard's "3+ thumbnails" heading supports multiple images, but the hover-swap pattern itself isn't validated. On touch devices, a tap-to-swap that hijacks the first tap could conflict with tapping through to Square, so a swipeable image strip or "+2 photos" indicator is safer (inference).
- For a modest catalog, use a "Load more" button with lazy-loaded images rather than infinite scroll. This also keeps the footer reachable.
- Since checkout is on Square, the card's tap target is effectively an outbound link. Label it clearly (e.g. "View on Square") so the context switch is not a surprise (inference; no study found).

### Gaps
- I found no public research-backed rule for grid density (1 vs 2 columns on mobile; 3 vs 4 on desktop). Baymard has premium material on this that I could not reach. The two-column mobile grid is industry convention, not a cited finding here.
- I found no controlled study of hover image swaps or of badges ("New", "Sale", "Last one") on clothing click-through.
- I could not retrieve Baymard's full text on title length or truncation in list items.

## Mobile-specific findings (thumb reach, tap targets, sticky CTAs)

### Takeaway
Tap targets should meet at least WCAG 2.2's 24x24 CSS px (AA), and ideally the platform guidelines of 44pt (Apple) or 48dp (Google). Hoober's observations show that a large share of users operate phones one-handed. I found no rigorous public study on sticky CTAs for listing pages.

### Cited Findings
- **[Standard]** WCAG 2.2 SC 2.5.8 Target Size (Minimum), Level AA: pointer targets must be at least 24x24 CSS px, or spaced so that a 24px circle centred on each target doesn't touch another. Exceptions: equivalent control, inline text, user-agent controls, essential. — [DAISY KB](https://kb.daisy.org/publishing/docs/wcag/target-size-minimum.html); [Deque axe rule](https://dequeuniversity.com/rules/axe/4.8/target-size)
- **[Standard]** Apple's minimum tap target is 44x44 pt; Google Material recommends 48x48 dp (about 7 mm). — [IxDF](https://ixdf.org/literature/article/how-to-use-tappability-affordances); [Redalyc academic paper](https://www.redalyc.org/pdf/496/49645986004.pdf)
- **[Observational, older classic, 2013]** In Steven Hoober's field observations, 49% of people held their phones one-handed. His "thumb zone" describes the comfortable reach area for one-handed use, and people also switch grips and use two thumbs. — [Smashing Magazine, The Thumb Zone](https://www.smashingmagazine.com/2016/09/the-thumb-zone-designing-for-mobile-users/)
- **[Tested]** Auto-rotating carousels on mobile caused unintended taps or detours (see the homepage section). — [Baymard](https://baymard.com/blog/homepage-carousel)
- **[Opinion/heuristic]** Partially persistent (reveal-on-scroll-up) headers save space on mobile. — [NN/g, sticky headers](https://www.nngroup.com/articles/sticky-headers/)

### Inferences
- Make every card fully tappable with a minimum height of 44px for text buttons. Put category and size chips and the "Load more" button within easy thumb reach. Avoid tiny swatch dots as the only tap targets.
- A sticky bottom CTA mostly helps product detail pages. On a list or grid page with outbound Square links it adds little, so a sticky header with categories is the better use of persistent space (inference).

### Gaps
- I found no credible 2022–2026 A/B data on sticky CTAs or bottom navigation bars for mobile apparel stores.

## Performance and Core Web Vitals impact on conversion

### Takeaway
Credible studies, a mix of A/B tests and correlational analyses, consistently link faster loading, especially LCP and layout stability, to higher retail conversion. Effect sizes vary widely by site and should not be treated as guaranteed lifts.

### Cited Findings
- **[Correlational, 2020]** Deloitte Digital, "Milliseconds Make Millions" (37 brands in retail, travel, luxury and lead generation, EU/US, 4 weeks of mobile data; commissioned by Google). A 0.1s mobile speed improvement was associated with an 8.4% rise in retail conversions and a 9.2% rise in retail average order value. The PDF rounds the conversion figure to about 8%. Product page to add-to-basket progression rose 9.1% for retail. The 0.1s only counted when every page in the journey improved on four metrics (FMP, Estimated Input Latency, GA page load time, TTFB). — [Deloitte Ireland](https://www.deloitte.com/ie/en/services/consulting/research/milliseconds-make-millions.html); [Deloitte PDF](https://www2.deloitte.com/content/dam/Deloitte/ie/Documents/Consulting/Milliseconds_Make_Millions_report.pdf); [web.dev case study](https://web.dev/case-studies/milliseconds-make-millions); [WARC](https://www.warc.com/en/article/milliseconds-make-millions%3A-a-study-on-how-improvements-in-mobile-site-speed-positively-affect-a-brand%E2%80%99s-bottom-line-4ce17b61c16949cbb961036aafa85dbb)
- **[A/B test, 2021]** Vodafone (Italy) split landing-page traffic 50/50. The variant with 31% better field LCP produced 8% more sales, a 15% better lead-to-visit rate and an 11% better cart-to-visit rate. — [web.dev, Vodafone](https://web.dev/case-studies/vodafone)
- **[A/B test + correlational]** Rakuten 24 found that a good homepage LCP was associated with up to 61.13% higher conversion rate, 26.09% higher revenue per visitor and 11.26% higher AOV. Its Core Web Vitals A/B test produced +53.37% revenue per visitor and +33.13% conversion rate. — [web.dev, Rakuten 24](https://web.dev/case-studies/rakuten)
- **[Correlational, fashion retailer]** Farfetch: conversion rate fell an average of 1.3% for each additional 100 ms of LCP, and the exit rate fell 3.1% for each 0.01 improvement in CLS. — [web.dev, Farfetch](https://web.dev/farfetch/)
- **[Case study, Shopify]** Sunday Citizen improved conversions by focusing on performance. *I only saw the title in search results; figures were not retrieved.* — [Shopify Performance blog](https://performance.shopify.com/en-ca/blogs/blog/how-sunday-citizen-improved-conversions-by-focusing-on-performance)

### Inferences
- For a static site whose LCP element is almost always the hero or first product image, the highest-leverage moves are: preload or prioritise the hero image (fetchpriority), lazy-load below-the-fold card images, serve responsive AVIF/WebP, and set explicit width and height or aspect-ratio on every card image so CLS stays near zero. Farfetch's CLS correlation is from a fashion retailer, so it is directly relevant.
- Avoid heavy third-party embeds (e.g. Square widgets) on list pages. Plain outbound links keep the static site fast.

### Gaps
- The commonly quoted "53% of mobile visits abandoned if load >3s" (Google/Think with Google, 2016) was not verified in this session and is an older industry estimate. Treat it with caution.
- I could not fetch web.dev pages (blocked). Figures come from search snippets of those pages.

## Accessibility findings that affect conversion

### Takeaway
Inaccessible sites lose a measurable share of disabled shoppers, who rarely complain and instead leave. The most common real-world failures, low-contrast text and missing alt text, are exactly the ones a clothing grid with text over photos is prone to.

### Cited Findings
- **[Survey, UK, 2019]** Click-Away Pound: 69% of disabled online consumers would leave a site that was hard to use because of their disability. That represents about 4.9 million shoppers and £17.1bn, around 10% of UK online spend. 83% limit their shopping to sites they know are accessible, 86% have paid more on an accessible site, and only 8% contact the site owner about problems. 72% hit barriers on more than a quarter of new sites they visit. — [Click-Away Pound 2019 press release](https://www.clickawaypound.com/downloads/CAP2019PR2.pdf); [AbilityNet](https://abilitynet.org.uk/news-blogs/research-shows-businesses-lose-17-billion-ignoring-accessibility-needs); [Recite Me summary](https://reciteme.com/news/six-key-points-from-the-click-away-pound-survey-2019)
- **[Automated audit, 2025]** WebAIM Million: low-contrast text appeared on 79.1% of the top 1M home pages (29.6 instances per page on average). Missing alt text appeared on 55.5% of pages, and 18.5% of all home page images had no alt text. The six most common error types account for 96% of detected errors and have been the same for 5 years. This is automated testing only. — [WebAIM Million 2025](https://webaim.org/projects/million/2025)
- **[Standard]** WCAG 2.2 target size minimum of 24x24 CSS px (see the mobile section). — [DAISY KB](https://kb.daisy.org/publishing/docs/wcag/target-size-minimum.html)
- **[Tested, older classic]** Auto-advancing carousels are particularly hard for slower readers and users with motor difficulties. — [Yale Usability](https://usability.yale.edu/usability-best-practices/hero-imagescarousels); [UMBC FAQ](https://umbc.atlassian.net/wiki/spaces/faq/pages/30762196/Why+don+t+Slideshows+Auto-rotate)

### Inferences
- Product cards need descriptive alt text (brand, item, colour), real link text rather than "click here" (e.g. "View Levi's 501 jeans, size 32, on Square"), sufficient contrast for price and size text, especially over images, visible focus states, and no auto-motion. These fixes also address the most common failures in the WebAIM data.

### Gaps
- No controlled A/B test directly linking accessibility fixes to conversion lift was found. The Click-Away Pound data is self-reported survey data (UK).
