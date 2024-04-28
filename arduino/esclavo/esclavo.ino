// Librerias necesarias
#include <Wire.h>

// Constantes
const int CANAL_COMUNICACION = 8;
const int CANTIDAD_DECIMALES = 2;
const int CANTIDAD_BYTES = 7;
const int PIN_SENSOR = A0;
const int TIEMPO_ESPERA = 1000;
const int MAX_VOLTAJE = 5;
const int MAX_ANALOGICO = 1023;
const int VALOR_AJUSTE = 100;

// Variables
char valor_bytes[CANTIDAD_BYTES];

// Función de inicialización
void setup() {
  // Inicializar la comunicación I2C
  Wire.begin(CANAL_COMUNICACION);
  Wire.onRequest(enviar_datos);
  
  // Inicializar el puerto serial para mensajes de depuración
  Serial.begin(9600);
  Serial.println("Iniciando envío de datos...");
}

// Función para manejar cuando se solicitan datos
void enviar_datos() {
  // Leer el valor del sensor analógico y convertirlo a temperatura
  int valor_analogico = analogRead(PIN_SENSOR);
  float temperatura = (valor_analogico * MAX_VOLTAJE * VALOR_AJUSTE) / MAX_ANALOGICO;
    
  // Mostrar los datos enviados en el puerto serial
  Serial.println("Datos enviados: " + String(temperatura));
  
  // Convertir la temperatura a formato de bytes y enviarla por I2C
  dtostrf(temperatura, CANTIDAD_BYTES, CANTIDAD_DECIMALES, valor_bytes);
  Wire.write(valor_bytes);
}

// Función para manejar el bucle principal
void loop() {
  delay(TIEMPO_ESPERA);
}
