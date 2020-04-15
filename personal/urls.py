from django.contrib import admin
from django.urls import path
from personal import views

urlpatterns = [
    path('registroEmpleado/', views.registroEmpleado, name='registrarEmpleado'),
    path('usuario/nuevo/', views.Persona, name='register'),
    path('login/', views.login_user),
]


