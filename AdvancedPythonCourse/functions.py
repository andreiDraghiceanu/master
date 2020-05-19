import legb
from legb import func as legb_func

from pypackage.pymodule import GLOBAL_VAR, pym_function
from pypackage import pymodule
from pypackage import GLOBAL_VAR, pym_function


def func(a, b=0):
    """Docstring for function - inline documentation"""
    return a + b


res1 = func(10)
res2 = func(10, 20)


legb.func('blabla')
legb_func('aaaaa')

print(GLOBAL_VAR, pym_function(10, 5))
print(pymodule.GLOBAL_VAR, pymodule.pym_function(10, 5))
