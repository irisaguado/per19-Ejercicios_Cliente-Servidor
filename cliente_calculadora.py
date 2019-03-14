import socket
IP ='127.0.0.1'
PORT = 8097

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def menu():
    menu = '''Bienvenido a calculadora:
    Pulsar:
    0. Salir
    1. Sumar
    2. Multiplicar
    3.Restar
    4.Dividir
    '''
    print(menu)
    eleccion = input('¿Qué desea hacer?:')
    return eleccion

def num_1():
    num_1 = input('Primer número:')
    num_1 = str.encode(num_1)
    return num_1
def num_2():
    num_2 = input('Segundo número:')
    num_2 = str.encode(num_2)
    return num_2

try:
    cliente.connect((IP,PORT))
    while True:
        menu1 = menu()
        if menu1 == '0':
            print('Adios!')
            menu1 = str.encode(menu1)
            cliente.send(menu1)
            cliente.close()
            break
        menu1 = str.encode(menu1)
        cliente.send(menu1)
        numero_1 = num_1()
        cliente.send(numero_1)
        numero_2 = num_2()
        cliente.send(numero_2)
        result = cliente.recv(1000).decode('utf-8')
        print('El resultado es:',result)


except OSError:
    print("Socket already used")
    cliente.close()
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((IP, PORT))
