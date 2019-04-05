from app import app
from flask import request, jsonify
from objects.keys import Keys
import rsa


@app.route('/todo/api/login', methods=['POST'])
def todo_login():
    obj = []

    for key in request.json:
        obj.append({"name": key, "value": request.json[key]})

    Keys().set_keys(obj)
    return jsonify({"data": "Ok"})


@app.route('/todo/api/check_in', methods=['POST'])
def todo_check_in():
    obj = request.json
    (public_key, private_key) = rsa.newkeys(256)

    # print(public_key, private_key)
    # print(public_key.e)
    # print(public_key.n)
    # sm tyt
    # ___________________________________________
    # a = 7465475643
    # b = 345843653765437564375348
    #
    #
    # ok = rsa.PublicKey(e=gg, n=jjj)
    # key = ()
    # key.e = a
    # key.n = b
    # ____________________________________________

    a = public_key.save_pkcs1(format='DER')
    print(a)

    keys = [
        {"name": "public_key", "value": str(public_key.save_pkcs1(format='DER'))},
        {"name": "private_key", "value": str(private_key.save_pkcs1(format='DER'))}
    ]
    Keys().set_keys(keys)

    return jsonify({"data": "Ok"})


