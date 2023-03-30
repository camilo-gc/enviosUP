from django.contrib import admin
from personal.models import Tipo_documento, Persona, Cliente, Empleado, Rol, Funcionalidad, Funcionalidad_rol
# Register your models here.

admin.site.register(Tipo_documento)
admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(Funcionalidad)
admin.site.register(Funcionalidad_rol)