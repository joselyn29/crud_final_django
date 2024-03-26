from django.db import models

# Create your models here.
# creando clase o tabla en la base de datos 'agenda_evento_db'

class evento_tbl (models.Model):
    #  id = models.CharField(max_length=100)
     organizador = models.CharField(max_length=100)
     tipo = models.CharField(max_length=100)
     fecha = models.DateField()
     hora = models.TimeField()
     lugar = models.TextField() 
     presupuesto = models.FloatField(max_length=100)
     cantidad_personas = models.CharField(max_length=100)
       
     def __str__(self):
        return f"{self.nombre} ({self.tipo})"