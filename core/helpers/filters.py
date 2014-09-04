from core.managers import tasks


class BaseFilter(object):

    def __init__(self, name):
        self.name = name

    def start(self, task, prev):

        result = task.result()
        if not result or 'data' not in result:
            return

        data = result['data']

        if isinstance(data, list):
            result['data'] = []
            for line in data:
                filtered = self.filter(line)
                if filtered:
                    result['data'].append(filtered)
        else:
            result['data'] = self.filter(data)

        task._result = result

        tasks.add_to_queue(self.name, task, prev)

    def filter(self, data):
        raise NotImplemented('You have to add filter to your node')