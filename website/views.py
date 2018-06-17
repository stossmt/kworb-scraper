from django.http import HttpResponse
from website.settings import DEBUG


def index(request):
    return HttpResponse(DEBUG)