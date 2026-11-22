/* ==========================================================================
   Smilecraft — behaviour
   Quiet Apple-style motion: content reveals, counters, carousel, hours.
   ========================================================================== */
(function () {
  "use strict";

  var doc = document;
  var body = doc.body;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Sticky header shadow --------------------------------------- */
  var head = doc.querySelector(".site-head");
  if (head) {
    var markScroll = function () {
      head.dataset.stuck = String(window.pageYOffset > 12);
    };
    window.addEventListener("scroll", markScroll, { passive: true });
    markScroll();
  }

  /* ---------- Clinic config ---------------------------------------------- */
  var CLINIC = {
    tz: "Asia/Kolkata",
    hours: { 0: null, 1: [540, 1260], 2: [540, 1260], 3: [540, 1260], 4: [540, 1260], 5: [540, 1260], 6: [540, 1260] }
  };
  var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  function tzParts() {
    try {
      var f = new Intl.DateTimeFormat("en-GB", {
        timeZone: CLINIC.tz, weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false
      });
      var p = {};
      f.formatToParts(new Date()).forEach(function (x) { if (x.type !== "literal") p[x.type] = x.value; });
      var map = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
      var h = parseInt(p.hour, 10);
      if (h === 24) h = 0;
      return { day: map[p.weekday], mins: h * 60 + parseInt(p.minute, 10) };
    } catch (e) {
      var d = new Date();
      return { day: d.getDay(), mins: d.getHours() * 60 + d.getMinutes() };
    }
  }

  function fmt(mins) {
    var h = Math.floor(mins / 60), m = mins % 60;
    var hh = h % 12 === 0 ? 12 : h % 12;
    return hh + ":" + (m < 10 ? "0" + m : m) + " " + (h >= 12 ? "PM" : "AM");
  }

  function openState() {
    var t = tzParts();
    var slot = CLINIC.hours[t.day];
    if (slot && t.mins >= slot[0] && t.mins < slot[1]) {
      return { open: true, text: "Open now" };
    }
    for (var i = 0; i < 8; i++) {
      var d = (t.day + i) % 7, s = CLINIC.hours[d];
      if (!s) continue;
      if (i === 0 && t.mins < s[0]) return { open: false, text: "Opens " + fmt(s[0]) + " today" };
      if (i > 0) {
        var label = d === (t.day + 1) % 7 ? "tomorrow" : DAYS[d];
        return { open: false, text: "Opens " + label + " " + fmt(s[0]) };
      }
    }
    return { open: false, text: "Closed" };
  }

  function paintStatus() {
    var s = openState();
    doc.querySelectorAll("[data-open-status]").forEach(function (el) {
      el.dataset.open = s.open ? "true" : "false";
      var t = el.querySelector("[data-status-text]");
      if (t) t.textContent = s.text; else el.textContent = s.text;
    });
    var t = tzParts();
    doc.querySelectorAll("table.hours").forEach(function (table) {
      table.querySelectorAll("tr[data-day]").forEach(function (tr) {
        tr.dataset.today = String(parseInt(tr.dataset.day, 10) === t.day);
      });
    });
  }

  /* ---------- Mobile drawer ---------------------------------------------- */
  var burger = doc.querySelector("[data-burger]");
  var drawer = doc.querySelector("[data-drawer]");
  var drawerClose = doc.querySelector("[data-drawer-close]");

  function setMenu(open) {
    body.dataset.menu = open ? "open" : "closed";
    if (burger) burger.setAttribute("aria-expanded", String(open));
    if (drawer) drawer.setAttribute("aria-hidden", String(!open));
    doc.documentElement.style.overflow = open ? "hidden" : "";
  }
  if (burger) burger.addEventListener("click", function () { setMenu(body.dataset.menu !== "open"); });
  if (drawerClose) drawerClose.addEventListener("click", function () { setMenu(false); });
  if (drawer) drawer.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
  doc.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && body.dataset.menu === "open") { setMenu(false); if (burger) burger.focus(); }
  });

  /* ---------- Reveals ----------------------------------------------------- */
  doc.querySelectorAll("[data-stagger]").forEach(function (group) {
    Array.prototype.slice.call(group.querySelectorAll("[data-reveal]")).forEach(function (el, i) {
      if (!el.style.getPropertyValue("--i")) el.style.setProperty("--i", i);
    });
  });

  var targets = doc.querySelectorAll("[data-reveal]");
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.04 });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---------- Counters ---------------------------------------------------- */
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function runCounter(el) {
    var target = parseFloat(el.dataset.count);
    if (isNaN(target)) return;
    if (reduce) { el.textContent = String(target); return; }
    var dur = 1400, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      el.textContent = Math.round(target * easeOut(p)).toString();
      if (p < 1) window.requestAnimationFrame(step);
      else el.textContent = String(target);
    }
    window.requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { runCounter(en.target); cio.unobserve(en.target); }
      });
    }, { threshold: 0.6 });
    doc.querySelectorAll("[data-count]").forEach(function (el) { cio.observe(el); });
  } else {
    doc.querySelectorAll("[data-count]").forEach(runCounter);
  }

  /* ---------- Carousel ---------------------------------------------------- */
  doc.querySelectorAll("[data-slider]").forEach(function (slider) {
    var track = slider.querySelector("[data-slider-track]");
    var prev = slider.querySelector("[data-slider-prev]");
    var next = slider.querySelector("[data-slider-next]");
    if (!track) return;
    function step(dir) {
      var first = track.firstElementChild;
      var w = first ? first.getBoundingClientRect().width + 14 : 300;
      track.scrollBy({ left: dir * w, behavior: "smooth" });
    }
    if (prev) prev.addEventListener("click", function () { step(-1); });
    if (next) next.addEventListener("click", function () { step(1); });
  });

  /* ---------- Lightbox ---------------------------------------------------- */
  var lb = doc.querySelector("[data-lightbox]");
  if (lb) {
    var lbImg = lb.querySelector("img");
    var lbCap = lb.querySelector("[data-lb-cap]");
    var lastFocus = null;
    function openLb(src, cap) {
      lastFocus = doc.activeElement;
      lbImg.src = src;
      lbImg.alt = cap || "";
      if (lbCap) lbCap.textContent = cap || "";
      lb.dataset.open = "true";
      doc.documentElement.style.overflow = "hidden";
      lb.querySelector("[data-lb-close]").focus();
    }
    function closeLb() {
      lb.dataset.open = "false";
      doc.documentElement.style.overflow = "";
      lbImg.removeAttribute("src");
      if (lastFocus) lastFocus.focus();
    }
    doc.querySelectorAll("[data-full]").forEach(function (el) {
      el.addEventListener("click", function () { openLb(el.dataset.full, el.dataset.cap); });
      el.setAttribute("tabindex", "0");
      el.setAttribute("role", "button");
      el.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openLb(el.dataset.full, el.dataset.cap); }
      });
    });
    lb.addEventListener("click", function (e) {
      if (e.target === lb || e.target.closest("[data-lb-close]")) closeLb();
    });
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && lb.dataset.open === "true") closeLb();
    });
  }

  /* ---------- Marquee ----------------------------------------------------- */
  doc.querySelectorAll(".marquee__track").forEach(function (track) {
    track.innerHTML += track.innerHTML;
  });

  /* ---------- Clinic tour ------------------------------------------------- */
  var tour = doc.querySelector("[data-tour]");
  if (tour) {
    var tSlides = Array.prototype.slice.call(tour.querySelectorAll("[data-tour-slides] img"));
    var tDots = Array.prototype.slice.call(tour.querySelectorAll("[data-tour-dot]"));
    var tTimer = null, tIdx = 0;
    function tourShow(n) {
      tIdx = n;
      tSlides.forEach(function (s, k) { s.classList.toggle("is-on", k === n); });
      tDots.forEach(function (d, k) { d.setAttribute("aria-current", String(k === n)); });
    }
    function tourNext() { tourShow((tIdx + 1) % tSlides.length); }
    function tourStop() { if (tTimer) { clearInterval(tTimer); tTimer = null; } }
    function tourStart() {
      if (reduce || tSlides.length < 2) return;
      tTimer = setInterval(tourNext, 4800);
    }
    tDots.forEach(function (d, k) {
      d.addEventListener("click", function () { tourStop(); tourShow(k); tourStart(); });
    });
    tourStart();

    var tourVideo = tour.querySelector("[data-tour-video]");
    if (tourVideo) {
      tourVideo.addEventListener("loadeddata", function () {
        tour.dataset.hasVideo = "true";
        tourStop();
        var p = tourVideo.play();
        if (p && p.catch) p.catch(function () {});
      });
      try { tourVideo.load(); } catch (e) {}
    }
  }

  /* ---------- Footer year ------------------------------------------------- */
  doc.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- First-touch attribution ------------------------------------- */
  var ATTR_KEY = "sc_attr_v1";
  function readAttr() {
    try { return JSON.parse(localStorage.getItem(ATTR_KEY) || "null"); } catch (e) { return null; }
  }
  (function () {
    if (readAttr()) return;
    var q = new URLSearchParams(location.search);
    var ref = doc.referrer || "";
    var channel = "direct";
    if (q.get("utm_source")) channel = q.get("utm_source");
    else if (/instagram/i.test(ref)) channel = "instagram";
    else if (/facebook|fb\./i.test(ref)) channel = "facebook";
    else if (/google/i.test(ref)) channel = "google";
    else if (/bing|yahoo|duckduckgo/i.test(ref)) channel = "search";
    else if (ref && ref.indexOf(location.host) === -1) {
      try { channel = new URL(ref).hostname.replace(/^www\./, ""); } catch (e) { channel = "referral"; }
    }
    try {
      localStorage.setItem(ATTR_KEY, JSON.stringify({
        channel: channel,
        campaign: q.get("utm_campaign") || "",
        medium: q.get("utm_medium") || "",
        landing: location.pathname + location.search,
        first: new Date().toISOString()
      }));
    } catch (e) {}
  })();

  window.sc = window.sc || {};
  window.sc.attr = readAttr;
  window.sc.attrLine = function () {
    var a = readAttr();
    if (!a) return "";
    return [a.channel, a.campaign, a.medium].filter(Boolean).join(" / ");
  };
  window.sc.track = function (name, data) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: name }, data || {}));
    if (window.va) { try { window.va("event", { name: name }); } catch (e) {} }
  };

  doc.addEventListener("click", function (e) {
    var a = e.target.closest("a");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("wa.me") > -1) window.sc.track("whatsapp_click", {});
    else if (href.indexOf("tel:") === 0) window.sc.track("call_click", {});
    else if (href.indexOf("writereview") > -1) window.sc.track("google_review_click", {});
    else if (href.indexOf("maps") > -1) window.sc.track("map_click", {});
  });

  paintStatus();
  setInterval(paintStatus, 60000);
})();
