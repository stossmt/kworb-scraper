from django.urls import path
from website import views as websiteview
from kworb import views as kworbview

urlpatterns = [
    path('', websiteview.index, name='index'),
    path('kworb/', kworbview.kworb, name='kworb'),
    path('stats/', kworbview.stats, name='stats'),
]
