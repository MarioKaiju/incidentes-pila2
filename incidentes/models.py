from django.urls import reverse
from django.db import models

# Create your models here.
class Incidente(models.Model):
  ASEGURAMIENTO = (
        ('PT', 'Perdida total'),
        ('DC', 'Daños colaterales'),
        ('DP', 'Daños parciales'),
    )
  id_vehiculo = models.BigAutoField(primary_key=True)
  matricula = models.CharField(max_length=10, unique=True)
  modelo = models.TextField()
  propietario = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE
  )
  aseguramiento = models.CharField(max_length=2, choices=ASEGURAMIENTO)

  def __str__(self):
    return self.modelo + self.propietario

  def get_absolute_url(self):
    return reverse('detalle_incidente', args=[str(self.id_vehiculo)])
