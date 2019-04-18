import socket
from essense.fs.json_files import JsonFiles
from essense.decorators import *
import json

jsObj = JsonFiles()
PORT = 9092


@thread
def get_messages():
    """Функция для обработки всех запросов в приложении
    Постороена по принципку своего API типизации запросов
    """
    sock = socket.socket()
    sock.bind(('', PORT))

    while True:
        sock.listen(10)
        conn, addr = sock.accept()
        message = conn.recv(2048).decode()
        obj = json.loads(message)

        types = str(obj["type"]).split('_')
        print(obj)
        if types[0] == 'request':
            print('request')
            if types[1] == 'action':
                action(obj["data"])
            elif types[1] == 'tranzaction':
                print('tranzaction')
                if types[2] == 'newUser':
                    tranzaction_line = json.dumps(obj)
                    with open('data/tmp/pull.json', 'a') as f:
                        f.write(tranzaction_line)
                        f.close()
                elif types[2] == 'pay':
                    pass
            elif types[1] == 'block':
                print('block')
                name = str(jsObj.get_prop(obj, 'data.header.block_id'))
                with open('data/blockchain/' + name + '.json', 'w') as f:
                    json.dump(obj, f, indent=5)

        elif types[0] == "answer":
            if types[1] == 'action':
                add_action_user(obj["data"]["id"])


def action(data):
    """Ответ пользователя на запрос его активности в сети"""
    my_data = jsObj.get_json('data/user.json')

    if not check_id(data["id"]):
        pass
        # user_m.add_user()

    print('================')
    print(my_data)
    answer = {
        "type": "answer_action",
        "data": {"id": my_data["id"]}
    }

    send_message(data["ip"], answer)
    add_action_user(data["id"])


def add_action_user(id_user):
    """Добавить пользователя, который отправил запрос о том, что он в сети
    :param id_user: <str> id пользователя
    """
    action_user = jsObj.get_json('data/action_users.json')
    users = jsObj.get_json('data/list.json')
    data = {}

    for user in users:
        if user["id"] == id_user:
            data = user
            break

    if not action_user:
        action_user = []

    test = False
    for user in action_user:
        if user["ip"] == data["ip"]:
            test = True
            break

    if not test:
        action_user.append(data)

        jsObj.set_json_in_file('data/action_users.json', action_user)


def check_id(id_user=''):
    """Проверка, есть ли такой поль зователь в сети"""
    test = False
    users = jsObj.get_json('data/list.json')
    for user in users:
        if user["id"] == id_user:
            test = True
            break

    return test


def send_message(ip, data):
    """Отправка сообщения пользователю"""
    sock = socket.socket()
    print(data)
    try:
        sock.connect((ip, PORT))
        try:
            mess = json.dumps(data).encode()
        except TypeError:
            mess = str(data).encode()
        sock.send(mess)
        sock.close()
    except OSError:
        print('aaaaaaa')


def get_action_users():
    """Метод получения всех активных пользователей"""
    users = jsObj.get_json('data/list.json')
    my_data = jsObj.get_json('data/user.json')
    for user in users:
        test = False
        try:
            test = my_data["ip"]
        except KeyError:
            return
        if user["ip"] != my_data["ip"]:
            message = {
                "type": "request_action",
                "data": {
                    "id": my_data["id"],
                    "ip": my_data["ip"]
                }
            }
            print('aaaaaaa')
            print(user["ip"])
            print(message)
            send_message(user["ip"], message)


def send_all(data):
    """Метод отправки всем активным пользователям сообщения"""
    users = jsObj.get_json('data/action_users.json')
    for user in users:
        send_message(user["ip"], data)
