#!/bin/sh
sleep 5
flask db upgrade
sleep 5
flask seed-db
sleep 5
gunicorn -b :5000 --access-logfile - --error-logfile - stationaryshop:app --timeout 120
