from app import app
from flask import request, jsonify, url_for
from Essenses.user import User


@app.route('/todo/api/register', methods=['POST'])
def todo_register():
    data = request.json
    print(data)

    token = User().registration(data)

    return jsonify({'data': 'Ok', 'location': url_for('keys', token=token)})

