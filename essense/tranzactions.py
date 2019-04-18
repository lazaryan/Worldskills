class Tranzaction(object, type):
    def create_tranzaction(self, type, data, sign):
        """Метолд создания новой транзакции"""
        tranzaction = {
            "type": type,
            "data": data,
            "sign": sign
        }

        return tranzaction

    def chek_tranzaction(self, type, tranzaction):
        """Метод проверки транзакции и выполнения ее функций"""
        if (type == 'pay'):
            pass
        elif (type == 'newUser'):
            pass


