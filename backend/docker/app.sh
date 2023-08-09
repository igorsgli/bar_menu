#!/bin/bash

python manage.py migrate

python manage.py collectstatic --no-input

python manage.py load

gunicorn config.wsgi:application --bind 0:8000
