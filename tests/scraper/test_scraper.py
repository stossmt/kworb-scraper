from django.test import TestCase
from bs4 import BeautifulSoup
from kworb import scraper
from kworb.models import Song
from datetime import datetime, date
from decimal import Decimal


class ScrapperTestSuccess(TestCase):

    def test_scrape_date_success(self):
        scraper.scrape(datetime.strptime("03-06-2018", '%m-%d-%Y').date())

        expected = [datetime.strptime("03-06-2018", '%m-%d-%Y').date(), 1, 0, "NF", "Let You Down", 17145, 11, 1104, -161, Decimal('90.583'), Decimal('0.372'), 138, 1]
        actual = list(Song.objects.filter(artist='NF').values_list())

        for count, field in enumerate(expected):
            self.assertEqual(expected[count], actual[0][count+1])

    def calc_url(scrape_date):
        wrong_format = str(scrape_date)
        correct_format = wrong_format.replace("-", "")
        return "http://kworb.net/radio/pop/archives/" + correct_format + ".html"

    def test_calc_url(self):
        actual = scraper.calc_url(date.today())
        expected = 'https://kworb.net/radio/pop/archives/' + str(date.today()).replace("-", "") + '.html'
        self.assertEqual(actual, expected)

    def test_format_song(self):
        song = ['<tr class="d0"><td>49</td><td>--</td><td><div>DRAKE</div></td><td><div>In My Feelings</div></td><td>607</td><td>--</td><td>603</td><td>--</td><td>3.835</td><td>--</td><td>1</td><td>1/10</td><td>49</td><td>607</td><td>603</td><td>3.835</td></tr>',
                     '<tr class="d0"><td>1</td><td>=</td><td><div>ARIANA GRANDE</div></td><td><div>No Tears Left To Cry</div></td><td>16395</td><td>+32</td><td>705</td><td>-167</td><td>94.557</td><td>+0.565</td><td>85</td><td>12/85</td><td>1</td><td>16395</td><td>4665</td><td>94.557</td></tr>']

        for count, s in enumerate(song):
            soup = BeautifulSoup(s, 'html.parser')
            song[count] = scraper.format_song(soup, datetime.strptime("07-14-2018", '%m-%d-%Y').date())

        self.assertEqual(song[0][0], datetime.strptime("07-14-2018", '%m-%d-%Y').date())
        self.assertEqual(song[0][1], '49')
        self.assertEqual(song[0][2], None)
        self.assertEqual(song[0][3], "DRAKE")
        self.assertEqual(song[0][4], "In My Feelings")
        self.assertEqual(song[0][5], '607')
        self.assertEqual(song[0][6], None)
        self.assertEqual(song[0][7], '603')
        self.assertEqual(song[0][8], None)
        self.assertEqual(song[0][9], '3.835')
        self.assertEqual(song[0][10], None)
        self.assertEqual(song[0][11], '1')
        self.assertEqual(song[0][13], '49')

        self.assertEqual(song[1][0], datetime.strptime("07-14-2018", '%m-%d-%Y').date())
        self.assertEqual(song[1][1], '1')
        self.assertEqual(song[1][2], '0')
        self.assertEqual(song[1][3], "ARIANA GRANDE")
        self.assertEqual(song[1][4], "No Tears Left To Cry")
        self.assertEqual(song[1][5], '16395')
        self.assertEqual(song[1][6], '32')
        self.assertEqual(song[1][7], '705')
        self.assertEqual(song[1][8], '-167')
        self.assertEqual(song[1][9], '94.557')
        self.assertEqual(song[1][10], '0.565')
        self.assertEqual(song[1][11], '85')
        self.assertEqual(song[1][13], '1')

    def test_parse_int(self):
        self.assertEqual(scraper.parse_int('='), '0')
        self.assertEqual(scraper.parse_int('+123'), '123')
        self.assertEqual(scraper.parse_int('-1234'), '-1234')
        self.assertEqual(scraper.parse_int(None), None)
        self.assertEqual(scraper.parse_int('--'), '--')

    def test_parse_null(self):
        self.assertEqual(None, scraper.parse_null('--'))
        self.assertEqual('Hello World', scraper.parse_null('Hello World'))
