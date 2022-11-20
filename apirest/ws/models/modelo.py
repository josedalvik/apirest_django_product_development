from django.db import models

class Prediccion(models.Model):
    alpha = models.DecimalField(max_digits=30, decimal_places=23)
    delta = models.DecimalField(max_digits=30, decimal_places=23)
    u = models.DecimalField(max_digits=30, decimal_places=23)
    g = models.DecimalField(max_digits=30, decimal_places=23)
    r = models.DecimalField(max_digits=30, decimal_places=23)
    i = models.DecimalField(max_digits=30, decimal_places=23)
    z = models.DecimalField(max_digits=30, decimal_places=23)
    redshift = models.DecimalField(max_digits=30, decimal_places=23)
    fecha_creacion = models.DateField()
    galaxy = models.DecimalField(max_digits=4, decimal_places=3)
    qso = models.DecimalField(max_digits=4, decimal_places=3)
    star = models.DecimalField(max_digits=4, decimal_places=3)
    valor_real = models.CharField()
    fecha_actualizacion = models.DateField()
	