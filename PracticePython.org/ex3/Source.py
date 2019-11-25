a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
num=int(input("Give me a number to return elements smaller than that number:"))
for x in a:
    if (x<num):
        b.append(x)

print(b)