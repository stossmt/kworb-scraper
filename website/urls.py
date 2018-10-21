from django.urls import path
from website import views as websiteview
from kworb import views as kworbview
from dashboard import views as dashboardview


urlpatterns = [
    path('', websiteview.index, name='index'),
    path('kworb/', kworbview.kworb, name='kworb'),
    path('dashboard/', dashboardview.dashboard, name='dashboard'),
]
