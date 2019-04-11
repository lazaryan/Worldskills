from fs.json_files import JsonFiles
import rsa
import hashlib
import copy
import socket
import os


class User(object):
    """Класс работы пользователя в целом"""
    def registration(self, data={}):
        """Метод регистрации нового пользователя"""
        if not data:
            return False

        (public_key, private_key) = rsa.newkeys(256)
        ip_user = socket.gethostbyname(socket.getfqdn())

        concat_keys = str(public_key) + str(private_key)
        id_user = hashlib.sha256(concat_keys.encode('utf-8')).hexdigest()

        prKey = {
            "n": private_key.n,
            "e": private_key.e,
            "d": private_key.d,
            "p": private_key.p,
            "q": private_key.q
        }

        user_list = {
            "public_key": {
                "n": public_key.n,
                "e": public_key.e
            },
            "ip": ip_user,
            "name": data["name"],
            "email": data["email"],
            "role": data["role"],
            "id": id_user
        }

        user = copy.copy(user_list)
        user = JsonFiles().set_prop(user, 'private_key', prKey)

        JsonFiles().set_json('data/user.json', user)
        self.add_user(user_list)

        return self.create_token()

    @staticmethod
    def add_user(user):
        """Метод получения пользователя"""
        JsonFiles().set_prop_to_file('data/list.json', user["id"], user)

    @staticmethod
    def create_token():
        """Метод создания однаразового токена"""
        token = hashlib.sha1(os.urandom(128)).hexdigest()

        data = JsonFiles().get_json('data/tmp/token.json')

        print(data)

        if not data:
            print('aaaaaaaaaaaa')
            data = []

        data.append(token)

        JsonFiles().set_json('data/tmp/token.json', data)

        return token
