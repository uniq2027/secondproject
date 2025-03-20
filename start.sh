#!/bin/bash

# Run database migrations (if needed)
python manage.py migrate

# Start the Django app with Waitress
waitress-serve --listen=0.0.0.0:10000 myproject.wsgi:application
