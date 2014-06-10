import os

_REGISTRY = []

def load_modules():
    global _REGISTRY
    _REGISTRY = [module for module in os.listdir('nodes')
            if os.path.isdir(os.path.join('nodes', module))
            and module != '__pycache__']

load_modules()