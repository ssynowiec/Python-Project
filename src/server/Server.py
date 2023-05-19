# File: Server.py
#
# The main file responsible for the server.
# Its main task is to start the server and coordinate with other software files.

import os
from src import app
from src.server.ServerConfig import ServerConfig
from src.Utils.EnvSystem import EnvSystem


class Server:
    __HOST: str
    __PORT: int

    @classmethod
    def __init__(cls):
        env: EnvSystem = EnvSystem('serverConfig.env')

        cls.__HOST = os.getenv('SERVER_HOST')
        cls.__PORT = int(os.getenv('SERVER_PORT'))
        # TODO: Complete the server configuration using the configuration file.

    @classmethod
    def start(cls):
        app.run(cls.__HOST, cls.__PORT)
