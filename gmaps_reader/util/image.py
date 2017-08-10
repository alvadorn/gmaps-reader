import threading

COUNT = 0
lock = threading.Lock()

def save_image(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)

def select_name(prefix='img'):
    global COUNT
    lock.acquire()
    name = prefix + str(COUNT)
    _increment()
    lock.release()
    return name

def _increment():
    global COUNT
    COUNT = COUNT + 1
