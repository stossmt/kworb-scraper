from __future__ import absolute_import, unicode_literals
from kworb.scraper import scrape_today, scrape
from website.celeryapp import app
from celery.signals import worker_ready
from datetime import datetime, date, timedelta


@app.task(name='daily_scrape', bind=True, max_retries=8, soft_time_limit=10, default_retry_delay=30 * 60)
def daily_scrape(self):
    try:
        scrape_today()
    except Exception as exc:
        raise self.retry(exc)


@worker_ready.connect
def at_start(sender=None, **kwargs):
    historical_scrape.delay()


@app.task(bind=True, max_retries=3, soft_time_limit=10 * 60, default_retry_delay=30)
def historical_scrape(self):
    date_current = date.today()
    one_day = timedelta(days=1)

    while date_current.year > 2017:
        try:
            scrape(date_current)
        except Exception as exc:
            raise self.retry(exc)

        date_current -= one_day
