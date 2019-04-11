import json
from fs.files import Files


class JsonFiles(Files):
    """Класс работы с json файлами"""
    def __init__(self):
        super().__init__()

    def get_json(self, path_to_file=''):
        """Метод получения json из файла"""
        if (not self._is_file(path_to_file)) or self._is_zero_file(path_to_file):
            return {}

        with open(path_to_file, 'r') as file:
            value = json.load(file)

        return value or {}

    def set_json(self, path_to_file='', data={}):
        """Метод записи объекта в файл"""
        if not self._is_file(path_to_file):
            self._create_file(path_to_file)

        with open(path_to_file, 'w') as file:
            json.dump(data, file)

        return True

    def set_prop_to_file(self, path_to_file, prop, value):
        """Установить мвойство объекта и записать в файл"""
        if not self._is_file(path_to_file):
            self._create_file(path_to_file)

        data = self.get_json(path_to_file)
        data = self.set_prop(data, prop, value)

        self.set_json(path_to_file, data)

        return True

    def set_prop(self, data, prop, value):
        """Метод добавления свойства (рекурсивный)"""
        path = str(prop).split('.', 1)

        if len(path) == 1:
            data[path[0]] = value
        else:
            try:
                data[path[0]] = self.set_prop(data[path[0]], path[1], value)
            except KeyError:
                data[path[0]] = {}
                data[path[0]] = self.set_prop(data[path[0]], path[1], value)

        return data

    def is_zero_file(self, path_to_file=''):
        return self._is_zero_file(path_to_file)
