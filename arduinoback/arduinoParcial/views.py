from django.shortcuts import render
from .models import Sensor

def lecturas(request):
    lecturas = Sensor.objects.all()
    return render(request, 'lecturas_sensor.html', {'lecturas': lecturas})

