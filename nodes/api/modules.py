import asyncio
from core.helpers.inputs import SocketInput
from core.helpers.filters import BaseFilter
from core.helpers.outputs import OutputSocket
from core.managers import modules

@asyncio.coroutine
def treat_data(data, transport):
    return {'data': data, 'transport': transport}


@modules.register('pykmin_api_listener')
class ModuleInput(SocketInput):
    port = 8080

    def start(self):
        self.treatment = treat_data
        super(ModuleInput, self).start()


@modules.register('pykmin_api_filter')
class OrderHandler(BaseFilter):

    def filter(self, data):
        order = data.split(maxsplit=1)
        if order[0] == 'stop':
            module = order[1]
            module_instance = modules.get_element(module)
            module_instance.stop()
            return 'Module sucessfully stopped'

        if order[0] == 'start':
            module = order[1]
            module_instance = modules.get_element(module)
            module_instance.start()
            return 'Module sucessfully started'

        if order[0] == 'list':
            ret = []
            for element in modules.get_inputs():
                ret.append("- %s" % element)
            return '\n'.join(ret)

        return 'Error ...'

@modules.register('pykmin_api_output')
class ToSocket(OutputSocket):

    def data_send(self, data=None):
        super(ToSocket, self).data_send(self.data)

