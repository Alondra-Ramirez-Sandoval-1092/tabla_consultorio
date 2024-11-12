from django.db import models

# Create your models here.
class Consultorio(models.Model):
    id_consult=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    doctor=models.CharField(max_length=40)
    especialidad=models.CharField(max_length=30)
    horario=models.CharField(max_length=12)
    cita=models.CharField(max_length=40)

    def __str__(self) :
        return self.nombre