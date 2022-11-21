from django.db import models

class Prediccion(models.Model):
    id = models.AutoField(primary_key=True)
    alpha = models.DecimalField(max_digits=30, decimal_places=23)
    delta = models.DecimalField(max_digits=30, decimal_places=23)
    u = models.DecimalField(max_digits=30, decimal_places=23)
    g = models.DecimalField(max_digits=30, decimal_places=23)
    r = models.DecimalField(max_digits=30, decimal_places=23)
    i = models.DecimalField(max_digits=30, decimal_places=23)
    z = models.DecimalField(max_digits=30, decimal_places=23)
    redshift = models.DecimalField(max_digits=30, decimal_places=23)
    fecha_creacion = models.DateField(default=None, blank=True, null=True)
    galaxy = models.DecimalField(max_digits=30, decimal_places=23, default=None, blank=True, null=True)
    qso = models.DecimalField(max_digits=30, decimal_places=23, default=None, blank=True, null=True)
    star = models.DecimalField(max_digits=30, decimal_places=23, default=None, blank=True, null=True)
    valor_real = models.CharField(max_length=20, default=None, blank=True, null=True)
    fecha_actualizacion = models.DateField(default=None, blank=True, null=True)
	