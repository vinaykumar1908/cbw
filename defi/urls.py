from django.urls import path, include
from defi import views


urlpatterns = [
    path('', views.DefiHome2, name='defi_home'),
    path('addDPC/', views.AddDPC, name='addDPC'),
    path('addTC/', views.AddTC, name='addTC'),
    path('addMC/', views.AddMC, name='addMC'),
    path('showDPCdet/<int:Serial>/', views.showDPCdet, name='showDPCdet'),
    path('showTCdet/<int:Serial>/', views.showTCdet, name='showTCdet'),
    path('showMCdet/<int:Serial>/', views.showMCdet, name='showMCdet'),
    path('addDPCpart/<int:Serial>/', views.addDPCpart, name='addDPCpart'),
    path('addDPCdef/<int:Serial>/', views.addDPCdef, name='addDPCdef'),
    path('addDPCremark/<int:Serial>/', views.addDPCRemark, name='addDPCremark'),
    path('addTCpart/<int:Serial>/', views.addTCpart, name='addTCpart'),
    path('addTCdef/<int:Serial>/', views.addTCdef, name='addTCdef'),
    path('addTCremark/<int:Serial>/', views.addTCRemark, name='addTCremark'),
    path('addMCpart/<int:Serial>/', views.addMCpart, name='addMCpart'),
    path('addMCdef/<int:Serial>/', views.addMCdef, name='addMCdef'),
    path('addMCremark/<int:Serial>/', views.addMCRemark, name='addMCremark'),
    path('PartAutocomplete/', views.partAutocomplete, name='partAutocomplete'),
    path('DefAutocomplete/', views.defAutocomplete, name='defAutocomplete'),
    path('TCPartAutocomplete/', views.TCpartAutocomplete, name='TCpartAutocomplete'),
    path('TCDefAutocomplete/', views.TCdefAutocomplete, name='TCdefAutocomplete'),
    path('MCPartAutocomplete/', views.MCpartAutocomplete, name='MCpartAutocomplete'),
    path('MCDefAutocomplete/', views.MCdefAutocomplete, name='MCdefAutocomplete'),
    #path('CC/', views.CCHomePageView, name='CC_home'),
]