# Register your models here.
#cloud_journey/src/pets/admin.py
from django.contrib import admin
from pets.models import Pets

admin.site.register(Pets)