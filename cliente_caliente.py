import socket
IP ='127.0.0.1'
PORT = 8097

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def caliente():
    num = input('Introduce un número:')
    num = str.encode(num)
    return num

try:
    cliente.connect((IP,PORT))
    continua = True
    while continua:
        num = caliente()
        cliente.send(num)
        resp_serv = cliente.recv(1000).decode('utf-8')
        print(resp_serv)
        if resp_serv == 'FELICIDADES!!':
            break
    cliente.close()

except OSError:
    print("Socket already used")
    cliente.close()
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((IP, PORT))
