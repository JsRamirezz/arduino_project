import serial
import csv
import time

puerto_serial = 'COM3'
bauds = 9600

archivo_csv = 'datos_sensor.csv'

with serial.Serial(puerto_serial, bauds, timeout=1) as ser, open(archivo_csv, 'w', newline='') as archivo_csv:
    # Configurar el escritor CSV
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Tiempo', 'Valor del Sensor (ppm)'])

    while True:
        try:
            # Leer valor del puerto serial
            lectura_serial = ser.readline().decode('utf-8').strip()

            # Buscar la posición del primer dígito en la cadena
            inicio_valor = next((i for i, c in enumerate(lectura_serial) if c.isdigit()), None)

            # Extraer la parte numérica de la cadena
            valor_sensor_str = lectura_serial[inicio_valor:]

            # Verificar si la cadena no está vacía y el valor supera los 300 ppm antes de convertirla
            if valor_sensor_str and int(valor_sensor_str) > 300:
                # Convertir el valor a entero
                valor_sensor_int = int(valor_sensor_str)
                tiempo_actual = time.strftime("%Y-%m-%d %H:%M:%S")

                # Escribir en el archivo CSV
                escritor_csv.writerow([tiempo_actual, valor_sensor_int])
                print(f'Tiempo: {tiempo_actual}, Valor del Sensor: {valor_sensor_int} ppm')

            # Pausa de 1 segundo entre lecturas
            time.sleep(1)

        except KeyboardInterrupt:
            print("Programa interrumpido.")
            break