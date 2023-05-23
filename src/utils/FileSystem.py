# File: FileSystem.py
#
# The class responsible for files and things related to them.

import os


class FileSystem:
    @staticmethod
    def get_file_list(_pathToDir: str) -> list[str]:
        return os.listdir(_path)

    @staticmethod
    def get_sort_file_list(_pathToDir: str) -> list[str]:
        return sorted(FileSystem.get_file_list(_pathToDir))

    @staticmethod
    def delete_file(_pathToFile) -> None:
        os.remove(_pathToFile)

    @staticmethod
    def exist_file( _pathToFile) -> bool:
        return os.path.exists(_pathToFile)
