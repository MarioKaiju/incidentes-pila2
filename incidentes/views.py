from django.views.generic import ListView
from .models import Incidente

# Create your views here.
class VistaListaIncidentes(ListView):
  model= Incidente
  template_name = 'inicio.html'