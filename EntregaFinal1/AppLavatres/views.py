<<<<<<< HEAD
from django.contrib import messages
from django.shortcuts import render, redirect
from AppLavatres.models import Vehiculo, Indumentaria, Animal
from AppLavatres.forms import *

=======
from email import message

from django.contrib import messages
from django.shortcuts import render, redirect
from AppLavatres.models import Vehiculo, Indumentaria, Animal
from AppLavatres.forms import FormularioVehiculo, FormularioIndumentaria, FormularioAnimales, BusquedaDominio, BusquedaCliente, BusquedaDuenio
>>>>>>> main

def inicio(request):
    contexto = {
        "valor1": "este es un valor"
    }
    return render(request, 'index.html', contexto)


def vehiculo_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioVehiculo(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            vehiculo1 = Vehiculo(tipo_vehiculo=data.get('tipo_vehiculo'), aspirado=data.get('aspirado'), dominio=data.get('dominio'), ingreso=data.get('ingreso'), egreso=data.get('egreso'))
            vehiculo1.save()
            messages.info(request, 'Vehículo cargado satisfactoriamente')
            return redirect('AppLavatresAutoFormulario')
            
        else:
            messages.info(request, 'formulario no cargado')
         
    
    vehiculos = Vehiculo.objects.all()
    contexto = {
        'form': FormularioVehiculo(),
        'vehiculos': vehiculos
    }
    return render(request, 'AppLavatres/vehiculos.html', contexto)
            
            
def indumentaria_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioIndumentaria(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            indumentaria1 = Indumentaria(tipo_indumentaria=data.get('tipo_indumentaria'), ropa_blanca=data.get('ropa_blanca'), nombre_cliente=data.get('nombre_cliente'), fecha_retiro=data.get('fecha_retiro'))
            indumentaria1.save()
            messages.info(request, 'Prenda cargada satisfactoriamente')
            return redirect('AppLavatresIndumentariaFormulario')
<<<<<<< HEAD
    
    indumentarias = Indumentaria.objects.all()
=======
        else:
            messages.info(request, 'formulario no cargado')    

    indumentaria1 = Indumentaria.objects.all()
>>>>>>> main
    contexto = {
        'form': FormularioIndumentaria(),
        'indumentaria': indumentarias
    }
    return render(request, 'AppLavatres/indumentarias.html', contexto)
               

def animales_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioAnimales(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            animal1 = Animal(tipo_animal=data.get('tipo_animal'), nombre_duenio=data.get('nombre_duenio'), corte_pelo=data.get('corte_pelo'), fecha_turno=data.get('fecha_turno'))
            animal1.save()
            return redirect('AppLavatresMascotaFormulario')
        else:
            messages.info(request, 'formulario no cargado')

    animal1 = Animal.objects.all()
    contexto = {
        'form': FormularioAnimales(),
        'animal': Animal
    }
    return render(request, 'AppLavatres/animales.html', contexto)

def busqueda_vehiculo_post(request):
    dominio = request.GET.get('dominio')
    vehiculos = Vehiculo.objects.filter(dominio__icontains=dominio)
    print(vehiculos)

<<<<<<< HEAD
def busqueda_vehiculo(request):
    dominio = request.GET.get('dominio',"None")
    autos = Vehiculo.objects.filter(dominio__icontains=dominio)
    
    contexto ={
        'form' : BusquedaVehiculo(),
       'autos' : autos  
    }
    return render(request,'AppLavatres/vehiculo_filtrado.html', contexto )
    
    
    
=======
    contexto = {
        'vehiculos': vehiculos
    }
    return render(request, 'AppLavatres/vehiculo_filtrado.html', contexto)

def busqueda_vehiculo(request):
>>>>>>> main

    contexto = {
        'form': BusquedaDominio()
    }

    return render(request, 'AppLavatres/busqueda_vehiculo.html', contexto)

def busqueda_indumentaria_post(request):
    nombre_cliente = request.GET.get('nombre_cliente')
    indumentarias = Indumentaria.objects.filter(nombre_cliente__icontains=nombre_cliente)

    contexto = {
        'indumentarias': indumentarias
    }
    return render(request, 'AppLavatres/indumentaria_filtrado.html', contexto)

def busqueda_indumentaria(request):

    contexto = {
        'form': BusquedaCliente()
    }

    return render(request, 'AppLavatres/busqueda_indumentaria.html', contexto)

def busqueda_animal_post(request):
    nombre_duenio = request.GET.get('nombre_duenio')
    animales = Animal.objects.filter(nombre_duenio__icontains=nombre_duenio)

    contexto = {
        'animales': animales
    }
    return render(request, 'AppLavatres/animal_filtrado.html', contexto)

def busqueda_animal(request):

    contexto = {
        'form': BusquedaDuenio()
    }

    return render(request, 'AppLavatres/busqueda_animal.html', contexto)
