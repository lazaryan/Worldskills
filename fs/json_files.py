from fs.files import Files
import json


class JsonFiles(Files):
    def __init__(self):
        super().__init__()

    def get_data(self, path_to_file=''):
        if self._is_zero_file(path_to_file):
            return {}

        with open(path_to_file, 'r') as file:
            value = json.load(file)

        return value or {}

    def set_prop(self, target={}, prop='', value=''):
        """Метод изменения (или добавления) свойства в объект"""
        props = prop.split('.', 1)
        if len(props) == 1:
            target[props[0]] = value
        else:
            try:
                target[props[0]] = self.set_prop(target[props[0]], props[1], value)
            except KeyError:
                target[props[0]] = {}
                target[props[0]] = self.set_prop(target[props[0]], props[1], value)

        return target

    def del_prop(self, target={}, prop=''):
        """Метод удаления свойства, если оно есть в объекте"""
        if not target:
            return target

        props = prop.split('.', 1)

        if len(props) == 1:
            try:
                del target[prop]
            except KeyError:
                return target
            except TypeError:
                return target
        else:
            target[props[0]] = self.del_prop(target[props[0]], props[1])

        return target

    def write_data(self, path_to_file, data):
        """Метод записи json объекта в файл"""
        if not self._is_file(path_to_file):
            self._create_file(path_to_file)

        if not data:
            data = {}

        with open(path_to_file, 'w') as file:
            json.dump(data, file)

    def del_file(self, path_to_file=''):
        return self._del_file(path_to_file)

    def __write_default_data(self, path_to_file=''):
        """Метод записи стартового значения"""
        if self._is_file(path_to_file):
            self.write_data(path_to_file, {})
        else:
            self._create_file(path_to_file)
            self.write_data(path_to_file, {})
