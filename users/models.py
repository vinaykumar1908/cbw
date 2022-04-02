from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Profile(AbstractUser):
    DesignationChoices = (
        ("Officer", "Officer"),
        ("SSE/CB", "SSE/CB"),
        ("JE/CB", "JE/CB"),
        ("Techical Asst", "Technical Asst"),
    )
    PlaceOfPosting = (
        ("Sickline Office", "Sickline Office"),
        ("ROH Office", "ROH"),
        ("Contract Office", "Contract Office"),
        ("Tech Cell Office", "Tech Cell Office"),
        ("OMRS Office", "OMRS Office"),
        ("SSE Planning Office", "SSE Planning Office"),
        ("M&P Section", "M&P Section"),
        ("CB Administration", "CB Administration"),
        ("Stores", "Stores"),
        ("Wheel Shop", "Wheel Shop"),
    )
    
    Name = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Mobile = models.BigIntegerField(null=True, blank=True)
    LocalAddress = models.TextField(null=True, blank=True)
    IDNumber = models.CharField(max_length=30, default='ID Number', null=True)
    Designation = models.CharField(max_length=30, default='JE/CB', null=True, blank=True)
    Posted = models.CharField(max_length=30, choices=PlaceOfPosting, default='Tech Cell Office', null=True, blank=True)
    DateOfJoining = models.DateField(null=True, default='1001-01-01', blank=True)

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        else:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
