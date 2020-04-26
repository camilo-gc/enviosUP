from django.shortcuts import render
from django.http import HttpResponse
from empresa.models import Sucursal, Tarifa
from envio.models import Tipo_mercancia

# Create your views here.
def index(request):
    return render(request, 'empresa/index.html', {})

def puntosServicios(request):
    sucursales = Sucursal.objects.all().order_by('mun_id')
    return render(request, 'empresa/', {'suc':sucursales})

def tarifas(request):
    tarifas = Tarifa.objects.all()
    tiposMercancias = Tipo_mercancia.objects.all()
    return render(request, 'empresa/tarifas.html', {'tar':tarifas[0] , 'tms':tiposMercancias})

def descubrenos(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'empresa/nosotros.html',{'sucu':sucursales})

def politicas(request):
    return render(request, 'empresa/legal.html',{})