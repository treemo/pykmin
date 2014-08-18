from collections import OrderedDict

__all__ = ('register',)

_REGISTRY = OrderedDict()


def register(name, object):
    _REGISTRY[name] = object


def get_element(name):
    return _REGISTRY.get(name)
