#!/usr/bin/python3
import importlib.util
import sys
def get_module_names(module_path):
    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = [name for name in dir(module) if not name.startswith('__')]
    return sorted(names)
if __name__ == "__main__":
    module_path = '/tmp/hidden_4.pyc'
    names = get_module_names(module_path)
    for name in names:
        print(name)
