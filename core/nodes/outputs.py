class Output(object):
    def __init__(self, name):
        self.name = name

    def start(self, task):
        pass


class OutputFile(Output):
    file = ''

    def start(self, task):
        if not self.file:
            raise AttributeError('You need to set file attribute')

        # TODO: Vérifier que le chemin existe avant d'ouvrir le fichier


        with open(self.file, 'wb') as f:
            f.write(task.result()['data'])


class OutputSocket(Output):
    transport = None
    data = ''

    def start(self, task):
        self.transport = task.result()['transport']
        self.data = task.result()['data']
        self.data_send()

    def data_send(self, data=None):
        if data is None:
            return

        self.transport.write(data)
        self.transport.close()