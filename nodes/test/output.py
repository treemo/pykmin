from core.managers import outputs

class ToFile():
    def start(self):
        print('OUT!')

outputs.register('test_output', ToFile())