class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def bellen(self):
        print("%s bellt Wuff" % self.name)
    
    def getalter(self):
        return self.alter


bello = Hund("Bello", 5)
celo = Hund("Celo", 4)
if bello.alter == 5:
    print("yess")

bello.alter = 3
print(bello.alter)
print(celo.alter)
print(bello.getalter())

bello.bellen()