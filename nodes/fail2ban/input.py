from core.helpers.inputs import FileInput
from core.managers import inputs


class ModuleInput(FileInput):
    filename = 'fail2ban.log'

inputs.register('f2b_input', ModuleInput)