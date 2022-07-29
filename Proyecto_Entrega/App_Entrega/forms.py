from django import forms

class Cliente(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    actividad = forms.CharField()
    fecha = forms.DateField()

class Colaborador(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    correo = forms.EmailField()
    Negocio = forms.CharField()  

class Buzon(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    sugerencia = forms.CharField()
