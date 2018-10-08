from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Player


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'home_page.html'
    model = Player
    queryset = Player.objects.filter(is_active=1)

    def get_context_data(self, **kwargs):
        ctx = super(HomePageView, self).get_context_data(**kwargs)
        ctx['high_risk'] = self.queryset.filter(id=10)
        ctx['med_risk'] = self.queryset.filter(id=2)
        ctx['low_risk'] = self.queryset.filter(id=3)
        for field in ctx['high_risk']:
            print(field)
        return ctx

