web: gunicorn techscan.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=techscan --loglevel=info
