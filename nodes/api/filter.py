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
        order = data.rstrip().split(maxsplit=1)
        if order[0] == 'stop':
            module = order[1]
            module_instance = inputs.get_element(module)
            module_instance.stop()
            return b'Module sucessfully stopped'

        if order[0] == 'start':
            module = order[1]
            module_instance = inputs.get_element(module)
            module_instance.start()
            return b'Module sucessfully started'

        if order[0] == 'list':
            ret = []
            for element in inputs.get_all_elements():
                ret.append("- %s" % element)
            return '\n'.join(ret).encode('utf-8')

        return b'Error ...'

filters.register('pykmin_api_filter', OrderHandler)