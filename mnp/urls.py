from django.urls import path, include
from mnp import views

urlpatterns = [
    path('AddData/', views.addData, name='MnP_add_data'),
    path('Status/', views.status, name='MnP_status'),
    path('AddMnp/', views.AddMnp, name='AddMnp'),
    path('showmnpdet/<int:Serial>/', views.showmnpdet, name='showmnpdet'),
    path('togglestatus/<int:Serial>/', views.togglestatus, name='togglestatus'),
    path('AddMnpRemark/<int:Serial>/', views.AddMnpRemark, name='AddMnpRemark'),
    #path('ShopAutocomplete/', views.ShopAutocomplete, name='Shop'),
    path('SectionAutocomplete/', views.SectionAutocomplete, name='Section'),
    path('TypeAutocomplete/', views.TypeAutocomplete, name='Type'),
]
