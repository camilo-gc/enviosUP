from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.
def registroCliente(request):
    return render(request, 'cliente/Registro_cliente.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff is not False:
                return redirect(reverse_lazy('admin:index'))#Redirecciona panel admin #acordar lo de app_name para la rutas
#            else:
                #Se deve validar que rol tiene el usuario para redireccionarlo despues
#                return redirect(reverse_lazy('home'))#Redireccionar Panel NO administrador
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'empresa/index.html')#De prueba, se debe modificar.
#    if request.user.is_active:
#        return redirect(reverse_lazy('home'))
#    else:
#        return render(request, "")

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect(reverse_lazy('home'))

