# Paramarsh Construction - Procfile
# ==========================
#
# This file tells the web server (like Heroku, Render, etc.) how to run the application.
# It defines the process types and their commands.
#
# The 'web' process type is the main application that handles HTTP requests.
# Other process types (like 'worker' for background jobs) can be added here.
#
# Author: Paramarsh Construction Team
# Version: 1.0.0

# Web process - runs the main Flask application
# Uses Gunicorn WSGI server for production deployment
# $PORT is provided by the hosting platform (Heroku, Render, etc.)
web: gunicorn --bind 0.0.0.0:$PORT app:app 