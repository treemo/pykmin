from core.nodes.outputs import OutputFile
from core.managers import outputs


class ToFile(OutputFile):
    file = 'f2b.log'

    def write(self, data):
        return '%s is banned!' % data

outputs.register('f2b_output', ToFile)