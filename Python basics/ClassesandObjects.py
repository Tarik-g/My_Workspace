class Hund:

    # alter = 5
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def bellen(self):
        print("%s bellt Wuff" % self.name)
    
    def getalter(self):
        return self.alter

Bello = Hund("Bello", 5)

if Bello.alter == 5:
    print("yess")

Celo = Hund("Celo", 4)

Bello.alter = 3

print(Bello.alter)
print(Celo.alter)

Bello.bellen()

print(Bello.getalter())