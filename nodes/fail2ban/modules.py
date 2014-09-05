from core.helpers.filters import BaseFilter
from core.helpers.inputs import FileInput
from core.helpers.outputs import OutputFile
from core.managers import modules


@modules.register('f2b_input')
class ModuleInput(FileInput):
    filename = 'fail2ban.log'


@modules.register('f2b_filter')
class ModuleFilter(BaseFilter):

    def filter(self, data):
        if 'Ban' in data:
            return [data.split()[-1], 'ban']
        elif 'Unban' in data:
            return [data.split()[-1], 'unban']
        return None


@modules.register('f2b_output')
class ToFile(OutputFile):
    file = 'f2b.log'

    def write(self, data):
        ip, state = data
        return '%s is %sned!' % (ip, state)

