import os
from essense.fs.directorys import Directory


class Files(Directory):
    def __init__(self):
        """Инициализация класса"""
        super().__init__()

    def _create_file(self, path_to_file=''):
        """
        Метод создания файлаю При необходимости создаются все необходимые директории
        :param path_to_file: <str> путь к файлу
        :return: <bool> Успешность опперации
        """
        if self.is_file(path_to_file):
            return False

        path = os.path.dirname(path_to_file)

        if not self._is_dir(path):
            self._create_dir(path)

        open(path_to_file, 'w').close()

        return True

    def clear_file(self, path_to_file=''):
        """
        Метод очистки существующего файла. Если файла нет - возвращается False
        :param path_to_file: <str> путь к файлу
        :return: <bool> Успешность опперации
        """
        if not self.is_file(path_to_file):
            return False

        open(path_to_file, 'w').close()

    def _del_file(self, path_to_file=''):
        """
        Метод удаления существующего файла. Если файла нет - возвращается False
        :param path_to_file: <str> путь к файлу
        :return: <bool> Успешность опперации
        """
        if not self.is_file(path_to_file):
            return False

        os.remove(path_to_file)

        return True

    def is_zero_file(self, path_to_file=''):
        """Метод проверки пустоты файла"""
        return (not self.is_file(path_to_file)) or os.path.getsize(path_to_file) == 0

    @staticmethod
    def is_file(path_to_file=''):
        """Метод проверки файла"""
        return os.path.isfile(path_to_file)
