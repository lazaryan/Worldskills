import os
from fs.directorys import Directorys


class Files(Directorys):
    """Класс работы с файлами"""
    def __init__(self):
        super().__init__()

    def _create_file(self, path_to_file):
        """Метод создания файла"""
        if self._is_file(path_to_file):
            return False

        director = os.path.dirname(path_to_file)

        if not self._is_dir(director):
            self._create_dir(director)

        open(path_to_file, 'w').close()

        return True

    def _clear_file(self, path_to_file=''):
        """Метод очистки файла"""
        if self._is_zero_file(path_to_file):
            return False

        open(path_to_file, 'w').close()

        return True

    def _del_file(self, path_to_file):
        """Метод удаления файла"""
        if not self._is_file(path_to_file):
            return False

        os.remove(path_to_file)

        return True

    def _is_zero_file(self, path_to_file=''):
        """Метод проверки файла на пустоту"""
        return (not self._is_file(path_to_file)) or os.path.getsize(path_to_file) == 0

    @staticmethod
    def _is_file(path_to_file=''):
        """Метод проверки существования файла"""
        return os.path.isfile(path_to_file)
