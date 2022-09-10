from django.db import models

class Vehiculo(models.Model):
    tipo_vehiculo = models.CharField(max_length=30)
    aspirado = models.BooleanField()
    dominio = models.CharField(max_length=7)
    ingreso = models.DateTimeField()
    egreso = models.DateTimeField()
    
class Indumentaria(models.Model):
    tipo_indumentaria = models.CharField(max_length=40)
    ropa_blanca = models.BooleanField()
    nombre_cliente = models.CharField(max_length=30)
    fecha_retiro = models.DateTimeField()
    
class Animal(models.Model):
    tipo_animal = models.CharField(max_length=30)
    nombre_duenio = models.CharField(max_length=30)
    corte_pelo = models.BooleanField()
    fecha_turno = models.DateTimeField()

