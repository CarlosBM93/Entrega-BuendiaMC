
from django.contrib import admin
from django.urls import path
from views import inicio, cultural, gastronomico, natural, formularioCliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('cultural/', cultural),
    path('gastronomico/', gastronomico),
    path('natural/', natural),
    path('registro-cliente/',formularioCliente)
]
