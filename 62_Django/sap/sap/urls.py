"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from webapp.views import bienvenido
from webapp.views import domicilios
from personas.views import detallePersona, nuevoDomicilio, detalleDomicilio, editarDomicilio, eliminarDomicilio
from personas.views import nuevaPersona
from personas.views import editarPersona
from personas.views import eliminarPersona

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bienvenido/', bienvenido)
    path('', bienvenido, name='index'),
    path('domicilios', domicilios, name='domicilios'),
    path('detalle_persona/<int:id>', detallePersona),
    path('detalle_domicilio/<int:id>', detalleDomicilio),
    path('nueva_persona', nuevaPersona),
    path('nuevo_domicilio', nuevoDomicilio),
    path('editar_persona/<int:id>', editarPersona),
    path('editar_domicilio/<int:id>', editarDomicilio),
    path('eliminar_persona/<int:id>', eliminarPersona),
    path('eliminar_domicilio/<int:id>', eliminarDomicilio)
]
