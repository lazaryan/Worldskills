from essense.fs.json_files import JsonFiles
from essense.sockets import *
from essense.blocks import Block
import rsa
import os
import copy
import socket
import hashlib
import base64


jsObj = JsonFiles()


class User(object):
    __COUNT_TRANZACION__ = 0
    __TIIMER__ = 10
    __ACTIVE__ = False

    @thread
    @pause(5)
    def pull_monitoring(self):
        """Метод мониторинга пулла транзакций для начала майнинга"""
        print('staaaaaaarty=====================================================')
        if not jsObj.is_zero_file('data/tmp/pull.json'):
            print('0000000000000000000000000000')
            self.__ACTIVE__ = True

        if self.__ACTIVE__:
            self.build_block()

        self.pull_monitoring()

    def mine_block(self, new_block):
        """Метод майнинга блока"""
        print("start mining")
        print(new_block)
        flag = True
        while flag:
            to_hash = (json.dumps(new_block['data']['body'])).encode()
            to_hash = hashlib.sha256(to_hash).hexdigest()
            print(to_hash[-2::1])
            if (to_hash[-2::1] == '00'):
                jsObj.set_prop(new_block, 'data.header.hash', to_hash)
                flag = False
            else:
                nonce = jsObj.get_prop(new_block, 'data.body.nonce')
                nonce = str(int(nonce) + 1)
                jsObj.set_prop(new_block, 'data.body.nonce', nonce)

        return new_block

    @pause(__TIIMER__)
    def build_block(self):
        block = Block()

        tranzactions = jsObj.get_json('data/tmp/pull.json')
        self.__ACTIVE__ = False
        jsObj.clear_file('data/tmp/pull.json')

        body = block.build_body(tranzactions)
        my_sign = self.sign(body)
        head = block.build_head(my_sign)

        raw_block = block.create_block(head, body)

        new_block = self.mine_block(raw_block)

        # tranzactions = jsObj.get_json('data/tmp/pull.json')

        print("WELL DONE")

        block_id = jsObj.get_json('data/data.json')
        block_id["id_finish"] = int(block_id["id_finish"]) + 1
        jsObj.set_json_in_file('data/data.json', block_id)

        print(block_id["id_finish"])

        path = 'data/blockchain/' + str(block_id["id_finish"]) + '.json'
        with open(path, 'w') as f:
            json.dump(new_block, f, indent=5)
            f.close()

        # jsObj.set_json_in_file(path, new_block,)

        send_all(new_block)

        return new_block

    def register(self, role):
        """Метод регистрации нового пользователя"""
        (piublic_key, private_key) = rsa.newkeys(512)

        user = {
            "ip": socket.gethostbyname(socket.getfqdn()),
            "id": hashlib.sha1(str(piublic_key).encode('utf-8')).hexdigest(),
            "role": role,
            "public_key": {
                "n": piublic_key.n,
                "e": piublic_key.e
            }
        }

        # AAAAA УБЕРИ
        # user["id"] = 'e9d9dc947bf04359766a1f02369e91352c05f5e1'

        prKey = {
            "n": private_key.n,
            "e": private_key.e,
            "d": private_key.d,
            "p": private_key.p,
            "q": private_key.q
        }

        user_action = copy.copy(user)
        user_action = jsObj.set_prop(user_action, 'private_key', prKey)

        jsObj.set_json_in_file('data/user.json', user_action)

        token = self.__create_token()

        # sign = hashlib.sha256(json.dumps(user).encode()).hexdigest()
        sign = (base64.b64encode(rsa.sign(json.dumps(user).encode(), private_key, 'SHA-256'))).decode()

        tranzaction = {
            "type": "request_tranzaction_newUser",
            "data": user,
            "sign": sign
        }

        send_all(tranzaction)
        return token

    @staticmethod
    def get_ip():
        """Метод получения ip активного пользователя"""
        user = jsObj.get_json('data/user.json')
        return user["ip"]

    @staticmethod
    def sign(data):
        """Метод получения цифровой подписи"""
        user = jsObj.get_json('data/user.json')
        pr_key = user["private_key"]

        send_pr_key = rsa.PrivateKey(pr_key["n"], pr_key["e"], pr_key["d"], pr_key["p"], pr_key["q"])

        return (base64.b64encode(rsa.sign(json.dumps(data).encode(), send_pr_key, 'SHA-256'))).decode()

    @staticmethod
    def verify(data, id_user, sign):
        """Метод проверки цифровой подписи"""
        list_users = jsObj.get_json('data/list.json')
        plc = {}
        for user in list_users:
            if user["id"] == id_user:
                plc = user["public_key"]

        if not plc:
            return False

        new_public_key = rsa.PublicKey(plc["n"], plc["e"])
        try:
            sign = base64.b64decode(sign.encode())
            rsa.verify(json.dumps(data).encode(), new_public_key, sign.encode())
            return True
        except Warning:
            return False

    @staticmethod
    def __create_token():
        """Метод генерации  токена"""
        token = hashlib.sha256(str(os.urandom(128)).encode()).hexdigest()

        list_token = jsObj.get_json('data/tokens.json')
        if not list_token:
            list_token = []

        list_token.append(token)

        jsObj.set_json_in_file('data/tokens.json', list_token)

        return token
