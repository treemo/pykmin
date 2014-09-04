from core.nodes.outputs import Output
from core.managers import outputs


class ToFile(Output):

    def start(self, task):
        print(self.data)
        print('hello')

outputs.register('f2b_output', ToFile)