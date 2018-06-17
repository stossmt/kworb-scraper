web: gunicorn website.wsgi
worker: celery worker --app=website.celeryapp -B --loglevel=info