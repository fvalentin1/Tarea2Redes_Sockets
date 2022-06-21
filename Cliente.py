import socket

#Bandera que establece el estado del menú
menu = True

#Ciclo while para el menú
while menu:

    #Enunciado del menú
    print("Programa de recepción de datos de sensor")
    print("Seleccione la cantidad de datos a recibir:")

    #Se recibe la entrada del menú
    opcion = input("Opción: ")

    #Se intenta recibir un entero mayor a cero, en caso contrario se realizará la excepción correspondiente
    try:

        #Como la entrada es un String, se convierte a Entero
        opcion = int(opcion)

        #Control de error si el valor es un Entero, pero menor o igual a 0
        if (opcion<=0):
            print ("Ingrese una cantidad entera mayor a 0")
        else:
            #Si es mayor a 0, se realiza la operación

            #Define mi_socket (Cliente)
            mi_socket = socket.socket()

            #Conectar al socket del servidor
            mi_socket.connect(('192.168.100.47', 37430))

            #Se envía mensaje al Servidor
            msje = "Hola Servidor, desde el cliente"
            mi_socket.send(msje.encode("ascii"))

            #Se recibe mensaje del servidor
            respuesta = mi_socket.recv(1024)
            txt = respuesta.decode("ascii")
            print (txt)

            #Se transforma el valor Entero a String, para enviarlo a través del socket
            cantidad = str(opcion)

            #Se envía el valor al Servidor
            mi_socket.send(cantidad.encode("ascii"))

            #Ciclo for para reciir los datos desde el Servidor, e imprimirlos aquí en el Cliente
            for i in range(opcion):
                datos = mi_socket.recv(1024)
                aux = datos.decode("ascii")
                print (aux)
                print ()
                
                #Cuando se recibe la totalidad de los datos, se notifica al Cliente el recibo exitoso de estos
                if((i+1)==opcion):
                    print("Recibo exitoso")

            #Solicitud de desconexion del socket
            mi_socket.close()

            #Como el recibo de datos ya fue realizado, el menú se desactiva
            menu = False
    except:
        #Control de error en caso de ingresar un String, o algún valor no válido como un flotante, o un simbolo.
        print()
        print("Ocurrió un error, por favor reintente")
        print()
        print("-----------------")
