import unittest
from datetime import date, timedelta
from kworb.scraper import Scraper
from kworb.models import Song
from dashboard import models


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        Song.objects.all().delete()
        scraper = Scraper()

        next_date_to_scrape = date.today()
        one_day = timedelta(days=1)

        for day in range(10):
            chart = scraper.scrape_url(next_date_to_scrape)
            for song in chart:
                scraper.build_song_model(song)
            next_date_to_scrape -= one_day

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        Song.objects.all().delete()