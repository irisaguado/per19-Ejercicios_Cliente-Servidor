import socket

IP = "127.0.0.1"
PORT = 9088

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.connect((IP, PORT))
except OSError:
    print("Socket already used")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

condition = True
while condition:
    ms_client = input('Escriba su mensaje:')
    send_cliente = str.encode(ms_client)
    s.send(send_cliente)
    if ms_client.lower() == 'salir':
        break
    msg_servidor = s.recv(2048).decode("utf-8")
    if msg_servidor.lower() == 'salir':
        condition = False
    print("El servidor dice:", msg_servidor)

s.close()
