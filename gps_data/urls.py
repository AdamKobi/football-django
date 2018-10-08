from django.urls import path
from .views import GpsDataListView, ChartsData

app_name = 'gps'
urlpatterns = [
    path('', GpsDataListView.as_view(), name='home' ),
    path('data/', ChartsData.as_view(), name='data' )
]