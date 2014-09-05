import asyncio
from core.helpers.inputs import SocketInput
from core.managers import inputs


@asyncio.coroutine
def treat_data(data, transport):
    return {'data': data, 'transport': transport}


@inputs.register('test_input')
class ModuleInput(SocketInput):

    def start(self):
        self.treatment = treat_data
        super(ModuleInput, self).start()
