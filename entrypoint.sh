#!/bin/sh

source ../.env
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn app.wsgi:application --bind 0.0.0.0:8000 --log-level debug

