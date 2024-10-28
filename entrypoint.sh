#!/bin/bash

# Apply database migrations
python manage.py migrate

# Collect static files (optional, if you are serving static files)
python manage.py collectstatic --noinput

# Run the Django development server (or use gunicorn for production)
python manage.py runserver 0.0.0.0:8000
