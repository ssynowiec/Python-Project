# File: ServerInfo.py
#
# A file containing information about the server.
# It does NOT set server parameters but takes an active part in its configuration

from src import app


class ServerInfo:
    """
    A class containing information about the current server configuration.

    Parameters:
        _config (dict): A dictionary containing a basic configuration based.
    """
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
        """
        A method that sets ONE server parameter.

        Parameters:
            _key (str): The name of the parameter you want to change.
            _value (any): The new value for our parameter.
        """
        if cls.__is_key_exist(_key):
            cls.__serverInfo.update({_key: _value})

    @classmethod
    def set_configs(cls, _config: dict) -> None:
        """
        A method that allows you to change multiple server parameters.
        (The order of entry does not matter).

        Parameters:
            _config (dict): Dictionary with any number of new parameter settings.
        """
        for key, value in _config.items():
            cls.set_config(key, value)

    @classmethod
    def get_all_config(cls) -> dict:
        """
        A method that returns information about the current server settings.

        Return:
            Dictionary with all the current configuration of the server.

        """
        return cls.__serverInfo
