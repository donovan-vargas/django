from django.contrib import admin
from .models import UserProfile, \
    StatesCatalog, \
    SuburbCatalog, \
    CitiesCatalog, \
    PostalCodeCatalog, \
    UserAddress


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(StatesCatalog)
admin.site.register(SuburbCatalog)
admin.site.register(CitiesCatalog)
admin.site.register(PostalCodeCatalog)
admin.site.register(UserAddress)

