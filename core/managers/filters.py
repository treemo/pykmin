from collections import OrderedDict

__all__ = ('register',)

_REGISTRY = OrderedDict()


def register(name):
    def inner(orig_class):
        _REGISTRY[name] = orig_class(name)
        return orig_class
    return inner


def get_element(name):
    return _REGISTRY.get(name)
