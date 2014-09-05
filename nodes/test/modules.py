import asyncio
from core.helpers.inputs import SocketInput
from core.helpers.filters import BaseFilter
from core.helpers.outputs import OutputFile, OutputSocket, OutputLogger
from core.managers import modules


@asyncio.coroutine
def treat_data(data, transport):
    return {'data': data, 'transport': transport}


@modules.register('test_input')
class ModuleInput(SocketInput):

    def start(self):
        self.treatment = treat_data
        super(ModuleInput, self).start()


@modules.register('test_filter')
class ModuleFilter(BaseFilter):

    def filter(self, data):
        return '%sa' % data


@modules.register('test_output2')
class ToFile(OutputFile):
    file = 'test.log'


@modules.register('test_output')
class ToSocket(OutputSocket):

    def data_send(self, data=None):
        super(ToSocket, self).data_send(self.data)


@modules.register('logger_output')
class ToLogger(OutputLogger):

    def write(self, data):
        return '[FAIL2BAN] %s' % data

