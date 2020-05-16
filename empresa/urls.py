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
]
