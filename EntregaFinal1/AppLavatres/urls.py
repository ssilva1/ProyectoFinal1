
from django.urls import path
from AppLavatres.views import *


urlpatterns = [
    path('', inicio, name='AppLavatresInicio'),
    path('carga_vehiculo/', vehiculo_formulario, name='AppLavatresAutoFormulario'),
    path('carga_indumentaria/', indumentaria_formulario, name='AppLavatresIndumentariaFormulario'),
    path('carga_mascota/', animales_formulario, name='AppLavatresMascotaFormulario'),
    ]