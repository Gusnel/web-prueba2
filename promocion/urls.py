"""promocion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from modulos.mp.views import form, contact, list, visitarMipyme, addpromo, registrarMipyme, eliminarMipyme, buscar_productos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', form),
    path('contact/', contact),
    path('list/', list),
    path('list/visitarMipyme/<int:codigo>/', visitarMipyme),
    path('addpromo/', addpromo),
    path('registrarMipyme/', registrarMipyme),
    path('eliminarMipyme/<codigo>', eliminarMipyme),
    path('buscar_productos/', buscar_productos, name='buscar_productos'),
    path('visitarMipyme/<codigo>/', visitarMipyme, name='visitarMipyme'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

