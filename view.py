from app import app
from flask import render_template, redirect, url_for
from objects.keys import Keys
import rsa


@app.route('/')
def index():
    if not action():
        return redirect(url_for('login'))

    # text = 'test'
    # keys = Keys().get_keys()
    #
    # message = 'hello Alisa!'.encode('utf8')
    # print(keys['public_key'])
    # crypto = rsa.encrypt(message, keys['public_key'].encode('utf8'))  # Зашифровка
    # message = rsa.decrypt(crypto, keys['private_key'].encode('utf8'))  # Расшифровка
    # print(message.decode('utf8'))

    return render_template('index.html', action=True)


@app.route('/login')
def login():
    if action():
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/unlogin')
def unlogin():
    Keys().delete_keys()

    return redirect(url_for('login'))


@app.route('/keys')
def my_keys():
    if not action():
        return redirect(url_for('login'))

    return render_template('keys.html', action=True, keys=Keys().get_keys())


@app.route('/checkin')
def check_in():
    return render_template('check_in.html', action=action())


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


def action():
    keys = Keys().get_keys()

    if not keys:
        return False

    test = ''
    try:
        test = keys["public_key"]
        test = keys["private_key"]
    except KeyError:
        return False

    return True
