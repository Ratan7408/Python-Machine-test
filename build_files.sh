#!/bin/bash
# Build script for Vercel deployment

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
" 