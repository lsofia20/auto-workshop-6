// Librerias necesarias
#include <Wire.h>

// Constantes
const int CANAL_COMUNICACION = 8;
const int CANTIDAD_BYTES = 7;
const int PIN_LED = 13;
const int TIEMPO_ESPERA = 1000;
const int LIMITE_TEMPERATURA = 30;

// Función de inicialización
void setup() {
  Serial.begin(9600);
  pinMode(PIN_LED, OUTPUT); 
  Wire.begin(CANAL_COMUNICACION);
}

// Función principal
void loop() {
  // Solicitar los datos al dispositivo esclavo
  Wire.requestFrom(CANAL_COMUNICACION, CANTIDAD_BYTES);

  // Recolectar los datos recibidos
  String temperatura = "";
  while (Wire.available()) {
    char byte = Wire.read();
    temperatura += byte;
  }
  
  // Comprobar si la temperatura es alta
  if (temperatura.toInt() > LIMITE_TEMPERATURA) {
    digitalWrite(PIN_LED , HIGH);
  } else {
    digitalWrite(PIN_LED , LOW);
  }

  // Enviar los datos al puerto serial
  Serial.println(temperatura);
  delay(TIEMPO_ESPERA);
}
