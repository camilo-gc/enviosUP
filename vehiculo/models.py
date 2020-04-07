from django.db import models
from personal.models import Empleado

# 0 -> Inactivo
# 1 -> Activo

class Tipo_vehiculo(models.Model):
   tv_id = models.AutoField(primary_key = True)
   tv_nombre = models.CharField(max_length = 100)
   tv_descripcion = models.CharField(max_length = 350, null = True, blank = True)
   tv_estado = models.IntegerField(default = 1, max_length = 1)

class Vehiculo(models.Model):
    veh_id = models.AutoField(primary_key = True)
    tv_id = models.ForeignKey(Tipo_vehiculo, on_delete = models.PROTECT)
    emp_id = models.ForeignKey(Empleado, on_delete = models.PROTECT)
    veh_marca = models.CharField(max_length = 50)
    veh_modelo = models.CharField(max_length = 50)
    veh_matricula = models.CharField(max_length = 50)
    veh_capacidad = models.CharField(max_length = 50)
    veh_cubicaje = models.CharField(max_length = 50)
    veh_estado = models.IntegerField(default = 1, max_length = 1)
