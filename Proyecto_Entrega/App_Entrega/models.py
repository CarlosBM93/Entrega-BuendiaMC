from mailbox import NoSuchMailboxError
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido =models.CharField(max_length=80)
    correo =models.EmailField()
    actividad =models.CharField(max_length=80)
    fecha = models.DateField()

class Colaborador(models.Model):
    nombre = models.CharField(max_length=80)
    apellido =models.CharField(max_length=80)
    telefono = models.IntegerField()
    correo =models.EmailField()
    Negocio = models.CharField(max_length=80)  

class Buzon(models.Model):
    nombre = models.CharField(max_length=80)
    apellido =models.CharField(max_length=80)
    correo =models.EmailField()
    sugerencia =models.CharField(max_length=80)
