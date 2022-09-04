#from socket import fromshare
from django import forms


class FormularioVehiculo(forms.Form):
    tipo_vehiculo = forms.CharField(max_length=30)
    aspirado = forms.BooleanField()
    dominio = forms.CharField(max_length=7)
    ingreso = forms.DateTimeField()
    egreso = forms.DateTimeField()
    
