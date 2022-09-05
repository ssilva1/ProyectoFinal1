#from socket import fromshare
from django import forms


class FormularioVehiculo(forms.Form):
    tipo_vehiculo = forms.CharField(max_length=30)
    aspirado = forms.BooleanField()
    dominio = forms.CharField(max_length=7)
    ingreso = forms.DateTimeField()
    egreso = forms.DateTimeField()
    
class FormularioIndumentaria(forms.Form):
    tipo_indumentaria = forms.CharField(max_length=40)
    ropa_banca = forms.BooleanField()
    nombre_cliente = forms.CharField(max_length=30)
    fecha_retiro = forms.DateTimeField()
    

class FormularioAnimales(forms.Form):
    tipo_animal = forms.CharField(max_length=30)
    nombre_duenio = forms.BooleanField()
    corte_pelo = forms.BooleanField()
    fecha_turno = forms.DateTimeField()