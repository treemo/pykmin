from core.managers import filters
from core.helpers.filters import BaseFilter


class ModuleFilter(BaseFilter):

    def filter(self, data):
        return '%sa' % data

filters.register('test_filter', ModuleFilter)