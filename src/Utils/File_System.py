from pathlib import Path


class File:
    @staticmethod
    def GetRootDir() -> str:
        return str(Path(__file__).parent.parent.parent)

    # Specify the file path relative to root
    @staticmethod
    def GetFile(_path):
        return open(_path, "rb")
