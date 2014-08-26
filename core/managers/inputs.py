from collections import OrderedDict

__all__ = ('register',)

_REGISTRY = OrderedDict()


def register(name, object):
    _REGISTRY[name] = object(name)


def get_element(name):
    return _REGISTRY.get(name)


def get_all_elements():
    return _REGISTRY.keys()