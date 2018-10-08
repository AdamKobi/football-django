from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import Player
from .forms import PlayerForm

class PlayerCreateView(LoginRequiredMixin,CreateView):
    model = Player
    form_class = PlayerForm

class PlayerDetailView(LoginRequiredMixin,DetailView):
    model = Player

class PlayerListView(LoginRequiredMixin,ListView):
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goalkeepers'] = self.object_list.filter(position='goalkeeper')
        context['defense'] = self.object_list.filter(position='defender')
        context['midfielder'] = self.object_list.filter(position='midfielder')
        context['forward'] = self.object_list.filter(position='forward')
        return context



