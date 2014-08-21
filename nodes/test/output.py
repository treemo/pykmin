from core.nodes.outputs import OutputFile, OutputSocket
from core.managers import outputs


class ToFile(OutputFile):
    file = 'test.log'


class ToSocket(OutputSocket):

    def data_send(self, data=None):
        super(ToSocket, self).data_send(self.data)

outputs.register('test_output', ToSocket)
outputs.register('test_output2', ToFile)