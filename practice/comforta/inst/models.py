from django.db import models
import uuid
import random
from string import ascii_letters, digits
from users.models import User
from random import choices


class Installation(models.Model):
    owner = models.OneToOneField(
        User, to_field='email', null=True, on_delete=models.DO_NOTHING)
    UIN = models.CharField(max_length=17, null=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, null=False)
    FirmwareVersion = models.CharField(null=False, max_length=254)
    FirmwareLastUpdateDate = models.DateField(null=True)
    DeviceEnabled = models.BooleanField(null=False, default=False)
    DeviceModes = [('off', 'Off'), ('one', 'One'), ('two', 'Two'),
                   ('three', 'Three'), ('four', 'Four')]
    DeviceMode = models.CharField(
        null=False, choices=DeviceModes, max_length=254, default=DeviceModes[0][0])
    NetworkModes = [('home', 'Home'), ('OneDevice', 'OneDevice')]
    NetworkMode = models.CharField(
        null=False, choices=NetworkModes, max_length=254, default=NetworkModes[0][0])
    LastCO2Value = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    InUse = models.BooleanField(null=False, default=False)
    NightModeEnabled = models.BooleanField(null=False, default=False)
    NightModeAuto = models.BooleanField(null=False, default=False)
    NightModeFrom = models.TimeField(null=True)
    NightModeTo = models.TimeField(null=True)
    DateCreated = models.DateField(null=False, auto_now_add=True)
    DateUpdated = models.DateField(null=False, auto_now=True)

    def __str__(self):
        return self.UIN

    def save(self, *args, **kwargs):
        if not self.UIN:
            AllDigits = ascii_letters+digits
            self.UIN = 'zCO2-'+''.join(choices(AllDigits, k=12))
            while Installation.objects.filter(UIN=self.UIN).exists():
                AllDigits = ascii_letters+digits
                self.UIN = 'zCO2-'+''.join(choices(AllDigits, k=12))
        super(Installation, self).save(*args, **kwargs)
