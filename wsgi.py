"""
WSGI entry point for production deployment.
Used by Gunicorn, Railway, Render, Heroku, etc.

Usage:
  gunicorn wsgi:app
  gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2
"""

from app import app

if __name__ == "__main__":
    app.run()
