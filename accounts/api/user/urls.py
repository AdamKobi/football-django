from django.urls import path, include
from django.contrib import admin

from .views import UserDetailAPIView

app_name = 'api-user'

urlpatterns = [
    path('<str:email>/', UserDetailAPIView.as_view(), name='detail'),
]