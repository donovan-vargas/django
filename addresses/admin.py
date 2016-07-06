from django.contrib import admin

from .models import  StatesCatalog, \
    SuburbCatalog, \
    CitiesCatalog, \
    PostalCodeCatalog, \
    Addresses

# Register your models here.
admin.site.register(StatesCatalog)
admin.site.register(SuburbCatalog)
admin.site.register(CitiesCatalog)
admin.site.register(PostalCodeCatalog)
admin.site.register(Addresses)

