from django.contrib import admin
from App.models import Pais
from App.models import Carousel

# Register your models here.
admin.site.register(Carousel)

class PaisAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'updated_at']
    search_fields = ['name', 'status', 'created_at']
    list_per_page = 8

admin.site.register(Pais, PaisAdmin)

