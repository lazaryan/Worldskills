from fs.json_files import JsonFiles
from Essenses.decorators import *


class Block(object):
    def __init__(self, id_miner=''):
        __data__ = {"id": id_miner}

    __block__ = {}  # Блок
    __data__ = {}  # Наша информация о блоке
    __transition__ = []  # Список транзакий блока

    __TIME_CREATE__ = 120  # Время создания блока (в секундах)
    __NONCE__ = 5

    def create_block(self):
        """Метод создания нового блока"""
        if self.__block__:
            return self.__block__

        self.__block__ = self.__template_block()
        self.__start_mininng(self.__block__)
        return self.__block__

    def get_block(self):
        """Метод возвращение блока"""
        return JsonFiles().set_prop(self.__block__, 'body.transitions', self.get_transaction())

    def set_transaction(self, transaction):
        """Метод получения новой транзакции"""
        if not self.__block__:
            self.create_block()

        self.__transition__.append(transaction)

    def get_transaction(self):
        return self.__transition__

    @thread
    @pause(__TIME_CREATE__)
    def __start_mininng(self, obj):
        """Метод начала майнинга. Запустится через __TIME_CREATE__"""
        a = self.__NONCE__
        # etc...
        hash_block = '12332423432423'

        return hash_block

    def __clear_block(self):
        """Метод очистки блока"""
        self.__block__ = {}

    @staticmethod
    def __template_block():
        """Общий шаблое для блока"""
        return {
            "header": {
                "id": "",
                "date": time.time(),
                "size": 0
            },
            "body": {
                "transactions": [],
                "count": 0
            },
            "signature": "",
            "hash": ""
        }
