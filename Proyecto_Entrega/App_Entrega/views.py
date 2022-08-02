from django.http import HttpResponse
from App_Entrega.models import Cliente, Colaborador, Buzon
from App_Entrega.forms import Formulariocliente, Formulariocolaborador, Formulariobuzon
from django.shortcuts import render

#Pantallas principales

def inicio(self):
    return render(self,"inicio.html")

def cultural(self):
    return render (self, "cultural.html")

def gastronomico(self):
    return render(self, "gastronomico.html")

def natural(self):
    return render(self,"natural.html")


    
#Vistas para generar los registros de los formularios

def formularioClientes(request):

    return render(request,"formularioCliente.html")

def formularioColaboradores(request):
    
    return render(request,"formularioColaborador.html")

def formularioBuzon(request):
    
    return render(request,"formularioBuzon.html")


#Vistas para generar los ingresos de datos en la BD

def buscarCliente(request):

    if request.GET["correo"]:

        correo = request.GET['correo']
        cliente = Cliente.objects.filter(correo_icontains=correo)

        return render(request, "listaClientes.html", {"correo":correo, "cliente" : cliente})
    
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def buscarColaborador(request):

    if request.GET["correo"]:

        correo = request.GET['correo']
        colaborador = Colaborador.objects.filter(correo_icontains=correo)

        return render(request, "listaColaboradores.html", {"correo":correo, "colab" : cliente})
    
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
    
def buscarBuzon(request):

    if request.GET["correo"]:

        correo = request.GET['correo']
        sugerencia = Buzon.objects.filter(correo_icontains=correo)

        return render(request, "listaBuzon.html", {"correo":correo, "cliente" : cliente})
    
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)