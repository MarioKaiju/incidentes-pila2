from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Incidente

# Create your views here.
class VistaListaIncidentes(ListView):
  model = Incidente
  template_name = 'inicio.html'
  context_object_name = 'lista_incidentes'

class VistaDetalleIncidente(DetailView):
  model = Incidente
  template_name = 'detalle_incidente.html'
  context_object_name = 'incidente'


class VistaCrearIncidente(CreateView):
  model = Incidente
  template_name = 'nuevo_incidente.html'
  fields = ['modelo', 'matricula', 'propietario', 'aseguramiento']

class VistaEditarIncidente(UpdateView):
  model = Incidente
  template_name = 'editar_incidente.html'
  fields = ['modelo', 'matricula', 'aseguramiento']

class VistaEliminarIncidente(DeleteView):
  model= Incidente
  template_name = 'eliminar_incidente.html'
  success_url = reverse_lazy('inicio')
  context_object_name = 'incidente'