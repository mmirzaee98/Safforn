#!/bin/bash

# Apply database migrations
python manage.py migrate

# Run the Django development server (or use gunicorn for production)
python manage.py runserver 0.0.0.0:8000
