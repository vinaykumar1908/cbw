from django.urls import path, include
from defi2 import views


urlpatterns = [
    path('', views.DefiHome20, name='defi_home0'),
    path('addDPC0/', views.AddDPC0, name='addDPC0'),
    path('addTC0/', views.AddTC0, name='addTC0'),
    path('addMC0/', views.AddMC0, name='addMC0'),
    path('showDPCdet0/<int:Serial>/', views.showDPCdet0, name='showDPCdet0'),
    path('showTCdet0/<int:Serial>/', views.showTCdet0, name='showTCdet0'),
    path('showMCdet0/<int:Serial>/', views.showMCdet0, name='showMCdet0'),
    path('addDPCpart0/<int:Serial>/', views.addDPCpart0, name='addDPCpart0'),
    path('addDPCdef0/<int:Serial>/', views.addDPCdef0, name='addDPCdef0'),
    path('addDPCremark0/<int:Serial>/', views.addDPCRemark0, name='addDPCremark0'),
    path('addTCpart0/<int:Serial>/', views.addTCpart0, name='addTCpart0'),
    path('addTCdef0/<int:Serial>/', views.addTCdef0, name='addTCdef0'),
    path('addTCremark0/<int:Serial>/', views.addTCRemark0, name='addTCremark0'),
    path('addMCpart0/<int:Serial>/', views.addMCpart0, name='addMCpart0'),
    path('addMCdef0/<int:Serial>/', views.addMCdef0, name='addMCdef0'),
    path('addMCremark0/<int:Serial>/', views.addMCRemark0, name='addMCremark0'),
    path('PartAutocomplete0/', views.partAutocomplete0, name='partAutocomplete0'),
    path('DefAutocomplete0/', views.defAutocomplete0, name='defAutocomplete0'),
    path('SecAutocomplete0/', views.SecAutocomplete0, name='secAutocomplete0'),
    path('TCSecAutocomplete0/', views.TCSecAutocomplete0, name='TCsecAutocomplete0'),
    path('TCPartAutocomplete0/', views.TCpartAutocomplete0, name='TCpartAutocomplete0'),
    path('TCDefAutocomplete0/', views.TCdefAutocomplete0, name='TCdefAutocomplete0'),
    path('MCPartAutocomplete0/', views.MCpartAutocomplete0, name='MCpartAutocomplete0'),
    path('MCDefAutocomplete0/', views.MCdefAutocomplete0, name='MCdefAutocomplete0'),
    path('MCSecAutocomplete0/', views.MCSecAutocomplete0, name='MCsecAutocomplete0'),
    path('DTMsectionAutocomplete0/', views.DTMsectionAutocomplete0, name='DTMsectionAutocomplete0'),
    path('DTMpartAutocomplete0/', views.DTMpartAutocomplete0, name='DTMpartAutocomplete0'),
    #path('CC/', views.CCHomePageView, name='CC_home'),
    path('List0/', views.DefiListHome20, name='defi_list_home0'),
    path('DTMsearch0/', views.DTMsearch0, name='DTMsearch0'),

    path('Exporthome0/', views.Exporthome0, name='Export_home0'),
    path('ExportExcel0/', views.ExportExcel0, name='exportexcel0'),
]