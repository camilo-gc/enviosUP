from base64 import b64encode, b64decode
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from empresa.views import buscar_empleado
from empresa.models import Sucursal
from personal.models import Tipo_documento, Rol, Persona, Empleado

# Create your views here.

def registroEmpleado(request):
    tiposDoc = Tipo_documento.objects.all()
    roles = Rol.objects.all()
    sucursales = Sucursal.objects.all()
    if request.method == "POST":
        nombre = request.POST.get('nombre', None)
        apellido = request.POST.get('apellido', None)
        fecha_nac = request.POST.get('fecha_nacimiento', None)
        direccion = request.POST.get('direccion', None)
        telefono = request.POST.get('telefono', None)
        celular = request.POST.get('celular', None)
        tipo_doc = request.POST.get('tipo_documento', None)
        documento = request.POST.get('documento', None)
        correo = request.POST.get('correo', None)
        contrasena = codificarContrasena(request.POST.get('clave1', None))
        rol = request.POST.get('roles', None)
        sucursal = request.POST.get('sucursales', None)
        inicioContrato = request.POST.get('fecha_inicio', None)
        finContrato = request.POST.get('fecha_fin', None)
        salario = request.POST.get('salario', None)
        existe = Persona.objects.filter(per_documento=documento).exists()
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
        except:
            messages.error(request, 'Ocurrio un error.')
    else:
        ''

    return render(request, 'registroEmpleado.html', {'tipos': tiposDoc, 'roles': roles, 'suc': sucursales})


def login_user(request):

    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if request.user.is_superuser is not False:
            # Redirecciona panel admin #acordar lo de app_name para la rutas
            return redirect(reverse_lazy('administracion'))
        elif request.user.is_staff is not False:
            # Se deve validar que rol tiene el usuario para redireccionarlo despues
            # Redireccionar Panel NO administrador
            return redirect(reverse_lazy('operacion'))
        else:
            messages.error(
                request, 'Esta intentando ingresar al sistema desde un lugar no permitido')
            # De prueba, se debe modificar.
            return render(request, 'empresa/index.html')
    else:
        messages.error(request, 'Usuario o contraseña incorrectos')
        # De prueba, se debe modificar.
        return redirect(reverse_lazy('login'))

def eliminar_empleado(request):
    usuario = request.user
    if usuario.is_active:
        tiposDoc = Tipo_documento.objects.all()
        roles = Rol.objects.all()
        sucursales = Sucursal.objects.all()
        if request.method == "POST":
            documento = request.POST.get('per_documento', None)
            rol = request.POST.get('roles', None)
            sucursal = request.POST.get('suc_id', None)
            fin_contrato = request.POST.get('emp_finContrato', None)
            salario = request.POST.get('emp_salario', None)
            emp = Empleado.objects.filter(per_documento=documento)
            per = Persona.objects.filter(per_documento=documento)
            usu = User.objects.get(username = per[0].per_email)

            try:
                empleado = Empleado(emp_id=emp[0].emp_id)
                empleado.emp_inicio_contrato = emp[0].emp_inicio_contrato
                empleado.emp_fin_contrato = fin_contrato
                empleado.emp_salario = salario
                empleado.emp_estado = 0
                empleado.per_documento = per[0]
                empleado.rol_id = Rol(rol_id=rol)
                empleado.suc_id = Sucursal(suc_id=sucursal)
                empleado.save()
               
                usu.is_active = False
                usu.save()

                messages.success(request, 'El empleado se elimino con exito')

            except Exception as e:
                messages.error(request, "Algo ha salido mal")
                print(e)
        return render(request, 'empleado.html', {'tipos': tiposDoc, 'roles': roles, 'suc': sucursales})
    else:
        return redirect(reverse_lazy('login'))
 
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
            fin_contrato = request.POST.get('emp_finContrato', None)
            salario = request.POST.get('emp_salario', None)
            emp = Empleado.objects.filter(per_documento=documento)
            per = Persona.objects.filter(per_documento=documento)

            try:
                persona = Persona(per_documento=documento)                
                empleado = Empleado(emp_id=emp[0].emp_id)
                persona.per_documento_id = documento
                persona.per_nombre = nombre
                persona.per_apellido = apellido
                persona.per_fecha_naci = per[0].per_fecha_naci
                persona.per_email = correo
                persona.per_contraseña = per[0].per_contrasena #Revisar...
                persona.per_telefono = telefono
                persona.per_celular = celular
                persona.per_direccion = direccion
                persona.td_id = per[0].td_id
                empleado.emp_inicio_contrato = emp[0].emp_inicio_contrato
                empleado.emp_fin_contrato = fin_contrato
                empleado.emp_salario = salario
                empleado.emp_estado = emp[0].emp_estado
                empleado.per_documento = per[0]
                empleado.rol_id = Rol(rol_id=rol)
                empleado.suc_id = Sucursal(suc_id=sucursal)

                persona.save()
                empleado.save()
                messages.success(request, 'Revisando Actualización exitosa')
                messages.success(request, 'Actualización exitosa')

            except Exception as e:
                messages.error(request, "Algo ha salido mal")
                print(e)
        else:
            ''

        return render(request, 'empleado.html', {'tipos': tiposDoc, 'roles': roles, 'suc': sucursales})
    else:
        return redirect(reverse_lazy('login'))



def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect(reverse_lazy('login'))


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
