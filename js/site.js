// Velocity Shop: filters and "Show more" for the shop, category tiles, back photos on hover, entrances.
// Every product is already in the HTML; this only shows, hides and reveals what is there.
(function () {
  'use strict';
  document.documentElement.classList.add('js');
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var PAGE = 24;
  var still = window.matchMedia('(prefers-reduced-motion: reduce)');
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');

  // ---------- Entrances (content is visible without script) ----------
  var reveals = $$('.sec-head, .cats-head, .why-text, .about-text, .faq-head, .final > *');
  reveals.forEach(function (el) { el.classList.add('reveal'); });
  if ('IntersectionObserver' in window && !still.matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px 15% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  // ---------- Product cards rise in as they come into view ----------
  if ('IntersectionObserver' in window && !still.matches) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); cio.unobserve(en.target); } });
    }, { rootMargin: '0px 0px 15% 0px' });
    $$('.card, .cat-grid > li, .step').forEach(function (c, i) { c.classList.add('rise'); c.style.setProperty('--d', (i % 4) * 50 + 'ms'); cio.observe(c); });
  }

  // ---------- Back photo: created on first hover or focus, so unseen photos never download ----------
  function wake(e) {
    var a = e.target.closest && e.target.closest('.card a[data-back]');
    if (!a) return;
    var back = new Image();
    back.className = 'back'; back.alt = ''; back.width = 560; back.height = 560; back.decoding = 'async';
    back.src = a.getAttribute('data-back');
    a.removeAttribute('data-back');
    a.querySelector('.pic').appendChild(back);
  }
  if (finePointer.matches) {
    document.addEventListener('pointerover', wake);
    document.addEventListener('focusin', wake);
  }

  // ---------- The shop ----------
  var grid = $('#grid');
  if (!grid) return;
  var cards = $$('.card', grid);
  var fCat = $('#f-cat'), fSize = $('#f-size'), fPrice = $('#f-price');
  var count = $('#f-count'), more = $('#more'), none = $('#none');
  var shown = PAGE;
  var price = function (c) { return parseFloat(c.querySelector('.price').textContent.replace(/[^0-9.]/g, '')); };

  function matches(c) {
    return (!fCat.value || c.getAttribute('data-cat') === fCat.value) &&
           (!fSize.value || c.getAttribute('data-size') === fSize.value) &&
           (!fPrice.value || price(c) < Number(fPrice.value));
  }
  function render(animateFrom) {
    var hits = cards.filter(matches);
    cards.forEach(function (c) { c.hidden = true; c.classList.remove('is-new'); });
    hits.slice(0, shown).forEach(function (c, i) {
      c.hidden = false;
      if (animateFrom != null && i >= animateFrom && !still.matches) c.classList.add('is-new');
    });
    var filtered = fCat.value || fSize.value || fPrice.value;
    count.textContent = hits.length ? 'Showing ' + Math.min(shown, hits.length) + ' of ' + hits.length + (filtered ? ' matching' : '') : 'No matches';
    more.parentNode.hidden = hits.length <= shown;
    more.textContent = 'Show ' + Math.min(PAGE, hits.length - shown) + ' more';
    none.hidden = hits.length > 0;
    return hits;
  }
  function filter() { shown = PAGE; render(null); }
  [fCat, fSize, fPrice].forEach(function (s) { s.addEventListener('change', filter); });
  $('#reset').addEventListener('click', function () { fCat.value = ''; fSize.value = ''; fPrice.value = ''; filter(); fCat.focus(); });
  more.addEventListener('click', function () {
    var from = shown;
    shown += PAGE;
    var hits = render(from);
    var next = hits[from] && hits[from].querySelector('a');
    if (next) next.focus({ preventScroll: true });
  });
  // Category tiles set the filter, then the link jumps to the shop.
  $$('.cat[data-cat]').forEach(function (a) {
    a.addEventListener('click', function () { fCat.value = a.getAttribute('data-cat'); fSize.value = ''; fPrice.value = ''; filter(); });
  });
  render(null);
})();
