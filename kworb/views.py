from django.http import HttpResponse
from django.shortcuts import render


def kworb(request):
    return HttpResponse("Kworb")


def dashboard(request):
    return render(request, 'dashboard.html')