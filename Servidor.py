import socket
import time
import Adafruit_DHT

#Referencia a la librería del sensor
SENSOR_DHT = Adafruit_DHT.DHT22
#Pin GPIO para recibir los datos
PIN_DHT = 4

#Define mi_socket (Servidor)
mi_socket = socket.socket()

#Define funcion BIND, estableciendo IP, Puerto y Protocolo (TCP)
mi_socket.bind( ('192.168.100.47', 37430) )

#El socket escuchará hasta 5 solicitudes en simultaneo,
#de alcanzar este límite deberia rechazar la sexta solicitud, o ponerla en espera
mi_socket.listen(5)

#Se establece la conexión, y se obtiene la dirección del cliente que se ha conectado
conexion, addr = mi_socket.accept()
print ("Nueva conexion establecida!")
print (addr)

#Se recibe un mensaje desde el cliente
peticion = conexion.recv(1024)
txt = peticion.decode("ascii")
print (txt)

#Se envía un mensaje al cliente
msje = "Hola, te saludo desde el servidor!"
conexion.send(msje.encode("ascii"))

#Se recibe un valor desde el cliente en formato de String
aux = conexion.recv(1024)
opcion = aux.decode("ascii")

#Se realiza la transformación del String a Entero
#El control de errores se realiza en el cliente, este valor siempre será un Entero en forma de String
opcion = int(opcion)

#Ciclo for para obtener la cantidad de datos solicitados
for i in range(opcion):

    #Se realiza la medición de los parametros
    humedad, temperatura = Adafruit_DHT.read(SENSOR_DHT, PIN_DHT)

    #Se le da formato a los datos para enviarlos
    #La lectura puede ser correcta o incorrecta, debido a que el sensor es sensible a otras cosas como la estática
    #o la presencia de polvo, entre otras cosas
    if humedad is not None and temperatura is not None:
        temp = ("Temp={0:0.1f}C Hum={1:0.1f}%".format(temperatura, humedad))
    else:
        temp = "Error en la lectura"
    
    #Se imprime que dato se está enviando actualmente
    print("Enviando dato "+str(i+1)+" de "+str(opcion))

    #Se envia el mensaje correspondiente
    conexion.send(temp.encode("ascii"))

    #Se esperan 3 segundos para realizar la próxima medición
    time.sleep(3)

    #Cuando se envía la totalidad de los datos, se notifica en el servidor,
    #la totalidad de los datos enviados hacia el cliente
    if((i+1)==opcion): print("Envío exitoso")

#Solicitud de desconexión del socket
mi_socket.close()
