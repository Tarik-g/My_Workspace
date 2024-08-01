primzahlen = [ 2, 3, 5, 7, 11, 13, 17]

for primzahl in primzahlen:
    print(primzahl)

print("-------------------")
for x in range(3):
    print (x)
print("-------------------")
for x in range(3,6):
    print (x)
print("-------------------")
for x in range(3,10, 2):
    print (x)
print("-------------------")

zaehler = 0
while zaehler < 3:
    print(zaehler)
    zaehler += 1

print("-------------------")

zaehler = 0
while True:
    print(zaehler)
    zaehler += 1
    if zaehler > 3:
        break

print("-------------------")

zaehler = 0
while True:
    print(zaehler)
    zaehler += 1
    if zaehler > 3:
        break
print("-------------------")
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")