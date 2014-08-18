from core.managers import tasks, filters


class ModuleFilter(object):

    def start(self, task, prev):
        print('hello')
        tasks.add_to_queue('test_filter', task, prev)

filters.register('test_filter', ModuleFilter())