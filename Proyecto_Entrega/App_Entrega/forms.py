from django import forms

class Formulariocliente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    actividad = forms.CharField()
    fecha = forms.DateField()

class Formulariocolaborador(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    correo = forms.EmailField()
    negocio = forms.CharField()  

class Formulariobuzon(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    sugerencia = forms.CharField()
