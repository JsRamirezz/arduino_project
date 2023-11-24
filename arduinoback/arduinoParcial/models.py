from django.db import models

class Sensor(models.Model):
    tiempo = models.DateTimeField()
    valor_sensor = models.IntegerField()


