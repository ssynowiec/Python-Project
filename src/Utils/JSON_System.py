import json
from src.Utils.File_System import File


class JSON_System:
    @staticmethod
    def GetJson(_path: str):
        return json.load(File.GetFile(File.GetRootDir() + _path))
