from django.urls import path, include

from charts0 import views 

urlpatterns = [
    path('', views.chartshome0, name='chartshome0'),
    path('dpcchart0/', views.dpcchart0, name='dpcchart0'),
    path('tcchart0/', views.tcchart0, name='tcchart0'),
    path('mcchart0/', views.mcchart20, name='mcchart20'),
    ]
