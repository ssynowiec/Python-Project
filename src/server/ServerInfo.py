# File: ServerInfo.py
#
# A file containing information about the server.
# It does NOT set server parameters but takes an active part in its configuration

from src import app


class ServerInfo:
    __serverInfo: dict

    # The basic configuration should ALWAYS be specified as a parameter.
    @classmethod
    def __init__(cls, _config: dict):
        cls.__serverInfo = dict(_config)

    @classmethod
    def __is_key_exist(cls, _key: any) -> bool:
        return _key in cls.__serverInfo

    @classmethod
    def set_config(cls, _key: str, _value: any) -> None:
        if cls.__is_key_exist(_key):
            cls.__serverInfo.update({_key: _value})

    @classmethod
    def set_configs(cls, _config: dict) -> None:
        for key, value in _config.items():
            cls.set_config(key, value)

    @classmethod
    def get_all_config(cls) -> dict:
        return cls.__serverInfo
