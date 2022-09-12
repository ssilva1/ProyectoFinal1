
from django.urls import path
from AppLavatres.views import *


urlpatterns = [
    path('', inicio, name='AppLavatresInicio'),
    path('carga_vehiculo/', vehiculo_formulario, name='AppLavatresAutoFormulario'),
    path('carga_indumentaria/', indumentaria_formulario, name='AppLavatresIndumentariaFormulario'),
    path('carga_mascota/', animales_formulario, name='AppLavatresMascotaFormulario'),
    path('busqueda_vehiculo_post/', busqueda_vehiculo_post, name='AppLavatresBusquedaVehiculoPost'),
    path('busqueda_vehiculo/', busqueda_vehiculo, name='AppLavatresBusquedaVehiculo'),
    path('busqueda_indumentaria_post/', busqueda_indumentaria_post, name='AppLavatresBusquedaIndumentariaPost'),
    path('busqueda_indumentaria/', busqueda_indumentaria, name='AppLavatresBusquedaIndumentaria'),
    path('busqueda_animal_post/', busqueda_animal_post, name='AppLavatresBusquedaAnimalPost'),
    path('busqueda_animal/', busqueda_animal, name='AppLavatresBusquedaAnimal')
    ]