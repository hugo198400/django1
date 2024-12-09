from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Area(models.Model):
    des_aaa = models.CharField(max_length=255)

    def __str__(self):
        return self.des_aaa

class Ala(models.Model):
    ala = models.CharField(max_length=255)
    id_aaa = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.ala

class Punto(models.Model):
    cod = models.CharField(max_length=255)
    id_aaa = models.ForeignKey(Area, on_delete=models.CASCADE)
    id_ala = models.ForeignKey(Ala, on_delete=models.CASCADE)
    sector = models.CharField(max_length=50, default='por definir')
    meta_km= models.FloatField(default=0.0)
    meta_vol= models.FloatField(default=0.0)
    avance_km = models.FloatField(default=0.0)
    avance_vol = models.FloatField(default=0.0)
    estado = models.CharField(max_length=50, choices=[('Culminado', 'Culminado'), ('Ejecución', 'Ejecución'), ('Programado', 'Programado')], default='Programado')

    def __str__(self):
        return self.cod

class RegAvance(models.Model):
    fecha = models.DateField(auto_now_add=True)
    id_punto = models.ForeignKey(Punto, on_delete=models.CASCADE)
    avance_km = models.FloatField(default=0.0)
    avance_vol = models.FloatField(default=0.0)
    estado = models.CharField(max_length=50, choices=[('Culminado', 'Culminado'), ('Ejecución', 'Ejecución'), ('Programado', 'Programado')], default='Programado')

    def __str__(self):
        return f'{self.id_punto} - {self.fecha}'


class CustomUser(AbstractUser):
    ala = models.ForeignKey(Ala, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.username


