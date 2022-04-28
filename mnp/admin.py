from django.contrib import admin
from .models import MNPShop, MNPSection, MNPType, MnP, MnPRemark
# Register your models here.

admin.site.register(MNPShop)
admin.site.register(MNPSection)
admin.site.register(MNPType)
admin.site.register(MnP)
admin.site.register(MnPRemark)
