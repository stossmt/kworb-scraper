from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from website import celeryconfig

# This document serves as the entrance point to celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

app = Celery('website')

app.config_from_object(celeryconfig)

app.autodiscover_tasks([])
