import Functions
from Functions import summe
from Functions import summe as addieren

#alles importieren mit namespace
from Functions import *

print(Functions.summe(3,4))
print(summe(3,4))
print(addieren(3,4))

import expPackage.expimport
print(expPackage.expimport.substract(10, 5))

from expPackage import expimport
print(expimport.substract(15, 5))

#import sys
#print(sys.path)

#dir(Functions)
#help

#sys.path.append('/path/to/your/modules')
#sys.path.append('/another/path')