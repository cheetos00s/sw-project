from django.db import models
from django.conf import settings
from django import forms
from datetime import datetime
# Create your models here.

class Carousel(models.Model):
    image       = models.ImageField(upload_to="pics/%y/%m/%d/")
    title       = models.CharField(max_length=150)
    action_name = models.CharField(max_length=50)
    link        = models.TextField(null=True, blank=True)
    sub_title   = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libreria(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    año_publicacion = models.DateField()
    precio = models.IntegerField()
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial_id = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Libreria_libro(models.Model):
    libro_id = models.ForeignKey(Libro, on_delete=models.CASCADE)
    libreria_id = models.ForeignKey(Libreria, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.libro_id
