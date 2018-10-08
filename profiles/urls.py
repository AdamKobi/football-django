from django.urls import path
from .views import PlayerCreateView, PlayerDetailView, PlayerListView

app_name = 'profiles'
urlpatterns = [
    path('', PlayerListView.as_view(), name='list' ),
    path('new/', PlayerCreateView.as_view(), name='new' ),
    path('<int:pk>/', PlayerDetailView.as_view(), name='detail'),
]