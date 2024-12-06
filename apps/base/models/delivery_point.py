import re

from django.core.exceptions import ValidationError
from django.db import models

from .asset import Asset


def validate_phone_number(value):
    if not re.fullmatch(r"^\+?\d{10,15}$", value):
        raise ValidationError(
            "Phone number must be between 10 and 15 digits, optionally starting with '+'."
        )


def validate_mpan(value):
    if not re.fullmatch(r"S\d{21}", value):
        raise ValidationError("MPAN must be a letter 'S' followed by 21 digits.")


class DeliveryPoint(models.Model):
    address = models.CharField(max_length=500)
    mpam = models.CharField(max_length=22, validators=[validate_mpan])
    phone = models.CharField(max_length=16, validators=[validate_phone_number])
    email = models.EmailField()
    supplier = models.CharField(max_length=30)
    tariff = models.CharField(max_length=30)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.email)
