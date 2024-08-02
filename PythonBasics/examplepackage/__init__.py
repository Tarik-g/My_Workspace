from .expample_import1 import substract
from .example_import2 import function2

__all__ = [ 'substract', 'function2']

# Only expose function1 and function2
# _example_import3 is not included in __all__, so it remains internal