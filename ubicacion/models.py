from django.db import models

# 0 -> Inactivo
# 1 -> Activo

class Departamento(models.Model):
    dep_id = models.AutoField(primary_key = True)
    dep_nombre = models.CharField(max_length = 70)
    dep_codigo = models.IntegerField()
    dep_estado = models.IntegerField(default = 0, max_length = 1)

    def __str__(self):
        return self.dep_nombre

class Municipio(models.Model):
    mun_id = models.AutoField(primary_key = True)
    dep_id = models.ForeignKey(Departamento, on_delete = models.PROTECT)
    mun_codigo = models.IntegerField()
    mun_nombre = models.CharField(max_length = 70)
    mun_estado = models.IntegerField(default = 0, max_length = 1)

    def __str__(self):
        return self.mun_nombre
