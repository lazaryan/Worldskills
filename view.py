from app import app
from flask import redirect, render_template, url_for, request
from essense.fs.json_files import JsonFiles

jsObj = JsonFiles()


@app.route('/')
def index():
    if active_user():
        return render_template('index.html', data=action_info(), action=active_user())
    else:
        return render_template('enter.html', action=active_user())


@app.route('/register')
def register():
    return render_template('register.html', action=active_user())


@app.route('/enter')
def enter():
    return render_template('enter.html', action=active_user())


@app.route('/help')
def help():
    return render_template('help.html', action=active_user())


@app.route('/keys/', methods=['GET'])
def keys():
    token = request.args["token"]
    tokens = JsonFiles().get_json('data/tokens.json')

    if not token:
        return redirect(url_for('index'))

    if token in tokens:
        tokens.remove(token)
        JsonFiles().set_json_in_file('data/tokens.json', tokens)
    else:
        return redirect(url_for('index'))

    keys = get_keys()

    return render_template('keys.html', public=keys[0], private=keys[1], action=active_user())


@app.errorhandler(404)
def not_page(e):
    return redirect(url_for('index'))


def action_info():
    users = jsObj.get_json('data/action_users.json')
    my_data = jsObj.get_json('data/user.json')

    list_id = []
    for user in users:
        try:
            list_id.append(user["id"])
        except KeyError:
            pass

    data = {
        "id_users": list_id,
        "tail": get_tail(),
        "my_id": my_data["id"]
    }

    return data


def get_keys():
    user = jsObj.get_json('data/user.json')
    public_key = user["public_key"]
    private_key = user["private_key"]

    return [public_key, private_key]


def get_tail():
    with open('data/tail', 'r') as file:
        lines = file.readlines()

    money = 0
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        print(int(line.split(' ')[1]))
        money += int(line.split(' ')[1])

    return money


def active_user():
    return not jsObj.is_zero_file('data/user.json')
