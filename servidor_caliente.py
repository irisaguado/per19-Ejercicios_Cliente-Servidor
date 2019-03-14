import socket
from random import randint

IP ='127.0.0.1'
PORT = 8097
max_conection = 2

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def caliente(n_r,num):
    if num == n_r:
        msg = 'FELICIDADES!!'
    elif (n_r - 10) <= num <= (n_r + 10):
        msg = 'caliente, caliente!'
    elif num > (n_r + 10):
        msg = 'frio, frio por arriba'
    elif num < (n_r - 10):
        msg = 'frio, frio por debajo'

    return msg



try:
    servidor.bind((IP,PORT))
    servidor.listen(max_conection)
    while True:
        print()
        print("Esperando Conexiones en {} {}".format(IP,PORT))
        (cliente, address) = servidor.accept()
        n_r = randint(0,99)
        print('Número generado aleatoriamente:',n_r)
        continua = True
        while continua:
            num = int(cliente.recv(1000).decode("utf-8"))
            mensaje = caliente(n_r,num)
            if mensaje == 'FELICIDADES!!':
                continua = False
            mensaje = str.encode(mensaje)
            cliente.send(mensaje)
        cliente.close()


except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
