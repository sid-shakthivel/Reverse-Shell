import socket
import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT"))
SERVER = os.getenv("SERVER_IP")
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

server.listen()

connection, addr = server.accept()

while True:
    command = input("COMMAND: ")
    connection.send(command.encode())
    if command == "exit":
        break
    output = connection.recv(1024).decode()
    print(output)

connection.close()

server.close()
