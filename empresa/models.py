from django.db import models
from ubicacion.models import Municipio

# 0 -> Inactivo
# 1 -> Activo

class Envios_up(models.Model):
    eu_nit = models.CharField(max_length = 15, primary_key = True)
    eu_nombre = models.CharField(max_length = 50)
    eu_telefono = models.CharField(max_length = 10)
    eu_email = models.EmailField()
    eu_mision = models.CharField(max_length = 600)
    eu_vision = models.CharField(max_length = 600)
    eu_fecha_inicio = models.DateField()

class Sucursal(models.Model):
    suc_id = models.AutoField(primary_key = True)
    eu_nit = models.ForeignKey(Envios_up, on_delete = models.PROTECT)
    mun_id = models.ForeignKey(Municipio, on_delete = models.PROTECT)
    suc_nombre = models.CharField(max_length = 50)
    suc_telefono = models.CharField(max_length = 10)
    suc_direccion = models.CharField(max_length = 50)

class Tarifa(models.Model):
    tar_id = models.AutoField(primary_key = True)
    tar_municipal = models.DecimalField(max_digits = 10, decimal_places = 2)
    tar_departamental = models.DecimalField(max_digits = 10, decimal_places = 2)
    tar_nacional = models.DecimalField(max_digits = 10, decimal_places = 2)
