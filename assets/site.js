// Velocity Shop landing page: the hanger on the stage, Find your size and the rail counts.
// Everything here reads /rack/rack.json and /rack/images.json, the same files the rack page and the Square sync use.
(function () {
  'use strict';
  document.documentElement.classList.add('js');

  var UTM = 'utm_source=velocityshop.github.io&utm_medium=referral&utm_campaign=landing';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var year = $('#year');
  if (year) year.textContent = String(new Date().getFullYear());

  function tagUrl(url, slot) {
    return url + (url.indexOf('?') < 0 ? '?' : '&') + UTM + '&utm_content=' + encodeURIComponent(slot);
  }
  function pieceKey(id) { return String(id).replace(/[^a-z0-9]/gi, '').slice(-6).toLowerCase(); }
  // The same piece links the rack makes: /rack/#<name>-<last six of the Square id>
  function rackHref(item) {
    var s = String(item.name).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
    if (s.length > 48) s = s.slice(0, 48).replace(/-[^-]*$/, '');
    return '/rack/#' + (s ? s + '-' : '') + pieceKey(item.id);
  }
  function money(p) { var n = Number(p); return isFinite(n) && n > 0 ? '$' + (n % 1 ? n.toFixed(2) : String(n)) : ''; }

  // Size groups for the chips. Jeans are listed by waist (33, 38×32), dress shirts by neck (14.5, 15.5).
  function group(size) {
    var s = String(size || '').trim().toUpperCase();
    if (!s) return '';
    if (/^(XS|S|M|L|XL|XXL)$/.test(s)) return s;
    if (s.indexOf('×') > -1 || s.indexOf('X') > 0) return 'waist';
    var n = parseFloat(s);
    if (isFinite(n)) return n < 20 ? 'neck' : 'waist';
    return '';
  }
  function tagClass(size) {
    var g = group(size);
    return g === 'waist' ? 'sz-denim' : g ? 'sz-' + g.toLowerCase() : 'sz-neck';
  }

  // ---------- Entrances: content is visible without script; this only adds the rise ----------
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window && !reduce.matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px' });
    reveals.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight) el.classList.add('is-in'); else io.observe(el);
    });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  // ---------- The stage ----------
  function figureFor(item, im, eager) {
    var fig = document.createElement('figure');
    fig.className = 'layer';
    var g = document.createElement('div');
    g.className = 'garment';
    g.style.setProperty('--r', (im.w / im.h).toFixed(4));
    var img = new Image();
    img.width = im.w; img.height = im.h;
    img.decoding = 'async';
    if (!eager) img.loading = 'lazy';
    img.alt = 'Front of the ' + item.name + ', size ' + (item.size || 'one size') + (money(item.price) ? ', ' + money(item.price) + ' CAD' : '') + '.';
    img.src = '/rack/' + im.front;
    g.appendChild(img);
    if (item.size || item.price) {
      var tag = document.createElement('div');
      var label = item.size ? String(item.size) : '';
      tag.className = 'tag ' + tagClass(item.size);
      tag.setAttribute('aria-hidden', 'true');
      tag.innerHTML = '<div class="tag-card"><span class="tag-label">SIZE</span><span class="tag-size' + (label.length > 3 ? ' long' : '') + '"></span><span class="tag-rule"></span><span class="tag-price"></span><span class="tag-cur">CAD</span></div>';
      $('.tag-size', tag).textContent = label || '—';
      $('.tag-price', tag).textContent = money(item.price);
      g.appendChild(tag);
    }
    fig.appendChild(g);
    return fig;
  }

  function Stage(layersEl, captionEl) {
    this.layers = layersEl;
    this.caption = captionEl;
    this.list = [];
    this.i = -1;
    this.timer = 0;
    this.paused = false;
  }
  Stage.prototype.show = function (item, im) {
    var fig = figureFor(item, im, this.i < 0);
    var layers = this.layers;
    layers.appendChild(fig);
    var swap = function () {
      requestAnimationFrame(function () {
        $$('.layer.is-on', layers).forEach(function (old) {
          old.classList.remove('is-on');
          setTimeout(function () { if (old.parentNode && !old.classList.contains('is-on')) old.remove(); }, 320);
        });
        fig.classList.add('is-on');
      });
    };
    var img = $('img', fig);
    if (img.complete) swap(); else { img.addEventListener('load', swap, { once: true }); img.addEventListener('error', swap, { once: true }); }
    if (this.caption) {
      var name = document.createElement('p');
      name.className = 'stage-name';
      name.textContent = item.name;
      var links = document.createElement('p');
      links.className = 'stage-links';
      links.innerHTML = '<a target="_blank" rel="noopener">See it on Square <span aria-hidden="true">↗</span><span class="vh"> (opens in a new tab)</span></a><a>Find it on the rack</a>';
      var a = $$('a', links);
      a[0].href = tagUrl(item.link, 'stage');
      a[1].href = rackHref(item);
      this.caption.replaceChildren(name, links);
    }
  };
  Stage.prototype.play = function (list, images, start) {
    this.list = list;
    this.images = images;
    this.i = -1;
    this.next(start || 0);
  };
  Stage.prototype.next = function (to) {
    clearTimeout(this.timer);
    if (!this.list.length) return;
    var j = typeof to === 'number' ? to : (this.i + 1) % this.list.length;
    var item = this.list[j];
    this.show(item, this.images[item.photo]);
    this.i = j;
    this.schedule();
  };
  Stage.prototype.schedule = function () {
    var self = this;
    clearTimeout(this.timer);
    if (reduce.matches || this.list.length < 2) return;
    this.timer = setTimeout(function () {
      if (self.paused || document.hidden) self.schedule(); else self.next();
    }, 4200);
  };

  // ---------- Data ----------
  Promise.all([
    fetch('/rack/rack.json').then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }),
    fetch('/rack/images.json').then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
  ]).then(function (res) { start(res[0], res[1]); }).catch(function () { /* the page reads fine without the live parts */ });

  function start(config, images) {
    var items = (config.items || []).filter(function (it) { return it && it.link && /^https:\/\//.test(it.link); });
    var shown = items.filter(function (it) { return it.photo && images[it.photo]; });

    // Newest first, so the stage opens on what just went up.
    shown.sort(function (a, b) { return String(b.added || '').localeCompare(String(a.added || '')); });

    var stage = new Stage($('#stage-layers'), $('#stage-caption'));
    var stageEl = $('#stage');
    stageEl.addEventListener('pointerenter', function () { stage.paused = true; });
    stageEl.addEventListener('pointerleave', function () { stage.paused = false; });
    stageEl.addEventListener('focusin', function () { stage.paused = true; });
    stageEl.addEventListener('focusout', function () { stage.paused = false; });
    stage.play(shown, images, 0);

    railCounts(items);
    sizes(items, shown, images, stage);
  }

  // ---------- On the rail: live count and lowest price per category ----------
  function railCounts(items) {
    $$('.menu tr[data-cat]').forEach(function (tr) {
      var cat = tr.getAttribute('data-cat');
      var mine = items.filter(function (it) { return it.cat === cat; });
      var cell = $('[data-val]', tr);
      if (!cell || !mine.length) return;
      var low = Math.min.apply(null, mine.map(function (it) { return Number(it.price) || Infinity; }));
      cell.innerHTML = '';
      cell.appendChild(document.createTextNode(isFinite(low) ? 'from ' + money(low) : ''));
      var small = document.createElement('small');
      small.textContent = mine.length + (mine.length === 1 ? ' piece' : ' pieces');
      cell.appendChild(small);
    });
  }

  // ---------- Find your size ----------
  function sizes(items, shown, images, stage) {
    var chips = $$('#chips .chip');
    var list = $('#size-list');
    var count = $('#size-count');
    var frame = $('#size-frame');
    var wide = window.matchMedia('(min-width: 960px)');
    var mini = null;

    chips.forEach(function (chip) {
      var g = chip.getAttribute('data-size');
      var n = items.filter(function (it) { return group(it.size) === g; }).length;
      if (!n) { chip.disabled = true; chip.title = 'Nothing in this size right now'; }
    });

    function choose(chip) {
      var on = chip.getAttribute('aria-pressed') !== 'true';
      chips.forEach(function (c) { c.setAttribute('aria-pressed', c === chip && on ? 'true' : 'false'); });
      var g = on ? chip.getAttribute('data-size') : '';
      list.replaceChildren();
      if (!g) {
        count.innerHTML = 'Pick a size above, or <a href="/rack/">browse every piece on the rack</a>.';
        frame.classList.remove('has');
        stage.play(shown, images, 0);
        return;
      }
      var mine = items.filter(function (it) { return group(it.size) === g; })
        .sort(function (a, b) { return (Number(a.price) || 0) - (Number(b.price) || 0); });
      var label = chip.textContent.trim();
      count.textContent = mine.length + (mine.length === 1 ? ' piece' : ' pieces') + ' in ' + label + ' right now.';
      mine.forEach(function (it) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = tagUrl(it.link, 'size-' + g.toLowerCase());
        a.target = '_blank';
        a.rel = 'noopener';
        a.innerHTML = '<span class="n"></span><span class="p"></span>';
        $('.n', a).textContent = it.name + (/^(XS|S|M|L|XL|XXL)$/.test(g) ? '' : ' (' + it.size + ')');
        $('.p', a).innerHTML = money(it.price) + ' <span aria-hidden="true">↗</span><span class="vh"> CAD, opens in a new tab</span>';
        li.appendChild(a);
        list.appendChild(li);
      });
      var pics = mine.filter(function (it) { return it.photo && images[it.photo]; });
      if (!pics.length) { frame.classList.remove('has'); return; }
      if (wide.matches) {
        stage.play(pics, images, 0);
      } else {
        // On phones the stage is up top, out of sight; the same hanger appears right under the chips.
        if (!mini) {
          frame.innerHTML = '<div class="stage-layers"></div>';
          mini = new Stage($('.stage-layers', frame), null);
        }
        frame.classList.add('has');
        mini.play(pics, images, 0);
      }
    }
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () { if (!chip.disabled) choose(chip); });
    });
  }
})();
