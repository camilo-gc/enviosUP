from django.shortcuts import render

# Create your views here.
def registroCliente(request):
    return render(request, 'cliente/Registro_cliente.html', {})
