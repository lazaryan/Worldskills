import socket
import threading

from time import sleep


def thread(func):
    def wrapper(*args, **kwargs):
        cth = threading.Thread(target=func, args=args, kwargs=kwargs)
        cth.start()

    return wrapper


@thread
def server():
    print('server...')
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)

    conn, adr = sock.accept()
    while True:
        data = conn.recv(1024) \
            .decode('utf-8')

        if data:
            print('data: ' + data)

    conn.close()


def client():
    print('client...')
    sock = socket.socket()
    sock.connect(('169.254.50.46', 9090))

    while True:
        message = 'my my my my'
        sleep(3)
        data = message.encode()
        sock.send(data)

        if data == b'test':
            break


th2 = threading.Thread(target=client, args=())
th1 = threading.Thread(target=server, args=())

if __name__ == '__main__':
    th2.start()
    th1.start()
    #client()
    #server()
# client()

# e1 = threading.Event()
# e2 = threading.Event()
#
# th2 = threading.Thread(name='client', target=client(), args=(1, e2, e1))
# # th1 = threading.Thread(name='server', target=server(), args=(0, e1, e2))
#
# th2.start()
#
# print('dfgfdgfdgdf')
# print('dfgfdgfdgdf')
# print('dfgfdgfdgdf')
# print('dfgfdgfdgdf')
# print('dfgfdgfdgdf')
# # th1.start()
#
# th2.run()
#
# e1.set()
#
# # th1.join()
# th2.join()
#
# # while True:
# #     print('test test')
# #     sleep(3)
#
# #server()

