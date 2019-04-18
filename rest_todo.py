import rsa
import view
import datetime

from app import app
from view import *
from essense.sockets import *
from flask import jsonify, request, url_for

from essense.user import User


"""Запуск Rest Функций проекта
Ответы на все запросы с клиентской стороны
"""


@app.route('/todo/api/register', methods=['POST'])
def todo_register():
    """Регичстрация пользователя"""
    role = request.json["data"]

    token = User().register(role)

    return jsonify({"data": {"status": "Ok", "location": url_for('keys', token=token)}})


@app.route('/todo/api/pay', methods=['POST'])
def todo_pay():
    """Выполнения оплаты"""
    data_req = request.json
    print('===============================')

    if (int(data_req["coins"]) > get_tail()):
        return jsonify({"data": "err"})

    data = {
        "to": data_req["to"],
        "from": data_req["from"],
        "coins": data_req["coins"],
        "time": datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
    }
    tranzaction = {
        "type": "request_tranzaction_pay",
        "data": data,
        "sign": User().sign(data)
    }

    send_all(tranzaction)

    return jsonify({"data": "Ok"})


@app.route('/todo/api/enter', methods=['POST'])
def todo_enter():
    """вход в сеть"""
    data_req = request.json

    list_users = jsObj.get_json('data/list.json')
    test = False
    id = ''
    for user in list_users:
        if user["id"] == data_req["id"]:
            test = True
            id = user["id"]

    if not test:
        return jsonify({"data": "err"})

    get_action_users()

    return jsonify({"data": "Ok"})


@app.route('/todo/api/exit')
def todo_exit():
    """Выход из приложения"""
    jsObj.clear_file('data/user.json')
    return redirect(url_for('index'))


def get_tail():
    """Получения того, сколько у нас денег в сети"""
    with open('data/tail', 'r') as file:
        lines = file.readlines()

    money = 0
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        print(int(line.split(' ')[1]))
        money += int(line.split(' ')[1])

    return money