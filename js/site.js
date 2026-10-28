// Velocity Shop: filters and "Show more" for the sheet, the category index, the How it works row and entrances.
// Every product is already in the HTML; this only shows, hides and orders what is there.
(function () {
  'use strict';
  document.documentElement.classList.add('js');
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var PAGE = 24;
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  var still = window.matchMedia('(prefers-reduced-motion: reduce)');

  // ---------- Entrances (content is visible without script) ----------
  var watch = $$('.reveal, .card-big');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px 15% 0px' });
    watch.forEach(function (el) { io.observe(el); });
  } else {
    watch.forEach(function (el) { el.classList.add('is-in'); });
  }

  // ---------- The shop ----------
  var grid = $('#grid');
  if (!grid) return;
  var cards = $$('.card', grid);
  var fCat = $('#f-cat'), fSize = $('#f-size'), count = $('#f-count'), more = $('#more'), none = $('#none');
  var shown = PAGE;

  function matches(card) {
    return (!fCat.value || card.getAttribute('data-cat') === fCat.value) &&
           (!fSize.value || card.getAttribute('data-size') === fSize.value);
  }
  function render(animateFrom) {
    var hits = cards.filter(matches);
    cards.forEach(function (c) { c.hidden = true; c.classList.remove('is-new'); });
    hits.slice(0, shown).forEach(function (c, i) {
      c.hidden = false;
      if (animateFrom != null && i >= animateFrom) c.classList.add('is-new');
    });
    // The big frame belongs to the unfiltered sheet only.
    cards[0].classList.toggle('card-big', !fCat.value && !fSize.value);
    var n = Math.min(shown, hits.length);
    count.textContent = hits.length ? 'Showing ' + n + ' of ' + hits.length + (fCat.value || fSize.value ? ' matching' : '') : 'No matches';
    more.hidden = hits.length <= shown;
    more.textContent = 'Show ' + Math.min(PAGE, hits.length - shown) + ' more';
    none.hidden = hits.length > 0;
    return hits;
  }
  function filter() { shown = PAGE; render(null); }
  fCat.addEventListener('change', filter);
  fSize.addEventListener('change', filter);
  $('#reset').addEventListener('click', function () { fCat.value = ''; fSize.value = ''; filter(); fCat.focus(); });
  more.addEventListener('click', function () {
    var from = shown;
    shown += PAGE;
    var hits = render(from);
    // Keyboard users carry on from the first new piece.
    var next = hits[from] && hits[from].querySelector('a');
    if (next) next.focus({ preventScroll: true });
  });
  // Links in the category index set the matching filter, then jump to the shop.
  function applyFrom(el) {
    var cat = el.getAttribute('data-cat'), size = el.getAttribute('data-size');
    if (cat != null) { fCat.value = cat; fSize.value = ''; }
    if (size != null) { fSize.value = size; fCat.value = ''; }
    filter();
  }
  $$('.index-col a').forEach(function (a) {
    a.addEventListener('click', function () { applyFrom(a); });
  });

  // The back photo downloads only when someone points at or tabs to a piece.
  function wake(e) {
    var a = e.target.closest && e.target.closest('.card a');
    if (!a || !a.hasAttribute('data-back')) return;
    var back = new Image();
    back.className = 'back';
    back.alt = '';
    back.width = 560; back.height = 560;
    back.decoding = 'async';
    back.src = a.getAttribute('data-back');
    a.removeAttribute('data-back');
    a.querySelector('.pic').appendChild(back);
  }
  if (finePointer.matches) {
    grid.addEventListener('pointerover', wake);
    grid.addEventListener('focusin', wake);
  }

  render(null);

  // ---------- Category index: hovering a name shows what is in it ----------
  var desc = $('#index-desc');
  if (desc) {
    $$('.index-col a').forEach(function (a) {
      var show = function () { desc.textContent = a.getAttribute('data-desc'); };
      a.addEventListener('pointerenter', show);
      a.addEventListener('focus', show);
    });
  }

  // ---------- Pieces in the sheet rise in as they come into view ----------
  if ('IntersectionObserver' in window && !still.matches) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); cio.unobserve(en.target); } });
    }, { rootMargin: '0px 0px 15% 0px' });
    cards.forEach(function (c, i) { c.style.setProperty('--d', (i % 5) * 40 + 'ms'); cio.observe(c); });
  }
})();
