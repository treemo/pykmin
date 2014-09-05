from core.managers import filters, inputs
from core.helpers.filters import BaseFilter


@filters.register('pykmin_api_filter')
class OrderHandler(BaseFilter):

    def filter(self, data):
        order = data.split(maxsplit=1)
        if order[0] == 'stop':
            module = order[1]
            module_instance = inputs.get_element(module)
            module_instance.stop()
            return 'Module sucessfully stopped'

        if order[0] == 'start':
            module = order[1]
            module_instance = inputs.get_element(module)
            module_instance.start()
            return 'Module sucessfully started'

        if order[0] == 'list':
            ret = []
            for element in inputs.get_all_elements():
                ret.append("- %s" % element)
            return '\n'.join(ret)

        return 'Error ...'
