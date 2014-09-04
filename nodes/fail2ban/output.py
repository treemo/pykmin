from core.nodes.outputs import Output
from core.managers import outputs


class ToFile(Output):

    def start(self, task):
        super(ToFile, self).start(task)
        print(self.data)

outputs.register('f2b_output', ToFile)