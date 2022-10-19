from django.shortcuts import render
from  django.views.generic import ListView
from  django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Restaurante, Recomendaciones
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django_staff_required.views import StaffRequiredMixin
# Create your views here.

class RestauranteList(LoginRequiredMixin, ListView): #R del CRUD
    model = Restaurante

class RestauranteCrear(LoginRequiredMixin, CreateView): #C del CRUD
    model = Restaurante
    success_url = "/App1/restaurantes/"
    fields = ["Nombre","Localizacion","Categoria","Especialidad","Reseña"]

class RestauranteDetalle(LoginRequiredMixin, DetailView):
    model = Restaurante

class RestauranteUpdate(LoginRequiredMixin, UpdateView): #U del CRUD
    model = Restaurante
    success_url = "/App1/restaurantes/"
    fields = ["Nombre","Localizacion","Categoria","Especialidad","Reseña"]

class RestauranteBorrar(LoginRequiredMixin, DeleteView): #D del CRUD
    model = Restaurante
    success_url = "/App1/restaurantes/"

def inicio(request):

    return render(request,"App1/inicio.html")

def registro(request):

    if request.method=="POST":

        #formu = UserCreationForm(request.POST)
        formu = FormularioRegistro(request.POST)

        if formu.is_valid():

            nombreUsuario = formu.cleaned_data["username"]

            formu.save()

            return render(request, "App1/inicio.html", {"mensaje": f"Usuario {nombreUsuario} creado!!"})
    else:
        #formu = UserCreationForm()
        formu = FormularioRegistro()


    return render(request, "App1/registro.html", {"form4":formu})

@login_required
def editarUsuario(request):

    usuarioConectado = request.user

    if request.method == "POST":

        miFormulario2 = FormularioEditarUsuario(request.POST)

        if miFormulario2.is_valid():

            info = miFormulario2.cleaned_data

            usuarioConectado.email = info["email"] #Actualizar la info
            usuarioConectado.password1 = info["password1"]
            usuarioConectado.password2 = info["password2"]


            usuarioConectado.save
            return render(request, "App1/inicio.html")

    else:
        miFormulario2 = FormularioEditarUsuario(initial = {
            "email":usuarioConectado.email,
            })

    contexto = {"miForm":miFormulario2, "usuario":usuarioConectado}
    return render(request, "App1/editarUsuarios.html", contexto)

def iniciar_sesion(request):
    if request.method=="POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:
                login(request, user)

                return render(request, "App1/inicio.html", {"mensaje":f"Hola {user}"})

        else:

            return render(request, "App1/inicio.html", {"mensaje":f"Datos incorrectos!!!"})

    else:
        form = AuthenticationForm()

        return render(request, "App1/login.html", {"form3":form})
@login_required
def busquedaRestaurantes(request):
    return render(request, "App1/busquedaRestaurantes.html")
@login_required
def buscar(request):
    if request.GET["Categoria"]:
    
        busqueda = request.GET["Categoria"]
        restaurantes = Restaurante.objects.filter(Categoria__icontains=busqueda)

        return render(request, "App1/resultados.html",{"restaurantes":restaurantes, "busqueda":busqueda})

    else:
        mensaje = "No enviaste datos"
    return HttpResponse(mensaje)

class RecomendacionesList(LoginRequiredMixin, ListView): #R del CRUD
    model = Recomendaciones

class RecomendacionesCrear(LoginRequiredMixin, CreateView): #C del CRUD
    model = Recomendaciones
    success_url = "/App1/recomendaciones/"
    fields = ["Nombre","Localizacion","Categoria","Especialidad","Reseña","imagen"]

class RecomendacionesDetalle(LoginRequiredMixin, DetailView):
    model = Recomendaciones

class RecomendacionesUpdate(LoginRequiredMixin, UpdateView): #U del CRUD
    model = Recomendaciones
    success_url = "/App1/recomendaciones/"
    fields = ["Nombre","Localizacion","Categoria","Especialidad","Reseña","imagen"]

class RecomendacionesBorrar(LoginRequiredMixin, DeleteView): #D del CRUD
    model = Recomendaciones
    success_url = "/App1/recomendaciones/"

@login_required
def home(request):

    return render(request,"App1/home.html")