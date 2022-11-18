from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here
class VistaRegistro(CreateView):
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
  form_class = UserCreationForm