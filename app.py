from flask import Flask
from flask import request
import threading
import yaml

import socketApp

app: Flask = Flask("TanketteAPI")  # Flask app instance

tServers: dict = {}  # {code: {players: {ipPlayer1: {posX: 0, posY: 0, direction: None, timeSinceLastMessage: 0, bullets: []}, ipPlayer2: {posX: 0, posY: 0, direction: None, timeSinceLastMessage: 0, bullets: []}}}, status: "waiting", map: "map1"}

config: dict = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)  # Load the config file into a dictionary


# Add a new server to the servers dictionary
def addServer(code: int) -> None:
    tServers[code]: dict = {"players": {}, "status": "waiting", "map": "map1"}
    return None


# Join a server with the given code and ip
def playerJoin(code: int, ip: str) -> None:
    tServers[code]["players"][ip]: dict = {"posX": 0, "posY": 0, "direction": None, "timeSinceLastMessage": 0, "bullets": []}
    return None


# Create a new socket with the given urlHost and port
def createSocket(urlHost: str, port: int) -> None:
    return None


# Create a new server with the given code
@app.route('/tanketteapi/create/<int:code>', methods=['POST'])
def createServer(code: int) -> tuple:
    if code in tServers:
        return "Server already exists", 401
    addServer(code)
    return "Server created", 201


# Join a server with the given code
@app.route('/tanketteapi/join/<int:code>', methods=['POST'])
def joinServer(code: int) -> tuple:
    if code not in tServers:
        return "Server does not exist", 402
    if request.remote_addr in tServers[code]["players"]:
        return "You are already in the server", 403
    if len(tServers[code]["players"]) >= 2:
        return "Server is full", 404
    playerJoin(code, request.remote_addr)
    return "Server joined", 202


@app.route('/tanketteapi/servers', methods=['GET'])
def getServers() -> tuple:
    if len(tServers) == 0:
        return "No servers available", 405
    return tServers, 200


if __name__ == '__main__':
    app.run()
