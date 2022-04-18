from django.contrib import admin
from .models import Bogie, RailPoint, BogieReceiveRegister, FabBogieRegister, BogieDispatchRegister
# Register your models here.

admin.site.register(Bogie)
admin.site.register(RailPoint)
admin.site.register(BogieReceiveRegister)
admin.site.register(FabBogieRegister)
admin.site.register(BogieDispatchRegister)