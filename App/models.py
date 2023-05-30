from django.db import models
from django.utils.translation import gettext_lazy as _

class pais(models.Model):
    nombre = models.TextField(max_length=100)
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

class ciudad(models.Model):
    nombre = models.TextField(max_length=100)
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    pais = models.ForeignKey(pais, related_name="ciudad", blank=True, null=True, on_delete=models.CASCADE)

class facultad(models.Model):
    nombre = models.TextField(max_length=100)
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

class pregrado(models.Model):
    nombre = models.TextField(max_length=100)
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    facultad = models.ForeignKey(facultad, related_name="id_facultad", blank=True, null=True, on_delete=models.CASCADE)


class egresado(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    cedula = models.IntegerField(null=False)
    numero_carne = models.TextField(max_length=100)
    direccion = models.TextField(max_length=100)
    celular = models.TextField(max_length=100)
    correo_personal = models.TextField(max_length=100)
    correo_institucional = models.TextField(max_length=100)
    fecha_nacimiento = models.TextField(max_length=100)
    promocion = models.TextField(max_length=100)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    ciudad = models.ForeignKey(ciudad, related_name="id_ciudad", blank=True, null=True, on_delete=models.CASCADE)
    pregrado = models.ForeignKey(pregrado, related_name="id_pregrado", blank=True, null=True, on_delete=models.CASCADE)


class empresa(models.Model):
    nombre = models.TextField(max_length=100)
    nit = models.TextField(max_length=100)
    direccion = models.TextField(max_length=100)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)

class historial_laboral(models.Model):
    cargo = models.TextField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)

    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    empresa = models.ForeignKey(empresa, related_name="id_empresa", blank=True, null=True, on_delete=models.CASCADE)
    egresado = models.ForeignKey(egresado, related_name="id_egresado", blank=True, null=True, on_delete=models.CASCADE)

class institucion_educativa(models.Model):
    nombre = models.TextField(max_length=100)
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

class posgrado(models.Model):
    nombre = models.TextField(max_length=100)
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    institucion_educativa = models.ForeignKey(institucion_educativa, related_name="id_universidad", blank=True, null=True, on_delete=models.CASCADE)

class estudio_academico(models.Model):
    class estado(models.IntegerChoices):
        CREATED = 0, _('creado')
        COMPLETED = 1, _('Completado')
        FAILED = 2, _('Fallido')
    
    estado = models.IntegerField(default=Status.CREATED, choices=Status.choices)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    posgrado = models.ForeignKey(posgrado, related_name="id_posgrado", blank=True, null=True, on_delete=models.CASCADE)
    egresado = models.ForeignKey(egresado, related_name="id_egresado", blank=True, null=True, on_delete=models.CASCADE)

