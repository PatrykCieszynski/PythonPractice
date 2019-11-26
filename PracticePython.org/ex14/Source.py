import random

def GenerateList(listname):
    for x in range(0, random.randint(5, 21)):
        listname.append(random.randint(0, 10))
    listname.sort()


def RemoveDuplicatsSets(listname):
    b = []
    b = list(set(a))
    return b


def RemoveDuplicatsLoop(listname):
    c = []
    for x in a:
        if x not in c:
            c.append(x)
    return c


a = []
GenerateList(a)
print(a)
print(RemoveDuplicatsSets(a))
print(RemoveDuplicatsLoop(a))
