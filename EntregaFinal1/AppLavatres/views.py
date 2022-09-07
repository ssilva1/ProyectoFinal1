from django.contrib import messages
from django.shortcuts import render, redirect
from AppLavatres.models import Vehiculo, Indumentaria, Animal
from AppLavatres.forms import FormularioVehiculo, FormularioIndumentaria, FormularioAnimales

# Create your views here.
def inicio(request):
    contexto = {
        "valor1": "este es un valor"
    }
    return render(request, 'index.html', contexto)

"""
def vehiculos(request):

    return HttpResponse('Vista Vehiculo')


def indumentarias(request):

    return HttpResponse('Vista Indumentaria')

def animales(request):

    return HttpResponse('Vista Animal')
"""

def vehiculo_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioVehiculo(data=request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            vehiculo1 = Vehiculo(tipo_vehiculo=data.get('tipo_vehiculo'), aspirado=data.get('aspirado'), dominio=data.get('dominio'), ingreso=data.get('ingreso'), egreso=data.get('egreso'))
            vehiculo1.save()
            return redirect('AppLavatresAutoFormulario')
        else:
            messages.info(request, 'formulario no cargado')
         
    
    vehiculos = Vehiculo.objects.all()
    contexto = {
        'form': FormularioVehiculo(),
        'vehiculos': vehiculos
    }
    return render(request, 'AppLavatres/vehiculos.html', contexto)
            
            
"""def indumentaria_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioIndumentaria(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            indumentaria1 = Indumentaria(tipo_indumentaria=data.get('tipo_indumentaria'), ropa_blanca=boolean(), nombre_cliente=data.get('cliente'), egreso=datetime.time())
            indumentaria1.save()
            return redirect('AppLavatresIndumentariaFormulario')
    
    indumentaria1 = Indumentaria.objects.all()
    contexto = {
        'form': FormularioIndumentaria(),
        'indumentaria': Indumentaria
    }
    return render(request, 'AppLavatres/indumentarias.html', contexto)"""
               

"""def animales_formulario(request):
    if request.method == "POST":
        mi_formulario = FormularioAnimales(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            animal1 = Animal(tipo_animal=data.get('tipo_animal'), nombre_duenio=data.get('cliente'), core_pelo=boolean(), fecha_turno=datetime.time())
            animal1.save()
            return redirect('AppLavatresAnimalesFormulario')
    
    animal1 = Animal.objects.all()
    contexto = {
        'form': FormularioAnimales(),
        'animal': Animal
    }
    return render(request, 'AppLavatres/animales.html', contexto)"""




