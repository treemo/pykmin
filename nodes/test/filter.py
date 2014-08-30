from core.managers import tasks, filters
from core.nodes.filters import BaseFilter


class ModuleFilter(BaseFilter):

    def filter(self, data):
        return data + b'a'

filters.register('test_filter', ModuleFilter)