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
    def __IsExist(cls, _key: any):
        return _key in cls.__serverInfo

    @classmethod
    def SetConfig(cls, _config: dict) -> None:
        for key, value in _config.items():
            if cls.__IsExist(key):
                cls.__serverInfo.update({key: value})

            else:
                # TODO: Handle a possible error.
                pass

    @classmethod
    def SetConfigs(cls, _key: any, _value: any) -> None:
        if cls.__IsExist(_key):
            cls.__serverInfo.update({_key: _value})

    @classmethod
    def GetAllConfig(cls) -> dict:
        return cls.__serverInfo

    @classmethod
    def GetConfig(cls, _nameConfigElement: str) -> any:
        try:
            value: any = cls.__serverInfo[_nameConfigElement]
        except ValueError:
            # TODO: Add appropriate logs to the code!
            value = None

        return value
