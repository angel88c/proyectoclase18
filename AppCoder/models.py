from django.db import models

# Create your models here.
# Le estoy diciendo que Curso es un Modelo

#Este objeto, la orm lo va a cobnvertir en una tabla
class Curso(models.Model):    
    nombre   = models.CharField(max_length = 50)
    comision = models.IntegerField()
    

class Estudiante(models.Model):
    nombre   = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email    = models.EmailField()
    
class Profesor(models.Model):
    nombre    = models.CharField(max_length = 50)
    apellido  = models.CharField(max_length = 50)
    email     = models.EmailField()
    profesion = models.CharField(max_length = 50)
    
class Entregable(models.Model):
    nombre        = models.CharField(max_length = 50)
    fecha_entrega = models.DateField()
    entregadi     = models.BooleanField()


