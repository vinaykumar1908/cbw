from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.



class registerWheelDispatchedCDOLKO(models.Model):
    WHEEL_CHOICES = ( 
    ("NotAdded", "NotAdded"),
    ("BCN", "BCN"), 
    ("ICF", "ICF"),
    ) 
    WheelSetNo = models.CharField(max_length=100)
    Type = models.CharField(max_length=11, choices = WHEEL_CHOICES, default = 'NotAdded')
    Date = models.DateField(null=True, blank=True)
    WorkOrderNo = models.CharField(max_length=100, unique=True)
    WorkDone = models.CharField(max_length=500)
    def __str__(self):
        return str(self.WheelSetNo)


class registerWheelDispatchedDSLTKD(models.Model):
    WHEEL_CHOICES = ( 
    ("NotAdded", "NotAdded"),
    ("WAP4", "WAP4"), 
    ("WAP7", "WAP7"),
    ("WDP4", "WDP4"),
    ) 
    WheelSetNo = models.CharField(max_length=100)
    Type = models.CharField(max_length=11, choices = WHEEL_CHOICES, default = 'NotAdded')
    Date = models.DateField(null=True, blank=True)
    WorkOrderNo = models.CharField(max_length=100, unique=True)
    WorkDone = models.CharField(max_length=500)
    def __str__(self):
        return str(self.WheelSetNo)

class registerWheelDispatchedDSLAMV(models.Model):
    WHEEL_CHOICES = ( 
    ("NotAdded", "NotAdded"),
    ("WAP4", "WAP4"), 
    ("WAP7", "WAP7"),
    ("WDP4", "WDP4"),
    ) 
    WheelSetNo = models.CharField(max_length=100)
    Type = models.CharField(max_length=11, choices = WHEEL_CHOICES, default = 'NotAdded')
    Date = models.DateField(null=True, blank=True)
    WorkOrderNo = models.CharField(max_length=100, unique=True)
    WorkDone = models.CharField(max_length=500)
    def __str__(self):
        return str(self.WheelSetNo)


class registerWheelDispatchedCARSHEDGZB(models.Model):
    WHEEL_CHOICES = ( 
    ("NotAdded", "NotAdded"),
    ("DMC", "DMC"),
    ) 
    WheelSetNo = models.CharField(max_length=100)
    Type = models.CharField(max_length=11, choices = WHEEL_CHOICES, default = 'NotAdded')
    Date = models.DateField(null=True, blank=True)
    WorkOrderNo = models.CharField(max_length=100, unique=True)
    WorkDone = models.CharField(max_length=500)
    def __str__(self):
        return str(self.WheelSetNo)


class registerWheelDispatchedELSSRE(models.Model):
    WHEEL_CHOICES = ( 
    ("NotAdded", "NotAdded"),
    ("WAP4", "WAP4"), 
    ("WAP7", "WAP7"),
    ("WDP4", "WDP4"),
    ) 
    WheelSetNo = models.CharField(max_length=100)
    Type = models.CharField(max_length=11, choices = WHEEL_CHOICES, default = 'NotAdded')
    Date = models.DateField(null=True, blank=True)
    WorkOrderNo = models.CharField(max_length=100, unique=True)
    WorkDone = models.CharField(max_length=500)
    def __str__(self):
        return str(self.WheelSetNo)