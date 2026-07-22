/* ================================================
   Elzain Ali · Medical Logistics Platform
   script.js — Language · Modal · Nav · Form · Anim
   ================================================ */

'use strict';

const LANG_KEY = 'ea_lang';
let currentLang = localStorage.getItem(LANG_KEY) || 'de';

/* ──── 1. LANGUAGE SWITCHER ──── */
function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem(LANG_KEY, lang);

  document.documentElement.lang = lang;
  document.documentElement.dir  = lang === 'ar' ? 'rtl' : 'ltr';
  document.title = lang === 'ar'
    ? 'إلزاين علي – سائق متخصص | نقل المرضى والعينات الطبية'
    : 'Elzain Ali | Professioneller Fahrer – Patienten & Medizin';

  document.querySelectorAll('[data-de]').forEach(el => {
    const val = el.getAttribute('data-' + lang);
    if (!val) return;
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      el.placeholder = val;
    } else if (el.tagName === 'OPTION') {
      el.textContent = val;
    } else if (!el.querySelector('*')) {
      el.innerHTML = val;   // allow &amp; entities in ticker
    }
  });

  const btn = document.getElementById('lang-toggle');
  if (btn) {
    btn.querySelector('.l-de').classList.toggle('active-lang', lang === 'de');
    btn.querySelector('.l-ar').classList.toggle('active-lang', lang === 'ar');
  }

  // Fix Arabic phone direction
  document.querySelectorAll('.phone-display, .phone-val').forEach(el => {
    el.setAttribute('dir', 'ltr');
  });
}

document.getElementById('lang-toggle')
  ?.addEventListener('click', () => applyLanguage(currentLang === 'de' ? 'ar' : 'de'));

// Apply on load
applyLanguage(currentLang);


/* ──── 2. PHOTO MODAL ──── */
(function setupModal() {
  const modal    = document.getElementById('photo-modal');
  const backdrop = document.getElementById('modal-backdrop');
  const closeBtn = document.getElementById('modal-close');
  const modalImg = document.getElementById('modal-img');
  if (!modal) return;

  function open(src, alt) {
    modalImg.src = src;
    modalImg.alt = alt || '';
    modal.removeAttribute('hidden');
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }
  function close() {
    modal.setAttribute('hidden', '');
    document.body.style.overflow = '';
  }

  document.addEventListener('click', e => {
    const trigger = e.target.closest('[data-modal-src]');
    if (trigger) {
      e.preventDefault();
      open(trigger.dataset.modalSrc, trigger.getAttribute('aria-label') || '');
    }
  });

  closeBtn?.addEventListener('click', close);
  backdrop?.addEventListener('click', close);
  document.addEventListener('keydown', e => {
    if (!modal.hasAttribute('hidden') && e.key === 'Escape') close();
  });
})();


/* ──── 3. MOBILE NAV ──── */
(function setupNav() {
  const burger = document.getElementById('burger');
  const nav    = document.getElementById('main-nav');
  if (!burger || !nav) return;

  burger.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    burger.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', String(open));
  });

  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    burger.classList.remove('open');
    burger.setAttribute('aria-expanded', 'false');
  }));

  document.addEventListener('click', e => {
    if (!nav.contains(e.target) && !burger.contains(e.target)) {
      nav.classList.remove('open');
      burger.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });
})();


/* ──── 4. CONTACT FORM ──── */
(function setupForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', e => {
    e.preventDefault();
    const name    = document.getElementById('f-name')?.value.trim();
    const email   = document.getElementById('f-email')?.value.trim();
    const company = document.getElementById('f-company')?.value.trim() || '';
    const service = document.getElementById('f-service')?.value || '';
    const msg     = document.getElementById('f-msg')?.value.trim();

    if (!name || !email || !msg) {
      alert(currentLang === 'ar'
        ? 'يرجى ملء جميع الحقول الإلزامية.'
        : 'Bitte alle Pflichtfelder ausfüllen.');
      return;
    }

    const sub  = service
      ? (currentLang === 'ar' ? 'طلب خدمة: ' : 'Anfrage: ') + service
      : (currentLang === 'ar' ? 'استفسار من الموقع' : 'Anfrage über Lebenslauf-Website');
    const compLine = company ? `\nUnternehmen: ${company}` : '';
    const body = encodeURIComponent(
      `${msg}\n\n──────────────\nName: ${name}${compLine}\nE-Mail: ${email}`
    );
    window.location.href =
      `mailto:zainetsoftg@gmail.com?subject=${encodeURIComponent(sub)}&body=${body}`;
    form.reset();
  });
})();


/* ──── 5. SCROLL ANIMATIONS ──── */
(function setupAnimations() {
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('[data-anim]').forEach(el => el.classList.add('visible'));
    return;
  }
  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('[data-anim]').forEach(el => obs.observe(el));
})();


/* ──── 6. ACTIVE NAV ON SCROLL ──── */
(function setupActiveNav() {
  const sections = document.querySelectorAll('section[id]');
  const links    = document.querySelectorAll('#main-nav a[href*="#"]');
  if (!sections.length) return;

  new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      links.forEach(a => {
        a.classList.toggle('active', a.getAttribute('href').includes('#' + e.target.id));
      });
    });
  }, { rootMargin: '-30% 0px -60% 0px' }).observe;

  // Simpler: just highlight current page link (Flask sets active class via Jinja2)
})();
