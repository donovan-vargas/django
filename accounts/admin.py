from django.contrib import admin

<<<<<<< HEAD
from .models import UserProfile
=======
from .models import UserProfile, \
    StatesCatalog, \
    SuburbCatalog, \
    CitiesCatalog, \
    PostalCodeCatalog, \
    UserAddress
>>>>>>> f5e9ad2b2513f9a876289f5ac2623a93702833c3

# Register your models here.
<<<<<<< HEAD
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'reg_date',)
    search_fields = ('user',)
    list_filter = ('reg_date',)
    date_hierarchy = 'reg_date'
    fields = ('user', 'photo', 'telephone', 'active',)
    raw_id_fields = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
=======
admin.site.register(UserProfile)
admin.site.register(StatesCatalog)
admin.site.register(SuburbCatalog)
admin.site.register(CitiesCatalog)
admin.site.register(PostalCodeCatalog)
admin.site.register(UserAddress)
>>>>>>> f5e9ad2b2513f9a876289f5ac2623a93702833c3
