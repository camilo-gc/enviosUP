from django.contrib import admin
from django.urls import path
from empresa import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tarifas/', views.tarifas, name='tarifas'),
    path('descubrenos/', views.descubrenos, name='descubrenos'),
    path('politicas/', views.politicas, name='politicas'),
    path('administracion/', views.administracion, name= 'administracion'),
    path('operacion/', views.operacional, name= 'operacion'),
    path('login/', views.login, name= 'login'),
    path('empleado/', views.empleado, name= 'empleado'),
    path('l_envios/', views.l_envios, name= 'l_envios'),
    path('rastreo/<int:numGuia>/', views.rastreo, name= 'rastreo'),
    path('PL_principal/', views.PL_principal, name='PL_principal'),
    path('PL_R_Envio/', views.PL_R_Envio, name='PL_R_Envio'),
    path('PL_L_Mercancia/', views.PL_L_Mercancia, name='PL_L_Mercancia'),
    path('PL_L_envios/', views.PL_L_envios, name='PL_L_envios'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_mercancia/', views.registrar_mercancia, name='registrar_mercancia'),
    path('modificar_cliente/', views.modificar_cliente, name='modificar_cliente'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('buscar_empleado/', views.buscar_empleado, name='buscar_emp'),    
    path('Guia/<int:numGuia>/', views.Guia, name='Guia'), 
    path('buscar_cliente_ajax/', views.buscar_cliente_ajax, name='buscar_cliente_ajax'),
    path('buscar_destinatario_ajax/', views.buscar_destinatario_ajax, name='buscar_destinatario_ajax'),
    path('buscar_precio/', views.buscar_precio, name='buscar_precio'),
    path('buscar_empleado_ajax/', views.buscar_empleado_ajax, name='buscar_empleado_ajax'),
]
