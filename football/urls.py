"""football URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.documentation import include_docs_urls

from .views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include_docs_urls(title='Foot-AI API')),
    path('api/auth/', include('accounts.api.urls', namespace='api-auth')),
    path('api/user/', include('accounts.api.user.urls', namespace='api-user')),
    path('api/injuries/', include('injuries.api.urls', namespace='api-injuries')),
    path('api/players/', include('profiles.api.urls', namespace='api-players')),
    path('api/gps/', include('gps_data.api.urls', namespace='api-gps')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^(?P<path>.*)', TemplateView.as_view(template_name='ng.html'), name='home'),
]
