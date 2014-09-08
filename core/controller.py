import asyncio
import functools
import signal
import yaml
import logging.config
from core.managers import nodes, modules, tasks
from functools import reduce


def getFromDict(data_dict, key_list):
    return reduce(lambda d, k: d[k], key_list, data_dict)


class Controller(object):
    def __init__(self):
        self._init_mapping()
        self._init_logger()
        self.loop = asyncio.get_event_loop()
        self.logger = logging.getLogger(self.__class__.__name__)

    def _init_logger(self):
        with open('configs/logger.conf') as file:
            config = yaml.load(file)
            logging.config.dictConfig(config)

    def _init_mapping(self):
        with open('configs/mapping.conf') as f:
            self.mapping = yaml.load(f)

    def _import_nodes(self, module_name):
        for node in nodes._REGISTRY:
            try:
                input_path = 'nodes.%s.%s' % (node, module_name)
                __import__(input_path)
            except ImportError as e:
                self.logger.error(e)

    def autodiscover_modules(self):
        self._import_nodes('modules')
        for name in modules._REGISTRY:
            if name in self.mapping:
                modules.add_input(name)
                modules._REGISTRY[name].start()

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
                    modules.get_element(next_step).start(t_object, path)
                tasks.remove_from_queue(name, t_object, prev)
            yield from asyncio.sleep(0.5)

    def start(self):
        for signame in ('SIGINT', 'SIGTERM'):
            self.loop.add_signal_handler(getattr(signal, signame),
                                         functools.partial(self.stop, signame))
        asyncio.async(self.handle_finished_tasks(), loop=self.loop)
        self.loop.run_forever()

    def stop(self, signame):
        print("Pykmin exited with signal %s" % signame)
        self.loop.stop()