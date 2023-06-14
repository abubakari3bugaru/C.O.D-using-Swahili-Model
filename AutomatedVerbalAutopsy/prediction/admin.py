from django.contrib import admin
from .models import Predictions

admin.site.register(Predictions)

class Predictions(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
