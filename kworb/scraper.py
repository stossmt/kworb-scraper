import requests
from kworb.models import Song
from bs4 import BeautifulSoup
from datetime import date, timedelta


class Scraper(object):

    # Scrapes and models today's chart
    def scrape_today(self):
        chart = self.scrape_url(date.today())
        for song in chart:
            self.build_song_model(song)

    # Scrapes and models all charts from 1/1/2017 to today (inclusive)
    def scrape_historical(self):
        date_current = date.today()
        one_day = timedelta(days=1)

        while date_current.year > 2017:
            chart = self.scrape_url(date_current)
            for song in chart:
                self.build_song_model(song)
            date_current -= one_day

    def scrape_date(self, scrape_date):
        queryset = Song.objects.filter(date_created=scrape_date)
        if len(queryset) < 50:
            chart = self.scrape_url(scrape_date)
            for song in chart:
                self.build_song_model(song)

    # Scrapes chart at a given date
    # Returns a list of songs. Each song is a list of that song's attributes
    def scrape_url(self, scrape_date):
        try:
            page = requests.get(self.calc_url(scrape_date))
        except requests.HTTPError:
            print("This Kworb address cannot be accessed")

        try:
            soup = BeautifulSoup(page.content, 'html.parser')
        except BeautifulSoup.HTMLParseError:
            print("HTML Parsing Error")

        # Each index in song_rows is a new row in the html data table
        # Each row contains all data for exactly one song
        # songRows[0] is the chart header information, so it will be omitted
        # songRows[1:50] contains data for all 50 songs

        song_rows = list(soup.find_all("tr"))

        # Iterate through songList (rows)
        # Divide each song (row) into a list of columns
        songs = []
        for song in song_rows[1:51]:
            tempSong = list(song.find_all("td"))
            tempSong.insert(0, scrape_date)

            try:
                self.format_song_data(tempSong)
            except Exception:
                printf("Unable to format data")

            songs.append(tempSong)

        return songs

    # Parameter: <columns> is a list containing a single songs data, used to create a Song model
    def build_song_model(self, columns):
        try:
            Song.objects.create(
                date_created=columns[0],
                position=columns[1],
                position_change=columns[2],
                artist=columns[3],
                title=columns[4],
                spins=columns[5],
                spins_change=columns[6],
                bullet=columns[7],
                bullet_change=columns[8],
                audience=columns[9],
                audience_change=columns[10],
                days=columns[11],
                peak=columns[13]
            )

        except Exception:
            print(columns)
            print("Inputs could not be validated for song model")

    # Generates chart URL based on scrape_date
    def calc_url(self, scrape_date):
        wrong_format = str(scrape_date)
        correct_format = wrong_format.replace("-", "")
        return "http://kworb.net/radio/pop/archives/" + correct_format + ".html"

    # Reformats chart data so that it can be modeled correctly
    def format_song_data(self, columns):
        # Removes html tags
        for index, item in enumerate(columns):
            if index != 0:
                columns[index] = item.get_text()

        # Kworb indicates 'no change' as "=", but model expects an int
        self.format_change(columns, 2)
        self.format_change(columns, 6)
        self.format_change(columns, 8)
        self.format_change(columns, 10)

        for index, item in enumerate(columns):
            if columns[index] == "--":
                columns[index] = None

    # Converts "=" string to "0", converts "+number" to "number"
    def format_change(self, columns, index):
        value = columns[index]
        if value == "=":
            columns[index] = 0
        elif value[0] == "+":
            columns[index] = value[1:]