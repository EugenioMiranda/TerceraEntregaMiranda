from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre=models.CharField(max_length=40)

    marca=models.CharField(max_length=40)

    codigo=models.IntegerField()

    def __str__(self):
        return f'{self.nombre}  {self.marca}  {self.codigo}'

class Cliente(models.Model):

    nombre=models.CharField(max_length=40)

    apellido=models.CharField(max_length=40)

    email = models.EmailField()

    dni=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}  {self.apellido}'



class Empleado(models.Model):

    nombre=models.CharField(max_length=40)

    apellido=models.CharField(max_length=40)

    email = models.EmailField(unique=True)

    dni = models.IntegerField()

    sector=models.CharField(max_length=100, default='default_sector_value')

    def __str__(self):
        return f'{self.nombre}  {self.apellido}'