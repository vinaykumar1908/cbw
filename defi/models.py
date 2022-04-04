from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class DPC(models.Model):
    DPCName = models.CharField(max_length=100)
    Date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='dpcauth')
    def __str__(self):
        return self.DPCName

class TC(models.Model):
    TCName = models.CharField(max_length=100)
    Date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='tcauth')
    
    def __str__(self):
        return self.TCName

class MC(models.Model):
    MCName = models.CharField(max_length=100)
    Date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='mcauth')
    
    def __str__(self):
        return self.MCName

class DPCArea(models.Model):
    DPCArea = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.DPCArea

class DPCDef(models.Model):
    DPCDef = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.DPCDef

class DPCRemark(models.Model):
    DPCName = models.ForeignKey(DPC, on_delete=models.CASCADE, related_name='DPCName1')
    Date = models.DateTimeField(default=timezone.now)
    DPCDefArea = models.ForeignKey(DPCArea, on_delete=models.CASCADE, related_name='DPCArea1')
    DPCDef = models.ForeignKey(DPCDef, on_delete=models.CASCADE, related_name='DPCDef1')
    def __str__(self):
        return self.DPCName.DPCName

class TCArea(models.Model):
    TCCArea = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.TCCArea

class TCDef(models.Model):
    TCDef = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.TCDef

class TCRemark(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    TCName = models.ForeignKey(TC, on_delete=models.CASCADE, related_name='TCName1')
    TCDefArea = models.ForeignKey(TCArea, on_delete=models.CASCADE, related_name='TCArea1')
    TCDef = models.ForeignKey(TCDef, on_delete=models.CASCADE, related_name='TCDef1')
    def __str__(self):
        return self.TCName.TCName

class MCArea(models.Model):
    MCArea = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.MCArea

class MCDef(models.Model):
    MCDef = models.CharField(max_length=100, blank=True, null=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.MCDef

class MCRemark(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    MCName = models.ForeignKey(MC, on_delete=models.CASCADE, related_name='MCName1')
    MCDefArea = models.ForeignKey(MCArea, on_delete=models.CASCADE, related_name='MCArea1')
    MCDef = models.ForeignKey(MCDef, on_delete=models.CASCADE, related_name='MCDef1')
    def __str__(self):
        return self.MCName.MCName


