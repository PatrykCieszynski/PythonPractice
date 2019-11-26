def fibonacci(a):
    i=1
    if a == 0:
        fib = []
    elif a == 1:
        fib = [1]
    elif a == 2:
        fib = [1, 1]
    elif a > 2:
        fib = [1, 1]
        while i < (a-1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

a = int(input("How many fibonacci numbers to generate: "))

print(fibonacci(a))
