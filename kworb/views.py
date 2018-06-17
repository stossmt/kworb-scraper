from django.http import HttpResponse


def kworb(request):
    return HttpResponse("Kworb")


def stats(request):
    return HttpResponse("stats")