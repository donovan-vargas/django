# coding=utf-8
from django.contrib import admin
from .models import ProviderCatalog, \
    PaymentCatalog, \
    ProducerCatalog, \
    ProductCatalog,  \
    Store, \
    Inventory, \
    EntryOrder, \
    EntryOrderDetail, \
    OutOrder, \
    OutOrderDetail, \
    Sales, \
    SalesDetail

admin.site.register(ProviderCatalog)
admin.site.register(PaymentCatalog)
admin.site.register(ProducerCatalog)
admin.site.register(ProductCatalog)
admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(EntryOrder)
admin.site.register(EntryOrderDetail)
admin.site.register(OutOrder)
admin.site.register(OutOrderDetail)
admin.site.register(Sales)
admin.site.register(SalesDetail)



