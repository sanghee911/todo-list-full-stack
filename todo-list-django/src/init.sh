#!/bin/bash
python check_db_port.py --service-name=db --ip=db --port=5432 && \
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', '', 'root123')" && \
gunicorn django_demo.wsgi -b 0.0.0.0:8000
# gunicorn --workers 3 --bind unix:/src/django_demo/django.sock django_demo.wsgi:application
