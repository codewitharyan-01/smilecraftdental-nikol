/* ==========================================================================
   Smilecraft — upgrade behaviours
   Treatment finder, booking slot picker, FAQ search, sticky book bar, to-top.
   ========================================================================== */
(function () {
  "use strict";

  var doc = document;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Reveal variants + zoom reveal ------------------------------- */
  doc.querySelectorAll("[data-stagger]").forEach(function (group) {
    Array.prototype.slice.call(group.querySelectorAll("[data-reveal]")).forEach(function (el, i) {
      if (!el.style.getPropertyValue("--i")) el.style.setProperty("--i", i);
    });
  });

  var targets = doc.querySelectorAll("[data-reveal]:not(.is-in), .zoom-reveal, .draw-line");
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        io.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---------- Treatment finder -------------------------------------------- */
  var finder = doc.querySelector("[data-finder]");
  if (finder) {
    var MAP = {
      "Toothache": {
        title: "Probably a cavity, or the nerve is involved",
        text: "If the pain lingers after something hot or cold, or wakes you at night, the nerve is likely inflamed. That means a filling if it is caught early, or a root canal if it is not.",
        link: "treatments/root-canal.html",
        label: "Read about root canal treatment"
      },
      "Sensitivity": {
        title: "Usually exposed root or worn enamel",
        text: "A short sharp sting that passes quickly is often gum recession or enamel wear. A check-up, a desensitising treatment or a small filling usually settles it.",
        link: "book.html?service=Check-up+%2F+not+sure+yet",
        label: "Book a check-up"
      },
      "Bleeding gums": {
        title: "Gum inflammation — worth treating early",
        text: "Bleeding when brushing is the first sign of gingivitis. A scaling and polishing with proper home care reverses it; left alone it becomes periodontal disease.",
        link: "book.html?service=Scaling+%26+gum+care",
        label: "Book a cleaning"
      },
      "A missing tooth": {
        title: "An implant, a bridge, or a partial denture",
        text: "Three routes, and the right one depends on the bone and the teeth either side. An implant leaves the neighbours untouched; a bridge is faster and cheaper.",
        link: "treatments/dental-implants.html",
        label: "Read about implants"
      },
      "Crooked teeth": {
        title: "Orthodontics — braces or clear aligners",
        text: "Crowding is easier to clean once straightened, which is why it matters beyond appearance. Aligners suit mild to moderate cases; braces handle the complex ones.",
        link: "treatments/braces-aligners.html",
        label: "Read about braces and aligners"
      },
      "Stained teeth": {
        title: "Whitening first, veneers only if shape is the issue",
        text: "Surface stain comes off with a polish. Deeper discolouration responds to bleaching. If the teeth are also chipped or uneven, that is a smile design conversation.",
        link: "treatments/smile-design.html",
        label: "Read about smile design"
      }
    };

    var chips = finder.querySelectorAll("[data-symptom]");
    var panel = finder.querySelector("[data-finder-result]");
    var rTitle = finder.querySelector("[data-finder-title]");
    var rText = finder.querySelector("[data-finder-text]");
    var rLink = finder.querySelector("[data-finder-link]");

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var key = chip.dataset.symptom;
        var data = MAP[key];
        if (!data) return;
        chips.forEach(function (c) { c.setAttribute("aria-pressed", "false"); });
        chip.setAttribute("aria-pressed", "true");
        rTitle.textContent = data.title;
        rText.textContent = data.text;
        rLink.textContent = data.label;
        rLink.href = data.link;
        panel.dataset.show = "true";
        if (!reduce) panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
      });
    });
  }

  /* ---------- Booking: real slot picker ----------------------------------- */
  var dateEl = doc.getElementById("date");
  var slotWrap = doc.querySelector("[data-slot-grid]");
  var slotInput = doc.getElementById("slot");
  var slotNote = doc.querySelector("[data-slot-note]");

  if (dateEl) {
    var today = new Date();
    var istNow = new Date(today.getTime() + (330 + today.getTimezoneOffset()) * 60000);
    var minISO = istNow.toISOString().slice(0, 10);
    dateEl.min = minISO;

    // Build 30-minute slots 09:00 → 20:30
    var SLOTS = [];
    for (var m = 9 * 60; m <= 20 * 60 + 30; m += 30) {
      var h = Math.floor(m / 60), mm = m % 60;
      var hh = h % 12 === 0 ? 12 : h % 12;
      SLOTS.push({
        mins: m,
        label: hh + ":" + (mm < 10 ? "0" + mm : mm) + " " + (h >= 12 ? "PM" : "AM")
      });
    }

    function renderSlots() {
      if (!slotWrap || !slotInput) return;
      var val = dateEl.value;
      slotWrap.innerHTML = "";
      slotInput.value = "";
      if (!val) {
        slotWrap.hidden = true;
        if (slotNote) slotNote.dataset.show = "false";
        return;
      }
      var d = new Date(val + "T00:00:00");
      var day = d.getDay();

      if (day === 0) {
        slotWrap.hidden = true;
        if (slotNote) {
          slotNote.textContent = "Sundays are closed. Please pick Monday to Saturday, or message us and we will find another time.";
          slotNote.dataset.show = "true";
          slotNote.classList.add("slot-note--warn");
        }
        return;
      }
      if (slotNote) { slotNote.dataset.show = "false"; slotNote.classList.remove("slot-note--warn"); }

      slotWrap.hidden = false;
      var isToday = val === minISO;
      var nowMins = istNow.getHours() * 60 + istNow.getMinutes();

      SLOTS.forEach(function (s) {
        var b = doc.createElement("button");
        b.type = "button";
        b.className = "slot";
        b.textContent = s.label;
        b.setAttribute("aria-pressed", "false");
        b.dataset.label = s.label;
        if (isToday && s.mins <= nowMins + 60) {
          b.disabled = true;
          b.title = "Too soon — pick a later time";
        }
        b.addEventListener("click", function () {
          slotWrap.querySelectorAll(".slot").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
          b.setAttribute("aria-pressed", "true");
          slotInput.value = s.label;
          slotInput.dispatchEvent(new Event("change", { bubbles: true }));
        });
        slotWrap.appendChild(b);
      });
    }

    dateEl.addEventListener("change", renderSlots);
    if (dateEl.value) renderSlots();
  }

  /* ---------- FAQ search --------------------------------------------------- */
  var search = doc.querySelector("[data-faq-search]");
  if (search) {
    var items = Array.prototype.slice.call(doc.querySelectorAll(".faq__item"));
    var empty = doc.querySelector("[data-faq-empty]");
    search.addEventListener("input", function () {
      var q = search.value.trim().toLowerCase();
      var shown = 0;
      items.forEach(function (item) {
        var text = item.textContent.toLowerCase();
        var hit = !q || text.indexOf(q) > -1;
        item.hidden = !hit;
        if (hit) shown++;
      });
      if (empty) empty.dataset.show = String(shown === 0);
    });
  }

  /* ---------- Sticky book bar + back to top -------------------------------- */
  var bar = doc.querySelector("[data-sticky-book]");
  var toTop = doc.querySelector("[data-to-top]");

  function onScroll() {
    var y = window.pageYOffset;
    if (bar) bar.dataset.show = String(y > 520);
    if (toTop) toTop.dataset.show = String(y > 900);
  }
  if (bar || toTop) {
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
  if (toTop) {
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
    });
  }

  /* ---------- Auto-advance review carousel -------------------------------- */
  var track = doc.querySelector("[data-slider-track]");
  if (track && !reduce) {
    var paused = false;
    ["pointerdown", "mouseenter", "focusin"].forEach(function (ev) {
      track.addEventListener(ev, function () { paused = true; });
    });
    ["mouseleave", "focusout"].forEach(function (ev) {
      track.addEventListener(ev, function () { paused = false; });
    });
    setInterval(function () {
      if (paused || doc.hidden) return;
      var card = track.firstElementChild;
      if (!card) return;
      var step = card.getBoundingClientRect().width + 16;
      if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 8) {
        track.scrollTo({ left: 0, behavior: "smooth" });
      } else {
        track.scrollBy({ left: step, behavior: "smooth" });
      }
    }, 5200);
  }

  /* ---------- Video: play only when visible ------------------------------- */
  var vids = doc.querySelectorAll("[data-autoplay]");
  if (vids.length && "IntersectionObserver" in window) {
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) {
          var p = v.play();
          if (p && p.catch) p.catch(function () {});
        } else {
          v.pause();
        }
      });
    }, { threshold: 0.35 });
    vids.forEach(function (v) { vio.observe(v); });
  }
})();
