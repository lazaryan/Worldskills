# from app import app
# import view
# import rest_todo

import os
from time import sleep


# from Essenses.decorators import thread
# from Essenses.block import Block


# @thread
# def server():
#     block = Block()
#     block.create_block()


if __name__ == '__main__':
    # server()
    #app.run()
    with open('data/test.txt', 'r') as f:
        a = f.readlines()
        print(len(a))
        os.system('cls')

    count = 0

    os.system('start python test.py')
    # os.startfile('./test.py')

    while True:
        print(a)
        print('test')
        print('log')
        sleep(5)
        os.system('cls')
        count += 1
