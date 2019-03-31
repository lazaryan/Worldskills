from app import app
from flask import request, jsonify
from objects.keys import Keys


@app.route('/todo/api/login', methods=['POST'])
def todo_login():
    obj = []

    for key in request.json:
        obj.append({"name": key, "value": request.json[key]})

    Keys().set_keys(obj)
    return jsonify({"data": "Ok"})


