from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# This document serves as the entrance point to celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

app = Celery('website')

app.config_from_object(celeryconfig)

app.autodiscover_tasks([])

# Dumps its own request information
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))