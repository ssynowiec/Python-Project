# File: ServerConfig.py
#
# The file that configures the server in every possible way.
# Remember to stick to the SOLID rules when writing here.

from src.server.ServerInfo import ServerInfo
from datetime import timedelta
from src import app


class ServerConfig:
    __serverInfo: ServerInfo

    @classmethod
    def __init__(cls):
        cls.__set_default_config()

    # TODO: Add error handling when the config file doesn't work.
    # A method that sets the server's default parameters. Do not change anything in the dictionary that
    # contains these parameters. This is a backup in case the configuration file is not available or some
    # other sudden error occurs.
    @classmethod
    def __set_default_config(cls) -> None:
        defaultConfig: dict = {
            'APPLICATION_ROOT': None,
            'DEBUG': False,
            'EXPLAIN_TEMPLATE_LOADING': False,
            'JSONIFY_MIMETYPE': 'application/json',
            'JSONIFY_PRETTYPRINT_REGULAR': True,
            'JSON_AS_ASCII': True,
            'JSON_SORT_KEYS': True,
            'LOGGER_HANDLER_POLICY': 'always',
            'LOGGER_NAME': None,
            'MAX_CONTENT_LENGTH': None,
            'PERMANENT_SESSION_LIFETIME': timedelta(days=31),
            'PREFERRED_URL_SCHEME': 'http',
            'PRESERVE_CONTEXT_ON_EXCEPTION': None,
            'PROPAGATE_EXCEPTIONS': None,
            'SECRET_KEY': None,
            'SEND_FILE_MAX_AGE_DEFAULT': timedelta(seconds=43200),
            'SERVER_NAME': None,
            'SESSION_COOKIE_DOMAIN': None,
            'SESSION_COOKIE_HTTPONLY': True,
            'SESSION_COOKIE_NAME': 'session',
            'SESSION_COOKIE_PATH': None,
            'SESSION_COOKIE_SECURE': False,
            'SESSION_REFRESH_EACH_REQUEST': True,
            'TEMPLATES_AUTO_RELOAD': None,
            'TESTING': False,
            'TRAP_BAD_REQUEST_ERRORS': False,
            'TRAP_HTTP_EXCEPTIONS': False,
            'USE_X_SENDFILE': False
        }
        cls.__serverInfo = ServerInfo(defaultConfig)

    @classmethod
    def __update_settings(cls) -> None:
        settingsList: dict = cls.__serverInfo.get_all_config()

        for nameSetting, val in settingsList.items():
            app.config[nameSetting] = val

    # Sets one specific parameter.
    @classmethod
    def set_config_element(cls, _nameConfigElement: str, _val: any) -> None:
        cls.__serverInfo.set_config(_nameConfigElement, _val)

    # Sets the parameter list. The order doesn't matter.
    @classmethod
    def set_config_elements(cls, _configList: dict) -> None:
        cls.__serverInfo.set_configs(_configList)

    # Updates the setting of EVERY item whether it has been changed or not.
    @classmethod
    def updata_config(cls) -> None:
        cls.__update_settings()

    @classmethod
    def get_current_settings(cls) -> dict:
        return cls.__serverInfo.get_all_config()
