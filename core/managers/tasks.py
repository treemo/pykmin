_QUEUE = []


def finished():
    return _QUEUE


def add_to_queue(name, task, previous=None):
    _QUEUE.append((name, task, previous))


def remove_from_queue(name, task, prev):
    _QUEUE.remove((name, task, prev))