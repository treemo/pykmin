from core import Controller

if __name__ == '__main__':
    controller = Controller()
    controller.autodiscover_modules()
    controller.start()