from fs.files import Files
from configparser import ConfigParser


class IniFiles(object, Files):
    """Класс работы с .ini файлами"""
    def __init__(self):
        super()

    def get_prop(self, path_to_file='./data.ini', name_section='', name_prop=''):
        """
        Метод получения необходимого поля из ini файла
        :param path_to_file: <str> Путь к файлу с конфигурациями
        :param name_section: <str> Имя секции, данные которые нам нужны
        :param name_prop: <str> Имя свойства, котроое мы хотим получить
        :return: <str|bool|num> Необходимое нам значение (если нет свойства или оно пустое - возвращает пустую строку)
        """
        if not self._is_not_zero_file(path_to_file):
            return ''

        config = ConfigParser()
        config.read(path_to_file)

        return config.get(name_section, name_prop)

    def set_prop(self, path_to_file='./data.ini', name_section='', name_prop='', value_prop=''):
        """
        Метод получения необходимого свойства из ini файла
        :param path_to_file: <str> Путь к файлу с конфигурациями
        :param name_section: <str> Имя секции, в которую мы хоти внести данные
        :param name_prop: <str> Имя свойства, котроое мы хотим внести
        :param value_prop: <str|bool|num> Значение свойства
        :return: <bool> True - если операция удалась, иначе - False
        """
        if not self._is_not_zero_file(path_to_file):
            self._create_file(path_to_file)

        config = ConfigParser()
        config.read(path_to_file)

        config.set(name_section, name_prop, value_prop)

        with open(path_to_file, 'w') as configfile:
            config.write(configfile)
