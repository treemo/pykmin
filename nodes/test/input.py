import asyncio
from core.nodes.inputs import SocketInput
from core.managers import inputs

class TestServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.transport.write(data)

    def connection_lost(self, exc):
        self.transport.close()


class ModuleInput(SocketInput):
    protocol = TestServer

    def start(self):
        self.logger.info('Test input launched')
        super(ModuleInput, self).start()

inputs.register('test_input', ModuleInput())