#!/bin/sh
flask db upgrade
flask seed-db
gunicorn -b :5000 --access-logfile - --error-logfile - stationaryshop:app --timeout 120
