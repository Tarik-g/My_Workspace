from PythonBasics import examplepackage
import functions
from functions import summe
from functions import summe as addieren

#alles importieren mit namespace
from functions import *

print(functions.summe(3,4))
print(summe(3,4))
print(addieren(3,4))

#import PythonBasics.examplepackage.expample_import1
print(examplepackage.expample_import1.substract(10, 5))

from PythonBasics.examplepackage import expample_import1
print(expample_import1.substract(15, 5))

#import sys
#print(sys.path)

#dir(functions)
#help

#sys.path.append('/path/to/your/modules')
#sys.path.append('/another/path')