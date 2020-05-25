from base64 import b64encode, b64decode
import time
from random import randrange
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.models import User
from empresa.models import Sucursal, Tarifa, Envios_up
from envio.models import Tipo_mercancia
from personal.models import Tipo_documento, Persona, Empleado, Rol
from django.views.generic import View
from envio.models import Tipo_mercancia, Forma_pago, Tipo_mercancia, Destinatario, Mercancia
from personal.models import Tipo_documento, Persona, Empleado, Rol, Cliente
from ubicacion.models import Departamento, Municipio

# Create your views here.
from enviosUP.utileria_r import render_to_pdf #created in step 4

 
     
def Guia(request, numGuia):
    print("NUMERO DE GUIA: " + str(numGuia))
    mer = Mercancia.objects.all().filter(mer_num_guia = numGuia)
    emp = Envios_up.objects.all()
    data = {
        'numguia': numGuia,
        'doc_cli': str(mer[0].cli_documento.per_documento.per_documento),
        'fp': mer[0].fp_id.fp_nombre,
        'nom_cli': mer[0].cli_documento.per_documento.per_nombre,
        'ape_cli': mer[0].cli_documento.per_documento.per_apellido,
        'cel_cli': mer[0].cli_documento.per_documento.per_celular,
        'tel_cli': mer[0].cli_documento.per_documento.per_telefono,
        'cor_cli': mer[0].cli_documento.per_documento.per_email,
        'dir_cli': mer[0].cli_documento.per_documento.per_direccion,
        'doc_des': str(mer[0].des_documento.des_documento),
        'nom_des': mer[0].des_documento.des_nombre,
        'cel_des': mer[0].des_documento.des_celular,
        'tel_des': mer[0].des_documento.des_telefono,
        'mun': str(mer[0].des_documento.mun_id.mun_nombre) + " - " + str(mer[0].des_documento.mun_id.dep_id.dep_nombre),
        'dir_des': mer[0].des_documento.des_direccion,
        'cor_des': mer[0].des_documento.des_email,
        'tm': mer[0].tm_id.tm_nombre,
        'peso': str(mer[0].mer_peso),
        'con': mer[0].mer_contenido,
        'dec': str(mer[0].mer_precio),
        'precio': str(mer[0].mer_precio_envio),
        'n': [0,1,2],
        'nombre': emp[0].eu_nombre,
        'nit': emp[0].eu_nit,
        'suc': mer[0].emp_id.suc_id.suc_nombre,
        'direccion': mer[0].emp_id.suc_id.suc_direccion + ", "+ mer[0].emp_id.suc_id.mun_id.mun_nombre + " - " +mer[0].emp_id.suc_id.mun_id.dep_id.dep_nombre,
        'correo': emp[0].eu_email,
        'telefono': mer[0].emp_id.suc_id.suc_telefono,
        'fecha': time.strftime("%d-%m-%Y"),
    }
    print(data)
    pdf = render_to_pdf('Guia.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def index(request):
    return render(request, 'empresa/index.html', {})


def rastreo(request):
    return render(request, 'rastreo.html', {})


def login(request):
    return render(request, 'login.html', {})

"""def eliminar_emp(request):
    tiposDoc = Tipo_documento.objects.all()
    return render(request, 'eliminar_empleado.html', {'tipo':tiposDoc})
"""
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

def registrar_mercancia(request):
    numGuia = "Ninguno"
    formapago = Forma_pago.objects.all()
    tipomer = Tipo_mercancia.objects.all()
    muni = Municipio.objects.select_related('dep_id').filter(mun_estado=1).order_by('mun_id')
    
    if request.method == "POST":
        #Persona
        doc = request.POST.get('cli_doc', None)
        nom = request.POST.get('cli_nom', None)
        ape = request.POST.get('cli_ape', None)
        cel = request.POST.get('cli_cel', None)
        tel = request.POST.get('cli_tel', None)
        email = request.POST.get('cli_cor', None)
        direccion = request.POST.get('cli_dir', None)
        #Destinatario
        desDoc = request.POST.get('des_doc', None)
        desNom = request.POST.get('des_nom', None)
        desCel = request.POST.get('des_cel', None)
        desTel = request.POST.get('des_tel', None)
        desMun = request.POST.get('mun', None)
        desDir = request.POST.get('des_dir', None)
        desCor = request.POST.get('des_cor', None)
        #Mercancia
        fp = request.POST.get('fpago', None)
        tm = request.POST.get('tmer', None)
        con = request.POST.get('contenido', None)
        peso = request.POST.get('peso', None)
        alto = request.POST.get('alto', None)
        largo = request.POST.get('largo', None)
        ancho = request.POST.get('ancho', None)
        declarado = request.POST.get('declarado', None)
        precio = request.POST.get('precio', None)
        #Empleado
        empleado = request.POST.get('emp_doc', None)

        tarifas = Tarifa.objects.all()
        emp = Empleado.objects.select_related('suc_id').filter(per_documento=empleado)
        des = Municipio.objects.select_related('dep_id').filter(mun_id=desMun)
        emp_dep = emp[0].suc_id.mun_id.dep_id.dep_id
        des_dep = des[0].dep_id.dep_id
        
        if (emp_dep == des_dep):
            precio = int(precio) + tarifas[0].tar_departamental
        else:
            precio = int(precio) + tarifas[0].tar_nacional
        print(precio)
        try:
            person = Persona(per_documento=int(doc), td_id_id = 1, per_nombre=nom, per_apellido=ape, per_celular=cel, per_telefono=tel, per_email=email, per_direccion=direccion)
            person.save()
            existe = Cliente.objects.filter(per_documento=doc).exists()
            if (existe):
                cli = Cliente.objects.filter(per_documento=doc)
            else:
                fecha = time.strftime("%Y-%m-%d")
                cliente = Cliente(per_documento_id=doc, cli_fecha_registro = fecha)
                cliente.save()
                cli = Cliente.objects.filter(per_documento=doc)
            

            destino = Destinatario(des_documento=desDoc, des_nombre=desNom, des_celular=desCel, des_telefono=desTel, des_direccion=desDir, des_email=desCor, mun_id_id=int(desMun))
            destino.save()
            numGuia = time.strftime("%Y%m%d") + str(randrange(10000))

            if (int(tm) == 1):
                mercancia = Mercancia(tm_id_id = int(tm), fp_id_id = int(fp), cli_documento_id = int(cli[0].cli_id), des_documento_id = int(desDoc), emp_id_id = int(emp[0].emp_id), mer_contenido = con, mer_peso = int(peso), mer_precio = int(declarado), mer_precio_envio = int(precio), mer_num_guia = numGuia)
                mercancia.save()
                messages.success(request, 'Registro exitoso. Número de Guía: ' + numGuia)
            else:
                mercancia = Mercancia(tm_id_id = int(tm), fp_id_id = int(fp), cli_documento_id = int(cli[0].cli_id), des_documento_id = int(desDoc), emp_id_id = int(emp[0].emp_id), mer_contenido = con, mer_peso = int(peso), mer_alto = int(alto), mer_ancho = int(ancho), mer_largo = int(largo), mer_precio = int(declarado), mer_precio_envio = int(precio), mer_num_guia = numGuia)
                mercancia.save()
                messages.success(request, 'Registro exitoso. Número de Guía: ' + numGuia)
                Guia(request)
        except Exception as e:
                messages.error(request, "Algo ha salido mal")
                print(e)
    else: ''


    return render(request, 'registrar_mercancia.html', {'fp': formapago, 'tm': tipomer, 'mun': muni, 'guia': numGuia})
    
def buscar_cliente_ajax(request):
    doc = request.GET.get('doc')
    person = Persona.objects.filter(per_documento=doc)
    data = serializers.serialize('json', person, fields = ('per_documento', 'per_nombre', 'per_apellido', 'per_telefono', 'per_celular', 'per_direccion', 'per_email'))
    return HttpResponse(data, content_type='application/json')

def buscar_destinatario_ajax(request):
    doc = request.GET.get('doc')
    destinatario = Destinatario.objects.filter(des_documento = doc)
    data = serializers.serialize('json', destinatario, fields = ('des_documento', 'mun_id', 'des_nombre', 'des_telefono', 'des_celular', 'des_direccion', 'des_email'))
    return HttpResponse(data, content_type='application/json')

def buscar_empleado_ajax(request):
    doc = request.GET.get('doc')
    person = Empleado.objects.filter(per_documento = doc)
    data = serializers.serialize('json', person, fields = ('emp_id', 'emp_estado'))
    return HttpResponse(data, content_type='application/json')

def buscar_precio(request):
    tm = request.GET.get('id')
    precio = Tipo_mercancia.objects.filter(tm_id = tm)
    data = serializers.serialize('json', precio, fields = ('tm_id','tm_precio', 'tm_precio_adicional'))
    return HttpResponse(data, content_type='application/json')


def modificar_cliente(request):
    return render(request, 'modificar_cliente.html', {})

def modificar_empleado(request):
    usuario = request.user
    if usuario.is_active:

        tiposDoc = Tipo_documento.objects.all()
        roles = Rol.objects.all()
        sucursales = Sucursal.objects.all()
        if request.method == "POST":
            nombre = request.POST.get('per_nombre', None)
            apellido = request.POST.get('per_apellido', None)
            direccion = request.POST.get('per_direccion', None)
            telefono = request.POST.get('per_telefono', None)
            celular = request.POST.get('per_celular', None)
            documento = request.POST.get('per_documento', None)
            correo = request.POST.get('per_email', None)
            rol = request.POST.get('roles', None)
            sucursal = request.POST.get('suc_id', None)
            finContrato = request.POST.get('emp_finContrato', None)
            salario = request.POST.get('emp_salario', None)
            existe = Persona.objects.filter(per_documento=documento).exists()
            try:
                if(existe):
                    persona = Persona(per_documento=documento, per_nombre=nombre, per_apellido=apellido,
                                      per_email=correo, per_telefono=telefono, per_celular=celular, per_direccion=direccion)
                    emp = Empleado.objects.all().filter(per_documento_id = documento)
                    empleado = Empleado(emp_id=emp[0].emp_id, suc_id_id=sucursal, rol_id_id=rol,
                                        emp_fin_contrato=finContrato, emp_salario=salario, emp_estado=1)
                   
                    persona.save()
                    empleado.save()
                    messages.success(request, 'Actualización exitosa')
                    
                else:
                    messages.info(request, 'No se encuentra registrado')
                    
            except Exception as e:
                messages.error(request, "Algo ha salido mal")
                print(e)
        else:
            ''

        return render(request, 'empleado.html', {'tipos': tiposDoc, 'roles': roles, 'suc': sucursales})
    else:
        return redirect(reverse_lazy('login'))


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
            try:
                if(existe):
                    messages.info(request, 'Ya se encuentra registrado.')
                else:
                    persona = Persona(per_documento=documento, per_nombre=nombre, per_apellido=apellido, per_fecha_naci=fecha_nac,
                                      per_email=correo, per_telefono=telefono, per_celular=celular, per_direccion=direccion, td_id_id=tipo_doc, per_contrasena=contrasena)
                    empleado = Empleado(per_documento_id=documento, suc_id_id=sucursal, rol_id_id=rol, emp_inicio_contrato=inicioContrato,
                                        emp_fin_contrato=finContrato, emp_salario=salario, emp_estado=1)
                    usuario = User.objects.create_user(correo, correo, contrasena)
                    usuario.first_name = nombre
                    usuario.last_name = apellido
                    usuario.is_staff = True
                    

                    if rol == '1':
                        usuario.is_superuser = True

                    persona.save()
                    empleado.save()
                    usuario.save()
                    messages.success(request, 'Registro exitoso.')
            except Exception as e:
                messages.error(request, "Algo ha salido mal")
                print(e)
        else:
            ''

        return render(request, 'empleado.html', {'tipos': tiposDoc, 'roles': roles, 'suc': sucursales})
    else:
        return redirect(reverse_lazy('login'))  # Probaaaaaar!!!

def buscar_empleado(request):
    documento = request.POST.get('bus_per_documento', None)
    emp = Empleado.objects.filter(per_documento_id=documento).filter(emp_estado = 1)
    if emp.exists():
        tiposDoc = Tipo_documento.objects.all()
        roles = Rol.objects.all()
        sucursales = Sucursal.objects.all()
        per = emp[0].per_documento
        id_rol = emp[0].rol_id.rol_id
        id_suc = emp[0].suc_id.suc_id
        return render(request, 'eliminar_empleado.html', {'tipos': tiposDoc, 'roles': roles, 'suc': sucursales, 'per':per, 'emp':emp, 'rol':id_rol, 'su': id_suc})
    else:
        messages.info(request, 'Empleado no encontrado.')
        return redirect(reverse_lazy('empleado'))

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
    return render(request, 'empresa/nosotros.html', {'sucu': sucursales})


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
