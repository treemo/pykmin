from collections import OrderedDict

__all__ = ('register',)

_REGISTRY = OrderedDict()
_INPUTS = set()

def register(name):
    def inner(orig_class):
        _REGISTRY[name] = orig_class(name)
        return orig_class
    return inner


def get_element(name):
    return _REGISTRY.get(name)


def get_all_elements():
    return _REGISTRY.keys()


def add_input(name):
    _INPUTS.add(name)

def get_inputs():
    return _INPUTS