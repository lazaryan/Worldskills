from app import app
import view
import rest_todo
from essense.sockets import *
from essense.decorators import *
from essense.fs.json_files import JsonFiles
from essense.user import User

user = User()

def client():
    """Клиентская часть проекта"""
    app.run()


@thread
def server():
    """Серверная часть кода, которая работает в отдельном потоке"""
    clear_data()
    user.pull_monitoring()
    get_messages()
    get_action_users()


def clear_data():
    """Очистка всех временных файлов"""
    JsonFiles().set_json_in_file('data/action_users.json', [])
    JsonFiles().clear_file('data/pull.json')


if __name__ == '__main__':
    """Запуск проекта"""
    server()
    client()
