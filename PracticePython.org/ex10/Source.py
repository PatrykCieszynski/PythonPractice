import random


a = random.sample(range(0, 50), random.randint(5, 20))
b = random.sample(range(0, 50), random.randint(5, 20))
a.sort()
b.sort()
print(a)
print(b)
print([x for x in a if x in b])