from django.urls import path
from .views import InjuryDetailView, InjuryListView, InjuryCreateView

app_name = 'injuries'
urlpatterns = [
    path('list/', InjuryListView.as_view(), name='list' ),
    path('new/', InjuryCreateView.as_view(), name='new' ),
    path('<int:pk>/', InjuryDetailView.as_view(), name='detail'),
]