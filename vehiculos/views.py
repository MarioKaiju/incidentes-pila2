from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vehiculo

# Create your views here.
class VistaListaVehiculos(ListView):
  model = Vehiculo
  template_name = 'lista_vehiculos.html'
  context_object_name = 'lista_vehiculos'

class VistaDetalleVehiculos(DetailView):
  model = Vehiculo
  template_name = 'detalle_vehiculo.html'
  context_object_name = 'vehiculo'

class VistaAgregarVehiculo(CreateView):
  model = Vehiculo
  template_name = 'nuevo_vehiculo.html'
  fields = ['modelo', 'año', 'marca', 'url_imagen']

class VistaEditarVehiculo(UpdateView):
  model = Vehiculo
  template_name = 'editar_vehiculo.html'
  fields = ['modelo', 'año', 'marca', 'url_imagen']

class VistaEliminarVehiculo(DeleteView):
  model= Vehiculo
  template_name = 'eliminar_vehiculo.html'
  success_url = reverse_lazy('lista_vehiculo')
  context_object_name = 'vehiculo'