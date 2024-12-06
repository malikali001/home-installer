from django.db import models

from .custom_user import CustomUser


class Asset(models.Model):
    tech_specs = models.CharField(max_length=30)
    pv_string = models.CharField(max_length=30)
    inverter = models.CharField(max_length=30)
    status = models.CharField(max_length=25)
    address = models.CharField(max_length=500)
    battery = models.CharField(max_length=30)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tech_specs)
