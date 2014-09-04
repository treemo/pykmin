class Output(object):
    data = ''

    def __init__(self, name):
        self.name = name

    def start(self, task):
        self.data = task.result()['data']


class OutputFile(Output):
    file = ''

    def start(self, task):
        super(OutputFile, self).start(task)

        if not self.file:
            raise AttributeError('You need to set file attribute')

        # TODO: Vérifier que le chemin existe avant d'ouvrir le fichier

        with open(self.file, 'wb') as f:
            f.write(self.data)


class OutputSocket(Output):
    transport = None

    def start(self, task):
        super(OutputSocket, self).start(task)
        self.transport = task.result()['transport']
        self.data_send()

    def data_send(self, data=None):
        if data is None:
            return

        self.transport.write(data)
        self.transport.close()