from app import app
import view
import rest_todo

from Essenses.decorators import thread
from Essenses.block import Block


@thread
def server():
    block = Block()
    block.create_block()


if __name__ == '__main__':
    server()
    app.run()
