"""
Paramarsh Construction - WSGI Entry Point
===================================

This file serves as the WSGI (Web Server Gateway Interface) entry point
for production deployment of the Paramarsh application.

WSGI is a specification that describes how a web server communicates with
web applications. This file allows the application to be deployed using
production WSGI servers like Gunicorn, uWSGI, or mod_wsgi.

Usage:
- Development: python app.py
- Production: gunicorn wsgi:app

Author: Paramarsh Construction Team
Version: 1.0.0
"""

# Import the Flask application instance from the main app module
from app import app

# WSGI application object that production servers will use
# This is the standard way to expose a Flask app to WSGI servers
application = app

if __name__ == "__main__":
    """
    Entry point when the script is run directly.
    
    This allows the WSGI file to be used for both development and production.
    In development, you can run: python wsgi.py
    In production, WSGI servers will use the 'app' object directly.
    """
    # Run the Flask development server
    # Note: In production, use a proper WSGI server instead
    app.run(debug=False, host='0.0.0.0', port=5001) 