import socket

PORT = 9088
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5


def process_client(clientsocket):
    condition = True
    while condition:
        msg_cliente =  clientsocket.recv(2048).decode("utf-8")
        print("El cliente dice:", msg_cliente)
        if msg_cliente.lower() == 'salir':
            break
        msg_servidor = input('Escribe tu mensaje:')
        send_servidor = str.encode(msg_servidor)
        if msg_servidor.lower() == 'salir':
            condition = False
        clientsocket.send(send_servidor)
    clientsocket.close()



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
