from django.db import models
from empresa.models import Sucursal

# 0 -> Inactivo
# 1 -> Activo

class Tipo_documento(models.Model):
    td_id =  models.AutoField(primary_key = True)
    td_nombre = models.CharField(max_length = 50)
    td_descripcion = models.CharField(max_length = 350, null = True, blank = True)

class Funcionalidad(models.Model):
    fun_id =  models.AutoField(primary_key = True)
    fun_nombre = models.CharField(max_length = 100)
    fun_descripcion = models.CharField(max_length = 350, null = True, blank = True)

class Rol(models.Model):
    rol_id =  models.AutoField(primary_key = True)
    rol_nombre = models.CharField(max_length = 50)
    rol_descripcion = models.CharField(max_length = 350, null = True, blank = True)

class Funcionalidad_rol(models.Model):
    fun_id = models.ForeignKey(Funcionalidad, on_delete = models.PROTECT)
    rol_id = models.ForeignKey(Rol, on_delete = models.PROTECT)

class Persona(models.Model):
    per_documento = models.CharField(max_length = 15, primary_key = True) 
    td_id = models.ForeignKey(Tipo_documento, on_delete = models.PROTECT)
    per_nombre = models.CharField(max_length = 50)
    per_apellido = models.CharField(max_length = 50)
    per_fecha_naci = models.DateField()
    per_email = models.EmailField(null = True)
    per_contrasena = models.TextField()
    per_telefono = models.CharField(max_length = 10, null = True, blank = True)
    per_celular = models.CharField(max_length = 10, null = True, blank = True)
    per_direccion = models.CharField(max_length = 100)

class Cliente(models.Model):
    per_documento = models.ForeignKey(Persona,  on_delete = models.PROTECT, primary_key = True)
    cli_estado = models.IntegerField(default = 1, max_length = 1)
    cli_fecha_registro = models.DateField()

class Empleado(models.Model):
    emp_id = models.AutoField(primary_key = True)
    per_documento = models.OneToOneField(Persona, on_delete = models.PROTECT)
    suc_id = models.ForeignKey(Sucursal, on_delete = models.PROTECT)
    rol_id = models.ForeignKey(Rol, on_delete = models.PROTECT)
    emp_inicio_contrato = models.DateField()
    emp_fin_contrato = models.DateField()
    emp_salario = models.DecimalField(max_digits = 10, decimal_places = 2)
    emp_estado = models.IntegerField(default = 1, max_length = 1)

