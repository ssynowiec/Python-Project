from src.server import Server

if __name__ == '__main__':
    # Server mode can accept debugging (True) or normal mode (False)
    DEBUG = False   # <- True = Debug On
    serverPtr = Server()

    serverPtr.Server_START(DEBUG)

