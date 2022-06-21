# Tarea 2 - Redes de Computadores

## Descripción Informe

***Universidad Católica de la Santísima Concepción***

***Curso:*** Redes de Computadores

***Código:*** IN1082C

***Profesor:*** Yasmany Prieto H.

***Nombre:*** Felipe Valentín M.


## Descripción Tarea
Desarrollo de aplicación Cliente-Servidor mediante el uso de Sockets de Berkeley




## ¿En que consiste la aplicación?
Consiste en recibir datos desde una Raspberry Pi (3B+) en la cual se encuentra conectado un Sensor de Temperatura y Humedad (DHT22) de forma directa en su puerto GPIO (General Purpose Input/Output, Entrada/Salida de Propósito General). Estos datos son comunicados a través de una conexión por Socket TCP/IP con un dispositivo y aplicación Cliente.

## Elección de Socket
Se elige un socket TCP/IP por razones de carácter teórico y personal, comenzando en que TCP a diferencia de UDP, es un protocolo orientado a la conexión, que nos proporciona un mejor manejo de errores, y nos garantiza la entrega de los datos. A pesar de que UDP es no orientado a la conexión, parece ser más rápido que TCP, ya que este está continuamente enviando datos, sin verificar si llegaron a destino. Ahora la razón personal es que anteriormente había trabajado con Sockets TCP en un curso anterior (en lenguaje Python), a lo cual ya sabía cómo funcionaba la librería que permite el funcionamiento de estos.
