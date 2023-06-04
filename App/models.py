from django.db import models

# Create your models here.
GENERO = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

TIPO_DOC = (
    ('Citizenship ID', 'Citizenship ID'),
    ('Foreigner ID', 'Foreigner ID'),
    ('Identity Card', 'Identity Card'),
    ('Passport', 'Passport')
)

TIPO_GRADO = (
    ('Ceremony', 'Ceremony'),
    ('Window', 'Window')
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

class Pregrado(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Posgrado(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Egresado(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    numero_carne = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, choices=GENERO)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    correo_personal = models.CharField(max_length=100)
    correo_institucional = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    promocion = models.IntegerField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tipo_grado = models.CharField(max_length=50, choices=TIPO_GRADO)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    pregrado = models.ForeignKey(Pregrado, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Academico(models.Model):
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posgrado = models.ForeignKey(Posgrado, on_delete=models.CASCADE)
    egresado = models.ForeignKey(Egresado, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Laboral(models.Model):
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Egresado = models.ForeignKey(Egresado, on_delete=models.CASCADE)

    def __str__(self):
        return self.name