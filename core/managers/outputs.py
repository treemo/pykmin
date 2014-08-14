from collections import OrderedDict

__all__ = ('register',)

_REGISTRY = OrderedDict()
_QUEUE = []

def register(name, object):
    _REGISTRY[name] = object

def get_element(name):
    return _REGISTRY.get(name)

def finished():
    return _QUEUE

def add_to_queue(name, task):
    _QUEUE.append((name, task))

def remove_from_queue(name, task):
    _QUEUE.remove((name, task))