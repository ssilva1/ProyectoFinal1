from datetime import datetime
from urllib import request
from xmlrpc.client import boolean
from django.shortcuts import render, redirect
from AppLavatres.models import Vehiculo, Indumentaria, Animal
from AppLavatres.forms import FormularioVehiculo

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
        mi_formulario = FormularioVehiculo(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            vehiculo1 = Vehiculo(tipo_vehiculo=data.get('tipo_vehiculo'), aspirado=data.get('aspirado'), dominio=data.get('dominio'), ingreso=data.get('ingreso'), egreso=data.get('egreso'))
            vehiculo1.save()
            return redirect('AppLavatresAutoFormulario')
    
    vehiculos = Vehiculo.objects.all()
    contexto = {
        'form': FormularioVehiculo(),
        'vehiculos': vehiculos
    }
    return render(request, 'AppLavatres/vehiculos.html', contexto)
            
            
    






