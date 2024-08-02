telefonbuch = {}

telefonbuch["tarik"] = 176
telefonbuch["far"] = 190
telefonbuch["mart"] = 154
telefonbuch["rar"] = 134

print(telefonbuch)

for name, nummer in telefonbuch.items():
    print(name, nummer)

for name in telefonbuch.items():
    print(name)

for name in telefonbuch:
    print(name)

telefonbuch = {
    "meh" : 231432,
    "joh" :23742347
}
print(telefonbuch)

del telefonbuch["meh"]
telefonbuch.pop("joh")
print(telefonbuch)