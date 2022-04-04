from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
class Rake(models.Model):
    Name = models.CharField(max_length=100,unique=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)
    def __str__(self):
        return self.Name

class DPC(models.Model):
    RakeName = models.ForeignKey(Rake, on_delete=models.CASCADE, related_name='RDPC')
    DPCName = models.CharField(max_length=100)
    def __str__(self):
        return self.DPCName

class TC(models.Model):
    RakeName = models.ForeignKey(Rake, on_delete=models.CASCADE, related_name='RTC')
    TCName = models.CharField(max_length=100)
    def __str__(self):
        return self.TCName

class DPCArea(models.Model):
    DPCArea = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.DPCArea

class DPCDef(models.Model):
    DPCDef = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.DPCDef

class DPCRemark(models.Model):
    DPCName = models.ForeignKey(DPC, on_delete=models.CASCADE, related_name='DPCName1')
    DPCDefArea = models.ForeignKey(DPCArea, on_delete=models.CASCADE, related_name='DPCArea1')
    DPCDef = models.ForeignKey(DPCDef, on_delete=models.CASCADE, related_name='DPCDef1')
    def __str__(self):
        return self.DPCName.DPCName

class TCArea(models.Model):
    TCCArea = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.TCArea

class TCDef(models.Model):
    TCDef = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.TCDef

class TCRemark(models.Model):
    TCName = models.ForeignKey(TC, on_delete=models.CASCADE, related_name='TCName1')
    TCDefArea = models.ForeignKey(TCArea, on_delete=models.CASCADE, related_name='TCArea1')
    TCDef = models.ForeignKey(TCDef, on_delete=models.CASCADE, related_name='TCDef1')
    def __str__(self):
        return self.TCName.TCName

