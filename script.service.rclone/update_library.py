import os
import time

# Define la ruta de la fuente de datos
data_source_path = "dav://127.0.0.1:23457/Gcryptlaura"

# Define el intervalo de tiempo en segundos en el que se comprobará si hay nuevo contenido
check_interval = 600 # 10 minutos

# Obtiene el tiempo de la última modificación de la fuente de datos
last_update_time = os.path.getmtime(data_source_path)

while True:
    # Obtiene el tiempo de la última modificación de la fuente de datos
    current_update_time = os.path.getmtime(data_source_path)

    # Si el tiempo de la última modificación es diferente al tiempo guardado
    if current_update_time != last_update_time:
        # Actualiza la biblioteca de KODI
        os.system("xbmc-send -a 'UpdateLibrary(video)'")
        # Guarda el nuevo tiempo de última modificación
        last_update_time = current_update_time

    # Duerme el script por el intervalo de tiempo definido
    time.sleep(check_interval)

