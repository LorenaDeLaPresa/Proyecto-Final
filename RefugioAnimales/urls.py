"""RefugioAnimales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from django.views import View
from blog.views import index 
from animal.views import AnimalCreate, AnimalList, animal_list
from usuario.views import RegistroUsuario
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nuevo/', AnimalCreate.as_view(), name='animal_crear'),
    path('listar/', animal_list, name='animal_listar'),
    path('blog', index),    
    path('listar2', AnimalList.as_view(), name='animal_listar2'),
    path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),
    #path('api-auth/', include('rest_framework.urls'))
]
