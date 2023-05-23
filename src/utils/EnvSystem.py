# File: EnvSystem.py
#
# A file created to retrieve data from .env files in a way that will make the code cleaner.
# In addition, we are able to use this class to immediately parse the data into the appropriate type, which I noticed
# that had not happened before. All "clean" fetched data was type <str>.

import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from src.utils.ParseSystem import ParseSystem


class EnvSystem:
    __fileName: str
    __path: Path

    # The constructor itself specifies the directory with the file, so we only enter the name of the file
    # from which we would like to extract data.
    @classmethod
    def __init__(cls, _fileName: str):
        cls.__fileName = _fileName
        cls.__path = Path('config/' + _fileName)

        if find_dotenv(ParseSystem.to_string(cls.__path)):
            cls.__load_data()

    @classmethod
    def __load_data(cls) -> None:
        load_dotenv(dotenv_path=cls.__path)

    @classmethod
    def file_exist(cls) -> bool:
        if find_dotenv(ParseSystem.to_string(cls.__path)):
            return True

        return False

    @staticmethod
    def get_env_element(_nameElement: str) -> any:
        return ParseSystem.auto_parse(os.getenv(_nameElement))
