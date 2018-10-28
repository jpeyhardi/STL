from . import _stl
from . import __stl

from functools import wraps
import sys

__all__ = []

__module__ = sys.modules[__name__]
for var in dir(__stl.statiskit.stl):
    if var.startswith('Set'):
        setattr(__module__, var, getattr(__stl.statiskit.stl, var))
        __all__.append(var)

def decoration(cls):

    def wrapper__init__(f):
        @wraps(f)
        def __init__(self, arg=None):
            if arg is None:
                f(self)
            elif not isinstance(arg, self.__class__):
                raise TypeError('\'arg\' parameter must be a \'' + self.__class__ + '\' instance')
            else:
                f(self, arg)
        return __init__

    cls.__init__ = wrapper__init__(cls.__init__)

    # def __eq__(self, other):
    # if isinstance(other, self.__class__):
    #     return all(self[index] == other[index] for index in range(len(self)))
    # else:
    #     return False

    # cls.__eq__ = __eq__
    # del __eq__

    def __str__(self):
        return "{" + ", ".join(str(value) for value in self) + "}"

    cls.__str__ = __str__

    def __repr__(self):
        return "{" + ", ".join(repr(value) for value in self) + "}"

    cls.__repr__ = __repr__

    def _repr_latex_(self):
        return "$\\left\\{" + ", ".join(getattr(value, "_repr_latex_", getattr(value, "__repr__"))() for value in self) + "\\right\\}$"

    cls._repr_latex_ = _repr_latex_

for cls in __stl.std._Set:
    decoration(cls)