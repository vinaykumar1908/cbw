from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class MNPShop(models.Model):
    Shop = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Shop

class MNPSection(models.Model):
    Shop = models.ForeignKey(MNPShop, on_delete=models.DO_NOTHING, related_name='MNPSecShop')
    Section = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.Shop}'s {self.Section}"

class MNPType(models.Model):
    Type = models.CharField(max_length=100, blank=True, null=True, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.Type

class MnP(models.Model):
    MachineName = models.CharField(max_length=100)
    UpdateDate = models.DateField(null=True, blank=True)
    ManufacDate = models.DateField(null=True, blank=True)
    EsttDate = models.DateField(null=True, blank=True)
    LastOverhaulDate = models.DateField(null=True, blank=True)
    LastCalibDate = models.DateField(null=True, blank=True)
    Shop = models.ForeignKey(MNPShop, on_delete=models.DO_NOTHING, related_name='MNPShop')
    Section = models.ForeignKey(MNPSection, on_delete=models.DO_NOTHING, related_name='MNPSection')
    Type = models.ForeignKey(MNPType, on_delete=models.DO_NOTHING, related_name='MNPType')
    pic = models.FileField(upload_to='uploadsMNPpics/%Y/%m/%d/', blank=True, null=True)
    MnPStatus = models.BooleanField(default='False', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='mnpauth')
    def __str__(self):
        return f"{self.MachineName}"

class MnPRemark(models.Model):
    MachineName = models.ForeignKey(MnP, on_delete=models.DO_NOTHING, related_name='mnpmachrem')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='mnpremauth')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    commentfile = models.FileField(upload_to='uploadsMNPRemark/%Y/%m/%d/', blank=True, null=True)
    def __str__(self):
        return f"{self.MachineName}: Date:{self.created_date}: Text:{self.approved_comment}"