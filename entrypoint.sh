#!/bin/sh
set -o errexit
set -o pipefail
set -o nounset

export PGPASSWORD=pw_feeder.db
until psql -h db -U feeder_db_admin -d feeder_database -w -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python manage.py migrate --noinput
exec "$@"