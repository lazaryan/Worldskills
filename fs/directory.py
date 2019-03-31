import os
import errno
import shutil


class Directory(object):
    @staticmethod
    def _create_dir(path_to_dir=''):
        """
        Метод создания директории. Директорий может быть создано несколько вложанных
        :param path_to_dir: <str> Путь к папке
        :return: <bool> Успешность операции
        """
        try:
            os.makedirs(path_to_dir, exist_ok=True)
        except OSError as exception:
            if exception != errno.EEXIST:
                raise
            else:
                return False

        return True

    @staticmethod
    def _del_dir(path_to_dir=''):
        """
        Метод удаление директории
        :param path_to_dir:  <str> Путь к директории
        :return: <bool> Успешность операции
        """
        shutil.rmtree(path_to_dir, ignore_errors=True)

        return True

    @staticmethod
    def _clear_dir(path_to_dir):
        """
        Метод очистки директории
        :param path_to_dir: <str> Путь к директории
        :return:  <bool> Успешность операции
        """
        for root, dirs, files in os.walk(path_to_dir):
            for file in files:
                os.unlink(os.path.join(root, file))
            for directory in dirs:
                shutil.rmtree(os.path.join(root, directory))
