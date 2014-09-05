from core.helpers.outputs import OutputFile, OutputSocket, OutputLogger
from core.managers import outputs


@outputs.register('test_output2')
class ToFile(OutputFile):
    file = 'test.log'


@outputs.register('test_output')
class ToSocket(OutputSocket):

    def data_send(self, data=None):
        super(ToSocket, self).data_send(self.data)


@outputs.register('logger_output')
class ToLogger(OutputLogger):

    def write(self, data):
        return '[FAIL2BAN] %s' % data

