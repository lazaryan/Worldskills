import threading
import time


def thread(func):
    def wrapper(*args, **kwargs):
        print('tyt')
        cth = threading.Thread(target=func, args=args, kwargs=kwargs)
        cth.start()

    return wrapper


def pause(t):
    def wrapper(f):
        def tmp(*args, **kwargs):
            time.sleep(t)
            return f(*args, **kwargs)
        return tmp

    return wrapper
