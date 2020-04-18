from django.contrib import admin
from django.urls import path
from empresa import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tarifas/', views.tarifas, name='tarifas'),
    path('descrubrenos/', views.descubrenos, name='descubrenos'),
    path('politicas/', views.politicas, name='politicas'),
]
