
import os
import inspect
from importlib import import_module
from PyQt5 import QtWidgets


# the final dict for storing classes by classname
widgets = {}


# find python files in this directory
for f in os.listdir(os.path.dirname(__file__)):
    name, ext = os.path.splitext(f)

    if ext != '.py':
        continue

    if name == '__init__':
        continue

    # import the module
    module = import_module('.{}'.format(name), package=__name__)

    # search each modules dict for classes that implement QWidget
    for key in module.__dict__:
        e = module.__dict__[key]

        if not inspect.isclass(e):
            continue

        if issubclass(e, QtWidgets.QWidget):
            widgets[key] = e
