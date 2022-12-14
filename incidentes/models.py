from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.
class UUIDModel(models.Model):
  id_incidente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Incidente(UUIDModel):
  ASEGURAMIENTO = (
        ('PT', 'Perdida total'),
        ('DC', 'Daños colaterales'),
        ('DP', 'Daños parciales'),
    )
  matricula = models.CharField(max_length=10, unique=False)
  fecha = models.DateField()
  descripcion = models.TextField(blank=True, default="")
  modelo = models.ForeignKey(
    'vehiculos.Vehiculo',
    on_delete=models.CASCADE
  )
  propietario = models.ForeignKey(
    User,
    on_delete=models.CASCADE
  )
  aseguramiento = models.CharField(max_length=2, choices=ASEGURAMIENTO)
  comentarios = models.TextField(default="", blank=True)

  def __str__(self):
    return str(self.matricula) + " " +  str(self.modelo) + " - " + str(self.propietario)

  def get_absolute_url(self):
    return reverse('detalle_incidente', args=[str(self.id_incidente)])
