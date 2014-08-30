from core.nodes.inputs import FileInput
from core.managers import inputs


class ModuleInput(FileInput):
    filename = 'i3.log'

inputs.register('test_input2', ModuleInput)