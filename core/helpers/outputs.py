import logging

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

        with open(self.file, 'a') as f:
            if isinstance(self.data, list):
                for data in self.data:
                    line = self.write(data)
                    f.write(line+'\n')
            else:
                line = self.write(self.data)
                f.write(line+'\n')

    def write(self, data):
        return data


class OutputSocket(Output):
    transport = None

    def start(self, task, prev):
        super(OutputSocket, self).start(task)
        self.transport = task.result()['transport']
        self.data_send()

    def data_send(self, data=None):
        if data is None:
            return

        self.transport.write(data.encode())
        self.transport.close()


class OutputLogger(Output):

    def __init__(self, name):
        super(OutputLogger, self).__init__(name)
        self.logger = logging.getLogger(self.__class__.__name__)

    def start(self, task):
        super(OutputLogger, self).start(task)

        msg = self.write(self.data)
        self.logger.critical(msg)

    def write(self, data):
        return data
