import asyncio
from core.nodes.inputs import SocketInput
from core.managers import inputs

@asyncio.coroutine
def treat_data(data, transport):
    return {'data': data, 'transport': transport}


class ModuleInput(SocketInput):
    port = 8080

    def start(self):
        self.treatment = treat_data
        super(ModuleInput, self).start()

inputs.register('pykmin_api_listener', ModuleInput)