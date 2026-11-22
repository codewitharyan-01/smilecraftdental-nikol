/* ==========================================================================
   Smilecraft — site behaviour
   Vanilla JS. Every feature degrades to a usable page without it.
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------------------- */
  /* Header: condense, hide on scroll down, back on scroll up                */
  /* ---------------------------------------------------------------------- */
  (function header() {
    var el = $("[data-header]");
    if (!el) return;
    var last = window.scrollY;
    var ticking = false;

    function update() {
      var y = window.scrollY;
      el.setAttribute("data-pinned", y > 8 ? "true" : "false");
      if (y > 320 && y > last + 4 && !document.body.hasAttribute("data-menu")) {
        el.setAttribute("data-hidden", "true");
      } else if (y < last - 4 || y < 120) {
        el.setAttribute("data-hidden", "false");
      }
      last = y;
      ticking = false;
    }

    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
    }, { passive: true });
  })();

  /* ---------------------------------------------------------------------- */
  /* Mobile drawer                                                          */
  /* ---------------------------------------------------------------------- */
  (function drawer() {
    var open = $("[data-menu-open]");
    var close = $("[data-menu-close]");
    var panel = $("[data-drawer]");
    if (!open || !panel) return;

    function setOpen(state) {
      if (state) {
        document.body.setAttribute("data-menu", "open");
        document.body.classList.add("is-locked");
        open.setAttribute("aria-expanded", "true");
        var first = panel.querySelector("a, button");
        if (first) first.focus({ preventScroll: true });
      } else {
        document.body.removeAttribute("data-menu");
        document.body.classList.remove("is-locked");
        open.setAttribute("aria-expanded", "false");
      }
    }

    open.addEventListener("click", function () { setOpen(document.body.getAttribute("data-menu") !== "open"); });
    if (close) close.addEventListener("click", function () { setOpen(false); });
    panel.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 1080) setOpen(false);
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* Nav dropdown                                                           */
  /* ---------------------------------------------------------------------- */
  (function dropdown() {
    $$("[data-dropdown]").forEach(function (item) {
      var trigger = $(".nav__trigger", item);
      if (!trigger) return;
      var timer;

      function set(state) {
        item.setAttribute("data-open", state ? "true" : "false");
        trigger.setAttribute("aria-expanded", state ? "true" : "false");
      }

      item.addEventListener("mouseenter", function () {
        if (window.innerWidth <= 1080) return;
        clearTimeout(timer);
        set(true);
      });
      item.addEventListener("mouseleave", function () {
        if (window.innerWidth <= 1080) return;
        timer = setTimeout(function () { set(false); }, 120);
      });
      trigger.addEventListener("click", function (e) {
        e.preventDefault();
        set(item.getAttribute("data-open") !== "true");
      });
      document.addEventListener("click", function (e) {
        if (!item.contains(e.target)) set(false);
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") set(false);
      });
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* Opening hours — always computed for Asia/Kolkata                       */
  /* ---------------------------------------------------------------------- */
  (function hours() {
    var OPEN_MIN = 9 * 60;      // 09:00
    var CLOSE_MIN = 21 * 60;    // 21:00
    var NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var SHORT = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

    function istNow() {
      var parts;
      try {
        parts = new Intl.DateTimeFormat("en-GB", {
          timeZone: "Asia/Kolkata", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false
        }).formatToParts(new Date());
      } catch (e) { return null; }
      var map = {};
      parts.forEach(function (p) { map[p.type] = p.value; });
      var idx = SHORT.indexOf(map.weekday);
      if (idx < 0) return null;
      return { day: idx, min: (parseInt(map.hour, 10) % 24) * 60 + parseInt(map.minute, 10) };
    }

    function label(min) {
      var h = Math.floor(min / 60);
      var m = min % 60;
      var h12 = h % 12 === 0 ? 12 : h % 12;
      var suffix = h < 12 ? "AM" : "PM";
      return h12 + (m ? ":" + (m < 10 ? "0" + m : m) : ":00") + " " + suffix;
    }

    function nextOpening(day) {
      for (var i = 1; i <= 7; i++) {
        var d = (day + i) % 7;
        if (d !== 0) {
          return (i === 1 ? "tomorrow" : NAMES[d]) + " " + label(OPEN_MIN);
        }
      }
      return "Monday " + label(OPEN_MIN);
    }

    function compute() {
      var t = istNow();
      if (!t) return { open: false, text: "Mon–Sat, 9 AM – 9 PM", short: "9 AM – 9 PM" };
      if (t.day === 0) return { open: false, text: "Closed Sunday · opens Monday " + label(OPEN_MIN), short: "Closed Sunday" };
      if (t.min < OPEN_MIN) return { open: false, text: "Opens today " + label(OPEN_MIN), short: "Opens " + label(OPEN_MIN) };
      if (t.min >= CLOSE_MIN) return { open: false, text: "Closed · opens " + nextOpening(t.day), short: "Closed · opens " + (t.day === 6 ? "Mon " : "tomorrow ") + label(OPEN_MIN) };
      return { open: true, text: "Open now · until " + label(CLOSE_MIN), short: "Open now" };
    }

    var state = compute();

    $$("[data-status]").forEach(function (el) {
      el.setAttribute("data-open", state.open ? "true" : "false");
      var txt = $("[data-status-text]", el);
      if (txt) txt.textContent = state.text;
      var short = $("[data-status-short]", el);
      if (short) short.textContent = state.short;
    });

    // highlight today in every hours table
    var t = istNow();
    if (t) {
      $$("[data-hours] tr[data-day]").forEach(function (row) {
        if (parseInt(row.getAttribute("data-day"), 10) === t.day) row.setAttribute("data-today", "true");
      });
    }
  })();

  /* ---------------------------------------------------------------------- */
  /* Scroll reveal                                                          */
  /* ---------------------------------------------------------------------- */
  (function reveal() {
    var items = $$("[data-reveal]");
    if (!items.length) return;
    if (reduceMotion || !("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }

    $$("[data-reveal-group]").forEach(function (group) {
      $$("[data-reveal]", group).forEach(function (el, i) {
        if (!el.style.getPropertyValue("--d")) el.style.setProperty("--d", (i * 70) + "ms");
      });
    });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });

    items.forEach(function (el) { io.observe(el); });
  })();

  /* ---------------------------------------------------------------------- */
  /* Counters                                                               */
  /* ---------------------------------------------------------------------- */
  (function counters() {
    var els = $$("[data-count]");
    if (!els.length) return;

    function run(el) {
      var target = parseFloat(el.getAttribute("data-count"));
      var decimals = (el.getAttribute("data-count").split(".")[1] || "").length;
      if (reduceMotion) { el.textContent = target.toFixed(decimals); return; }
      var start = performance.now();
      var dur = 1200;
      function tick(now) {
        var p = Math.min((now - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = (target * eased).toFixed(decimals);
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    }

    if (!("IntersectionObserver" in window)) { els.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { run(e.target); io.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    els.forEach(function (el) { io.observe(el); });
  })();

  /* ---------------------------------------------------------------------- */
  /* Symptom picker                                                         */
  /* ---------------------------------------------------------------------- */
  (function picker() {
    $$("[data-picker]").forEach(function (root) {
      var tabs = $$("[role=tab]", root);
      var panels = $$("[role=tabpanel]", root);
      if (!tabs.length) return;

      function select(i, focus) {
        tabs.forEach(function (t, j) {
          t.setAttribute("aria-selected", j === i ? "true" : "false");
          t.tabIndex = j === i ? 0 : -1;
        });
        panels.forEach(function (p, j) { p.setAttribute("data-active", j === i ? "true" : "false"); });
        if (focus) tabs[i].focus();
      }

      tabs.forEach(function (tab, i) {
        tab.addEventListener("click", function () { select(i); });
        tab.addEventListener("keydown", function (e) {
          if (e.key === "ArrowRight") { select((i + 1) % tabs.length, true); e.preventDefault(); }
          if (e.key === "ArrowLeft") { select((i - 1 + tabs.length) % tabs.length, true); e.preventDefault(); }
        });
      });
      select(0);
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* FAQ accordion                                                          */
  /* ---------------------------------------------------------------------- */
  (function faq() {
    $$("[data-faq] .faq__item").forEach(function (item) {
      var btn = $(".faq__q", item);
      var panel = $(".faq__a", item);
      if (!btn || !panel) return;

      btn.addEventListener("click", function () {
        var open = item.getAttribute("data-open") === "true";
        if (open) {
          panel.style.height = panel.scrollHeight + "px";
          requestAnimationFrame(function () { panel.style.height = "0px"; });
          item.setAttribute("data-open", "false");
          btn.setAttribute("aria-expanded", "false");
        } else {
          panel.style.height = panel.scrollHeight + "px";
          item.setAttribute("data-open", "true");
          btn.setAttribute("aria-expanded", "true");
          panel.addEventListener("transitionend", function done() {
            if (item.getAttribute("data-open") === "true") panel.style.height = "auto";
            panel.removeEventListener("transitionend", done);
          });
        }
      });
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* Review rail: buttons + drag                                            */
  /* ---------------------------------------------------------------------- */
  (function rail() {
    $$("[data-rail]").forEach(function (track) {
      var wrap = track.closest("[data-rail-wrap]") || track.parentElement;
      var prev = $("[data-rail-prev]", wrap);
      var next = $("[data-rail-next]", wrap);

      function step() {
        var card = track.firstElementChild;
        return card ? card.getBoundingClientRect().width + 16 : 340;
      }

      if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
      if (next) next.addEventListener("click", function () { track.scrollBy({ left: step(), behavior: "smooth" }); });

      var down = false, startX = 0, startLeft = 0, moved = false;
      track.addEventListener("pointerdown", function (e) {
        if (e.pointerType === "mouse" && e.button !== 0) return;
        down = true; moved = false;
        startX = e.clientX; startLeft = track.scrollLeft;
      });
      track.addEventListener("pointermove", function (e) {
        if (!down) return;
        var dx = e.clientX - startX;
        if (Math.abs(dx) > 4) { moved = true; track.style.scrollSnapType = "none"; track.scrollLeft = startLeft - dx; }
      });
      ["pointerup", "pointerleave", "pointercancel"].forEach(function (evt) {
        track.addEventListener(evt, function () {
          down = false;
          track.style.scrollSnapType = "";
        });
      });
      track.addEventListener("click", function (e) {
        if (moved) { e.preventDefault(); moved = false; }
      }, true);
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* Gallery lightbox                                                       */
  /* ---------------------------------------------------------------------- */
  (function lightbox() {
    var items = $$("[data-lightbox]");
    var box = $("[data-lightbox-box]");
    if (!items.length || !box) return;

    var img = $("img", box);
    var cap = $("[data-lightbox-cap]", box);
    var current = 0;
    var lastFocus = null;

    function show(i) {
      current = (i + items.length) % items.length;
      var el = items[current];
      var full = el.getAttribute("data-full") || $("img", el).src;
      img.src = full;
      img.alt = $("img", el).alt || "";
      if (cap) cap.textContent = el.getAttribute("data-label") || "";
      box.setAttribute("data-open", "true");
      document.body.classList.add("is-locked");
    }

    function hide() {
      box.setAttribute("data-open", "false");
      document.body.classList.remove("is-locked");
      if (lastFocus) lastFocus.focus({ preventScroll: true });
    }

    items.forEach(function (el, i) {
      el.addEventListener("click", function () {
        lastFocus = el;
        show(i);
      });
    });

    var close = $("[data-lightbox-close]", box);
    if (close) close.addEventListener("click", hide);
    box.addEventListener("click", function (e) { if (e.target === box) hide(); });
    document.addEventListener("keydown", function (e) {
      if (box.getAttribute("data-open") !== "true") return;
      if (e.key === "Escape") hide();
      if (e.key === "ArrowRight") show(current + 1);
      if (e.key === "ArrowLeft") show(current - 1);
    });
    $$("[data-lightbox-prev]", box).forEach(function (b) { b.addEventListener("click", function () { show(current - 1); }); });
    $$("[data-lightbox-next]", box).forEach(function (b) { b.addEventListener("click", function () { show(current + 1); }); });
  })();

  /* ---------------------------------------------------------------------- */
  /* Inline video play/pause                                                */
  /* ---------------------------------------------------------------------- */
  (function video() {
    $$("[data-video]").forEach(function (wrap) {
      var v = $("video", wrap);
      var btn = $("[data-video-btn]", wrap);
      if (!v || !btn) return;
      var label = $("[data-video-label]", btn);

      function sync() {
        var paused = v.paused;
        btn.setAttribute("aria-label", paused ? "Play the clinic tour" : "Pause the clinic tour");
        if (label) label.textContent = paused ? "Play" : "Pause";
      }

      btn.addEventListener("click", function () {
        if (v.paused) { v.play(); } else { v.pause(); }
      });
      v.addEventListener("play", sync);
      v.addEventListener("pause", sync);
      sync();
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* Copy to clipboard                                                      */
  /* ---------------------------------------------------------------------- */
  (function copy() {
    $$("[data-copy]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var text = btn.getAttribute("data-copy");
        var done = function () {
          var old = btn.getAttribute("data-label-orig") || btn.textContent;
          btn.setAttribute("data-label-orig", old);
          btn.textContent = "Copied";
          setTimeout(function () { btn.textContent = old; }, 1800);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done).catch(function () {});
        } else {
          var ta = document.createElement("textarea");
          ta.value = text;
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand("copy"); done(); } catch (e) {}
          document.body.removeChild(ta);
        }
      });
    });
  })();

  /* ---------------------------------------------------------------------- */
  /* Year + scroll progress                                                 */
  /* ---------------------------------------------------------------------- */
  (function misc() {
    $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

    var bar = $("[data-progress]");
    if (!bar) return;
    window.addEventListener("scroll", function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.transform = "scaleX(" + (max > 0 ? h.scrollTop / max : 0) + ")";
    }, { passive: true });
  })();

  /* ---------------------------------------------------------------------- */
  /* Analytics shim — pushes to dataLayer if you add GTM/GA later            */
  /* ---------------------------------------------------------------------- */
  window.track = function (event, data) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: event }, data || {}));
  };
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a, button");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("wa.me") > -1) window.track("whatsapp_click", { page: location.pathname });
    else if (href.indexOf("tel:") === 0) window.track("call_click", { page: location.pathname });
    else if (href.indexOf("writereview") > -1) window.track("google_review_click", { page: location.pathname });
    else if (href.indexOf("maps") > -1) window.track("directions_click", { page: location.pathname });
  });

})();
