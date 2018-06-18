from celery.schedules import crontab
import os


broker_url = 'amqp://XKyqKfqq:Y6Pz7q5VZWG8C4bAexzmDvwBU-keK6CY@angry-nightshade-929.bigwig.lshift.net:10005/NJaxOldf9DEk'
result_backend = 'redis://h:p6d4500ea009229883ce860047c6e00e13273ec4e7f8e0b9e598f7c21fe906061@ec2-34-207-32-74.compute-1.amazonaws.com:13549'

task_serializer = 'json'
result_serializer = 'json'

result_persistent = False
result_expires = 3600

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}
task_soft_time_limit = 420

accept_content = ['application/json']

beat_schedule = {
    'daily-scrape': {
        'task': 'kworb.tasks.daily_scrape',
        'schedule': crontab(hour=8),
    },
}