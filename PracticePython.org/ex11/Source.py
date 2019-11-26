def get_integer(text="Give me a number: "):
    return int(input(text))


def is_prime(a):
    for x in range(2, num):
        if a % x == 0:
            return 0
    return 1


num = get_integer("Give me a number to check if it is prime: ")

if is_prime(num) == 1:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
