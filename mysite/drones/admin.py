from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Drone, Zone, Simulation

admin.site.register(Drone)
admin.site.register(Zone)
admin.site.register(Simulation)