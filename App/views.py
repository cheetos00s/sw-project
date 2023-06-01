from django.shortcuts import render
<<<<<<< HEAD
#
from App.models import Pais
from django.utils import timezone
=======
>>>>>>> b2582d48cd86ebf359d301421cbf65aa0336f794

# New imports
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Frontend
def frontend(request):
    return render(request, "App/frontend.html")

# Backend
@login_required(login_url="/login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, "App/backend.html")
<<<<<<< HEAD
=======
# -----------------------------------------|
>>>>>>> b2582d48cd86ebf359d301421cbf65aa0336f794

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
            return HttpResponseRedirect('/backend')
        else:
            messages.error(request, "Enter your data correctly.")
            return HttpResponseRedirect('/')
        
# Logout Function
def LogoutUser(request):
    logout(request)
    request.user = None
<<<<<<< HEAD
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
=======
    return HttpResponseRedirect('/')
>>>>>>> b2582d48cd86ebf359d301421cbf65aa0336f794
