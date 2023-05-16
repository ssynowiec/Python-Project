import os
from flask import Flask
from logging.config import dictConfig
from src.Utils.JSON_System import JSON_System

app: Flask = Flask(__name__)
dictConfig(JSON_System.GetJson('\\config\\loggerConfig'))


import src.Controller.IndexController
