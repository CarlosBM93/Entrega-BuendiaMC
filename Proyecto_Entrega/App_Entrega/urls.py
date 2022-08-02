
from django.contrib import admin
from django.urls import path
from App_Entrega.views import inicio, cultural, gastronomico, natural, formularioClientes, formularioColaboradores, formularioBuzon, busquedaCliente, resultadoCliente, busquedaColaborador,resultadoColaborador, busquedaBuzon, resultadoBuzon

urlpatterns = [

    #url de los apartados principales de la página
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('cultural/', cultural, name='cultural'),
    path('gastronomico/', gastronomico, name='gastronomico'),
    path('natural/', natural, name='natural'),

    #url de los formularios
    path('formulario-cliente/',formularioClientes, name='formularioCliente'),
    path('formulario-colaborador/', formularioColaboradores, name='formularioColaborador'),
    path('buzon/', formularioBuzon, name='buzon'),

    #url para busqueda en los formularios
    path('busquedaCliente/',busquedaCliente, name='busquedaCliente'),
    path('resultadoCliente/',resultadoCliente,name='resultadoCliente'),

    path('busquedaColaborador/',busquedaColaborador, name='busquedaColaborador'),
    path('resultadoColaborador/',resultadoColaborador,name='resultadoColaborador'),

    path('busquedaBuzon/',busquedaBuzon, name='busquedaBuzon'),
    path('resultadoBuzon/',resultadoBuzon,name='resultadoBuzon'),
]
