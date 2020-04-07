from django.contrib import admin
from django.urls import path
from empresa.views import index

urlpatterns = [
    path('', index),
]
