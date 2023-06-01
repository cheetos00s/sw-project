from django.contrib import admin
from App.models import Pais

class PaisAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'updated_at']
    search_fields = ['name', 'status', 'created_at']
    list_per_page = 8

admin.site.register(Pais, PaisAdmin)
