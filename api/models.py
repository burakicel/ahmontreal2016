from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.
class Location(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
        related_name="profile",
        verbose_name=("user"))
    longitude = models.DecimalField(max_digits=31, decimal_places=10)
    latitude = models.DecimalField(max_digits=31, decimal_places=10)