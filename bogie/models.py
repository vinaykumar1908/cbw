from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class Bogie(models.Model):
    BogieType = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    Quantity = models.IntegerField(blank=True,null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='bogieuser')
    def __str__(self):
        return self.BogieType

class RailPoint(models.Model):
    PlaceName = models.CharField(max_length=100, unique=True)
    Date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='railpointuser')
    def __str__(self):
        return self.PlaceName

class BogieReceiveRegister(models.Model):
    BogieType = models.ForeignKey(Bogie, on_delete=models.DO_NOTHING, related_name='BogieTypeRec')
    PlaceName = models.ForeignKey(RailPoint, on_delete=models.DO_NOTHING, related_name='BogieRecFrom')
    Quantity = models.IntegerField(blank=True,null=True)
    Date = models.DateTimeField(default=timezone.now)
    RecDate = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='railpointuser2')
    def __str__(self):
        return f'{self.Quantity} {self.BogieType} bogies received from {self.PlaceName} on {self.RecDate}'

class BogieDispatchRegister(models.Model):
    BogieType = models.ForeignKey(Bogie, on_delete=models.DO_NOTHING, related_name='BogieTypeDisp')
    PlaceName = models.ForeignKey(RailPoint, on_delete=models.DO_NOTHING, related_name='BogieDispFrom')
    Quantity = models.IntegerField(blank=True,null=True)
    Date = models.DateTimeField(default=timezone.now)
    DispDate = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='railpointuser3')
    def __str__(self):
        return f'{self.Quantity} {self.BogieType} bogies dispatched to {self.PlaceName} on {self.DispDate}'

class FabBogieRegister(models.Model):
    BogieType = models.ForeignKey(Bogie, on_delete=models.DO_NOTHING, related_name='BogieTypeFab')
    Quantity = models.IntegerField(blank=True,null=True)
    Date = models.DateTimeField(default=timezone.now)
    RepDate = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, related_name='railpointuser4')
    def __str__(self):
        return f'{self.Quantity} {self.BogieType} bogies repaired in Fabrication Shop on {self.RepDate}'


