#cloud_journey/src/pets/views.py
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from pets.models import Pets


class PetsListView(ListView):
    model = Pets
