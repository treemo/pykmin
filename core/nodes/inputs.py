import asyncio
import logging
import os
from pathlib import Path
from core.managers import tasks
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


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
        self.logger.info('%s launched' % self.name)


class SocketInput(Input):
    protocol = BaseProtocol
    treatment = None
    server = None
    address = '127.0.0.1'
    port = 8888

    def start(self):
        super(SocketInput, self).start()
        proto = self.protocol(self.name, self.treatment)
        coro = self.loop.create_server(lambda: proto,
                                       self.address, self.port)

        self.server = self.loop.run_until_complete(coro)

    def stop(self):
        self.server.wait_closed()


class FileHandler(FileSystemEventHandler):

    def __init__(self, filename, input_name, loop):
        self.filename = filename
        self.input_name = input_name
        self.loop = loop
        self.size = os.stat(filename).st_size

    def on_modified(self, event):
        filename = event.src_path

        if self.filename != filename:
            return

        task = asyncio.async(self.get_modifications(), loop=self.loop)
        task.add_done_callback(self.next_step)

    @asyncio.coroutine
    def get_modifications(self):
        with open(self.filename, 'r') as f:
            f.seek(self.size)
            modifications = f.readlines()
        self.size = os.stat(self.filename).st_size
        return {'data': modifications}

    def next_step(self, task):
        tasks.add_to_queue(self.input_name, task)


class FileInput(Input):
    dir = '/var/log'
    filename = ''
    obs = None

    def start(self):
        super(FileInput, self).start()
        self.obs = Observer()

        dir = Path(self.dir)
        filedir = dir / self.filename
        event_handler = FileHandler(str(filedir), self.name, self.loop)

        self.obs.schedule(event_handler, self.dir)
        self.obs.start()

    def stop(self):
        self.obs.stop()
        self.obs.join()