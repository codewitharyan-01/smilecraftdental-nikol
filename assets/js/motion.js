/* ==========================================================================
   Smilecraft — motion layer
   Word reveals, parallax, magnetic buttons, tilt, video visibility and a page
   veil. Everything is additive: if this file never loads, the site is still
   complete and readable.
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var wide = function () { return window.innerWidth > 900; };

  /* ---------------------------------------------------------------------- */
  /* 1. Split a headline into masked words                                  */
  /* ---------------------------------------------------------------------- */
  function splitElement(el) {
    var frag = document.createDocumentFragment();
    var idx = 0;
    var nodes = Array.prototype.slice.call(el.childNodes);

    nodes.forEach(function (node) {
      if (node.nodeType === 3) {
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (!part.trim()) { frag.appendChild(document.createTextNode(part)); return; }
          var w = document.createElement("span");
          var i = document.createElement("i");
          w.className = "w";
          i.textContent = part;
          w.appendChild(i);
          w.style.setProperty("--wi", idx++);
          frag.appendChild(w);
        });
        return;
      }
      if (node.nodeType === 1) {
        if (node.tagName === "BR") {
          frag.appendChild(document.createElement("br"));
          idx += 2;
          return;
        }
        var wrap = document.createElement("span");
        var inner = document.createElement("i");
        wrap.className = "w";
        inner.appendChild(node.cloneNode(true));
        wrap.appendChild(inner);
        wrap.style.setProperty("--wi", idx++);
        frag.appendChild(wrap);
      }
    });

    el.innerHTML = "";
    el.appendChild(frag);
  }

  (function words() {
    var targets = $$("[data-split]");
    if (!targets.length) return;

    if (reduce) return;

    targets.forEach(function (el) {
      try { splitElement(el); } catch (err) { /* leave the heading untouched */ }
    });

    if (!("IntersectionObserver" in window)) {
      targets.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.25 });

    targets.forEach(function (el) { io.observe(el); });
  })();

  /* ---------------------------------------------------------------------- */
  /* 2. Image reveals (clip-path)                                           */
  /* ---------------------------------------------------------------------- */
  (function imageReveal() {
    var items = $$(".reveal-img");
    if (!items.length) return;
    if (reduce || !("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.1 });
    items.forEach(function (el) { io.observe(el); });
  })();

  /* ---------------------------------------------------------------------- */
  /* 3. Parallax                                                            */
  /* ---------------------------------------------------------------------- */
  (function parallax() {
    var items = $$("[data-parallax]");
    if (!items.length || reduce) return;
    var ticking = false;

    function frame() {
      var vh = window.innerHeight;
      items.forEach(function (el) {
        if (!wide()) { el.style.transform = ""; return; }
        var rect = el.getBoundingClientRect();
        if (rect.bottom < -200 || rect.top > vh + 200) return;
        var speed = parseFloat(el.getAttribute("data-parallax")) || 0.06;
        var offset = (rect.top + rect.height / 2 - vh / 2) * speed;
        offset = Math.max(-70, Math.min(70, offset));
        el.style.transform = "translate3d(0," + offset.toFixed(1) + "px,0)";
      });
      ticking = false;
    }

    function onScroll() {
      if (!ticking) { ticking = true; window.requestAnimationFrame(frame); }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    frame();
  })();

  /* ---------------------------------------------------------------------- */
  /* 4. Magnetic buttons                                                     */
  /* ---------------------------------------------------------------------- */
  (function magnetic() {
    if (reduce) return;
    $$("[data-magnetic]").forEach(function (el) {
      var raf = null;
      el.addEventListener("pointermove", function (e) {
        if (!wide() || e.pointerType !== "mouse") return;
        var r = el.getBoundingClientRect();
        var dx = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
        var dy = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
        if (raf) cancelAnimationFrame(raf);
        raf = requestAnimationFrame(function () {
          el.style.transform = "translate(" + (dx * 5).toFixed(1) + "px," + (dy * 4).toFixed(1) + "px)";
        });
      });
      el.addEventListener("pointerleave", function () {
        if (raf) cancelAnimationFrame(raf);
        el.style.transform = "";
      });
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* 5. Tilt on cards                                                       */
  /* ---------------------------------------------------------------------- */
  (function tilt() {
    if (reduce) return;
    $$("[data-tilt]").forEach(function (el) {
      var raf = null;
      el.addEventListener("pointermove", function (e) {
        if (!wide() || e.pointerType !== "mouse") return;
        var r = el.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        if (raf) cancelAnimationFrame(raf);
        raf = requestAnimationFrame(function () {
          el.style.transform = "perspective(900px) rotateX(" + (-py * 3).toFixed(2) + "deg) rotateY(" + (px * 3.4).toFixed(2) + "deg) translateY(-2px)";
        });
      });
      el.addEventListener("pointerleave", function () {
        if (raf) cancelAnimationFrame(raf);
        el.style.transform = "";
      });
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* 6. Videos only play while on screen                                    */
  /* ---------------------------------------------------------------------- */
  (function videoVisibility() {
    var vids = $$("video[data-managed]");
    if (!vids.length) return;

    vids.forEach(function (v) {
      v.muted = true;
      v.setAttribute("muted", "");
      v.playsInline = true;
      v.setAttribute("playsinline", "");
      if (reduce) { v.removeAttribute("autoplay"); v.pause(); return; }
    });

    if (reduce || !("IntersectionObserver" in window)) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) {
          var p = v.play();
          if (p && p.catch) p.catch(function () {});
        } else {
          v.pause();
        }
      });
    }, { threshold: 0.15 });

    vids.forEach(function (v) { io.observe(v); });
  })();

  /* ---------------------------------------------------------------------- */
  /* 7. Page veil                                                           */
  /* ---------------------------------------------------------------------- */
  (function veil() {
    var box = $("[data-veil-box]");
    if (!box) return;

    document.addEventListener("click", function (e) {
      var a = e.target.closest("a");
      if (!a) return;
      var href = a.getAttribute("href") || "";
      if (!href || a.target === "_blank" || a.hasAttribute("download")) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
      if (href.charAt(0) === "#" || /^(tel:|mailto:|https?:)/i.test(href)) return;
      if (a.hasAttribute("data-no-veil")) return;

      e.preventDefault();
      document.body.setAttribute("data-veil", "out");
      window.setTimeout(function () { window.location.href = href; }, 220);
    });

    window.addEventListener("pageshow", function () {
      document.body.removeAttribute("data-veil");
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* 8. Section index highlight (desktop, if present)                       */
  /* ---------------------------------------------------------------------- */
  (function sectionIndex() {
    var links = $$("[data-index-link]");
    if (!links.length || !("IntersectionObserver" in window)) return;
    var map = {};
    links.forEach(function (a) {
      var id = a.getAttribute("href").replace("#", "");
      var sec = document.getElementById(id);
      if (sec) map[id] = a;
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.removeAttribute("data-active"); });
          var a = map[e.target.id];
          if (a) a.setAttribute("data-active", "true");
        }
      });
    }, { rootMargin: "-40% 0px -50% 0px" });
    Object.keys(map).forEach(function (id) { io.observe(document.getElementById(id)); });
  })();

})();

/* --------------------------------------------------------------------------
   9. Density pass: header state, spotlight, sticky book pill, back to top
   -------------------------------------------------------------------------- */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function onScroll() {
    document.body.setAttribute("data-scrolled", window.scrollY > 24 ? "true" : "false");
    var pill = document.querySelector("[data-book-pill]");
    if (pill) pill.setAttribute("data-show", window.scrollY > 620 ? "true" : "false");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (!reduce && window.matchMedia("(pointer: fine)").matches) {
    var tiles = document.querySelectorAll(".card, .svc, .review, .bento__tile, .rail-card");
    Array.prototype.forEach.call(tiles, function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        el.style.setProperty("--mx", (((e.clientX - r.left) / r.width) * 100).toFixed(1) + "%");
        el.style.setProperty("--my", (((e.clientY - r.top) / r.height) * 100).toFixed(1) + "%");
      });
    });
  }

  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-top]");
    if (!t) return;
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
  });
})();

/* --------------------------------------------------------------------------
   10. Micro-interactions: card tilt, and a hard guarantee that no
       reveal-clipped image can stay invisible.
   -------------------------------------------------------------------------- */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  window.setTimeout(function () {
    Array.prototype.forEach.call(document.querySelectorAll(".reveal-img:not(.is-in)"), function (el) {
      el.classList.add("is-in");
    });
  }, 1400);

  if (reduce || !window.matchMedia("(pointer: fine)").matches) return;

  Array.prototype.forEach.call(document.querySelectorAll(".svc, .bento__tile"), function (el) {
    var raf = null;
    el.addEventListener("pointermove", function (e) {
      var r = el.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width - 0.5;
      var py = (e.clientY - r.top) / r.height - 0.5;
      if (raf) cancelAnimationFrame(raf);
      raf = requestAnimationFrame(function () {
        el.style.transform = "perspective(900px) rotateX(" + (-py * 2.2).toFixed(2) +
          "deg) rotateY(" + (px * 2.6).toFixed(2) + "deg) translateY(-2px)";
      });
    });
    el.addEventListener("pointerleave", function () {
      if (raf) cancelAnimationFrame(raf);
      el.style.transform = "";
    });
  });
})();
