import os
import shutil

class Directorys(object):
    """Класс для работы с папками"""
    @staticmethod
    def _create_dir(path_to_dir=''):
        """
        Метод создания директоии
        :param path_to_dir: <str> путь к папке
        :return: <bool> успешность операции
        """
        os.makedirs(path_to_dir, exist_ok=True)

        return True

    def _del_dir(self, path_to_dir=''):
        """
        Метод удаления директории
        :param path_to_dir: <str> путь к папке
        :return: <bool> успешность операции
        """
        if not self.__is_dir(path_to_dir):
            return False;

        shutil.rmtree(path_to_dir, ignore_errors=True)

        return True

    def _clear_dir(self, path_to_dir=''):
        """Метод очистки директории"""

        if not self.__is_dir(path_to_dir):
            return False

        for root, dirs, files in os.walk(path_to_dir):
            for file in files:
                os.unlink(os.path.join(root, file))
            for direct in dirs:
                self._del_dir(os.path.join(root, direct))

        return True

    @staticmethod
    def _is_dir(path_to_dir):
        return os.path.isdir(path_to_dir)
