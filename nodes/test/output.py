from core.managers import outputs


class ToFile():
    def __init__(self, name):
        pass

    def start(self, task):
        data = task.result()
        print(data)


outputs.register('test_output', ToFile)