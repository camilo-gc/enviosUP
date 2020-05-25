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
    path('rastreo/', views.rastreo, name= 'rastreo'),
    path('PL_principal/', views.PL_principal, name='PL_principal'),
    path('PL_R_Mercancia/', views.PL_R_Mercancia, name='PL_R_Mercancia'),
    path('PL_L_Mercancia/', views.PL_L_Mercancia, name='PL_L_Mercancia'),
    path('PL_L_envios/', views.PL_L_envios, name='PL_L_envios'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_envio/', views.registrar_envio, name='registrar_envio'),
    path('modificar_cliente/', views.modificar_cliente, name='modificar_cliente'),
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('buscar_empleado/', views.buscar_empleado, name='buscar_emp'),
    
]
