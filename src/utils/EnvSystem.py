# File: EnvSystem.py
#
# A file created to retrieve data from .env files in a way that will make the code cleaner.
# In addition, we are able to use this class to immediately parse the data into the appropriate type, which I noticed
# that had not happened before. All "clean" fetched data was type <str>.

import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta
from src.server.ServerInfo import ServerInfo
from src.utils.ParseSystem import ParseSystem


class EnvSystem:
    __fileName: str
    __path: Path
    __configData: dict

    # The constructor itself specifies the directory with the file, so we only enter the name of the file
    # from which we would like to extract data.
    @classmethod
    def __init__(cls, _fileName: str):
        cls.__fileName = _fileName
        cls.__path = Path('config/' + _fileName)
        cls.__configData = dict()

        cls.__load_data()

    @classmethod
    def __load_data(cls) -> None:
        load_dotenv(dotenv_path=cls.__path)

    # A method created specifically for retrieving data on server parameters.
    # Better don't touch.
    @classmethod
    def get_config_server(cls, _currentSettings: dict) -> dict:
        for key, _ in _currentSettings.items():
            val = EnvSystem.get_env_element(key)

            if key in ['PERMANENT_SESSION_LIFETIME', 'SEND_FILE_MAX_AGE_DEFAULT']:
                cls.__configData.setdefault(key, timedelta(seconds=int(val)))
                continue

            cls.__configData.setdefault(key, ParseSystem.auto_parse(val))

        return cls.__configData

    @staticmethod
    def get_env_element(_nameElement: str) -> any:
        return ParseSystem.auto_parse(os.getenv(_nameElement))
