from django.shortcuts import render
from personal.models import Tipo_documento, Persona, Rol, Empleado
from empresa.models import Sucursal
from base64 import b64encode, b64decode
from django.contrib import messages

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
        try:
            persona = Persona(per_documento=documento, per_nombre=nombre, per_apellido=apellido, per_fecha_naci=fecha_nac,
                        per_email=correo, per_telefono=telefono, per_celular=celular, per_direccion=direccion, td_id_id=tipo_doc, per_contrasena=contrasena)
            persona.save()

            empleado = Empleado(per_documento_id=documento, suc_id_id=sucursal, rol_id_id=rol, emp_inicio_contrato=inicioContrato,
                        emp_fin_contrato=finContrato, emp_salario=salario, emp_estado=1)
            empleado.save()

            messages.success(request, 'Registro exitoso.')
        except:
            messages.error(request, 'Ocurrio un error.')
    else:''

    return render(request, 'cliente/registroEmpleado.html', {'tipos': tiposDoc, 'roles':roles, 'suc':sucursales})

 

def codificarContrasena(cadena):
    b = cadena.encode("UTF-8") # codificando la cadena en bytes
    e = b64encode(b) # codificar los bytes Base64
    con = e.decode("UTF-8") # decodificando los bytes Base64 a cadena
    return con

def decodificarContrasena(cadena):
    b1 = cadena.encode("UTF-8")# codificar la cadena codificaada Base64 en bytes
    d = b64decode(b1)# decodificando los bytes Base64
    con2 = d.decode("UTF-8") # decodificando los bytes a cadena
    return con2
