from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):

    return HttpResponse('Vista inicio')


def vehiculos(request):

    return HttpResponse('Vista Vehiculo')

def indumentarias(request):

    return HttpResponse('Vista Indumentaria')

def animales(request):

    return HttpResponse('Vista Animal')







