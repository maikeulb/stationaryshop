#!/bin/sh
# this script is used to boot a Docker container
flask db upgrade
flask seed-db
exec gunicorn -b :5000 --access-logfile - --error-logfile - stationaryshop:app
