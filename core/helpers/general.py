import asyncio


class ThreadedMixin(object):

    def start(self, *args):
        asyncio.Task(self.thread(*args))

    def thread(self, *args):
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None,
                                      super(ThreadedMixin, self).start,
                                      *args)
        yield from future
