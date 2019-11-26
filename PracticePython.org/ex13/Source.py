def fibonacci(a):
    if a == 0 or a == 1:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)


a = int(input("How many fibonacci numbers to generate: "))
print([fibonacci(i) for i in range(a)])
