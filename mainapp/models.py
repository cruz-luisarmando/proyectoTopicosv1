from django.db import models

# Create your models here.
class Paso(models.Model):
    nombre_paso = models.CharField(max_length=50)
    descripcion_paso =models.TextField()

    def __str__(self):
        return self.nombre_paso
