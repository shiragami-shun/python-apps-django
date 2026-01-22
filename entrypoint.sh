#!/bin/sh
set -e

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Starting gunicorn..."
gunicorn python_apps_django.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 2 \
  --threads 4
