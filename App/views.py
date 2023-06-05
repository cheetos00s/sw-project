
#
from django.shortcuts import render, redirect
from .models import Autor, Editorial, Libreria, Libro, Libreria_libro


# New imports
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# /**/
from .models import Libreria
from .resources import LibreriaResource
from tablib import Dataset
from django.http import HttpResponse
import time

import csv, io
from datetime import datetime




# Frontend
def frontend(request):
    
    return render(request, "App/frontend.html")

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

def upload_csv(request):
    if request.method == 'POST':
        if 'myfile' in request.FILES and 'myfile2' in request.FILES and 'myfile3' in request.FILES and 'myfile4' in request.FILES:
            myfile = request.FILES['myfile']
            myfile2 = request.FILES['myfile2']
            myfile3 = request.FILES['myfile3']
            myfile4 = request.FILES['myfile4']

            if myfile.name.endswith('.csv') and myfile2.name.endswith('.csv') and myfile3.name.endswith('.csv') and myfile4.name.endswith('.csv'):
                # Leer y procesar el primer archivo CSV para Libreria
                data_set = myfile.read().decode('utf-8')
                io_string = io.StringIO(data_set)
                next(io_string)  # Saltar la primera línea del encabezado
                for row in csv.reader(io_string, delimiter=','):
                    _, created = Libreria.objects.update_or_create(
                        nombre=row[0],
                        direccion=row[1],
                        telefono=row[2]
                    )

                # Leer y procesar el segundo archivo CSV para Editorial
                data_set2 = myfile2.read().decode('utf-8')
                io_string2 = io.StringIO(data_set2)
                next(io_string2)  # Saltar la primera línea del encabezado
                for row in csv.reader(io_string2, delimiter=','):
                    _, created = Editorial.objects.update_or_create(
                        nombre=row[0],
                        direccion=row[1],
                        ciudad=row[2],
                        telefono=row[3],
                        correo=row[4]
                    )

                # Leer y procesar el tercer archivo CSV para Autor
                data_set3 = myfile3.read().decode('utf-8')
                io_string3 = io.StringIO(data_set3)
                next(io_string3)  # Saltar la primera línea del encabezado
                for row in csv.reader(io_string3, delimiter=','):
                    _, created = Autor.objects.update_or_create(
                        nombre=row[0],
                        apellido=row[1],
                        direccion=row[2],
                        telefono=row[3],
                        fecha_nacimiento=row[4]
                    )

                # Leer y procesar el cuarto archivo CSV para Libro
                data_set4 = myfile4.read().decode('utf-8')
                io_string4 = io.StringIO(data_set4)
                next(io_string4)  # Saltar la primera línea del encabezado
                for row in csv.reader(io_string4, delimiter=','):
                    autor = Autor.objects.get(id=row[3])
                    editorial = Editorial.objects.get(id=row[4])
                    _, created = Libro.objects.update_or_create(
                        titulo=row[0],
                        año_publicacion=row[1],
                        precio=row[2],
                        autor_id=autor,
                        editorial_id=editorial
                    )
                
                
                messages.success(request, 'Archivos CSV cargados exitosamente.')
            else:
                messages.error(request, 'Se requieren archivos CSV válidos.')
        else:
            messages.error(request, 'Se requieren cuatro archivos CSV.')
            
    return render(request, 'App/upload_libreria.html')






# Llama a la función para insertar los libros en la tabla Libreria_libro

