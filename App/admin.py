from django.contrib import admin
<<<<<<< HEAD
from App.models import Pais

class PaisAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'updated_at']
    search_fields = ['name', 'status', 'created_at']
    list_per_page = 8

admin.site.register(Pais, PaisAdmin)
=======

# Register your models here.
>>>>>>> b2582d48cd86ebf359d301421cbf65aa0336f794
