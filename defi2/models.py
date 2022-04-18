from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class DPC0(models.Model):
    DPCName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='dpcauth0')
    def __str__(self):
        return self.DPCName

class TC0(models.Model):
    TCName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    Memu = models.BooleanField(default='False', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='tcauth0')
    
    def __str__(self):
        return self.TCName

class MC0(models.Model):
    MCName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='mcauth0')
    
    def __str__(self):
        return self.MCName

class DPCArea0(models.Model):
    DPCArea = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.DPCArea

class DPCDef0(models.Model):
    DPCDef = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.DPCDef

class DPCSection0(models.Model):
    Section = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Section

class DPCRemark0(models.Model):
    DPCName = models.ForeignKey(DPC0, on_delete=models.DO_NOTHING, related_name='DPCName10')
    Date = models.DateTimeField(default=timezone.now)
    POHDate = models.DateField(null=True, blank=True)
    Section = models.ForeignKey(DPCSection0, on_delete=models.DO_NOTHING, related_name='DPCSection10')
    DPCDefArea = models.ForeignKey(DPCArea0, on_delete=models.DO_NOTHING, related_name='DPCArea10')
    DPCDef = models.ForeignKey(DPCDef0, on_delete=models.DO_NOTHING, related_name='DPCDef10')
    def __str__(self):
        return self.DPCName.DPCName

class TCArea0(models.Model):
    TCCArea = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.TCCArea

class TCDef0(models.Model):
    TCDef = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.TCDef

class TCSection0(models.Model):
    Section = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Section

class TCRemark0(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    TCName = models.ForeignKey(TC0, on_delete=models.DO_NOTHING, related_name='TCName10')
    POHDate = models.DateField(null=True, blank=True)
    Section = models.ForeignKey(TCSection0, on_delete=models.DO_NOTHING, related_name='TCSection10')
    TCDefArea = models.ForeignKey(TCArea0, on_delete=models.DO_NOTHING, related_name='TCArea10')
    TCDef = models.ForeignKey(TCDef0, on_delete=models.DO_NOTHING, related_name='TCDef10')
    def __str__(self):
        return self.TCName.TCName

class MCArea0(models.Model):
    MCArea = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.MCArea

class MCDef0(models.Model):
    MCDef = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.MCDef

class MCSection0(models.Model):
    Section = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Section

class MCRemark0(models.Model):
    Date = models.DateTimeField(default=timezone.now)
    MCName = models.ForeignKey(MC0, on_delete=models.DO_NOTHING, related_name='MCName10')
    POHDate = models.DateField(null=True, blank=True)
    Section = models.ForeignKey(MCSection0, on_delete=models.DO_NOTHING, related_name='MCSection10')
    MCDefArea = models.ForeignKey(MCArea0, on_delete=models.DO_NOTHING, related_name='MCArea1')
    MCDef = models.ForeignKey(MCDef0, on_delete=models.DO_NOTHING, related_name='MCDef1')
    def __str__(self):
        return self.MCName.MCName


