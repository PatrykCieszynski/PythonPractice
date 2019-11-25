import random

def GenerateList(listname):
    for x in range(0,random.randint(5, 21)):
        listname.append(random.randint(0,30))

    listname.sort()


a = []
b = []
ab = []

GenerateList(a)
GenerateList(b)

print(a)
print(b)

for x in a:
    if(x in b and x not in ab):
        ab.append(x)

print(ab)