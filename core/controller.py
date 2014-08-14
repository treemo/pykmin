import asyncio
import yaml
import logging.config
from core.managers import inputs, outputs, nodes

class Controller(object):
    def __init__(self):
        self._init_mapping()
        self._init_logger()
        self.loop = asyncio.get_event_loop()

    def _init_logger(self):
        with open('configs/logger.conf') as file:
            config = yaml.load(file)
            logging.config.dictConfig(config)


    def _init_mapping(self):
        with open('configs/mapping.conf') as f:
            self.mapping = yaml.load(f)

    def _import_nodes(self, submodule_name):
        for module in nodes._REGISTRY:
            try:
                input_path = 'nodes.%s.%s' % (module, submodule_name)
                __import__(input_path)
            except ImportError:
                pass

    def autodiscover_inputs(self):
        self._import_nodes('input')

        for name in inputs._REGISTRY:
            if name in self.mapping:
                inputs._REGISTRY[name].start()

    def autodiscover_outputs(self):
        self._import_nodes('output')

    @asyncio.coroutine
    def handle_finished_tasks(self):
        while True:
            for input, task in inputs.finished():
                next_step = self.mapping.get(input)
                if next_step:
                    outputs.get_element(next_step).start(task)
                inputs.remove_from_queue(input, task)
            yield from asyncio.sleep(0.5)

    def start(self):
        asyncio.async(self.handle_finished_tasks(), loop=self.loop)
        self.loop.run_forever()
