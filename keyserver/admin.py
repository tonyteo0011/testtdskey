from django.contrib import admin
from .models import Key

class KeyAdmin(admin.ModelAdmin):
    list_display = ['user', 'tool', 'key', 'created_date', 'expiry_date']
    list_filter = ['tool']
    search_fields = ['user']


admin.site.register(Key, KeyAdmin)