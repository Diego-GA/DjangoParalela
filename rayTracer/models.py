from django.db import models

# Create your models here.
class RayTracerData(models.Model):
    numero_hilos = models.CharField(max_length=50)
    numerador_proporcion = models.CharField(max_length=50)
    denominador_proporcion = models.CharField(max_length=50)
    ancho_imagen = models.CharField(max_length=50)
    muestras_por_pixel = models.CharField(max_length=50)
    numerador_max_rayos = models.CharField(max_length=50)
    coordenada_x = models.CharField(max_length=50)
    coordenada_y = models.CharField(max_length=50)
    coordenada_z = models.CharField(max_length=50)
    valor_R_esfera1 = models.CharField(max_length=50)
    valor_G_esfera1 = models.CharField(max_length=50)
    valor_B_esfera1 = models.CharField(max_length=50)
    valor_R_esfera2 = models.CharField(max_length=50)
    valor_G_esfera2 = models.CharField(max_length=50)
    valor_B_esfera2 = models.CharField(max_length=50)
    indice_refraccion = models.CharField(max_length=50)

    def __str__(self):
        return f"RayTracerData {self.id}"
