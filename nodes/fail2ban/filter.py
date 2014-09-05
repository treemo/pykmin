from core.managers import filters
from core.helpers.filters import BaseFilter


@filters.register('f2b_filter')
class ModuleFilter(BaseFilter):

    def filter(self, data):
        if 'Ban' in data:
            return [data.split()[-1], 'ban']
        elif 'Unban' in data:
            return [data.split()[-1], 'unban']
        return None

