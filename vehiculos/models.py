from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class UUIDModel(models.Model):
  id_vehiculo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Vehiculo(UUIDModel):
  modelo = models.TextField(primary_key=True, unique=True)
  año = models.IntegerField(default=1990)
  marca = models.TextField(default="")
  url_imagen = models.TextField(default="")

  def __str__(self):
    return str(self.modelo) + " " +  str(self.año)

#  def get_absolute_url(self):
#   return reverse('detalle_vehiculo', args=[str(self.id_vehiculo)])