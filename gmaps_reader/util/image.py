import threading

COUNT = 0
lock = threading.Lock()

def save_image(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)

def select_name():
    global COUNT
    lock.acquire()
    name = 'img' + str(COUNT)
    _increment()
    lock.release()
    return name

def _increment():
    global COUNT
    COUNT = COUNT + 1
