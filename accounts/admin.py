from django.contrib import admin

from .models import UserProfile, \
    StatesCatalog, \
    SuburbCatalog, \
    CitiesCatalog, \
    PostalCodeCatalog, \
    UserAddress

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'ref_date')
    search_fields = ('user')
    list_filter = ('ref_date')
    date_hierarchy = 'ref_date'
    fields = ('user', 'photo', 'telephone', 'active',)
    raw_id_fields = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(StatesCatalog)
admin.site.register(SuburbCatalog)
admin.site.register(CitiesCatalog)
admin.site.register(PostalCodeCatalog)
admin.site.register(UserAddress)
