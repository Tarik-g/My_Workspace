import random

def drei_zufalls_Zahlen():
    for i in range(2):
        yield random.randint(1,100)
    
    yield random.randint(1,1000)

for zufalls_zahl in drei_zufalls_Zahlen():
    print("Und die nächste zahl %d" % zufalls_zahl)

def fib():
    a,b = 1,1
    while 1:
        yield a
        a,b = b, a+b

import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break