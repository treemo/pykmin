from core.managers import filters
from core.helpers.filters import BaseFilter


class ModuleFilter(BaseFilter):

    def filter(self, data):
        if 'Ban' in data:
            return [data.split()[-1], 'ban']
        elif 'Unban' in data:
            return [data.split()[-1], 'unban']
        return None

filters.register('f2b_filter', ModuleFilter)