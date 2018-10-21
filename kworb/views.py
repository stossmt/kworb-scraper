from django.shortcuts import render
from datetime import date, timedelta
from kworb.models import Song
import json


def kworb(request):
    chart = list(Song.objects.filter(date_created=date.today()).values_list())

    if not chart:
        chart = list(Song.objects.filter(date_created=date.today()-timedelta(days=1)).values_list())

    chart = parse_null(chart)

    context = {'chart_today': json.dumps(chart, default=str)}
    return render(request, 'kworb.html', context)


def parse_null(chart):
    parsed = []

    for index, song in enumerate(chart):
        parsed.append([])
        parsed[index] = ["--" if field is None else field for field in song]

    return parsed
