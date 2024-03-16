import socket
import requests
import threading
import yaml
import pickle

config: dict = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)  # Load the config file into a dictionary


def clients(clientSocket: socket, clientAddr: str) -> None:
    myConnections: list = []
    tServers: dict = requests.get(f"http://{config['URL_HOST']}:{config['PORT']}/tanketteapi/servers").json()
    for server in tServers:
        if clientAddr in tServers[server]["players"]:
            myConnections.append(server)

    while True:
        data: list = pickle.loads(clientSocket.recv(1024))  # [


# Create a new socket with the given urlHost and port
def mySocket(urlHost: str, port: int) -> None:
    s: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((urlHost, port))
    s.listen(5)

    while True:
        c, addr = s.accept()
        # Do something with the connection
        c.close()
