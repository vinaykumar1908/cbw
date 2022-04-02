from django.urls import path
from users import views

urlpatterns = [
    path('updateProfile', views.profileUpdate, name='updateProfile'),
]
