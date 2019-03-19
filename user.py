from fs.iniFiles import IniFiles


class User(object):
    """Класс пользователя"""
    def __init__(self):
        super()

    def get_list_users(self):
        """
        Метод получения всех пользователей, которые сечас в сети
        :return: <obj> Список пользователей (их Ip и Port)
        """
        pass

    def create_transaction(self, data):
        """
        Метод для создания транзакции перевода денек
        :param data: <obj> Все необходимые данные для транзакции
        :return: <obj> Объект транзакции
        """
        pass

    def get_new_block(self, block):
        """
        Метод записи нового блока в цепочку. Если блок не был добавлен, то функция возвращает ошибку
        :param block: <obj> Новый блок
        :return: <bool> True при успешном добавление и False - если возникла ошибка
        """
        pass

    def check_blockchain(self):
        """
        Метод проверки целостности блокчейна
        :return: <arr> Список блоков с измененной структурой
        """
        pass
