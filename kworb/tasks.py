from __future__ import absolute_import, unicode_literals
from kworb.scraper import Scraper
from website.celeryapp import app
from celery.signals import worker_ready


@app.task(name='daily_scrape', bind=True, max_retries=8, soft_time_limit=10, default_retry_delay=30 * 60)
def daily_scrape(self):

    scraper = Scraper()
    try:
        scraper.scrape_today()
    except Exception as exc:
        raise self.retry(exc)


@worker_ready.connect
def at_start(sender=None, **kwargs):
    historical_scrape.delay()


@app.task(bind=True, max_retries=3, soft_time_limit=10 * 60, default_retry_delay=30)
def historical_scrape(self):
    scraper = Scraper()
    try:
        scraper.scrape_historical()
    except Exception as exc:
        raise self.retry(exc)
