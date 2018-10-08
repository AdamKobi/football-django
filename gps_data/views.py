from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RawData
from profiles.models import Player
from rest_framework.views import APIView
from rest_framework.response import Response
from django_pandas.io import read_frame
from pandas import to_datetime
from datetime import date

class GpsDataListView(LoginRequiredMixin,ListView):
    model = RawData
    template_name = 'gps_data/detail.html'
    queryset = RawData.objects.filter(date__year=2018).order_by('-date')[:200]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_queryset()
        df = read_frame(data)
        context['data'] = df.loc[:, df.columns != 'id'].get_values()
        context['headers'] = df.columns[1:].str.replace('_', ' ').str.capitalize()
        return context

class ChartsData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs = RawData.objects.filter(date__year=2018).filter(athlete_id=1)
        df = read_frame(qs)
        default_items = df['duration'].get_values()
        labels = df['date'].dt.date.get_values()
        data = {
            'labels': labels,
            'data': default_items,
        }
        return Response(data)

