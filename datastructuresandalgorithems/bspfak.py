def fak(zahl):
    if zahl == 1:
        return 1
    return fak(zahl - 1) * zahl

ergebnis = fak(4)

print(ergebnis)


def fakt(zahl):
    res = 1
    for i in range(zahl):
        res = res * (i+1)
    return res

ergebnis = fakt(4)

print(ergebnis)