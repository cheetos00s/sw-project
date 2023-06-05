from import_export import resources
from .models import *

class LibreriaResource(resources.ModelResource):
    class Meta:
        model = Libreria

class EditorialResource(resources.ModelResource):
    class Meta:
        model = Editorial