from django.db import models
from datetime import datetime

# Create your models here.
class Tutoriallac(models.Model):
    nombre_tutorial_lac = models.CharField(max_length=50)
    descripcion_tutorial_lac = models.CharField(max_length=100)
    contenido_tutorial_lac = models.TextField(default="contenido")
    fecha_cambio_lac = models.DateTimeField("Ultima fecha de modificación", default=datetime.now())

    def __str__(self):
        return self.nombre_tutorial_lac


