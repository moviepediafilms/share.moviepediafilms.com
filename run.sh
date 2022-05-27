#!/bin/bash

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:80 --access-logfile - --workers 3 --capture-output wsgi:app
