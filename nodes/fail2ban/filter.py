from core.managers import filters
from core.nodes.filters import BaseFilter


class ModuleFilter(BaseFilter):

    def filter(self, data):
        if 'Ban' in data:
            return data.split()[-1]
        return None

filters.register('f2b_filter', ModuleFilter)