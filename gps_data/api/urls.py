from django.urls import path
from .views import GpsAPIView, GpsRudView

app_name = 'api'
urlpatterns = [
    path('', GpsAPIView.as_view(), name='gps-listcreate'),
    path('<int:pk>/', GpsRudView.as_view(), name='gps-rud')
]   