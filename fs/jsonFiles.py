import os
import json

from .files import Files


class JsonFiles(Files):
    """Класс для работы с json файлами"""
    def __init__(self):
        super().__init__()

    def _create_file(self, path_to_file, default_data=''):
        """
        Метод для создания файла
        Безопасно создает файл и все необходимые пути для этого
        Каждому файлу придает дефолтную форму

        :param path_to_file: <str> Путь к файлу
        :param default_data: <obj|str> Что должно быть в файле по умолчанию
        :return: <bool> True - если операция прошла успешно
        """
        path = os.path.dirname(path_to_file)

        if os.path.exists(path):
            if not os.path.exists(path_to_file):
                open(path_to_file, 'w').close()
        else:
            self._create_directory(path)
            open(path_to_file, 'w').close()

        self._write_default_data(path_to_file, default_data)

        return True

    def _write_default_data(self, path_to_file='', default_data=''):
        """Записывает дефолтную структуру в файл"""
        if not self._is_not_zero_file(path_to_file):
            self._write_data(path_to_file, default_data)

    def _get_property(self, path_to_file='', property_name=''):
        """Метод получения значения свойства объекта из файла

        :param path_to_file: <str> Путь к файлу для чтения
        :param property_name: <str> Имя читаемого свойства
        :return: <str> Возвращает значения свойства или пустую строку, если его нет
        """
        data = self._get_json(path_to_file)

        try:
            value = data[property_name]
        except KeyError:
            value = ''

        return value

    def _set_property(self,  path_to_file='', property_name='', value=''):
        """Метод записывает свойство в файл

        :param path_to_file: <str> Путь к файлу
        :param property_name: <str> Имя свойства
        :param value: <any> Значение свойства
        :return: <bool> True в случае успеха
        """
        data = self._get_json(path_to_file)

        data[property_name] = value

        self._write_data(path_to_file, data)

        return True

    def _del_property(self, path_to_file='', property_name=''):
        """
        Метод удаления свойства json файла
        :param path_to_file: <str> путь к файлу
        :param property_name: <str> имя свойства
        :return: <bool> True - в случае успеха и False в случае ошибки
        """
        data = self._get_json(path_to_file)

        if not data:
            return
        try:
            del data[property_name]
        except KeyError:
            return False

        self._write_data(path_to_file, data)

        return True

    @staticmethod
    def _get_json(path_to_file=''):
        """Метод получения json объекта из файла"""
        if not os.path.isfile(path_to_file):
            return {}

        with open(path_to_file, 'r') as file:
            value = json.load(file)

        return value

    @staticmethod
    def _write_data(path_to_file='', data=()):
        """Метод записи json объекта в файл"""
        if not os.path.isfile(path_to_file):
            return ''

        if not data:
            data = {}

        with open(path_to_file, 'w') as json_file:
            json.dump(data, json_file)
