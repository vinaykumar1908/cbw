from django.contrib import admin
from .models import Rake, DPC, TC, DPCArea, DPCDef, DPCRemark,TCArea, TCDef, TCRemark
# Register your models here.
admin.site.register(Rake)
admin.site.register(DPC)
admin.site.register(TC)
admin.site.register(DPCArea)
admin.site.register(DPCDef)
admin.site.register(DPCRemark)
admin.site.register(TCArea)
admin.site.register(TCDef)
admin.site.register(TCRemark)
