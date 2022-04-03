from django.urls import path, include
from defi import views


urlpatterns = [
    path('', views.DefiHome.as_view(), name='defi_home'),
    #path('STR/', views.STRHomePageView, name='STR_home'),
    #path('CC/', views.CCHomePageView, name='CC_home'),
]