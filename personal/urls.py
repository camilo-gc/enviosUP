from django.contrib import admin
from django.urls import path
from personal import views

urlpatterns = [
    path('registroEmpleado/', views.registroEmpleado, name='registrarEmpleado'),
    path('login/', views.login_user, name= 'inicio_sesion'),
]
