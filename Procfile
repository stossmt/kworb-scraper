web: gunicorn website.wsgi
worker: celery worker --app=chartwebsite.celeryapp -B --loglevel=info