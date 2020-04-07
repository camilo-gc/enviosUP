from django.db import models
from personal.models import Cliente
from personal.models import Empleado
from ubicacion.models import Municipio
from vehiculo.models import Vehiculo

# 0 -> Inactivo
# 1 -> Activo

#  envio, estado, estado envio
class Forma_pago(models.Model):
    fp_id = models.AutoField(primary_key = True)
    fp_nombre = models.CharField(max_length = 50)
    tv_descripcion = models.CharField(max_length = 350, null = True, blank = True)

class Tipo_mercancia(models.Model):
    tm_id = models.AutoField(primary_key = True)
    tm_nombre = models.CharField(max_length = 50)
    tm_peso_max = models.IntegerField()
    tm_peso_min = models.IntegerField()
    tm_precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    tm_precio_adicional = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0, blank = True)
    tm_descripcion = models.CharField(max_length = 350, null = True, blank = True)
    tv_estado =  models.IntegerField()

class Destinatario(models.Model):
    des_id = models.AutoField(primary_key = True)
    mun_id = models.ForeignKey(Municipio, on_delete = models.PROTECT)
    des_documento = models.CharField(max_length = 15)
    des_nombre = models.CharField(max_length = 100)
    des_direccion = models.CharField(max_length = 50)
    des_telefono = models.CharField(max_length = 15, blank = True)
    des_celular = models.CharField(max_length = 15)

class Mercancia(models.Model):
    mer_id = models.AutoField(primary_key = True)
    cli_documento = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    des_documento = models.ForeignKey(Destinatario, on_delete = models.PROTECT)
    tm_id = models.ForeignKey(Tipo_mercancia, on_delete = models.PROTECT)
    emp_id = models.ForeignKey(Empleado, on_delete = models.PROTECT)
    fp_id = models.ForeignKey(Forma_pago, on_delete = models.PROTECT)
    mer_peso = models.DecimalField(max_digits = 10, decimal_places = 2)
    mer_alto = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
    mer_ancho = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
    mer_largo = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
    mer_precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    mer_precio_envio = models.DecimalField(max_digits = 10, decimal_places = 2)

class Envio(models.Model):
    env_id = models.AutoField(primary_key = True)
    mer_id = models.ForeignKey(Mercancia, on_delete = models.PROTECT)
    veh_id = models.ForeignKey(Vehiculo, on_delete = models.PROTECT)
    emp_id = models.ForeignKey(Empleado, on_delete = models.PROTECT)
    env_registro = models.DateField()
    env_entrega_estimada = models.DateField()

class Estado(models.Model):
    est_id = models.AutoField(primary_key = True)
    est_nombre = models.CharField(max_length = 50)
    est_descripcion = models.CharField(max_length = 350, null = True, blank = True)
    est_envio = models.ManyToManyField(Envio, through='Estado_envio')

class Estado_envio(models.Model):
    env_id = models.ForeignKey(Envio, on_delete = models.PROTECT)
    est_id = models.ForeignKey(Estado, on_delete = models.PROTECT)
    ee_fecha = models.DateField()
    ee_descripcion = models.CharField(max_length = 350, null = True, blank = True)


