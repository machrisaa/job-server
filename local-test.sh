#!/bin/bash

source .env.graphnet

python ./manage.py migrate

python ./manage.py createsuperuser --noinput

python ./manage.py ensure_admins
python ./manage.py collectstatic --no-input

python ./manage.py runserver localhost:8000
