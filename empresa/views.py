from base64 import b64encode, b64decode
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from empresa.models import Sucursal, Tarifa
from envio.models import Tipo_mercancia
from personal.models import Tipo_documento, Persona, Empleado, Rol
from django.views.generic import View
# Create your views here.
from enviosUP.utileria_r import render_to_pdf #created in step 4

 
     
def Guia(request):
    pdf = render_to_pdf('Guia.html')
    return HttpResponse(pdf, content_type='application/pdf')


def index(request):
    return render(request, 'empresa/index.html', {})


def login(request):
    return render(request, 'login.html', {})

def PL_principal(request):
    return render(request, 'PL_principal.html', {})

def PL_R_Mercancia(request):
    return render(request, 'PL_R_Mercancia.html', {})

def PL_L_Mercancia(request):
    return render(request, 'PL_L_Mercancia.html', {})

def PL_L_envios(request):
    return render(request, 'PL_L_envios.html', {})
    
def registrar_cliente(request):
    return render(request, 'registrar_cliente.html', {})

def registrar_envio(request):
    return render(request, 'registrar_envio.html', {})

def modificar_cliente(request):
    return render(request, 'modificar_cliente.html', {})

def buscar_cliente(request):
    return render(request, 'buscar_cliente.html', {})

def administracion(request):
    usuario = request.user
    if usuario.is_active:
        return render(request, 'administracion.html', {'user': usuario})
    else:
        return redirect(reverse_lazy('login'))  # Probaaaaaar!!!

def empleado(request):
    usuario = request.user
    if usuario.is_active:

        tiposDoc = Tipo_documento.objects.all()
        roles = Rol.objects.all()
        sucursales = Sucursal.objects.all()
        if request.method == "POST":
            nombre = request.POST.get('per_nombre', None)
            apellido = request.POST.get('per_apellido', None)
            fecha_nac = request.POST.get('per_fechanaci', None)
            direccion = request.POST.get('per_direccion', None)
            telefono = request.POST.get('per_telefono', None)
            celular = request.POST.get('per_celular', None)
            tipo_doc = request.POST.get('tipo_documento', None)
            documento = request.POST.get('per_documento', None)
            correo = request.POST.get('per_email', None)
            contrasena = request.POST.get('per_contraseña', None)
            rol = request.POST.get('roles', None)
            sucursal = request.POST.get('suc_id', None)
            inicioContrato = request.POST.get('emp_inicioContrato', None)
            finContrato = request.POST.get('emp_finContrato', None)
            salario = request.POST.get('emp_salario', None)
            existe = Persona.objects.filter(per_documento=documento).exists()
            print(nombre)
            print(rol)
            print(sucursal)
            print(tipo_doc)
            print(existe)
            print(apellido)
            print(correo)
            print(fecha_nac)
            print(inicioContrato)
            print(finContrato)
            print(salario)
            try:
                if(existe):
                    messages.info(request, 'Ya se encuentra registrado.')
                else:
                    persona = Persona(per_documento=documento, per_nombre=nombre, per_apellido=apellido, per_fecha_naci=fecha_nac,
                                per_email=correo, per_telefono=telefono, per_celular=celular, per_direccion=direccion, td_id_id=tipo_doc, per_contrasena=contrasena)
                    empleado = Empleado(per_documento_id=documento, suc_id_id=sucursal, rol_id_id=rol, emp_inicio_contrato=inicioContrato,
                                emp_fin_contrato=finContrato, emp_salario=salario, emp_estado=1)
                    persona.save()
                    empleado.save()
                    messages.success(request, 'Registro exitoso.')
            except Exception as e:
                messages.error(request, "Algo ha salido mal")
                print (e)
        else:
            ''


        return render(request, 'empleado.html', {'tipos': tiposDoc, 'roles': roles, 'suc': sucursales})
    else:
        return redirect(reverse_lazy('login'))  # Probaaaaaar!!!

def l_envios(request):
    usuario = request.user
    if usuario.is_active:
        return render(request, 'l_envios.html')
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
    sucursales = Sucursal.objects.select_related('mun_id').order_by('mun_id')
    return render(request, 'empresa/nosotros.html',{'sucu':sucursales})

def politicas(request):
    return render(request, 'empresa/legal.html', {})



def codificarContrasena(cadena):
    b = cadena.encode("UTF-8")  # codificando la cadena en bytes
    e = b64encode(b)  # codificar los bytes Base64
    con = e.decode("UTF-8")  # decodificando los bytes Base64 a cadena
    return con


def decodificarContrasena(cadena):
    # codificar la cadena codificaada Base64 en bytes
    b1 = cadena.encode("UTF-8")
    d = b64decode(b1)  # decodificando los bytes Base64
    con2 = d.decode("UTF-8")  # decodificando los bytes a cadena
    return con2

