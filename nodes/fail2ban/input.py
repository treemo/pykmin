from core.helpers.inputs import FileInput
from core.managers import inputs


@inputs.register('f2b_input')
class ModuleInput(FileInput):
    filename = 'fail2ban.log'

