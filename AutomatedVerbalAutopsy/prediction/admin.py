from django.contrib import admin
from questionnaire.models import COD,CODWithSababu

admin.site.register(CODWithSababu)

class CODWithSababu(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
