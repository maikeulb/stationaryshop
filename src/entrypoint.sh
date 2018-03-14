#!/bin/sh
# this script is used to boot a Docker container
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - stationaryshop:app
