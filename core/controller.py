import asyncio
import yaml
import logging.config
from core.managers import inputs, outputs, nodes, filters, tasks
from functools import reduce


def getFromDict(data_dict, key_list):
    return reduce(lambda d, k: d[k], key_list, data_dict)


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

    def autodiscover_filters(self):
        self._import_nodes('filter')

    def autodiscover_outputs(self):
        self._import_nodes('output')

    @asyncio.coroutine
    def handle_finished_tasks(self):
        while True:
            for name, t_object, prev in tasks.finished():
                if not prev:
                    path = [name]
                else:
                    path = prev + [name]
                next_steps = getFromDict(self.mapping, path)

                if isinstance(next_steps, dict):
                    next_steps = next_steps.keys()
                else:
                    next_steps = next_steps.split()

                for next_step in next_steps:
                    if next_step and 'output' in next_step:
                        outputs.get_element(next_step).start(t_object)
                    elif next_step and 'filter' in next_step:
                        filters.get_element(next_step).start(t_object, path)
                tasks.remove_from_queue(name, t_object, prev)
            yield from asyncio.sleep(0.0000000005)

    def start(self):
        asyncio.async(self.handle_finished_tasks(), loop=self.loop)
        self.loop.run_forever()
