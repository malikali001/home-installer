from django.contrib import admin

from .models import (Asset, Contract, ContractFile, CustomUser, DeliveryPoint,
                     Message, Product, Query)

admin.site.register(Asset)
admin.site.register(Contract)
admin.site.register(ContractFile)
admin.site.register(CustomUser)
admin.site.register(DeliveryPoint)
admin.site.register(Message)
admin.site.register(Product)
admin.site.register(Query)
