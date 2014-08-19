import asyncio
from core.nodes.inputs import SocketInput
from core.managers import inputs


@asyncio.coroutine
def treat_data(data):
    return data


class ModuleInput(SocketInput):
    port = 8889

    def start(self):
        self.treatment = treat_data
        self.logger.info('Test input 2 launched')
        super(ModuleInput, self).start()

inputs.register('test_input2', ModuleInput)