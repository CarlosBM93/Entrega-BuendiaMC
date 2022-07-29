
from django.contrib import admin
from django.urls import path
from App_Entrega.views import inicio, cultural, gastronomico, natural, formularioCliente, formularioColaborador, formularioBuzon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('cultural/', cultural),
    path('gastronomico/', gastronomico),
    path('natural/', natural),
    path('registro-cliente/',formularioCliente),
    path('registro-colaborador/', formularioColaborador),
    path('buzon/', formularioBuzon),
]
