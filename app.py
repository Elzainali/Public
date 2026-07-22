"""
Elzain Ali – Medical Logistics & Transport Platform
Flask backend: Patient/Elderly Transport + Medical Samples/Pharmacy Drugs Transport
DSGVO-compliant · Production-ready · GitHub/Cloud deployment
"""

import os
from flask import Flask, render_template, request, jsonify, redirect, url_for

# Load .env file when running locally (ignored on cloud platforms)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv optional; cloud platforms set env vars directly

# ──────────────────────────────────────────
# App factory
# ──────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-in-production")

# Disable debug in production
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "0") == "1"

# ──────────────────────────────────────────
# Driver / Representative Profile
# ──────────────────────────────────────────
DRIVER_PROFILE = {
    "name":       "Elzain Ali",
    "title":      "Spezialisierter Fahrer – Patienten, Senioren & medizinische Versorgung",
    "phone":      "+49 177 183 26 62",
    "phone_href": "tel:+491771832662",
    "email":      "zainetsoftg@gmail.com",
    "location":   "Ahnsbeck, 29353 Celle, Niedersachsen",
    "photo":      "Ali.jpg",
    "logo":       "elzain.jpg",
    "licenses": [
        "Führerschein Klasse B (seit 2017)",
        "Personenbeförderungsschein § 47/48 FeV (seit 11/2024)",
    ],
    "languages": ["Deutsch (B2)", "Englisch (B2)", "Arabisch (Muttersprache)"],
    "gallery": [
        {"file": "photo1.jpg",                       "alt": "Medikamentenübergabe mit Schutzhandschuhen"},
        {"file": "photo2.jpg",                       "alt": "Medizinische Blutprobe – Versandröhrchen"},
        {"file": "photo3.jpg",                       "alt": "Medizinische Proben – FREIGESTELLTE HUMAN SPECIMEN"},
        {"file": "photo4.jpg",                       "alt": "Medikamenten-Lagerübergabe Apotheke"},
        {"file": "photo5.jpg",                       "alt": "Eilige Arzneimittel Expresslieferung"},
        {"file": "photo6.jpg",                       "alt": "Apothekenfahrer vor APOTHEKE"},
        {"file": "photo8.jpg",                       "alt": "Professionelles Beratungsgespräch"},
        {"file": "photo9.jpg",                       "alt": "Apothekenfahrer – lächelnd am Steuer"},
        {"file": "Screenshot_2026-07-21_122006.jpg", "alt": "Patiententransport – Rollstuhllift"},
        {"file": "Screenshot_2026-07-21_121859.jpg", "alt": "Barrierefreies Transportfahrzeug"},
        {"file": "Screenshot_2026-07-21_122456.jpg", "alt": "Modernes Taxi-/Transportfahrzeug"},
        {"file": "elzain.jpg",                       "alt": "Elzain Ali – Pharmazeutika Transport Logo"},
    ],
}

