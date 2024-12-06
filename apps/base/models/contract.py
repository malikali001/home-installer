from django.db import models
from django.utils import timezone

from .asset import Asset


class Contract(models.Model):
    timestamp = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=25)
    contract_type = models.CharField(max_length=25)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
