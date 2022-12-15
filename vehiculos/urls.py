from django.urls import path
from .views import VistaAgregarVehiculo, VistaDetalleVehiculos, VistaListaVehiculos, VistaEditarVehiculo, VistaEliminarVehiculo

urlpatterns = [
  path('', VistaListaVehiculos.as_view(), name='lista_vehiculos'),
  path('<uuid:pk>/', VistaDetalleVehiculos.as_view(), name='detalle_vehiculo'),
  path('nuevo/', VistaAgregarVehiculo.as_view(), name='nuevo_vehiculo'),
  path('<uuid:pk>/editar/', VistaEditarVehiculo.as_view(), name='editar_vehiculo'),
  path('<uuid:pk>/eliminar/', VistaEliminarVehiculo.as_view(), name='eliminar_vehiculo'),
]