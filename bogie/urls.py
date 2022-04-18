from django.urls import path, include
from bogie import views


urlpatterns = [
    path('fabricationshop/', views.fabshop, name='fabshop'),
    path('recdispatch/', views.recdispatch, name='recdispatch'),
    path('BogieAutocomplete/', views.BogieAutocomplete, name='BogieAutocomplete'),
    path('SourceAutocomplete/', views.SourceAutocomplete, name='SourceAutocomplete'),
    path('addFabBogie/', views.addFabBogie, name='addFabBogie'),
    path('receiptBogie/', views.receiptBogie, name='receiptBogie'),
    path('dispatchBogie/', views.dispatchBogie, name='dispatchBogie'),
]