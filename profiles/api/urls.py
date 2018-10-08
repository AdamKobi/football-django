from django.urls import path
from .views import PlayerAPIView, PlayerRudView

app_name = 'player-api'
urlpatterns = [
    path('', PlayerAPIView.as_view(), name='listcreate'),
    path('<int:pk>/', PlayerRudView.as_view(), name='rud')
]   