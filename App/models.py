from django.db import models

# Create your models here.
GENDER = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino')
)

CAREER = (
    ('Cedula de Ciudadania', 'Cedula de Ciudadania'),
    ('Cedula de Extranjeria', 'Cedula de Extranjeria'),
    ('Tarjeta de Identidad', 'Tarjeta de Identidad'),
    ('Pasaporte', 'Pasaporte')
)

class Carousel(models.Model):
    image       = models.ImageField(upload_to="pics/%y/%m/%d/")
    title       = models.CharField(max_length=150)
    action_name = models.CharField(max_length=50)
    link        = models.TextField(null=True, blank=True)
    sub_title   = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Pais(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Facultad(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Empresa(models.Model):
    name = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Institucion(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ciudad(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    