import requests
from kworb.models import Song
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError


def scrape(scrape_date):
    chart = scrape_url(scrape_date)
    for song in chart:
        build_song_model(song)


def scrape_url(scrape_date):
    page = requests.get(calc_url(scrape_date))
    soup = BeautifulSoup(page.content, 'html.parser')

    song_list = list(soup.find_all("tr"))[1:51]

    for count, song in enumerate(song_list):
        song_list[count] = format_song(song, scrape_date)

    return song_list


def calc_url(scrape_date):
    date_string = str(scrape_date).replace("-", "")
    return "https://kworb.net/radio/pop/archives/" + date_string + ".html"


def build_song_model(song):
    try:
        Song.objects.create(
            date_created=song[0],
            position=song[1],
            position_change=song[2],
            artist=song[3],
            title=song[4],
            spins=song[5],
            spins_change=song[6],
            bullet=song[7],
            bullet_change=song[8],
            audience=song[9],
            audience_change=song[10],
            days=song[11],
            peak=song[13]
        )

    except ValidationError:
        print('Inputs could not be validated for song model' + song)


def format_song(song, scrape_date):
    song = list(song.find_all("td"))

    for count, field in enumerate(song):
        field = field.get_text()
        field = parse_null(field)
        if count in {1, 5, 6, 9}:
            field = parse_int(field)
        song[count] = field

    song.insert(0, scrape_date)
    return song


def parse_int(string):
    if string is None:
        return string
    elif string == "=":
        return '0'
    elif string[0] == "+":
        return string[1:]
    else:
        return string


def parse_null(value):
    if value == "--":
        return None
    return value
