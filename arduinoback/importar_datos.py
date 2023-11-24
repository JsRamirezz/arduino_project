import pandas as pd
import os   

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arduinoback.settings")

import django
django.setup()

from arduinoParcial.models import Sensor

# Ruta al archivo CSV
archivo_csv = 'datos_sensor.csv'

# Cargar datos desde el CSV a un DataFrame
df = pd.read_csv(archivo_csv)

# Iterar sobre las filas del DataFrame e insertar en MongoDB
for _, row in df.iterrows():
    Sensor.objects.create(tiempo=row['Tiempo'], valor_sensor=row['Valor del Sensor (ppm)'])



