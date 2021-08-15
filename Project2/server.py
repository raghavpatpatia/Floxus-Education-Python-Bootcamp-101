import socket
import threading

# creating host and port
PORT = 51000
HOST = socket.gethostbyname(socket.gethostname())

ADDRESS = (HOST, PORT)

FORMAT = "utf-8"

clients = []
names = []

# create a new socket for the server where AF_INET is the type of address(will return IPv4) and Sock_STREAM is TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDRESS)


def startchat():
    print("Server is working on", HOST)

    server.listen()

    while True:
        connection, addr = server.accept()
        connection.send("NAME".encode(FORMAT))

        name = connection.recv(1050).decode(FORMAT)

        names.append(name)

        clients.append(connection)

        print(f"Name is: {name}")
        print(f"Client is: {connection}")

        broadcastMessage(f"{name} has joined chat room".encode(FORMAT))

        connection.send("Connection successful".encode(FORMAT))

        thread = threading.Thread(target=receive, args=(connection, addr))

        thread.start()

        print(f"active connections {threading.activeCount() - 1}")


def receive(connection, addr):
    print(f"New Connection {addr}")

    connected = True

    while connected:
        message = connection.recv(1050)

        broadcastMessage(message)

    connection.close()


def broadcastMessage(message):
    for client in clients:
        client.send(message)


startchat()
