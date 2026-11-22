/* ==========================================================================
   Smilecraft — scroll effects engine
   Auto-tags blocks on every page, reveals them on scroll, adds a progress bar,
   counts numbers up, and keeps a fallback so nothing can stay hidden.
   ========================================================================== */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- scroll progress -------------------------------------------------- */
  var bar = document.createElement("div");
  bar.className = "fx-progress";
  bar.setAttribute("aria-hidden", "true");
  document.body.appendChild(bar);

  /* ---- what animates, everywhere ---------------------------------------- */
  var SEL = [
    ".section-head", ".card", ".svc", ".bento__tile", ".triage__row",
    ".triage__panels", ".step", ".review", ".faq__item", ".visit__row",
    ".rail-card", ".book-card", ".revband", ".cta", ".split__media",
    ".split__body > *", ".film-stage", ".film-tile", ".gal__item",
    ".footer__grid > *", ".doctor__body > *"
  ].join(",");

  var nodes = Array.prototype.slice.call(document.querySelectorAll(SEL));
  var counts = new Map();

  nodes.forEach(function (el) {
    el.classList.add("fx");
    if (!el.hasAttribute("data-reveal")) el.setAttribute("data-reveal", "");
    var parent = el.parentElement || document.body;
    var n = counts.get(parent) || 0;
    counts.set(parent, n + 1);
    el.style.setProperty("--d", Math.min(n * 55, 330) + "ms");
  });

  function show(el) { el.classList.add("is-in"); }

  /* ---- reveal ----------------------------------------------------------- */
  if (reduce || !("IntersectionObserver" in window)) {
    nodes.forEach(show);
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { show(e.target); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
    nodes.forEach(function (el) { io.observe(el); });
  }

  /* ---- scroll sweep + progress bar -------------------------------------- */
  var ticking = false;

  function frame() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    bar.style.transform = "scaleX(" + (max > 0 ? h.scrollTop / max : 0) + ")";

    if (!reduce) {
      var vh = window.innerHeight;
      for (var i = 0; i < nodes.length; i++) {
        var el = nodes[i];
        if (el.classList.contains("is-in")) continue;
        var r = el.getBoundingClientRect();
        if (r.top < vh * 0.94 && r.bottom > -24) show(el);
      }
    }
    ticking = false;
  }

  function onScroll() {
    if (!ticking) { ticking = true; window.requestAnimationFrame(frame); }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  window.addEventListener("load", onScroll);
  frame();

  /* nothing above the fold should stay invisible for long */
  window.setTimeout(function () {
    var vh = window.innerHeight;
    nodes.forEach(function (el) {
      if (el.getBoundingClientRect().top < vh * 1.15) show(el);
    });
  }, 700);

  /* ---- number count-up -------------------------------------------------- */
  if (!reduce) {
    Array.prototype.forEach.call(document.querySelectorAll(".bento__num"), function (el) {
      var text = el.textContent.trim();
      var target = parseFloat(text);
      if (isNaN(target)) return;
      var dec = (text.split(".")[1] || "").length;
      var done = false;

      function run() {
        if (done) return;
        done = true;
        var t0 = performance.now();
        var dur = 900;
        function tick(t) {
          var p = Math.min((t - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = (target * eased).toFixed(dec);
          if (p < 1) window.requestAnimationFrame(tick);
        }
        window.requestAnimationFrame(tick);
      }

      if ("IntersectionObserver" in window) {
        var seen = new IntersectionObserver(function (entries) {
          entries.forEach(function (e) {
            if (e.isIntersecting) { run(); seen.disconnect(); }
          });
        }, { threshold: 0.4 });
        seen.observe(el);
      } else {
        run();
      }
    });
  }

  /* ---- gentle parallax on the portrait ---------------------------------- */
  if (!reduce) {
    var portrait = document.querySelector(".doctor__media img");
    if (portrait) {
      var pTicking = false;
      var par = function () {
        var r = portrait.getBoundingClientRect();
        var vh = window.innerHeight;
        if (r.bottom > -60 && r.top < vh + 60) {
          var off = ((r.top + r.height / 2) - vh / 2) * 0.035;
          off = Math.max(-18, Math.min(18, off));
          portrait.style.transform = "translate3d(0," + off.toFixed(1) + "px,0) scale(1.04)";
        }
        pTicking = false;
      };
      window.addEventListener("scroll", function () {
        if (!pTicking) { pTicking = true; window.requestAnimationFrame(par); }
      }, { passive: true });
      par();
    }
  }
  document.documentElement.classList.add("fx-ready");
})();

