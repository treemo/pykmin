from core.helpers.outputs import OutputFile
from core.managers import outputs


@outputs.register('f2b_output')
class ToFile(OutputFile):
    file = 'f2b.log'

    def write(self, data):
        ip, state = data
        return '%s is %sned!' % (ip, state)

