from django.db import models
from django.utils import timezone

from .custom_user import CustomUser


class Query(models.Model):
    message = models.TextField()
    address = models.TextField(blank=False)
    tiles_type = models.CharField(max_length=25)
    interested_in = models.CharField(max_length=25)
    timestamp = models.DateTimeField(default=timezone.now())
    electricity_consumption = models.CharField(max_length=25)
    building_height = models.CharField(max_length=25)
    available_surface_for_pv = models.PositiveIntegerField()
    orientation = models.CharField(max_length=25)
    interested_in = models.JSONField(default=list)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
