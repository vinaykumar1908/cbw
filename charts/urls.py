from django.urls import path, include

from charts import views 

urlpatterns = [
    path('', views.chartshome, name='chartshome'),
    path('dpcchart/', views.dpcchart, name='dpcchart'),
    path('tcchart/', views.tcchart, name='tcchart'),
    path('mcchart/', views.mcchart, name='mcchart'),
    ]
