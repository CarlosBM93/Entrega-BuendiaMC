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

#Vistas para generar formularios

def formularioCliente(request):
    if request.method == 'POST':
        formulario = Formulariocliente()
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            registro = Cliente(nombre = data['nombre'],  apellido = data['apellido'], correo = data['correo'], actividad = data['actividad'], fecha = data['fecha'])
            registro.save()
            return render(request, "registroCliente.html")
        else:
            formulario = Formulariocliente()
        return render(request, "registroCliente.html", {"registros" : registro})

def formularioColaborador(request):
        if request.method == 'POST':
            formulario  = Formulariocolaborador()

        if formulario.is_valid():
            data = formulario.cleaned_data
            registro = Colaborador(nombre = data['nombre'],  apellido = data['apellido'], telefono = data['telefono'], correo = data['correo'], negocio = data['negocio'])
            registro.save()
            return render(request, "registroColaborador.html")
        else:
            formulario = Formulariocolaborador()
        return render(request, "registroColaborador.html", {"registros" : registro})

def formularioBuzon(request):
        if request.method == 'POST':
            formulario  = Formulariobuzon()

        if formulario.is_valid():
            data = formulario.cleaned_data
            registro = Buzon(nombre = data['nombre'],  apellido = data['apellido'], correo = data['correo'], sugerencia = data['sugerencia'])
            registro.save()
            return render(request, "registroBuzon.html")
        else:
            formulario = Formulariobuzon()
        return render(request, "registroBuzon.html", {"registros" : registro})
    
#Vistas para generar los buscadores de los formularios

