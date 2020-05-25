from django.contrib import admin
from django.urls import path
from personal import views

urlpatterns = [
    path('registroEmpleado/', views.registroEmpleado, name='registrarEmpleado'),
    path('validacion/', views.login_user, name= 'inicio_sesion'),
    path('validacion/', views.login_user, name= 'validacion'),
    path('logout/', views.logout, name= 'logout'),
    path('mod_emp/', views.modificar_empleado, name='modificar_empleado'),
    path('elim_emp/', views.eliminar_empleado, name='eliminar_empleado'),
]
