# Importar librerías
import time
import serial
import decouple
import thingspeak


# Función para realizar la conexión con el puerto serial
def conectar_puerto_serial(puerto, velocidad, tiempo_espera):
    try:
        return serial.Serial(puerto, velocidad, timeout=tiempo_espera)
    except serial.SerialException as error:
        print(f"Error al abrir el puerto serial: {error}")
        return None


# Función para enviar datos a ThingSpeak
def enviar_datos_nube(canal, datos):
    try:
        canal.update({1: datos})
        print("Datos enviados a ThingSpeak:", datos)
    except Exception as error:
        print(f"Error al enviar datos a ThingSpeak: {error}")


# Función principal
if __name__ == "__main__":
    # Configurar las credenciales de ThingSpeak
    ID_CANAL = decouple.config("ID_CANAL")
    API_ESCRITURA = decouple.config("API_ESCRITURA")
    canal_thingspeak = thingspeak.Channel(id=ID_CANAL, api_key=API_ESCRITURA)

    # Configurar el puerto serial
    PUERTO = "/dev/ttyACM0"
    VELOCIDAD = 9600
    TIEMPO_ESPERA = 1
    puerto_serial = conectar_puerto_serial(PUERTO, VELOCIDAD, TIEMPO_ESPERA)

    if puerto_serial:
        try:
            while True:
                datos = puerto_serial.readline().decode().strip()
                print(datos)
                #if datos:
                    #enviar_datos_nube(canal_thingspeak, datos)
                time.sleep(0.5)  # Espera breve para evitar lecturas excesivas
        except KeyboardInterrupt:
            print("Detención del programa por el usuario.")
        finally:
            puerto_serial.close()
    else:
        print("No se pudo establecer la conexión con el puerto serial.")
