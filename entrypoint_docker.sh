#!/usr/bin/env bash

rm delete_example/migrations/0*  # leave __init__.py intact

./poll_until_db_is_up.sh

./manage.py makemigrations

# Show the Postgres SQL that will be generated and applied
./manage.py sqlmigrate delete_example 0001

./manage.py migrate

chown -R 1001:1001 delete_example/migrations

./manage.py shell_plus --notebook