from django.contrib import admin
from .models import DPC, TC,MC, DPCArea, DPCDef, DPCRemark,TCArea, TCDef, TCRemark, MCArea, MCDef, MCRemark
# Register your models here.

admin.site.register(DPC)
admin.site.register(TC)
admin.site.register(MC)
admin.site.register(DPCArea)
admin.site.register(DPCDef)
admin.site.register(DPCRemark)
admin.site.register(TCArea)
admin.site.register(TCDef)
admin.site.register(TCRemark)
admin.site.register(MCArea)
admin.site.register(MCDef)
admin.site.register(MCRemark)
