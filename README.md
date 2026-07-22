# Elzain Ali – Medical Logistics & Transport Platform

**Professioneller Fahrdienst** | Patienten · Senioren · Medizinische Versorgung  
Live-CV & Buchungsplattform · Flask · DSGVO-konform

---

## 📁 Project Structure

```
elzain-ali-fahrdienst/
├── app.py                  ← Flask application (routes, data, config)
├── wsgi.py                 ← WSGI entry point for Gunicorn / cloud
├── requirements.txt        ← Python dependencies
├── Procfile                ← Heroku / Railway / Render process file
├── runtime.txt             ← Python version pin (Heroku/Render)
├── render.yaml             ← One-click Render.com deployment
├── railway.json            ← One-click Railway.app deployment
├── .env.example            ← Environment variable template
├── .gitignore              ← Git exclusions (secrets, cache, venv)
├── templates/
│   ├── base.html           ← Shared header, ticker, footer
│   ├── index.html          ← Home page
│   ├── about.html          ← About / CV page
│   ├── services.html       ← All services
│   ├── service_detail.html ← Individual service detail
│   ├── gallery.html        ← Photo gallery
│   ├── contact.html        ← Contact form
│   ├── impressum.html      ← Legal notice (§ 5 TMG)
│   ├── datenschutz.html    ← Privacy policy (DSGVO)
│   ├── 404.html            ← Not found error page
│   └── 500.html            ← Server error page
└── static/
    ├── css/style.css       ← All styles (no external fonts/CDN)
    ├── js/script.js        ← Language switcher, modal, nav, form
    └── img/                ← All images (13 files)
```

---

## 🚀 Quick Deployment Guide

### Option A — Render.com (Recommended · Free · Frankfurt region)

1. Push this folder to a GitHub repository
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Render detects `render.yaml` automatically → click **Apply**
5. Done — your site is live in ~2 minutes

### Option B — Railway.app

1. Push to GitHub
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub**
3. Select your repo — `railway.json` is detected automatically
4. Add environment variable: `SECRET_KEY` = (a long random string)
5. Done

### Option C — Heroku

```bash
heroku create elzain-ali-fahrdienst
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
heroku config:set FLASK_ENV=production FLASK_DEBUG=0
git push heroku main
```

### Option D — Local Development

```bash
# 1. Clone / unzip the project
cd elzain-ali-fahrdienst

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment
cp .env.example .env
# Edit .env and set a real SECRET_KEY

# 5. Run dev server
python app.py
# → http://localhost:5000
```

### Option E — GitHub Pages (Static only)

> GitHub Pages serves static HTML only — Flask requires a server.  
> Use Render or Railway (both have free tiers) for the full Flask app.  
> Alternatively, export the site as static HTML using `flask freeze` (add `flask-frozen` to requirements).

---

## 🌐 URL Routes

| URL | Page |
|-----|------|
| `/` | Home |
| `/about` | Über mich / CV |
| `/services` | Leistungen |
| `/services/patient-transport` | Patienten- & Seniorentransport |
| `/services/medical-supply` | Medizinische Proben & Apotheke |
| `/gallery` | Galerie |
| `/contact` | Kontakt |
| `/impressum` | Impressum (§ 5 TMG) |
| `/datenschutz` | Datenschutzerklärung (DSGVO) |
| `/health` | Health check (cloud platforms) |
| `GET /api/profile` | Public driver profile (JSON) |
| `POST /api/booking` | Booking request (JSON) |

---

## 🔐 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | **Yes** | Flask session secret — generate with `secrets.token_hex(32)` |
| `FLASK_ENV` | No | `production` (default) or `development` |
| `FLASK_DEBUG` | No | `0` for production, `1` for debug |
| `PORT` | No | Auto-set by cloud platforms; default `5000` |

---

## ✅ DSGVO / Legal Compliance

- ✅ No external fonts (Google Fonts etc.) — system font stack only
- ✅ No CDNs, no tracking scripts, no analytics
- ✅ No cookies set by the application
- ✅ Contact form uses `mailto:` — no server-side data storage
- ✅ Impressum compliant with § 5 TMG / DDG
- ✅ Datenschutzerklärung compliant with EU GDPR / DSGVO
- ✅ Hosting note (GitHub/Render) documented in Datenschutzerklärung

---

## 📞 Contact

**Elzain Ali**  
📱 0177 183 26 62  
✉️ zainetsoftg@gmail.com  
📍 Ahnsbeck, 29353 Celle, Niedersachsen
