// Velocity Shop: the hero deck, filters on Shop all, back photos on hover, entrances.
// Every product is already in the HTML; this only shows, hides and reveals what is there.
(function () {
  'use strict';
  document.documentElement.classList.add('js');
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
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

  // ---------- Hero deck: every 2 seconds the top piece is dealt off and tucked under the pile ----------
  var deck = $('#deck');
  if (deck && !still.matches) {
    var order = $$('.deck-card', deck);
    var pause = $('#deck-pause');
    var paused = false, held = false, timer = null;
    var place = function () {
      order.forEach(function (c, i) {
        c.style.setProperty('--p', i);
        if (i) { c.setAttribute('tabindex', '-1'); c.setAttribute('aria-hidden', 'true'); }
        else { c.removeAttribute('tabindex'); c.removeAttribute('aria-hidden'); }
      });
    };
    var deal = function () {
      if (paused || held || document.hidden) return;
      var top = order[0];
      top.classList.add('is-dealt');
      setTimeout(function () {
        order.push(order.shift());
        place();
        top.classList.remove('is-dealt');
      }, 280);
    };
    var start = function () { if (!timer) timer = setInterval(deal, 2000); };
    var hold = function (on) { held = on; };
    deck.addEventListener('pointerenter', function () { hold(true); });
    deck.addEventListener('pointerleave', function () { hold(false); });
    deck.addEventListener('focusin', function () { hold(true); });
    deck.addEventListener('focusout', function () { hold(false); });
    pause.hidden = false;
    pause.addEventListener('click', function () {
      paused = !paused;
      pause.setAttribute('aria-pressed', String(paused));
      pause.textContent = paused ? 'Play' : 'Pause';
    });
    // Only deal while the deck is on screen.
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        if (en[0].isIntersecting) start(); else { clearInterval(timer); timer = null; }
      }).observe(deck);
    } else start();
  }

  // ---------- Shop all: filters, read from and written to the address (?cat=tees) ----------
  var grid = $('#grid');
  if (!grid) return;
  var cards = $$('.card', grid);
  var fCat = $('#f-cat'), fSize = $('#f-size'), fPrice = $('#f-price');
  var count = $('#f-count'), none = $('#none');
  var price = function (c) { return parseFloat(c.querySelector('.price').textContent.replace(/[^0-9.]/g, '')); };
  var params = new URLSearchParams(location.search);
  [['cat', fCat], ['size', fSize], ['price', fPrice]].forEach(function (p) {
    var v = params.get(p[0]);
    if (v && $$('option', p[1]).some(function (o) { return o.value === v; })) p[1].value = v;
  });

  function matches(c) {
    return (!fCat.value || c.getAttribute('data-cat') === fCat.value) &&
           (!fSize.value || c.getAttribute('data-size') === fSize.value) &&
           (!fPrice.value || price(c) < Number(fPrice.value));
  }
  function render() {
    var hits = 0;
    cards.forEach(function (c) { var on = matches(c); c.hidden = !on; if (on) hits++; });
    var filtered = fCat.value || fSize.value || fPrice.value;
    count.textContent = hits ? (filtered ? hits + ' of ' + cards.length + ' pieces' : cards.length + ' pieces') : 'No matches';
    none.hidden = hits > 0;
    var q = new URLSearchParams();
    if (fCat.value) q.set('cat', fCat.value);
    if (fSize.value) q.set('size', fSize.value);
    if (fPrice.value) q.set('price', fPrice.value);
    var qs = q.toString();
    history.replaceState(null, '', location.pathname + (qs ? '?' + qs : ''));
  }
  [fCat, fSize, fPrice].forEach(function (s) { s.addEventListener('change', function () { render(); window.scrollTo({ top: 0 }); }); });
  $('#reset').addEventListener('click', function () { fCat.value = ''; fSize.value = ''; fPrice.value = ''; render(); fCat.focus(); });
  render();
})();
