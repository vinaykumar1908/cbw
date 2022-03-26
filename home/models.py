from django.db import models

# Create your models here.
#from django.db import models
#from django.db import models
#from django.urls import reverse
#from django.utils import timezone
#from django.utils.translation import gettext_lazy as _
# Create your models here.
#from django.db import models
#from stores import models as SM
#import math
# Create your models here.


# class p(models.Model):

#     Item = models.CharField(unique=True, max_length=100, default="NULL")
#     PL_Number = models.BigIntegerField(unique=True, null=True)
#     AAC = models.IntegerField(null=True)
#     Stock = models.IntegerField(null=True)
#     updateTime = models.DateTimeField(default=timezone.now)
#     MAC = models.IntegerField(default=00, blank=True)
#     critical = models.CharField(max_length=30, null=True, blank=True)

#     def __str__(self):
#         return str(self.Item)

#     def MACfun(self):
#         self.MAC = math.floor((self.AAC)/12)
#         self.save()
#         print(self.MAC)
#         return self.MAC

#     def criticalFun(self):
#         x = self.AAC
#         y = x/12
#         z = x/2
#         l = self.Stock
#         if l <= y:
#             self.critical = "Critical Item"
#             self.save()
#             return self.critical
#         elif l >= y and l <= z:
#             self.critical = "Hot Item"
#             self.save()
#             return self.critical
#         elif l >= z and l <= x:
#             self.critical = "Not Critical"
#             self.save()
#             return self.critical
#         elif l > x:
#             self.critical = "Stock Enough for 1 Year"
#             self.save()
#             return self.critical

#     def filterCriticalFun(self):
#         qs = p.objects.all().exclude(critical="Not Critical").exclude(critical="Stock Enough for 1 Year").exclude(critical="Hot Item")
#         return qs
