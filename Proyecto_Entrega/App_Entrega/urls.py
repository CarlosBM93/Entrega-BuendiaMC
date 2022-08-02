
from django.contrib import admin
from django.urls import path
from App_Entrega.views import inicio, cultural, gastronomico, natural, formularioClientes, formularioColaboradores, formularioBuzon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('cultural/', cultural, name='cultural'),
    path('gastronomico/', gastronomico, name='gastronomico'),
    path('natural/', natural, name='natural'),

    path('formulario-cliente/',formularioClientes, name='formularioCliente'),
    path('formulario-colaborador/', formularioColaboradores, name='formularioColaborador'),
    path('buzon/', formularioBuzon, name='buzon'),
]