# ──────────────────────────────────────────
# Services catalogue
# ──────────────────────────────────────────
SERVICES = [
    {
        "id":       "patient-transport",
        "icon":     "🚑",
        "title_de": "Patienten- & Seniorentransport",
        "title_ar": "نقل المرضى وكبار السن",
        "desc_de": (
            "Würdevoller, sicherer und pünktlicher Transport von Patienten und Senioren "
            "zu Arzt-, Therapie- und Dialysetrminen. Einsatz barrierefreier Fahrzeuge "
            "mit Rollstuhlliftern. Einfühlsame Begleitung auf dem gesamten Weg."
        ),
        "desc_ar": (
            "نقل آمن وكريم ومنتظم للمرضى وكبار السن إلى مواعيد الطبيب والعلاج وغسيل الكلى. "
            "استخدام مركبات مجهزة بمصاعد للكراسي المتحركة. مرافقة متعاطفة طوال الرحلة."
        ),
        "features_de": [
            "Rollstuhlgerechte Fahrzeuge mit hydraulischem Lift",
            "Sanfte Fahrweise für empfindliche Patienten",
            "Koordination mit Pflegepersonal & Angehörigen",
            "Zuverlässige Einhaltung aller Termine",
        ],
        "features_ar": [
            "مركبات مجهزة للكراسي المتحركة مع مصعد هيدروليكي",
            "أسلوب قيادة لطيف للمرضى الحساسين",
            "التنسيق مع فريق التمريض والعائلة",
            "التزام موثوق بجميع المواعيد",
        ],
    },
    {
        "id":       "medical-supply",
        "icon":     "💊",
        "title_de": "Medizinische Proben & Apothekenlieferung",
        "title_ar": "نقل الأدوية والعينات من المعامل والصيدليات",
        "desc_de": (
            "Fachgerechter Transport von Blutproben, Laborpräparaten und Apothekenmedikamenten "
            "unter strikter Einhaltung der Kühlkette und aller Hygienevorschriften. "
            "Lückenlose Dokumentation und sichere Übergabe an Kliniken und Labors."
        ),
        "desc_ar": (
            "نقل متخصص لعينات الدم والمستحضرات المختبرية وأدوية الصيدليات مع الالتزام الصارم "
            "بسلسلة التبريد وجميع بروتوكولات النظافة. توثيق كامل وتسليم آمن للعيادات والمختبرات."
        ),
        "features_de": [
            "Einhaltung der gesamten Kühlkette (2–8 °C)",
            "DSGVO-konforme Dokumentation & Übergabe",
            "Strikte Hygieneprotokolle & Schutzausrüstung",
            "Express- und Routenfahrten nach Absprache",
        ],
        "features_ar": [
            "الحفاظ على سلسلة التبريد الكاملة (2-8 درجات مئوية)",
            "توثيق وتسليم متوافق مع اللوائح",
            "بروتوكولات نظافة صارمة ومعدات حماية",
            "رحلات سريعة ودورية حسب الاتفاق",
        ],
    },
]

# ──────────────────────────────────────────
# In-memory booking store (replace with DB in production)
# ──────────────────────────────────────────
_booking_store: list[dict] = []


# ──────────────────────────────────────────
# Routes
# ──────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html", driver=DRIVER_PROFILE, services=SERVICES)


@app.route("/about")
def about():
    return render_template("about.html", driver=DRIVER_PROFILE)


@app.route("/services")
def services():
    return render_template("services.html", driver=DRIVER_PROFILE, services=SERVICES)


@app.route("/services/<service_id>")
def service_detail(service_id: str):
    service = next((s for s in SERVICES if s["id"] == service_id), None)
    if not service:
        return redirect(url_for("services"))
    return render_template("service_detail.html", driver=DRIVER_PROFILE, service=service)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", driver=DRIVER_PROFILE)


@app.route("/contact")
def contact():
    return render_template("contact.html", driver=DRIVER_PROFILE)


@app.route("/impressum")
def impressum():
    return render_template("impressum.html", driver=DRIVER_PROFILE)


@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html", driver=DRIVER_PROFILE)


# ──────────────────────────────────────────
# API
# ──────────────────────────────────────────

@app.route("/api/profile")
def api_profile():
    """Public driver profile (no sensitive contact details)."""
    public = {k: v for k, v in DRIVER_PROFILE.items() if k not in ("phone", "email")}
    public["services"] = [
        {"id": s["id"], "title_de": s["title_de"], "title_ar": s["title_ar"]}
        for s in SERVICES
    ]
    return jsonify(public)


@app.route("/api/booking", methods=["POST"])
def api_booking():
    """Accept a booking request (JSON)."""
    data = request.get_json(silent=True) or {}
    required = ("name", "phone", "service", "date")
    missing = [f for f in required if not data.get(f)]
    if missing:
        return jsonify({"ok": False, "error": f"Missing fields: {missing}"}), 400

    entry = {
        "id":      len(_booking_store) + 1,
        "name":    data["name"],
        "phone":   data["phone"],
        "email":   data.get("email", ""),
        "service": data["service"],
        "date":    data["date"],
        "notes":   data.get("notes", ""),
    }
    _booking_store.append(entry)
    return jsonify({"ok": True, "booking_id": entry["id"]}), 201


# ──────────────────────────────────────────
# Health check (required by most cloud platforms)
# ──────────────────────────────────────────

@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": "elzain-ali-fahrdienst"}), 200


# ──────────────────────────────────────────
# Error handlers
# ──────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", driver=DRIVER_PROFILE), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html", driver=DRIVER_PROFILE), 500


# ──────────────────────────────────────────
# Dev server entry point
# ──────────────────────────────────────────
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
