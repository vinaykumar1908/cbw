from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.



class DefiHome(LoginRequiredMixin, TemplateView):
    template_name = 'deficiencies/defhome.html'