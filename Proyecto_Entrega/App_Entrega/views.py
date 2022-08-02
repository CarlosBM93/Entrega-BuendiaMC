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

    if request.method =='POST':

        cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'],correo=request.POST['correo'],actividad=request.POST['actividad'],fecha=request.POST['fecha'])
        
        cliente.save()

        return render(request,'inicio.html')

    return render(request,"formularioCliente.html")


def formularioColaboradores(request):
    
    if request.method=='POST':

        colaborador=Colaborador(nombre=request.POST['nombre'], apellido=request.POST['apellido'],telefono=request.POST['telefono'],correo=request.POST['correo'],negocio=request.POST['negocio'])
        
        colaborador.save()

    return render(request,"formularioColaborador.html")

def formularioBuzon(request):
    
    if request.method=='POST':
        buzon=Buzon(nombre=request.POST['nombre'], apellido=request.POST['apellido'], correo=request.POST['correo'], sugerencia=request.POST['sugerencia'])
        
        buzon.save()

    return render(request,"formularioBuzon.html")


#Vistas para busquedas en la BD

def busquedaCliente(request):

    return render(request,'busquedaClientes.html')


def resultadoCliente(request):

    if request.GET['actividad']:

        actividad = request.GET['actividad']

        cliente = Cliente.objects.filter(actividad__icontains=actividad)

        return render(request, "resultadosClientes.html", {"actividad" : actividad, "cliente" : cliente})
    
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def busquedaColaborador(request):

    return render(request,'busquedaColaboradores.html')


def resultadoColaborador(request):

    if request.GET['negocio']:

        negocio = request.GET['negocio']

        colaborador = Colaborador.objects.filter(negocio__icontains=negocio)

        return render(request, "resultadosColaboradores.html", {"negocio" : negocio, "colaborador" : colaborador})
    
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def busquedaBuzon(request):

    return render(request,'busquedaBuzon.html')


def resultadoBuzon(request):

    if request.GET['nombre']:

        cliente = request.GET['nombre']

        sugerencia = Buzon.objects.filter(nombre__icontains=cliente)

        return render(request, "resultadosBuzon.html", {"nombre" : cliente, "sugerencia" : sugerencia})
    
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
