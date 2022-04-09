from django.urls import path, include
from letters import views

urlpatterns = [
    path('', views.LetterView, name='Letter_home'),
    path('Letter/Print', views.LetterPrintPdf, name='LetterPrint'),
]
