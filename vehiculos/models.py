from django.contrib import admin
from django.contrib.auth.models import User

# Método para convertir variables en columnas y agregarles especificaciones de una.
from django.db import models

# Establezco las columnas de la base de datos que contendrá el modelo.
class Marca(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Anio(models.Model):
    # Columna para agregar digitos numéricos.
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Combustible(models.Model):
    # Columna para agregar digitos numéricos.
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pais(models.Model):
    # Columna para agregar digitos numéricos.
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Auto(models.Model):
    name = models.CharField(max_length=120)

    mark = models.ForeignKey(
        # Vincula la columna con el modelo de Marcas de Autos.
        Marca,
        on_delete=models.SET_NULL,
        related_name='marcas',
        # Habilita que la columna pueda ser nula.
        null=True,        
    )

    # Se declara que la columna es de caracter numérico.
    price = models.DecimalField(
        # Especifica que el número no puede tener más de diez dígitos.
        max_digits=10,
        decimal_places=2,
    )

    year = models.ForeignKey(
        Anio,
        on_delete=models.SET_NULL,
        related_name='anios',
        null=True,
    )

    fuel = models.ForeignKey(
        Combustible,
        on_delete=models.SET_NULL,
        related_name='combustibles',
        null=True,
    )

    country = models.ForeignKey(
        Pais,
        on_delete=models.SET_NULL,
        related_name='paises',
        null=True,
    )

    def __str__(self):
        return self.name

