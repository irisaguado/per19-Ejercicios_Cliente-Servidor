import socket
IP ='127.0.0.1'
PORT = 8097
max_conection = 5
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def suma(num_1,num_2):
    resultado = num_1 + num_2
    return resultado

def multiplicacion(num_1, num_2):
    resultado = num_1 * num_2
    return resultado

def resta(num_1,num_2):
    resultado = num_1 - num_2
    return resultado

def division(num_1,num_2):
    try:
        resultado = num_1 / num_2
        return resultado
    except ZeroDivisionError:
        resultado = 'No se puede dividir por cero'
        return resultado

try:
    servidor.bind((IP,PORT))
    servidor.listen(max_conection)
    while True:
        print()
        print("Esperando Conexiones en {} {}".format(IP,PORT))
        (cliente, address) = servidor.accept()
        continua = True
        while continua:
            menu_opcion = int(cliente.recv(100).decode('utf-8'))
            if menu_opcion == 0:
                cliente.close()
                break
            num_1 = int(cliente.recv(100).decode('utf-8'))
            num_2 = int(cliente.recv(100).decode('utf-8'))
            if menu_opcion == 1:
                suma1 = suma(num_1, num_2)
                suma1 = str(suma1)
                suma1 = str.encode(suma1)
                cliente.send(suma1)
            elif menu_opcion == 2:
                mult1 = multiplicacion(num_1, num_2)
                mult1 = str(mult1)
                mult1 = str.encode(mult1)
                cliente.send(mult1)
            elif menu_opcion == 3:
                resta1 = resta(num_1, num_2)
                resta1 = str(resta1)
                resta1 = str.encode(resta1)
                cliente.send(resta1)
            elif menu_opcion == 4:
                division1 = division(num_1, num_2)
                division1 = str(division1)
                division1 = str.encode(division1)
                cliente.send(division1)



except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
