from os import environ
from pathlib import Path

from flask import request
from src.Utils.JSON_System import JSON_System
from src import app

import os
from dotenv import load_dotenv

dotenv_path = Path('../config/.env')
load_dotenv(dotenv_path=dotenv_path)

class Server:
    __HOST: str
    __PORT: int
    __debug: bool

    @classmethod
    def __init__(cls):
        cls.__HOST = str()
        cls.__PORT = 0
        cls.__debug = False

    @classmethod
    def __ConfigServer(cls, _host: str = 'localhost', _port: int = 5555):
        host = os.getenv('HOST')
        cls.__HOST = host

        try:
            port = os.getenv('PORT')
            cls.__PORT = port

        except ValueError:
            cls.__PORT = 5555

    @classmethod
    def __setSettings(cls):
        try:
            app.logger.info('Attempting to read the server configuration from a file...')

            serverConfig = JSON_System.GetJson('/config/serverConfig')['connect']
            cls.__ConfigServer(serverConfig['host'], serverConfig['port'])

            app.logger.info('The basic parameters of the server were successfully set.')
        except:
            app.logger.warning('Problem detected. Setting the default server parameters.')
            cls.__ConfigServer()

    @classmethod
    def Server_START(cls, _debug: bool = False):
        app.logger.info("Server switch-on in progress....")

        try:
            cls.__debug = _debug

            cls.__setSettings()

            app.logger.info('The server has been successfully started.')
            app.run(cls.__HOST, cls.__PORT, debug=_debug)

        except RuntimeError:
            app.logger.critical('An unexpected critical problem has occurred!')
            exit(21)
