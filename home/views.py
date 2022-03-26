
from django.views.generic import TemplateView, ListView, DetailView


class HomePageView(TemplateView):
    template_name = 'success.html'

