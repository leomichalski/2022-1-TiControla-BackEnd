#!/bin/bash

python manage.py flush --no-input
python manage.py makemigrations user_data
python manage.py migrate
./manage.py createsuperuser --no-input --username=${DJANGO_SUPERUSER_USERNAME} --email=leonardomichalskim@gmail.com
gunicorn core.wsgi:application --bind :8080 --workers 3
