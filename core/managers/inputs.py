from collections import OrderedDict

__all__ = ('register',)

_REGISTRY = OrderedDict()
_QUEUE = []

def register(name, object):
    _REGISTRY[name] = object

def finished():
    return _QUEUE

def add_to_queue(name):
    _QUEUE.append(name)