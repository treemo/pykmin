from asyncio import InvalidStateError
from core.managers import tasks, filters


class ModuleFilter(object):

    def __init__(self, name):
        self.name = name

    def start(self, task, prev):
        result = task.result()
        if not result:
            return

        data = result['data']
        result['data'] = self.filter(data)
        task._result = result

        tasks.add_to_queue(self.name, task, prev)

    def filter(self, data):
        return data + b'a'

filters.register('test_filter', ModuleFilter)