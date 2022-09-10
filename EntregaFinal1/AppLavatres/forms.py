from django import forms


class FormularioVehiculo(forms.Form):
    tipo_vehiculo = forms.CharField(max_length=30)
    aspirado = forms.BooleanField(required=False)
    dominio = forms.CharField(max_length=7)
    ingreso = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    egreso = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    
class FormularioIndumentaria(forms.Form):
    tipo_indumentaria = forms.CharField(max_length=40)
    ropa_banca = forms.BooleanField(required=False)
    nombre_cliente = forms.CharField(max_length=30)
    fecha_retiro = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    

class FormularioAnimales(forms.Form):
    tipo_animal = forms.CharField(max_length=30)
    nombre_duenio = forms.CharField(max_length=30) 
    corte_pelo = forms.BooleanField(required=False)
    fecha_turno = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type':'date'}))