#!/bin/sh
echo waiting for db
./wait-for-it.sh db:5432 -t 5

flask db upgrade
flask seed-db

echo waiting for redis
./wait-for-it.sh redis:6379 -t 5

echo executing gunicorn
gunicorn -b :5000 --access-logfile - --error-logfile - stationaryshop:app --timeout 120
