import asyncio
import logging
from core.managers import tasks


class BaseProtocol(asyncio.Protocol):
    transport = None
    handler = None

    def __init__(self, name, handler):
        self.name = name
        self.handler = handler

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        task = asyncio.Task(self.handler(data, self.transport))
        task.add_done_callback(self.next_step)

    def next_step(self, task):
        tasks.add_to_queue(self.name, task)


class Input(object):

    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.__class__.__name__)
        self.loop = asyncio.get_event_loop()

    def start(self):
        pass


class SocketInput(Input):
    protocol = BaseProtocol
    treatment = None
    server = None
    address = '127.0.0.1'
    port = 8888

    def start(self):
        proto = self.protocol(self.name, self.treatment)
        coro = self.loop.create_server(lambda: proto,
                                        self.address, self.port)
        self.server = self.loop.run_until_complete(coro)

    def stop(self):
        self.server.close()