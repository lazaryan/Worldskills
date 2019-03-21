import os
import errno
import shutil


class Directory (object):
    """Класс для работы с директориями"""
    @staticmethod
    def _create_directory(path=''):
        """
        Создает директорию
        :param path: <str> Путь к директории
        :return: <bool> True в случае успеха
        """
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as exception:
            if exception != errno.EEXIST:
                raise

        return True

    @staticmethod
    def _delete_directory(path):
        """
        Метод удаления директории

        :param path: <str> Путь к директории
        :return: <bool> True в случае успеха
        """
        shutil.rmtree(path, ignore_errors=False)

        return True

    @staticmethod
    def _clear_directory(path):
        """
        Метод очистки директории
        Метод очищает все содержимое директории
        Включая все вложенне файлы и подкаталоги

        :param path: <str> Путь к директории
        :return: <bool> True в случае успеха
        """
        for root, dirs, files in os.walk(path):
            for file in files:
                os.unlink(os.path.join(root, file))
            for directory in dirs:
                shutil.rmtree(os.path.join(root, directory))

        return True
