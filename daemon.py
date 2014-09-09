from core import Controller

controller = Controller()

def start():
    controller.autodiscover_modules()
    controller.start()

def stop():
    controller.stop()

if __name__ == '__main__':
    start()