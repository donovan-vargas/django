from django.contrib import admin

from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'reg_date',)
    search_fields = ('user',)
    list_filter = ('reg_date',)
    date_hierarchy = 'reg_date'
    fields = ('user', 'photo', 'telephone', 'active',)
    raw_id_fields = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
