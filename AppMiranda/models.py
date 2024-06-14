from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre=models.CharField(max_length=40)

    marca=models.CharField(max_length=40)

    codigo=models.IntegerField()


class Cliente(models.Model):

    nombre=models.CharField(max_length=40)

    apellido=models.CharField(max_length=40)

    email = models.EmailField(default='euuge@miranda.com')

    dni=models.IntegerField()



class Empleado(models.Model):

    nombre=models.CharField(max_length=40)

    apellido=models.CharField(max_length=40)

    email=models.EmailField()

    dni=models.IntegerField()

    sector=models.CharField(max_length=100, default='default_sector_value')