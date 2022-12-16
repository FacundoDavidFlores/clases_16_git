"""mi_proyecto URL Configuration

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
from django.contrib import admin
from django.urls import path
from AppCoder.views import (saludo, saludo_dos, saludo_a, mostrar_mi_template, mostrar_familiares, 
                            BuscarFamiliar, AltaFamiliar)
from blog.views import index as blog_index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/saludar', saludo),
    path('hola-mundo/saludar-dos', saludo_dos),
    path('hola-mundo/saludar/<nombre>', saludo_a),
    path('mostrar_mi_template/', mostrar_mi_template),
    path('mi_familiar/', mostrar_familiares),
    path('blog/', blog_index),
    path('mi_familiar/buscar', BuscarFamiliar.as_view()),
    path('mi_familiar/alta', AltaFamiliar.as_view()),
]
