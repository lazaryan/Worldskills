import os
import shutil


class Directory(object):
    def _create_dir(self, path_to_dir=''):
        """
        Метод создания директории
        :param path_to_dir: <str> путь к папке
        :return: <bool> Успешность опперации
        """
        if self._is_dir(path_to_dir):
            return False

        os.makedirs(path_to_dir, exist_ok=True)
        return True

    def _del_dir(self, path_to_dir=''):
        """
        Метод удаления папок
        :param path_to_dir: <str> путь к папке
        :return: <bool> Успешность опперации
        """
        if self._is_dir(path_to_dir):
            return False

        shutil.rmtree(path_to_dir, ignore_errors=True)

        return True

    def _clear_dir(self, path_to_dir=''):
        """
        Метод удаления всех папок и файлов в данном каталоге
        :param path_to_dir:  <str> путь к папке
        :return: <bool> Успешность опперации
        """
        if self._is_dir(path_to_dir):
            return False

        for root, dirs, files in os.walk(path_to_dir):
            for file in files:
                os.unlink(os.path.join(root, file))
            for directory in dirs:
                self._del_dir(os.path.join(root, directory))

        return True

    @staticmethod
    def _is_dir(path_to_dir):
        """Проверка если папка существует"""
        return os.path.isdir(path_to_dir)
