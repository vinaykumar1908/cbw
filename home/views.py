
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'success.html'

