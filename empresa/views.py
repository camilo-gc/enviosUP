from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from empresa.models import Sucursal, Tarifa
from envio.models import Tipo_mercancia

# Create your views here.


def index(request):
    return render(request, 'empresa/index.html', {})


def login(request):
    return render(request, 'login.html', {})


def administracion(request):
    usuario = request.user
    if usuario.is_active:
        return render(request, 'administracion.html', {'user': usuario})
    else:
        return redirect(reverse_lazy('login'))  # Probaaaaaar!!!


def operacional(request):
    usuario = request.user
    if usuario.is_active:
        return render(request, 'operacional.html', {'user': usuario})
    else:
        return redirect(reverse_lazy('login'))  # Probaaaaaar!!!


def puntosServicios(request):
    sucursales = Sucursal.objects.all().order_by('mun_id')
    return render(request, 'empresa/', {'suc': sucursales})


def tarifas(request):
    tarifas = Tarifa.objects.all()
    tiposMercancias = Tipo_mercancia.objects.all()
    return render(request, 'empresa/tarifas.html', {'tar': tarifas[0], 'tms': tiposMercancias})


def descubrenos(request):
    return render(request, 'empresa/nosotros.html', {})


def politicas(request):
    return render(request, 'empresa/legal.html', {})
