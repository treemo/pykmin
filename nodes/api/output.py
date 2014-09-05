from core.helpers.outputs import OutputSocket
from core.managers import outputs


@outputs.register('pykmin_api_output')
class ToSocket(OutputSocket):

    def data_send(self, data=None):
        super(ToSocket, self).data_send(self.data)

