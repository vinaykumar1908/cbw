from django.urls import path, include
from defi import views


urlpatterns = [
    path('', views.DefiHome2, name='defi_home'),
    path('addRake/', views.AddRake, name='addRake'),
    #path('CC/', views.CCHomePageView, name='CC_home'),
]