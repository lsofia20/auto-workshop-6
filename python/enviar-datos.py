# Importar las bibliotecas necesarias
import serial
import decouple
import thingspeak

# Configuración de las credenciales de ThingSpeak
ID_CANAL = decouple.config("ID_CANAL")
API_ESCRITURA = decouple.config("API_ESCRITURA")

# Configuración del puerto serial
PUERTO = "/dev/ttyACM0"
VELOCIDAD = 9600
TIMEOUT = 1

# Iniciar el programa
try:
    # Inicializar la comunicación serial y con la API
    puerto_serial = serial.Serial(PUERTO, VELOCIDAD, timeout=TIMEOUT)
    canal_thingspeak = thingspeak.Channel(id=ID_CANAL, api_key=API_ESCRITURA)
    while True:
        # Leer los datos del puerto serial
        datos = puerto_serial.readline().decode().strip()

        # Verificar si se recibieron datos válidos
        if datos:
            # Enviar los datos al canal de ThingSpeak
            canal_thingspeak.update({1: datos})
            print("Datos enviados a ThingSpeak:", datos)
except KeyboardInterrupt:
    # Manejar la finalizacion del programa
    print("Programa interrumpido por el usuario.")
except Exception as error:
    # Manejar cualquier otro error que ocurra durante la ejecución
    print(f"Se produjo un error: {error}.")
finally:
    # Cerrar la conexión con el puerto serial
    puerto_serial.close()
