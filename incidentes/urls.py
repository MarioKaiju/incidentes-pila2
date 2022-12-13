from django.urls import path
from .views import VistaListaIncidentes, VistaDetalleIncidente, VistaCrearIncidente, VistaEditarIncidente, VistaEliminarIncidente

urlpatterns = [
  path('', VistaListaIncidentes.as_view(), name='inicio'),
  path('inc/<uuid:pk>/', VistaDetalleIncidente.as_view(), name='detalle_incidente'),
  path('inc/nuevo/', VistaCrearIncidente.as_view(), name='nuevo_incidente'),
  path('inc/<uuid:pk>/editar/', VistaEditarIncidente.as_view(), name='editar_incidente'),
  path('inc/<uuid:pk>/eliminar/', VistaEliminarIncidente.as_view(), name='eliminar_incidente'),
]