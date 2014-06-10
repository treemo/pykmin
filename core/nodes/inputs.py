import asyncio
import logging

from core.managers import inputs

class Input(object):

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.loop = asyncio.get_event_loop()

    def start(self):
        pass

    def next(self):
        inputs.add_to_queue('test_input')


class SocketInput(Input):
    protocol = None
    address = '127.0.0.1'
    port = 8888

    def start(self):
        coroutine = self.loop.create_server(self.protocol, self.address, self.port)
        self.loop.run_until_complete(coroutine)