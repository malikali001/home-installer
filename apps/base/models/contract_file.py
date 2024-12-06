from django.db import models

from .contract import Contract


class ContractFile(models.Model):
    file = models.ImageField(upload_to="contract_files/")
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
