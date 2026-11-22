/* ==========================================================================
   Smilecraft — lead capture
   --------------------------------------------------------------------------
   There is no backend. Every form on this site:
     1. validates in the browser,
     2. keeps a draft in this browser only (so a returning visitor is not
        asked to retype anything),
     3. hands the finished enquiry to WhatsApp with the message written out,
     4. optionally also POSTs it to an email endpoint if you set one below.

   TO CHANGE THE RECEIVING NUMBER
     Edit WA_NUMBER — country code + number, digits only, no plus sign.

   TO ALSO RECEIVE ENQUIRIES BY EMAIL (optional, free)
     Create a form at https://web3forms.com, paste the access key into
     WEB3FORMS_KEY. Leave it empty and nothing is posted anywhere.
   ========================================================================== */
(function () {
  "use strict";

  var CONFIG = {
    WA_NUMBER: "919427451885",
    WEB3FORMS_KEY: "",                       // e.g. "a1b2c3d4-...."
    DRAFT_KEY: "sc_draft_v2",
    SOURCE_KEY: "sc_source_v2",
    CARD_KEY: "sc_leadcard_v2"
  };

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var track = window.track || function () {};

  /* ---------------------------------------------------------------------- */
  /* Where did this visitor come from? Stored once, reused for the session.  */
  /* ---------------------------------------------------------------------- */
  var source = (function () {
    try {
      var saved = localStorage.getItem(CONFIG.SOURCE_KEY);
      if (saved) return saved;
    } catch (e) {}

    var p = new URLSearchParams(location.search);
    var label = "direct";
    if (p.get("gclid") || p.get("gad_source")) label = "google ads";
    else if (p.get("utm_source")) label = p.get("utm_source");
    else if (document.referrer) {
      try {
        var host = new URL(document.referrer).hostname.replace(/^www\./, "");
        if (host.indexOf("google.") > -1) label = "google";
        else if (host.indexOf("instagram") > -1) label = "instagram";
        else if (host.indexOf("facebook") > -1) label = "facebook";
        else if (host.indexOf("wa.me") > -1 || host.indexOf("whatsapp") > -1) label = "whatsapp";
        else if (host !== location.hostname) label = host;
      } catch (e) {}
    }
    if (p.get("utm_campaign")) label += " / " + p.get("utm_campaign");
    try { localStorage.setItem(CONFIG.SOURCE_KEY, label); } catch (e) {}
    return label;
  })();

  var LANDING = (function () {
    try {
      var l = sessionStorage.getItem("sc_landing");
      if (!l) { l = location.pathname + location.search; sessionStorage.setItem("sc_landing", l); }
      return l;
    } catch (e) { return location.pathname; }
  })();

  /* ---------------------------------------------------------------------- */
  /* Helpers                                                                */
  /* ---------------------------------------------------------------------- */
  function stamp() {
    try {
      return new Intl.DateTimeFormat("en-GB", {
        timeZone: "Asia/Kolkata", day: "2-digit", month: "short", year: "numeric",
        hour: "2-digit", minute: "2-digit", hour12: true
      }).format(new Date()) + " IST";
    } catch (e) { return new Date().toString(); }
  }

  function digits(v) { return (v || "").replace(/\D/g, ""); }

  function validPhone(v) {
    var d = digits(v);
    if (d.length === 12 && d.indexOf("91") === 0) d = d.slice(2);
    if (d.length === 11 && d.charAt(0) === "0") d = d.slice(1);
    return /^[6-9]\d{9}$/.test(d);
  }

  function normalisePhone(v) {
    var d = digits(v);
    if (d.length === 12 && d.indexOf("91") === 0) d = d.slice(2);
    if (d.length === 11 && d.charAt(0) === "0") d = d.slice(1);
    return d;
  }

  function validEmail(v) { return /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v); }

  function waURL(text) {
    return "https://wa.me/" + CONFIG.WA_NUMBER + "?text=" + encodeURIComponent(text);
  }

  function openWA(text) {
    var url = waURL(text);
    var win = window.open(url, "_blank", "noopener");
    if (!win) location.href = url;
    track("enquiry_submitted", { channel: "whatsapp", source: source });
  }

  /* ---------------------------------------------------------------------- */
  /* Validation                                                             */
  /* ---------------------------------------------------------------------- */
  function fieldWrap(el) {
    return el.closest(".field") || el.closest(".consent") || el.parentElement;
  }

  function setError(el, msg) {
    var f = fieldWrap(el);
    el.setAttribute("aria-invalid", "true");
    if (f) {
      f.setAttribute("data-invalid", "true");
      var e = f.querySelector("[data-error]") || f.querySelector(".field__error");
      if (e) e.textContent = msg;
    }
  }

  function clearError(el) {
    var f = fieldWrap(el);
    el.removeAttribute("aria-invalid");
    if (f) f.removeAttribute("data-invalid");
  }

  function validate(form) {
    var ok = true;
    var first = null;

    $$("[data-required], [data-validate]", form).forEach(function (el) {
      if (el.offsetParent === null && el.type !== "hidden") return;   // inside a hidden wizard step
      if (el.type === "checkbox") {
        if (el.hasAttribute("data-required") && !el.checked) {
          setError(el, "Please tick this box so we can reply.");
          ok = false; first = first || el;
        } else clearError(el);
        return;
      }

      var v = (el.value || "").trim();
      clearError(el);

      if (el.hasAttribute("data-required") && !v) {
        setError(el, "This one is needed.");
        ok = false; first = first || el;
        return;
      }
      if (!v) return;

      if (el.getAttribute("data-validate") === "phone" && !validPhone(v)) {
        setError(el, "Enter a 10-digit mobile number, or the +91 number.");
        ok = false; first = first || el;
      }
      if (el.getAttribute("data-validate") === "email" && !validEmail(v)) {
        setError(el, "That email does not look complete.");
        ok = false; first = first || el;
      }
    });

    if (first) {
      first.focus({ preventScroll: false });
      first.scrollIntoView({ block: "center", behavior: "smooth" });
    }
    return ok;
  }

  /* ---------------------------------------------------------------------- */
  /* Draft memory — this device only                                        */
  /* ---------------------------------------------------------------------- */
  function saveDraft(data) {
    try { localStorage.setItem(CONFIG.DRAFT_KEY, JSON.stringify(data)); } catch (e) {}
  }

  function loadDraft() {
    try { return JSON.parse(localStorage.getItem(CONFIG.DRAFT_KEY) || "null"); } catch (e) { return null; }
  }

  function prefill(form, data) {
    if (!data) {
      var preset = new URLSearchParams(location.search).get("treatment");
      if (preset) {
        var sel = form.querySelector("select[name=treatment]");
        if (sel) {
          Array.prototype.forEach.call(sel.options, function (o) {
            if (o.value.toLowerCase() === preset.toLowerCase()) sel.value = o.value;
          });
        }
        var reason = form.querySelector("[name=reason]");
        if (reason && !reason.value) reason.value = preset;
      }
      return;
    }
    Object.keys(data).forEach(function (k) {
      var el = form.querySelector("[name='" + k + "']");
      if (!el || el.type === "checkbox" || el.type === "radio") return;
      if (!el.value) el.value = data[k];
    });
  }

  /* ---------------------------------------------------------------------- */
  /* Message builder                                                        */
  /* ---------------------------------------------------------------------- */
  function buildMessage(kind, data) {
    var lines = [];
    var title = kind === "booking" ? "NEW APPOINTMENT REQUEST" : kind === "callback" ? "CALLBACK REQUEST" : kind === "leadcard" ? "QUICK ENQUIRY" : "WEBSITE ENQUIRY";
    lines.push(title + " — Smilecraft website");
    lines.push("");
    if (data.name) lines.push("Name: " + data.name);
    if (data.phone) lines.push("Phone: " + data.phone);
    if (data.email) lines.push("Email: " + data.email);
    if (data.patient) lines.push("Patient: " + data.patient);
    if (data.treatment) lines.push("Treatment: " + data.treatment);
    if (data.date) lines.push("Preferred date: " + data.date);
    if (data.time) lines.push("Preferred time: " + data.time);
    if (data.reason) lines.push("Problem: " + data.reason);
    if (data.notes) lines.push("Notes: " + data.notes);
    lines.push("");
    lines.push("Source: " + source + " · " + LANDING);
    lines.push("Sent: " + stamp());
    lines.push("");
    lines.push("— sent from the website booking form");
    return lines.join("\n");
  }

  function collect(form) {
    var data = {};
    $$("input, select, textarea", form).forEach(function (el) {
      if (!el.name) return;
      if (el.type === "checkbox") { if (el.checked) data[el.name] = "yes"; return; }
      if (el.type === "radio") { if (el.checked) data[el.name] = el.value; return; }
      var v = (el.value || "").trim();
      if (v) data[el.name] = el.type === "tel" ? normalisePhone(v) : v;
    });
    return data;
  }

  /* ---------------------------------------------------------------------- */
  /* Optional email delivery (Web3Forms)                                    */
  /* ---------------------------------------------------------------------- */
  function postEmail(payload) {
    if (!CONFIG.WEB3FORMS_KEY) return Promise.resolve(false);
    return fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(Object.assign({
        access_key: CONFIG.WEB3FORMS_KEY,
        subject: "Website enquiry — " + (payload.name || "visitor"),
        from_name: "Smilecraft website"
      }, payload))
    }).then(function (r) { return r.ok; }).catch(function () { return false; });
  }

  /* ---------------------------------------------------------------------- */
  /* Success panel                                                          */
  /* ---------------------------------------------------------------------- */
  function showSent(form, message, data) {
    var shell = form.closest("[data-form-shell]");
    if (!shell) return;
    form.hidden = true;
    var sent = $("[data-sent]", shell);
    if (!sent) return;
    sent.setAttribute("data-show", "true");
    var msgBox = $("[data-sent-message]", sent);
    if (msgBox) msgBox.textContent = message;

    var copyBtn = $("[data-sent-copy]", sent);
    if (copyBtn) copyBtn.setAttribute("data-copy", message);

    var nameOut = $("[data-sent-name]", sent);
    if (nameOut && data.name) nameOut.textContent = data.name.split(" ")[0];
    sent.scrollIntoView({ block: "center", behavior: "smooth" });
    sent.focus && sent.setAttribute("tabindex", "-1");
    if (sent.focus) sent.focus({ preventScroll: true });
    track("lead_captured", { channel: "whatsapp", kind: form.getAttribute("data-lead-form") || "form" });
  }

  /* ---------------------------------------------------------------------- */
  /* Wizard (booking page)                                                  */
  /* ---------------------------------------------------------------------- */
  function initWizard(form) {
    var steps = $$("[data-step]", form);
    if (steps.length < 2) return null;
    var marks = $$("[data-wizard-step]");
    var current = 0;

    function paint() {
      steps.forEach(function (s, i) { s.hidden = i !== current; });
      marks.forEach(function (m, i) {
        m.setAttribute("data-state", i === current ? "active" : i < current ? "done" : "todo");
      });
    }

    function stepValid() {
      var ok = true;
      $$("[data-required], [data-validate]", steps[current]).forEach(function (el) {
        if (el.offsetParent === null) return;
        if (el.type === "checkbox") {
          if (el.hasAttribute("data-required") && !el.checked) { setError(el, "Please tick this box so we can reply."); ok = false; }
          else clearError(el);
          return;
        }
        var v = (el.value || "").trim();
        clearError(el);
        if (el.hasAttribute("data-required") && !v) { setError(el, "This one is needed."); ok = false; return; }
        if (v && el.getAttribute("data-validate") === "phone" && !validPhone(v)) { setError(el, "Enter a 10-digit mobile number."); ok = false; }
        if (v && el.getAttribute("data-validate") === "email" && !validEmail(v)) { setError(el, "That email does not look complete."); ok = false; }
      });
      if (!ok) {
        var bad = $("[data-invalid='true'] input, [data-invalid='true'] select, [data-invalid='true'] textarea", form);
        if (bad) bad.focus();
      }
      return ok;
    }

    $$("[data-next]", form).forEach(function (b) {
      b.addEventListener("click", function () {
        if (!stepValid()) return;
        current = Math.min(current + 1, steps.length - 1);
        paint();
        form.scrollIntoView({ block: "start", behavior: "smooth" });
        var first = $("input:not([type=hidden]), select, textarea", steps[current]);
        if (first) first.focus({ preventScroll: true });
        updatePreview(form);
      });
    });

    $$("[data-back]", form).forEach(function (b) {
      b.addEventListener("click", function () {
        current = Math.max(current - 1, 0);
        paint();
        form.scrollIntoView({ block: "start", behavior: "smooth" });
      });
    });

    paint();
    return { paint: paint, isLast: function () { return current === steps.length - 1; } };
  }

  function updatePreview(form) {
    var preview = document.querySelector("[data-preview]");
    if (!preview) return;
    var data = collect(form);
    var kind = form.getAttribute("data-lead-form") || "booking";
    preview.textContent = buildMessage(kind, data);
  }

  /* ---------------------------------------------------------------------- */
  /* Wire up every form                                                     */
  /* ---------------------------------------------------------------------- */
  $$("[data-lead-form]").forEach(function (form) {
    var wizard = initWizard(form);
    prefill(form, loadDraft());

    $$("input, select, textarea", form).forEach(function (el) {
      el.addEventListener("input", function () {
        clearError(el);
        if (form.getAttribute("data-lead-form") === "booking") updatePreview(form);
      });
      el.addEventListener("change", function () {
        if (form.getAttribute("data-lead-form") === "booking") updatePreview(form);
      });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(form)) return;

      var data = collect(form);
      saveDraft({ name: data.name, phone: data.phone, email: data.email });

      var kind = form.getAttribute("data-lead-form") || "enquiry";
      var message = buildMessage(kind, data);

      var btn = form.querySelector("[type=submit]");
      if (btn) { btn.disabled = true; btn.setAttribute("data-busy", "true"); }

      // The WhatsApp hand-off must happen in the same tick as the click on
      // some mobile browsers, so it is fired before the optional network call.
      openWA(message);
      postEmail(Object.assign({ message: message, source: source, page: LANDING }, data));

      setTimeout(function () {
        if (btn) { btn.disabled = false; btn.removeAttribute("data-busy"); }
        showSent(form, message, data);
        if (wizard) wizard.paint();
      }, 260);
    });

    if (form.getAttribute("data-lead-form") === "booking") updatePreview(form);
  });

  /* ---------------------------------------------------------------------- */
  /* WhatsApp links elsewhere on the site: attach page context              */
  /* ---------------------------------------------------------------------- */
  $$("a[href^='https://wa.me/']").forEach(function (a) {
    if (a.hasAttribute("data-no-prefill")) return;
    var extra = a.getAttribute("data-wa-context");
    if (!extra) return;
    a.setAttribute("href", a.getAttribute("href").split("?")[0] + "?text=" + encodeURIComponent(extra + "\n\n(Source: " + source + " · " + location.pathname + ")"));
  });

  /* ---------------------------------------------------------------------- */
  /* Return-visit card — shown once, never on the booking page, easy to close */
  /* ---------------------------------------------------------------------- */
  (function leadcard() {
    var card = $("[data-leadcard]");
    if (!card) return;

    var skipPages = ["/book.html", "/contact.html", "/thank-you.html"];
    if (skipPages.some(function (p) { return location.pathname.indexOf(p) > -1; })) return;

    var shown = false;
    try {
      var last = parseInt(localStorage.getItem(CONFIG.CARD_KEY) || "0", 10);
      if (Date.now() - last < 12 * 60 * 60 * 1000) return;   // 12 hours
    } catch (e) {}

    function open() {
      if (shown) return;
      var dismissedThisSession = false;
      try { dismissedThisSession = sessionStorage.getItem("sc_card_dismissed") === "1"; } catch (e) {}
      if (dismissedThisSession) return;
      shown = true;
      card.setAttribute("data-open", "true");
      track("leadcard_shown", { source: source });
    }

    function close() {
      card.setAttribute("data-open", "false");
      try {
        localStorage.setItem(CONFIG.CARD_KEY, String(Date.now()));
        sessionStorage.setItem("sc_card_dismissed", "1");
      } catch (e) {}
    }

    var closeBtn = $("[data-leadcard-close]", card);
    if (closeBtn) closeBtn.addEventListener("click", close);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && card.getAttribute("data-open") === "true") close();
    });

    // exit intent on pointer devices, scroll depth on touch
    document.addEventListener("mouseout", function (e) {
      if (e.clientY <= 0 && !e.relatedTarget) open();
    });
    var scrolled = false;
    window.addEventListener("scroll", function () {
      if (scrolled) return;
      var pct = (window.scrollY + window.innerHeight) / document.body.scrollHeight;
      if (pct > 0.58) { scrolled = true; setTimeout(open, 1200); }
    }, { passive: true });

    var cardForm = $("form", card);
    if (cardForm) {
      cardForm.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!validate(cardForm)) return;
        var data = collect(cardForm);
        var msg = buildMessage("leadcard", data);
        saveDraft({ name: data.name, phone: data.phone, email: data.email });
        openWA(msg);
        postEmail(Object.assign({ message: msg, source: source, page: LANDING }, data));
        close();
      });
    }
  })();

  /* Expose a tiny API for inline handlers (e.g. treatment prefill links) */
  window.Smilecraft = {
    source: source,
    waURL: waURL,
    message: buildMessage
  };
})();
