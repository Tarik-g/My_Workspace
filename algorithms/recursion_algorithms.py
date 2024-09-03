def factorial_recursive(zahl):
    if zahl == 1:
        return 1
    return factorial_recursive(zahl - 1) * zahl

print(factorial_recursive(4))


def factorial_iterative(zahl):
    res = 1
    for i in range(zahl):
        res = res * (i+1)
    return res

print(factorial_iterative(4))