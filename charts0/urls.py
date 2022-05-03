from django.urls import path, include

from charts0 import views 

urlpatterns = [
    path('', views.chartshome0, name='chartshome0'),
    path('partschart0/', views.partschart0, name='partschart0'),
    path('sectionchart0/', views.sectionchart0, name='sectionchart0'),
    ]
