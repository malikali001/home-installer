from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return str(self.name)
