from django.contrib import admin
from .models import sensor
from .models import Dispositivo
# Register your models here.
admin.site.register(sensor)
admin.site.register(Dispositivo)

