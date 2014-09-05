from core.managers import filters
from core.helpers.filters import BaseFilter


@filters.register('test_filter')
class ModuleFilter(BaseFilter):

    def filter(self, data):
        return '%sa' % data

