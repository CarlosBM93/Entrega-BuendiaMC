
from django.contrib import admin
from django.urls import path
from App_Entrega.views import inicio, cultural, gastronomico, natural, formularioCliente, formularioColaborador, formularioBuzon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('cultural/', cultural, name='cultural'),
    path('gastronomico/', gastronomico, name='gastronomico'),
    path('natural/', natural, name='natural'),
    path('registro-cliente/',formularioCliente, name='registro_cliente'),
    path('registro-colaborador/', formularioColaborador, name='registro_colaborador'),
    path('buzon/', formularioBuzon, name='buzon'),
]
