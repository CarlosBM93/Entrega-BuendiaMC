
from django.db import models

class Cliente(models.Model):

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    correo = models.EmailField()
    actividad = models.CharField(max_length=80)
    fecha = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.actividad}'
class Colaborador(models.Model):

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    telefono = models.IntegerField()
    correo = models.EmailField()
    negocio = models.CharField(max_length=80)  

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} - {self.negocio}'
class Buzon(models.Model):

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    correo = models.EmailField()
    sugerencia = models.CharField(max_length=280)

    def __str__(self) -> str:
       return f'{self.nombre} {self.apellido} - {self.sugerencia}'