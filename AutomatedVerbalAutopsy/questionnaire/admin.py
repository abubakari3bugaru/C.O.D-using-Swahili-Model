
from django.contrib import admin
from .models import COD

admin.site.register(COD)

class COD(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
