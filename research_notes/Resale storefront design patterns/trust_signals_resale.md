# Trust signals, policy messaging and social proof for online resale clothing stores

Method note: Done 2026-10-28. Direct fetches of baymard.com, nngroup.com and realstyle.therealreal.com failed: those hosts are outside this session's allowed network domains. Findings for those sites come from search-result snippets and secondary write-ups, and they are labelled as such. Vendor or marketing claims are marked **[vendor claim]**.

## 1. How do resale stores present shipping speed and cost, return windows and conditions, and where on the page?

### Takeaway
Shoppers look for shipping cost and the return policy on the product page, before they add to cart. Costs that show up late are the top reason for abandoning checkout. A small resale seller should state shipping cost and speed, the return window and any final-sale exceptions in three places: a header bar, next to the Buy button, and on a full policy page. These statements should be short and match each other.

### Cited Findings
- Baymard testing: 64% of users looked for shipping costs on the product page before deciding to add to cart. Product pages that showed a shipping estimate somewhere on the page outperformed pages that showed none. (Baymard article reached via search snippet only, not fetched.) — [Baymard: Show shipping costs on product pages](https://baymard.com/blog/show-shipping-costs-on-product-pages)
- Baymard 2025 abandonment reasons, as reported second-hand. Of non-browsing abandonments: 39% left because extra costs (shipping, tax, fees) were too high, 21% because delivery was too slow, 19% because they didn't trust the site with card info, 19% because account creation was forced, 15% because the returns policy was unsatisfactory, and 14% because they couldn't see the total cost up front. Average cart abandonment is about 70.19%. — [Baymard: reduce cart abandonment](https://baymard.com/blog/reduce-cart-abandonment); [Shoplazza summary](https://www.shoplazza.com/blog/how-to-reduce-shopping-cart-abandonment?hs_amp=true); [eDesk summary](https://www.edesk.com/blog/shopping-cart-abandonment)
  - Conflict: some write-ups quote 48% for extra costs, 26% for account creation and 25% for payment trust. These look like earlier editions or a different base. Use the 2025 figures above and attribute them to Baymard. — [Really Good Designs](https://reallygooddesigns.com/checkout-page-design/)
- Baymard's own 2025 checkout article gives the "didn't trust the site with their credit card information" figure as 19%, from 1,026 US respondents. — [Baymard: perceived security of payment form](https://baymard.com/blog/perceived-security-of-payment-form) (snippet only)
- A secondary summary attributed to Baymard says 60% of users expect to find the return policy on the product page and 44% of sites don't provide it there. I could not verify this against Baymard's own pages. — [Shoplazza summary](https://www.shoplazza.com/blog/how-to-reduce-shopping-cart-abandonment?hs_amp=true)
- NN/g's long-standing trust framework names four factors: design quality, up-front disclosure, comprehensive and current content, and connection to the rest of the web. NN/g says users appreciate sites that are up front about everything affecting the customer experience, such as what is included in a base cost. (Snippet only, not fetched.) — [NN/g: Trustworthy design](https://nngroup.com/articles/trustworthy-design/)
- ThredUp's official help center: original shipping is not refunded, final-sale items can't be returned, and orders paid with store credit are refunded as store credit. Prepaid return labels are only for the 48 contiguous states. — [ThredUp help: return policy](https://help.thredup.com/en_us/what-is-thredup-s-return-policy-HJjbVX1jn.md)
  - Third-party guides add a 14-day window (postmarked within 14 days of delivery), a requirement that the barcode tag stay attached, and fees of $1.99 restocking and $8.99 return shipping. These fees are unverified and may conflict with the official page. — [topbubbleindex](https://www.topbubbleindex.com/blog/thredup-returns/); [thereturnguide](https://thereturnguide.com/blogs/online-retailers-returns/thredup-return-policy)
- Patagonia Worn Wear applies its Ironclad Guarantee to used items: if you're not satisfied when you receive a product, or it doesn't perform, email info@wornwear.com. — [Worn Wear product page](https://wornwear.patagonia.com/products/ws-merino-waffle-crew_50535_rstp)
- Trustpilot reviews of ThredUp show frequent complaints about the return policy. This is anecdotal. — [Trustpilot ThredUp](https://ie.trustpilot.com/review/thredup.com?page=5)

### Inferences
- For a small seller, the most useful placements are:
  1. A one-line header or announcement bar with the actual shipping rule, for example "Ships in X business days · $Y flat / free over $Z".
  2. Two or three lines directly under the Buy button: shipping cost and speed, the returns summary, and a link to the full policy.
  3. A full policies page linked from the footer and from the checkout handoff.
- Product cards usually don't carry policy text. They carry price, size, condition and sold state.
- The 14% "couldn't see total cost up front" figure matters for a Square handoff. If shipping is calculated only inside Square checkout, the shopper meets it late. Stating a flat rate on the site addresses this.
- Resale norms leave room to be honest about limits, such as final-sale exceptions, return shipping paid by the buyer, or store-credit refunds. ThredUp and others restrict returns openly. What matters is that the limits are stated before purchase, not that the policy is generous.

### Gaps
- I couldn't fetch Baymard's or NN/g's primary pages, so the figures come from snippets and secondary write-ups.
- I found no research specifically on header-bar versus near-CTA placement for resale.
- I didn't verify the return windows of The RealReal, Vestiaire, Depop or Grailed.

## 2. Condition grading: scales used and how condition is shown on cards and detail pages; the simplest honest alternative

### Takeaway
Most platforms use a 3 to 5 tier verbal scale, roughly New with tags, Excellent/Like new, Very good, Good, Fair/As is. Each tier comes with a short definition and examples of flaws, and the flaws themselves must be shown. A seller who doesn't grade every item can use eBay's three-tier "Pre-owned - Excellent / Good / Fair" model, or label everything "Pre-owned" and list and photograph each flaw. The definitions should sit on a condition-guide page.

### Cited Findings
- **eBay (pre-owned apparel, US since 4 Feb 2025):** three grades replaced the generic "Pre-owned".
  - Pre-owned - Excellent: worn but like new, little to no signs of wear; any wear must still be disclosed.
  - Pre-owned - Good: gently used, a few signs of wear, and all imperfections should be shown and described in the listing.
  - Pre-owned - Fair: significant visible flaws, heavy wear, and/or missing or damaged components.
  - Existing "Pre-owned" clothing listings were moved to "Pre-owned - Good" automatically. eBay Australia extended the grades to handbags and some accessories from 22 Jul 2025.
  - Sources: [eBay.ca announcement](https://community.ebay.ca/t5/Announcements/Introducing-new-conditions-for-pre-loved-clothing/ba-p/515845); [Value Added Resource](https://www.valueaddedresource.net/ebay-pre-loved-fashion-conditions-2025-updates/); [eBay AU seller news](https://www.ebay.com.au/sellercentre/aussie-seller-news/april-2025/plf-conditions-grading); [eBay developer condition IDs](https://developer.ebay.com/api-docs/sell/static/metadata/condition-id-values.html)
- **The RealReal:**
  - Pristine: no signs of wear, tags attached (jewelry exempt from tags).
  - Excellent: perfect condition, no tags.
  - Very Good: for example slight fabric lightening, small stains or snags, slightly worn handbag corners.
  - Good: more prominent wear such as fading, stains and snags.
  - Fair: the bottom of its standards.
  - Product listings also show "As Is" below Fair.
  - Primary page not fetchable; based on search snippets. — [TRR RealStyle: condition in luxury resale](https://realstyle.therealreal.com/condition-in-luxury-resale/); [TRR consign page](https://therealreal.com/TRR/SELLITFORWARD)
- **Patagonia Worn Wear:** three grades, each defined on every product page.
  - Excellent: look and feel barely worn.
  - Great: minor signs of wear.
  - Good: visible repair marks and normal wear from adventures.
  - Examples listed include discoloration, scratches, fading and pilling. Some listings also have item-specific condition notes.
  - Source: [Worn Wear product page](https://wornwear.patagonia.com/products/half-mass_48274_bch)
- **ThredUp:** product pages show a condition label such as "Very Good Condition". I could not find ThredUp's official grade definitions; third-party descriptions vary and are unreliable. — [ThredUp product page example](https://www.thredup.com/product/women-madewell-blue-jeans/227983051); [blog review](https://elisabethmcknight.com/is-thredup-legit/)
- **Vestiaire Collective:** a seller guide says Vestiaire applies its own grading rather than letting sellers pick freely. Vestiaire's FAQ says lingerie and swimwear listed as Good or Fair are rejected at verification. Forum buyers report "very good" items arriving with more wear than expected. These reports are anecdotal. — [Vendoo seller guide](https://uk.blog.vendoo.co/how-does-vestiaire-collective-work-for-sellers); [Vestiaire FAQ](https://faq.vestiairecollective.com/hc/en-gb/articles/16480403093393); [PurseForum thread](https://forum.purseblog.com/threads/vestiaire-collective-experiences.770874/page-91)
- **Grailed:** four buckets: New/Not worn, Gently used, Used, Very worn. The definitions come from a third-party scraper's documentation, not from Grailed: deadstock or new with tags; minimal signs of wear; moderate signs of wear; heavily worn or distressed. — [Apify Grailed scraper](https://apify.com/solidcode/grailed-scraper)
- **Vintage sellers:**
  - One shop lists every specific flaw, grades conservatively on subjective flaws, and rates condition separately from rarity. — [Vintage Vixen](https://www.vintagevixen.com/pages/grading-condition-of-vintage-clothing)
  - A shirt reseller uses a 10-point scale where 10 is new or mint and stocks only 7.5 and up. — [Casual Football Shirts](https://casualfootballshirts.co.uk/blogs/shirts/vintage-shirt-condition-guide)
  - An "As Is" tier is used for heavily worn, stained or repaired items. — [Vinnies](https://vinniesfinds.com.au/pages/size-guide)
  - A seller guide advises photographing condition issues and contacting the buyer before shipping if a flaw was missed. — [Defunkd](https://www.defunkd.com/blog/2014/06/08/grading-and-measuring/)
- Buyer hesitation: a small pulse survey (n=137, by Echo Group, not ThredUp) found 20% chose "concerned about quality and hygiene" as their main reaction to secondhand clothing. Treat it with caution given the sample size. — [Echo Group](https://www.echogroup.ai/articles/81b9f682-a59a-4475-83a6-7c4664322388)

### Inferences
- Cards versus detail pages: the observed pattern is a short condition label on the card or near the price ("Very Good Condition", "Pre-owned - Good"). The detail page holds the definition, often a tooltip or link to a condition guide (Patagonia puts it inline), plus item-specific condition notes.
- Simplest honest alternative for a seller who doesn't formally grade: adopt eBay's three-tier vocabulary, which shoppers already know. If even that isn't feasible:
  - label everything "Pre-owned";
  - add a per-item line such as "Flaws: none found" or "Flaws: small mark on left cuff (photo 4)";
  - add a site-wide statement such as "Every item is checked and any flaws we find are listed and photographed".
- Never use "like new" or "excellent" unless the item really meets it. Vestiaire forum complaints show that grade inflation is the main trust failure.

### Gaps
- ThredUp's official condition definitions were not found.
- Grailed's official wording was not found; only a third-party mapping.
- I didn't verify Depop's condition fields.

## 3. Authenticity guarantees, "quality checked" processes, and real photography

### Takeaway
Large platforms build trust by publishing their process: who checks items, how and how often. The process itself is the trust signal. A small seller can't claim formal authentication, but can honestly describe what it does check and show real photos of each item, including flaws.

### Cited Findings
- Vestiaire's Trust Report says every piece is checked physically or digitally by at least one expert **[vendor claim]**.
  - Its FAQ says items are screened digitally before listing, and about 8% are filtered out. Physical authentication happens only if the buyer adds authentication and quality control to the order.
  - Vestiaire reports 60 authenticators, two months of initial training and 180 hours of training per year **[vendor claim]**.
  - Sources: [Marks & Clerk on Vestiaire Trust Report 2022](https://www.marks-clerk.com/insights/latest-insights/102i0zy-vestiaire-collectives-trust-report-2022/); [Vestiaire FAQ: how authentic are items](https://faq.vestiairecollective.com/hc/en-gb/articles/16329420537745-Buyer-How-authentic-are-items-on-Vestiaire-Collective); [Grazia](https://graziamagazine.com/articles/for-vestiaire-collective-authentication-is-the-real-deal/)
- A 2026 comparison says Fashionphile, The RealReal and Vestiaire all authenticate high-value items in-house and offer authenticity guarantees. The qualifier "high value" means not every item gets the same scrutiny. — [ShopBack comparison 2026](https://www.shopback.com/blog/fashion/us-preloved-luxury-vestiaire-vs-fashionphile-vs-the-realreal-2026)
- eBay's Pre-owned - Good definition requires that all imperfections be shown and described, which makes flaw photos a platform norm. — [eBay.ca](https://community.ebay.ca/t5/Announcements/Introducing-new-conditions-for-pre-loved-clothing/ba-p/515845)

### Inferences
- A small seller should not use the words "authenticated" or "guaranteed authentic" unless it has a real process and remedy behind them.
- Honest substitutes:
  - "Every item is inspected, measured and photographed by us."
  - "Photos are of the actual item."
  - "Flaws are listed and pictured."
  - "If it's not as described, contact us within X days."
- Recommended photo set per item: front, back, label or tag, close-up of fabric, and every flaw. Add flat-lay measurements in the description to reduce sizing anxiety.

### Gaps
- I found no controlled study isolating the effect of flaw photos on conversion or returns in resale.
- The RealReal's per-item inspection rules were not verified.

## 4. Social proof without on-site reviews: what's ethical and effective, and what must never be faked

### Takeaway
Reviews strongly affect purchase likelihood, and the effect is largest for the first few reviews and for higher-priced items. A small seller without on-site reviews can link to real off-site reputation, such as an eBay feedback profile, Google Business reviews or Instagram. US law (the FTC rule effective October 2024) makes fake or cherry-picked reviews, misrepresented testimonials and fake follower or engagement metrics risky. Show real counts with links to verify them.

### Cited Findings
- Spiegel Research Center (Northwestern) with PowerReviews:
  - Purchase likelihood for a product with five reviews is 270% greater than for one with none.
  - Showing reviews lifted conversion 190% for lower-priced and 380% for higher-priced products.
  - Marginal benefit falls sharply after the first five reviews.
  - Purchase likelihood peaks at 4.0 to 4.7 stars and declines toward 5.0.
  - The data came from three retailers, including a high-end gift retailer, and dates from 2017.
  - Source: [Spiegel: How Online Reviews Influence Sales](https://spiegel.medill.northwestern.edu/How-Online-Reviews-Influence-Sales)
- The FTC final rule on fake reviews was announced 14 Aug 2024 and effective about 21 Oct 2024. It bans:
  - fake reviews and testimonials, including AI-generated ones;
  - buying positive or negative reviews;
  - undisclosed insider reviews;
  - suppressing negative reviews;
  - buying or selling fake indicators of social media influence, such as followers or views, where the buyer knew or should have known they were fake and uses them commercially.
  - Civil penalties are about $51,744 per violation, adjusted for inflation.
  - Sources: [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials); [Davis Wright Tremaine](https://dwt.com/insights/2024/08/ftc-finalizes-rule-banning-fake-consumer-reviews); [Manatt](https://manatt.com/insights/newsletters/client-alert/ftc-issues-final-rule-banning-fake-reviews-and-tes)
- Enforcement precedent: Fashion Nova paid $4.2M in 2022 over allegedly hiding reviews below four stars. The FTC also settled with Hey Dude over allegedly suppressing 1 to 3 star reviews. — [Olshan Law](https://www.olshanlaw.com/Advertising-Law-Blog/alert-to-ecommerce-marketers-suppressing-negative-reviews-can-lead); [UNC JOLT](https://journals.law.unc.edu/ncjolt/?p=8598)
- NN/g lists "connection to the rest of the web" as a trust factor, which supports linking out to verifiable third-party profiles. (Snippet only.) — [NN/g: Trustworthy design](https://nngroup.com/articles/trustworthy-design/)

### Inferences
- Ethical and effective options:
  - A "See our eBay feedback" link showing the real percentage and count, plus a date.
  - A Google review rating that links to the live listing.
  - An Instagram handle and feed.
  - A real "Sold" state on items that have actually sold, which shows turnover.
  - A few verbatim buyer quotes with a source and date, and permission where needed.
- Never fake or inflate any of these: reviews, star ratings, review or sold counts, follower numbers, "X people viewing", urgency timers, "only 1 left" on items that aren't unique, or badges for services not actually used.
- Don't show only the 5-star quotes while implying they represent all reviews.
- Because each resale item is unique, "1 of 1" or "only one available" is true and needs no false urgency.

### Gaps
- I found no study measuring the conversion effect of off-site review links, such as an eBay feedback link, compared with on-site reviews.
- I didn't verify current FTC litigation or amendments to the rule after 2024.

## 5. Payment trust: messaging about secure third-party checkout, payment icons, and the evidence on trust badges

### Takeaway
How secure a page feels is driven mostly by how secure it looks and by recognizable brand names. Badges from names shoppers know beat unfamiliar ones. Published conversion lifts from trust badges are mostly vendor case studies with bundled changes, so they are weak evidence. For a Square checkout, the honest and effective message is a factual line such as "Secure checkout by Square — we never see or store your card details", with accepted-payment icons, placed next to the Buy button and in the footer.

### Cited Findings
- Baymard (snippets; pages not fetchable):
  - Users judge security by gut feeling, which is largely driven by how visually secure the page looks.
  - Users see some parts of a page as more secure than others, for example card fields that are visually enclosed.
  - Adding any seal raised perceived security, including a generic seal made by the researchers.
  - Sources: [Baymard: perceived security of payment form](https://baymard.com/blog/perceived-security-of-payment-form); [Baymard: site seal trust](https://baymard.com/blog/site-seal-trust)
- Baymard's 2013/2016 seal survey:
  - Norton about 36%, McAfee about 23%, TRUSTe and BBB about 13% each, after excluding "don't know". 49% chose "Don't know / no preference".
  - These are dated preference data, not conversion data. Respondent counts differ across secondary sources.
  - A secondary blog claims a later Baymard test found a made-up padlock seal beat real vendors; this is unverified.
  - Sources: [OpenSRS summary](https://opensrs.com/blog/which-site-seal-do-people-trust-the-most-2013-survey-results); [TrustSignals blog](https://www.trustsignals.com/blog/trust-badges-work-and-we-have-the-receipts-to-prove-it) **[vendor of seals]**
- CXL eye-tracking study of six trust badges on a checkout page:
  - Viewing patterns were similar across all badge variants.
  - The PayPal badge drew the most attention; McAfee the least.
  - Google, Norton and PayPal were most often recalled as adding security.
  - The study measured attention and recall, not conversion.
  - Source: [CXL research study: checkout optimization](https://conversionxl.com/research-study/checkout-optimization/)
- Vendor conversion claims (weak evidence):
  - VWO reported a 32% lift in visits to the payment page, from a test that changed the CTA text, colors and badges together (6,585 visitors, 3 weeks), so badges weren't isolated **[vendor claim]**. — [VWO](https://vwo.com/blog/32-increase-in-conversions-by-ab-testing-for-the-right-reasons)
  - Searchbloom reported a 12.6% conversion lift after adding badges and card logos **[vendor claim]**. — [Searchbloom](https://searchbloom.com/?p=30712)
  - The "up to 32–42% sales" figure appears without a named source. — [Exotel](https://exotel.com/blog/trust-badges-conversion-rates/)
- Square's own statements **[vendor claim]**:
  - Its products and online payment APIs are PCI-DSS compliant, and Square takes on the compliance burden.
  - Payments are encrypted so unencrypted card data never touches the seller's device or app.
  - A Square-hosted checkout is available.
  - I did not find Square explicitly saying card data is never stored.
  - Sources: [Square secure payments (GB)](https://squareup.com/gb/en/payments/secure); [Square Developer online payments](https://developer.squareup.com/au/en/online-payment-apis)

### Inferences
- With Square-hosted checkout, the seller's site never handles card data. The truthful copy is "Payments are processed securely by Square. We never see your full card number." Avoid "we never store" claims about Square itself unless verified.
- Use real card and wallet icons only for methods Square actually accepts on this store.
- Don't use a generic padlock or "100% Secure" seal that isn't backed by anything. Baymard's finding that fake seals work is a reason for caution, not permission.
- Place the line where card anxiety arises: under the Buy button and on the cart or handoff, not only in the footer.
- When the shopper leaves for Square, say so before the redirect ("You'll complete payment on Square's secure checkout"). That way the domain change doesn't feel like a red flag. This is an inference; no source tested it.

### Gaps
- I couldn't access Baymard's full 2022 seal-test results or its payment-form research.
- I found no independent, isolated A/B test of badges alone that reported a conversion effect.
- I found no research on whether the Square brand specifically is recognized or trusted by shoppers, compared with PayPal or Shop Pay.
