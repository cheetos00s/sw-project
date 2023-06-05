from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Autor, Editorial, Libreria, Libro, Libreria_libro

@admin.register(Libreria)
class LibreriaAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')

@admin.register(Editorial)
class EditorialAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'telefono', 'correo')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'telefono', 'fecha_nacimiento')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'año_publicacion', 'precio', 'autor_id', 'editorial_id')

@admin.register(Libreria_libro)
class LibreriaLibroAdmin(admin.ModelAdmin):
    list_display = ('libro_id', 'libreria_id', 'cantidad')
