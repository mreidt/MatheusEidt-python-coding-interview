#!/bin/sh
set -e
. /venv/bin/activate

[ ! -f "/store/docker/local/vars.env" ] \
&& echo 'Unable to find docker/local/vars.env' \
&& exit 1

while read -r line; do
    echo $line | grep . | grep -v '^#' && export $line
done < /store/docker/local/vars.env

/wait && gunicorn --reload store.wsgi --workers 1 --bind 0.0.0.0:8000 --timeout 360 --log-level debug --preload
