from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from injuries.models import Injury
from injuries.forms import InjuryForm
from profiles.models import Player

class InjuryCreateView(LoginRequiredMixin,CreateView):
        
    model = Injury
    template_name = 'injuries/injuries_form.html'
    form_class = InjuryForm

    def get_context_data(self, **kwargs):
        ctx = super(InjuryCreateView, self).get_context_data(**kwargs)
        ctx['form'].fields['athlete'].queryset = Player.objects.filter(is_active=1)
        return ctx

    def form_valid(self, form):
        user = self.request.user
        instance = form.save(commit=False)
        instance.created_by = user
        instance.save()
        return super(InjuryCreateView, self).form_valid(form)


class InjuryDetailView(LoginRequiredMixin,DetailView):
    model = Injury

class InjuryListView(LoginRequiredMixin,ListView):
    model = Injury
    paginate_by = 20