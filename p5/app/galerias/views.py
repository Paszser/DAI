from django.shortcuts import render, HttpResponse, redirect

from galerias.forms import FormularioCuadro, FormularioGaleria, FormularioRegistro
from .models import Cuadro, Galeria
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='loginPage')
def index(request):
    context = {}
    return render(request,'index.html', context)

def test_template(request):
    context = {'saludado': 'Luiso'}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = FormularioRegistro()

        if request.method == 'POST':
            form = FormularioRegistro(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')
                messages.success(request, "La cuenta fue creada para " + user)

                return redirect('loginPage')

        context = {'form': form}
        return render(request, 'account/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username o Contraseña es incorrecta.')

        context = {}
        return render(request, 'account/login.html', context)

@login_required(login_url='loginPage')
def logoutUser(request):
    logout(request)
    return redirect('loginPage')

#######################
####### GALERÍAS ######
#######################

@login_required(login_url='loginPage')
def listarGalerias(request):
    galerias = Galeria.objects.all()
    context = {"galerias": galerias}
    return render(request,'ListaGalerias.html', context)

@login_required(login_url='loginPage')
def anadirGaleria(request):
    galeria = FormularioGaleria()
    context = {"form": galeria}
    return render(request, 'AnadirGaleria.html', context)

@login_required(login_url='loginPage')
def procesarAnadir(request):
    galeria = FormularioGaleria(request.POST)
    context = {"form": galeria, "mensaje": 'OK'}
    if galeria.is_valid():
        galeria.save()
        galeria = FormularioGaleria()
    return render(request, 'AnadirGaleria.html', context)

@login_required(login_url='loginPage')
def edit(request, id_galeria):
    galeria = Galeria.objects.filter(nombre=id_galeria).first()
    form = FormularioGaleria(instance=galeria)
    context = {"form": form, "galeria": galeria}
    return render(request, "galeriaEdit.html", context)

@login_required(login_url='loginPage')
def actualizarGaleria(request, id_galeria):
        galeria = Galeria.objects.get(pk=id_galeria)
        form = FormularioGaleria(request.POST, instance=galeria)
        if form.is_valid():
            form.save()
        galerias = Galeria.objects.all()
        context = {"galerias": galerias}
        return render(request,'ListaGalerias.html', context)

@login_required(login_url='loginPage')
def delete(request, id_galeria):
    galeria = Galeria.objects.get(pk=id_galeria)
    galeria.delete()
    galerias = Galeria.objects.all()
    context = {"galerias": galerias, "mensaje": 'OK'}
    return render(request,'ListaGalerias.html', context)

#######################
####### CUADROS ######
#######################

@login_required(login_url='loginPage')
def listarCuadros(request):
    cuadros = Cuadro.objects.all()
    context = {"cuadros": cuadros}
    return render(request,'ListaCuadros.html', context)

@login_required(login_url='loginPage')
def anadirCuadro(request):
    cuadro = FormularioCuadro()
    context = {"form": cuadro}
    return render(request, 'AnadirCuadro.html', context)

@login_required(login_url='loginPage')
def procesarAnadirCuadro(request):
    cuadro = FormularioCuadro(request.POST)
    context = {"form": cuadro, "mensaje": 'OK'}
    if cuadro.is_valid():
        cuadro.save()
        cuadro = FormularioCuadro()
    return render(request, 'AnadirCuadro.html', context)

@login_required(login_url='loginPage')
def editCuadro(request, id_cuadro):
    cuadro = Cuadro.objects.filter(pk=id_cuadro).first()
    form = FormularioCuadro(instance=cuadro)
    context = {"form": form, "cuadro": cuadro}
    return render(request, "cuadroEdit.html", context)

@login_required(login_url='loginPage')
def actualizarCuadro(request, id_cuadro):
        cuadro = Cuadro.objects.get(pk=id_cuadro)
        form = FormularioCuadro(request.POST, instance=cuadro)
        if form.is_valid():
            form.save()
        cuadros = Cuadro.objects.all()
        context = {"cuadros": cuadros}
        return render(request,'ListaCuadros.html', context)

@login_required(login_url='loginPage')
def deleteCuadro(request, id_cuadro):
    cuadro = Cuadro.objects.get(pk=id_cuadro)
    cuadro.delete()
    cuadros = Cuadro.objects.all()
    context = {"cuadros": cuadros, "mensaje": 'OK'}
    return render(request,'ListaCuadros.html', context)

