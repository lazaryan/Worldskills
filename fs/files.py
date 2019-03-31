import os
from fs.directory import Directory


class Files(Directory):
    def __init__(self):
        super().__init__()

    def _create_file(self, path_to_file=''):
        """
        Метод создания файла
        :param path_to_file: <str> Путь к файлу
        :return: <bool> Успешность операции
        """
        directory = os.path.dirname(path_to_file)

        if not os.path.isdir(directory):
            self._create_dir(directory)
            open(path_to_file, 'w').close()
            return True
        else:
            if os.path.isfile(path_to_file):
                return False
            else:
                open(path_to_file, 'w').close()
                return True

    @staticmethod
    def _clear_file(path_to_file=''):
        """
        Метод очистки файла
        :param path_to_file: <str> Путь к файлу
        :return: <bool> Успешность операции
        """
        if not os.path.isfile(path_to_file):
            return False
        open(path_to_file, 'w').close()

        return True

    @staticmethod
    def _del_file(path_to_file=''):
        """
        Удаление файла
        :param path_to_file: <str> Путь к файлу
        :return: <bool> Успешность операции
        """
        if not os.path.isfile(path_to_file):
            return False

        os.remove(path_to_file)

        return True

    @staticmethod
    def _is_file(path_to_file):
        return os.path.isfile(path_to_file)

    @staticmethod
    def _is_zero_file(path_to_file=''):
        """
        Проверяет файл на пустоту
        :param path_to_file: <str> Путь к файлу
        :return: <bool> Возвращает Boolean значение
        """
        return not (os.path.isfile(path_to_file) and os.path.getsize(path_to_file) > 0)
