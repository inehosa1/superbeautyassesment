from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipment(models.Model):
    """
    Modelo para equipo
    """
    reference = models.CharField("Referencia", max_length=50)
    brand = models.CharField("Marca", max_length=50)
    processor = models.CharField("Procesador", max_length=50)
    memory = models.CharField("Memoria", max_length=50)
    disk = models.CharField("Disco", max_length=50)
    type = models.CharField("Tipo", max_length=50)
    
    class Meta:	
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    
class UserEquipment(models.Model):
    """
    Modelo para asignar equipo al usuario
    """
    date_assignment = models.DateTimeField("Fecha de asignación", max_length=50)
    date_delivery  = models.DateTimeField("Fecha de entrega", max_length=50)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    equipment =  models.ForeignKey(Equipment, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Equipo asignado a usuario'
        verbose_name_plural = 'Equipos asignados a usuarios'