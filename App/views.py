from django.shortcuts import render
#
from App.models import *
from django.utils import timezone
from django.shortcuts import get_object_or_404


# New imports
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from App.models import Carousel
from django.conf import settings

# Frontend
def frontend(request):
    carousel = Carousel.objects.all()
    print(carousel)
    context  = {
        'carousel' : carousel
    }
    return render(request, "App/frontend.html",context)

# Backend
@login_required(login_url="/login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, "App/backend.html")

# Login Function
def Login(request):
    if request.user.is_authenticated:
        return render(request, "App/backend.html")
    else:
        messages.info(request, "Please login to access this page.")
        return HttpResponseRedirect('/')

# Login User
def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            return HttpResponseRedirect('/home')
        else:
            messages.error(request, "Enter your data correctly.")
            return HttpResponseRedirect('/')
        
# Logout Function
def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')

#|------------------------------------|
#               PAIS
#|------------------------------------|

# Function to render the page with all produts
def pais_list(request):
    all_pais_list = Pais.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/pais_list.html', {"paises": all_pais_list})

# Funtion to insert product

def pais_add(request):
    if request.method == "POST":
        if  request.POST.get('name'):
            pais = Pais()
            pais.name = request.POST.get('name') 
            pais.status = 1  # Set status=1 by default
            pais.created_at = timezone.now()  # Set created_at to current timestamp
            pais.updated_at = timezone.now()
            pais.save()
            return HttpResponseRedirect("pais_list/")
    else:
        return render(request, 'App/pais_add.html')

# Function to view candidate individually
def pais(request, pais_id):
    pais = Pais.objects.get(id = pais_id)
    if pais != None:
        return render(request, "App/pais_view.html", {'pais':pais})


# Function to Edit product
def pais_edit(request):
    if request.method == "POST":
        pais_id = request.POST.get('id')
        pais_name = request.POST.get('name')
        pais = Pais.objects.get(id=pais_id)
        if pais != None:
            pais.name = pais_name
            pais.save()
            return HttpResponseRedirect("/pais_list/")


# Delete Function
def pais_delete(request, pais_id):
    pais = Pais.objects.get(id=pais_id)
    if pais:
        pais.status = 0
        pais.save()

    return HttpResponseRedirect("/pais_list/")

#|------------------------------------|
#               FACULTAD
#|------------------------------------|

# Function to render the page with all produts
def facultad_list(request):
    all_facultad_list = Facultad.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/facultad_list.html', {"facultades": all_facultad_list})

# Funtion to insert product

def facultad_add(request):
    if request.method == "POST":
        if  request.POST.get('name'):
            facultad = Facultad()
            facultad.name = request.POST.get('name') 
            facultad.status = 1  # Set status=1 by default
            facultad.created_at = timezone.now()  # Set created_at to current timestamp
            facultad.updated_at = timezone.now()
            facultad.save()
            return HttpResponseRedirect("facultad_list/")
    else:
        return render(request, 'App/facultad_add.html')

# Function to view candidate individually
def facultad(request, facultad_id):
    facultad = Facultad.objects.get(id = facultad_id)
    if facultad != None:
        return render(request, "App/facultad_view.html", {'facultad':facultad})


# Function to Edit product
def facultad_edit(request):
    if request.method == "POST":
        facultad_id = request.POST.get('id')
        facultad_name = request.POST.get('name')
        facultad = Facultad.objects.get(id=facultad_id)
        if facultad != None:
            facultad.name = facultad_name
            facultad.save()
            return HttpResponseRedirect("/facultad_list/")


# Delete Function
def facultad_delete(request, facultad_id):
    facultad = Facultad.objects.get(id=facultad_id)
    if facultad:
        facultad.status = 0
        facultad.save()

    return HttpResponseRedirect("/facultad_list/")

#|------------------------------------|
#             INSTITUCION
#|------------------------------------|

# Function to render the page with all produts
def institucion_list(request):
    all_institucion_list = Institucion.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/institucion_list.html', {"instituciones": all_institucion_list})

# Funtion to insert product

def institucion_add(request):
    if request.method == "POST":
        if  request.POST.get('name'):
            institucion = Institucion()
            institucion.name = request.POST.get('name') 
            institucion.status = 1  # Set status=1 by default
            institucion.created_at = timezone.now()  # Set created_at to current timestamp
            institucion.updated_at = timezone.now()
            institucion.save()
            return HttpResponseRedirect("institucion_list/")
    else:
        return render(request, 'App/institucion_add.html')

# Function to view candidate individually
def institucion(request, institucion_id):
    institucion = Institucion.objects.get(id = institucion_id)
    if institucion != None:
        return render(request, "App/institucion_view.html", {'institucion':institucion})


# Function to Edit product
def institucion_edit(request):
    if request.method == "POST":
        institucion_id = request.POST.get('id')
        institucion_name = request.POST.get('name')
        institucion = Institucion.objects.get(id=institucion_id)
        if institucion != None:
            institucion.name = institucion_name
            institucion.save()
            return HttpResponseRedirect("/institucion_list/")


# Delete Function
def institucion_delete(request, institucion_id):
    institucion = Institucion.objects.get(id=institucion_id)
    if institucion:
        institucion.status = 0
        institucion.save()

    return HttpResponseRedirect("/institucion_list/")


#|------------------------------------|
#             EMPRESA
#|------------------------------------|

# Function to render the page with all produts
def empresa_list(request):
    all_empresa_list = Empresa.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/empresa_list.html', {"empresas": all_empresa_list})

# Funtion to insert product

def empresa_add(request):
    if request.method == "POST":
        if  request.POST.get('name')\
            and request.POST.get('nit') \
            or request.POST.get('direccion'):
            empresa = Empresa()
            empresa.name = request.POST.get('name')
            empresa.nit = request.POST.get('nit') 
            empresa.direccion = request.POST.get('direccion') 
            empresa.status = 1  # Set status=1 by default
            empresa.created_at = timezone.now()  # Set created_at to current timestamp
            empresa.updated_at = timezone.now()
            empresa.save()
            return HttpResponseRedirect("empresa_list/")
    else:
        return render(request, 'App/empresa_add.html')

# Function to view candidate individually
def empresa(request, empresa_id):
    empresa = Empresa.objects.get(id = empresa_id)
    if empresa != None:
        return render(request, "App/empresa_view.html", {'empresa':empresa})


# Function to Edit product
def empresa_edit(request):
    if request.method == "POST":
        empresa_id = request.POST.get('id')
        empresa_name = request.POST.get('name')
        empresa_nit = request.POST.get('nit')
        empresa_direccion = request.POST.get('direccion')
        empresa = Empresa.objects.get(id=empresa_id)
        if empresa != None:
            empresa.name = empresa_name
            empresa.nit = empresa_nit
            empresa.direccion = empresa_direccion
            empresa.save()
            return HttpResponseRedirect("/empresa_list/")


# Delete Function
def empresa_delete(request, empresa_id):
    empresa = Empresa.objects.get(id=empresa_id)
    if empresa:
        empresa.status = 0
        empresa.save()

    return HttpResponseRedirect("/empresa_list/")

#|------------------------------------|
#             CIUDAD
#|------------------------------------|

# Function to render the page with all produts
def ciudad_list(request):
    pais = Pais.objects.all()
    print(pais)
    all_ciudad_list = Ciudad.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/ciudad_list.html', {"ciudades": all_ciudad_list, "context":pais})

# Funtion to insert product

def ciudad_add(request):
    pais = Pais.objects.all()
    context  = {
        'pais' : pais
    }
    print(context)
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('pais_id'):
            ciudad = Ciudad()
            ciudad.name = request.POST.get('name')
            ciudad.pais_id = request.POST.get('pais_id') 
            ciudad.status = 1  # Set status=1 by default
            ciudad.created_at = timezone.now()  # Set created_at to current timestamp
            ciudad.updated_at = timezone.now()
            ciudad.save()
            return HttpResponseRedirect("ciudad_list/")
    else:
        return render(request, 'App/ciudad_add.html',context)


# Function to view candidate individually
def ciudad(request, ciudad_id):
    pais = Pais.objects.all()
    ciudad = Ciudad.objects.get(id = ciudad_id)
    if ciudad != None:
        return render(request, "App/ciudad_view.html", {'ciudad': ciudad, 'pais':pais})


def ciudad_edit(request):
    if request.method == "POST":
        ciudad_id = request.POST.get('id')
        ciudad_name = request.POST.get('name')
        ciudad_pais_id = request.POST.get('pais_id') 
        ciudad = Ciudad.objects.get(id=ciudad_id)
        if ciudad != None:
            ciudad.name = ciudad_name
            ciudad.pais_id = ciudad_pais_id
            ciudad.save()
            return HttpResponseRedirect("ciudad_list/")
# Delete Function
def ciudad_delete(request, ciudad_id):
    ciudad = Ciudad.objects.get(id=ciudad_id)
    if ciudad:
        ciudad.status = 0
        ciudad.save()

    return HttpResponseRedirect("/ciudad_list/")

#|------------------------------------|
#             PREGRADO
#|------------------------------------|

# Function to render the page with all produts
def pregrado_list(request):
    pregrado = Pregrado.objects.all()
    print(pregrado)
    all_pregrado_list = Pregrado.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/pregrado_list.html', {"pregrados": all_pregrado_list, "context":pregrado})

# Funtion to insert product

def pregrado_add(request):
    facultad = Facultad.objects.all()
    context  = {
        'facultad' : facultad
    }
    print(context)
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('facultad_id'):
            pregrado = Pregrado()
            pregrado.name = request.POST.get('name')
            pregrado.facultad_id = request.POST.get('facultad_id') 
            pregrado.status = 1  # Set status=1 by default
            pregrado.created_at = timezone.now()  # Set created_at to current timestamp
            pregrado.updated_at = timezone.now()
            pregrado.save()
            return HttpResponseRedirect("pregrado_list/")
    else:
        return render(request, 'App/pregrado_add.html',context)


# Function to view candidate individually
def pregrado(request, pregrado_id):
    facultad = Facultad.objects.all()
    pregrado = Pregrado.objects.get(id = pregrado_id)
    if pregrado != None:
        return render(request, "App/pregrado_view.html", {'pregrado': pregrado, 'facultad':facultad})


def pregrado_edit(request):
    if request.method == "POST":
        pregrado_id = request.POST.get('id')
        pregrado_name = request.POST.get('name')
        pregrado_facultad_id = request.POST.get('facultad_id') 
        pregrado = Pregrado.objects.get(id=pregrado_id)
        if pregrado != None:
            pregrado.name = pregrado_name
            pregrado.facultad_id = pregrado_facultad_id
            pregrado.save()
            return HttpResponseRedirect("pregrado_list/")


# Delete Function
def pregrado_delete(request, pregrado_id):
    pregrado = Pregrado.objects.get(id=pregrado_id)
    if pregrado:
        pregrado.status = 0
        pregrado.save()

    return HttpResponseRedirect("/pregrado_list/")

#|------------------------------------|
#             POSGRADO
#|------------------------------------|

# Function to render the page with all produts
def posgrado_list(request):
    posgrado = Posgrado.objects.all()
    print(posgrado)
    all_posgrado_list = Posgrado.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/posgrado_list.html', {"posgrados": all_posgrado_list, "context":posgrado})

def posgrado_add(request):
    institucion = Institucion.objects.all()
    context  = {
        'institucion' : institucion
    }
    print(context)
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('institucion_id'):
            posgrado = Posgrado()
            posgrado.name = request.POST.get('name')
            posgrado.institucion_id = request.POST.get('institucion_id') 
            posgrado.status = 1  # Set status=1 by default
            posgrado.created_at = timezone.now()  # Set created_at to current timestamp
            posgrado.updated_at = timezone.now()
            posgrado.save()
            return HttpResponseRedirect("posgrado_list/")
    else:
        return render(request, 'App/posgrado_add.html',context)

def posgrado_edit(request):
    if request.method == "POST":
        posgrado_id = request.POST.get('id')
        posgrado_name = request.POST.get('name')
        posgrado_institucion_id = request.POST.get('institucion_id') 
        posgrado = Posgrado.objects.get(id=posgrado_id)
        if posgrado != None:
            posgrado.name = posgrado_name
            posgrado.institucion_id = posgrado_institucion_id
            posgrado.save()
            return HttpResponseRedirect("posgrado_list/")



# Function to view candidate individually
def posgrado(request, posgrado_id):
    institucion = Institucion.objects.all()
    posgrado = Posgrado.objects.get(id = posgrado_id)
    if posgrado != None:
        return render(request, "App/posgrado_view.html", {'posgrado': posgrado, 'institucion':institucion})

# Delete Function
def posgrado_delete(request, posgrado_id):
    posgrado = Posgrado.objects.get(id=posgrado_id)
    if posgrado:
        posgrado.status = 0
        posgrado.save()

    return HttpResponseRedirect("/posgrado_list/")

#|------------------------------------|
#             EGRESADO
#|------------------------------------|

# Function to render the page with all produts
def egresado_list(request):
    egresado = Egresado.objects.all()
    print(egresado)
    all_egresado_list = Egresado.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/egresado_list.html', {"egresados": all_egresado_list, "context":egresado})

# Funtion to insert product
def egresado_add(request):
    ciudad = Ciudad.objects.all()
    pregrado = Pregrado.objects.all()
    context  = {
        'ciudad' : ciudad,
        'pregrado' : pregrado
    }
    print(context)
    if request.method == "POST":
        if request.POST.get('name') \
            and request.POST.get('apellido') \
            and request.POST.get('cedula') \
            and request.POST.get('numero_carne') \
            and request.POST.get('genero') \
            and request.POST.get('direccion') \
            and request.POST.get('celular') \
            and request.POST.get('correo_personal') \
            and request.POST.get('correo_institucional') \
            and request.POST.get('fecha_nacimiento') \
            and request.POST.get('promocion') \
            and request.POST.get('tipo_grado') \
            and request.POST.get('ciudad_id') \
            or request.POST.get('pregrado_id'):
            egresado = Egresado()
            egresado.name = request.POST.get('name')
            egresado.apellido = request.POST.get('apellido')
            egresado.cedula = request.POST.get('cedula')
            egresado.numero_carne = request.POST.get('numero_carne')
            egresado.genero = request.POST.get('genero')
            egresado.direccion = request.POST.get('direccion')
            egresado.celular = request.POST.get('celular')
            egresado.correo_personal = request.POST.get('correo_personal')
            egresado.correo_institucional = request.POST.get('correo_institucional')
            egresado.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            egresado.promocion = request.POST.get('promocion')
            egresado.tipo_grado = request.POST.get('tipo_grado')
            egresado.ciudad_id = request.POST.get('ciudad_id')
            egresado.pregrado_id = request.POST.get('pregrado_id')
            egresado.status = 1  # Set status=1 by default
            egresado.created_at = timezone.now()  # Set created_at to current timestamp
            egresado.updated_at = timezone.now()
            egresado.save()
            return HttpResponseRedirect("egresado_list/")
    else:
        return render(request, 'App/egresado_add.html',context)

def egresado_edit(request):
    if request.method == "POST":
        egresado_id = request.POST.get('id')
        egresado_name = request.POST.get('name')
        egresado_apellido = request.POST.get('apellido')
        egresado_cedula = request.POST.get('cedula')
        egresado_numero_carne = request.POST.get('numero_carne')
        egresado_genero = request.POST.get('genero')
        egresado_direccion = request.POST.get('direccion')
        egresado_celular = request.POST.get('celular')
        egresado_correo_personal = request.POST.get('correo_personal')
        egresado_correo_institucional = request.POST.get('correo_institucional')
        egresado_fecha_nacimiento = request.POST.get('fecha_nacimiento')
        egresado_promocion = request.POST.get('promocion')
        egresado_tipo_grado = request.POST.get('tipo_grado')
        egresado_ciudad_id = request.POST.get('ciudad_id')
        egresado_pregrado_id = request.POST.get('pregrado_id') 
        egresado = Egresado.objects.get(id=egresado_id)
        if egresado != None:
            egresado.name = egresado_name
            egresado.apellido = egresado_apellido
            egresado.cedula = egresado_cedula
            egresado.numero_carne = egresado_cedula
            egresado.genero = egresado_genero
            egresado.direccion = egresado_direccion
            egresado.celular = egresado_celular
            egresado.correo_personal = egresado_correo_personal
            egresado.correo_institucional = egresado_correo_institucional
            egresado.fecha_nacimiento = egresado_fecha_nacimiento
            egresado.promocion = egresado_promocion
            egresado.tipo_grado = egresado_tipo_grado
            egresado.updated_at = timezone.now()
            egresado.ciudad_id = egresado_ciudad_id
            egresado.pregrado_id = egresado_pregrado_id
            egresado.save()
            return HttpResponseRedirect("egresado_list/")

# Function to view candidate individually
def egresado(request, egresado_id):
    ciudad = Ciudad.objects.all()
    pregrado = Pregrado.objects.all()
    egresado = Egresado.objects.get(id = egresado_id)
    if egresado != None:
        return render(request, "App/egresado_view.html", {'egresado': egresado, 'ciudad': ciudad, 'pregrado': pregrado})

# Delete Function
def egresado_delete(request, egresado_id):
    egresado = Egresado.objects.get(id=egresado_id)
    if egresado:
        egresado.status = 0
        egresado.save()

    return HttpResponseRedirect("/egresado_list/")


#|------------------------------------|
#             Laboral
#|------------------------------------|

# Function to render the page with all produts
def laboral_list(request):
    laboral = Laboral.objects.all()
    print(laboral)
    all_laboral_list = Laboral.objects.filter(status=1).order_by('-created_at')
    return render(request, 'App/laboral_list.html', {"laborals": all_laboral_list, "context":laboral})

# Funtion to insert product
def laboral_add(request):
    egresado = Egresado.objects.all()
    empresa = Empresa.objects.all()
    context  = {
        'egresado' : egresado,
        'empresa' : empresa
    }
    print(context)
    if request.method == "POST":
        if request.POST.get('egresado_id') \
            and request.POST.get('cargo') \
            and request.POST.get('fecha_inicio') \
            and request.POST.get('fecha_fin') \
            and request.POST.get('empresa_id') :
            laboral = Laboral()
            laboral.Egresado_id = request.POST.get('egresado_id')
            laboral.cargo = request.POST.get('cargo')
            laboral.fecha_inicio = request.POST.get('fecha_inicio')
            laboral.fecha_fin = request.POST.get('fecha_fin')
            laboral.empresa_id = request.POST.get('empresa_id')
            laboral.status = 1  # Set status=1 by default
            laboral.created_at = timezone.now()  # Set created_at to current timestamp
            laboral.updated_at = timezone.now()
            laboral.save()
            return HttpResponseRedirect("laboral_list/")
    else:
        return render(request, 'App/laboral_add.html',context)

def laboral_edit(request):
    if request.method == "POST":
        laboral_id = request.POST.get('id')
        laboral_Egresado_id = request.POST.get('egresado_id')
        laboral_cargo = request.POST.get('cargo')
        laboral_fecha_inicio = request.POST.get('fecha_inicio')
        laboral_fecha_fin = request.POST.get('fecha_fin')
        laboral_empresa_id = request.POST.get('empresa_id')
        laboral = Laboral.objects.get(id=laboral_id)
        if laboral != None:
            laboral.Egresado_id = laboral_Egresado_id
            laboral.cargo = laboral_cargo
            laboral.fecha_inicio = laboral_fecha_inicio
            laboral.fecha_fin = laboral_fecha_fin
            laboral.empresa_id = laboral_empresa_id
            laboral.save()
            return HttpResponseRedirect("laboral_list/")

# Function to view candidate individually
def laboral(request, laboral_id):
    egresado = Egresado.objects.all()
    empresa = Empresa.objects.all()
    laboral = Laboral.objects.get(id = laboral_id)
    if laboral != None:
        return render(request, "App/laboral_view.html", {'laboral': laboral, 'egresado': egresado, 'empresa': empresa})

# Delete Function
def laboral_delete(request, laboral_id):
    laboral = Laboral.objects.get(id=laboral_id)
    if laboral:
        laboral.status = 0
        laboral.save()

    return HttpResponseRedirect("/laboral_list/")

