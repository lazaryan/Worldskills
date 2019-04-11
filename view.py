from app import app
from flask import render_template, redirect, url_for, request
from fs.json_files import JsonFiles


@app.route('/')
def index():
    if not action_user():
        return redirect('registration')

    return render_template('index.html')


@app.route('/registration')
def registration():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/keys')
def keys():
    token = request.args.get('token')

    tokens = JsonFiles().get_json('data/tmp/token.json')

    if len(token) == 0 or not (token in tokens):
        return redirect('index')

    tokens.remove(token)
    user = JsonFiles().get_json('data/user.json')
    keys_user = {'public_key': user['public_key'], 'private_key': user['private_key']}

    print(keys_user)
    JsonFiles().set_json('data/tmp/token.json', tokens)

    return render_template('keys.html', keys_user=keys_user)


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


def action_user():
    return not JsonFiles().is_zero_file('data/user.json')
