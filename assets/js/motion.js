/* ==========================================================================
   Smilecraft — motion engine
   Scroll progress, word reveal, parallax, counters, comparison slider, tilt.
   ========================================================================== */
(function () {
  "use strict";

  var doc = document;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Page loaded flag (hero choreography) ------------------------ */
  window.addEventListener("load", function () { doc.body.dataset.loaded = "true"; });
  // Fallback in case load already fired
  if (doc.readyState === "complete") doc.body.dataset.loaded = "true";
  window.setTimeout(function () { doc.body.dataset.loaded = "true"; }, 400);

  /* ---------- Scroll progress --------------------------------------------- */
  var bar = doc.querySelector("[data-scroll-progress]");
  function paintProgress() {
    if (!bar) return;
    var max = doc.documentElement.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(window.pageYOffset / max, 1) : 0;
    bar.style.transform = "scaleX(" + p + ")";
  }

  /* ---------- Reveal observer --------------------------------------------- */
  var revealEls = doc.querySelectorAll(".split-line, .word-reveal, .mask-reveal, [data-reveal]");
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---------- Word reveal for headings ------------------------------------ */
  doc.querySelectorAll("[data-words]").forEach(function (el) {
    if (reduce || el.dataset.done) return;
    var count = 0;

    function walk(node) {
      var frag = doc.createDocumentFragment();
      Array.prototype.slice.call(node.childNodes).forEach(function (child) {
        if (child.nodeType === 3) {
          child.textContent.split(/(\s+)/).forEach(function (chunk) {
            if (!chunk) return;
            if (!chunk.trim()) { frag.appendChild(doc.createTextNode(chunk)); return; }
            var w = doc.createElement("span");
            w.className = "w";
            w.style.setProperty("--w", count++);
            var inner = doc.createElement("span");
            inner.textContent = chunk;
            w.appendChild(inner);
            frag.appendChild(w);
          });
        } else if (child.nodeType === 1) {
          var clone = child.cloneNode(false);
          clone.appendChild(walk(child));
          frag.appendChild(clone);
        }
      });
      return frag;
    }

    try {
      var built = walk(el);
      el.innerHTML = "";
      el.appendChild(built);
      el.classList.add("word-reveal");
      el.dataset.done = "1";
    } catch (e) { /* leave text as-is */ }
  });

  /* ---------- Parallax ----------------------------------------------------- */
  var parEls = Array.prototype.slice.call(doc.querySelectorAll("[data-parallax]"));
  function paintParallax() {
    if (reduce || !parEls.length) return;
    var vh = window.innerHeight;
    parEls.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -160 || r.top > vh + 160) return;
      var speed = parseFloat(el.dataset.parallax) || 0.08;
      var offset = (r.top + r.height / 2 - vh / 2) * speed;
      offset = Math.max(-70, Math.min(70, offset));
      var target = el.querySelector("img") || el;
      target.style.transform = "translate3d(0," + offset.toFixed(1) + "px,0)" +
        (target === el && el.classList.contains("parallax-wrap") ? "" : "");
    });
  }

  /* ---------- Counters ----------------------------------------------------- */
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function runCounter(el) {
    var target = parseFloat(el.dataset.count);
    var dec = parseInt(el.dataset.decimals || "0", 10);
    if (isNaN(target)) return;
    if (reduce) { el.textContent = dec ? target.toFixed(dec) : String(target); return; }
    var dur = 1400, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var v = target * easeOut(p);
      el.textContent = dec ? v.toFixed(dec) : String(Math.round(v));
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = dec ? target.toFixed(dec) : String(target);
    }
    requestAnimationFrame(step);
  }
  var counters = doc.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { runCounter(en.target); cio.unobserve(en.target); }
      });
    }, { threshold: 0.55 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(runCounter);
  }

  /* ---------- Comparison slider ------------------------------------------- */
  doc.querySelectorAll("[data-ba]").forEach(function (root) {
    var beforeLayer = root.querySelector(".ba__before");
    var handle = root.querySelector(".ba__handle");
    if (!beforeLayer) return;
    var dragging = false;
    var pct = 50;

    function apply(p) {
      pct = Math.max(4, Math.min(96, p));
      beforeLayer.style.clipPath = "inset(0 " + (100 - pct) + "% 0 0)";
      if (handle) handle.style.left = pct + "%";
    }

    function fromEvent(e) {
      var r = root.getBoundingClientRect();
      var x = (e.touches ? e.touches[0].clientX : e.clientX) - r.left;
      apply((x / r.width) * 100);
    }

    root.addEventListener("pointerdown", function (e) {
      dragging = true;
      root.setPointerCapture(e.pointerId);
      fromEvent(e);
    });
    root.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      fromEvent(e);
    });
    ["pointerup", "pointercancel", "pointerleave"].forEach(function (ev) {
      root.addEventListener(ev, function () { dragging = false; });
    });
    root.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") { apply(pct - 4); e.preventDefault(); }
      if (e.key === "ArrowRight") { apply(pct + 4); e.preventDefault(); }
    });
    root.setAttribute("tabindex", "0");
    root.setAttribute("role", "slider");
    root.setAttribute("aria-label", "Before and after comparison");
    root.setAttribute("aria-valuemin", "0");
    root.setAttribute("aria-valuemax", "100");

    apply(50);
  });

  /* ---------- Tilt --------------------------------------------------------- */
  if (!reduce && window.matchMedia("(min-width: 981px)").matches) {
    doc.querySelectorAll("[data-tilt]").forEach(function (el) {
      var limit = 6;
      el.addEventListener("mousemove", function (e) {
        var r = el.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = "perspective(900px) rotateX(" + (-py * limit) +
          "deg) rotateY(" + (px * limit) + "deg) translateY(-3px)";
      });
      el.addEventListener("mouseleave", function () { el.style.transform = ""; });
    });
  }

  /* ---------- Button cursor glow ------------------------------------------ */
  doc.querySelectorAll(".btn").forEach(function (b) {
    b.addEventListener("mousemove", function (e) {
      var r = b.getBoundingClientRect();
      b.style.setProperty("--mx", ((e.clientX - r.left) / r.width) * 100 + "%");
      b.style.setProperty("--my", ((e.clientY - r.top) / r.height) * 100 + "%");
    });
  });

  /* ---------- Scroll loop -------------------------------------------------- */
  var ticking = false;
  function frame() {
    paintProgress();
    paintParallax();
    ticking = false;
  }
  function onScroll() {
    if (!ticking) { ticking = true; requestAnimationFrame(frame); }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  frame();
})();
