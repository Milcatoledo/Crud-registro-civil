from django.db import models

class genero(models.TextChoices):
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'

class Registro_civil(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=genero.choices)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"