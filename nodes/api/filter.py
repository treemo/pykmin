from core.managers import filters, tasks, inputs


class OrderHandler(object):

    def __init__(self, name):
        self.name = name

    def start(self, task, prev):
        result = task.result()
        data = result['data']
        result['data'] = self.filter(data)
        task._result = result

        tasks.add_to_queue(self.name, task, prev)

    def filter(self, data):
        data = data.decode('utf-8')
        if data.startswith('stop'):
            module = data.rstrip().split(maxsplit=1)[-1]
            module_instance = inputs.get_element(module)
            module_instance.stop()
            return b'Module sucessfully stopped'
        return b'Error ...'

filters.register('pykmin_api_filter', OrderHandler)