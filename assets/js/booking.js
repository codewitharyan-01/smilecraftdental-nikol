/* ==========================================================================
   Smilecraft — appointment enquiry → WhatsApp
   No backend. The visitor's details are assembled into a pre-filled WhatsApp
   message and handed to WhatsApp; delivery happens in the visitor's own app.
   ========================================================================== */
(function () {
  "use strict";

  var form = document.getElementById("enquiry-form");
  if (!form) return;

  var WHATSAPP = "919427451885";
  var STORE = "sc_last_enquiry_v1";

  var $ = function (sel, root) { return (root || form).querySelector(sel); };
  var preview = document.querySelector("[data-preview]");
  var previewBody = document.querySelector("[data-preview-body]");
  var sent = document.querySelector("[data-sent]");
  var waLink = document.querySelector("[data-wa-link]");
  var copyBtn = document.querySelector("[data-copy]");

  /* ---------- Prefill --------------------------------------------------- */
  // ?service=Dental+Implants on a treatment page pre-selects the treatment.
  var params = new URLSearchParams(location.search);
  var preset = params.get("service");
  if (preset) {
    var sel = $("#treatment");
    if (sel) {
      var match = Array.prototype.find.call(sel.options, function (o) {
        return o.value.toLowerCase() === preset.toLowerCase();
      });
      if (match) sel.value = match.value;
    }
  }

  // Returning visitors get their own details back, saved only in their browser.
  try {
    var saved = JSON.parse(localStorage.getItem(STORE) || "null");
    if (saved) {
      ["name", "phone", "email"].forEach(function (k) {
        var el = document.getElementById(k);
        if (el && saved[k] && !el.value) el.value = saved[k];
      });
    }
  } catch (e) {}

  /* ---------- Validation ------------------------------------------------ */
  function fieldOf(el) { return el.closest(".field") || el.parentElement; }

  function setError(el, msg) {
    var f = fieldOf(el);
    el.setAttribute("aria-invalid", "true");
    if (f) {
      f.dataset.invalid = "true";
      var e = f.querySelector(".field__error");
      if (e && msg) e.textContent = msg;
    }
  }
  function clearError(el) {
    var f = fieldOf(el);
    el.removeAttribute("aria-invalid");
    if (f) f.dataset.invalid = "false";
  }

  function validPhone(raw) {
    var d = (raw || "").replace(/\D/g, "");
    if (d.length === 12 && d.indexOf("91") === 0) d = d.slice(2);
    if (d.length === 11 && d.charAt(0) === "0") d = d.slice(1);
    return /^[6-9]\d{9}$/.test(d);
  }

  function validEmail(raw) {
    return !raw || /^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(raw.trim());
  }

  function validate() {
    var ok = true;
    var first = null;

    var name = $("#name");
    if (!name.value.trim() || name.value.trim().length < 2) {
      setError(name, "Please tell us your name.");
      ok = false; first = first || name;
    } else clearError(name);

    var phone = $("#phone");
    if (!validPhone(phone.value)) {
      setError(phone, "Enter a valid 10-digit Indian mobile number.");
      ok = false; first = first || phone;
    } else clearError(phone);

    var email = $("#email");
    if (!validEmail(email.value)) {
      setError(email, "That email address doesn’t look right.");
      ok = false; first = first || email;
    } else clearError(email);

    var treatment = $("#treatment");
    if (!treatment.value) {
      setError(treatment, "Choose the reason for your visit.");
      ok = false; first = first || treatment;
    } else clearError(treatment);

    var consent = $("#consent");
    var consentField = consent.closest(".field") || consent.parentElement;
    if (!consent.checked) {
      consentField.dataset.invalid = "true";
      ok = false; first = first || consent;
    } else {
      consentField.dataset.invalid = "false";
    }

    if (first) {
      first.focus({ preventScroll: false });
      first.scrollIntoView({ behavior: "smooth", block: "center" });
    }
    return ok;
  }

  /* ---------- Message --------------------------------------------------- */
  function prettyDate(iso) {
    if (!iso) return "";
    var d = new Date(iso + "T00:00:00");
    if (isNaN(d)) return iso;
    return d.toLocaleDateString("en-IN", { weekday: "short", day: "numeric", month: "short", year: "numeric" });
  }

  function readForm() {
    var fd = new FormData(form);
    var get = function (k) { return (fd.get(k) || "").toString().trim(); };
    return {
      name: get("name"),
      phone: get("phone"),
      email: get("email"),
      treatment: get("treatment"),
      date: get("date"),
      slot: get("slot"),
      patient: get("patient") || "New patient",
      notes: get("notes")
    };
  }

  function buildMessage(d) {
    var L = [];
    L.push("Hello Smilecraft, I would like to book an appointment.");
    L.push("");
    L.push("Name: " + d.name);
    L.push("Phone: " + d.phone);
    if (d.email) L.push("Email: " + d.email);
    L.push("Referred as: " + d.patient);
    L.push("");
    L.push("Reason for visit: " + d.treatment);
    if (d.date) L.push("Preferred date: " + prettyDate(d.date));
    if (d.slot) L.push("Preferred time: " + d.slot);
    if (d.notes) {
      L.push("");
      L.push("Notes: " + d.notes);
    }
    L.push("");
    var src = (window.sc && window.sc.attrLine) ? window.sc.attrLine() : "";
    L.push("— Sent from the Smilecraft website" + (src ? " (" + src + ")" : ""));
    return L.join("\n");
  }

  function waHref(msg) {
    return "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(msg);
  }

  /* ---------- Live preview ---------------------------------------------- */
  function refreshPreview() {
    if (!preview) return;
    var d = readForm();
    var ready = d.name && validPhone(d.phone) && d.treatment;
    if (!ready) {
      preview.dataset.show = "false";
      return;
    }
    preview.dataset.show = "true";
    if (previewBody) previewBody.textContent = buildMessage(d);
  }
  form.addEventListener("input", refreshPreview);
  form.addEventListener("change", refreshPreview);

  /* ---------- Submit ---------------------------------------------------- */
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    // Honeypot: a real person never fills this hidden field.
    var trap = form.querySelector('input[name="company_website"]');
    if (trap && trap.value) return;

    if (!validate()) return;

    var d = readForm();
    var msg = buildMessage(d);
    var href = waHref(msg);

    try {
      localStorage.setItem(STORE, JSON.stringify({ name: d.name, phone: d.phone, email: d.email }));
    } catch (err) {}

    if (window.sc && window.sc.track) {
      window.sc.track("enquiry_submitted", { treatment: d.treatment, patient: d.patient });
    }

    if (waLink) waLink.href = href;
    window.open(href, "_blank", "noopener");

    if (preview) preview.dataset.show = "false";
    form.hidden = true;
    if (sent) {
      sent.dataset.show = "true";
      sent.scrollIntoView({ behavior: "smooth", block: "center" });
      var h = sent.querySelector("h3");
      if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
    }
  });

  /* ---------- Copy fallback --------------------------------------------- */
  if (copyBtn) {
    copyBtn.addEventListener("click", function () {
      var text = (previewBody && previewBody.textContent) || buildMessage(readForm());
      var done = function () {
        var old = copyBtn.textContent;
        copyBtn.textContent = "Copied to clipboard";
        setTimeout(function () { copyBtn.textContent = old; }, 2000);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(fallback);
      } else fallback();
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand("copy"); done(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
  }

  /* ---------- Date floor = today (IST) ----------------------------------- */
  var dateEl = document.getElementById("date");
  if (dateEl) {
    var now = new Date();
    var ist = new Date(now.getTime() + (330 + now.getTimezoneOffset()) * 60000);
    dateEl.min = ist.toISOString().slice(0, 10);
  }

  refreshPreview();
})();
