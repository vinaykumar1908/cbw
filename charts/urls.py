from django.urls import path, include

from charts import views 

urlpatterns = [
    path('', views.chartshome, name='chartshome'),
    path('partschart/', views.partschart, name='partschart'),
    path('sectionchart/', views.sectionchart, name='sectionchart'),
    path('partdata/', views.partsdata, name='partsdata'),
    ]
