class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def bellen(self):
        print("%s bellt Wuff" % self.name)
    
    def getalter(self):
        return self.alter


Bello = Hund("Bello", 5)
Celo = Hund("Celo", 4)
if Bello.alter == 5:
    print("yess")

Bello.alter = 3
print(Bello.alter)
print(Celo.alter)
print(Bello.getalter())

Bello.bellen()