from core.nodes.outputs import OutputFile
from core.managers import outputs


class ToFile(OutputFile):
    file = 'test.log'

outputs.register('test_output', ToFile)