from django.urls import path
from .views import InjuryAPIView, InjuryRudView

app_name = 'api'
urlpatterns = [
    path('', InjuryAPIView.as_view(), name='injury-listcreate'),
    path('<int:pk>/', InjuryRudView.as_view(), name='injury-rud')
]   