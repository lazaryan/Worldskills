from app import app
from flask import render_template, redirect, url_for
from objects.keys import Keys


@app.route('/')
def index():
    if not action():
        return redirect(url_for('login'))

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

    return redirect(url_for('index'))


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
