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
    def __parse_data(cls, _key, _val) -> None:
        match _val:
            case 'None':
                cls.__configData.setdefault(key, None)

            case 'False':
                cls.__configData.setdefault(key, False)

            case 'True':
                cls.__configData.setdefault(key, True)

            case _val if _val.isdecimal():
                cls.__configData.setdefault(key, float(_val))

            case _:
                cls.__configData.setdefault(key, _val)

    @classmethod
    def __load_data(cls) -> None:
        load_dotenv(dotenv_path=cls.__path)

    # A method created specifically for retrieving data on server parameters.
    # Better don't touch.
    @classmethod
    def get_config_server(cls, _currentSettings: dict) -> dict:
        for key, _ in _currentSettings.items():
            val = os.getenv(str(key))

            if key in ['PERMANENT_SESSION_LIFETIME', 'SEND_FILE_MAX_AGE_DEFAULT']:
                cls.__configData.setdefault(key, timedelta(seconds=int(val)))
                continue

            cls.__parse_data(key, val)

        return cls.__configData
