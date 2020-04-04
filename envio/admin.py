from django.contrib import admin
from envio.models import Tipo_mercancia, Forma_pago, Envio, Mercancia, Estado, Estado_envio, Destinatario

# Register your models here.
admin.site.register(Tipo_mercancia)
admin.site.register(Forma_pago)
admin.site.register(Mercancia)
admin.site.register(Destinatario)
admin.site.register(Envio)
admin.site.register(Estado)
admin.site.register(Estado_envio)

