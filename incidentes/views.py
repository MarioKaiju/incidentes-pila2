from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Incidente

# Create your views here.
class VistaListaIncidentes(ListView):
  model = Incidente
  template_name = 'inicio.html'
  context_object_name = 'lista_incidentes'
  def get_queryset(self):
    queryset = super().get_queryset()
    if self.request.user.is_superuser:
      return queryset
    if self.request.user.is_authenticated:
      return queryset.filter(propietario=self.request.user)
    else:
      return queryset

class VistaDetalleIncidente(DetailView):
  model = Incidente
  template_name = 'detalle_incidente.html'
  context_object_name = 'incidente'

class VistaCrearIncidente(CreateView):
  model = Incidente
  template_name = 'nuevo_incidente.html'
  fields = ['modelo', 'aseguramiento', 'matricula', 'fecha', 'descripcion']
  def form_valid(self, form):
    form.instance.propietario = self.request.user
    print(settings.EMAIL_HOST_USER)
    send_mail(
      'Nuevo incidente',
      'Ha recibido un nuevo incidente, por favor verifique la página',
      settings.EMAIL_HOST_USER,
      ['marioavazquez2011@hotmail.com'],
      fail_silently=False
    )
    self.form_valid
    return super().form_valid(form)

class VistaEditarIncidente(UpdateView):
  model = Incidente
  template_name = 'editar_incidente.html'
  fields = ['modelo', 'matricula', 'aseguramiento']

class VistaEliminarIncidente(DeleteView):
  model= Incidente
  template_name = 'eliminar_incidente.html'
  success_url = reverse_lazy('inicio')
  context_object_name = 'incidente'

class VistaComentarIncidente(UpdateView):
  model = Incidente
  template_name = 'comentar_incidente.html'
  fields = ['comentarios']