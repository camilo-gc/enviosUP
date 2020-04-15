from django.contrib import admin
from django.urls import path
from personal import views

urlpatterns = [
    path('registroCliente/', views.registroCliente),
    path('login/', views.login_user),
]


