import threading
import socket

host = '127.0.0.1'
port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
pseudos = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            pseudo =  pseudos[index]
            broadcast(f"{pseudo} s'est déconnecté".encode('utf-8'))
            pseudos.remove(pseudo)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connecté a {str(address)}")

        client.send('NAME'.encode('utf-8'))
        pseudo = client.recv(1024).decode('utf-8')
        clients.append(client)

        print(f"Le nom du client est : {pseudo} !")
        broadcast(f"{pseudo} a rejoint le salon !".encode('utf-8'))
        client.send("Connecté au server !".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

#print("Le serveur est sur écoute... Patientez un moment")
#receive()