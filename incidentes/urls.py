from django.urls import path
from .views import VistaListaIncidentes

urlpatterns = [
  path('', VistaListaIncidentes.as_view(), name='inicio')
]